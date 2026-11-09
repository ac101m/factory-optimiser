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
* Items are plain ids with optional metadata in a separate items file
  (sink points, sinkable flag). See config/items.json.
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


class ConfigError(Exception):
    """Raised when the JSON configuration is malformed or inconsistent."""


@dataclass(frozen=True)
class MachineSpec:
    """Static spec of a building type: base power draw and max Somersloops."""

    id: str = ""
    name: str = ""
    power_draw: float = 0.0
    max_sloops: int = DEFAULT_MAX_SLOOPS


#: Fallback applied to machine types referenced by recipes but without a spec
#: file (a warning is emitted by the loader). All machines "just work" even if
#: you never write a spec file: 0 MW, up to 3 sloops.
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


@dataclass(frozen=True)
class Grade:
    """Per-sloop-grade multipliers: output (rho), input (kappa), power (pi)."""

    rho: float
    kappa: float
    pi: float


@dataclass(frozen=True)
class Augmenters:
    cost: int = 10
    bonus: float = 0.10
    max: int | None = None


@dataclass
class Parameters:
    resources: dict[str, float]
    sloop_grades: dict[int, Grade]
    somersloop_budget: float
    augmenters: Augmenters


@dataclass
class Config:
    items: dict[str, Item]
    recipes: list[Recipe]
    parameters: Parameters
    machines: dict[str, MachineSpec] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    recipes_dir: Path = Path("recipes")
    machines_dir: Path = Path("machines")

    def item_name(self, item_id: str, fallback: str | None = None) -> str:
        item = self.items.get(item_id)
        if item is not None and item.name:
            return item.name
        if fallback is not None and fallback != item_id:
            return f"{fallback} ({item_id})"
        return item_id

    # -- building / machine helpers -------------------------------------------

    def max_sloops_for(self, machine: str) -> int:
        """Highest sloop grade available on a machine type, clamped by the grade table."""
        spec = self.machines.get(machine, DEFAULT_MACHINE)
        cap = spec.max_sloops
        highest = max(self.parameters.sloop_grades) if self.parameters.sloop_grades else 0
        return min(cap, highest)

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


def load_items(path: str | Path) -> dict[str, Item]:
    raw = _read_json(path, "items")
    items: dict[str, Item] = {}
    for item_id, spec in raw.items():
        if item_id.startswith("_"):
            continue  # allow comments / metadata keys
        if not isinstance(spec, dict):
            raise ConfigError(f"items file {path}: entry {item_id!r} must be an object")
        name = spec.get("name", item_id)
        sinkable = bool(spec.get("sinkable", True))
        points = float(spec.get("sink_points", 0.0))
        items[item_id] = Item(id=item_id, name=name, sinkable=sinkable, points=points)
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
    max_machines = raw.get("max_machines")
    if max_machines is not None:
        max_machines = float(max_machines)
    return Recipe(
        id=recipe_id,
        name=name,
        machine=machine,
        inputs=inputs,
        outputs=outputs,
        power_draw=power_draw,
        max_machines=max_machines,
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

    grades_raw = raw.get("sloop_grades", {})
    if "0" not in grades_raw:
        raise ConfigError(f"parameters file {path}: sloop_grades must include grade 0")
    sloop_grades: dict[int, Grade] = {}
    for k, spec in grades_raw.items():
        if str(k).startswith("_"):
            continue
        sloop_grades[int(k)] = Grade(
            rho=float(spec["rho"]), kappa=float(spec["kappa"]), pi=float(spec["pi"])
        )

    aug_raw = raw.get("augmenters", {})
    augmenters = Augmenters(
        cost=int(aug_raw.get("cost", 10)),
        bonus=float(aug_raw.get("bonus", 0.10)),
        max=aug_raw.get("max"),
    )

    return Parameters(
        resources=resources,
        sloop_grades=sloop_grades,
        somersloop_budget=float(raw.get("somersloop_budget", 0.0)),
        augmenters=augmenters,
    )


def load_config(
    recipes_dir: str | Path = "recipes",
    machines_dir: str | Path = "machines",
    items_path: str | Path = "config/items.json",
    parameters_path: str | Path = "config/parameters.json",
) -> Config:
    recipes = load_recipes(recipes_dir)
    machines = load_machines(machines_dir)
    items = load_items(items_path)
    parameters = load_parameters(parameters_path)
    config = Config(
        items=items,
        recipes=recipes,
        parameters=parameters,
        machines=machines,
        recipes_dir=Path(recipes_dir),
        machines_dir=Path(machines_dir),
    )

    # Cross-check: warn about items referenced by recipes that have no entry.
    referenced = set()
    for recipe in recipes:
        referenced.update(recipe.inputs)
        referenced.update(recipe.outputs)
    referenced.discard(POWER_ITEM)
    for item_id in sorted(referenced):
        if item_id not in items:
            config.warnings.append(
                f"item {item_id!r} referenced by recipes has no entry in {items_path} "
                f"(assuming sinkable with 0 sink points)"
            )
    # Warn about recipes for unknown machine types (they fall back to defaults).
    known_machines = set(machines) | {"default"}
    for recipe in recipes:
        if recipe.machine not in known_machines:
            config.warnings.append(
                f"recipe {recipe.id!r} uses unknown machine {recipe.machine!r} "
                f"(no spec in {machines_dir}; using defaults: {DEFAULT_MAX_SLOOPS} max sloops, "
                f"{DEFAULT_MACHINE.power_draw} MW)"
            )
    # Warn about resource caps for items that are also produced.
    produced = set(config.produced_items)
    for item_id in parameters.resources:
        if item_id in produced:
            config.warnings.append(
                f"resource {item_id!r} is both produced by a recipe and map-capped; "
                f"the cap applies to total consumption"
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
