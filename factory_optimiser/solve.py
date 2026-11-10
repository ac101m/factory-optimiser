"""Solver wrapper: solve a built MILP and read back the flows (Design.md §9)."""

from __future__ import annotations

from dataclasses import dataclass, replace

import numpy as np
from scipy.optimize import LinearConstraint, milp

from .io_config import CLOCK_POWER_EXP, POWER_ITEM, sloop_multipliers
from .model import EPS, Problem


class SolveError(RuntimeError):
    pass


#: Points/min of slack allowed on the phase-2 (machine tiebreak) floor. Far
#: below any meaningful gap in the objective, but larger than HiGHS's numeric
#: feasibility tolerance so the phase-1 optimum is reachable.
MACHINE_FLOOR_TOL = 1e-2


@dataclass
class Solution:
    """Read-back of one solved problem (fixed augmenter count)."""

    problem: Problem
    status: int
    message: str
    objective: float                  # sink points per minute
    #: activities[(r, k, clock)] -> machines running recipe r, grade k (sloops),
    #: at clock `clock` (1.0 = 100%). k>=1 grades are integer by construction.
    activities: dict[tuple[int, int, float], float]
    sinks: dict[str, float]           # produced item -> items/min sent to the sink
    raw_sinks: dict[str, float]       # raw item -> items/min extracted and sunk
    power_consumed: float = 0.0       # MW
    power_generated: float = 0.0      # MW (base generator output, pre-multiplier)
    sloops_used: float = 0.0
    solve_seconds: float = 0.0

    @property
    def power_available(self) -> float:
        """Deliverable capacity (MW) seen by consumers.

        = base generation * m(N) + the flat MW each augmenter generates itself
        (N * augmenters.power_mw, which the bonus m(N) does not apply to).
        """
        return (
            self.power_generated * self.problem.power_multiplier
            + self.problem.flat_power_mw
        )

    @property
    def n_augmenters(self) -> int:
        return self.problem.n_augmenters


def solve(
    problem: Problem,
    *,
    time_limit: float = 30.0,
    minimize_machines: float | None = None,
) -> Solution:
    """Solve the MILP and return a read-back Solution.

    Phase 1 maximizes sink points. When ``minimize_machines`` is given (a
    points/min floor — normally the phase-1 optimum), the plan is resolved
    *lexicographically*: among all plans reaching that floor, return the one
    with the fewest total machines (Design.md §10).

    Why: the phase-1 objective prices output and the constraints price power,
    sloops and supply — but nothing prices *building count*. Wherever power has
    slack, "60 Screw constructs at 50% clock" is then exactly as optimal as
    "30 at 100%" (identical output, only machines and draw differ). In-game
    that is strictly worse (build time, space, belts, UPS). Phase 2 collapses
    such flat faces onto the fewest-buildings plan — e.g. back to 30 at 100% —
    while *retaining* underclocking whenever power genuinely binds (there the
    machine-minimizing high clock is infeasible, so the solver clocks up only
    as far as the power budget allows). Only the plan changes; the reported
    objective stays at the phase-1 floor.

    Raises :class:`SolveError` if HiGHS does not reach an optimal (or at least
    feasible / time-limited) solution in either phase.
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
    _raise_on_failure(problem, result)
    first = _read_back(problem, np.asarray(result.x), elapsed,
                       status=result.status, message=str(result.message))

    if minimize_machines is None:
        return first

    # --- Phase 2: fewest machines among plans at the phase-1 optimum --------
    # Machine count = ceil(activity), so minimizing total activity is the
    # smallest-building tiebreak. Pin the point total at the phase-1 floor with
    # one extra linear row (sum_i points[i] * sink[i] >= floor - tol); the
    # activities' objective coefficients become 1 (0 on sinks).
    config = problem.config
    n_vars = len(problem.c)
    c2 = np.zeros(n_vars)
    for col in problem.activity_col.values():
        c2[col] = 1.0
    pin_row = np.zeros(n_vars)
    for item, col in problem.sink_col.items():
        pin_row[col] = config.items[item].points
    for item, col in problem.raw_sink_col.items():
        pin_row[col] = config.items[item].points
    problem2 = replace(
        problem,
        c=c2,
        constraints=[
            *problem.constraints,
            LinearConstraint(
                pin_row[np.newaxis, :],
                lb=minimize_machines - MACHINE_FLOOR_TOL,
                ub=np.inf,
            ),
        ],
    )
    start2 = time.perf_counter()
    result2: OptimizeResult = milp(
        c=problem2.c,
        constraints=problem2.constraints,
        integrality=problem2.integrality,
        bounds=problem2.bounds,
        options={"time_limit": time_limit, "mip_rel_gap": 1e-6},
    )
    elapsed2 = time.perf_counter() - start2
    _raise_on_failure(problem2, result2)
    sol = _read_back(problem2, np.asarray(result2.x), elapsed + elapsed2,
                     status=result2.status, message=str(result2.message))
    # Fold sub-machine clock slivers (e.g. 0.02 @ 100% beside 19.96 @ 50%) so
    # the reported build shows no whole phantom machines; output and points are
    # unchanged (see _consolidate_clock_slivers).
    sol = _consolidate_clock_slivers(sol)
    # Lexicographic: phase-1 points are THE value; phase-2 only chose the plan.
    sol.objective = first.objective
    return sol


def _raise_on_failure(problem: Problem, result) -> None:
    if result.status != 0:
        raise SolveError(
            f"HiGHS failed (status {result.status}) at N={problem.n_augmenters}: {result.message}"
        )
    if result.x is None:
        raise SolveError(f"HiGHS returned no solution at N={problem.n_augmenters}")


def _read_back(
    problem: Problem,
    x: np.ndarray,
    elapsed: float,
    status: int = 0,
    message: str = "",
) -> Solution:
    """Read a solved variable vector back into a :class:`Solution`."""
    config = problem.config

    activities: dict[tuple[int, int, float], float] = {}
    for (r, k, c), col in problem.activity_col.items():
        val = float(x[col])
        activities[(r, k, c)] = val if abs(val) > EPS else 0.0

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
    # Clock scales generator output linearly but consumer draw by c^1.321928.
    power_consumed, power_generated = _account_power(problem, activities)

    sloops_used = sum(k * v for (r, k, c), v in activities.items())
    return Solution(
        problem=problem,
        status=status,
        message=message,
        objective=objective,
        activities=activities,
        sinks=sinks,
        raw_sinks=raw_sinks,
        power_consumed=power_consumed,
        power_generated=power_generated,
        sloops_used=sloops_used,
        solve_seconds=elapsed,
    )


def _account_power(problem: Problem, activities) -> tuple[float, float]:
    """(power_consumed, power_generated) MW recomputed from a set of activities."""
    config = problem.config
    power_consumed = 0.0
    power_generated = 0.0
    power_draw_cache = _power_draw_rates(problem)
    for (r, k, c), val in activities.items():
        if val <= 0.0:
            continue
        recipe = config.recipes[r]
        grade = sloop_multipliers(k, config.max_sloops_for(recipe.machine))
        power_generated += c * grade.rho * recipe.outputs.get(POWER_ITEM, 0.0) * val
        power_consumed += (c ** CLOCK_POWER_EXP) * grade.pi * power_draw_cache[r] * val
    return power_consumed, power_generated


def _consolidate_clock_slivers(sol: Solution) -> Solution:
    """Fold sub-half-machine clock slivers so the *reported* plan has no phantom machines.

    Phase 2 minimizes total machine-equivalents ``sum(x)``, but the report
    shows ``ceil(x)`` per (r, k, c) column (report.downconvert). At sub-machine
    scale those two diverge: a "0.02 machines @ 100%" sliver next to "19.96 @
    50%" shaves 0.02 equivalents off the LP objective yet *reports* as a whole
    extra machine (ceil(0.02) = 1). We fold such slivers into the grade's
    LOWEST clock column:

    * output is preserved exactly (output = c*rho*beta*x, so x*c = const);
    * power strictly decreases (draw per output grows with clock), so points
      (which price fuel/sink flows, never power) cannot fall and the phase-2
      floor still holds;
    * the sliver's ceil=1 machine goes away, and the fold adds at most one to
      the target column -> reported machines never increase.

    Only the continuous k=0 grade can carry fractional slivers (integer grades
    are exact), and we only fold when there is a dominant (>= 1 machine) column
    to fold into. The reported point total and sink flows are unchanged.
    """
    activities = sol.activities
    if not activities:
        return sol

    by_grade: dict[tuple[int, int], list[tuple[float, float]]] = {}
    for (r, k, c), v in activities.items():
        if k == 0 and v > 0.0:
            by_grade.setdefault((r, k), []).append((c, v))

    for (r, k), cols in by_grade.items():
        lo = min(c for c, _v in cols)
        v_lo = sum(v for c, v in cols if c == lo)
        if v_lo < 1.0:
            continue  # no dominant column to fold into
        folded = False
        for ch, vh in cols:
            if ch == lo or vh >= 0.5:
                continue
            v_lo += vh * (ch / lo)
            del activities[(r, k, ch)]
            folded = True
        if folded:
            activities[(r, k, lo)] = v_lo

    if by_grade:
        power_consumed, power_generated = _account_power(sol.problem, activities)
        sol.power_consumed = power_consumed
        sol.power_generated = power_generated
    return sol


def _power_draw_rates(problem: Problem) -> dict[int, float]:
    """Per-recipe base power draw (MW at 100% clock), resolved against machine defaults."""
    config = problem.config
    return {r: config.power_draw_for(recipe) for r, recipe in enumerate(config.recipes)}
