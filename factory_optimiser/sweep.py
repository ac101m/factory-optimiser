"""Sweep harness: Alien Power Augmenters (Design.md §6) and marginal analysis.

Because a MILP has no well-defined shadow prices (integrality breaks marginal
continuity), marginal values are computed from **sweep deltas** (Design.md §3):
empirical points/min per extra augmenter / Somersloop / unit of map resource.
"""

from __future__ import annotations

from dataclasses import dataclass

from .io_config import Config
from .model import build_problem
from .solve import Solution, solve


@dataclass
class AugResult:
    """Outcome of one full solve at a fixed augmenter count N."""

    n_augmenters: int
    sloop_budget: float
    power_multiplier: float
    flat_power_mw: float   # N * augmenters.power_mw (bonus does not apply to it)
    solution: Solution
    solve_seconds: float

    @property
    def points_per_min(self) -> float:
        return self.solution.objective


def sweep_augmenters(
    config: Config,
    max_augmenters: int | None = None,
    *,
    time_limit: float = 30.0,
) -> list[AugResult]:
    """Solve for every affordable N; N = 0..floor(S_total / cost)."""
    params = config.parameters
    cost = params.augmenters.cost
    if max_augmenters is None:
        if params.augmenters.max is not None:
            max_augmenters = params.augmenters.max
        else:
            max_augmenters = max(0, int(params.somersloop_budget // cost))
    else:
        max_augmenters = min(max_augmenters, max(0, int(params.somersloop_budget // cost)))

    results: list[AugResult] = []
    for n in range(0, max_augmenters + 1):
        problem = build_problem(config, n_augmenters=n)
        sol = solve(problem, time_limit=time_limit)
        results.append(
            AugResult(
                n_augmenters=n,
                sloop_budget=problem.sloop_budget,
                power_multiplier=problem.power_multiplier,
                flat_power_mw=problem.flat_power_mw,
                solution=sol,
                solve_seconds=sol.solve_seconds,
            )
        )
    return results


def best_augmenter(
    config: Config,
    max_augmenters: int | None = None,
    *,
    time_limit: float = 30.0,
) -> AugResult:
    """Best augmenter count; ties resolve toward fewer augmenters (keeps sloops
    available for production machines)."""
    best: AugResult | None = None
    for result in sweep_augmenters(config, max_augmenters, time_limit=time_limit):
        if best is None or result.points_per_min > best.points_per_min + 1e-6:
            best = result
    assert best is not None
    return best


def sweep_somersloops(
    config: Config,
    budgets: list[float],
    *,
    time_limit: float = 30.0,
) -> list[tuple[float, float]]:
    """Marginal-value curve: total Somersloop budget -> best points/min.

    The augmenter count is re-optimised for every budget, so the curve reflects
    the best use of each additional Somersloop.
    """
    curve: list[tuple[float, float]] = []
    for budget in budgets:
        best = 0.0
        params = config.parameters
        max_n = max(0, int(budget // params.augmenters.cost))
        for n in range(0, max_n + 1):
            problem = build_problem(
                config, n_augmenters=n, sloop_budget=budget - params.augmenters.cost * n
            )
            sol = solve(problem, time_limit=time_limit)
            best = max(best, sol.objective)
        curve.append((budget, best))
    return curve


def sweep_resource(
    config: Config,
    item: str,
    caps: list[float],
    *,
    time_limit: float = 30.0,
) -> list[tuple[float, float]]:
    """Marginal-value curve of one map resource: cap R -> best points/min.

    Applies to the optional ``resources`` table only. The canonical way to
    model map availability is extractor recipes (see :func:`sweep_extractor_nodes`).
    """
    curve: list[tuple[float, float]] = []
    for cap in caps:
        old = config.parameters.resources.get(item)
        config.parameters.resources[item] = cap
        try:
            curve.append((cap, best_augmenter(config, time_limit=time_limit).points_per_min))
        finally:
            if old is None:
                del config.parameters.resources[item]
            else:
                config.parameters.resources[item] = old
    return curve


def extractor_recipes(config: Config) -> list[int]:
    """Indices of *extractor* recipes: no material inputs (miners, pumps, ...).

    These are how raw map resources are created in the recipes model: each
    node purity is one recipe whose ``max_machines`` is the node count.
    """
    return [r for r, recipe in enumerate(config.recipes) if not recipe.inputs]


def sweep_extractor_nodes(
    config: Config,
    *,
    time_limit: float = 30.0,
) -> list[tuple[int, float, float, float]]:
    """Marginal value of one extra node of each extractor recipe.

    Returns ``(recipe_idx, base_cap, points_at_base, points_at_base_plus_one)``.
    This is the resource marginal curve under the miner-recipe model — "which
    node should I expand next?".
    """
    import dataclasses

    out: list[tuple[int, float, float, float]] = []
    for r in extractor_recipes(config):
        recipe = config.recipes[r]
        if recipe.max_machines is None:
            continue  # uncapped extractor: "add a node" is meaningless
        base_pts = best_augmenter(config, time_limit=time_limit).points_per_min
        bumped_recipe = dataclasses.replace(recipe, max_machines=recipe.max_machines + 1)
        config.recipes[r] = bumped_recipe
        try:
            bumped = best_augmenter(config, time_limit=time_limit).points_per_min
        finally:
            config.recipes[r] = recipe
        out.append((r, recipe.max_machines, base_pts, bumped))
    return out
