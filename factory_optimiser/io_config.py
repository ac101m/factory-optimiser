"""Load items, recipes and parameters from JSON files in the project hierarchy.

Generalised data format ("the JSON way to express a recipe"):

* Every file in a recipes/ tree is one recipe (a single machine model at 100%
  clock), e.g. ``recipes/manufacturing/iron_plate.json``::
  Subdirectories are just for organization — loading is a recursive glob that
  picks up every ``*.json`` anywhere under recipes/.

      {
        "id": "iron_plate",
        "name": "Iron Plate",
        "machine": "constructor",
        "inputs":  {"iron_ingot": 30.0},   # items/min consumed per machine
        "outputs": {"iron_plate": 20.0},   # items/min produced per machine
        "power_draw": 4.0,                 # optional; overrides machine default (MW)
        "max_machines": 30                 # optional; per-recipe cap
      }

* ``inputs``/``outputs`` map item ids to per-machine rates at 100% clock.
  A recipe may list ``"power": <MW>`` in ``outputs`` to be a generator.
* **Extractor recipes** (miners, water/oil pumps, ...) have **empty ``inputs``**
  and the raw material in ``outputs``; their ``max_machines`` is the number of
  that node (purity) type available on the map. This is how map extraction is
  modeled: supply is capped by extractor machine counts, and extractors draw
  power via their machine type like any other building. Split node purities
  into separate recipes (e.g. ``iron_ore_pure`` vs ``iron_ore_impure``).
* Items are plain ids with optional metadata — one file per item under
  items/ (id, name, sinkable, sink_points), the same pattern as machines.
  Filenames starting with ``_`` (e.g. ``_template.json``) are ignored so
  reference/template files can sit alongside the data.
* Game parameters (sloop-grade tables, augmenters, optional per-item resource
  caps, power defaults per machine, somersloop budget) live in
  config/parameters.json. The optional ``resources`` table bounds total
  *consumption* of an item; prefer extractor recipes for supply limits.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

#: Special item id for electrical power (MW). Only produced by generators,
#: only consumed via a recipe's power draw. Not sinkable, no sink points.
POWER_ITEM = "power"
DEFAULT_MAX_SLOOPS = 3

#: Overclocking power exponent (confirmed in-game): a machine's power draw
#: multiplies by (clock_speed/100)^1.321928 when overclocked. Stacks
#: multiplicatively with the Somersloop pi multiplier. The game overclock cap
#: is 250%.
CLOCK_POWER_EXP = 1.321928

#: Highest overclock the game allows (250%); parameters beyond this are
#: out-of-game and flagged by the consistency check.
GAME_MAX_CLOCK = 2.5

#: Alien Power Augmenter self-generation: each augmenter adds this many flat MW
#: of power on top of the multiplicative bonus, and the bonus does NOT apply to
#: it (confirmed in-game: 500 MW per augmenter).
DEFAULT_AUGMENTER_POWER_MW = 500.0


class ConfigError(Exception):
    """Raised when the JSON configuration is malformed or inconsistent."""


@dataclass(frozen=True)
class MachineSpec:
    """Static spec of a building type: base power draw and max Somersloops."""

    id: str = ""
    name: str = ""
    power_draw: float = 0.0
    max_sloops: int = DEFAULT_MAX_SLOOPS
    overclockable: bool = True


#: Fallback applied to machine types referenced by recipes but without a spec
#: file (a warning is emitted by the loader). All machines "just work" even if
#: you never write a spec file: 0 MW, up to 3 sloops, overclockable.
DEFAULT_MACHINE = MachineSpec(id="", name="(default)", power_draw=0.0, max_sloops=DEFAULT_MAX_SLOOPS)


@dataclass(frozen=True)
class Item:
    id: str
    name: str = ""
    sinkable: bool = True
    points: float = 0.0


@dataclass(frozen=True)
class Recipe:
    id: str
    name: str
    machine: str
    inputs: dict[str, float]
    outputs: dict[str, float]
    power_draw: float = 0.0
    max_machines: float | None = None
    unlimited: bool = False          # derived from max_machines=-1 in JSON:
                                     # extractor on a genuinely-infinite resource
                                     # (e.g. water); skips the uncapped warning
    map_resource: str | None = None  # node-group tag shared across miner tiers;
                                     # the group cap lives in
                                     # parameters.map_resources (one miner per
                                     # node, so mk1/2/3 sum to the node count)


@dataclass(frozen=True)
class Grade:
    """Multipliers for a slooped machine: output (rho), input (kappa), power (pi).

    Produced by :func:`sloop_multipliers` from the confirmed in-game formula
    (rho = 1+k/T, kappa = 1, pi = (1+k/T)^2 for k of T slots filled).
    """

    rho: float
    kappa: float
    pi: float


@dataclass(frozen=True)
class Augmenters:
    """Alien Power Augmenter constants.

    Each augmenter costs ``cost`` Somersloops, multiplies *base* (unaugmented)
    generation by an additive ``bonus`` per augmenter, and independently adds
    ``power_mw`` flat MW that the bonus does not affect.
    """

    cost: int = 10
    bonus: float = 0.10
    max: int | None = None
    power_mw: float = DEFAULT_AUGMENTER_POWER_MW


@dataclass
class Parameters:
    resources: dict[str, float]
    somersloop_budget: float
    augmenters: Augmenters
    #: Overclock clock-value tiers (as multiples of 100% clock). Only the
    #: values listed are available as choices; sorted, deduplicated, always
    #: containing 1.0 (the base clock). Default [1.0] = no overclocking.
    overclock_tiers: list[float] = field(default_factory=lambda: [1.0])
    #: Required power-generation overproduction (reserve): the grid must
    #: deliver ``(1 + power_overproduction) * consumption``, i.e. the plan
    #: always keeps a ``power_overproduction`` margin of capacity in hand over
    #: the load it draws (a real grid cannot run at exactly 100% of its
    #: generation). Default 0.01 = 1% headroom.
    power_overproduction: float = 0.01
    #: Node-group caps: each map resource (one resource x purity, e.g.
    #: "iron_node_normal") bounds the TOTAL number of machines across every
    #: recipe tagged ``map_resource = <same key>`` — one miner per node, so
    #: miner tiers mk1/2/3 share a single cap. The cap is the node count.
    map_resources: dict[str, float] = field(default_factory=dict)


def sloop_multipliers(k: int, total_slots: int) -> Grade:
    """Confirmed Somersloop grade multipliers (Design.md §5.2, §8).

    With ``k`` of ``total_slots`` slots filled on a machine:

        rho   (output) = 1 + k/total_slots   — linear, doubles at full slots
        kappa (input)  = 1                   — inputs do NOT increase
        pi    (power)  = (1 + k/total_slots)^2

    Example: a 2-slot machine with 1 slot filled -> 1.5x output, same input,
    (1.5)^2 = 2.25x power. ``total_slots`` <= 0 => no slooping possible and
    every multiplier is 1 (matches machines with zero sloop slots).
    """
    frac = (k / total_slots) if total_slots > 0 else 0.0
    return Grade(rho=1.0 + frac, kappa=1.0, pi=(1.0 + frac) ** 2)


@dataclass
class Config:
    items: dict[str, Item]
    recipes: list[Recipe]
    parameters: Parameters
    machines: dict[str, MachineSpec] = field(default_factory=dict)
    recipes_dir: Path = Path("recipes")
    machines_dir: Path = Path("machines")
    items_dir: Path = Path("items")

    def item_name(self, item_id: str, fallback: str | None = None) -> str:
        item = self.items.get(item_id)
        if item is not None and item.name:
            return item.name
        if fallback is not None and fallback != item_id:
            return f"{fallback} ({item_id})"
        return item_id

    # -- building / machine helpers -------------------------------------------

    def max_sloops_for(self, machine: str) -> int:
        """Total Somersloop slots (T) of a machine type.

        This is both the cap on how many sloops the machine accepts (k in
        0..T) and the denominator of the confirmed sloop multipliers — see
        :func:`sloop_multipliers`.
        """
        return self.machines.get(machine, DEFAULT_MACHINE).max_sloops

    def is_overclockable(self, machine: str) -> bool:
        """Whether a machine type may be overclocked (flag per machine spec)."""
        return self.machines.get(machine, DEFAULT_MACHINE).overclockable

    def power_draw_for(self, recipe: Recipe) -> float:
        """Base power draw (MW) for a recipe: its override, else its machine type."""
        if recipe.power_draw:
            return recipe.power_draw
        return self.machines.get(recipe.machine, DEFAULT_MACHINE).power_draw

    # -- classification helpers -------------------------------------------------

    @property
    def produced_items(self) -> list[str]:
        produced = set()
        for recipe in self.recipes:
            produced.update(recipe.outputs)
        produced.discard(POWER_ITEM)
        return sorted(produced)

    @property
    def consumed_items(self) -> list[str]:
        consumed = set()
        for recipe in self.recipes:
            consumed.update(recipe.inputs)
        return sorted(consumed)

    def is_sinkable(self, item_id: str) -> bool:
        return item_id != POWER_ITEM and self.items.get(item_id, Item(item_id)).sinkable


# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------


def load_item(path: str | Path) -> Item:
    """One item metadata JSON file, e.g. ``items/iron_ore.json``::

        {
          "id": "iron_ore",
          "name": "Iron Ore",
          "sinkable": false,      # may the AWESOME sink accept it? (default true)
          "sink_points": 10.0     # points per unit (default 0)
        }

    The ``id`` is what a recipe's ``inputs``/``outputs`` refer to.
    """
    raw = _read_json(path, "item")
    item_id = raw.get("id")
    if not item_id:
        raise ConfigError(f"item file {path}: missing 'id'")
    return Item(
        id=item_id,
        name=raw.get("name", item_id),
        sinkable=bool(raw.get("sinkable", True)),
        points=float(raw.get("sink_points", 0.0)),
    )


def load_items(directory: str | Path) -> dict[str, Item]:
    """Load every item JSON under ``directory`` (recursive, sorted).

    Files whose name starts with ``_`` are ignored (metadata / templates).
    """
    dir_path = Path(directory)
    if not dir_path.is_dir():
        raise ConfigError(f"items directory not found: {dir_path}")
    items: dict[str, Item] = {}
    for path in sorted(dir_path.rglob("*.json")):
        if path.name.startswith("_"):
            continue
        item = load_item(path)
        if item.id in items:
            raise ConfigError(f"duplicate item id {item.id!r} in {path}")
        items[item.id] = item
    if not items:
        raise ConfigError(f"no item JSON files found in {dir_path}")
    return items


def load_recipe(path: str | Path) -> Recipe:
    raw = _read_json(path, "recipe")
    recipe_id = raw.get("id")
    if not recipe_id:
        raise ConfigError(f"recipe file {path}: missing 'id'")
    name = raw.get("name", str(recipe_id))
    machine = raw.get("machine", "default")
    inputs = _rate_dict(raw.get("inputs"), path, "inputs")
    outputs = _rate_dict(raw.get("outputs"), path, "outputs")
    if not outputs:
        raise ConfigError(f"recipe {recipe_id!r} ({path}): no outputs")
    power_draw = float(raw.get("power_draw", 0.0))
    map_resource = raw.get("map_resource")
    max_machines = raw.get("max_machines")
    unlimited = False
    if max_machines is not None:
        max_machines = float(max_machines)
        if max_machines == -1:
            # Sentinel, not a real cap: "deliberately unlimited" supply, for
            # extractors on truly-infinite map resources (water, nitrogen, ...).
            # Normalized away here so the model and audit never see a literal
            # -1 cap (model.py would emit ub=-1 and make every plan infeasible;
            # consistency.py would flag it as a non-positive cap). Any NEGATIVE
            # value OTHER than -1 stays as-is and is flagged by the audit.
            max_machines = None
            unlimited = True
    return Recipe(
        id=recipe_id,
        name=name,
        machine=machine,
        inputs=inputs,
        outputs=outputs,
        power_draw=power_draw,
        max_machines=max_machines,
        unlimited=unlimited,
        map_resource=map_resource,
    )


def load_machine(path: str | Path) -> MachineSpec:
    """One machine-spec JSON file, e.g. ``machines/constructor.json``.::

        {
          "id": "constructor",
          "name": "Constructor",
          "power_draw": 4.0,   # MW at 100% clock (0 for generators)
          "max_sloops": 3      # highest Somersloop grade this building accepts
        }

    The ``id`` is what a recipe's ``machine`` field refers to.
    """
    raw = _read_json(path, "machine")
    machine_id = raw.get("id")
    if not machine_id:
        raise ConfigError(f"machine file {path}: missing 'id'")
    return MachineSpec(
        id=machine_id,
        name=raw.get("name", machine_id),
        power_draw=float(raw.get("power_draw", 0.0)),
        max_sloops=int(raw.get("max_sloops", DEFAULT_MAX_SLOOPS)),
        overclockable=bool(raw.get("overclockable", True)),
    )


def load_machines(directory: str | Path) -> dict[str, MachineSpec]:
    """Load every machine-spec JSON under ``directory`` (recursive, sorted)."""
    dir_path = Path(directory)
    if not dir_path.is_dir():
        raise ConfigError(f"machines directory not found: {dir_path}")
    machines: dict[str, MachineSpec] = {}
    for path in sorted(dir_path.rglob("*.json")):
        spec = load_machine(path)
        if spec.id in machines:
            raise ConfigError(f"duplicate machine id {spec.id!r} in {path}")
        machines[spec.id] = spec
    if not machines:
        raise ConfigError(f"no machine JSON files found in {dir_path}")
    return machines


def load_recipes(directory: str | Path) -> list[Recipe]:
    dir_path = Path(directory)
    if not dir_path.is_dir():
        raise ConfigError(f"recipes directory not found: {dir_path}")
    recipes: list[Recipe] = []
    seen: set[str] = set()
    # Recursive glob: recipes may live in subdirectories for organization
    # (e.g. recipes/mining/, recipes/manufacturing/). Sorted for determinism.
    for path in sorted(dir_path.rglob("*.json")):
        recipe = load_recipe(path)
        if recipe.id in seen:
            raise ConfigError(f"duplicate recipe id {recipe.id!r} in {path}")
        seen.add(recipe.id)
        recipes.append(recipe)
    if not recipes:
        raise ConfigError(f"no recipe JSON files found in {dir_path}")
    return recipes


def load_parameters(path: str | Path) -> Parameters:
    raw = _read_json(path, "parameters")

    resources = {
        str(k): float(v)
        for k, v in raw.get("resources", {}).items()
        if not str(k).startswith("_")
    }

    map_resources = {
        str(k): float(v)
        for k, v in raw.get("map_resources", {}).items()
        if not str(k).startswith("_")
    }

    aug_raw = raw.get("augmenters", {})
    augmenters = Augmenters(
        cost=int(aug_raw.get("cost", 10)),
        bonus=float(aug_raw.get("bonus", 0.10)),
        max=aug_raw.get("max"),
        power_mw=float(aug_raw.get("power_mw", DEFAULT_AUGMENTER_POWER_MW)),
    )

    # Overclock tier list: parse `overclock.tiers` (or tolerate a bare list),
    # force 1.0 in (the base clock is always available), sort ascending.
    overclock_raw = raw.get("overclock", {})
    if isinstance(overclock_raw, dict):
        overclock_raw = overclock_raw.get("tiers", [1.0])
    tiers = sorted({float(t) for t in overclock_raw} | {1.0})

    # Power-generation overproduction: `power.overproduction` (fraction of load
    # over-produced / kept as reserve).
    power_raw = raw.get("power", {})
    if not isinstance(power_raw, dict):
        power_raw = {}

    return Parameters(
        resources=resources,
        somersloop_budget=float(raw.get("somersloop_budget", 0.0)),
        augmenters=augmenters,
        overclock_tiers=tiers,
        power_overproduction=float(power_raw.get("overproduction", 0.01)),
        map_resources=map_resources,
    )


def load_config(
    recipes_dir: str | Path = "recipes",
    machines_dir: str | Path = "machines",
    items_dir: str | Path = "items",
    parameters_path: str | Path = "config/parameters.json",
) -> Config:
    recipes = load_recipes(recipes_dir)
    machines = load_machines(machines_dir)
    items = load_items(items_dir)
    parameters = load_parameters(parameters_path)
    config = Config(
        items=items,
        recipes=recipes,
        parameters=parameters,
        machines=machines,
        recipes_dir=Path(recipes_dir),
        machines_dir=Path(machines_dir),
        items_dir=Path(items_dir),
    )
    return config


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _read_json(path: str | Path, what: str) -> dict:
    p = Path(path)
    if not p.is_file():
        raise ConfigError(f"{what} file not found: {p}")
    try:
        raw = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ConfigError(f"{what} file {p} is not valid JSON: {exc}") from exc
    if not isinstance(raw, dict):
        raise ConfigError(f"{what} file {p} must contain a JSON object")
    return raw


def _rate_dict(value, path: str, field_name: str) -> dict[str, float]:
    if not isinstance(value, dict):
        raise ConfigError(f"recipe file {path}: '{field_name}' must be an object")
    rates: dict[str, float] = {}
    for item_id, rate in value.items():
        rates[str(item_id)] = float(rate)
    return rates
