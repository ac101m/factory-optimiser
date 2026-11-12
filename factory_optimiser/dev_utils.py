"""Developer utilities for extracting data from a Satisfactory game install.

Dev-only tooling, deliberately kept out of the main ``factory-optimiser`` CLI.
It reads the game's AutoJSON export (``<game-dir>/CommunityResources/Docs/
en-US.json``, a UTF-16 LE dump) and *lifts* individual machine / recipe / item
records into our internal JSON format (see :mod:`io_config`), pretty-printed
for copy-pasting into the repo's ``recipes/``, ``items/`` and ``machines/``
directories.

Read-only interrogation of the game files: it never writes to the game install
or to the repo (''diff'' only compares). It is not an authoritative source for
what the recipes are — that lives in the repo, curated by hand.

Typical use when adding a recipe::

    factory-optimiser-dev-utils recipe "Compacted Coal"

matches the public in-game name and prints the repo's hand-format JSON::

    {
      "id": "compacted_coal",          # from RECIPE_MANIFEST, or a suggested slug
      "name": "Alternate: Compacted Coal",
      "machine": "assembler",
      "inputs": {"coal": 60.0},
      "outputs": {"compacted_coal": 45.0}
    }

Warnings (unmapped item classes, anything that needs a human decision) go to
*stderr* so stdout stays valid, pasteable JSON.

The manifests below are ClassName -> (our internal id, JSON path) lookup
tables: they translate the game's ClassNames into the ids our repo uses, and
carry the hand-confirmed machine ``max_sloops`` (which the game does not
export). They are translation tables, not an authoritative recipe catalogue —
the recipe set itself is defined by the repo's ``recipes/`` files.

Formatting rules applied to the raw game data (deliberate, to match our model):

* Rates are per minute at 100% clock: ``amount * 60 / duration``.
* Fluids/gases (``RF_LIQUID``/``RF_GAS``) are stored internally in m³/min, so
  the per-minute rate is divided by 1000.
* Liquids/gases are modelled non-sinkable (``sinkable: false, sink_points: 0``)
  even though the game assigns sink points to some of them.
* Names come verbatim from the en-US localisation (``mDisplayName``), including
  the game's "Alternate: " prefix on alternate recipes.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

# Allow running as a plain script: `python factory_optimiser/dev_utils.py`.
# When executed directly the module has no parent package, so the relative
# imports below would fail without this bootstrap.
if __package__ in (None, ""):
    __package__ = "factory_optimiser"
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from . import __version__

from docopt import DocoptExit, docopt  # noqa: E402

# --------------------------------------------------------------------------
# Manifests: game ClassName -> (our internal id, project-relative JSON path)
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class _M:
    """One manifest entry: our internal ID + where our JSON for it lives."""

    id: str
    path: str


@dataclass(frozen=True)
class _Machine:
    """Machine manifest entry: ID, path, and the max Somersloop slots.

    ``max_sloops`` is **not** exported by the game's AutoJSON docs, so it must
    be provided here (hand-confirmed values); the tooling never guesses it.
    """

    id: str
    path: str
    max_sloops: int


MACHINE_MANIFEST = {
    "Build_AssemblerMk1_C": _Machine("assembler", "machines/assembler.json", 2),
    "Build_Blender_C": _Machine("blender", "machines/blender.json", 4),
    "Build_ConstructorMk1_C": _Machine("constructor", "machines/constructor.json", 1),
    "Build_Converter_C": _Machine("converter", "machines/converter.json", 2),
    "Build_FoundryMk1_C": _Machine("foundry", "machines/foundry.json", 2),
    "Build_FrackingSmasher_C": _Machine("resource_well_pressurizer", "machines/resource_well_pressurizer.json", 0),
    "Build_GeneratorCoal_C": _Machine("coal_generator", "machines/coal_generator.json", 0),
    "Build_GeneratorFuel_C": _Machine("fuel_generator", "machines/fuel_generator.json", 0),
    "Build_GeneratorGeoThermal_C": _Machine("geothermal_generator", "machines/geothermal_generator.json", 0),
    "Build_GeneratorNuclear_C": _Machine("nuclear_power_plant", "machines/nuclear_power_plant.json", 0),
    "Build_HadronCollider_C": _Machine("accelerator", "machines/accelerator.json", 4),
    "Build_ManufacturerMk1_C": _Machine("manufacturer", "machines/manufacturer.json", 4),
    "Build_QuantumEncoder_C": _Machine("quantum_encoder", "machines/quantum_encoder.json", 4),
    "Build_MinerMk1_C": _Machine("miner_mk1", "machines/miner.json", 0),
    "Build_MinerMk2_C": _Machine("miner_mk2", "machines/miner_mk2.json", 0),
    "Build_MinerMk3_C": _Machine("miner_mk3", "machines/miner_mk3.json", 0),
    "Build_OilPump_C": _Machine("oil_extractor", "machines/oil_extractor.json", 0),
    "Build_OilRefinery_C": _Machine("refinery", "machines/refinery.json", 2),
    "Build_Packager_C": _Machine("packager", "machines/packager.json", 0),
    "Build_SmelterMk1_C": _Machine("smelter", "machines/smelter.json", 1),
    "Build_WaterPump_C": _Machine("water_extractor", "machines/water_extractor.json", 0),
}

ITEM_MANIFEST = {
    "Desc_SpaceElevatorPart_5_C": _M("adaptive_control_unit", "items/adaptive_control_unit.json"),
    "Desc_SpaceElevatorPart_7_C": _M("assembly_director_system", "items/assembly_director_system.json"),
    "Desc_SpaceElevatorPart_3_C": _M("automated_wiring", "items/automated_wiring.json"),
    "Desc_CircuitBoardHighSpeed_C": _M("ai_limiter", "items/ai_limiter.json"),
    "Desc_AlienPowerFuel_C": _M("alien_power_matrix", "items/alien_power_matrix.json"),
    "Desc_AluminumPlate_C": _M("alclad_aluminum_sheet", "items/alclad_aluminum_sheet.json"),
    "Desc_AluminumCasing_C": _M("aluminum_casing", "items/aluminum_casing.json"),
    "Desc_AluminumIngot_C": _M("aluminum_ingot", "items/aluminum_ingot.json"),
    "Desc_AluminumScrap_C": _M("aluminum_scrap", "items/aluminum_scrap.json"),
    "Desc_AluminaSolution_C": _M("alumina_solution", "items/alumina_solution.json"),
    "Desc_SpaceElevatorPart_11_C": _M("ballistic_warp_drive", "items/ballistic_warp_drive.json"),
    "Desc_Battery_C": _M("battery", "items/battery.json"),
    "Desc_OreBauxite_C": _M("bauxite", "items/bauxite.json"),
    "Desc_SpaceElevatorPart_10_C": _M("biochemical_sculptor", "items/biochemical_sculptor.json"),
    "Desc_Cable_C": _M("cable", "items/cable.json"),
    "Desc_GoldIngot_C": _M("caterium_ingot", "items/caterium_ingot.json"),
    "Desc_OreGold_C": _M("caterium_ore", "items/caterium_ore.json"),
    "Desc_CircuitBoard_C": _M("circuit_board", "items/circuit_board.json"),
    "Desc_Coal_C": _M("coal", "items/coal.json"),
    "Desc_CompactedCoal_C": _M("compacted_coal", "items/compacted_coal.json"),
    "Desc_Computer_C": _M("computer", "items/computer.json"),
    "Desc_Cement_C": _M("concrete", "items/concrete.json"),
    "Desc_CoolingSystem_C": _M("cooling_system", "items/cooling_system.json"),
    "Desc_CopperIngot_C": _M("copper_ingot", "items/copper_ingot.json"),
    "Desc_OreCopper_C": _M("copper_ore", "items/copper_ore.json"),
    "Desc_CopperDust_C": _M("copper_powder", "items/copper_powder.json"),
    "Desc_CopperSheet_C": _M("copper_sheet", "items/copper_sheet.json"),
    "Desc_LiquidOil_C": _M("crude_oil", "items/crude_oil.json"),
    "Desc_CrystalOscillator_C": _M("crystal_oscillator", "items/crystal_oscillator.json"),
    "Desc_CrystalShard_C": _M("power_shard", "items/power_shard.json"),
    "Desc_DarkMatter_C": _M("dark_matter_crystal", "items/dark_matter_crystal.json"),
    "Desc_DarkEnergy_C": _M("dark_matter_residue", "items/dark_matter_residue.json"),
    "Desc_Diamond_C": _M("diamonds", "items/diamonds.json"),
    "Desc_DissolvedSilica_C": _M("dissolved_silica", "items/dissolved_silica.json"),
    "Desc_ElectromagneticControlRod_C": _M("electromagnetic_control_rod", "items/electromagnetic_control_rod.json"),
    "Desc_GasTank_C": _M("empty_fluid_tank", "items/empty_fluid_tank.json"),
    "Desc_SteelPlateReinforced_C": _M("encased_industrial_beam", "items/encased_industrial_beam.json"),
    "Desc_PlutoniumCell_C": _M("encased_plutonium_cell", "items/encased_plutonium_cell.json"),
    "Desc_UraniumCell_C": _M("encased_uranium_cell", "items/encased_uranium_cell.json"),
    "Desc_QuantumEnergy_C": _M("excited_photonic_matter", "items/excited_photonic_matter.json"),
    "Desc_QuantumOscillator_C": _M("superposition_oscillator", "items/superposition_oscillator.json"),
    "Desc_FicsiteIngot_C": _M("ficsite_ingot", "items/ficsite_ingot.json"),
    "Desc_FicsiteMesh_C": _M("ficsite_trigon", "items/ficsite_trigon.json"),
    "Desc_Ficsonium_C": _M("ficsonium", "items/ficsonium.json"),
    "Desc_FicsoniumFuelRod_C": _M("ficsonium_fuel_rod", "items/ficsonium_fuel_rod.json"),
    "Desc_LiquidFuel_C": _M("fuel", "items/fuel.json"),
    "Desc_ModularFrameFused_C": _M("fused_modular_frame", "items/fused_modular_frame.json"),
    "Desc_AluminumPlateReinforced_C": _M("heat_sink", "items/heat_sink.json"),
    "Desc_ModularFrameHeavy_C": _M("heavy_modular_frame", "items/heavy_modular_frame.json"),
    "Desc_HeavyOilResidue_C": _M("heavy_oil_residue", "items/heavy_oil_residue.json"),
    "Desc_HighSpeedConnector_C": _M("high_speed_connector", "items/high_speed_connector.json"),
    "Desc_IonizedFuel_C": _M("ionized_fuel", "items/ionized_fuel.json"),
    "Desc_IronIngot_C": _M("iron_ingot", "items/iron_ingot.json"),
    "Desc_OreIron_C": _M("iron_ore", "items/iron_ore.json"),
    "Desc_IronPlate_C": _M("iron_plate", "items/iron_plate.json"),
    "Desc_IronRod_C": _M("iron_rod", "items/iron_rod.json"),
    "Desc_Stone_C": _M("limestone", "items/limestone.json"),
    "Desc_ModularFrame_C": _M("modular_frame", "items/modular_frame.json"),
    "Desc_Motor_C": _M("motor", "items/motor.json"),
    "Desc_NitricAcid_C": _M("nitric_acid", "items/nitric_acid.json"),
    "Desc_NitrogenGas_C": _M("nitrogen_gas", "items/nitrogen_gas.json"),
    "Desc_NonFissibleUranium_C": _M("non_fissile_uranium", "items/non_fissile_uranium.json"),
    "Desc_SpaceElevatorPart_9_C": _M("nuclear_pasta", "items/nuclear_pasta.json"),
    "Desc_PackagedNitrogenGas_C": _M("packaged_nitrogen_gas", "items/packaged_nitrogen_gas.json"),
    "Desc_PetroleumCoke_C": _M("petroleum_coke", "items/petroleum_coke.json"),
    "Desc_Plastic_C": _M("plastic", "items/plastic.json"),
    "Desc_PlutoniumFuelRod_C": _M("plutonium_fuel_rod", "items/plutonium_fuel_rod.json"),
    "Desc_PlutoniumPellet_C": _M("plutonium_pellet", "items/plutonium_pellet.json"),
    "Desc_PlutoniumWaste_C": _M("plutonium_waste", "items/plutonium_waste.json"),
    "Desc_PolymerResin_C": _M("polymer_resin", "items/polymer_resin.json"),
    "Desc_PressureConversionCube_C": _M("pressure_conversion_cube", "items/pressure_conversion_cube.json"),
    "Desc_QuartzCrystal_C": _M("quartz_crystal", "items/quartz_crystal.json"),
    "Desc_HighSpeedWire_C": _M("quickwire", "items/quickwire.json"),
    "Desc_ModularFrameLightweight_C": _M("radio_control_unit", "items/radio_control_unit.json"),
    "Desc_RawQuartz_C": _M("raw_quartz", "items/raw_quartz.json"),
    "Desc_IronPlateReinforced_C": _M("reinforced_iron_plate", "items/reinforced_iron_plate.json"),
    "Desc_RocketFuel_C": _M("rocket_fuel", "items/rocket_fuel.json"),
    "Desc_Rotor_C": _M("rotor", "items/rotor.json"),
    "Desc_Rubber_C": _M("rubber", "items/rubber.json"),
    "Desc_SAM_C": _M("sam", "items/sam.json"),
    "Desc_SAMFluctuator_C": _M("sam_fluctuator", "items/sam_fluctuator.json"),
    "Desc_SAMIngot_C": _M("reanimated_sam", "items/reanimated_sam.json"),
    "Desc_Silica_C": _M("silica", "items/silica.json"),
    "Desc_SingularityCell_C": _M("singularity_cell", "items/singularity_cell.json"),
    "Desc_SpaceElevatorPart_1_C": _M("smart_plating", "items/smart_plating.json"),
    "Desc_SpaceElevatorPart_12_C": _M("ai_expansion_server", "items/ai_expansion_server.json"),
    "Desc_SpaceElevatorPart_2_C": _M("versatile_framework", "items/versatile_framework.json"),
    "Desc_SpaceElevatorPart_4_C": _M("modular_engine", "items/modular_engine.json"),
    "Desc_SpaceElevatorPart_6_C": _M("magnetic_field_generator", "items/magnetic_field_generator.json"),
    "Desc_SpaceElevatorPart_8_C": _M("thermal_propulsion_rocket", "items/thermal_propulsion_rocket.json"),
    "Desc_Stator_C": _M("stator", "items/stator.json"),
    "Desc_SteelPlate_C": _M("steel_beam", "items/steel_beam.json"),
    "Desc_SteelIngot_C": _M("steel_ingot", "items/steel_ingot.json"),
    "Desc_SteelPipe_C": _M("steel_pipe", "items/steel_pipe.json"),
    "Desc_Sulfur_C": _M("sulfur", "items/sulfur.json"),
    "Desc_SulfuricAcid_C": _M("sulfuric_acid", "items/sulfuric_acid.json"),
    "Desc_ComputerSuper_C": _M("supercomputer", "items/supercomputer.json"),
    "Desc_IronScrew_C": _M("screws", "items/screws.json"),
    "Desc_TemporalProcessor_C": _M("neural_quantum_processor", "items/neural_quantum_processor.json"),
    "Desc_TimeCrystal_C": _M("time_crystal", "items/time_crystal.json"),
    "Desc_MotorLightweight_C": _M("turbo_motor", "items/turbo_motor.json"),
    "Desc_LiquidTurboFuel_C": _M("turbofuel", "items/turbofuel.json"),
    "Desc_OreUranium_C": _M("uranium", "items/uranium.json"),
    "Desc_NuclearFuelRod_C": _M("uranium_fuel_rod", "items/uranium_fuel_rod.json"),
    "Desc_NuclearWaste_C": _M("uranium_waste", "items/uranium_waste.json"),
    "Desc_Water_C": _M("water", "items/water.json"),
    "Desc_Wire_C": _M("wire", "items/wire.json"),
}

RECIPE_MANIFEST = {
    "Recipe_AILimiter_C": _M("ai_limiter", "recipes/assembler/ai_limiter.json"),
    "Recipe_Alternate_AILimiter_Plastic_C": _M("plastic_ai_limiter", "recipes/assembler/plastic_ai_limiter.json"),
    "Recipe_Alternate_AdheredIronPlate_C": _M("adhered_iron_plate", "recipes/assembler/adhered_iron_plate.json"),
    "Recipe_Alternate_AlcladCasing_C": _M("alclad_casing", "recipes/assembler/alclad_casing.json"),
    "Recipe_Alternate_AluminumRod_C": _M("aluminum_rod", "recipes/constructor/aluminum_rod.json"),
    "Recipe_Alternate_BoltedFrame_C": _M("bolted_frame", "recipes/assembler/bolted_frame.json"),
    "Recipe_Alternate_Cable_1_C": _M("insulated_cable", "recipes/assembler/insulated_cable.json"),
    "Recipe_Alternate_Cable_2_C": _M("quickwire_cable", "recipes/assembler/quickwire_cable.json"),
    "Recipe_Alternate_CateriumIngot_Tempered_C": _M("tempered_caterium_ingot", "recipes/foundry/tempered_caterium_ingot.json"),
    "Recipe_Alternate_CircuitBoard_1_C": _M("silicon_circuit_board", "recipes/assembler/silicon_circuit_board.json"),
    "Recipe_Alternate_CircuitBoard_2_C": _M("caterium_circuit_board", "recipes/assembler/caterium_circuit_board.json"),
    "Recipe_Alternate_ClassicBattery_C": _M("classic_battery", "recipes/manufacturer/classic_battery.json"),
    "Recipe_Alternate_CoatedCable_C": _M("coated_cable", "recipes/refinery/coated_cable.json"),
    "Recipe_Alternate_CoatedIronPlate_C": _M("coated_iron_plate", "recipes/assembler/coated_iron_plate.json"),
    "Recipe_Alternate_CokeSteelIngot_C": _M("coke_steel_ingot", "recipes/foundry/coke_steel_ingot.json"),
    "Recipe_Alternate_Computer_1_C": _M("caterium_computer", "recipes/manufacturer/caterium_computer.json"),
    "Recipe_Alternate_Computer_2_C": _M("crystal_computer", "recipes/assembler/crystal_computer.json"),
    "Recipe_Alternate_Concrete_C": _M("fine_concrete", "recipes/assembler/fine_concrete.json"),
    "Recipe_Alternate_CoolingDevice_C": _M("cooling_device", "recipes/blender/cooling_device.json"),
    "Recipe_Alternate_CopperAlloyIngot_C": _M("copper_alloy_ingot", "recipes/foundry/copper_alloy_ingot.json"),
    "Recipe_Alternate_CopperIngot_Tempered_C": _M("tempered_copper_ingot", "recipes/foundry/tempered_copper_ingot.json"),
    "Recipe_Alternate_CopperRotor_C": _M("copper_rotor", "recipes/assembler/copper_rotor.json"),
    "Recipe_Alternate_CrystalOscillator_C": _M("insulated_crystal_oscillator", "recipes/manufacturer/insulated_crystal_oscillator.json"),
    "Recipe_Alternate_DarkMatter_Crystallization_C": _M("dark_matter_crystallization", "recipes/accelerator/dark_matter_crystallization.json"),
    "Recipe_Alternate_DarkMatter_Trap_C": _M("dark_matter_trap", "recipes/accelerator/dark_matter_trap.json"),
    "Recipe_Alternate_Diamond_Cloudy_C": _M("cloudy_diamonds", "recipes/accelerator/cloudy_diamonds.json"),
    "Recipe_Alternate_Diamond_OilBased_C": _M("oil_based_diamonds", "recipes/accelerator/oil_based_diamonds.json"),
    "Recipe_Alternate_Diamond_Petroleum_C": _M("petroleum_diamonds", "recipes/accelerator/petroleum_diamonds.json"),
    "Recipe_Alternate_Diamond_Pink_C": _M("pink_diamonds", "recipes/converter/pink_diamonds.json"),
    "Recipe_Alternate_ElectricMotor_C": _M("electric_motor", "recipes/assembler/electric_motor.json"),
    "Recipe_Alternate_ElectroAluminumScrap_C": _M("electrode_aluminum_scrap", "recipes/refinery/electrode_aluminum_scrap.json"),
    "Recipe_Alternate_ElectrodeCircuitBoard_C": _M("electrode_circuit_board", "recipes/assembler/electrode_circuit_board.json"),
    "Recipe_Alternate_ElectromagneticControlRod_1_C": _M("electromagnetic_connection_rod", "recipes/assembler/electromagnetic_connection_rod.json"),
    "Recipe_Alternate_DilutedFuel_C": _M("diluted_fuel", "recipes/blender/diluted_fuel.json"),
    "Recipe_Alternate_EncasedIndustrialBeam_C": _M("encased_industrial_pipe", "recipes/assembler/encased_industrial_pipe.json"),
    "Recipe_Alternate_EnrichedCoal_C": _M("compacted_coal", "recipes/assembler/compacted_coal.json"),
    "Recipe_Alternate_FertileUranium_C": _M("fertile_uranium", "recipes/blender/fertile_uranium.json"),
    "Recipe_Alternate_FusedWire_C": _M("fused_wire", "recipes/assembler/fused_wire.json"),
    "Recipe_Alternate_HeatFusedFrame_C": _M("heat_fused_frame", "recipes/blender/heat_fused_frame.json"),
    "Recipe_Alternate_HeatSink_1_C": _M("heat_exchanger", "recipes/assembler/heat_exchanger.json"),
    "Recipe_Alternate_HeavyFlexibleFrame_C": _M("heavy_flexible_frame", "recipes/manufacturer/heavy_flexible_frame.json"),
    "Recipe_Alternate_HeavyOilResidue_C": _M("heavy_oil_residue", "recipes/refinery/heavy_oil_residue.json"),
    "Recipe_Alternate_HighSpeedConnector_C": _M("silicon_high_speed_connector", "recipes/manufacturer/silicon_high_speed_connector.json"),
    "Recipe_Alternate_IngotIron_C": _M("iron_alloy_ingot", "recipes/foundry/iron_alloy_ingot.json"),
    "Recipe_Alternate_IngotSteel_1_C": _M("solid_steel_ingot", "recipes/foundry/solid_steel_ingot.json"),
    "Recipe_Alternate_IngotSteel_2_C": _M("compacted_steel_ingot", "recipes/foundry/compacted_steel_ingot.json"),
    "Recipe_Alternate_InstantPlutoniumCell_C": _M("instant_plutonium_cell", "recipes/accelerator/instant_plutonium_cell.json"),
    "Recipe_Alternate_InstantScrap_C": _M("instant_scrap", "recipes/blender/instant_scrap.json"),
    "Recipe_Alternate_IronIngot_Basic_C": _M("basic_iron_ingot", "recipes/foundry/basic_iron_ingot.json"),
    "Recipe_Alternate_ModularFrame_C": _M("steeled_frame", "recipes/assembler/steeled_frame.json"),
    "Recipe_Alternate_ModularFrameHeavy_C": _M("heavy_encased_frame", "recipes/manufacturer/heavy_encased_frame.json"),
    "Recipe_Alternate_NuclearFuelRod_1_C": _M("uranium_fuel_unit", "recipes/manufacturer/uranium_fuel_unit.json"),
    "Recipe_Alternate_OCSupercomputer_C": _M("oc_supercomputer", "recipes/assembler/oc_supercomputer.json"),
    "Recipe_Alternate_Plastic_1_C": _M("recycled_plastic", "recipes/refinery/recycled_plastic.json"),
    "Recipe_Alternate_PlutoniumFuelUnit_C": _M("plutonium_fuel_unit", "recipes/assembler/plutonium_fuel_unit.json"),
    "Recipe_Alternate_PolymerResin_C": _M("polymer_resin", "recipes/refinery/polymer_resin.json"),
    "Recipe_Alternate_PureCateriumIngot_C": _M("pure_caterium_ingot", "recipes/refinery/pure_caterium_ingot.json"),
    "Recipe_Alternate_PureCopperIngot_C": _M("pure_copper_ingot", "recipes/refinery/pure_copper_ingot.json"),
    "Recipe_Alternate_PureIronIngot_C": _M("pure_iron_ingot", "recipes/refinery/pure_iron_ingot.json"),
    "Recipe_Alternate_PureQuartzCrystal_C": _M("pure_quartz_crystal", "recipes/refinery/pure_quartz_crystal.json"),
    "Recipe_Alternate_Quartz_Fused_C": _M("fused_quartz_crystal", "recipes/foundry/fused_quartz_crystal.json"),
    "Recipe_Alternate_Quartz_Purified_C": _M("quartz_purification", "recipes/refinery/quartz_purification.json"),
    "Recipe_Alternate_Quickwire_C": _M("fused_quickwire", "recipes/assembler/fused_quickwire.json"),
    "Recipe_Alternate_RadioControlSystem_C": _M("radio_control_system", "recipes/manufacturer/radio_control_system.json"),
    "Recipe_Alternate_RadioControlUnit_1_C": _M("radio_connection_unit", "recipes/manufacturer/radio_connection_unit.json"),
    "Recipe_Alternate_RecycledRubber_C": _M("recycled_rubber", "recipes/refinery/recycled_rubber.json"),
    "Recipe_Alternate_ReinforcedIronPlate_1_C": _M("bolted_iron_plate", "recipes/assembler/bolted_iron_plate.json"),
    "Recipe_Alternate_ReinforcedIronPlate_2_C": _M("stitched_iron_plate", "recipes/assembler/stitched_iron_plate.json"),
    "Recipe_Alternate_RocketFuel_Nitro_C": _M("nitro_rocket_fuel", "recipes/blender/nitro_rocket_fuel.json"),
    "Recipe_Alternate_Rotor_C": _M("steel_rotor", "recipes/assembler/steel_rotor.json"),
    "Recipe_Alternate_RubberConcrete_C": _M("rubber_concrete", "recipes/assembler/rubber_concrete.json"),
    "Recipe_Alternate_Screw_2_C": _M("steel_screw", "recipes/constructor/steel_screw.json"),
    "Recipe_Alternate_Screw_C": _M("cast_screw", "recipes/constructor/cast_screw.json"),
    "Recipe_Alternate_Silica_C": _M("cheap_silica", "recipes/assembler/cheap_silica.json"),
    "Recipe_Alternate_Silica_Distilled_C": _M("distilled_silica", "recipes/blender/distilled_silica.json"),
    "Recipe_Alternate_SloppyAlumina_C": _M("sloppy_alumina", "recipes/refinery/sloppy_alumina.json"),
    "Recipe_Alternate_Stator_C": _M("quickwire_stator", "recipes/assembler/quickwire_stator.json"),
    "Recipe_Alternate_SteelBeam_Aluminum_C": _M("aluminum_beam", "recipes/constructor/aluminum_beam.json"),
    "Recipe_Alternate_SteelBeam_Molded_C": _M("molded_beam", "recipes/foundry/molded_beam.json"),
    "Recipe_Alternate_SteelCastedPlate_C": _M("steel_cast_plate", "recipes/foundry/steel_cast_plate.json"),
    "Recipe_Alternate_SteelPipe_Iron_C": _M("iron_pipe", "recipes/constructor/iron_pipe.json"),
    "Recipe_Alternate_SteelPipe_Molded_C": _M("molded_steel_pipe", "recipes/foundry/molded_steel_pipe.json"),
    "Recipe_Alternate_SteelRod_C": _M("steel_rod", "recipes/constructor/steel_rod.json"),
    "Recipe_Alternate_SuperStateComputer_C": _M("super_state_computer", "recipes/manufacturer/super_state_computer.json"),
    "Recipe_Alternate_TurboBlendFuel_C": _M("turbo_blend_fuel", "recipes/blender/turbo_blend_fuel.json"),
    "Recipe_Alternate_TurboHeavyFuel_C": _M("turbo_heavy_fuel", "recipes/refinery/turbo_heavy_fuel.json"),
    "Recipe_Alternate_TurboMotor_1_C": _M("turbo_electric_motor", "recipes/manufacturer/turbo_electric_motor.json"),
    "Recipe_Alternate_TurboPressureMotor_C": _M("turbo_pressure_motor", "recipes/manufacturer/turbo_pressure_motor.json"),
    "Recipe_Alternate_Turbofuel_C": _M("turbofuel", "recipes/refinery/turbofuel.json"),
    "Recipe_Alternate_UraniumCell_1_C": _M("infused_uranium_cell", "recipes/manufacturer/infused_uranium_cell.json"),
    "Recipe_Alternate_WetConcrete_C": _M("wet_concrete", "recipes/refinery/wet_concrete.json"),
    "Recipe_Alternate_Wire_1_C": _M("iron_wire", "recipes/constructor/iron_wire.json"),
    "Recipe_Alternate_Wire_2_C": _M("caterium_wire", "recipes/constructor/caterium_wire.json"),
    "Recipe_AlienPowerFuel_C": _M("alien_power_matrix", "recipes/quantum_encoder/alien_power_matrix.json"),
    "Recipe_AluminaSolution_C": _M("alumina_solution", "recipes/refinery/alumina_solution.json"),
    "Recipe_AluminumScrap_C": _M("aluminum_scrap", "recipes/refinery/aluminum_scrap.json"),
    "Recipe_AluminumCasing_C": _M("aluminum_casing", "recipes/constructor/aluminum_casing.json"),
    "Recipe_AluminumSheet_C": _M("alclad_aluminum_sheet", "recipes/assembler/alclad_aluminum_sheet.json"),
    "Recipe_Battery_C": _M("battery", "recipes/blender/battery.json"),
    "Recipe_Bauxite_Caterium_C": _M("bauxite_caterium", "recipes/converter/bauxite_caterium.json"),
    "Recipe_Bauxite_Copper_C": _M("bauxite_copper", "recipes/converter/bauxite_copper.json"),
    "Recipe_Cable_C": _M("cable", "recipes/constructor/cable.json"),
    "Recipe_Caterium_Copper_C": _M("caterium_ore_copper", "recipes/converter/caterium_ore_copper.json"),
    "Recipe_Caterium_Quartz_C": _M("caterium_ore_quartz", "recipes/converter/caterium_ore_quartz.json"),
    "Recipe_CircuitBoard_C": _M("circuit_board", "recipes/assembler/circuit_board.json"),
    "Recipe_Coal_Iron_C": _M("coal_iron", "recipes/converter/coal_iron.json"),
    "Recipe_Coal_Limestone_C": _M("coal_limestone", "recipes/converter/coal_limestone.json"),
    "Recipe_ComputerSuper_C": _M("supercomputer", "recipes/manufacturer/supercomputer.json"),
    "Recipe_Computer_C": _M("computer", "recipes/manufacturer/computer.json"),
    "Recipe_Concrete_C": _M("concrete", "recipes/constructor/concrete.json"),
    "Recipe_CoolingSystem_C": _M("cooling_system", "recipes/blender/cooling_system.json"),
    "Recipe_CopperDust_C": _M("copper_powder", "recipes/constructor/copper_powder.json"),
    "Recipe_CopperSheet_C": _M("copper_sheet", "recipes/constructor/copper_sheet.json"),
    "Recipe_Copper_Quartz_C": _M("copper_ore_quartz", "recipes/converter/copper_ore_quartz.json"),
    "Recipe_Copper_Sulfur_C": _M("copper_ore_sulfur", "recipes/converter/copper_ore_sulfur.json"),
    "Recipe_CrystalOscillator_C": _M("crystal_oscillator", "recipes/manufacturer/crystal_oscillator.json"),
    "Recipe_DarkEnergy_C": _M("dark_matter_residue", "recipes/converter/dark_matter_residue.json"),
    "Recipe_DarkMatter_C": _M("dark_matter_crystal", "recipes/accelerator/dark_matter_crystal.json"),
    "Recipe_Diamond_C": _M("diamonds", "recipes/accelerator/diamonds.json"),
    "Recipe_ElectromagneticControlRod_C": _M("electromagnetic_control_rod", "recipes/assembler/electromagnetic_control_rod.json"),
    "Recipe_EncasedIndustrialBeam_C": _M("encased_industrial_beam", "recipes/assembler/encased_industrial_beam.json"),
    "Recipe_FicsiteIngot_AL_C": _M("ficsite_ingot_aluminum", "recipes/converter/ficsite_ingot_aluminum.json"),
    "Recipe_FicsiteIngot_CAT_C": _M("ficsite_ingot_caterium", "recipes/converter/ficsite_ingot_caterium.json"),
    "Recipe_FicsiteIngot_Iron_C": _M("ficsite_ingot_iron", "recipes/converter/ficsite_ingot_iron.json"),
    "Recipe_FicsiteMesh_C": _M("ficsite_trigon", "recipes/constructor/ficsite_trigon.json"),
    "Recipe_FicsoniumFuelRod_C": _M("ficsonium_fuel_rod", "recipes/quantum_encoder/ficsonium_fuel_rod.json"),
    "Recipe_Ficsonium_C": _M("ficsonium", "recipes/accelerator/ficsonium.json"),
    "Recipe_FusedModularFrame_C": _M("fused_modular_frame", "recipes/blender/fused_modular_frame.json"),
    "Recipe_GasTank_C": _M("empty_fluid_tank", "recipes/constructor/empty_fluid_tank.json"),
    "Recipe_HeatSink_C": _M("heat_sink", "recipes/assembler/heat_sink.json"),
    "Recipe_HighSpeedConnector_C": _M("high_speed_connector", "recipes/manufacturer/high_speed_connector.json"),
    "Recipe_IngotAluminum_C": _M("aluminum_ingot", "recipes/foundry/aluminum_ingot.json"),
    "Recipe_IngotCaterium_C": _M("caterium_ingot", "recipes/smelter/caterium_ingot.json"),
    "Recipe_IngotCopper_C": _M("copper_ingot", "recipes/smelter/copper_ingot.json"),
    "Recipe_IngotIron_C": _M("iron_ingot", "recipes/smelter/iron_ingot.json"),
    "Recipe_IngotSAM_C": _M("reanimated_sam", "recipes/constructor/reanimated_sam.json"),
    "Recipe_IngotSteel_C": _M("steel_ingot", "recipes/foundry/steel_ingot.json"),
    "Recipe_IonizedFuel_C": _M("ionized_fuel", "recipes/refinery/ionized_fuel.json"),
    "Recipe_IronPlateReinforced_C": _M("reinforced_iron_plate", "recipes/assembler/reinforced_iron_plate.json"),
    "Recipe_IronPlate_C": _M("iron_plate", "recipes/constructor/iron_plate.json"),
    "Recipe_IronRod_C": _M("iron_rod", "recipes/constructor/iron_rod.json"),
    "Recipe_Iron_Limestone_C": _M("iron_ore_limestone", "recipes/converter/iron_ore_limestone.json"),
    "Recipe_Limestone_Sulfur_C": _M("limestone_sulfur", "recipes/converter/limestone_sulfur.json"),
    "Recipe_LiquidFuel_C": _M("fuel", "recipes/refinery/fuel.json"),
    "Recipe_ModularFrameHeavy_C": _M("heavy_modular_frame", "recipes/manufacturer/heavy_modular_frame.json"),
    "Recipe_ModularFrame_C": _M("modular_frame", "recipes/assembler/modular_frame.json"),
    "Recipe_MotorTurbo_C": _M("turbo_motor", "recipes/manufacturer/turbo_motor.json"),
    "Recipe_Motor_C": _M("motor", "recipes/assembler/motor.json"),
    "Recipe_NitricAcid_C": _M("nitric_acid", "recipes/blender/nitric_acid.json"),
    "Recipe_Nitrogen_Bauxite_C": _M("nitrogen_gas_bauxite", "recipes/converter/nitrogen_gas_bauxite.json"),
    "Recipe_Nitrogen_Caterium_C": _M("nitrogen_gas_caterium", "recipes/converter/nitrogen_gas_caterium.json"),
    "Recipe_NonFissileUranium_C": _M("non_fissile_uranium", "recipes/blender/non_fissile_uranium.json"),
    "Recipe_NuclearFuelRod_C": _M("uranium_fuel_rod", "recipes/manufacturer/uranium_fuel_rod.json"),
    "Recipe_PackagedNitrogen_C": _M("packaged_nitrogen_gas", "recipes/packager/packaged_nitrogen_gas.json"),
    "Recipe_PetroleumCoke_C": _M("petroleum_coke", "recipes/refinery/petroleum_coke.json"),
    "Recipe_Plastic_C": _M("plastic", "recipes/refinery/plastic.json"),
    "Recipe_PlutoniumCell_C": _M("encased_plutonium_cell", "recipes/assembler/encased_plutonium_cell.json"),
    "Recipe_PlutoniumFuelRod_C": _M("plutonium_fuel_rod", "recipes/manufacturer/plutonium_fuel_rod.json"),
    "Recipe_Plutonium_C": _M("plutonium_pellet", "recipes/accelerator/plutonium_pellet.json"),
    "Recipe_PressureConversionCube_C": _M("pressure_conversion_cube", "recipes/assembler/pressure_conversion_cube.json"),
    "Recipe_PureAluminumIngot_C": _M("pure_aluminum_ingot", "recipes/smelter/pure_aluminum_ingot.json"),
    "Recipe_QuantumEnergy_C": _M("excited_photonic_matter", "recipes/converter/excited_photonic_matter.json"),
    "Recipe_QuartzCrystal_C": _M("quartz_crystal", "recipes/constructor/quartz_crystal.json"),
    "Recipe_Quartz_Bauxite_C": _M("raw_quartz_bauxite", "recipes/converter/raw_quartz_bauxite.json"),
    "Recipe_Quartz_Coal_C": _M("raw_quartz_coal", "recipes/converter/raw_quartz_coal.json"),
    "Recipe_Quickwire_C": _M("quickwire", "recipes/constructor/quickwire.json"),
    "Recipe_RadioControlUnit_C": _M("radio_control_unit", "recipes/manufacturer/radio_control_unit.json"),
    "Recipe_ResidualFuel_C": _M("residual_fuel", "recipes/refinery/residual_fuel.json"),
    "Recipe_ResidualPlastic_C": _M("residual_plastic", "recipes/refinery/residual_plastic.json"),
    "Recipe_ResidualRubber_C": _M("residual_rubber", "recipes/refinery/residual_rubber.json"),
    "Recipe_RocketFuel_C": _M("rocket_fuel", "recipes/blender/rocket_fuel.json"),
    "Recipe_Rotor_C": _M("rotor", "recipes/assembler/rotor.json"),
    "Recipe_Rubber_C": _M("rubber", "recipes/refinery/rubber.json"),
    "Recipe_SAMFluctuator_C": _M("sam_fluctuator", "recipes/manufacturer/sam_fluctuator.json"),
    "Recipe_Screw_C": _M("screws", "recipes/constructor/screws.json"),
    "Recipe_Silica_C": _M("silica", "recipes/constructor/silica.json"),
    "Recipe_SingularityCell_C": _M("singularity_cell", "recipes/manufacturer/singularity_cell.json"),
    "Recipe_SpaceElevatorPart_1_C": _M("smart_plating", "recipes/assembler/smart_plating.json"),
    "Recipe_SpaceElevatorPart_3_C": _M("automated_wiring", "recipes/assembler/automated_wiring.json"),
    "Recipe_SpaceElevatorPart_5_C": _M("adaptive_control_unit", "recipes/manufacturer/adaptive_control_unit.json"),
    "Recipe_SpaceElevatorPart_7_C": _M("assembly_director_system", "recipes/assembler/assembly_director_system.json"),
    "Recipe_SpaceElevatorPart_10_C": _M("biochemical_sculptor", "recipes/blender/biochemical_sculptor.json"),
    "Recipe_SpaceElevatorPart_11_C": _M("ballistic_warp_drive", "recipes/manufacturer/ballistic_warp_drive.json"),
    "Recipe_SpaceElevatorPart_12_C": _M("ai_expansion_server", "recipes/quantum_encoder/ai_expansion_server.json"),
    "Recipe_SpaceElevatorPart_9_C": _M("nuclear_pasta", "recipes/accelerator/nuclear_pasta.json"),
    "Recipe_SpaceElevatorPart_2_C": _M("versatile_framework", "recipes/assembler/versatile_framework.json"),
    "Recipe_SpaceElevatorPart_4_C": _M("modular_engine", "recipes/manufacturer/modular_engine.json"),
    "Recipe_SpaceElevatorPart_6_C": _M("magnetic_field_generator", "recipes/assembler/magnetic_field_generator.json"),
    "Recipe_SpaceElevatorPart_8_C": _M("thermal_propulsion_rocket", "recipes/manufacturer/thermal_propulsion_rocket.json"),
    "Recipe_Stator_C": _M("stator", "recipes/assembler/stator.json"),
    "Recipe_SteelBeam_C": _M("steel_beam", "recipes/constructor/steel_beam.json"),
    "Recipe_SteelPipe_C": _M("steel_pipe", "recipes/constructor/steel_pipe.json"),
    "Recipe_Sulfur_Coal_C": _M("sulfur_coal", "recipes/converter/sulfur_coal.json"),
    "Recipe_Sulfur_Iron_C": _M("sulfur_iron", "recipes/converter/sulfur_iron.json"),
    "Recipe_SulfuricAcid_C": _M("sulfuric_acid", "recipes/refinery/sulfuric_acid.json"),
    "Recipe_SuperpositionOscillator_C": _M("superposition_oscillator", "recipes/quantum_encoder/superposition_oscillator.json"),
    "Recipe_SyntheticPowerShard_C": _M("synthetic_power_shard", "recipes/quantum_encoder/synthetic_power_shard.json"),
    "Recipe_TemporalProcessor_C": _M("neural_quantum_processor", "recipes/quantum_encoder/neural_quantum_processor.json"),
    "Recipe_TimeCrystal_C": _M("time_crystal", "recipes/converter/time_crystal.json"),
    "Recipe_Uranium_Bauxite_C": _M("uranium_ore_bauxite", "recipes/converter/uranium_ore_bauxite.json"),
    "Recipe_UraniumCell_C": _M("encased_uranium_cell", "recipes/blender/encased_uranium_cell.json"),
    "Recipe_Wire_C": _M("wire", "recipes/constructor/wire.json"),
}


# --------------------------------------------------------------------------
# Docs loading + raw-field parsing
# --------------------------------------------------------------------------

DOCS_RELATIVE = Path("CommunityResources/Docs/en-US.json")

_FLUID_FORMS = {"RF_LIQUID", "RF_GAS"}


def _nc_tail(native_class: str) -> str:
    """Short class name from a NativeClass string, e.g. '"...FGRecipe'" -> 'FGRecipe'."""
    return native_class.rsplit(".", 1)[-1].rstrip("'")


# ItemClass="/.../Desc_OreIron.Desc_OreIron_C'",Amount=1)
_AMOUNT_RE = re.compile(r'ItemClass="[^"]*\.([A-Za-z0-9_]+)\'",Amount=([0-9.]+)')
# mProducedIn: ("/Game/.../Build_SmelterMk1.Build_SmelterMk1_C",...)
_BUILD_RE = re.compile(r"Build_[A-Za-z0-9_]+_C")


def docs_path(game_dir: str | Path) -> Path:
    return Path(game_dir) / DOCS_RELATIVE


def load_docs(game_dir: str | Path) -> list[dict]:
    """Return the AutoJSON export's group list (each ``{NativeClass, Classes}``)."""
    p = docs_path(game_dir)
    if not p.is_file():
        raise FileNotFoundError(f"game docs export not found: {p}")
    raw = json.load(open(p, encoding="utf-16"))  # AutoJSON dump is UTF-16 LE
    return raw


def _amounts(text: str) -> list[tuple[str, float]]:
    return [(cls, float(amt)) for cls, amt in _AMOUNT_RE.findall(text)]


def _buildables(text: str) -> list[str]:
    """Raw ``Build_*_C`` class names listed in an ``mProducedIn`` string."""
    return _BUILD_RE.findall(text)


# --------------------------------------------------------------------------
# Extraction to our internal format
# --------------------------------------------------------------------------


_ITEM_GROUPS = ("FGItemDescriptor", "FGResourceDescriptor", "FGConsumableDescriptor", "FGPowerShardDescriptor")


def item_form(docs: list[dict]) -> dict[str, str]:
    """Map every game item ClassName to its form (``RF_SOLID``/``RF_LIQUID``/``RF_GAS``)."""
    out: dict[str, str] = {}
    for g in docs:
        nc = _nc_tail(g["NativeClass"])
        if not any(nc.startswith(t) for t in _ITEM_GROUPS):
            continue
        for item in g["Classes"]:
            out[item["ClassName"]] = item.get("mForm", "RF_SOLID")
    return out


#: NativeClass groups whose classes are factory buildings with a power draw,
#: an overclockability flag and a ProducedIn role. The set includes generator,
#: extractor (incl. the well pressurizer, which is a FrackingActivator) and
#: water-pump groups.
_BUILD_GROUPS = (
    "FGBuildableManufacturer",
    "FGBuildableResourceExtractor",
    "FGBuildableGeneratorFuel",
    "FGBuildableGeneratorGeoThermal",
    "FGBuildableGeneratorNuclear",
    "FGBuildableWaterPump",
    "FGBuildableFrackingActivator",
    "FGBuildableFrackingExtractor",
)


def _true(s: object) -> bool:
    """Parse AutoJSON booleans, which are exported as the strings 'True'/'False'."""
    if isinstance(s, str):
        return s.strip().lower() in ("true", "1")
    return bool(s)


def machine_power(docs: list[dict]) -> dict[str, float]:
    """Map every buildable ClassName to its base power consumption (MW)."""
    out: dict[str, float] = {}
    for g in docs:
        nc = _nc_tail(g["NativeClass"])
        if any(t in nc for t in _BUILD_GROUPS):
            for b in g["Classes"]:
                out[b["ClassName"]] = float(b.get("mPowerConsumption", 0.0))
    return out


def machine_overclockable(docs: list[dict]) -> dict[str, bool]:
    """Map buildable ClassName -> whether it can be overclocked (mCanChangePotential)."""
    out: dict[str, bool] = {}
    for g in docs:
        nc = _nc_tail(g["NativeClass"])
        if any(t in nc for t in _BUILD_GROUPS):
            for b in g["Classes"]:
                out[b["ClassName"]] = _true(b.get("mCanChangePotential", True))
    return out


def _rate(amount: float, duration: float, form: str) -> float:
    """Per-minute rate at 100% clock; fluids/gases in m³/min (game stores ×1000)."""
    per_min = amount * 60.0 / duration
    if form in _FLUID_FORMS:
        per_min /= 1000.0
    return per_min


def _find_docs_class(docs, native_class: str, game_class: str) -> dict:
    for g in docs:
        if _nc_tail(g["NativeClass"]) == native_class:
            for c in g["Classes"]:
                if c["ClassName"] == game_class:
                    return c
    raise KeyError(f"no {native_class} '{game_class}' in docs")


def _rates_dict(text, duration, item_forms, items_by_class) -> dict[str, float]:
    out: dict[str, float] = {}
    for cls, amt in _amounts(text):
        our = items_by_class.get(cls, cls)  # unmapped items keep their ClassName
        out[our] = _rate(amt, duration, item_forms.get(cls, "RF_SOLID"))
    return out


def _first_machine(r: dict, machine_ids: dict[str, str]) -> str:
    for b in _buildables(r.get("mProducedIn", "")):
        if b in machine_ids:
            return machine_ids[b]
    return "default"


def _class_record(docs: list[dict], game_class: str) -> tuple[dict | None, str | None]:
    """The raw docs class dict for a ClassName, plus its NativeClass group tail."""
    for g in docs:
        for c in g["Classes"]:
            if c["ClassName"] == game_class:
                return c, _nc_tail(g["NativeClass"])
    return None, None


def _sink_points(docs, game_class) -> int:
    for g in docs:
        nc = _nc_tail(g["NativeClass"])
        if not any(nc.startswith(t) for t in _ITEM_GROUPS):
            continue
        for item in g["Classes"]:
            if item["ClassName"] == game_class:
                return int(item.get("mResourceSinkPoints", 0.0))
    return 0


# --------------------------------------------------------------------------
# Pretty-print: repo hand-format JSON (2-space indent, nested containers inline)
# --------------------------------------------------------------------------

_RATE_DECIMALS = 8  # repo stores per-minute rates to 8 decimals (e.g. 1.66666667)


def _format_json(obj) -> str:
    """Render JSON in the repo's hand-format: 2-space indent, nested containers inline."""

    def _inline(v):
        if isinstance(v, dict):
            if not v:
                return "{}"
            return "{" + ", ".join(f"{json.dumps(k)}: {_inline(x)}" for k, x in v.items()) + "}"
        if isinstance(v, (list, tuple)):
            return "[" + ", ".join(_inline(x) for x in v) + "]"
        return json.dumps(v)

    def _render(v, level: int) -> str:
        if isinstance(v, dict):
            if not v:
                return "  " * level + "{}"
            pad = "  " * level
            items = list(v.items())
            lines = [pad + "{"]
            for i, (k, x) in enumerate(items):
                comma = "," if i < len(items) - 1 else ""
                if isinstance(x, (dict, list)):
                    lines.append(f"{pad}  {json.dumps(k)}: {_inline(x)}{comma}")
                else:
                    lines.append(f"{pad}  {json.dumps(k)}: {json.dumps(x)}{comma}")
            lines.append(pad + "}")
            return "\n".join(lines)
        return json.dumps(v)

    return _render(obj, 0)


def _round_rates(d: dict, ndigits: int) -> dict:
    return {k: round(float(v), ndigits) for k, v in d.items()}


# --------------------------------------------------------------------------
# Lift commands: lift ONE object from the docs, pretty-print it (stdout JSON,
# warnings to stderr). Only used for human-driven data entry.
# --------------------------------------------------------------------------


def _suggest_id(display_name: str) -> str:
    """A lowercase snake_case id suggested from the en-US display name.

    Only a *suggestion* (and only used when the manifest has no entry and the
    caller did not pass an id); the user renames freely.
    """
    s = re.sub(r"^Alternate:\s*", "", display_name or "")
    s = re.sub(r"[^A-Za-z0-9]+", "_", s.strip()).strip("_")
    return s.lower()


# --------------------------------------------------------------------------
# Name resolution: lift commands take a public display name (or a ClassName)
# --------------------------------------------------------------------------

_CLASS_RE = re.compile(r"^(Recipe|Desc|Build)_[A-Za-z0-9_]+_C$")


def _group_records(docs, native_class: str) -> list[tuple[str, str]]:
    """All ``(ClassName, mDisplayName)`` pairs in the exact-matching NativeClass group."""
    for g in docs:
        if _nc_tail(g["NativeClass"]) == native_class:
            return [(c["ClassName"], c.get("mDisplayName", "")) for c in g["Classes"]]
    return []


def _recipe_candidates(docs) -> list[tuple[str, str]]:
    return _group_records(docs, "FGRecipe")


def _item_candidates(docs) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for g in docs:
        nc = _nc_tail(g["NativeClass"])
        if any(nc.startswith(t) for t in _ITEM_GROUPS):
            out += [(c["ClassName"], c.get("mDisplayName", "")) for c in g["Classes"]]
    return out


def _machine_candidates(docs) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for g in docs:
        nc = _nc_tail(g["NativeClass"])
        if any(t in nc for t in _BUILD_GROUPS):
            out += [(c["ClassName"], c.get("mDisplayName", "")) for c in g["Classes"]]
    return out


def _looks_like_class_name(s: str) -> bool:
    return bool(_CLASS_RE.match(s or ""))


def _norm_display(s: str) -> str:
    """Normalised name for matching: lowercase, 'Alternate: ' dropped, words only."""
    s = (s or "").lower()
    s = re.sub(r"^alternate:\s+", "", s)
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def _ambiguous(query: str, what: str, matches: list[tuple[str, str]]) -> KeyError:
    listing = ", ".join(n or c for c, n in matches[:8])
    extra = " …" if len(matches) > 8 else ""
    return KeyError(
        f"{query!r} is ambiguous — {what}s it could be: {listing}{extra}. "
        f"Be more specific or pass the ClassName."
    )


def _resolve_query(candidates: list[tuple[str, str]], query: str, what: str) -> tuple[str, str]:
    """Resolve a query to ``(ClassName, display name)``.

    A literal ClassName (``Recipe_/Desc_/Build_..._C``) is returned as-is; any
    other input is treated as a display-name fragment — case-insensitive, with
    the "Alternate: " prefix optional — preferring an exact name match, then a
    unique substring match. Raises ``KeyError`` with a helpful message when
    nothing matches or several things do.
    """
    nq = _norm_display(query)
    if not nq:
        raise KeyError(f"empty {what} query")
    if _looks_like_class_name(query):
        for c, n in candidates:
            if c == query:
                return c, n
        raise KeyError(f"no {what} class '{query}' in the docs")
    exact = [(c, n) for c, n in candidates if _norm_display(n) == nq]
    if len(exact) == 1:
        return exact[0]
    if len(exact) > 1:
        raise _ambiguous(query, what, exact)
    subs = [(c, n) for c, n in candidates if nq in _norm_display(n)]
    if len(subs) == 1:
        return subs[0]
    if not subs:
        raise KeyError(f"no {what} matching {query!r} in the docs")
    raise _ambiguous(query, what, subs)


def _recipes_for_item(docs: list[dict], item_class: str) -> list[str]:
    """Public display names of every FGRecipe in the docs producing ``item_class``."""
    found: set[str] = set()
    for g in docs:
        if _nc_tail(g["NativeClass"]) != "FGRecipe":
            continue
        for r in g["Classes"]:
            products = _amounts(r.get("mProduct", ""))
            if any(cls == item_class for cls, _ in products):
                found.add(r.get("mDisplayName", r["ClassName"]))
    return sorted(found, key=str.lower)


def _recipes_by_machine(docs: list[dict], machine_class: str) -> list[str]:
    """Public display names of every FGRecipe produced in ``machine_class``."""
    found: set[str] = set()
    for g in docs:
        if _nc_tail(g["NativeClass"]) != "FGRecipe":
            continue
        for r in g["Classes"]:
            if machine_class in _buildables(r.get("mProducedIn", "")):
                found.add(r.get("mDisplayName", r["ClassName"]))
    return sorted(found, key=str.lower)


def _emit(data: dict, notes: list[str]) -> int:
    for n in notes:
        print(f"# {n}", file=sys.stderr)
    print(_format_json(data))
    return 0


def lift_item(docs, name_or_class: str, our_id: str | None = None) -> tuple[dict, list[str]]:
    """Lift one item descriptor into our item shape (id, name, sinkable, sink_points).

    ``name_or_class`` is a public display name (e.g. "Screws") or a game
    ClassName (e.g. Desc_IronScrew_C); resolved automatically.
    """
    class_name, name = _resolve_query(_item_candidates(docs), name_or_class, "item")
    forms = item_form(docs)
    notes = []
    entry = ITEM_MANIFEST.get(class_name)
    if entry is None:
        notes.append("new item — not in ITEM_MANIFEST; id suggested from the display name")
    item_id = our_id or (entry.id if entry else _suggest_id(name))
    if forms.get(class_name, "RF_SOLID") in _FLUID_FORMS:
        data = {"id": item_id, "name": name, "sinkable": False, "sink_points": 0}
    else:
        data = {"id": item_id, "name": name, "sinkable": True, "sink_points": _sink_points(docs, class_name)}
    return data, notes


def lift_machine(docs, name_or_class: str, our_id: str | None = None) -> tuple[dict, list[str]]:
    """Lift one buildable into our machine spec (power + overclockable from docs,
    max_sloops from the manifest — it is not in the docs).

    ``name_or_class`` is a public display name (e.g. "Coal-Powered Generator")
    or a game ClassName (e.g. Build_GeneratorCoal_C); resolved automatically.
    """
    class_name, name = _resolve_query(_machine_candidates(docs), name_or_class, "machine")
    power = machine_power(docs)
    oc = machine_overclockable(docs)
    entry = MACHINE_MANIFEST.get(class_name)
    if entry is None:
        # The docs don't export sloop capacity, so no lift can provide it.
        # Refuse rather than emit a plausible-looking record with a silent 3.
        raise KeyError(
            f"{class_name} ('{name}') has no recorded max_sloops — it is not in "
            "MACHINE_MANIFEST, and the game docs do not export sloop capacity. "
            "Add it to MACHINE_MANIFEST (with the hand-confirmed max_sloops) "
            "before lifting it."
        )
    notes = []
    raw, _ = _class_record(docs, class_name)
    if raw is not None and "mEstimatedMininumPowerConsumption" in raw:
        # variable-power machines (Converter, Quantum Encoder...) export
        # mPowerConsumption=0; their real draw is a range. Never let 0.0 through
        # silently.
        lo = float(raw.get("mEstimatedMininumPowerConsumption", 0.0))
        hi = float(raw.get("mEstimatedMaximumPowerConsumption", lo))
        notes.append(
            f"variable-power machine (FGBuildableManufacturerVariablePower): "
            f"mPowerConsumption is 0 but actual draw is {lo:g}–{hi:g} MW — "
            f"decide how to model power_draw before saving"
        )
    data = {
        "id": our_id or entry.id,
        "name": name,
        "power_draw": power.get(class_name, 0.0),
        "max_sloops": entry.max_sloops,
        "overclockable": oc.get(class_name, True),
    }
    return data, notes


def lift_recipe(docs, name_or_class: str, our_id: str | None = None) -> tuple[dict, list[str]]:
    """Lift one FGRecipe into our recipe shape (id, name, machine, per-min rates).

    ``name_or_class`` is a public display name (e.g. "Pure Copper Ingot",
    "Alternate: " prefix optional) or a game ClassName (e.g.
    Recipe_Alternate_PureCopperIngot_C); resolved automatically.
    """
    class_name, name = _resolve_query(_recipe_candidates(docs), name_or_class, "recipe")
    r = _find_docs_class(docs, "FGRecipe", class_name)
    duration = float(r["mManufactoringDuration"])
    forms = item_form(docs)
    items_by_class = {cls: m.id for cls, m in ITEM_MANIFEST.items()}
    machine_ids = {cls: m.id for cls, m in MACHINE_MANIFEST.items()}
    machine = _first_machine(r, machine_ids)
    entry = RECIPE_MANIFEST.get(class_name)

    notes = []
    if entry is None:
        notes.append(f"new recipe — not in RECIPE_MANIFEST; id suggested from the display name")
    if machine == "default":
        built_in = ", ".join(_buildables(r.get("mProducedIn", ""))) or "(no mProducedIn)"
        notes.append(f"machine unknown — produced in: {built_in} (not in MACHINE_MANIFEST; add the machine first)")

    def _lifted(text) -> dict[str, float]:
        lifted = _rates_dict(text, duration, forms, items_by_class)
        for k in lifted:
            if k.endswith("_C"):  # unmapped item kept its ClassName
                notes.append(f"input/output item '{k}' not in ITEM_MANIFEST — map it to a repo item id")
        return _round_rates(lifted, _RATE_DECIMALS)

    data = {
        "id": our_id or (entry.id if entry else _suggest_id(name)),
        "name": name,
        "machine": machine,
        "inputs": _lifted(r["mIngredients"]),
        "outputs": _lifted(r["mProduct"]),
    }
    return data, notes


# --------------------------------------------------------------------------
# Whole-object diff (read-only consistency check against the repo's JSON)
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class _Diff:
    path: str
    field: str
    game: object
    repo: object = None


def _extract_recipe_for(docs, game_class: str) -> dict:
    from_manifest = RECIPE_MANIFEST[game_class]
    data, _ = lift_recipe(docs, game_class, from_manifest.id)
    return data


def _extract_item_for(docs, game_class: str) -> dict:
    from_manifest = ITEM_MANIFEST[game_class]
    data, _ = lift_item(docs, game_class, from_manifest.id)
    return data


def _extract_machine_for(docs, game_class: str) -> dict:
    entry = MACHINE_MANIFEST[game_class]
    data, _ = lift_machine(docs, game_class, entry.id)
    return data


def compare_recipe(docs, game_class: str, entry: _M, repo_path: str | Path) -> list[_Diff]:
    """Extract one recipe from the game and diff it against our JSON file."""
    game = _extract_recipe_for(docs, game_class)
    diffs: list[_Diff] = []
    repo = json.load(open(repo_path))
    if repo.get("name") != game["name"]:
        diffs.append(_Diff(entry.path, "name", game["name"], repo.get("name")))
    if _round_rates(repo.get("inputs", {}), 7) != _round_rates(game["inputs"], 7):
        diffs.append(_Diff(entry.path, "inputs", game["inputs"], repo.get("inputs")))
    if _round_rates(repo.get("outputs", {}), 7) != _round_rates(game["outputs"], 7):
        diffs.append(_Diff(entry.path, "outputs", game["outputs"], repo.get("outputs")))
    if repo.get("machine") != game["machine"]:
        diffs.append(_Diff(entry.path, "machine", game["machine"], repo.get("machine")))
    # Variable-power machines (accelerator, converter, quantum encoder...) draw
    # per-recipe power the docs store as two fields: the draw oscillates during
    # a cycle between `constant` (min) and `constant + factor` (max), so the
    # steady scalar to model is the average = constant + factor/2. The repo may
    # model this per-recipe (a "power_draw" override) or as a single machine
    # average (e.g. the converter, uniform across recipes); only validate when
    # the repo declares an override (absent = machine average, legitimate).
    if "power_draw" in repo:
        raw = _find_docs_class(docs, "FGRecipe", game_class)
        c = float(raw.get("mVariablePowerConsumptionConstant", 0.0))
        f = float(raw.get("mVariablePowerConsumptionFactor", 0.0))
        expected = c + f / 2.0
        # 1.0 = the universal fixed-machine default (constant 1 + factor 0);
        # a recipe with that gets no meaningful override from the docs.
        if abs(expected - 1.0) > 1e-9 and abs(float(repo.get("power_draw", 0.0)) - expected) > 1e-6:
            diffs.append(_Diff(entry.path, "power_draw", expected, repo.get("power_draw")))
    return diffs


def compare_item(docs, game_class: str, entry: _M, repo_path: str | Path) -> list[_Diff]:
    game = _extract_item_for(docs, game_class)
    repo = json.load(open(repo_path))
    diffs: list[_Diff] = []
    if repo.get("name") != game["name"]:
        diffs.append(_Diff(entry.path, "name", game["name"], repo.get("name")))
    for key in ("sinkable", "sink_points"):
        if repo.get(key) != game[key]:
            diffs.append(_Diff(entry.path, key, game[key], repo.get(key)))
    return diffs


def compare_machine(docs, game_class: str, entry: _Machine, repo_path: str | Path) -> list[_Diff]:
    game = _extract_machine_for(docs, game_class)
    repo = json.load(open(repo_path))
    diffs: list[_Diff] = []
    if repo.get("name") != game["name"]:
        diffs.append(_Diff(entry.path, "name", game["name"], repo.get("name")))
    # Variable-power machines (FGBuildableManufacturerVariablePower: e.g. the
    # Converter) export mPowerConsumption=0 but carry their real draw as an
    # estimated [lo, hi] range. Our scalar is a hand-chosen point in that range
    # (the docs give no single authoritative value), so any value within it is
    # correct; a bare 0.0 (the game's placeholder) is not.
    raw, _ = _class_record(docs, game_class)
    if raw is not None and "mEstimatedMininumPowerConsumption" in raw:
        lo = float(raw.get("mEstimatedMininumPowerConsumption", 0.0))
        hi = float(raw.get("mEstimatedMaximumPowerConsumption", lo))
        repo_pw = float(repo.get("power_draw", 0.0))
        if not (lo - 1e-9 <= repo_pw <= hi + 1e-9):
            diffs.append(_Diff(entry.path, "power_draw", f"{lo:g}–{hi:g}", repo.get("power_draw")))
        overclockable = repo.get("overclockable", True)
        if abs(float(overclockable) - float(game.get("overclockable", True))) > 1e-9:
            diffs.append(_Diff(entry.path, "overclockable", game.get("overclockable"), repo.get("overclockable")))
        return diffs
    for key in ("power_draw", "overclockable"):
        # overclockable defaults to True in our loader even when absent
        repo_v = repo.get(key, True) if key == "overclockable" else repo.get(key, 0.0)
        if abs(float(repo_v) - float(game[key])) > 1e-9:
            diffs.append(_Diff(entry.path, key, game[key], repo.get(key)))
    return diffs


def build_report(game_dir: str | Path, project_root: str | Path = ".") -> str:
    """Extract everything in the manifests and diff against the repo JSON."""
    docs = load_docs(game_dir)
    root = Path(project_root)
    lines: list[str] = []
    diffs: list[tuple[str, _Diff]] = []
    counts = {"machines": 0, "items": 0, "recipes": 0}

    for group, manifest, cmp in (
        ("machines", MACHINE_MANIFEST, compare_machine),
        ("items", ITEM_MANIFEST, compare_item),
        ("recipes", RECIPE_MANIFEST, compare_recipe),
    ):
        counts[group] = len(manifest)
        for game_class, entry in sorted(manifest.items()):
            path = root / entry.path
            if not path.is_file():
                lines.append(f"  MISSING  {entry.path}  ({game_class})")
                continue
            for d in cmp(docs, game_class, entry, path):
                diffs.append((group, d))
                lines.append(f"  DIFF  {d.path}  {d.field}: game={d.game!r} repo={d.repo!r}  ({game_class})")

    n_diff_recipes = sum(1 for g, _ in diffs if g == "recipes")
    n_diff_items = sum(1 for g, _ in diffs if g == "items")
    n_diff_machines = sum(1 for g, _ in diffs if g == "machines")
    n_game_recipes = sum(len(g["Classes"]) for g in docs if _nc_tail(g["NativeClass"]) == "FGRecipe")
    head = [
        f"dev_utils diff vs repo  ({docs_path(game_dir)})",
        f"  recipes:  {counts['recipes']} in manifest, {n_diff_recipes} differ",
        f"  items:    {counts['items']} in manifest, {n_diff_items} differ",
        f"  machines: {counts['machines']} in manifest, {n_diff_machines} differ",
    ]
    body = "\n".join(lines) if lines else "  (no differences — docs match the repo)"
    tail = (
        "  extra game recipes not tracked: %d in the game export vs %d in our "
        "manifest (power/extractor/well recipes are world data and stay "
        "hand-maintained; further alternates not yet added)."
        % (n_game_recipes, counts["recipes"])
    )
    return "\n".join(head) + "\n" + body + "\n" + tail


# --------------------------------------------------------------------------
# CLI (docopt)
# --------------------------------------------------------------------------

USAGE = """\
Satisfactory doc-lifting developer utilities (dev-only; the main optimiser CLI
is `factory-optimiser`). Lift one machine / recipe / item from the game's
AutoJSON docs into the repo's JSON format, ready to paste into recipes/,
items/ or machines/. Names are matched against the public in-game display
names. Read-only: it never writes to the game install or to the repo; the
recipe set itself is defined by the repo, not by this tool. Warnings go to
stderr; stdout stays valid JSON.

Usage:
  dev_utils item <name> [<id>] [options]
  dev_utils machine <name> [<id>] [options]
  dev_utils recipe <name> [<id>] [options]
  dev_utils recipes-for <item> [options]
  dev_utils recipes-by <machine> [options]
  dev_utils diff [options]
  dev_utils --version
  dev_utils --help

Commands:
  item <name>    Lift an item descriptor from the docs (repo JSON).
  machine <name> Lift a machine buildable from the docs (repo JSON). Errors
                 unless its max_sloops is recorded in MACHINE_MANIFEST — the
                 game docs do not export sloop capacity.
  recipe <name>  Lift a recipe from the docs (per-min rates, repo JSON).
  recipes-for <item>
                 List the recipes whose product includes the item.
  recipes-by <machine>
                 List the recipes whose machine produces them.
  diff           Diff every manifest entry against the repo JSON files.

Arguments:
  <name>   What to lift, by public display name — e.g. "Pure Copper Ingot",
           "Screws", "Coal-Powered Generator". Case-insensitive; "Alternate: "
           prefix optional; a partial match works if unambiguous. A game
           ClassName (Recipe_/Desc_/Build_ *_C) is also accepted.
  <id>     Our internal id; defaults to the manifest id, else a slug of the
           display name.
  <item>   Item name to look up; same matching rules as <name>.
  <machine>
           Machine name to look up; same matching rules as <name>.

Options:
  --game-dir DIR   Path to a Satisfactory install (CommunityResources/Docs is
                   read from it)                       [default: satisfactory-game-files]
  -h, --help       Show this message.
  --version        Show version.
"""


def _with_docs(handler):
    """Load the docs once, then hand them to the command handler."""

    def wrapped(args):
        try:
            docs = load_docs(args["--game-dir"])
        except FileNotFoundError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
        return handler(args, docs)

    return wrapped


@_with_docs
def _cmd_item(args, docs) -> int:
    try:
        data, notes = lift_item(docs, args["<name>"], args["<id>"])
    except KeyError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return _emit(data, notes)


@_with_docs
def _cmd_machine(args, docs) -> int:
    try:
        data, notes = lift_machine(docs, args["<name>"], args["<id>"])
    except KeyError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return _emit(data, notes)


@_with_docs
def _cmd_recipe(args, docs) -> int:
    try:
        data, notes = lift_recipe(docs, args["<name>"], args["<id>"])
    except KeyError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return _emit(data, notes)


@_with_docs
def _cmd_recipes_for(args, docs) -> int:
    try:
        item_class, item_name = _resolve_query(_item_candidates(docs), args["<item>"], "item")
    except KeyError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    recipes = _recipes_for_item(docs, item_class)
    if not recipes:
        print(f"(no recipes in the docs produce {item_name!r})")
        return 0
    for name in recipes:
        print(name)
    return 0


@_with_docs
def _cmd_recipes_by(args, docs) -> int:
    try:
        machine_class, machine_name = _resolve_query(_machine_candidates(docs), args["<machine>"], "machine")
    except KeyError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    recipes = _recipes_by_machine(docs, machine_class)
    if not recipes:
        print(f"(no recipes in the docs use {machine_name!r})")
        return 0
    for name in recipes:
        print(name)
    return 0


def _cmd_diff(args) -> int:
    try:
        report = build_report(args["--game-dir"], ".")
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(report)
    return 1 if "DIFF" in report else 0


def main(argv: list[str] | None = None) -> int:
    try:
        args = docopt(USAGE, argv=argv, version=f"factory-optimiser-dev-utils {__version__}")
    except DocoptExit as exc:
        print(exc, file=sys.stderr)
        return 2
    if args["item"]:
        return _cmd_item(args)
    if args["machine"]:
        return _cmd_machine(args)
    if args["recipe"]:
        return _cmd_recipe(args)
    if args["recipes-for"]:
        return _cmd_recipes_for(args)
    if args["recipes-by"]:
        return _cmd_recipes_by(args)
    if args["diff"]:
        return _cmd_diff(args)
    return 2  # unreachable: docopt requires one of the usage forms


if __name__ == "__main__":
    raise SystemExit(main())
