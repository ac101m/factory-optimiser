# Satisfactory Sink-Point Factory Optimizer — Design

## 1. Goal & scope

Given Satisfactory recipes, map resource limits, total Somersloop count, and Alien Power Augmenter behavior, output the **optimal build plan** (machine counts per recipe, Somersloop allocation, clock %) that **maximizes AWESOME sink points per minute**.
**In scope:** flow/throughput optimization — how many machines per recipe, and how to split Somersloops between production machines, power generators, and Alien Power Augmenters.
**Out of scope (decided):** spatial layout, belt routing, machine placement, electrical-grid separation. If that ever enters scope, it is NP-hard and _then_ a GA/local search would be justified — not now.

## 2. Central architectural decision: NO genetic algorithm

The original instinct was a GA. This is a flow/throughput planning problem — convex and linear — so it is solved **exactly and globally by a single MILP**. The GA is unnecessary.
Rationale (preserve this — an agent might otherwise "reintroduce" a GA):

*   Every flow relationship (a machine with k sloops at clock c does c× of each input/output) is linear in a single per-recipe scalar.
    
*   Map resource limits, power balance, item conservation, and sink flows are all linear constraints.
    
*   Total sink points is a linear objective.
    
*   Max of a linear objective over a linear (convex) feasible region → optimum at a vertex, found in milliseconds at Satisfactory scale (a few hundred items/recipes), deterministic, no tuning.
    
*   The GA is redundant _because_ the LP already allocates flow optimally; an outer GA layer choosing caps cannot improve a globally optimal solution.
    

## 3. Language & solver choice (decided at design close)

**Python**, not Rust. Rationale: Rust was chosen for thousands of parallel GA runs; there is no GA now, and a single MILP solves in milliseconds.

*   Examples: Sweeps are only ~5–10 solves → trivially handleable; no need for rayon.
    
*   **Solver:** `scipy.optimize.milp` is HiGHS under the hood (since SciPy 1.9) → same solver quality as a hand-wrapped Rust binding, with far less plumbing. Dependencies collapse to `scipy` + `numpy`.
    
*   Parallel sweeps (if ever needed): `concurrent.futures.ProcessPoolExecutor` over independent solve instances.
    
*   **Shadow-price caveat (important):** MIPs don't have well-defined duals/shadow prices because integrality breaks marginal-value continuity. For marginal analysis, use **sweep deltas** (empirical marginal-value curves) — the primary approach anyway. If numeric duals are wanted for a continuous relaxation, use `highspy` directly to read LP-relaxation duals. Sweeps over N (augmenters) / total sloops / resource caps are the robust path.
    

## 4. Core data model

*   **Items** and **recipes** are plain indices (labels only for reporting).
    
*   Each recipe has per-machine input rates α and output rates β (items/min) for base (unmodified) operation.
    
*   Machine-count caps per recipe are optional; by default recipes are limited only by map resources.
    
*   Two recipes may produce the same item; the solver may freely split production across them (legal in-game, strictly beneficial). **No "pick one variant per item" binaries needed** — dominated recipes are automatically unused.
    

## 5. Formal MILP model

### 5.1 Variables

*   `x[r][k]` — machines running recipe r with exactly k Somersloops, k = 0..K (K = max sloops per building, typically 3 — parameterize per machine/generator type).
    
*   `s[i]` — sink flow of item i (items/min sent to AWESOME sink).
    
*   **Power is modeled as just another item.**
    

### 5.2 Per-sloop-grade constants (parameter table — plug in real values)

For each grade k on a machine/generator:

*   `ρ_k` — output multiplier
    
*   `κ_k` — input multiplier
    
*   `π_k` — power draw multiplier
    

Do NOT hardcode these; keep them in a config/parameter table (see §8).

### 5.3 Constraints (one per item)

**Item material balance:**

```
Σ_r Σ_k ( ρ_k·β[r][i] − κ_k·α[r][i] )·x[r][k] = s[i] ≥ 0   ∀ items i
```

This one family does three jobs at once:

1.  Flow conservation.
    
2.  **"Scale back under insufficient supply"** — short supply forces total consumption down; _all_ consumers of a scarce item are scaled back as a group within the single equation (no recipe-by-recipe code).
    
3.  **Overflow is sunk** — surplus flows into `s[i]`.
    

**Scarcity behavior (may surprise; it's desired):** when several recipes consume the same scarce item, the solver does NOT scale them proportionally. It routes the scarce item to whichever consumer yields the most sink points per item, starving lower-value consumers first. This is the optimal behavior and needs no special code.
**Map resource limits (raw items):**

```
Σ_r Σ_k κ_k·α[r][raw] · x[r][k] ≤ R[raw]   # total extraction ≤ map availability
```

> **Decision (revised, 2026-11-09):** map extraction is no longer a bare
> per-item cap `R`. Raw materials are produced by **extractor recipes** —
> recipes with empty inputs (miners, pumps) whose output is the raw item and
> whose optional `max_machines` is the number of that node purity available.
> That machine cap replaces `R`, and extraction now costs power via the
> extractor's machine type (and can accept Somersloops). This is strictly more
> faithful: mining draw is real, and a power-tight optimum must pay for its own
> ore. The old `resources` table is retained only as an *optional* extra cap on
> total consumption of an item; it must not be combined with an extractor
> recipe for the same item (the loader warns). See §9.

**Global Somersloop budget:**

```
Σ_r Σ_k k·x[r][k] + (generator sloops, = k·y[p][k]) ≤ S_after_augmenters
```

(With augmenters handled by sweep — reserve their cost before this constraint, see §6.)
**Power balance:**

```
Σ_generators π_k·produced ≤ augmented_capacity
```

Generators consume fuel (an item) and produce power; machines consume power. Power has no point value, so the solver generates only what's needed (mirrors in-game generator throttling for free). Power plants are recipes and may have sloop grades (π_k captures their behavior).
**Integrality:**

*   Grades with k ≥ 1 = distinct physical sloop count per machine → make `x[r][k≥1]` integer.
    
*   k=0 grade may stay continuous (fractional underclocking is legal in-game) — recommended; or make everything integer — HiGHS handles either at this size.
    
*   `s[i]` and k=0 activities continuous.
    

### 5.4 Objective

```
maximize  Σ_i p[i]·s[i]   # p[i] = AWESOME sink points per unit of item i
```

## 6. Alien Power Augmenters — additive stacking

Mechanics (confirmed by user): each augmenter adds 10% of **base (unaugmented)** generation, **additively** (not compounding), and costs **10 Somersloops** to construct.
Multiplier: `m(N) = 1 + 0.10·N` for N augmenters.
**Handling decision: outer sweep — do NOT put augmenters in the MILP directly.**  
Why: capacity = `m(N)·B` where B (generation) is a variable → bilinear → not plain MILP. Since N is tiny (≤ floor(S_total/10), realistically ≤ ~5), solve one fully-linear MILP per candidate N:

```
for N in 0..=floor(S_total/10):
    sloop_budget_in_model = S_total − 10·N      # reserve augmenter cost
    fix power constraint ceiling at m(N) = 1 + 0.1·N
    solve the §5 model
    record total sink points/min
take argmax over N
```

Each run independent → trivially parallel (`ProcessPoolExecutor` if wanted). Yields the **marginal-value curve of augmenters** ("augmenter #k is worth X pts/min and steals Y sloops that could have slooped generators or final-product machines").
Because stacking is **additive**, marginal value per augmenter is constant → the curve is flat-then-drops where slooping production outcompetes another augmenter.
**Nice emergent behavior (free):** unused fuel (from needing fewer/slooped generators) is itself an item with a sink term, so augmenters can convert fuel into sink points — their value can exceed the pure power math.

## 7. Outputs & diagnostics

Per solved model (per N):

*   **Per recipe:** machine count, sloop grade (0..K), clock % (activity is fractional → machines = ceil(activity), clock% = activity/machines).
    
*   **Per item:** sink flows (+ full point breakdown).
    
*   **Marginal analysis:** via sweep deltas (see §3) — empirical points/min per: additional augmenter, additional Somersloop, additional unit of each map resource. This answers "which bottleneck to expand / which sloop to hunt / augmenter vs production-slooping" — and is more robust than MIP shadow prices.
    

## 8. Parameters needing in-game confirmation (config table / TODOs)

| Parameter | Value | Status |
| --- | --- | --- |
| Max sloops per machine/generator K | 3? | **confirm** |
| Per-grade multipliers ρ, κ, π | 2^k? or other | **confirm** (esp. input & power when slooped) |
| Augmenter sloop cost | 10 | confirmed |
| Augmenter stacking | additive +10%/unit of base | confirmed |
| Map extraction limits | **revised:** extractor recipes with `max_machines` = node count (see §5.3 note); optional `resources` table for an extra consumption cap | done |
| Sink points p[i] | per item | config input |
| Do power buildings accept sloops, same K? | ? | **confirm** |

Design is parameter-driven so these fill in without touching model code.

## 9. Python implementation outline

*   **Config module:** items, recipes, sloop-grade tables, sink points, map resource caps, augmenter constants (JSON or const dicts).
    
*   **Model builder:** `build_model(config, augmenter_count N, sloop_budget) -> milp objects` emitting variables/constraints/objective per §5.
    *   Recommendation: `scipy.optimize.milp` (HiGHS-backed, simplest). If duals of LP relaxation ever needed, use `highspy` directly.
        
*   **Solver wrapper:** solve, read back activities + sink flows.
    
*   **Down-conversion:** activity → `{machines, sloop grade, clock%}`.
    
*   **Sweep harness:** loops over N (and optionally over total sloop budget / resource caps), collecting points/min and marginal curves.
    
*   **Output/report:** build plan table (per recipe: machines, sloops, clock %) + marginal-value summary.
    
*   **Do NOT include:** GA, populations, fitness functions, crossover — explicitly excluded per §2.
    

## 10. Numerical notes

*   Work in float; clamp values ~1e-9 to zero.
    
*   **Degeneracy:** two recipes tying on points-per-item may yield an arbitrary mix. Doesn't change objective. For deterministic solutions, perturb weights by ~1e-6 or accept the arbitrary (but optimal-value) mix.
    
*   **Fallback:** if the MILP ever grinds (should not at this scale), relax integrality to LP and round activities up to integer machines.