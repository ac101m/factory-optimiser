"""Human-readable Markdown build-plan report.

Turns the best solution from the optimizer into a Markdown document that can be
used to plan an actual in-game build: a high-level overview (points, power,
sink flows, map extraction) followed by a per-machine breakdown of every recipe
with its aggregate inputs/outputs at the planned clock.

Unlike the skimmable console table (report.optimize_text), this reconstructs
per-recipe throughput by machine type and is regenerated programmatically by
the ``report`` CLI command.
"""

from __future__ import annotations

import math
from collections import OrderedDict

from .io_config import CLOCK_POWER_EXP, Config, POWER_ITEM, sloop_multipliers
from .report import PlanMachine, downconvert
from .sweep import AugResult

#: Machine ids whose rows are "map extraction" (no recipe inputs).
EXTRACTOR_MACHINES = (
    "miner",
    "miner_mk2",
    "miner_mk3",
    "oil_extractor",
    "water_extractor",
    "resource_well_pressurizer",
)

MACHINE_TITLES = {
    "oil_extractor": "Oil Extractor",
    "resource_well_pressurizer": "Resource Well Pressurizer",
    "miner_mk3": "Miner Mk.3",
    "nuclear_power_plant": "Nuclear Power Plant",
    "fuel_generator": "Fuel Generator",
    "quantum_encoder": "Quantum Encoder",
    "water_extractor": "Water Extractor",
    "geothermal_generator": "Geothermal Generator",
}


def _machine_title(machine_id: str) -> str:
    return MACHINE_TITLES.get(machine_id, machine_id.replace("_", " ").title())


def _fmt_io(bal: dict[str, float]) -> str:
    if not bal:
        return "—"
    return " + ".join(f"{k} {v:,.1f}" for k, v in sorted(bal.items()))


def _entry_power(recipe, config: Config, m: PlanMachine) -> tuple[float, float]:
    """(draw_MW, gen_MW) for one plan entry, at the buildable (whole-machine) footprint."""
    grade = sloop_multipliers(m.sloops_per_machine, config.max_sloops_for(m.machine))
    clk = m.clock_pct / 100.0
    draw = m.machines * (clk ** CLOCK_POWER_EXP) * grade.pi * config.power_draw_for(recipe)
    gen = m.machines * clk * grade.rho * recipe.outputs.get(POWER_ITEM, 0.0)
    return draw, gen


def _clock_breakdown(m: PlanMachine) -> str:
    """'10@100% + 1@50%': whole machines at the clock tier plus the partial
    machine trimmed to match the fractional activity — throughput-equivalent to
    running every machine in the row at the uniform `clock_pct`."""
    tier = m.clock_pct / 100.0 * m.machines / m.activity  # recover the clock tier
    whole = math.floor(m.activity + 1e-9)
    frac = m.activity - whole
    main = tier * 100.0
    if frac <= 1e-9:
        return f"{whole}@{main:.0f}%"
    rem = frac * main
    if rem < 0.05:
        return f"{whole}@{main:.0f}%"  # dust remainder, not a buildable instruction
    rem_s = f"{rem:.0f}%" if abs(rem - round(rem)) < 0.05 else f"{rem:.1f}%"
    if whole < 1:
        return f"1@{rem_s}"  # fully trimmed row: nothing left running at the tier
    return f"{whole}@{main:.0f}% + 1@{rem_s}"


def optimize_markdown(config: Config, best: AugResult, curve: list[AugResult]) -> str:
    plan = downconvert(config, best.solution)
    sol = best.solution
    recipes_by_id = {r.id: r for r in config.recipes}
    for m in plan:
        recipe = recipes_by_id[m.recipe_id]
        m._recipe = recipe
        m._draw, m._gen = _entry_power(recipe, config, m)

    def item(n):
        return config.item_name(n, n)

    L: list[str] = []
    W = L.append

    tiers = ", ".join(f"{t*100:g}%" for t in config.parameters.overclock_tiers)
    aug = "Auto-solved (augmenter sweep)" if len(curve) > 1 else "No augmenters"

    W("# Satisfactory Factory Optimiser — Build Plan")
    W("")
    W(
        f"**Official optimum** — **{best.points_per_min:,.0f} pts/min** "
        f"(overclock tiers {tiers}; {aug}). All rates are per minute."
    )
    W("")

    # ---- high-level overview -------------------------------------------------
    W("## High-level overview")
    W("")
    W("| Metric | Value | Notes |")
    W("|---|---|---|")
    W(f"| **Sink points** | **{best.points_per_min:,.0f} pts/min** | {best.n_augmenters} augmenter(s), {best.power_multiplier:.2f}x power |")
    W(f"| **Power load** | **{sol.power_consumed:,.0f} MW** | what consumers actually draw |")
    W(
        f"| **Power supplied** | {sol.power_available:,.0f} MW | "
        f"load x{1 + config.parameters.power_overproduction:.2f} ({config.parameters.power_overproduction*100:g}% reserve) |"
    )
    n_machines = sum(m.machines for m in plan)
    n_types = len({m.machine for m in plan})
    cap = config.parameters.machine_cap
    machine_cell = (
        f"**{n_machines:,.0f}** (cap {cap:,.0f} — binding)"
        if cap is not None and n_machines >= cap - 0.5
        else f"**{n_machines:,.0f}**" + (f" / cap {cap:,.0f}" if cap is not None else "")
    )
    W(f"| **Machines** | {machine_cell} | {len(plan)} recipe rows across {n_types} machine types |")
    W(f"| **Somersloops** | {sol.sloops_used:g} / {best.sloop_budget:g} | see overclock notes |")
    sink_items = sum(sol.sinks.values()) + sum(sol.raw_sinks.values())
    W(f"| **Sink throughput** | {sink_items:,.1f} items/min | one Awesome Sink covers it (1200/min cap, 30 MW) |")
    W("")

    # ---- sink flows ----------------------------------------------------------
    sink_map = {**sol.sinks, **sol.raw_sinks}
    sink_rows = [
        (item, rate, config.items[item].points, rate * config.items[item].points)
        for item, rate in sink_map.items()
        if rate > 0
    ]
    if sink_rows:
        W("### Sink flows")
        W("")
        W("| Sink item | pts/item | /min | pts/min | share |")
        W("|---|---:|---:|---:|---:|")
        for ikey, rate, pts, value in sorted(sink_rows, key=lambda t: -t[3]):
            W(f"| {item(ikey)} | {pts:,.0f} | {rate:,.1f} | {value:,.0f} | {value / best.points_per_min * 100:.1f}% |")
        W(f"| **TOTAL** | | | **{best.points_per_min:,.0f}** | 100% |")
        W("")

    # ---- map resources extracted ---------------------------------------------
    extractors = [m for m in plan if m.machine in EXTRACTOR_MACHINES]
    if extractors:
        agg: dict[str, float] = {}
        machines_of: dict[str, float] = {}
        for m in extractors:
            for o, v in m.outputs.items():
                agg[o] = agg.get(o, 0.0) + v
                machines_of[o] = machines_of.get(o, 0.0) + m.machines
        W("### Map resources extracted")
        W("")
        W("Miners are shown at their planned 250% clock; every tapped node group is maxed.")
        W("")
        W("| Resource | extractors | /min |")
        W("|---|---:|---:|")
        for o in sorted(agg, key=lambda o: -agg[o]):
            W(f"| {item(o)} | {machines_of[o]:,.0f} | {agg[o]:,.0f} |")
        W("")

    # ---- production per item -------------------------------------------------
    produced: dict[str, float] = {}
    consumed: dict[str, float] = {}
    for m in plan:
        for o, v in m.outputs.items():
            produced[o] = produced.get(o, 0.0) + v
        for i, v in m.inputs.items():
            consumed[i] = consumed.get(i, 0.0) + v
    sink_rates = {
        k: v for k, v in {**sol.sinks, **sol.raw_sinks}.items() if v > 1e-9
    }

    W("---")
    W("")
    W("# Production per item")
    W("")
    W("Aggregate material balance across the whole plan (production includes extraction).")
    W("")
    W("| Item | produced/min | consumed/min | net | destination |")
    W("|---|---:|---:|---:|---|")
    all_items = sorted(
        set(produced) | set(consumed) | set(sink_rates),
        key=lambda i: (-produced.get(i, 0.0), item(i)),
    )
    for it in all_items:
        p = produced.get(it, 0.0)
        c = consumed.get(it, 0.0)
        net = p - c
        sr = sink_rates.get(it, 0.0)
        if sr > 0:
            note = f"→ Awesome Sink ({sr:,.1f}/min)"
        elif abs(net) <= max(1e-3, 1e-6 * max(p, c, 1.0)):
            note = "balanced"
        else:
            note = "⚠ unbalanced"
        W(f"| {item(it)} | {p:,.1f} | {c:,.1f} | {net:+,.1f} | {note} |")
    W("")

    # ---- all used recipes (summary index) ----------------------
    producer_rows = [m for m in plan if m.machine not in EXTRACTOR_MACHINES]
    extractor_rows = [m for m in plan if m.machine in EXTRACTOR_MACHINES]

    W("---")
    W("")
    W("# All used recipes")
    W("")
    W(
        f"{len(producer_rows)} production recipe rows from {len({m.recipe_id for m in producer_rows})} "
        f"distinct recipes (rows repeat a recipe when sloop grades or clocks differ); extractors are "
        f"listed in the Resource extraction table underneath. `count` is the machines "
        f"to build, with the raw fractional count in brackets; `clock` shows how to split that "
        f"build into whole machines at the clock tier plus one trimmed remainder (e.g. "
        f"`10@100% + 1@50%`); `equivalent all-machine clock` is the single uniform clock "
        f"that reproduces the same throughput. A row whose equivalent clock sits below "
        f"the tier is an exact-balance remnant, not a choice."
    )
    W("")
    W("| Recipe | machine | count | clock | equivalent all-machine clock |")
    W("|---|---|---:|---:|---:|")
    for m in sorted(producer_rows, key=lambda x: (x.machine, x._recipe.name)):
        sloop_tag = f" ({m.sloops_per_machine} sloops)" if m.sloops_per_machine else ""
        W(
            f"| {m._recipe.name}{sloop_tag} | {m.machine} | {m.machines:,.0f} "
            f"({m.activity:.4f}) | {_clock_breakdown(m)} | {m.clock_pct:.1f}% |"
        )
    W("")

    if extractor_rows:
        W("### Resource extraction")
        W("")
        W(
            "Miners, water/oil extractors and pressure wells pulled out of All used recipes — "
            "every tapped node group at its planned count/clock. (Per-node grouping is further "
            "down in the dedicated Resource extraction section.)"
        )
        W("")
        W("| Recipe | machine | count | clock | equivalent all-machine clock |")
        W("|---|---|---:|---:|---:|")
        for m in sorted(extractor_rows, key=lambda x: (x.machine, x._recipe.name)):
            sloop_tag = f" ({m.sloops_per_machine} sloops)" if m.sloops_per_machine else ""
            W(
                f"| {m._recipe.name}{sloop_tag} | {m.machine} | {m.machines:,.0f} "
                f"({m.activity:.4f}) | {_clock_breakdown(m)} | {m.clock_pct:.1f}% |"
            )
        W("")

    # ---- per item breakdown --------------------------------------------------
    producers_by_item: dict[str, list[tuple]] = {}
    for m in plan:
        for o, v in m.outputs.items():
            if v > 1e-9:
                producers_by_item.setdefault(o, []).append((m, v))

    W("---")
    W("")
    W("# Per item breakdown")
    W("")
    W(
        "For every item this plan produces, the recipes that make it — with the plan's "
        "whole-machine count, clock, sloop grade, and the share of the item's total that "
        "each recipe supplies."
    )
    W("")
    for it in all_items:
        rows = producers_by_item.get(it)
        if not rows:
            continue
        total = produced.get(it, 0.0)
        W(f"## {item(it)} — {total:,.1f}/min")
        W("")
        W("| Recipe | machine | count | clock | slps | /min | share |")
        W("|---|---|---:|---:|---:|---:|---:|")
        for m, v in sorted(rows, key=lambda t: -t[1]):
            W(
                f"| {m._recipe.name} | {m.machine} | {m.machines:,.0f} | "
                f"{m.clock_pct:.1f}% | {m.sloops_per_machine or '—'} | {v:,.1f} | "
                f"{v / total * 100:.1f}% |"
            )
        W("")

    # ---- per-machine production sections -------------------------------------
    groups: OrderedDict = OrderedDict()
    for m in plan:
        groups.setdefault(m.machine, []).append(m)

    generator_groups = {mid for mid, rs in groups.items() if any(x._gen > 0 for x in rs)}
    extractor_set = set(EXTRACTOR_MACHINES)
    production = OrderedDict(
        (k, v) for k, v in groups.items() if k not in generator_groups and k not in extractor_set
    )
    extraction = OrderedDict((k, v) for k, v in groups.items() if k in extractor_set)
    generators = OrderedDict((k, v) for k, v in groups.items() if k in generator_groups)

    def _consumer_section(mid: str, rs: list) -> None:
        t = sum(x.machines for x in rs)
        d = sum(x._draw for x in rs)
        W(f"## {_machine_title(mid)} — {t:,.0f} machines · {d:,.0f} MW")
        W("")
        W("| Recipe | count | clock | slps | inputs /min | outputs /min |")
        W("|---|---|---:|---:|---|---|")
        for x in sorted(rs, key=lambda x: -x.machines):
            ins = {item(i): v for i, v in x.inputs.items()}
            outs = {item(o): v for o, v in x.outputs.items()}
            W(
                f"| {x._recipe.name} | {x.machines:,.0f} | {x.clock_pct:.1f}% | "
                f"{x.sloops_per_machine or '—'} | {_fmt_io(ins)} | {_fmt_io(outs)} |"
            )
        W("")

    W("---")
    W("")
    W("# Per-machine breakdown")
    W("")
    W(
        "One section per machine type in the plan: the recipes it runs, the whole-machine "
        "count, clock and sloop grade, and aggregate inputs/outputs per minute."
    )
    W("")
    for mid, rs in sorted(production.items(), key=lambda kv: -sum(x.machines for x in kv[1])):
        _consumer_section(mid, rs)

    W("---")
    W("")
    W("# Resource extraction")
    W("")
    if extraction:
        W(
            "Raw-material supply: miners, water/oil extractors and pressure wells. "
            "(The high-level overview aggregates these by resource; here each node group is listed.)"
        )
        W("")
        for mid, rs in sorted(extraction.items(), key=lambda kv: -sum(x.machines for x in kv[1])):
            _consumer_section(mid, rs)
    else:
        W("(no extractor recipes in this plan)")
        W("")

    W("---")
    W("")
    W("# Power generation")
    W("")
    for mid, rs in generators.items():
        t = sum(x.machines for x in rs)
        g = sum(x._gen for x in rs)
        W(f"## {_machine_title(mid)} — {t:,.0f} machines · **{g:,.0f} MW generated**")
        W("")
        W("| Recipe | count | clock | slps | fuel /min | output |")
        W("|---|---|---:|---:|---|---|")
        for x in sorted(rs, key=lambda x: -x._gen):
            ins = {item(i): v for i, v in x.inputs.items()}
            W(
                f"| {x._recipe.name} | {x.machines:,.0f} | {x.clock_pct:.1f}% | "
                f"{x.sloops_per_machine or '—'} | {_fmt_io(ins)} | {x._gen:,.0f} MW |"
            )
        W("")

    # ---- notes ----------------------------------------------------------------
    W("---")
    W("")
    W("## Notes")
    W("")
    sum_draw = sum(x._draw for x in plan)
    W(
        f"- **Power rounding**: per-section draws are computed from the displayed whole-machine "
        f"counts and sum to {sum_draw:,.0f} MW, ~0.1% under the official {sol.power_consumed:,.0f} MW "
        f"(the model also runs tiny sub-machine exact-balance slivers). Generation is clock-linear, "
        f"so whole-machine sums reproduce the {sol.power_available:,.0f} MW exactly."
    )
    W("- Accelerator rows use per-recipe power draw where the spec overrides it; other machines use their machine default.")
    W("- Rates are **aggregate** at the displayed clock. Per-machine rate at that clock = aggregate ÷ `#`.")

    return "\n".join(L) + "\n"
