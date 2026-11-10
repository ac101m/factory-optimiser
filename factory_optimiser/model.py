"""Build the MILP described in Design.md §5.

Variables
    x[r][k][c] : machines running recipe r with exactly k Somersloops (k = 0..K_r)
                 at clock c (c in the overclock tier list; see below)
    s[i]       : sink flow of item i (items/min sent to the AWESOME sink)

Overclocking (Design.md §8): a machine at clock c (c = clock/100) has
    output  c * rho(k) * beta
    input   c * kappa(k) * alpha
    power   c^1.321928 * pi(k) * draw       (game power curve, x sloop pi)
Clock choice enters as discrete *tiers* — one column per available clock value
— so the model stays an exact MILP (no machines x clock bilinearity). Which
machines are clockable and which clock values exist are config:
`overclockable` in machines/*.json + the `overclock.tiers` parameter. Clock
tiers attach to every grade of an overclockable machine: integer slooped
grades (k >= 1) — the sloop-efficiency lever; the sole grade of 0-slot machines
(extractors, e.g. miners) — the node-cap-breaker; and the continuous k=0 grade
of slot machines. Overclocking that continuous grade never raises the phase-1
point optimum (same output at more power), but the fewest-machines tiebreak
(Design.md §10) uses it to shrink building counts wherever power has slack;
when power binds the power row rejects the high clocks automatically.

Constraints
    item balance  : sum_r sum_k sum_c (c*rho_k*beta - c*kappa_k*alpha) * x = s >= 0
    resource caps : sum ... c*kappa_k*alpha[raw] * x <= R[raw]
    sloop budget  : sum ... k * x <= sloop_budget        (clock doesn't change it)
    power balance : sum (m(N)*c*rho_k*beta_power - c^1.321928*pi_k*power_draw) * x >= -N*W
                    (N*W = flat MW each augmenter generates; bonus doesn't apply)
    machine caps  : sum_k sum_c x[r][k][c] <= max_machines  (clock doesn't change it)

Objective
    maximize sum_i p[i] * s[i]   (implemented as minimize of the negation,
    with a tiny deterministic tie-break perturbation on p).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.optimize import Bounds, LinearConstraint

from .io_config import (
    Config,
    CLOCK_POWER_EXP,
    Grade,
    POWER_ITEM,
    sloop_multipliers,
)

#: Below this, an activity is treated as "not used" when reading back.
EPS = 1e-9


@dataclass
class Problem:
    """A fully-assembled MILP instance (one fixed augmenter count N)."""

    config: Config
    n_augmenters: int
    power_multiplier: float
    sloop_budget: float
    flat_power_mw: float        # N * augmenters.power_mw, free flat MW

    c: np.ndarray            # objective (minimize): -effective sink points
    integrality: np.ndarray  # 1 = integer variable
    bounds: Bounds
    constraints: list[LinearConstraint]

    n_activity: int          # first n_activity columns are machine activities
    #: (recipe_idx, grade, clock) -> column. Grades are k Somersloops; clock
    #: is the machine clock as a multiple of 100% (1.0 = base, 2.5 = 250%).
    activity_col: dict[tuple[int, int, float], int]
    sink_col: dict[str, int]                  # produced item -> column (sinkable only)
    raw_sink_col: dict[str, int]              # raw sinkable item -> column (sink via cap)
    has_power: bool          # whether the power-balance constraint is active


def build_problem(
    config: Config,
    *,
    n_augmenters: int = 0,
    sloop_budget: float | None = None,
    power_multiplier: float | None = None,
) -> Problem:
    """Build the MILP for a fixed augmenter count.

    ``sloop_budget`` defaults to the global budget minus the augmenters' cost;
    ``power_multiplier`` defaults to m(N) = 1 + bonus*N (Design.md §6).
    """
    params = config.parameters
    if sloop_budget is None:
        sloop_budget = params.somersloop_budget - params.augmenters.cost * n_augmenters
    if power_multiplier is None:
        power_multiplier = 1.0 + params.augmenters.bonus * n_augmenters
    flat_power_mw = n_augmenters * params.augmenters.power_mw

    recipes = config.recipes
    activity_seq, uses_power = _gather_machine_columns(config)

    # -- variables -----------------------------------------------------------
    activity_col: dict[tuple[int, int, float], int] = {}
    sink_col: dict[str, int] = {}
    objective: list[float] = []
    integrality: list[int] = []

    for (r, k, clk) in activity_seq:
        activity_col[(r, k, clk)] = len(integrality)
        objective.append(0.0)  # activities contribute to points only via sinks
        integrality.append(1 if k >= 1 else 0)  # Design.md §5.3 integrality
    for idx, item in enumerate(_sinkable_produced(config)):
        sink_col[item] = len(integrality)
        points = config.items[item].points
        # Deterministic tie-break: scale points by a tiny, stable factor per item
        # so that alternative optima resolve reproducibly (Design.md §10).
        objective.append(-points * (1.0 + 1e-9 * (idx + 1)))
        integrality.append(0)
    # Raw (non-produced) sinkable items: allow extracting them straight into the
    # sink. Each such item must have a map cap (otherwise unbounded points).
    # t[i] (items/min sunk) counts against the item's resource cap, so it
    # competes with recipes for the same map availability.
    produced_set = set(config.produced_items)
    raw_sink_items = [
        i for i in params.resources
        if i not in produced_set and i != POWER_ITEM and config.is_sinkable(i)
    ]
    raw_sink_col: dict[str, int] = {}
    for idx, item in enumerate(raw_sink_items):
        raw_sink_col[item] = len(integrality)
        points = config.items[item].points
        objective.append(-points * (1.0 + 1e-9 * (len(sink_col) + idx + 1)))
        integrality.append(0)

    n_vars = len(integrality)
    c = np.array(objective, dtype=float)
    integrality_arr = np.array(integrality, dtype=np.int8)

    # -- constraints ---------------------------------------------------------
    rows: list[np.ndarray] = []
    rows_lb: list[float] = []
    rows_ub: list[float] = []
    row_names: list[str] = []

    def add_row(row: dict[int, float], lb: float, ub: float, name: str) -> None:
        if not row:
            return
        arr = np.zeros(n_vars)
        for col, val in row.items():
            arr[col] = val
        rows.append(arr)
        rows_lb.append(lb)
        rows_ub.append(ub)
        row_names.append(name)

    recipes_by_idx = list(enumerate(recipes))
    produced = set(config.produced_items)

    def mult(r: int, k: int) -> Grade:
        """Sloop multipliers for recipe r at grade k (depends on the machine's slots)."""
        return sloop_multipliers(k, config.max_sloops_for(recipes[r].machine))

    # 1) Item material balance (one row per produced item, power excluded).
    for item in sorted(produced):
        row: dict[int, float] = {}
        for (r, k, clk) in activity_seq:
            grade = mult(r, k)
            rho_beta = grade.rho * recipes[r].outputs.get(item, 0.0)
            kappa_alpha = grade.kappa * recipes[r].inputs.get(item, 0.0)
            net = clk * (rho_beta - kappa_alpha)
            if net != 0.0:
                row[activity_col[(r, k, clk)]] = row.get(activity_col[(r, k, clk)], 0.0) + net
        if config.is_sinkable(item):
            # sum(net) - s[i] = 0, s[i] >= 0  (surplus flows into the sink)
            row[sink_col[item]] = row.get(sink_col[item], 0.0) - 1.0
            add_row(row, lb=0.0, ub=0.0, name=f"balance:{item}")
        else:
            # Can't sink; surplus may be wasted (net production >= 0).
            add_row(row, lb=0.0, ub=np.inf, name=f"balance:{item}(waste)" )

    # 2) Map resource limits. Sinking raw item i consumes t[i] of its cap.
    for item, cap in params.resources.items():
        row = {}
        for (r, k, clk) in activity_seq:
            grade = mult(r, k)
            rate = clk * grade.kappa * recipes[r].inputs.get(item, 0.0)
            if rate != 0.0:
                row[activity_col[(r, k, clk)]] = row.get(activity_col[(r, k, clk)], 0.0) + rate
        if item in raw_sink_col:
            row[raw_sink_col[item]] = row.get(raw_sink_col[item], 0.0) + 1.0
        add_row(row, lb=-np.inf, ub=cap, name=f"resource:{item}")

    # 3) Global Somersloop budget (clock doesn't change sloop usage).
    row = {activity_col[(r, k, clk)]: float(k) for (r, k, clk) in activity_seq if k > 0}
    add_row(row, lb=-np.inf, ub=sloop_budget, name="sloop_budget")

    # 4) Power balance (only when power appears anywhere):
    #    consumption <= m(N)*generation + N*W,
    #    where W = augmenters.power_mw is the flat MW each augmenter produces
    #    itself (the bonus m(N) does NOT apply to W). For a fixed N, N*W is a
    #    constant, so it only shifts the row's lower bound.
    #    Generators: +m(N)*c*rho(k)*output.  Consumers: -c^1.321928*pi(k)*power_draw.
    #    A configurable generation "overproduction" (Parameters.power_overproduction)
    #    multiplies the consumer draw so the grid must deliver (1+f)*load — the
    #    plan keeps that much overproduced capacity as reserve instead of
    #    running at exactly 100%.
    if uses_power:
        row = {}
        overprod = 1.0 + config.parameters.power_overproduction
        for (r, k, clk) in activity_seq:
            grade = mult(r, k)
            gen = power_multiplier * (clk * grade.rho) * recipes[r].outputs.get(POWER_ITEM, 0.0)
            draw = overprod * (clk ** CLOCK_POWER_EXP) * grade.pi * config.power_draw_for(recipes[r])
            val = gen - draw
            if val != 0.0:
                row[activity_col[(r, k, clk)]] = row.get(activity_col[(r, k, clk)], 0.0) + val
        add_row(row, lb=-flat_power_mw, ub=np.inf, name="power")

    # 5) Optional per-recipe machine caps (clock doesn't change machine count).
    for r, recipe in recipes_by_idx:
        if recipe.max_machines is not None:
            row = {activity_col[(rc, k, clk)]: 1.0 for (rc, k, clk) in activity_seq if rc == r}
            add_row(row, lb=-np.inf, ub=recipe.max_machines, name=f"cap:{recipe.id}")

    constraints = [LinearConstraint(np.stack(rows), rows_lb, rows_ub)] if rows else []

    return Problem(
        config=config,
        n_augmenters=n_augmenters,
        power_multiplier=power_multiplier,
        sloop_budget=sloop_budget,
        flat_power_mw=flat_power_mw,
        c=c,
        integrality=integrality_arr,
        bounds=Bounds(np.zeros(n_vars), np.full(n_vars, np.inf)),
        constraints=constraints,
        n_activity=len(activity_col),
        activity_col=activity_col,
        sink_col=sink_col,
        raw_sink_col=raw_sink_col,
        has_power=uses_power,
    )


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _sinkable_produced(config: Config) -> list[str]:
    return [i for i in config.produced_items if config.is_sinkable(i)]


def _grades(config: Config, r: int) -> list[int]:
    recipe = config.recipes[r]
    return list(range(config.max_sloops_for(recipe.machine) + 1))


def _clocks_for(config: Config, machine: str, k: int) -> list[float]:
    """Clock values available to grade k of a machine type.

    Overclockable machines may run at ANY configured tier on every grade. The
    tier list spans below-100% (underclocking — a convex power curve makes
    underclocked machines more power-efficient per unit) and above-100%
    (overclocking up to the 250% game cap). Overclocking an un-slooped machine
    does not raise the point optimum (same output at more power), but the
    fewest-machines tiebreak (Design.md §10) uses it to cut building counts
    wherever power has slack. Power shards are craftable in current
    Satisfactory, so their cost is not modeled: overclocking is free and the
    power row alone decides whether the high clocks are worth their draw.
    Non-overclockable machines (e.g. geothermal) are fixed at base clock for
    every grade.
    """
    if not config.is_overclockable(machine):
        return [1.0]
    return list(config.parameters.overclock_tiers)


def _gather_machine_columns(config: Config):
    """Return ([(r, k, c), ...] in column order, uses_power bool)."""
    cols: list[tuple[int, int, float]] = []
    uses_power = False
    for r, recipe in enumerate(config.recipes):
        # Resolved draw (recipe override or machine-type default) PLUS any
        # generator output. Using the resolved value matters: a config whose
        # machines draw power only via their machine type (no explicit
        # power_draw, no generator) must still activate the power constraint.
        if config.power_draw_for(recipe) or recipe.outputs.get(POWER_ITEM, 0.0):
            uses_power = True
        for k in _grades(config, r):
            for clk in _clocks_for(config, recipe.machine, k):
                cols.append((r, k, clk))
    return cols, uses_power
