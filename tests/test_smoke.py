#!/usr/bin/env python3
"""Smoke tests for the MILP model + CLI. Run: .venv/bin/python tests/test_smoke.py

No external test framework needed; plain asserts. Exits 0 when everything
holds, prints a summary per check.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from factory_optimiser.io_config import (
    Config,
    ConfigError,
    Item,
    Parameters,
    Recipe,
    MachineSpec,
    Augmenters,
)  # noqa: E402
from factory_optimiser.model import build_problem  # noqa: E402
from factory_optimiser.solve import solve  # noqa: E402
from factory_optimiser.sweep import best_augmenter, sweep_augmenters, sweep_somersloops  # noqa: E402
from factory_optimiser.report import downconvert, total_points  # noqa: E402

_CHECKS = 0


def check(name: str) -> None:
    global _CHECKS
    _CHECKS += 1
    print(f"  ok  {name}")


def load_example() -> Config:
    return Config(
        items={
            "ore": Item("ore", "Ore", sinkable=False),
            "bar": Item("bar", "Bar", sinkable=True, points=10.0),
            "art": Item("Art", "Art", sinkable=True, points=55.0),
            "coal": Item("coal", "Coal", sinkable=True, points=3.0),
        },
        recipes=[
            Recipe(id="bar", name="Bar", machine="constructor", inputs={"ore": 30.0}, outputs={"bar": 30.0}),
            Recipe(id="art", name="Art", machine="constructor", inputs={"bar": 15.0}, outputs={"art": 15.0}),
            Recipe(id="coal_power", name="Coal Power", machine="generator", inputs={"coal": 15.0}, outputs={"power": 75.0}),
        ],
        machines={
            "constructor": MachineSpec(id="constructor", power_draw=4.0, max_sloops=3),
            "generator": MachineSpec(id="generator", power_draw=0.0, max_sloops=1),
        },
        parameters=Parameters(
            resources={"ore": 60.0, "coal": 30.0},
            somersloop_budget=4.0,
            augmenters=Augmenters(cost=10, bonus=0.1),
        ),
    )


def test_milp_basic() -> None:
    cfg = load_example()
    # 60 ore/min -> bar -> art. All 60 ore yields either 60 bar or 30 art.
    # Art (55/sink unit at 15/min) is worth ~2.75x bar (10/unit at 30/min). The
    # solver should push all ore through art, with bar only as overflow.
    cfg.items["bar"] = Item("bar", "Bar", sinkable=True, points=10.0)
    sol = solve(build_problem(cfg, n_augmenters=0))
    assert abs(total_points(cfg, sol) - sol.objective) < 1e-6
    assert sol.sinks["art"] > 29.0  # ~all art derived
    # with 4 sloops, a k=3 bar machine (1 sloop? no - k=3 needs 3 sloops)
    assert sol.sloops_used <= cfg.parameters.somersloop_budget + 1e-9
    check("MILP: objective == sink point sum; sloops within budget")


def test_scarcity_routing() -> None:
    # When two consumers fight over scarce ore, the higher-value sink wins.
    cfg = load_example()
    cfg.recipes.append(
        Recipe(id="junk", name="Junk", machine="constructor",
               inputs={"ore": 30.0}, outputs={"junk": 30.0})
    )
    cfg.items["junk"] = Item("junk", "Junk", sinkable=True, points=1.0)
    sol = solve(build_problem(cfg, n_augmenters=0))
    assert sol.sinks.get("junk", 0.0) < 1e-6, "low-value recipe should be starved"
    check("MILP: scarce item routes to the highest-value consumer")


def test_power_balance() -> None:
    cfg = load_example()
    sol = solve(build_problem(cfg, n_augmenters=0))
    # Coal: 30/min available. Generators need 15/min each. Consumption <= deliverable.
    assert sol.power_consumed <= sol.power_available + 1e-6
    check("MILP: power consumption within augmented capacity")


def test_augmenter_flat_power() -> None:
    # Each augmenter adds flat_power_mw MW that the +10% bonus does NOT apply
    # to. N=1 should power a consumer-only factory that has NO generator at all.
    cfg = load_example()
    cfg.parameters.somersloop_budget = 20.0  # affords N=1 (cost 10)
    cfg.parameters.resources = {"ore": 60.0}  # drop coal so nothing is raw-sinkable
    cfg.recipes = [r for r in cfg.recipes if r.id != "coal_power"]  # no generator
    cfg.parameters.augmenters = Augmenters(cost=10, bonus=0.1, power_mw=500.0)

    prob = build_problem(cfg, n_augmenters=1)
    assert prob.flat_power_mw == 500.0
    sol = solve(prob)
    assert sol.objective > 0.0, "flat 500 MW from one augmenter must run consumers"
    assert sol.power_consumed <= sol.power_available + 1e-6
    assert abs(sol.power_available - (sol.power_generated * 1.1 + 500.0)) < 1e-6

    # With no augmenter the same factory is dead (no power at all).
    sol0 = solve(build_problem(cfg, n_augmenters=0))
    assert sol0.objective == 0.0
    check("power: augmenter flat MW is usable without a generator and un-bonused")


def test_augmenter_sweep_deterministic() -> None:
    cfg = load_example()
    r1 = best_augmenter(cfg)
    r2 = best_augmenter(cfg)
    assert r1.points_per_min == r2.points_per_min
    assert r1.n_augmenters == r2.n_augmenters
    results = sweep_augmenters(cfg)
    assert results[0].n_augmenters == 0
    assert [r.n_augmenters for r in results] == sorted(r.n_augmenters for r in results)
    check("sweep: deterministic, ascending N")


def test_downconvert_includes_grade_multiplier() -> None:
    cfg = load_example()
    cfg.parameters.somersloop_budget = 10.0
    cfg.recipes.clear()
    cfg.machines["constructor"] = MachineSpec(power_draw=0.0, max_sloops=3)  # power not under test
    # max_machines=1 forces sloops past the cap. The machine has T=3 slots, so a
    # k=3 machine gets rho = 1 + 3/3 = 2x output from the SAME 10 ore input.
    cfg.recipes.append(
        Recipe(id="bar", name="Bar", machine="constructor",
               inputs={"ore": 10.0}, outputs={"bar": 10.0}, max_machines=1.0)
    )
    cfg.items["bar"] = Item("bar", "Bar", sinkable=True, points=100.0)
    cfg.parameters.resources = {"ore": 100.0}
    sol = solve(build_problem(cfg, n_augmenters=0))
    plan = downconvert(cfg, sol)
    slooped = [m for m in plan if m.sloops_per_machine == 3]
    assert slooped, "with 10 sloops and a machine cap a k=3 bar machine should be used"
    m = slooped[0]
    # one k=3 machine: 2x the base 10/min output = 20/min, still 10 ore in
    assert abs(m.outputs["bar"] - 20.0) < 1e-6
    assert abs(m.inputs["ore"] - 10.0) < 1e-6, "slooping must not increase input"
    check("downconvert: output scaled by confirmed rho=1+k/T, input unchanged")


def test_sloop_multipliers_confirmed_formula() -> None:
    from factory_optimiser.io_config import sloop_multipliers

    # A 2-slot machine with 1 slot filled: 1.5x output, same input, (1.5)^2 power.
    g = sloop_multipliers(k=1, total_slots=2)
    assert abs(g.rho - 1.5) < 1e-9
    assert abs(g.kappa - 1.0) < 1e-9                      # inputs unchanged
    assert abs(g.pi - 2.25) < 1e-9
    # Full slots -> exactly 2x output and 4x power.
    gfull = sloop_multipliers(k=3, total_slots=3)
    assert abs(gfull.rho - 2.0) < 1e-9
    assert abs(gfull.pi - 4.0) < 1e-9
    # Base and unsloopable machines stay at 1x.
    g0 = sloop_multipliers(k=0, total_slots=2)
    assert abs(g0.rho - 1.0) < 1e-9 and abs(g0.kappa - 1.0) < 1e-9 and abs(g0.pi - 1.0) < 1e-9
    assert sloop_multipliers(k=0, total_slots=0).rho == 1.0  # no slots -> base
    check("sloops: confirmed formula rho=1+k/T, kappa=1, pi=(1+k/T)^2")


def test_machine_cap_enforced() -> None:
    cfg = load_example()
    cfg.parameters.somersloop_budget = 0.0
    cfg.recipes.clear()
    cfg.machines["constructor"] = MachineSpec(power_draw=0.0, max_sloops=3)  # power not under test
    cfg.recipes.append(
        Recipe(id="bar", name="Bar", machine="constructor",
               inputs={"ore": 10.0}, outputs={"bar": 10.0}, max_machines=2.0)
    )
    cfg.items["bar"] = Item("bar", "Bar", sinkable=True, points=100.0)
    cfg.parameters.resources = {"ore": 100.0}
    sol = solve(build_problem(cfg, n_augmenters=0))
    machines = sum(m.machines for m in downconvert(cfg, sol))
    assert machines <= 2.0 + 1e-9
    check("MILP: per-recipe max_machines cap enforced")


def test_cli_launcher_and_json() -> None:
    env = dict(os.environ, PYTHONPATH=str(ROOT))
    py = str(ROOT / ".venv" / "bin" / "python")
    ver = subprocess.run([py, "main.py", "--version"], env=env, capture_output=True, text=True)
    assert ver.returncode == 0 and "factory-optimiser" in ver.stdout
    proc = subprocess.run([py, "main.py", "optimize", "--json"], env=env, capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    data = json.loads(proc.stdout)
    assert "n_augmenters" in data["best"] and "flat_power_mw" in data["best"]
    assert data["best"]["sloops_used"] > 0
    proc = subprocess.run([py, "main.py", "sweep", "somersloops"], env=env, capture_output=True, text=True)
    assert proc.returncode == 0
    check("CLI: --version / optimize --json / sweep run through the launcher")


def test_dominated_recipe_unused() -> None:
    # Two recipes make the same item; the less efficient one is dominated.
    cfg = load_example()
    cfg.recipes.clear()
    cfg.machines["constructor"] = MachineSpec(power_draw=0.0, max_sloops=3)  # power not under test
    cfg.recipes.append(
        Recipe(id="bar_a", name="Bar A", machine="constructor",
               inputs={"ore": 30.0}, outputs={"bar": 30.0})
    )
    cfg.recipes.append(
        Recipe(id="bar_b", name="Bar B", machine="constructor",
               inputs={"ore": 60.0}, outputs={"bar": 30.0})  # 2x ore, same output
    )
    cfg.items["bar"] = Item("bar", "Bar", sinkable=True, points=50.0)
    cfg.parameters.resources = {"ore": 60.0}
    sol = solve(build_problem(cfg, n_augmenters=0))
    used = {cfg.recipes[r].id: v for (r, k, c), v in sol.activities.items() if v > 1e-9}
    assert abs(used.get("bar_a", 0.0) - 2.0) < 1e-6   # all 60 ore routed to Bar A
    assert "bar_b" not in used
    check("MILP: dominated recipe producing the same item is left unused")


def test_power_draw_inherited_from_machine_type() -> None:
    # Consumers draw power from machines[type], not from the recipe
    # JSON, so that draw must activate the power constraint even with no
    # generator present. Without a generator, no powered machine may run.
    cfg = load_example()
    cfg.recipes.clear()
    cfg.recipes.append(
        Recipe(id="bar", name="Bar", machine="constructor",
               inputs={"ore": 10.0}, outputs={"bar": 10.0})
    )
    cfg.items["bar"] = Item("bar", "Bar", sinkable=True, points=10.0)
    cfg.parameters.resources = {"ore": 100.0}
    problem = build_problem(cfg, n_augmenters=0)
    assert problem.has_power, "machine-default power draw must activate the power constraint"
    sol = solve(problem)
    assert sol.objective == 0.0, "no generator present -> powered machines cannot run"
    check("MILP: power draw inherited from machine type is enforced")


def test_extractor_recipe_bounds_supply() -> None:
    # A miner (no-input) recipe is the only ore source; its max_machines cap IS
    # the map resource limit. And because it draws power, no generator -> no ore.
    cfg = load_example()
    cfg.recipes.clear()
    cfg.parameters.resources = {}
    cfg.parameters.somersloop_budget = 0.0  # isolate max_machines from sloop multipliers
    cfg.machines["miner"] = MachineSpec(power_draw=0.0, max_sloops=3)
    cfg.machines["constructor"] = MachineSpec(power_draw=0.0, max_sloops=3)
    cfg.recipes.append(
        Recipe(id="miner", name="Miner", machine="miner",
               inputs={}, outputs={"ore": 60.0}, max_machines=2.0)
    )
    cfg.recipes.append(
        Recipe(id="smelter", name="Smelter", machine="constructor",
               inputs={"ore": 30.0}, outputs={"bar": 30.0})
    )
    cfg.items["ore"] = Item("ore", "Ore", sinkable=False)
    cfg.items["bar"] = Item("bar", "Bar", sinkable=True, points=10.0)
    sol = solve(build_problem(cfg, n_augmenters=0))
    # 2 miners x 60 ore/min = 120 ore/min -> 4 smelters -> 120 bar. No more.
    assert abs(sol.sinks["bar"] - 120.0) < 1e-6, "extractor max_machines must cap supply"
    # Now give the miner a power draw and remove any generator: nothing may run.
    cfg.machines["miner"] = MachineSpec(power_draw=5.0, max_sloops=3)
    sol2 = solve(build_problem(cfg, n_augmenters=0))
    assert sol2.objective == 0.0, "miner power draw must be enforced"
    check("MILP: extractor recipes cap supply via max_machines and draw power")


def test_overclock_slooped_machine() -> None:
    # A slooped machine on a capped recipe can be overclocked: with a clock
    # tier c=2.0, one k=1 machine (T=1: rho=2) puts out c*rho*beta = 40/min,
    # i.e. 4x the base machine for the same one sloop.
    cfg = load_example()
    cfg.parameters.somersloop_budget = 10.0
    cfg.parameters.overclock_tiers = [1.0, 2.0]
    cfg.recipes.clear()
    cfg.machines["constructor"] = MachineSpec(power_draw=0.0, max_sloops=1, overclockable=True)
    cfg.recipes.append(
        Recipe(id="bar", name="Bar", machine="constructor",
               inputs={"ore": 10.0}, outputs={"bar": 10.0}, max_machines=1.0)
    )
    cfg.items["bar"] = Item("bar", "Bar", sinkable=True, points=100.0)
    cfg.parameters.resources = {"ore": 100.0}
    sol = solve(build_problem(cfg, n_augmenters=0))
    plan = downconvert(cfg, sol)
    slooped = [m for m in plan if m.sloops_per_machine == 1]
    assert slooped, "the capped recipe must sloop (budget > 0, cap = 1)"
    m = max(slooped, key=lambda m: m.activity)
    assert abs(m.clock_pct - 200.0) < 1e-6, "slooped machine should be overclocked to 200%"
    assert abs(m.outputs["bar"] - 40.0) < 1e-6  # 2.0 clock * 2.0 rho * 10 base
    check("overclock: a slooped machine on a capped recipe is overclocked (c*rho*beta)")


def test_overclock_power_factor() -> None:
    # Power draw of an overclocked consumer uses c^1.321928 (game curve),
    # stacked on the sloop pi factor. With a 250% tier and no sloops:
    # draw = 4 MW * 2.5^1.321928.
    cfg = load_example()
    cfg.parameters.somersloop_budget = 0.0
    cfg.parameters.overclock_tiers = [1.0, 2.5]
    cfg.recipes.clear()
    cfg.machines["constructor"] = MachineSpec(power_draw=4.0, max_sloops=0, overclockable=True)
    cfg.recipes.append(
        Recipe(id="bar", name="Bar", machine="constructor",
               inputs={"ore": 10.0}, outputs={"bar": 10.0}, max_machines=1.0)
    )
    cfg.recipes.append(
        Recipe(id="coal_power", name="Coal Power", machine="generator",
               inputs={"coal": 15.0}, outputs={"power": 75.0})
    )
    cfg.items["bar"] = Item("bar", "Bar", sinkable=True, points=100.0)
    cfg.parameters.resources = {"ore": 100.0, "coal": 15.0}
    sol = solve(build_problem(cfg, n_augmenters=0))
    plan = downconvert(cfg, sol)
    bar = [m for m in plan if m.recipe_id == "bar"]
    assert bar and abs(bar[0].clock_pct - 250.0) < 1e-6
    expected = 4.0 * (2.5 ** 1.321928)
    assert abs(sol.power_consumed - expected) < 1e-6, "overclock power must be c^1.321928 * draw"
    assert sol.power_consumed <= sol.power_available + 1e-6
    check("overclock: power draw = c^1.321928 * base draw (confirmed game curve)")


def test_overclock_extractor_breaks_cap() -> None:
    # The game's biggest overclock win: miners (0-slot machines) at 250% break
    # the node cap -- 2 nodes * 60/min * 2.5 = 300 ore/min.
    cfg = load_example()
    cfg.parameters.overclock_tiers = [1.0, 2.5]
    cfg.parameters.resources = {}
    cfg.parameters.somersloop_budget = 0.0
    cfg.recipes.clear()
    cfg.machines["miner"] = MachineSpec(power_draw=0.0, max_sloops=0)  # overclockable default True
    cfg.machines["constructor"] = MachineSpec(power_draw=0.0, max_sloops=0)
    cfg.recipes.append(
        Recipe(id="miner", name="Miner", machine="miner",
               inputs={}, outputs={"ore": 60.0}, max_machines=2.0)
    )
    cfg.recipes.append(
        Recipe(id="smelter", name="Smelter", machine="constructor",
               inputs={"ore": 30.0}, outputs={"bar": 30.0})
    )
    cfg.items["ore"] = Item("ore", "Ore", sinkable=False)
    cfg.items["bar"] = Item("bar", "Bar", sinkable=True, points=10.0)
    sol = solve(build_problem(cfg, n_augmenters=0))
    assert abs(sol.sinks["bar"] - 300.0) < 1e-6, "overclocked miners must exceed the node cap"
    check("overclock: 0-slot extractor overclocking breaks node caps (real-game win)")


def test_non_overclockable_machine_fixed() -> None:
    # A machine marked overclockable=false can never be clocked above 100%,
    # no matter the tier list: capped extractor output stays 2 nodes * 60.
    cfg = load_example()
    cfg.parameters.overclock_tiers = [1.0, 2.5]
    cfg.parameters.resources = {}
    cfg.parameters.somersloop_budget = 0.0
    cfg.recipes.clear()
    cfg.machines["miner"] = MachineSpec(power_draw=0.0, max_sloops=0, overclockable=False)
    cfg.machines["constructor"] = MachineSpec(power_draw=0.0, max_sloops=0)
    cfg.recipes.append(
        Recipe(id="miner", name="Miner", machine="miner",
               inputs={}, outputs={"ore": 60.0}, max_machines=2.0)
    )
    cfg.recipes.append(
        Recipe(id="smelter", name="Smelter", machine="constructor",
               inputs={"ore": 30.0}, outputs={"bar": 30.0})
    )
    cfg.items["ore"] = Item("ore", "Ore", sinkable=False)
    cfg.items["bar"] = Item("bar", "Bar", sinkable=True, points=10.0)
    prob = build_problem(cfg, n_augmenters=0)
    miner_clocks = {c for (r, k, c) in prob.activity_col if r == 0}
    assert miner_clocks == {1.0}, "non-overclockable machine must have only the base clock"
    sol = solve(prob)
    assert abs(sol.sinks["bar"] - 120.0) < 1e-6, "non-overclockable extractor supply stays capped"
    check("overclock: overclockable=false fixes a machine at 100% (supply stays capped)")


def test_overclock_config_defaults_and_loader() -> None:
    import tempfile

    from factory_optimiser.io_config import load_machine, load_parameters

    # Parameters: no `overclock` key -> no overclocking ([1.0]); with tiers,
    # 1.0 is forced in, sorted and deduplicated.
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "parameters.json"
        p.write_text(json.dumps({
            "somersloop_budget": 10.0,
            "augmenters": {"cost": 10},
            "overclock": {"tiers": [2.5, 1.0, 2.0, 1.0]},
        }))
        params = load_parameters(p)
        assert params.overclock_tiers == [1.0, 2.0, 2.5]
    from factory_optimiser.io_config import Parameters, Augmenters
    params0 = Parameters(resources={}, somersloop_budget=0.0, augmenters=Augmenters())
    assert params0.overclock_tiers == [1.0], "default tier list = no overclocking"

    # Machine spec: overclockable defaults true; parses false from the file.
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "g.json").write_text('{"id": "geo_gen", "overclockable": false}')
        spec = load_machine(Path(tmp) / "g.json")
        assert spec.overclockable is False
    from factory_optimiser.io_config import MachineSpec
    assert MachineSpec(id="x").overclockable is True
    check("overclock: config defaults + loader (tiers normalized; overclockable flag)")


def test_overclock_consistency_checks() -> None:
    from factory_optimiser.consistency import check_config

    cfg = load_example()
    cfg.parameters.overclock_tiers = [1.0, -0.5]
    codes = {i.code for i in check_config(cfg) if i.severity == "error"}
    assert "overclock-nonpositive" in codes

    cfg.parameters.overclock_tiers = [1.0, 3.0]
    codes = {i.code for i in check_config(cfg) if i.severity == "warning"}
    assert "overclock-above-cap" in codes
    check("consistency: bad overclock tiers flagged (non-positive error, above-cap warn)")


def test_underclock_power_efficiency() -> None:
    # Convex power means underclocking is power-efficient: at 50% clock a
    # machine makes 0.5x output for only 0.5^1.321928 ~= 0.40x draw. Inside a
    # hard power cap this beats the power-linear fractional model. 10 machines
    # at 20 MW would want 200 MW; only 75 MW (one coal gen) is available.
    cfg = load_example()
    cfg.parameters.somersloop_budget = 0.0
    cfg.parameters.overclock_tiers = [0.5, 1.0]
    cfg.recipes.clear()
    cfg.machines["constructor"] = MachineSpec(power_draw=20.0, max_sloops=0, overclockable=True)
    cfg.recipes.append(
        Recipe(id="bar", name="Bar", machine="constructor",
               inputs={"ore": 10.0}, outputs={"bar": 10.0})
    )
    cfg.recipes.append(
        Recipe(id="coal_power", name="Coal Power", machine="generator",
               inputs={"coal": 15.0}, outputs={"power": 75.0})
    )
    cfg.items["bar"] = Item("bar", "Bar", sinkable=True, points=10.0)
    cfg.parameters.resources = {"ore": 100.0, "coal": 15.0}
    sol = solve(build_problem(cfg, n_augmenters=0))
    # Power budget 75 MW. c=1 alone caps at 75/20 = 3.75 machines -> 37.5 bar.
    # Underclocking to 50% (8.04 MW/full machine) reaches ~9.3 machines -> ~46.7 bar.
    assert sol.sinks["bar"] > 40.0, "50% underclock must beat the power-linear optimum (~46.7 vs 37.5)"
    assert sol.power_consumed <= sol.power_available + 1e-6
    assert abs(sol.power_consumed / 75.0) > 0.9, "should be hugging the power cap"
    check("underclock: 50% tier saves power via c^1.321928 inside a hard power cap")


def test_underclock_tier_attachment() -> None:
    # k=0 continuous of a slot machine gets only the <=1.0 (underclock) tiers;
    # the integer slooped grade k=1 gets the full tier list.
    cfg = load_example()
    cfg.parameters.overclock_tiers = [0.5, 0.75, 1.0, 2.0]
    cfg.recipes.clear()
    cfg.machines["constructor"] = MachineSpec(power_draw=0.0, max_sloops=1, overclockable=True)
    cfg.recipes.append(
        Recipe(id="bar", name="Bar", machine="constructor",
               inputs={"ore": 10.0}, outputs={"bar": 10.0})
    )
    cfg.items["bar"] = Item("bar", "Bar", sinkable=True, points=10.0)
    cfg.parameters.resources = {"ore": 10.0}
    prob = build_problem(cfg, n_augmenters=0)
    by_grade = {
        k: sorted({c for (r, k2, c) in prob.activity_col if k2 == k})
        for k in (0, 1)
    }
    assert by_grade[0] == [0.5, 0.75, 1.0], "continuous k=0 gets only underclock tiers"
    assert by_grade[1] == [0.5, 0.75, 1.0, 2.0], "integer slooped grade gets the full list"
    check("underclock: continuous k=0 gets <=1.0 tiers, slooped k>=1 gets all")


def test_minimize_machines_tiebreak() -> None:
    # Nothing in the phase-1 objective prices building count, so with power
    # slack "20 bar machines at 50%" ties "10 at 100%" (100 ore -> 100 bar/min
    # either way, same 1000 pts). The machine-count tiebreak must collapse the
    # flat face onto the fewest-buildings plan at the SAME points: 10 @ 100%.
    # Coal is a *non-sinkable* fuel here so it holds no value of its own (a
    # sinkable fuel would rightly trade machines to sink it — see the reduced
    # case this test's assertions guard against).
    cfg = load_example()
    cfg.parameters.somersloop_budget = 0.0
    cfg.parameters.overclock_tiers = [0.5, 1.0]
    cfg.recipes.clear()
    cfg.machines["constructor"] = MachineSpec(power_draw=4.0, max_sloops=0, overclockable=True)
    cfg.recipes.append(
        Recipe(id="bar", name="Bar", machine="constructor",
               inputs={"ore": 10.0}, outputs={"bar": 10.0})
    )
    cfg.items["bar"] = Item("bar", "Bar", sinkable=True, points=10.0)
    cfg.items["coal"] = Item("coal", "Coal", sinkable=False)  # pure fuel, no sink value
    cfg.recipes.append(
        Recipe(id="coal_power", name="Coal Power", machine="generator",
               inputs={"coal": 15.0}, outputs={"power": 75.0})
    )
    cfg.parameters.resources = {"ore": 100.0, "coal": 15.0}

    prob = build_problem(cfg, n_augmenters=0)
    phase1 = solve(prob)
    # Power must NOT be what caps bar: the ore supply (100/min) binds first.
    assert phase1.sinks["bar"] == 100.0, "ore cap should bind; power has slack"
    tied = solve(prob, minimize_machines=phase1.objective)
    assert abs(tied.objective - phase1.objective) < 1e-6, "tiebreak keeps the same points/min"

    def total_machines(sol) -> float:
        return sum(v for (r, k, c), v in sol.activities.items() if v > 0.0)

    assert total_machines(tied) <= total_machines(phase1) + 1e-9
    # Theoretical minimum for the *bar* recipe: 100 ore @ 10 ore/machine = 10
    # machine-equivalents, all clocked at the highest available c (1.0).
    # (Generators add their own ~0.5 machine-equivalents' worth of power, so we
    # count bar alone here.)
    def for_recipe(sol, c=None) -> float:
        total = 0.0
        for (r, k, clk), v in sol.activities.items():
            if sol.problem.config.recipes[r].id != "bar" or v <= 0.0:
                continue
            if c is None or clk == c:
                total += v
        return total

    assert abs(for_recipe(tied) - 10.0) < 1e-3, (
        f"fewest-machines bar plan should be 10 @100%, got {for_recipe(tied)}"
    )
    assert abs(for_recipe(tied, c=1.0) - 10.0) < 1e-3, (
        "bulk with power slack must be clocked at 100%, not 50%"
    )
    check("tiebreak: fewest machines at equal points (10@100% beats 20@50%) under power slack")


def test_tiebreak_keeps_underclock_when_power_binds() -> None:
    # Under a HARD power cap the fewest-machine tiebreak must NOT undo the
    # underclock: re-clocking to 100% is infeasible there, so the solver has to
    # stay on 50% to fit output in the power budget (that is exactly when
    # underclock pays). Same setup as test_underclock_power_efficiency.
    cfg = load_example()
    cfg.parameters.somersloop_budget = 0.0
    cfg.parameters.overclock_tiers = [0.5, 1.0]
    cfg.recipes.clear()
    cfg.machines["constructor"] = MachineSpec(power_draw=20.0, max_sloops=0, overclockable=True)
    cfg.recipes.append(
        Recipe(id="bar", name="Bar", machine="constructor",
               inputs={"ore": 10.0}, outputs={"bar": 10.0})
    )
    cfg.recipes.append(
        Recipe(id="coal_power", name="Coal Power", machine="generator",
               inputs={"coal": 15.0}, outputs={"power": 75.0})
    )
    cfg.items["bar"] = Item("bar", "Bar", sinkable=True, points=10.0)
    cfg.items["coal"] = Item("coal", "Coal", sinkable=False)  # pure fuel, no sink value
    cfg.parameters.resources = {"ore": 100.0, "coal": 15.0}

    prob = build_problem(cfg, n_augmenters=0)
    phase1 = solve(prob)
    assert phase1.sinks["bar"] > 40.0, "underclock beats the power-linear optimum (~46.7 vs 37.5)"
    tied = solve(prob, minimize_machines=phase1.objective)
    assert abs(tied.objective - phase1.objective) < 1e-6, "same points/min"
    assert tied.sinks["bar"] > 40.0, "tiebreak must not un-underclock a power-bound optimum"
    assert tied.power_consumed <= tied.power_available + 1e-6
    check("tiebreak: power-bound optimum stays underclocked (fewest machines can't re-clock)")


def test_tiebreak_does_not_trade_points_for_machines() -> None:
    # Coal is sinkable in-game (3 pts). Over-producing power wastes coal that
    # could be sunk, so the point-maximising plan underclocks the bar line and
    # *sinks the leftover fuel* — earning real points. The fewest-machine
    # tiebreak must NOT compress that away: lexicographic means points always
    # win over building count (compressing to 10@100% would forfeit ~25-30
    # pts/min of coal-sink value).
    cfg = load_example()
    cfg.parameters.somersloop_budget = 0.0
    cfg.parameters.overclock_tiers = [0.5, 1.0]
    cfg.recipes.clear()
    cfg.machines["constructor"] = MachineSpec(power_draw=4.0, max_sloops=0, overclockable=True)
    cfg.recipes.append(
        Recipe(id="bar", name="Bar", machine="constructor",
               inputs={"ore": 10.0}, outputs={"bar": 10.0})
    )
    cfg.items["bar"] = Item("bar", "Bar", sinkable=True, points=10.0)
    # keep the fixture's sinkable coal @ 3 pts -> raw-sink column exists
    cfg.recipes.append(
        Recipe(id="coal_power", name="Coal Power", machine="generator",
               inputs={"coal": 15.0}, outputs={"power": 75.0})
    )
    cfg.parameters.resources = {"ore": 100.0, "coal": 15.0}

    prob = build_problem(cfg, n_augmenters=0)
    phase1 = solve(prob)
    assert phase1.raw_sinks.get("coal", 0.0) > 5.0, (
        "optimum should sink surplus coal, not burn it all for power"
    )
    tied = solve(prob, minimize_machines=phase1.objective)
    assert abs(tied.objective - phase1.objective) < 1e-6, "same points/min"

    def bar_at(sol, c=None) -> float:
        total = 0.0
        for (r, k, clk), v in sol.activities.items():
            if sol.problem.config.recipes[r].id != "bar" or v <= 0.0:
                continue
            if c is None or clk == c:
                total += v
        return total

    # 10 @ 100% would burn far more coal (no sink value) -> ~1021 pts < 1025.8.
    # The tiebreak must keep the underclocked / fuel-sinking plan instead (bar
    # stays well above 10 machine-equivalents and not all at c=1.0).
    assert bar_at(tied) > 15.0, f"tiebreak must not compress away coal-sink value ({bar_at(tied)})"
    assert bar_at(tied, c=1.0) < bar_at(tied) - 1.0, "bar must stay partly underclocked"
    # And the phase-2 solution must not leave a phantom clock sliver (0.02 @
    # 100% beside 19.96 @ 50% would report as ceil=1 extra machine): the
    # consolidation pass folds it into the dominant 50% column -> one clean row.
    bar_cols = sorted({
        c for (r, k, c), v in tied.activities.items()
        if v > 0.0 and tied.problem.config.recipes[r].id == "bar"
    })
    assert bar_cols == [0.5], f"bar must consolidate onto one clock, got {bar_cols}"
    assert abs(bar_at(tied) - 20.0) < 1e-3, f"bar should fold to exactly 20 @ 50%, got {bar_at(tied)}"
    check("tiebreak: points beat machines — sinkable fuel blocks over-aggressive compression"
          " (and clock slivers are consolidated away)")


def test_machine_specs_load_from_files() -> None:
    import tempfile

    from factory_optimiser.io_config import load_machines

    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "alpha.json").write_text(
            '{"id": "alpha", "name": "Alpha", "power_draw": 7.5, "max_sloops": 2}'
        )
        (Path(tmp) / "sub").mkdir()
        (Path(tmp) / "sub" / "beta.json").write_text('{"id": "beta", "name": "Beta"}')
        machines = load_machines(tmp)  # recursive, sorted
        assert set(machines) == {"alpha", "beta"}
        assert machines["alpha"].name == "Alpha"
        assert machines["alpha"].power_draw == 7.5
        assert machines["alpha"].max_sloops == 2
        assert machines["beta"].power_draw == 0.0     # defaults applied
        assert machines["beta"].max_sloops == 3
    check("load_machines: specs load recursively, fields + defaults correct")


def test_items_load_from_files() -> None:
    import tempfile

    from factory_optimiser.io_config import load_items

    # Recursive + sorted, one item per file, defaults applied, and files whose
    # name starts with "_" are ignored (handy for templates/notes).
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "iron_ore.json").write_text(
            '{"id": "iron_ore", "name": "Iron Ore", "sinkable": false, "sink_points": 0}'
        )
        (Path(tmp) / "sub").mkdir()
        (Path(tmp) / "sub" / "bar.json").write_text('{"id": "bar"}')
        (Path(tmp) / "_template.json").write_text(
            '{"id": "should_be_ignored", "name": "Tpl", "sinkable": false}'
        )
        items = load_items(tmp)
        assert set(items) == {"iron_ore", "bar"}, "underscore-prefixed file must be ignored"
        assert items["iron_ore"].name == "Iron Ore"
        assert items["iron_ore"].sinkable is False
        assert items["bar"].sinkable is True   # defaults
        assert items["bar"].points == 0.0      # defaults

    # Duplicate item id across files is a hard error.
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "a.json").write_text('{"id": "dup"}')
        (Path(tmp) / "b.json").write_text('{"id": "dup"}')
        try:
            load_items(tmp)
            raise AssertionError("duplicate item id should raise ConfigError")
        except ConfigError:
            pass
    check("load_items: one file per item, recursive, defaults, '_'-files ignored, dup id errors")


def test_consistency_check_and_cli_gate() -> None:
    # The audit must be silent on a consistent config...
    from factory_optimiser.consistency import check_config

    cfg = load_example()
    assert not check_config(cfg), "baseline example config must audit clean"

    # ...but flag a recipe on an unknown machine type as an error.
    cfg2 = load_example()
    cfg2.recipes[0] = Recipe(
        id="bar", name="Bar", machine="nonexistent",
        inputs={"ore": 30.0}, outputs={"bar": 30.0},
    )
    codes = {i.code for i in check_config(cfg2) if i.severity == "error"}
    assert "unknown-machine" in codes

    # ...and an item referenced but missing from the items config.
    cfg3 = load_example()
    cfg3.recipes.append(
        Recipe(id="mystery", name="Mystery", machine="constructor",
               inputs={"ore": 1.0}, outputs={"mystery_item": 1.0})
    )
    codes = {i.code for i in check_config(cfg3) if i.severity == "error"}
    assert "missing-item" in codes

    # The CLI gate: 'check' runs the audit and exits 0 on the real project data.
    env = dict(os.environ, PYTHONPATH=str(ROOT))
    py = str(ROOT / ".venv" / "bin" / "python")
    proc = subprocess.run([py, "main.py", "check"], env=env, capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    assert "consistency check" in proc.stdout
    check("consistency: check_config flags errors; CLI 'check' gate exits 0 on clean data")


if __name__ == "__main__":
    test_milp_basic()
    test_scarcity_routing()
    test_power_balance()
    test_augmenter_flat_power()
    test_augmenter_sweep_deterministic()
    test_dominated_recipe_unused()
    test_downconvert_includes_grade_multiplier()
    test_sloop_multipliers_confirmed_formula()
    test_machine_cap_enforced()
    test_power_draw_inherited_from_machine_type()
    test_extractor_recipe_bounds_supply()
    test_overclock_slooped_machine()
    test_overclock_power_factor()
    test_overclock_extractor_breaks_cap()
    test_non_overclockable_machine_fixed()
    test_overclock_config_defaults_and_loader()
    test_overclock_consistency_checks()
    test_underclock_power_efficiency()
    test_underclock_tier_attachment()
    test_minimize_machines_tiebreak()
    test_tiebreak_keeps_underclock_when_power_binds()
    test_tiebreak_does_not_trade_points_for_machines()
    test_machine_specs_load_from_files()
    test_items_load_from_files()
    test_consistency_check_and_cli_gate()
    test_cli_launcher_and_json()
    print(f"\nAll {_CHECKS} smoke checks passed.")
