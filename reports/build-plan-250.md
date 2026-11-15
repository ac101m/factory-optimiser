# Satisfactory Factory Optimiser — Build Plan

**Official optimum** — **461,996,861 pts/min** (overclock tiers 100%, 125%, 150%, 175%, 200%, 225%, 250%; Auto-solved (augmenter sweep)). All rates are per minute.

**Configuration**: `fixed_max_clock` is ON — every overclockable machine is pinned to **250%**. The clock choice is removed from the model; whole-machine counts are then rounded up and trimmed back to ≤250%, so rows below 250% are exact-balance remnants of that rounding, not choices. Non-overclockable machines stay at base clock.

## High-level overview

| Metric | Value | Notes |
|---|---|---|
| **Sink points** | **461,996,861 pts/min** | 0 augmenter(s), 1.00x power |
| **Power load** | **1,342,803 MW** | what consumers actually draw |
| **Power supplied** | 1,356,231 MW | load x1.01 (1% reserve) |
| **Machines** | **12,043** | 138 recipe rows across 19 machine types |
| **Somersloops** | 104 / 104 | see overclock notes |
| **Sink throughput** | 381.1 items/min | one Awesome Sink covers it (1200/min cap, 30 MW) |

### Sink flows

| Sink item | pts/item | /min | pts/min | share |
|---|---:|---:|---:|---:|
| Ballistic Warp Drive | 2,895,334 | 110.2 | 319,176,105 | 69.1% |
| AI Expansion Server | 597,652 | 120.0 | 71,718,240 | 15.5% |
| Assembly Director System | 500,176 | 138.3 | 69,172,397 | 15.0% |
| Plutonium Fuel Rod | 153,184 | 12.6 | 1,930,118 | 0.4% |
| **TOTAL** | | | **461,996,861** | 100% |

### Map resources extracted

Miners are shown at their planned 250% clock; every tapped node group is maxed.

| Resource | extractors | /min |
|---|---:|---:|
| Water | 767 | 229,933 |
| Iron Ore | 127 | 92,100 |
| Limestone | 94 | 67,050 |
| Coal | 62 | 42,300 |
| Copper Ore | 55 | 36,900 |
| Caterium Ore | 17 | 15,000 |
| Raw Quartz | 17 | 13,500 |
| Crude Oil | 33 | 12,600 |
| Bauxite | 17 | 12,300 |
| Nitrogen Gas | 6 | 12,000 |
| Sulfur | 16 | 10,800 |
| SAM | 19 | 10,200 |
| Uranium | 5 | 2,100 |

---

# Production per item

Aggregate material balance across the whole plan (production includes extraction).

| Item | produced/min | consumed/min | net | destination |
|---|---:|---:|---:|---|
| Water | 243,914.8 | 243,914.8 | -0.0 | balanced |
| Iron Ingot | 156,574.5 | 156,574.6 | -0.0 | balanced |
| Wire | 95,469.4 | 95,469.4 | -0.0 | balanced |
| Iron Ore | 92,100.0 | 92,100.0 | +0.0 | balanced |
| Copper Ingot | 83,184.5 | 83,184.5 | +0.0 | balanced |
| Limestone | 67,050.0 | 67,050.0 | +0.0 | balanced |
| Coal | 52,094.4 | 52,094.4 | +0.0 | balanced |
| Quickwire | 49,704.0 | 49,704.0 | +0.0 | balanced |
| Aluminum Scrap | 37,787.8 | 37,787.8 | +0.0 | balanced |
| Copper Ore | 36,900.0 | 36,900.0 | +0.0 | balanced |
| Cable | 27,659.2 | 27,659.2 | +0.0 | balanced |
| Fuel | 25,658.5 | 25,658.5 | -0.0 | balanced |
| Copper Sheet | 24,367.7 | 24,367.7 | +0.0 | balanced |
| Steel Pipe | 23,130.4 | 23,130.4 | +0.0 | balanced |
| Alumina Solution | 22,672.7 | 22,672.7 | +0.0 | balanced |
| Rubber | 19,548.5 | 19,548.5 | +0.0 | balanced |
| Aluminum Ingot | 18,893.9 | 18,893.9 | +0.0 | balanced |
| Bauxite | 18,893.9 | 18,893.9 | -0.0 | balanced |
| Screws | 18,390.9 | 18,390.9 | -0.0 | balanced |
| Concrete | 17,251.9 | 17,251.9 | +0.0 | balanced |
| Heavy Oil Residue | 16,800.0 | 16,800.0 | +0.0 | balanced |
| Silica | 16,504.4 | 16,504.4 | +0.0 | balanced |
| Caterium Ore | 15,000.0 | 15,000.0 | -0.0 | balanced |
| Sulfur | 13,916.3 | 13,916.3 | +0.0 | balanced |
| Plastic | 13,650.2 | 13,650.2 | +0.0 | balanced |
| Raw Quartz | 13,500.0 | 13,500.0 | +0.0 | balanced |
| Nitrogen Gas | 13,495.4 | 13,495.4 | +0.0 | balanced |
| Crude Oil | 12,600.0 | 12,600.0 | +0.0 | balanced |
| Rocket Fuel | 11,985.5 | 11,985.5 | +0.0 | balanced |
| SAM | 10,200.0 | 10,200.0 | +0.0 | balanced |
| Dark Matter Residue | 9,761.9 | 9,761.9 | -0.0 | balanced |
| Excited Photonic Matter | 8,761.9 | 8,761.9 | +0.0 | balanced |
| Petroleum Coke | 8,428.5 | 8,428.5 | +0.0 | balanced |
| Polymer Resin | 8,400.0 | 8,400.0 | +0.0 | balanced |
| Alclad Aluminum Sheet | 7,821.6 | 7,821.6 | +0.0 | balanced |
| Iron Plate | 6,561.6 | 6,561.6 | +0.0 | balanced |
| Circuit Board | 6,356.6 | 6,356.6 | +0.0 | balanced |
| Copper Powder | 5,523.8 | 5,523.8 | +0.0 | balanced |
| Quartz Crystal | 4,998.5 | 4,998.5 | +0.0 | balanced |
| Diamonds | 4,704.8 | 4,704.8 | -0.0 | balanced |
| Caterium Ingot | 4,142.0 | 4,142.0 | +0.0 | balanced |
| Turbofuel | 4,104.4 | 4,104.4 | -0.0 | balanced |
| Dark Matter Crystal | 3,904.8 | 3,904.8 | +0.0 | balanced |
| Aluminum Casing | 3,535.2 | 3,535.2 | -0.0 | balanced |
| Empty Canister | 3,136.5 | 3,136.5 | +0.0 | balanced |
| Packaged Turbofuel | 3,136.5 | 3,136.5 | +0.0 | balanced |
| Stator | 2,699.9 | 2,699.9 | +0.0 | balanced |
| Reanimated SAM | 2,550.0 | 2,550.0 | +0.0 | balanced |
| Uranium Waste | 2,520.0 | 2,520.0 | +0.0 | balanced |
| Non-Fissile Uranium | 2,520.0 | 2,520.0 | +0.0 | balanced |
| Steel Ingot | 2,384.0 | 2,384.0 | -0.0 | balanced |
| Time Crystal | 2,352.4 | 2,352.4 | +0.0 | balanced |
| Battery | 2,183.0 | 2,183.0 | +0.0 | balanced |
| Uranium | 2,100.0 | 2,100.0 | +0.0 | balanced |
| Compacted Coal | 1,890.0 | 1,890.0 | +0.0 | balanced |
| Encased Uranium Cell | 1,680.0 | 1,680.0 | +0.0 | balanced |
| Nitric Acid | 1,580.2 | 1,580.2 | -0.0 | balanced |
| Steel Beam | 1,509.8 | 1,509.8 | +0.0 | balanced |
| Computer | 1,429.0 | 1,429.0 | +0.0 | balanced |
| Automated Wiring | 1,383.0 | 1,383.0 | +0.0 | balanced |
| AI Limiter | 1,377.8 | 1,377.8 | +0.0 | balanced |
| Ficsite Trigon | 1,200.0 | 1,200.0 | +0.0 | balanced |
| Encased Industrial Beam | 1,198.2 | 1,198.2 | +0.0 | balanced |
| Rotor | 1,061.0 | 1,061.0 | +0.0 | balanced |
| Modular Frame | 1,058.5 | 1,058.5 | +0.0 | balanced |
| Reinforced Iron Plate | 981.9 | 981.9 | -0.0 | balanced |
| Electromagnetic Control Rod | 877.9 | 877.9 | +0.0 | balanced |
| Plutonium Pellet | 756.0 | 756.0 | +0.0 | balanced |
| Sulfuric Acid | 756.0 | 756.0 | +0.0 | balanced |
| Crystal Oscillator | 499.9 | 499.9 | -0.0 | balanced |
| Motor | 487.9 | 487.9 | +0.0 | balanced |
| Heat Sink | 457.4 | 457.4 | +0.0 | balanced |
| Ficsite Ingot | 400.0 | 400.0 | +0.0 | balanced |
| Encased Plutonium Cell | 378.0 | 378.0 | +0.0 | balanced |
| Heavy Modular Frame | 359.4 | 359.4 | +0.0 | balanced |
| Adaptive Control Unit | 276.6 | 276.6 | +0.0 | balanced |
| Singularity Cell | 276.2 | 276.2 | +0.0 | balanced |
| Smart Plating | 276.2 | 276.2 | +0.0 | balanced |
| Radio Control Unit | 221.0 | 221.0 | +0.0 | balanced |
| Supercomputer | 218.3 | 218.3 | +0.0 | balanced |
| Versatile Framework | 200.0 | 200.0 | +0.0 | balanced |
| Superposition Oscillator | 190.5 | 190.5 | +0.0 | balanced |
| Cooling System | 165.7 | 165.7 | +0.0 | balanced |
| Assembly Director System | 138.3 | 0.0 | +138.3 | → Awesome Sink (138.3/min) |
| Modular Engine | 138.1 | 138.1 | +0.0 | balanced |
| AI Expansion Server | 120.0 | 0.0 | +120.0 | → Awesome Sink (120.0/min) |
| Ballistic Warp Drive | 110.2 | 0.0 | +110.2 | → Awesome Sink (110.2/min) |
| Fused Modular Frame | 82.9 | 82.9 | +0.0 | balanced |
| Neural-Quantum Processor | 80.0 | 80.0 | +0.0 | balanced |
| Magnetic Field Generator | 80.0 | 80.0 | -0.0 | balanced |
| Thermal Propulsion Rocket | 55.2 | 55.2 | +0.0 | balanced |
| Turbo Motor | 55.2 | 55.2 | +0.0 | balanced |
| Uranium Fuel Rod | 50.4 | 50.4 | +0.0 | balanced |
| Nuclear Pasta | 27.6 | 27.6 | +0.0 | balanced |
| Pressure Conversion Cube | 27.6 | 27.6 | +0.0 | balanced |
| Plutonium Fuel Rod | 12.6 | 0.0 | +12.6 | → Awesome Sink (12.6/min) |

---

# All used recipes

138 recipe rows from 137 distinct recipes (rows repeat a recipe when sloop grades or clocks differ). Flat index of the per-machine tables in this document — the columns reproduce the plan's whole-machine clocks, where a row below 100% is an exact-balance remnant.

| Recipe | machine | # | clock | slps |
|---|---|---:|---:|---:|
| Alternate: Dark Matter Trap | accelerator | 27 | 241.0% | — |
| Alternate: Turbo Diamonds | accelerator | 32 | 245.0% | — |
| Nuclear Pasta | accelerator | 23 | 240.2% | — |
| Plutonium Pellet | accelerator | 11 | 229.1% | — |
| AI Limiter | assembler | 111 | 248.2% | — |
| Alclad Aluminum Sheet | assembler | 105 | 248.3% | — |
| Alternate: Alclad Casing | assembler | 13 | 241.7% | — |
| Alternate: Cheap Silica | assembler | 126 | 249.5% | — |
| Alternate: Coated Iron Plate | assembler | 3 | 185.4% | — |
| Alternate: Copper Rotor | assembler | 38 | 248.2% | — |
| Alternate: Crystal Computer | assembler | 36 | 247.5% | — |
| Alternate: Electric Motor | assembler | 27 | 241.0% | — |
| Alternate: Encased Industrial Pipe | assembler | 120 | 249.6% | — |
| Alternate: Fused Quickwire | assembler | 221 | 249.9% | — |
| Alternate: Silicon Circuit Board | assembler | 204 | 249.3% | — |
| Alternate: Steeled Frame | assembler | 142 | 248.5% | — |
| Alternate: Stitched Iron Plate | assembler | 70 | 249.4% | — |
| Assembly Director System | assembler | 74 | 249.2% | — |
| Automated Wiring | assembler | 222 | 249.2% | — |
| Electromagnetic Control Rod | assembler | 88 | 249.4% | — |
| Encased Plutonium Cell | assembler | 31 | 243.9% | — |
| Heat Sink | assembler | 25 | 244.0% | — |
| Magnetic Field Generator | assembler | 32 | 250.0% | — |
| Pressure Conversion Cube | assembler | 12 | 230.2% | — |
| Smart Plating | assembler | 56 | 246.6% | — |
| Stator | assembler | 216 | 250.0% | — |
| Versatile Framework | assembler | 9 | 244.0% | — |
| Alternate: Cooling Device | blender | 14 | 236.7% | — |
| Alternate: Diluted Fuel | blender | 103 | 249.1% | — |
| Alternate: Heat-Fused Frame | blender | 12 | 230.2% | — |
| Alternate: Nitro Rocket Fuel | blender | 28 | 247.0% | — |
| Alternate: Turbo Blend Fuel | blender | 16 | 241.9% | — |
| Nitric Acid | blender | 22 | 239.4% | — |
| Non-Fissile Uranium | blender | 21 | 240.0% | — |
| Rocket Fuel | blender | 7 | 230.5% | — |
| Alternate: Aluminum Beam | constructor | 11 | 248.8% | — |
| Alternate: Iron Pipe | constructor | 371 | 249.4% | — |
| Alternate: Iron Wire | constructor | 1,698 | 249.9% | — |
| Alternate: Steel Screws | constructor | 29 | 243.9% | — |
| Cable | constructor | 369 | 249.9% | — |
| Copper Powder | constructor | 45 | 245.5% | — |
| Empty Canister | constructor | 21 | 248.9% | — |
| Ficsite Trigon | constructor | 16 | 250.0% | — |
| Iron Plate | constructor | 123 | 249.8% | — |
| Reanimated SAM | constructor | 34 | 250.0% | — |
| Bauxite (Caterium) | converter | 14 | 248.6% | — |
| Bauxite (Copper) | converter | 9 | 223.8% | — |
| Coal (Limestone) | converter | 33 | 247.3% | — |
| Excited Photonic Matter | converter | 18 | 243.4% | — |
| Ficsite Ingot (Aluminum) | converter | 6 | 222.2% | — |
| Nitrogen Gas (Caterium) | converter | 5 | 249.2% | — |
| Sulfur (Iron) | converter | 11 | 236.1% | — |
| Time Crystal | converter | 157 | 249.7% | — |
| Alternate: Molded Beam | foundry | 8 | 248.3% | — |
| Alternate: Solid Steel Ingot | foundry | 16 | 248.3% | — |
| Rocket Fuel Power | fuel_generator | 1,151 | 249.9% | — |
| Geothermal Power (Impure) | geothermal_generator | 9 | 100.0% | — |
| Geothermal Power (Normal) | geothermal_generator | 13 | 100.0% | — |
| Geothermal Power (Pure) | geothermal_generator | 9 | 100.0% | — |
| Adaptive Control Unit | manufacturer | 111 | 249.2% | — |
| Alternate: Caterium Computer | manufacturer | 121 | 249.5% | — |
| Alternate: Classic Battery | manufacturer | 30 | 242.6% | — |
| Alternate: Flexible Framework | manufacturer | 5 | 240.6% | — |
| Alternate: Heavy Encased Frame | manufacturer | 52 | 245.8% | — |
| Alternate: Infused Uranium Cell | manufacturer | 34 | 247.1% | — |
| Alternate: Insulated Crystal Oscillator | manufacturer | 107 | 249.1% | — |
| Alternate: Super-State Computer | manufacturer | 37 | 245.8% | — |
| Alternate: Turbo Electric Motor | manufacturer | 8 | 245.5% | — |
| Alternate: Uranium Fuel Unit | manufacturer | 34 | 247.1% | — |
| Ballistic Warp Drive | manufacturer | 1 | 23.8% | — |
| Ballistic Warp Drive | manufacturer | 22 | 250.0% | 4 |
| Modular Engine | manufacturer | 56 | 246.6% | — |
| Plutonium Fuel Rod | manufacturer | 21 | 240.0% | — |
| Radio Control Unit | manufacturer | 36 | 245.5% | — |
| Singularity Cell | manufacturer | 12 | 230.2% | — |
| Thermal Propulsion Rocket | manufacturer | 23 | 240.2% | — |
| Limestone (Impure) Mk.2 | miner_mk2 | 15 | 250.0% | — |
| Bauxite (Impure) Mk.3 | miner_mk3 | 5 | 250.0% | — |
| Bauxite (Normal) Mk.3 | miner_mk3 | 6 | 250.0% | — |
| Bauxite (Pure) Mk.3 | miner_mk3 | 6 | 250.0% | — |
| Caterium Ore (Normal) Mk.3 | miner_mk3 | 9 | 250.0% | — |
| Caterium Ore (Pure) Mk.3 | miner_mk3 | 8 | 250.0% | — |
| Coal (Impure) Mk.3 | miner_mk3 | 15 | 250.0% | — |
| Coal (Normal) Mk.3 | miner_mk3 | 31 | 250.0% | — |
| Coal (Pure) Mk.3 | miner_mk3 | 16 | 250.0% | — |
| Copper Ore (Impure) Mk.3 | miner_mk3 | 13 | 250.0% | — |
| Copper Ore (Normal) Mk.3 | miner_mk3 | 29 | 250.0% | — |
| Copper Ore (Pure) Mk.3 | miner_mk3 | 13 | 250.0% | — |
| Iron Ore (Impure) Mk.3 | miner_mk3 | 39 | 250.0% | — |
| Iron Ore (Normal) Mk.3 | miner_mk3 | 42 | 250.0% | — |
| Iron Ore (Pure) Mk.3 | miner_mk3 | 46 | 250.0% | — |
| Limestone (Normal) Mk.3 | miner_mk3 | 50 | 250.0% | — |
| Limestone (Pure) Mk.3 | miner_mk3 | 29 | 250.0% | — |
| Quartz (Impure) Mk.3 | miner_mk3 | 3 | 250.0% | — |
| Quartz (Normal) Mk.3 | miner_mk3 | 7 | 250.0% | — |
| Quartz (Pure) Mk.3 | miner_mk3 | 7 | 250.0% | — |
| SAM (Impure) Mk.3 | miner_mk3 | 10 | 250.0% | — |
| SAM (Normal) Mk.3 | miner_mk3 | 6 | 250.0% | — |
| SAM (Pure) Mk.3 | miner_mk3 | 3 | 250.0% | — |
| Sulfur (Impure) Mk.3 | miner_mk3 | 6 | 250.0% | — |
| Sulfur (Normal) Mk.3 | miner_mk3 | 5 | 250.0% | — |
| Sulfur (Pure) Mk.3 | miner_mk3 | 5 | 250.0% | — |
| Uranium (Impure) Mk.3 | miner_mk3 | 3 | 250.0% | — |
| Uranium (Normal) Mk.3 | miner_mk3 | 2 | 250.0% | — |
| Nuclear Power (Uranium) | nuclear_power_plant | 101 | 249.5% | — |
| Crude Oil (Impure) | oil_extractor | 10 | 250.0% | — |
| Crude Oil (Normal) | oil_extractor | 12 | 250.0% | — |
| Crude Oil (Pure) | oil_extractor | 8 | 250.0% | — |
| Packaged Turbofuel | packager | 63 | 248.9% | — |
| AI Expansion Server | quantum_encoder | 8 | 250.0% | 2 |
| Neural-Quantum Processor | quantum_encoder | 11 | 242.4% | — |
| Superposition Oscillator | quantum_encoder | 16 | 238.1% | — |
| Alternate: Electrode Aluminum Scrap | refinery | 51 | 247.0% | — |
| Alternate: Heavy Oil Residue | refinery | 168 | 250.0% | — |
| Alternate: Pure Caterium Ingot | refinery | 139 | 248.3% | — |
| Alternate: Pure Copper Ingot | refinery | 888 | 249.8% | — |
| Alternate: Pure Iron Ingot | refinery | 964 | 249.9% | — |
| Alternate: Pure Quartz Crystal | refinery | 39 | 244.1% | — |
| Alternate: Recycled Plastic | refinery | 92 | 247.3% | — |
| Alternate: Recycled Rubber | refinery | 103 | 248.4% | — |
| Alternate: Sloppy Alumina | refinery | 38 | 248.6% | — |
| Alternate: Steamed Copper Sheet | refinery | 434 | 249.5% | — |
| Alternate: Wet Concrete | refinery | 87 | 247.9% | — |
| Petroleum Coke | refinery | 29 | 242.2% | — |
| Residual Rubber | refinery | 84 | 250.0% | — |
| Sulfuric Acid | refinery | 7 | 216.0% | — |
| Turbofuel | refinery | 51 | 247.1% | — |
| Central Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — |
| Crater Lakes Oil Well | resource_well_pressurizer | 1 | 250.0% | — |
| Northern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — |
| Northwestern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — |
| Southeastern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — |
| Southern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — |
| Southwestern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — |
| Spire Coast Oil Well | resource_well_pressurizer | 1 | 250.0% | — |
| Swamp Oil Well | resource_well_pressurizer | 1 | 250.0% | — |
| Alternate: Pure Aluminum Ingot | smelter | 252 | 249.9% | — |
| Water Extraction | water_extractor | 767 | 249.8% | — |

---

# Per item breakdown

For every item this plan produces, the recipes that make it — with the plan's whole-machine count, clock, sloop grade, and the share of the item's total that each recipe supplies.

## Water — 243,914.8/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Water Extraction | water_extractor | 767 | 249.8% | — | 229,933.1 | 94.3% |
| Alternate: Electrode Aluminum Scrap | refinery | 51 | 247.0% | — | 13,225.7 | 5.4% |
| Non-Fissile Uranium | blender | 21 | 240.0% | — | 756.0 | 0.3% |

## Iron Ingot — 156,574.5/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Iron Ingot | refinery | 964 | 249.9% | — | 156,574.5 | 100.0% |

## Wire — 95,469.4/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Iron Wire | constructor | 1,698 | 249.9% | — | 95,469.4 | 100.0% |

## Iron Ore — 92,100.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Iron Ore (Pure) Mk.3 | miner_mk3 | 46 | 250.0% | — | 55,200.0 | 59.9% |
| Iron Ore (Normal) Mk.3 | miner_mk3 | 42 | 250.0% | — | 25,200.0 | 27.4% |
| Iron Ore (Impure) Mk.3 | miner_mk3 | 39 | 250.0% | — | 11,700.0 | 12.7% |

## Copper Ingot — 83,184.5/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Copper Ingot | refinery | 888 | 249.8% | — | 83,184.5 | 100.0% |

## Limestone — 67,050.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Limestone (Pure) Mk.3 | miner_mk3 | 29 | 250.0% | — | 34,800.0 | 51.9% |
| Limestone (Normal) Mk.3 | miner_mk3 | 50 | 250.0% | — | 30,000.0 | 44.7% |
| Limestone (Impure) Mk.2 | miner_mk2 | 15 | 250.0% | — | 2,250.0 | 3.4% |

## Coal — 52,094.4/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Coal (Pure) Mk.3 | miner_mk3 | 16 | 250.0% | — | 19,200.0 | 36.9% |
| Coal (Normal) Mk.3 | miner_mk3 | 31 | 250.0% | — | 18,600.0 | 35.7% |
| Coal (Limestone) | converter | 33 | 247.3% | — | 9,794.4 | 18.8% |
| Coal (Impure) Mk.3 | miner_mk3 | 15 | 250.0% | — | 4,500.0 | 8.6% |

## Quickwire — 49,704.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Fused Quickwire | assembler | 221 | 249.9% | — | 49,704.0 | 100.0% |

## Aluminum Scrap — 37,787.8/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Electrode Aluminum Scrap | refinery | 51 | 247.0% | — | 37,787.8 | 100.0% |

## Copper Ore — 36,900.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Copper Ore (Normal) Mk.3 | miner_mk3 | 29 | 250.0% | — | 17,400.0 | 47.2% |
| Copper Ore (Pure) Mk.3 | miner_mk3 | 13 | 250.0% | — | 15,600.0 | 42.3% |
| Copper Ore (Impure) Mk.3 | miner_mk3 | 13 | 250.0% | — | 3,900.0 | 10.6% |

## Cable — 27,659.2/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Cable | constructor | 369 | 249.9% | — | 27,659.2 | 100.0% |

## Fuel — 25,658.5/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Diluted Fuel | blender | 103 | 249.1% | — | 25,658.5 | 100.0% |

## Copper Sheet — 24,367.7/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Steamed Copper Sheet | refinery | 434 | 249.5% | — | 24,367.7 | 100.0% |

## Steel Pipe — 23,130.4/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Iron Pipe | constructor | 371 | 249.4% | — | 23,130.4 | 100.0% |

## Alumina Solution — 22,672.7/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Sloppy Alumina | refinery | 38 | 248.6% | — | 22,672.7 | 100.0% |

## Rubber — 19,548.5/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Recycled Rubber | refinery | 103 | 248.4% | — | 15,348.5 | 78.5% |
| Residual Rubber | refinery | 84 | 250.0% | — | 4,200.0 | 21.5% |

## Aluminum Ingot — 18,893.9/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Aluminum Ingot | smelter | 252 | 249.9% | — | 18,893.9 | 100.0% |

## Bauxite — 18,893.9/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Bauxite (Pure) Mk.3 | miner_mk3 | 6 | 250.0% | — | 7,200.0 | 38.1% |
| Bauxite (Caterium) | converter | 14 | 248.6% | — | 4,176.5 | 22.1% |
| Bauxite (Normal) Mk.3 | miner_mk3 | 6 | 250.0% | — | 3,600.0 | 19.1% |
| Bauxite (Copper) | converter | 9 | 223.8% | — | 2,417.5 | 12.8% |
| Bauxite (Impure) Mk.3 | miner_mk3 | 5 | 250.0% | — | 1,500.0 | 7.9% |

## Screws — 18,390.9/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Steel Screws | constructor | 29 | 243.9% | — | 18,390.9 | 100.0% |

## Concrete — 17,251.9/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Wet Concrete | refinery | 87 | 247.9% | — | 17,251.9 | 100.0% |

## Heavy Oil Residue — 16,800.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heavy Oil Residue | refinery | 168 | 250.0% | — | 16,800.0 | 100.0% |

## Silica — 16,504.4/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Cheap Silica | assembler | 126 | 249.5% | — | 16,504.4 | 100.0% |

## Caterium Ore — 15,000.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Caterium Ore (Pure) Mk.3 | miner_mk3 | 8 | 250.0% | — | 9,600.0 | 64.0% |
| Caterium Ore (Normal) Mk.3 | miner_mk3 | 9 | 250.0% | — | 5,400.0 | 36.0% |

## Sulfur — 13,916.3/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Sulfur (Pure) Mk.3 | miner_mk3 | 5 | 250.0% | — | 6,000.0 | 43.1% |
| Sulfur (Iron) | converter | 11 | 236.1% | — | 3,116.3 | 22.4% |
| Sulfur (Normal) Mk.3 | miner_mk3 | 5 | 250.0% | — | 3,000.0 | 21.6% |
| Sulfur (Impure) Mk.3 | miner_mk3 | 6 | 250.0% | — | 1,800.0 | 12.9% |

## Plastic — 13,650.2/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Recycled Plastic | refinery | 92 | 247.3% | — | 13,650.2 | 100.0% |

## Raw Quartz — 13,500.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Quartz (Pure) Mk.3 | miner_mk3 | 7 | 250.0% | — | 8,400.0 | 62.2% |
| Quartz (Normal) Mk.3 | miner_mk3 | 7 | 250.0% | — | 4,200.0 | 31.1% |
| Quartz (Impure) Mk.3 | miner_mk3 | 3 | 250.0% | — | 900.0 | 6.7% |

## Nitrogen Gas — 13,495.4/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Central Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 3,000.0 | 22.2% |
| Southwestern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 2,100.0 | 15.6% |
| Northwestern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 1,950.0 | 14.4% |
| Northern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 1,800.0 | 13.3% |
| Southeastern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 1,650.0 | 12.2% |
| Southern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 1,500.0 | 11.1% |
| Nitrogen Gas (Caterium) | converter | 5 | 249.2% | — | 1,495.4 | 11.1% |

## Crude Oil — 12,600.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Crude Oil (Pure) | oil_extractor | 8 | 250.0% | — | 4,800.0 | 38.1% |
| Crude Oil (Normal) | oil_extractor | 12 | 250.0% | — | 3,600.0 | 28.6% |
| Crude Oil (Impure) | oil_extractor | 10 | 250.0% | — | 1,500.0 | 11.9% |
| Crater Lakes Oil Well | resource_well_pressurizer | 1 | 250.0% | — | 1,350.0 | 10.7% |
| Spire Coast Oil Well | resource_well_pressurizer | 1 | 250.0% | — | 900.0 | 7.1% |
| Swamp Oil Well | resource_well_pressurizer | 1 | 250.0% | — | 450.0 | 3.6% |

## Rocket Fuel — 11,985.5/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Nitro Rocket Fuel | blender | 28 | 247.0% | — | 10,372.3 | 86.5% |
| Rocket Fuel | blender | 7 | 230.5% | — | 1,613.2 | 13.5% |

## SAM — 10,200.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| SAM (Normal) Mk.3 | miner_mk3 | 6 | 250.0% | — | 3,600.0 | 35.3% |
| SAM (Pure) Mk.3 | miner_mk3 | 3 | 250.0% | — | 3,600.0 | 35.3% |
| SAM (Impure) Mk.3 | miner_mk3 | 10 | 250.0% | — | 3,000.0 | 29.4% |

## Dark Matter Residue — 9,761.9/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Superposition Oscillator | quantum_encoder | 16 | 238.1% | — | 4,761.9 | 48.8% |
| AI Expansion Server | quantum_encoder | 8 | 250.0% | 2 | 3,000.0 | 30.7% |
| Neural-Quantum Processor | quantum_encoder | 11 | 242.4% | — | 2,000.0 | 20.5% |

## Excited Photonic Matter — 8,761.9/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Excited Photonic Matter | converter | 18 | 243.4% | — | 8,761.9 | 100.0% |

## Petroleum Coke — 8,428.5/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Petroleum Coke | refinery | 29 | 242.2% | — | 8,428.5 | 100.0% |

## Polymer Resin — 8,400.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heavy Oil Residue | refinery | 168 | 250.0% | — | 8,400.0 | 100.0% |

## Alclad Aluminum Sheet — 7,821.6/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alclad Aluminum Sheet | assembler | 105 | 248.3% | — | 7,821.6 | 100.0% |

## Iron Plate — 6,561.6/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Iron Plate | constructor | 123 | 249.8% | — | 6,144.4 | 93.6% |
| Alternate: Coated Iron Plate | assembler | 3 | 185.4% | — | 417.2 | 6.4% |

## Circuit Board — 6,356.6/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Silicon Circuit Board | assembler | 204 | 249.3% | — | 6,356.6 | 100.0% |

## Copper Powder — 5,523.8/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Copper Powder | constructor | 45 | 245.5% | — | 5,523.8 | 100.0% |

## Quartz Crystal — 4,998.5/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Quartz Crystal | refinery | 39 | 244.1% | — | 4,998.5 | 100.0% |

## Diamonds — 4,704.8/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Turbo Diamonds | accelerator | 32 | 245.0% | — | 4,704.8 | 100.0% |

## Caterium Ingot — 4,142.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Caterium Ingot | refinery | 139 | 248.3% | — | 4,142.0 | 100.0% |

## Turbofuel — 4,104.4/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Turbofuel | refinery | 51 | 247.1% | — | 2,362.5 | 57.6% |
| Alternate: Turbo Blend Fuel | blender | 16 | 241.9% | — | 1,741.9 | 42.4% |

## Dark Matter Crystal — 3,904.8/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Dark Matter Trap | accelerator | 27 | 241.0% | — | 3,904.8 | 100.0% |

## Aluminum Casing — 3,535.2/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Alclad Casing | assembler | 13 | 241.7% | — | 3,535.2 | 100.0% |

## Empty Canister — 3,136.5/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Empty Canister | constructor | 21 | 248.9% | — | 3,136.5 | 100.0% |

## Packaged Turbofuel — 3,136.5/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Packaged Turbofuel | packager | 63 | 248.9% | — | 3,136.5 | 100.0% |

## Stator — 2,699.9/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Stator | assembler | 216 | 250.0% | — | 2,699.9 | 100.0% |

## Reanimated SAM — 2,550.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Reanimated SAM | constructor | 34 | 250.0% | — | 2,550.0 | 100.0% |

## Uranium Waste — 2,520.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Nuclear Power (Uranium) | nuclear_power_plant | 101 | 249.5% | — | 2,520.0 | 100.0% |

## Non-Fissile Uranium — 2,520.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Non-Fissile Uranium | blender | 21 | 240.0% | — | 2,520.0 | 100.0% |

## Steel Ingot — 2,384.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Solid Steel Ingot | foundry | 16 | 248.3% | — | 2,384.0 | 100.0% |

## Time Crystal — 2,352.4/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Time Crystal | converter | 157 | 249.7% | — | 2,352.4 | 100.0% |

## Battery — 2,183.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Classic Battery | manufacturer | 30 | 242.6% | — | 2,183.0 | 100.0% |

## Uranium — 2,100.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Uranium (Normal) Mk.3 | miner_mk3 | 2 | 250.0% | — | 1,200.0 | 57.1% |
| Uranium (Impure) Mk.3 | miner_mk3 | 3 | 250.0% | — | 900.0 | 42.9% |

## Compacted Coal — 1,890.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Nitro Rocket Fuel | blender | 28 | 247.0% | — | 1,728.7 | 91.5% |
| Rocket Fuel | blender | 7 | 230.5% | — | 161.3 | 8.5% |

## Encased Uranium Cell — 1,680.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Infused Uranium Cell | manufacturer | 34 | 247.1% | — | 1,680.0 | 100.0% |

## Nitric Acid — 1,580.2/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Nitric Acid | blender | 22 | 239.4% | — | 1,580.2 | 100.0% |

## Steel Beam — 1,509.8/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Molded Beam | foundry | 8 | 248.3% | — | 894.0 | 59.2% |
| Alternate: Aluminum Beam | constructor | 11 | 248.8% | — | 615.8 | 40.8% |

## Computer — 1,429.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Caterium Computer | manufacturer | 121 | 249.5% | — | 1,132.0 | 79.2% |
| Alternate: Crystal Computer | assembler | 36 | 247.5% | — | 297.0 | 20.8% |

## Automated Wiring — 1,383.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Automated Wiring | assembler | 222 | 249.2% | — | 1,383.0 | 100.0% |

## AI Limiter — 1,377.8/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| AI Limiter | assembler | 111 | 248.2% | — | 1,377.8 | 100.0% |

## Ficsite Trigon — 1,200.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Ficsite Trigon | constructor | 16 | 250.0% | — | 1,200.0 | 100.0% |

## Encased Industrial Beam — 1,198.2/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Encased Industrial Pipe | assembler | 120 | 249.6% | — | 1,198.2 | 100.0% |

## Rotor — 1,061.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Copper Rotor | assembler | 38 | 248.2% | — | 1,061.0 | 100.0% |

## Modular Frame — 1,058.5/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Steeled Frame | assembler | 142 | 248.5% | — | 1,058.5 | 100.0% |

## Reinforced Iron Plate — 981.9/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Stitched Iron Plate | assembler | 70 | 249.4% | — | 981.9 | 100.0% |

## Electromagnetic Control Rod — 877.9/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Electromagnetic Control Rod | assembler | 88 | 249.4% | — | 877.9 | 100.0% |

## Plutonium Pellet — 756.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Plutonium Pellet | accelerator | 11 | 229.1% | — | 756.0 | 100.0% |

## Sulfuric Acid — 756.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Sulfuric Acid | refinery | 7 | 216.0% | — | 756.0 | 100.0% |

## Crystal Oscillator — 499.9/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Insulated Crystal Oscillator | manufacturer | 107 | 249.1% | — | 499.9 | 100.0% |

## Motor — 487.9/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Electric Motor | assembler | 27 | 241.0% | — | 487.9 | 100.0% |

## Heat Sink — 457.4/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Heat Sink | assembler | 25 | 244.0% | — | 457.4 | 100.0% |

## Ficsite Ingot — 400.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Ficsite Ingot (Aluminum) | converter | 6 | 222.2% | — | 400.0 | 100.0% |

## Encased Plutonium Cell — 378.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Encased Plutonium Cell | assembler | 31 | 243.9% | — | 378.0 | 100.0% |

## Heavy Modular Frame — 359.4/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heavy Encased Frame | manufacturer | 52 | 245.8% | — | 359.4 | 100.0% |

## Adaptive Control Unit — 276.6/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Adaptive Control Unit | manufacturer | 111 | 249.2% | — | 276.6 | 100.0% |

## Singularity Cell — 276.2/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Singularity Cell | manufacturer | 12 | 230.2% | — | 276.2 | 100.0% |

## Smart Plating — 276.2/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Smart Plating | assembler | 56 | 246.6% | — | 276.2 | 100.0% |

## Radio Control Unit — 221.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Radio Control Unit | manufacturer | 36 | 245.5% | — | 221.0 | 100.0% |

## Supercomputer — 218.3/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Super-State Computer | manufacturer | 37 | 245.8% | — | 218.3 | 100.0% |

## Versatile Framework — 200.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Versatile Framework | assembler | 9 | 244.0% | — | 109.8 | 54.9% |
| Alternate: Flexible Framework | manufacturer | 5 | 240.6% | — | 90.2 | 45.1% |

## Superposition Oscillator — 190.5/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Superposition Oscillator | quantum_encoder | 16 | 238.1% | — | 190.5 | 100.0% |

## Cooling System — 165.7/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Cooling Device | blender | 14 | 236.7% | — | 165.7 | 100.0% |

## Assembly Director System — 138.3/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Assembly Director System | assembler | 74 | 249.2% | — | 138.3 | 100.0% |

## Modular Engine — 138.1/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Modular Engine | manufacturer | 56 | 246.6% | — | 138.1 | 100.0% |

## AI Expansion Server — 120.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| AI Expansion Server | quantum_encoder | 8 | 250.0% | 2 | 120.0 | 100.0% |

## Ballistic Warp Drive — 110.2/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Ballistic Warp Drive | manufacturer | 22 | 250.0% | 4 | 110.0 | 99.8% |
| Ballistic Warp Drive | manufacturer | 1 | 23.8% | — | 0.2 | 0.2% |

## Fused Modular Frame — 82.9/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heat-Fused Frame | blender | 12 | 230.2% | — | 82.9 | 100.0% |

## Neural-Quantum Processor — 80.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Neural-Quantum Processor | quantum_encoder | 11 | 242.4% | — | 80.0 | 100.0% |

## Magnetic Field Generator — 80.0/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Magnetic Field Generator | assembler | 32 | 250.0% | — | 80.0 | 100.0% |

## Thermal Propulsion Rocket — 55.2/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Thermal Propulsion Rocket | manufacturer | 23 | 240.2% | — | 55.2 | 100.0% |

## Turbo Motor — 55.2/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Turbo Electric Motor | manufacturer | 8 | 245.5% | — | 55.2 | 100.0% |

## Uranium Fuel Rod — 50.4/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Uranium Fuel Unit | manufacturer | 34 | 247.1% | — | 50.4 | 100.0% |

## Nuclear Pasta — 27.6/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Nuclear Pasta | accelerator | 23 | 240.2% | — | 27.6 | 100.0% |

## Pressure Conversion Cube — 27.6/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Pressure Conversion Cube | assembler | 12 | 230.2% | — | 27.6 | 100.0% |

## Plutonium Fuel Rod — 12.6/min

| Recipe | machine | # | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Plutonium Fuel Rod | manufacturer | 21 | 240.0% | — | 12.6 | 100.0% |

---

# Per-machine breakdown

One section per machine type in the plan: the recipes it runs, the whole-machine count, clock and sloop grade, and aggregate inputs/outputs per minute.

## Refinery — 3,174 machines · 318,463 MW

| Recipe | # | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Pure Iron Ingot | 964 | 249.9% | — | Iron Ore 84,309.4 + Water 48,176.8 | Iron Ingot 156,574.5 |
| Alternate: Pure Copper Ingot | 888 | 249.8% | — | Copper Ore 33,273.8 + Water 22,182.5 | Copper Ingot 83,184.5 |
| Alternate: Steamed Copper Sheet | 434 | 249.5% | — | Copper Ingot 24,367.7 + Water 24,367.7 | Copper Sheet 24,367.7 |
| Alternate: Heavy Oil Residue | 168 | 250.0% | — | Crude Oil 12,600.0 | Heavy Oil Residue 16,800.0 + Polymer Resin 8,400.0 |
| Alternate: Pure Caterium Ingot | 139 | 248.3% | — | Caterium Ore 8,284.0 + Water 8,284.0 | Caterium Ingot 4,142.0 |
| Alternate: Recycled Rubber | 103 | 248.4% | — | Fuel 7,674.3 + Plastic 7,674.3 | Rubber 15,348.5 |
| Alternate: Recycled Plastic | 92 | 247.3% | — | Fuel 6,825.1 + Rubber 6,825.1 | Plastic 13,650.2 |
| Alternate: Wet Concrete | 87 | 247.9% | — | Limestone 25,877.9 + Water 21,564.9 | Concrete 17,251.9 |
| Residual Rubber | 84 | 250.0% | — | Polymer Resin 8,400.0 + Water 8,400.0 | Rubber 4,200.0 |
| Alternate: Electrode Aluminum Scrap | 51 | 247.0% | — | Alumina Solution 22,672.7 + Petroleum Coke 7,557.6 | Aluminum Scrap 37,787.8 + Water 13,225.7 |
| Turbofuel | 51 | 247.1% | — | Compacted Coal 1,890.0 + Fuel 2,835.1 | Turbofuel 2,362.5 |
| Alternate: Pure Quartz Crystal | 39 | 244.1% | — | Raw Quartz 6,426.7 + Water 3,570.4 | Quartz Crystal 4,998.5 |
| Alternate: Sloppy Alumina | 38 | 248.6% | — | Bauxite 18,893.9 + Water 18,893.9 | Alumina Solution 22,672.7 |
| Petroleum Coke | 29 | 242.2% | — | Heavy Oil Residue 2,809.5 | Petroleum Coke 8,428.5 |
| Sulfuric Acid | 7 | 216.0% | — | Sulfur 756.0 + Water 756.0 | Sulfuric Acid 756.0 |

## Constructor — 2,717 machines · 36,427 MW

| Recipe | # | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Iron Wire | 1,698 | 249.9% | — | Iron Ingot 53,038.6 | Wire 95,469.4 |
| Alternate: Iron Pipe | 371 | 249.4% | — | Iron Ingot 92,521.5 | Steel Pipe 23,130.4 |
| Cable | 369 | 249.9% | — | Wire 55,318.4 | Cable 27,659.2 |
| Iron Plate | 123 | 249.8% | — | Iron Ingot 9,216.5 | Iron Plate 6,144.4 |
| Copper Powder | 45 | 245.5% | — | Copper Ingot 33,142.9 | Copper Powder 5,523.8 |
| Reanimated SAM | 34 | 250.0% | — | SAM 10,200.0 | Reanimated SAM 2,550.0 |
| Alternate: Steel Screws | 29 | 243.9% | — | Steel Beam 353.7 | Screws 18,390.9 |
| Empty Canister | 21 | 248.9% | — | Plastic 1,568.3 | Empty Canister 3,136.5 |
| Ficsite Trigon | 16 | 250.0% | — | Ficsite Ingot 400.0 | Ficsite Trigon 1,200.0 |
| Alternate: Aluminum Beam | 11 | 248.8% | — | Aluminum Ingot 615.8 | Steel Beam 615.8 |

## Assembler — 1,981 machines · 99,051 MW

| Recipe | # | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Automated Wiring | 222 | 249.2% | — | Cable 27,659.2 + Stator 1,383.0 | Automated Wiring 1,383.0 |
| Alternate: Fused Quickwire | 221 | 249.9% | — | Caterium Ingot 4,142.0 + Copper Ingot 20,710.0 | Quickwire 49,704.0 |
| Stator | 216 | 250.0% | — | Steel Pipe 8,099.6 + Wire 21,598.8 | Stator 2,699.9 |
| Alternate: Silicon Circuit Board | 204 | 249.3% | — | Copper Sheet 13,984.4 + Silica 13,984.4 | Circuit Board 6,356.6 |
| Alternate: Steeled Frame | 142 | 248.5% | — | Reinforced Iron Plate 705.7 + Steel Pipe 3,528.4 | Modular Frame 1,058.5 |
| Alternate: Cheap Silica | 126 | 249.5% | — | Limestone 11,788.9 + Raw Quartz 7,073.3 | Silica 16,504.4 |
| Alternate: Encased Industrial Pipe | 120 | 249.6% | — | Concrete 5,990.8 + Steel Pipe 7,189.0 | Encased Industrial Beam 1,198.2 |
| AI Limiter | 111 | 248.2% | — | Copper Sheet 6,888.9 + Quickwire 27,555.6 | AI Limiter 1,377.8 |
| Alclad Aluminum Sheet | 105 | 248.3% | — | Aluminum Ingot 7,821.6 + Copper Ingot 2,607.2 | Alclad Aluminum Sheet 7,821.6 |
| Electromagnetic Control Rod | 88 | 249.4% | — | AI Limiter 877.9 + Stator 1,316.9 | Electromagnetic Control Rod 877.9 |
| Assembly Director System | 74 | 249.2% | — | Adaptive Control Unit 276.6 + Supercomputer 138.3 | Assembly Director System 138.3 |
| Alternate: Stitched Iron Plate | 70 | 249.4% | — | Iron Plate 3,272.9 + Wire 6,545.9 | Reinforced Iron Plate 981.9 |
| Smart Plating | 56 | 246.6% | — | Reinforced Iron Plate 276.2 + Rotor 276.2 | Smart Plating 276.2 |
| Alternate: Copper Rotor | 38 | 248.2% | — | Copper Sheet 2,122.0 + Screws 18,390.9 | Rotor 1,061.0 |
| Alternate: Crystal Computer | 36 | 247.5% | — | Circuit Board 445.5 + Crystal Oscillator 148.5 | Computer 297.0 |
| Magnetic Field Generator | 32 | 250.0% | — | Electromagnetic Control Rod 80.0 + Versatile Framework 200.0 | Magnetic Field Generator 80.0 |
| Encased Plutonium Cell | 31 | 243.9% | — | Concrete 1,512.0 + Plutonium Pellet 756.0 | Encased Plutonium Cell 378.0 |
| Alternate: Electric Motor | 27 | 241.0% | — | Electromagnetic Control Rod 244.0 + Rotor 487.9 | Motor 487.9 |
| Heat Sink | 25 | 244.0% | — | Alclad Aluminum Sheet 2,287.1 + Copper Sheet 1,372.3 | Heat Sink 457.4 |
| Alternate: Alclad Casing | 13 | 241.7% | — | Aluminum Ingot 4,713.7 + Copper Ingot 2,356.8 | Aluminum Casing 3,535.2 |
| Pressure Conversion Cube | 12 | 230.2% | — | Fused Modular Frame 27.6 + Radio Control Unit 55.2 | Pressure Conversion Cube 27.6 |
| Versatile Framework | 9 | 244.0% | — | Modular Frame 54.9 + Steel Beam 658.7 | Versatile Framework 109.8 |
| Alternate: Coated Iron Plate | 3 | 185.4% | — | Iron Ingot 208.6 + Plastic 41.7 | Iron Plate 417.2 |

## Manufacturer — 710 machines · 141,041 MW

| Recipe | # | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Caterium Computer | 121 | 249.5% | — | Circuit Board 4,528.1 + Quickwire 15,848.4 + Rubber 6,792.2 | Computer 1,132.0 |
| Adaptive Control Unit | 111 | 249.2% | — | Automated Wiring 1,383.0 + Circuit Board 1,383.0 + Computer 553.2 + Heavy Modular Frame 276.6 | Adaptive Control Unit 276.6 |
| Alternate: Insulated Crystal Oscillator | 107 | 249.1% | — | AI Limiter 499.9 + Quartz Crystal 4,998.5 + Rubber 3,499.0 | Crystal Oscillator 499.9 |
| Modular Engine | 56 | 246.6% | — | Motor 276.2 + Rubber 2,071.4 + Smart Plating 276.2 | Modular Engine 138.1 |
| Alternate: Heavy Encased Frame | 52 | 245.8% | — | Concrete 2,636.0 + Encased Industrial Beam 1,198.2 + Modular Frame 958.5 + Steel Pipe 4,313.4 | Heavy Modular Frame 359.4 |
| Alternate: Super-State Computer | 37 | 245.8% | — | Battery 2,183.0 + Computer 654.9 + Electromagnetic Control Rod 218.3 + Wire 5,457.4 | Supercomputer 218.3 |
| Radio Control Unit | 36 | 245.5% | — | Aluminum Casing 3,535.2 + Computer 221.0 + Crystal Oscillator 110.5 | Radio Control Unit 221.0 |
| Alternate: Infused Uranium Cell | 34 | 247.1% | — | Quickwire 6,300.0 + Silica 1,260.0 + Sulfur 2,100.0 + Uranium 2,100.0 | Encased Uranium Cell 1,680.0 |
| Alternate: Uranium Fuel Unit | 34 | 247.1% | — | Crystal Oscillator 50.4 + Electromagnetic Control Rod 168.0 + Encased Uranium Cell 1,680.0 + Rotor 168.0 | Uranium Fuel Rod 50.4 |
| Alternate: Classic Battery | 30 | 242.6% | — | Alclad Aluminum Sheet 3,820.2 + Plastic 4,365.9 + Sulfur 3,274.4 + Wire 6,548.9 | Battery 2,183.0 |
| Thermal Propulsion Rocket | 23 | 240.2% | — | Cooling System 165.7 + Fused Modular Frame 55.2 + Modular Engine 138.1 + Turbo Motor 55.2 | Thermal Propulsion Rocket 55.2 |
| Ballistic Warp Drive | 22 | 250.0% | 4 | Dark Matter Crystal 2,200.0 + Singularity Cell 275.0 + Superposition Oscillator 110.0 + Thermal Propulsion Rocket 55.0 | Ballistic Warp Drive 110.0 |
| Plutonium Fuel Rod | 21 | 240.0% | — | Electromagnetic Control Rod 75.6 + Encased Plutonium Cell 378.0 + Heat Sink 126.0 + Steel Beam 226.8 | Plutonium Fuel Rod 12.6 |
| Singularity Cell | 12 | 230.2% | — | Concrete 5,523.8 + Dark Matter Crystal 552.4 + Iron Plate 2,761.9 + Nuclear Pasta 27.6 | Singularity Cell 276.2 |
| Alternate: Turbo Electric Motor | 8 | 245.5% | — | Electromagnetic Control Rod 92.1 + Motor 128.9 + Radio Control Unit 165.7 + Rotor 128.9 | Turbo Motor 55.2 |
| Alternate: Flexible Framework | 5 | 240.6% | — | Modular Frame 45.1 + Rubber 360.9 + Steel Beam 270.7 | Versatile Framework 90.2 |
| Ballistic Warp Drive | 1 | 23.8% | — | Dark Matter Crystal 9.5 + Singularity Cell 1.2 + Superposition Oscillator 0.5 + Thermal Propulsion Rocket 0.2 | Ballistic Warp Drive 0.2 |

## Converter — 253 machines · 208,737 MW

| Recipe | # | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Time Crystal | 157 | 249.7% | — | Diamonds 4,704.8 | Time Crystal 2,352.4 |
| Coal (Limestone) | 33 | 247.3% | — | Limestone 29,383.2 + Reanimated SAM 816.2 | Coal 9,794.4 |
| Excited Photonic Matter | 18 | 243.4% | — | — | Excited Photonic Matter 8,761.9 |
| Bauxite (Caterium) | 14 | 248.6% | — | Caterium Ore 5,220.6 + Reanimated SAM 348.0 | Bauxite 4,176.5 |
| Sulfur (Iron) | 11 | 236.1% | — | Iron Ore 7,790.6 + Reanimated SAM 259.7 | Sulfur 3,116.3 |
| Bauxite (Copper) | 9 | 223.8% | — | Copper Ore 3,626.2 + Reanimated SAM 201.5 | Bauxite 2,417.5 |
| Ficsite Ingot (Aluminum) | 6 | 222.2% | — | Aluminum Ingot 1,600.0 + Reanimated SAM 800.0 | Ficsite Ingot 400.0 |
| Nitrogen Gas (Caterium) | 5 | 249.2% | — | Caterium Ore 1,495.4 + Reanimated SAM 124.6 | Nitrogen Gas 1,495.4 |

## Smelter — 252 machines · 3,383 MW

| Recipe | # | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Pure Aluminum Ingot | 252 | 249.9% | — | Aluminum Scrap 37,787.8 | Aluminum Ingot 18,893.9 |

## Blender — 223 machines · 54,429 MW

| Recipe | # | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Diluted Fuel | 103 | 249.1% | — | Heavy Oil Residue 12,829.2 + Water 25,658.5 | Fuel 25,658.5 |
| Alternate: Nitro Rocket Fuel | 28 | 247.0% | — | Coal 3,457.4 + Fuel 6,914.9 + Nitrogen Gas 5,186.1 + Sulfur 6,914.9 | Compacted Coal 1,728.7 + Rocket Fuel 10,372.3 |
| Nitric Acid | 22 | 239.4% | — | Iron Plate 526.7 + Nitrogen Gas 6,320.7 + Water 1,580.2 | Nitric Acid 1,580.2 |
| Non-Fissile Uranium | 21 | 240.0% | — | Nitric Acid 756.0 + Silica 1,260.0 + Sulfuric Acid 756.0 + Uranium Waste 1,890.0 | Non-Fissile Uranium 2,520.0 + Water 756.0 |
| Alternate: Turbo Blend Fuel | 16 | 241.9% | — | Fuel 580.6 + Heavy Oil Residue 1,161.3 + Petroleum Coke 871.0 + Sulfur 871.0 | Turbofuel 1,741.9 |
| Alternate: Cooling Device | 14 | 236.7% | — | Heat Sink 331.4 + Motor 82.9 + Nitrogen Gas 1,988.6 | Cooling System 165.7 |
| Alternate: Heat-Fused Frame | 12 | 230.2% | — | Aluminum Ingot 4,142.9 + Fuel 828.6 + Heavy Modular Frame 82.9 + Nitric Acid 662.9 | Fused Modular Frame 82.9 |
| Rocket Fuel | 7 | 230.5% | — | Nitric Acid 161.3 + Turbofuel 967.9 | Compacted Coal 161.3 + Rocket Fuel 1,613.2 |

## Accelerator — 93 machines · 202,238 MW

| Recipe | # | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Turbo Diamonds | 32 | 245.0% | — | Coal 47,047.6 + Packaged Turbofuel 3,136.5 | Diamonds 4,704.8 |
| Alternate: Dark Matter Trap | 27 | 241.0% | — | Dark Matter Residue 9,761.9 + Time Crystal 1,952.4 | Dark Matter Crystal 3,904.8 |
| Nuclear Pasta | 23 | 240.2% | — | Copper Powder 5,523.8 + Pressure Conversion Cube 27.6 | Nuclear Pasta 27.6 |
| Plutonium Pellet | 11 | 229.1% | — | Non-Fissile Uranium 2,520.0 + Uranium Waste 630.0 | Plutonium Pellet 756.0 |

## Packager — 63 machines · 2,103 MW

| Recipe | # | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Packaged Turbofuel | 63 | 248.9% | — | Empty Canister 3,136.5 + Turbofuel 3,136.5 | Packaged Turbofuel 3,136.5 |

## Quantum Encoder — 35 machines · 146,271 MW

| Recipe | # | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Superposition Oscillator | 16 | 238.1% | — | Alclad Aluminum Sheet 1,714.3 + Crystal Oscillator 190.5 + Dark Matter Crystal 1,142.9 + Excited Photonic Matter 4,761.9 | Dark Matter Residue 4,761.9 + Superposition Oscillator 190.5 |
| Neural-Quantum Processor | 11 | 242.4% | — | Excited Photonic Matter 2,000.0 + Ficsite Trigon 1,200.0 + Supercomputer 80.0 + Time Crystal 400.0 | Dark Matter Residue 2,000.0 + Neural-Quantum Processor 80.0 |
| AI Expansion Server | 8 | 250.0% | 2 | Excited Photonic Matter 2,000.0 + Magnetic Field Generator 80.0 + Neural-Quantum Processor 80.0 + Superposition Oscillator 80.0 | AI Expansion Server 120.0 + Dark Matter Residue 3,000.0 |

## Foundry — 24 machines · 1,278 MW

| Recipe | # | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Solid Steel Ingot | 16 | 248.3% | — | Coal 1,589.3 + Iron Ingot 1,589.3 | Steel Ingot 2,384.0 |
| Alternate: Molded Beam | 8 | 248.3% | — | Concrete 1,589.3 + Steel Ingot 2,384.0 | Steel Beam 894.0 |

---

# Resource extraction

Raw-material supply: miners, water/oil extractors and pressure wells. (The high-level overview aggregates these by resource; here each node group is listed.)

## Water Extractor — 767 machines · 51,458 MW

| Recipe | # | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Water Extraction | 767 | 249.8% | — | — | Water 229,933.1 |

## Miner Mk.3 — 414 machines · 62,555 MW

| Recipe | # | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Limestone (Normal) Mk.3 | 50 | 250.0% | — | — | Limestone 30,000.0 |
| Iron Ore (Pure) Mk.3 | 46 | 250.0% | — | — | Iron Ore 55,200.0 |
| Iron Ore (Normal) Mk.3 | 42 | 250.0% | — | — | Iron Ore 25,200.0 |
| Iron Ore (Impure) Mk.3 | 39 | 250.0% | — | — | Iron Ore 11,700.0 |
| Coal (Normal) Mk.3 | 31 | 250.0% | — | — | Coal 18,600.0 |
| Copper Ore (Normal) Mk.3 | 29 | 250.0% | — | — | Copper Ore 17,400.0 |
| Limestone (Pure) Mk.3 | 29 | 250.0% | — | — | Limestone 34,800.0 |
| Coal (Pure) Mk.3 | 16 | 250.0% | — | — | Coal 19,200.0 |
| Coal (Impure) Mk.3 | 15 | 250.0% | — | — | Coal 4,500.0 |
| Copper Ore (Impure) Mk.3 | 13 | 250.0% | — | — | Copper Ore 3,900.0 |
| Copper Ore (Pure) Mk.3 | 13 | 250.0% | — | — | Copper Ore 15,600.0 |
| SAM (Impure) Mk.3 | 10 | 250.0% | — | — | SAM 3,000.0 |
| Caterium Ore (Normal) Mk.3 | 9 | 250.0% | — | — | Caterium Ore 5,400.0 |
| Caterium Ore (Pure) Mk.3 | 8 | 250.0% | — | — | Caterium Ore 9,600.0 |
| Quartz (Normal) Mk.3 | 7 | 250.0% | — | — | Raw Quartz 4,200.0 |
| Quartz (Pure) Mk.3 | 7 | 250.0% | — | — | Raw Quartz 8,400.0 |
| Sulfur (Impure) Mk.3 | 6 | 250.0% | — | — | Sulfur 1,800.0 |
| Bauxite (Normal) Mk.3 | 6 | 250.0% | — | — | Bauxite 3,600.0 |
| SAM (Normal) Mk.3 | 6 | 250.0% | — | — | SAM 3,600.0 |
| Bauxite (Pure) Mk.3 | 6 | 250.0% | — | — | Bauxite 7,200.0 |
| Bauxite (Impure) Mk.3 | 5 | 250.0% | — | — | Bauxite 1,500.0 |
| Sulfur (Normal) Mk.3 | 5 | 250.0% | — | — | Sulfur 3,000.0 |
| Sulfur (Pure) Mk.3 | 5 | 250.0% | — | — | Sulfur 6,000.0 |
| Quartz (Impure) Mk.3 | 3 | 250.0% | — | — | Raw Quartz 900.0 |
| Uranium (Impure) Mk.3 | 3 | 250.0% | — | — | Uranium 900.0 |
| SAM (Pure) Mk.3 | 3 | 250.0% | — | — | SAM 3,600.0 |
| Uranium (Normal) Mk.3 | 2 | 250.0% | — | — | Uranium 1,200.0 |

## Oil Extractor — 30 machines · 4,029 MW

| Recipe | # | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Crude Oil (Normal) | 12 | 250.0% | — | — | Crude Oil 3,600.0 |
| Crude Oil (Impure) | 10 | 250.0% | — | — | Crude Oil 1,500.0 |
| Crude Oil (Pure) | 8 | 250.0% | — | — | Crude Oil 4,800.0 |

## Miner Mk2 — 15 machines · 755 MW

| Recipe | # | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Limestone (Impure) Mk.2 | 15 | 250.0% | — | — | Limestone 2,250.0 |

## Resource Well Pressurizer — 9 machines · 4,533 MW

| Recipe | # | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Crater Lakes Oil Well | 1 | 250.0% | — | — | Crude Oil 1,350.0 |
| Central Nitrogen Gas Well | 1 | 250.0% | — | — | Nitrogen Gas 3,000.0 |
| Northern Nitrogen Gas Well | 1 | 250.0% | — | — | Nitrogen Gas 1,800.0 |
| Northwestern Nitrogen Gas Well | 1 | 250.0% | — | — | Nitrogen Gas 1,950.0 |
| Southeastern Nitrogen Gas Well | 1 | 250.0% | — | — | Nitrogen Gas 1,650.0 |
| Southern Nitrogen Gas Well | 1 | 250.0% | — | — | Nitrogen Gas 1,500.0 |
| Southwestern Nitrogen Gas Well | 1 | 250.0% | — | — | Nitrogen Gas 2,100.0 |
| Spire Coast Oil Well | 1 | 250.0% | — | — | Crude Oil 900.0 |
| Swamp Oil Well | 1 | 250.0% | — | — | Crude Oil 450.0 |

---

# Power generation

## Geothermal Generator — 31 machines · **7,100 MW generated**

| Recipe | # | clock | slps | fuel /min | output |
|---|---|---:|---:|---|---|
| Geothermal Power (Pure) | 9 | 100.0% | — | — | 3,600 MW |
| Geothermal Power (Normal) | 13 | 100.0% | — | — | 2,600 MW |
| Geothermal Power (Impure) | 9 | 100.0% | — | — | 900 MW |

## Nuclear Power Plant — 101 machines · **630,000 MW generated**

| Recipe | # | clock | slps | fuel /min | output |
|---|---|---:|---:|---|---|
| Nuclear Power (Uranium) | 101 | 249.5% | — | Uranium Fuel Rod 50.4 + Water 60,480.0 | 630,000 MW |

## Fuel Generator — 1,151 machines · **719,131 MW generated**

| Recipe | # | clock | slps | fuel /min | output |
|---|---|---:|---:|---|---|
| Rocket Fuel Power | 1,151 | 249.9% | — | Rocket Fuel 11,985.5 | 719,131 MW |

---

## Notes

- **Power rounding**: per-section draws are computed from the displayed whole-machine counts and sum to 1,336,752 MW, ~0.1% under the official 1,342,803 MW (the model also runs tiny sub-machine exact-balance slivers). Generation is clock-linear, so whole-machine sums reproduce the 1,356,231 MW exactly.
- Accelerator rows use per-recipe power draw where the spec overrides it; other machines use their machine default.
- Rates are **aggregate** at the displayed clock. Per-machine rate at that clock = aggregate ÷ `#`.
