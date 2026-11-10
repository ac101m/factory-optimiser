# Satisfactory Factory Optimizer

Given Satisfactory recipes, map resource limits, a total Somersloop budget, and
Alien Power Augmenter behavior, this tool computes the **globally optimal build
plan** — how many machines per recipe, how to split Somersloops, and which
augmenters to build — that **maximizes AWESOME sink points per minute**.

It solves a single **MILP** with `scipy.optimize.milp` (HiGHS). There is
**no genetic algorithm**: the problem is a convex flow/throughput optimization
and the LP framework solves it exactly and deterministically. See `Design.md`
for the full model and the reasoning.

## Quick start

```bash
venv and deps:
  uv venv --seed .venv && uv pip install -e .     # or: pip install -e .

```

```bash
.venv/bin/factory-optimiser optimize      # best plan (augmenter sweep included)
.venv/bin/factory-optimiser optimize --json
.venv/bin/factory-optimiser optimize --no-augmenters
.venv/bin/factory-optimiser sweep augmenters      # pts/min per augmenter count
.venv/bin/factory-optimiser sweep somersloops     # pts/min per Somersloop budget
.venv/bin/factory-optimiser sweep resources       # pts/min per extra extractor node per raw material
.venv/bin/factory-optimiser --help
```

Run from the project root (the `recipes/`, `machines/`, `items/`, `config/`
data paths are resolved relative to the working directory; override with
`-r/-m/-t/-p`).

## How recipes are expressed (JSON)

Every file under `recipes/` describes **one recipe**, i.e. one machine model at
100% clock. Subdirectories are just for organizing the collection (e.g.
`recipes/mining/`, `recipes/manufacturing/`) — the loader recursively picks up
every `*.json`. Items are plain string ids. Example (`recipes/manufacturing/iron_plate.json`):

```json
{
  "id": "iron_plate",
  "name": "Iron Plate",
  "machine": "constructor",
  "inputs":  {"iron_ingot": 30.0},     // items/min consumed per machine
  "outputs": {"iron_plate": 20.0},     // items/min produced per machine
  "power_draw": 4.0,                   // optional: override the machine default (MW)
  "max_machines": 30                   // optional: hard cap on machines of this recipe
}
```

* Any number of inputs/outputs; items are just ids. Two recipes may produce the
  same item — the solver freely splits production, and dominated recipes are
  automatically left unused (no "pick one variant" machinery needed).
* A generator is expressed by listing `"power": <MW>` in `outputs` (it consumes
  fuel like any recipe and produces the special `power` item). Consumers draw
  power via `power_draw` (or the machine-type default).
* **Extractors** (miners, pumps) are recipes with **empty `inputs`** that output
  the raw material; their `max_machines` is the number of that node purity on
  the map. So map supply is a *recipe*, not a global number — extractors draw
  power (via the `miner`/`pump` machine type) and can even accept Somersloops.
  Node purities are separate recipes, e.g. `iron_ore_pure` (120/min, ×2 nodes)
  vs `iron_ore_impure` (30/min, ×1 node). Use `sweep resources` to see the
  marginal value of one more node of each type.
* `machine` refers to a building type whose spec lives in `machines/*.json`
  (one file per building: `id`, `name`, `power_draw`, `max_sloops` — same
  pattern as recipes). Unknown machines fall back to defaults and print a
  warning.
* `max_machines` is optional; without it recipes are limited only by map
  resources (Design.md §4). For extractor recipes, `max_machines` is the node
  count.

Supporting config:

* `items/*.json` — one item per file: `{id, name, sinkable, sink_points}`
  (same pattern as machines; subdirectories are fine, and files whose name
  starts with `_` — e.g. `_template.json` — are ignored). Items referenced by
  recipes but absent here get defaults (sinkable, 0 points) and are flagged by
  `factory-optimiser check`.
* `machines/*.json` — one building per file: `{id, name, power_draw, max_sloops}`
  (e.g. `machines/constructor.json`). Subdirectories are fine; loading is a
  recursive glob.
* `config/parameters.json` — Somersloop budget, Alien Power Augmenter cost &
  bonus (each augmenter also adds a flat `power_mw`, un-bonused). An optional
  `resources` table can still bound total *consumption* of an item, but the
  preferred way to limit supply is extractor recipes. Sloop multipliers are the
  confirmed in-game formula and not configured here: a machine with k of its T
  slots filled gets `ρ = 1+k/T` output, `κ = 1` input (unchanged), `π = (1+k/T)²`
  power; `T` is the machine's `max_sloops`.

The current recipes/items/parameters are **small placeholder examples** with
plausible-but-unconfirmed numbers; drop in real data later without touching the
model code.

## Model summary (see Design.md for the formal statement)

* Variables `x[r][k]`: machines running recipe `r` with exactly `k` Somersloops
  (`k ≥ 1` integer — you can't have half a slooped machine; `k = 0`
  continuous = fractional underclocking, which is legal in-game).
* One material-balance equation per produced item:
  `Σ (ρ_k·β − κ_k·α)·x = s[i] ≥ 0` — overflow flows into the sink, and scarce
  items are routed to the consumer with the highest points-per-item (starvation
  of weak recipes is the *optimal* behavior, not a bug).
* Raw materials are produced by extractor recipes whose `max_machines` is the
  node count — that cap *is* the map resource limit (plus power: miners draw MW
  like any machine).
* A global Somersloop budget `Σ k·x ≤ S`.
* Power is an item: generators produce it, machines consume it, and
  `consumption ≤ m(N)·generation` where `m(N) = 1 + 0.10·N`.
* Objective: `max Σ p[i]·s[i]`.

Alien Power Augmenters stack additively (`+10%` of base generation each, 10
Somersloops each) which is bilinear in the MILP, so the tool does an **outer
sweep over N** (Design.md §6): solve one fully-linear MILP per affordable N and
take the argmax. Because MILPs lack well-defined duals, marginal values are
reported as **sweep deltas** (empirical, robust) — that's what the `sweep`
subcommands print.

## Out of scope (decided)

Spatial layout, belt routing, machine placement, electrical-grid separation,
and overclocking beyond 100% (in-game power is nonlinear there). See Design.md.

## Development

```bash
.venv/bin/python tests/test_smoke.py     # smoke tests, no framework needed
```
