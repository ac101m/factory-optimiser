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
    

### 5.2 Per-sloop multipliers (CONFIRMED formula, per machine)

A machine has `T` total Somersloop slots (its `max_sloops`, per `machines/*.json`).
With `k` of those slots filled (k = 0..T):

*   `ρ(k,T) = 1 + k/T` — output multiplier (linear; doubles at full slots)
*   `κ(k,T) = 1` — input multiplier (**inputs do not increase with sloops**)
*   `π(k,T) = (1 + k/T)^2` — power draw multiplier (quadratic)

Example (confirmed): a 2-slot machine with 1 slot filled → `1.5×` output, same
input, `2.25×` power; full slots → `2×` output. Implemented in
`io_config.sloop_multipliers`; there is no global per-grade table because the
multipliers depend on each machine's own slot count `T`.

### 5.3 Constraints (one per item)

**Item material balance:**

```
Σ_r Σ_k ( ρ(k_r,T_r)·β[r][i] − κ·α[r][i] )·x[r][k] = s[i] ≥ 0   ∀ items i
```

with `κ = 1` (confirmed: slooping does not increase input consumption). So a
slooped machine converts the same feed into strictly more product — Somersloops
are a scarce multiplier on material efficiency, not just machine throughput.

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
**Generation overproduction (reserve):** the balance is `consumption ≤ (m(N)·generation + N·W)/(1 + s)` where `s = parameters.power_overproduction` (default `0.01` = 1%). I.e. the grid must deliver `(1 + s)×` the load, so the optimizer can never plan to run generation at exactly 100% of what consumers draw — the report keeps `s` of capacity as headroom (this is why the machine-count tiebreak throttles generators to `(1+s)·load`, not `load`). Configurable; a real grid needs margin for clock rounding, belt/pipe limits and throttle lag.
**Integrality:**

*   Grades with k ≥ 1 = distinct physical sloop count per machine → make `x[r][k≥1]` integer.
    
*   k=0 grade may stay continuous (fractional underclocking is legal in-game) — recommended; or make everything integer — HiGHS handles either at this size.
    
*   `s[i]` and k=0 activities continuous.
    

### 5.4 Objective

```
maximize  Σ_i p[i]·s[i]   # p[i] = AWESOME sink points per unit of item i
```

### 5.5 Clocking — discrete tiers (implemented)

Clocking multiplies a machine's throughput by `c = clock/100` at
`power × c^1.321928` — the confirmed in-game power curve, stacked
multiplicatively on the sloop π multiplier. Because the exponent is sub-linear
below 100%, **underclocking is power-efficient** (0.5× output for ~0.4× draw);
above 100% overclocking is power-hungry (2.5× output for ~3.4× draw, up to the
**250% game cap**). Inputs scale by `c` in both directions. Each tier value is
a config choice (`overclock.tiers` in `config/parameters.json`, shipped as
`[0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 2.5]`; `1.0` is always included). Machines
opt in per spec via `overclockable` in `machines/*.json` (default true;
geothermal is fixed at 100% — it is not overclockable in-game).

**Discrete tiers, not a continuous clock variable:** each available clock value
is one column, so the model stays an exact linear MILP — no machines×clock
bilinearity. A machine at clock `c` contributes

```
output   c · ρ(k) · β
input    c · κ(k) · α
power    c^1.321928 · π(k) · power_draw
sloops   k                        (clock doesn't change sloop usage)
machine cap  1                    (clock doesn't change machine count)
```

Clock tiers attach to **every grade of an overclockable machine** (an earlier
design capped the continuous `k = 0` grade at `c ≤ 1.0` on the argument that a
`c>1` continuous column is dominated by the power-efficient `c=1` one; that is
true of the *points-only* optimum but the fewest-machines tiebreak (§10) wants
exactly those columns, so the restriction was removed):
*   integer slooped grades `k ≥ 1` — the **sloop-efficiency lever** (one
    scarce sloop at 250% far outproduces spreading sloops, at ~25% more power
    per output);
*   the sole grade `k = 0` of **0-slot** overclockable machines (miners,
    extractors) — where overclocking pays most in-game, breaking node caps;
*   the continuous `k = 0` grade of slot machines — **overclocking there does
    not change the point optimum** (same output at more power), but it lets
    the fewest-machines tiebreak shrink building counts wherever power has
    slack. Power shards are craftable in current Satisfactory, so no shard
    resource is modeled: the high clock is priced only by the power row, which
    rejects it automatically whenever power binds.

Because nothing prices *building count*, wherever power has slack the optimum
is a **flat face in machines/clock** — "60 Screw constructs at 50%" is exactly
as optimal as "30 at 100%" (identical output, more buildings, less draw). The
`optimize` command resolves this lexicographically toward the **fewest
machines** (see §10): the reported plan is the smallest build that still hits
the optimum, which collapses the pointless underclocking away while *keeping*
genuine power-bound underclocking (there the high-clock plan is infeasible).

Backward compatibility: with `overclock.tiers` absent (or `[1.0]`) the model
is byte-identical to the pre-overclock formulation. The tier treatment was
validated at full-game scale (~300 recipes / ~180 items): nested supersets of
clock grids are monotone (a MILP max over nested feasible sets cannot
decrease), and solves certify optimality in single-digit seconds even for very
fine grids.

## 6. Alien Power Augmenters — additive stacking + flat self-generation

Mechanics (confirmed by user): each augmenter adds 10% of **base (unaugmented)** generation, **additively** (not compounding), costs **10 Somersloops** to construct, **and generates 500 MW of power itself, to which the bonus does NOT apply** (flat per augmenter).
Multiplier: `m(N) = 1 + 0.10·N` for N augmenters.
Total capacity: `capacity = m(N)·B + 500·N` where B is the factory's own (variable) power generation.
**Handling decision: outer sweep — do NOT put augmenters in the MILP directly.**  
Why: capacity = `m(N)·B + 500·N` where B (generation) is a variable → bilinear → not plain MILP. Since N is tiny (≤ floor(S_total/10)), solve one fully-linear MILP per candidate N:

```
for N in 0..=floor(S_total/10):
    sloop_budget_in_model = S_total − 10·N      # reserve augmenter cost
    fix coefficient m(N) = 1 + 0.1·N on generator output
    credit N·500 MW as flat power capacity (the row's lower bound; constant per N)
    solve the §5 model
    record total sink points/min
take argmax over N
```

Because `N·500` is constant for a fixed N, it only shifts the power-balance row's lower bound — the MILP stays linear. Each run independent → trivially parallel (`ProcessPoolExecutor` if wanted). Yields the **marginal-value curve of augmenters** ("augmenter #k is worth X pts/min, gives 500·k free MW, and steals Y sloops that could have slooped generators or final-product machines").
Because stacking is **additive**, marginal value per augmenter is constant → the curve is flat-then-drops where slooping production outcompetes another augmenter.
**Nice emergent behaviors (free):** (1) unused fuel (from needing fewer/slooped generators) is itself an item with a sink term, so augmenters can convert fuel into sink points — their value can exceed the pure power math; (2) with N ≥ 1 an augmenter's own 500 MW can power a consumer-only factory with no generator recipes at all.

## 7. Outputs & diagnostics

Per solved model (per N):

*   **Per recipe:** machine count, sloop grade (0..K), clock % (`machines = ceil(activity)`, `clock% = 100·c·activity/machines` — up to 250% when overclocked, under 100% for the continuous base grade).
    
*   **Per item:** sink flows (+ full point breakdown).
    
*   **Marginal analysis:** via sweep deltas (see §3) — empirical points/min per: additional augmenter, additional Somersloop, additional unit of each map resource. This answers "which bottleneck to expand / which sloop to hunt / augmenter vs production-slooping" — and is more robust than MIP shadow prices.
    
*   **Consistency check (`check` subcommand):** audits the loaded config before any solve — semantic issues that would otherwise surface as silently-wrong optima or all-zero solves. Runs as a pre-flight gate on *every* command (errors refuse to proceed, exit non-zero; warnings print to stderr and never block). Findings (deterministic order, errors first): unknown machine types referenced by recipes; items referenced but missing from the items config; unused machine specs / unused item entries; `max_sloops` beyond the grade table (clamped); non-positive rates / `max_machines`; items consumed but never produced and uncapped; produced items that are unsinkable and never consumed (dead end); power consumers with no generator; extractor recipes without a `max_machines` cap; `resources` caps on items that are also produced. It is pure data inspection — it never solves a MILP. `check --strict` additionally fails on warnings (for CI).
    

## 8. Parameters needing in-game confirmation (config table / TODOs)

| Parameter | Value | Status |
| --- | --- | --- |
| Per-machine Somersloop slots T | per machine spec (`max_sloops` in `machines/*.json`) | slots per building: **confirm** (data currently 0/1/2) |
| Sloop multipliers ρ, κ, π | ρ = 1+k/T, κ = 1, π = (1+k/T)² | confirmed |
| Overclock clock tiers | `overclock.tiers` in `config/parameters.json` (default `[1.0]` = off) | config; ships `[0.5,0.75,1.0,1.25,1.5,2.0,2.5]` (under- and overclock) |
| Overclock power factor | `c^1.321928`, stacked on sloop π | confirmed |
| Overclock cap | 250% (`GAME_MAX_CLOCK`); tiers above flagged as a warning | confirmed |
| Overclockable machines | per-machine `overclockable` flag (`machines/*.json`, default true); overclock available on every grade (slooped, 0-slot, and un-slooped continuous) | implemented; geothermal = false |
| Augmenter sloop cost | 10 | confirmed |
| Augmenter stacking | additive +10%/unit of base | confirmed |
| Augmenter flat power | +500 MW each, bonus does NOT apply | confirmed |
| Power-generation overproduction (reserve) | `power.overproduction` in `config/parameters.json` (default 0.01 = 1%) | config |
| Map extraction limits | **revised:** extractor recipes with `max_machines` = node count (see §5.3 note); optional `resources` table for an extra consumption cap | done |
| Sink points p[i] | per item | config input |
| Do power buildings accept sloops, same K? | ? | **confirm** |

Design is parameter-driven so these fill in without touching model code.

> **Note (revised):** building specs (`power_draw`, `max_sloops`) live in
> `machines/*.json` — one file per building type (id, name, power_draw,
> max_sloops), loaded like recipes, subdirectories allowed. A recipe's
> `machine` field refers to one of those ids; unknown ids fall back to 0 MW /
> max sloops with a loader warning.

> **Note (revised):** item metadata (`sinkable` flag, AWESOME `sink_points`)
> likewise lives in `items/*.json` — one file per item (id, name, sinkable,
> sink_points), loaded like machines/recipes (recursive glob, sorted,
> duplicate-id hard error). Files whose name starts with `_` are ignored so a
> `_template.json` can sit next to the data. `-t/--items` points at this
> directory.

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
    
*   **Machine count is unpriced, so the optimum is often a whole *flat face*,** not one plan — "60 Screw constructs at 50%" and "30 at 100%" deliver identical output/points whenever power has slack, and in-game only differ by build effort (which the objective ignores). The `optimize` command therefore runs a **lexicographic two-phase tiebreak** (`solve.solve(..., minimize_machines=...)`): phase 1 maximizes sink points; phase 2 pins the point total at the phase-1 optimum (one extra row, `Σ p[i]·s[i] ≥ V* − tol`) and *minimizes total machine-equivalents* `Σ x` (machines = ⌈x⌉, so minimizing Σ x minimizes buildings). Exactly two MILP solves (~seconds each). Only the *reported plan* changes — the objective stays at V*. Because the power row is still enforced, this keeps underclocking precisely where it pays (a power-bound optimum cannot re-clock to 100%: infeasible) and collapses it everywhere else (Screw back to 30 @ 100% — or, with overclocking allowed on un-slooped machines, straight to 12 @ 250%). Bonus: it also throttles idle generator capacity down to actual demand (+ the overproduction reserve). Two second-order details: (1) `Σ x` is a proxy for the reported `Σ⌈x⌉`, so a sub-machine clock sliver (e.g. 0.02 machines @ 100% beside 19.96 @ 50%) that shaves equivalents can *report* as an extra whole machine — a post-pass folds such slivers into the grade's lowest clock column (`_consolidate_clock_slivers`; output and points unchanged, draw only falls); (2) the model has **no power-shard resource** — current Satisfactory makes shards craftable, so overclocking is treated as free and the tiebreak uses it wherever power permits (matching the game's "spend shards, build fewer" without a shard ledger).
    
*   **Fallback:** if the MILP ever grinds (should not at this scale), relax integrality to LP and round activities up to integer machines.