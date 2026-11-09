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

from factory_optimiser.io_config import Config, Item, Parameters, Grade, Recipe, MachineSpec, Augmenters  # noqa: E402
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
            "coal": Item("coal", "Coal", sinkable=True, points=6.0),
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
            sloop_grades={0: Grade(1, 1, 1), 1: Grade(2, 2, 1), 2: Grade(4, 4, 1), 3: Grade(8, 8, 1)},
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
    # max_machines=1 forces the use of sloops to get past the cap: a k=3
    # machine makes 8x the base output, so 80/min from 80 ore.
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
    # one k=3 machine: 8x the base 10/min base output = 80/min
    assert abs(m.outputs["bar"] - 80.0) < 1e-6
    check("downconvert: output throughput scaled by grade rho")


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
    assert data["best"]["n_augmenters"] == 0
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
    used = {cfg.recipes[r].id: v for (r, k), v in sol.activities.items() if v > 1e-9}
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
    test_augmenter_sweep_deterministic()
    test_dominated_recipe_unused()
    test_downconvert_includes_grade_multiplier()
    test_machine_cap_enforced()
    test_power_draw_inherited_from_machine_type()
    test_extractor_recipe_bounds_supply()
    test_machine_specs_load_from_files()
    test_consistency_check_and_cli_gate()
    test_cli_launcher_and_json()
    print(f"\nAll {_CHECKS} smoke checks passed.")
