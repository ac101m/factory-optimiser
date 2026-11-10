"""Command-line interface (docopt) for the factory optimizer.

Commands:

    check                   audit the data model for consistency (no solve)
    optimize                best build plan (includes the augmenter sweep)
    sweep augmenters        points/min per augmenter count (marginal curve)
    sweep somersloops       points/min per total Somersloop budget
    sweep resources         points/min per unit of each map resource (marginal)

The consistency audit also runs before every other command; errors stop the
command (non-zero exit), warnings print to stderr and never block.
"""

from __future__ import annotations

import json
import sys
import warnings
from dataclasses import replace

# docopt 0.6.2 contains invalid escape sequences in its own source; under
# Python 3.12+ this emits SyntaxWarnings on every import. Silence only those.
warnings.filterwarnings("ignore", category=SyntaxWarning, module=r"docopt")

from docopt import DocoptExit, docopt  # noqa: E402

from . import __version__
from .consistency import audit_text, check_config, has_errors, has_warnings
from .io_config import ConfigError, load_config
from .report import (
    augmenter_curve_text,
    marginal_text,
    optimize_json,
    optimize_text,
)
from .solve import SolveError, solve
from .sweep import (
    AugResult,
    sweep_augmenters,
    sweep_extractor_nodes,
    sweep_somersloops,
)

USAGE = """\
Satisfactory sink-point factory optimizer (MILP).

Usage:
  factory_optimiser check [options] [--strict]
  factory_optimiser optimize [options]
  factory_optimiser sweep (augmenters | somersloops | resources) [options]
  factory_optimiser --version
  factory_optimiser --help

Commands:
  check                   Audit the data model for consistency (no solve; also
                          runs before every other command).
  optimize                Solve the optimal build plan (augmenter sweep included).
  sweep augmenters        Marginal-value curve: points/min per augmenter count.
  sweep somersloops       Marginal-value curve: points/min per Somersloop budget.
  sweep resources         Marginal-value curve: pts/min per extra extractor node on each raw material.

Options:
  -r DIR, --recipes DIR     Directory of recipe JSON files        [default: recipes]
  -m DIR, --machines DIR    Directory of machine-spec JSON files  [default: machines]
  -t DIR, --items DIR       Directory of item JSON files          [default: items]
  -p FILE, --parameters FILE
                            Parameters JSON                      [default: config/parameters.json]
  --max-augmenters N        Cap augmenter count (default: floor(Somersloop budget / cost))
  --no-augmenters           Force N=0 (no Alien Power Augmenters)
  --strict                  Treat audit warnings as failures too (check only).
  -j, --json                Emit machine-readable JSON instead of a table.
  -h, --help                Show this message.
  --version                 Show version.
"""


def main(argv: list[str] | None = None) -> int:
    try:
        args = docopt(USAGE, argv=argv, version=f"factory-optimiser {__version__}")
    except DocoptExit as exc:
        print(exc, file=sys.stderr)
        return 2

    try:
        config = load_config(
            args["--recipes"], args["--machines"], args["--items"], args["--parameters"]
        )
    except ConfigError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    # Consistency audit runs before anything else.
    issues = check_config(config)
    audit = audit_text(config, issues)

    if args["check"]:
        print(audit)
        if has_errors(issues) or (args["--strict"] and has_warnings(issues)):
            return 1
        return 0

    if issues:
        print(audit, file=sys.stderr)
        if has_errors(issues):
            return 1

    try:
        if args["optimize"]:
            return _cmd_optimize(args, config)
        return _cmd_sweep(args, config)
    except SolveError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except ConfigError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


def _cmd_optimize(args, config) -> int:
    max_n = _max_augmenters_arg(args)
    curve = sweep_augmenters(config, max_n)
    best = _pick_best(curve)
    # Machine-count tiebreak (Design.md §10): the phase-1 objective prices
    # output but nothing prices building count, so a plan with "more machines
    # at a lower clock" (e.g. 60 Screw constructs at 50% vs 30 at 100%, same
    # output, power slack) is equally optimal. Re-solve the best N's problem
    # lexicographically — same points/min, FEWEST machines — so the reported
    # plan is the smallest build that still hits the optimum (and still
    # underclocks wherever power genuinely binds). Points/min are unchanged.
    best = replace(best, solution=solve(best.solution.problem, minimize_machines=best.points_per_min))
    if args["--json"]:
        _dump_json(optimize_json(config, best, curve))
    else:
        print(optimize_text(config, best, curve))
    return 0


def _pick_best(results: list[AugResult]) -> AugResult:
    """Best augmenter count; ties resolve toward fewer augmenters."""
    best = None
    for result in results:
        if best is None or result.points_per_min > best.points_per_min + 1e-6:
            best = result
    assert best is not None
    return best


def _cmd_sweep(args, config) -> int:
    if args["augmenters"]:
        results = sweep_augmenters(config, _max_augmenters_arg(args))
        if args["--json"]:
            _dump_json(
                {
                    "dimension": "augmenters",
                    "points": [
                        {
                            "n_augmenters": r.n_augmenters,
                            "power_multiplier": r.power_multiplier,
                            "flat_power_mw": round(r.flat_power_mw, 2),
                            "points_per_min": round(r.points_per_min, 4),
                        }
                        for r in results
                    ],
                }
            )
        else:
            print(augmenter_curve_text(results, "Augmenter marginal-value curve"))
        return 0

    if args["somersloops"]:
        budget = config.parameters.somersloop_budget
        budgets = _budget_steps(0.0, max(budget, 1.0), n=8)
        curve = sweep_somersloops(config, budgets)
        if args["--json"]:
            _dump_json(
                {
                    "dimension": "somersloops",
                    "points": [
                        {"total_somersloops": b, "points_per_min": round(p, 4)}
                        for b, p in curve
                    ],
                }
            )
        else:
            print(
                marginal_text(
                    "Somersloop marginal-value curve (augmenters re-optimised at each budget)",
                    curve,
                    "total somersloops",
                )
            )
        return 0

    # resources: in the miner-recipe model, the "map resource" lever is how
    # many extractor nodes (miner recipes) you can place. Report the marginal
    # value of one more node for each raw material.
    nodes = sweep_extractor_nodes(config)
    if args["--json"]:
        out: dict = {"dimension": "resources", "extractors": {}}
    lines = ["=== Extractor node marginal value (best N each point; +1 node each) ==="]
    lines.append(
        f"  {'node':30s} {'yields':>18s} {'caps':>5s} {'pts/min@base':>13s} {'pts/min@+1 node':>16s} {'marginal':>10s}"
    )
    for r, cap, base_pts, bumped in nodes:
        recipe = config.recipes[r]
        label = f"{recipe.name or recipe.id} [{recipe.machine}]"
        yields = ", ".join(f"{config.item_name(i, i)} {rate:g}/min" for i, rate in recipe.outputs.items())
        marginal = bumped - base_pts
        lines.append(
            f"  {label:30s} {yields:>18s} {cap:>5g} {base_pts:>13,.1f} {bumped:>16,.1f} {marginal:>+10,.1f}"
        )
        if args["--json"]:
            out["extractors"][recipe.id] = {
                "produces": {i: round(r2, 4) for i, r2 in recipe.outputs.items()},
                "base_nodes": cap,
                "points_at_base": round(base_pts, 4),
                "points_with_one_more_node": round(bumped, 4),
                "marginal_points_per_node": round(marginal, 4),
            }
    if not lines[2:] and not nodes:
        lines.append("  (no extractor recipes with max_machines caps found)")
    if args["--json"]:
        _dump_json(out)
    else:
        print("\n".join(lines))
    return 0


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


def _max_augmenters_arg(args) -> int | None:
    value = args.get("--max-augmenters")
    if value not in (None, "auto"):
        return max(0, int(value))
    return 0 if args.get("--no-augmenters") else None


def _budget_steps(start: float, end: float, n: int) -> list[float]:
    if n <= 1:
        return [start, end]
    return [start + (end - start) * i / (n - 1) for i in range(n)]


def _dump_json(obj) -> None:
    print(json.dumps(obj, indent=2, sort_keys=False))


if __name__ == "__main__":
    raise SystemExit(main())
