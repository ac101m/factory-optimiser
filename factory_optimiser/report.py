"""Down-conversion and reporting (Design.md §7).

Down-conversion: an activity x[r][k] is converted to a build plan as
    machines = ceil(activity)
    clock%   = activity / machines * 100
For slooped grades (k >= 1) the activity is integer by construction, so this
simply reports whole machines at 100% clock. Continuous k=0 activities become
underclocked whole machines (legal in-game). Overclocking beyond 100% is out of
scope (nonlinear in-game power curve; Design.md §1).
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from .io_config import Config, POWER_ITEM, sloop_multipliers
from .solve import Solution
from .sweep import AugResult

_EPS = 1e-9


@dataclass
class PlanMachine:
    recipe_id: str
    name: str
    machine: str
    sloops_per_machine: int
    machines: float        # to build (ceiled; may exceed 1 for underclock)
    clock_pct: float       # 0..~100
    activity: float        # raw solver value (machine-equivalents)
    outputs: dict[str, float]  # total throughput items/min
    inputs: dict[str, float]


def downconvert(config: Config, solution: Solution) -> list[PlanMachine]:
    plan: list[PlanMachine] = []
    for (r, k), activity in sorted(solution.activities.items()):
        if activity <= _EPS:
            continue
        recipe = config.recipes[r]
        machines = math.ceil(activity - 1e-9)
        clock = activity / machines * 100.0
        grade = sloop_multipliers(k, config.max_sloops_for(recipe.machine))
        outputs = {
            i: grade.rho * v * activity
            for i, v in recipe.outputs.items()
            if i != POWER_ITEM and grade.rho * v * activity > _EPS
        }
        inputs = {i: grade.kappa * v * activity for i, v in recipe.inputs.items()}
        plan.append(
            PlanMachine(
                recipe_id=recipe.id,
                name=recipe.name or recipe.id,
                machine=recipe.machine,
                sloops_per_machine=k,
                machines=float(machines),
                clock_pct=clock,
                activity=activity,
                outputs=outputs,
                inputs=inputs,
            )
        )
    return plan


def total_points(config: Config, solution: Solution) -> float:
    pts = sum(
        config.items[i].points * rate
        for i, rate in solution.sinks.items()
    )
    pts += sum(
        config.items[i].points * rate
        for i, rate in solution.raw_sinks.items()
    )
    return pts


def optimize_text(config: Config, best: AugResult, curve: list[AugResult]) -> str:
    lines: list[str] = []

    lines.append("=== Satisfactory sink-point factory optimizer ===")
    lines.append(
        f"Map resources: "
        + ", ".join(f"{k} {v:g}/min" for k, v in config.parameters.resources.items())
    )
    lines.append(f"Somersloop budget: {config.parameters.somersloop_budget:g}")
    lines.append("")

    # Augmenter sweep curve (Design.md §6): +10% of base generation per
    # augmenter (additive) AND +500 MW flat each (the bonus doesn't apply to it).
    lines.append("Alien Power Augmenter sweep (10 sloops each, +10% base, +500 MW flat):")
    lines.append("  N | sloops left | power x |  flat MW |   pts/min     vs N-1")
    prev = None
    for res in curve:
        delta = ""
        if prev is not None:
            delta = f"{res.points_per_min - prev:+12,.1f}"
        lines.append(
            f"  {res.n_augmenters} | {res.sloop_budget:>11.0f} | {res.power_multiplier:>7.2f} | "
            f"{res.flat_power_mw:>8,.0f} | {res.points_per_min:>10,.1f}  {delta}"
        )
        prev = res.points_per_min
    lines.append(f"Best: N={best.n_augmenters}  {best.points_per_min:,.1f} pts/min")
    lines.append("")

    lines.append(
        f"OPTIMAL BUILD PLAN  (N={best.n_augmenters}, {best.power_multiplier:.2f}x power)"
    )
    plan = downconvert(config, best.solution)
    header = f"  {'recipe (machine)':44s} {'slp':>3s} {'mach':>5s} {'clk%':>6s}  outputs/min"
    lines.append("-" * len(header))
    lines.append(header)
    if not plan:
        lines.append("  (no machines — nothing is profitable)")
    else:
        for m in plan:
            label = f"{m.name} ({m.machine})"
            if len(label) > 40:
                label = label[:40] + "…"
            main_out = "; ".join(
                f"{config.item_name(i, i)} {rate:.1f}" for i, rate in sorted(m.outputs.items())
            )
            lines.append(
                f"  {label:44s} {m.sloops_per_machine:>3d} {m.machines:>5.0f} "
                f"{m.clock_pct:>6.1f}  {main_out}"
            )
    lines.append("-" * len(header))

    sol = best.solution
    sloop_text = (
        f"Somersloops used: {sol.sloops_used:g} / {best.sloop_budget:g}"
        if best.sloop_budget > 0
        else "Somersloops used: 0 (all spent on augmenters)"
    )
    lines.append(f"{sloop_text}")

    if best.solution.problem.has_power:
        lines.append(
            f"Power: {sol.power_consumed:,.0f} / {sol.power_available:,.0f} MW consumed "
            f"(base {sol.power_generated:,.0f} MW x {best.power_multiplier:.2f} "
            f"bonus + {best.flat_power_mw:,.0f} MW from augmenters, un-bonused)"
        )

    # Sink summary.
    sink_rows: list[tuple[str, float, float, float]] = []
    for item, rate in sol.sinks.items():
        if rate <= _EPS:
            continue
        pts = config.items[item].points
        sink_rows.append((config.item_name(item), rate, pts, rate * pts))
    for item, rate in sol.raw_sinks.items():
        if rate <= _EPS:
            continue
        pts = config.items[item].points
        sink_rows.append((config.item_name(item), rate, pts, rate * pts))
    if sink_rows:
        lines.append("")
        lines.append("Sink flows:")
        for name, rate, pts, value in sorted(sink_rows, key=lambda t: -t[3]):
            lines.append(
                f"  {name:32s} {rate:9,.1f}/min x {pts:7.1f} pts = {value:10,.1f} pts/min"
            )
        total = sum(t[3] for t in sink_rows)
        lines.append("-" * 72)
        lines.append(f"  {'TOTAL':32s} {'':>9s} {'':>7s} = {total:10,.1f} pts/min")

    return "\n".join(lines)


def augmenter_curve_text(results: list[AugResult], title: str) -> str:
    lines = [f"=== {title} ==="]
    lines.append(
        f"  N | power x |  flat MW |    pts/min    | marginal pts/augmenter vs N-1"
    )
    prev = None
    for res in results:
        delta = "" if prev is None else f"{res.points_per_min - prev:+12,.1f}"
        lines.append(
            f"  {res.n_augmenters} | {res.power_multiplier:>7.2f} | {res.flat_power_mw:>8,.0f} | "
            f"{res.points_per_min:>12,.1f} | {delta}"
        )
        prev = res.points_per_min
    return "\n".join(lines)


def marginal_text(header: str, rows: list[tuple[float, float]], value_name: str) -> str:
    """rows: (label, points/min). Prints a marginal delta per unit of label."""
    lines = [f"=== {header} ==="]
    lines.append(f"  {value_name:28s} {'pts/min':>12s} {'marginal /unit':>16s}")
    prev_value = None
    prev_pts = None
    for label, points in rows:
        delta = ""
        if prev_value is not None:
            delta = f"{(points - prev_pts) / (label - prev_value):+14.1f}"
        lines.append(f"  {label:>28.2f} {points:>12,.1f} {delta}")
        prev_value = label
        prev_pts = points
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# JSON
# ---------------------------------------------------------------------------


def optimize_json(config: Config, best: AugResult, curve: list[AugResult]) -> dict:
    plan = downconvert(config, best.solution)
    sol = best.solution
    return {
        "recipe_files": str(config.recipes_dir),
        "items": [config.items[i].name or i for i in config.produced_items],
        "best": {
            "n_augmenters": best.n_augmenters,
            "power_multiplier": best.power_multiplier,
            "flat_power_mw": round(best.flat_power_mw, 2),
            "sloops_used": sol.sloops_used,
            "sloops_budget_in_model": best.sloop_budget,
            "power_consumed_mw": round(sol.power_consumed, 2),
            "power_available_mw": round(sol.power_available, 2),
            "solve_seconds": round(sol.solve_seconds, 4),
            "plan": [
                {
                    "recipe": m.recipe_id,
                    "name": m.name,
                    "machine": m.machine,
                    "sloops_per_machine": m.sloops_per_machine,
                    "machines": m.machines,
                    "clock_percent": round(m.clock_pct, 2),
                    "activity": round(m.activity, 4),
                    "outputs": {k: round(v, 4) for k, v in m.outputs.items()},
                }
                for m in plan
            ],
            "sinks": {
                i: {
                    "rate_per_min": round(sol.sinks[i], 4),
                    "points_per_unit": config.items[i].points,
                    "points_per_min": round(sol.sinks[i] * config.items[i].points, 4),
                }
                for i in sol.sinks
                if sol.sinks[i] > _EPS
            },
            "raw_sinks": {
                i: {
                    "rate_per_min": round(sol.raw_sinks[i], 4),
                    "points_per_unit": config.items[i].points,
                    "points_per_min": round(sol.raw_sinks[i] * config.items[i].points, 4),
                }
                for i in sol.raw_sinks
                if sol.raw_sinks[i] > _EPS
            },
        },
        "augmenter_curve": [
            {
                "n_augmenters": r.n_augmenters,
                "sloops_left": r.sloop_budget,
                "power_multiplier": r.power_multiplier,
                "flat_power_mw": round(r.flat_power_mw, 2),
                "points_per_min": round(r.points_per_min, 4),
            }
            for r in curve
        ],
    }
