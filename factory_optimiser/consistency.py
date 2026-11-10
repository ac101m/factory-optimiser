"""Semantic consistency audit for a loaded :class:`Config`.

``load_config`` (io_config) performs *structural* validation — valid JSON,
required fields, unique ids — and raises :class:`ConfigError` on any violation.
This module performs the *semantic* audit: it inspects a fully-loaded Config
and reports issues (errors and warnings) that would otherwise surface only as
silently-wrong optima or confusing all-zero solves.

Severity levels:

* ``error``  — the data is inconsistent in a way that changes or breaks the
  results (e.g. a recipe on an unknown machine type, a missing item entry).
  The CLI refuses to proceed, exiting non-zero.
* ``warning`` — suspicious but possibly intentional (e.g. an unused machine
  spec, a produced item that can never leave the system). Reported, never
  blocks — except with ``check --strict``.

The audit is pure data inspection: it never solves a MILP.
"""

from __future__ import annotations

from dataclasses import dataclass

from .io_config import Config, DEFAULT_MACHINE, DEFAULT_MAX_SLOOPS, POWER_ITEM

SEVERITY_RANK = {"error": 0, "warning": 1, "info": 2}


@dataclass(frozen=True)
class Issue:
    """One finding of the consistency audit."""

    severity: str  # "error" | "warning" | "info"
    code: str      # short stable slug, e.g. "unknown-machine"
    message: str   # human-readable and actionable


def check_config(config: Config, include_info: bool = False) -> list[Issue]:
    """Audit a loaded config and return its issues, errors first.

    ``include_info`` toggles purely advisory findings (empty by default).
    """
    issues: list[Issue] = []
    params = config.parameters

    consumed = set(config.consumed_items)
    produced = set(config.produced_items)
    referenced = consumed | produced
    known_machines = set(config.machines)
    used_machines = {r.machine for r in config.recipes}
    capped = set(params.resources)

    # -- errors ---------------------------------------------------------------

    # Recipes on machine types with no spec: silently falls back to defaults,
    # which changes the optimum (0 MW, default sloop cap) without saying why.
    for r in config.recipes:
        if r.machine not in known_machines:
            issues.append(
                Issue(
                    "error",
                    "unknown-machine",
                    f"recipe {r.id!r} uses machine type {r.machine!r}, which has no "
                    f"spec in machines/ (falls back to {DEFAULT_MACHINE.power_draw:g} MW, "
                    f"{DEFAULT_MAX_SLOOPS} max sloops)",
                )
            )

    # Items referenced by recipes but missing from the items config: the loader
    # assumes sinkable with 0 points, silently tanking their sink value.
    for item_id in sorted(referenced - {POWER_ITEM} - set(config.items)):
        issues.append(
            Issue(
                "error",
                "missing-item",
                f"item {item_id!r} is referenced by recipes but has no entry in the "
                f"items config (assumed sinkable with 0 sink points)",
            )
        )

    # Non-positive rates or machine caps break conservation / are never usable.
    for r in config.recipes:
        for kind, rates in (("input", r.inputs), ("output", r.outputs)):
            for item_id, rate in rates.items():
                if rate <= 0:
                    issues.append(
                        Issue(
                            "error",
                            "nonpositive-rate",
                            f"recipe {r.id!r} has {kind} rate {rate:g} for item "
                            f"{item_id!r}; rates must be > 0",
                        )
                    )
        if r.max_machines is not None and r.max_machines <= 0:
            issues.append(
                Issue(
                    "error",
                    "nonpositive-cap",
                    f"recipe {r.id!r} has max_machines={r.max_machines:g}; it can "
                    "never run",
                )
            )

    for mid, spec in sorted(config.machines.items()):
        if spec.max_sloops < 0:
            issues.append(
                Issue(
                    "error",
                    "negative-sloop-cap",
                    f"machine {mid!r} has max_sloops={spec.max_sloops}; cannot be "
                    "negative",
                )
            )

    # -- warnings -------------------------------------------------------------

    for mid in sorted(known_machines - used_machines):
        issues.append(
            Issue(
                "warning",
                "unused-machine",
                f"machine spec {mid!r} is defined but no recipe uses it",
            )
        )

    for item_id in sorted(set(config.items) - referenced - {POWER_ITEM}):
        issues.append(
            Issue(
                "warning",
                "unused-item",
                f"item {item_id!r} is in the items config but no recipe produces or "
                "consumes it",
            )
        )

    # Consumed but nothing produces it and no resource cap -> starved forever.
    for item_id in sorted(consumed - produced - capped):
        issues.append(
            Issue(
                "warning",
                "unproducible-item",
                f"item {item_id!r} is consumed but produced by no recipe and has no "
                "resource cap; its consumers can never run",
            )
        )

    # Produced, never consumed, and not sinkable -> can never leave the system.
    for item_id in sorted(produced - consumed):
        if not config.is_sinkable(item_id):
            issues.append(
                Issue(
                    "warning",
                    "dead-end-item",
                    f"item {item_id!r} is produced but never consumed and is not "
                    "sinkable; it can never leave the system",
                )
            )

    # Power consumers with no generator: the optimum is stuck at 0 silently.
    needs_power = any(config.power_draw_for(r) > 0 for r in config.recipes)
    generates = any(POWER_ITEM in r.outputs for r in config.recipes)
    if needs_power and not generates:
        issues.append(
            Issue(
                "warning",
                "no-power-source",
                "recipes draw power but no recipe generates the 'power' item; "
                "powered machines can never run",
            )
        )

    # Extractor recipes (no inputs) without a node cap -> unbounded supply,
    # almost certainly a missing max_machines.
    for r in config.recipes:
        if not r.inputs and r.max_machines is None:
            issues.append(
                Issue(
                    "warning",
                    "uncapped-extractor",
                    f"extractor recipe {r.id!r} has no inputs and no max_machines "
                    "cap; its output supply is unbounded",
                )
            )

    # Resource caps on items that are also produced (double-limits supply).
    for item_id in sorted(capped & produced):
        issues.append(
            Issue(
                "warning",
                "capped-and-produced",
                f"item {item_id!r} is map-capped in 'resources' and also produced "
                "by a recipe; the cap applies to total consumption",
            )
        )

    if include_info:
        # Info-level findings (advisory only), omitted by default.
        pass

    return sorted(issues, key=lambda i: (SEVERITY_RANK[i.severity], i.code))


# ---------------------------------------------------------------------------
# Text rendering
# ---------------------------------------------------------------------------


def audit_text(config: Config, issues: list[Issue]) -> str:
    """Render the audit as a compact block for the terminal."""
    used = len({r.machine for r in config.recipes})
    lines = ["=== consistency check ==="]
    lines.append(
        f"  {len(config.recipes)} recipes, {len(config.machines)} machine specs "
        f"({used} referenced by recipes), {len(config.items)} items"
    )
    if not issues:
        lines.append("  ok  no issues found")
    else:
        for issue in issues:
            mark = "error" if issue.severity == "error" else "warn "
            lines.append(f"  {mark}  [{issue.code}] {issue.message}")
    errors = sum(1 for i in issues if i.severity == "error")
    warnings = sum(1 for i in issues if i.severity == "warning")
    lines.append(f"  {errors} error(s), {warnings} warning(s)")
    return "\n".join(lines)


def has_errors(issues: list[Issue]) -> bool:
    return any(i.severity == "error" for i in issues)


def has_warnings(issues: list[Issue]) -> bool:
    return any(i.severity == "warning" for i in issues)
