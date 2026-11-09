"""Solver wrapper: solve a built MILP and read back the flows (Design.md §9)."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from scipy.optimize import milp

from .io_config import POWER_ITEM
from .model import EPS, Problem


class SolveError(RuntimeError):
    pass


@dataclass
class Solution:
    """Read-back of one solved problem (fixed augmenter count)."""

    problem: Problem
    status: int
    message: str
    objective: float                  # sink points per minute
    activities: dict[tuple[int, int], float]  # (recipe_idx, grade) -> machines (sum of clock/share)
    sinks: dict[str, float]           # produced item -> items/min sent to the sink
    raw_sinks: dict[str, float]       # raw item -> items/min extracted and sunk
    power_consumed: float = 0.0       # MW
    power_generated: float = 0.0      # MW (base generator output, pre-multiplier)
    sloops_used: float = 0.0
    solve_seconds: float = 0.0

    @property
    def power_available(self) -> float:
        """Deliverable capacity (MW) seen by consumers = base * m(N)."""
        return self.power_generated * self.problem.power_multiplier

    @property
    def n_augmenters(self) -> int:
        return self.problem.n_augmenters


def solve(problem: Problem, *, time_limit: float = 30.0) -> Solution:
    """Solve the MILP and return a read-back Solution.

    Raises :class:`SolveError` if HiGHS does not reach an optimal (or at least
    feasible / time-limited) solution.
    """
    import time

    from scipy.optimize import OptimizeResult

    start = time.perf_counter()
    result: OptimizeResult = milp(
        c=problem.c,
        constraints=problem.constraints,
        integrality=problem.integrality,
        bounds=problem.bounds,
        options={"time_limit": time_limit, "mip_rel_gap": 1e-6},
    )
    elapsed = time.perf_counter() - start

    if result.status != 0:
        raise SolveError(
            f"HiGHS failed (status {result.status}) at N={problem.n_augmenters}: {result.message}"
        )
    if result.x is None:
        raise SolveError(f"HiGHS returned no solution at N={problem.n_augmenters}")

    x = np.asarray(result.x)
    config = problem.config

    activities: dict[tuple[int, int], float] = {}
    for (r, k), col in problem.activity_col.items():
        val = float(x[col])
        activities[(r, k)] = val if abs(val) > EPS else 0.0

    sinks: dict[str, float] = {}
    for item, col in problem.sink_col.items():
        val = float(x[col])
        sinks[item] = val if abs(val) > EPS else 0.0

    raw_sinks: dict[str, float] = {}
    for item, col in problem.raw_sink_col.items():
        val = float(x[col])
        raw_sinks[item] = val if abs(val) > EPS else 0.0

    # True objective = sum of actual sink points, recomputed from flows (the
    # solver's objective carried a 1e-9 tie-break perturbation, so -result.fun
    # is not the number we report).
    objective = 0.0
    for item, rate in sinks.items():
        objective += config.items[item].points * rate
    for item, rate in raw_sinks.items():
        objective += config.items[item].points * rate

    # Power accounting (recomputed from activities for reporting).
    # power_generated is BASE generator output (pre-augmenter); the deliverable
    # capacity seen by consumers is base * power_multiplier (Design.md §6).
    power_consumed = 0.0
    power_generated = 0.0
    power_draw_cache = _power_draw_rates(problem)
    for (r, k), val in activities.items():
        if val <= 0.0:
            continue
        recipe = config.recipes[r]
        grade = config.parameters.sloop_grades[k]
        power_generated += grade.rho * recipe.outputs.get(POWER_ITEM, 0.0) * val
        power_consumed += grade.pi * power_draw_cache[r] * val

    sloops_used = sum(k * v for (r, k), v in activities.items())
    return Solution(
        problem=problem,
        status=result.status,
        message=str(result.message),
        objective=objective,
        activities=activities,
        sinks=sinks,
        raw_sinks=raw_sinks,
        power_consumed=power_consumed,
        power_generated=power_generated,
        sloops_used=sloops_used,
        solve_seconds=elapsed,
    )


def _power_draw_rates(problem: Problem) -> dict[int, float]:
    """Per-recipe base power draw (MW at 100% clock), resolved against machine defaults."""
    config = problem.config
    rates: dict[int, float] = {}
    for r, recipe in enumerate(config.recipes):
        if recipe.power_draw:
            rates[r] = recipe.power_draw
        else:
            spec = config.parameters.machines.get(recipe.machine)
            rates[r] = spec.power_draw if spec is not None else 0.0
    return rates
