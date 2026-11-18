# Satisfactory Factory Optimiser — Build Plan

**Official optimum** — **455,800,604 pts/min** (overclock tiers 25%, 50%, 75%, 100%, 125%, 150%, 175%, 200%, 225%, 250%; Auto-solved (augmenter sweep)). All rates are per minute.

## High-level overview

| Metric | Value | Notes |
|---|---|---|
| **Sink points** | **455,800,604 pts/min** | 0 augmenter(s), 1.00x power |
| **Power load** | **1,004,591 MW** | what consumers actually draw |
| **Power supplied** | 1,014,637 MW | load x1.01 (1% reserve) |
| **Machines** | **8,238** (cap 8,192 — binding) | 138 recipe rows across 18 machine types |
| **Somersloops** | 104 / 104 | see overclock notes |
| **Sink throughput** | 322.6 items/min | one Awesome Sink covers it (1200/min cap, 30 MW) |

### Sink flows

| Sink item | pts/item | /min | pts/min | share |
|---|---:|---:|---:|---:|
| Ballistic Warp Drive | 2,895,334 | 120.0 | 347,440,080 | 76.2% |
| AI Expansion Server | 597,652 | 116.7 | 69,726,067 | 15.3% |
| Assembly Director System | 500,176 | 73.4 | 36,704,339 | 8.1% |
| Plutonium Fuel Rod | 153,184 | 12.6 | 1,930,118 | 0.4% |
| **TOTAL** | | | **455,800,604** | 100% |

### Map resources extracted

Miners are shown at their planned 250% clock; every tapped node group is maxed.

| Resource | extractors | /min |
|---|---:|---:|
| Water | 584 | 175,126 |
| Iron Ore | 88 | 80,400 |
| Coal | 62 | 42,300 |
| Limestone | 36 | 38,535 |
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
| Water | 188,658.7 | 188,658.7 | -0.0 | balanced |
| Iron Ore | 80,400.0 | 80,400.0 | +0.0 | balanced |
| Copper Ingot | 76,854.4 | 76,854.4 | +0.0 | balanced |
| Iron Ingot | 72,212.0 | 72,212.0 | +0.0 | balanced |
| Coal | 54,331.0 | 54,331.0 | -0.0 | balanced |
| Quickwire | 45,486.0 | 45,486.0 | +0.0 | balanced |
| Limestone | 38,535.2 | 38,535.2 | +0.0 | balanced |
| Copper Ore | 36,900.0 | 36,900.0 | -0.0 | balanced |
| Aluminum Scrap | 36,503.4 | 36,503.4 | +0.0 | balanced |
| Wire | 32,063.8 | 32,063.8 | +0.0 | balanced |
| Fuel | 21,914.0 | 21,914.0 | +0.0 | balanced |
| Alumina Solution | 21,902.0 | 21,902.0 | +0.0 | balanced |
| Silica | 20,796.0 | 20,796.0 | +0.0 | balanced |
| Rubber | 20,155.0 | 20,155.0 | -0.0 | balanced |
| Bauxite | 18,251.7 | 18,251.7 | +0.0 | balanced |
| Aluminum Ingot | 18,251.7 | 18,251.7 | -0.0 | balanced |
| Heavy Oil Residue | 16,800.0 | 16,800.0 | -0.0 | balanced |
| Concrete | 15,787.3 | 15,787.3 | -0.0 | balanced |
| Screws | 15,726.4 | 15,726.4 | +0.0 | balanced |
| Copper Sheet | 15,548.3 | 15,548.3 | +0.0 | balanced |
| Caterium Ore | 15,000.0 | 15,000.0 | -0.0 | balanced |
| Steel Pipe | 14,771.5 | 14,771.5 | +0.0 | balanced |
| Plastic | 14,167.8 | 14,167.8 | +0.0 | balanced |
| Raw Quartz | 13,500.0 | 13,500.0 | +0.0 | balanced |
| Nitrogen Gas | 13,017.3 | 13,017.3 | +0.0 | balanced |
| Crude Oil | 12,600.0 | 12,600.0 | +0.0 | balanced |
| Petroleum Coke | 11,353.1 | 11,353.1 | +0.0 | balanced |
| Sulfur | 10,800.0 | 10,800.0 | +0.0 | balanced |
| Dark Matter Residue | 10,750.0 | 10,750.0 | +0.0 | balanced |
| Excited Photonic Matter | 10,250.0 | 10,250.0 | -0.0 | balanced |
| SAM | 10,200.0 | 10,200.0 | +0.0 | balanced |
| Polymer Resin | 8,400.0 | 8,400.0 | -0.0 | balanced |
| Rocket Fuel | 6,292.3 | 6,292.3 | +0.0 | balanced |
| Copper Powder | 6,000.0 | 6,000.0 | +0.0 | balanced |
| Iron Plate | 5,836.9 | 5,836.9 | +0.0 | balanced |
| Diamonds | 5,266.7 | 5,266.7 | +0.0 | balanced |
| Circuit Board | 5,211.3 | 5,211.3 | +0.0 | balanced |
| Alclad Aluminum Sheet | 4,925.9 | 4,925.9 | +0.0 | balanced |
| Aluminum Casing | 4,329.5 | 4,329.5 | +0.0 | balanced |
| Dark Matter Crystal | 4,300.0 | 4,300.0 | +0.0 | balanced |
| Turbofuel | 4,290.6 | 4,290.6 | +0.0 | balanced |
| Caterium Ingot | 4,246.8 | 4,246.8 | -0.0 | balanced |
| Quartz Crystal | 3,568.0 | 3,568.0 | +0.0 | balanced |
| Empty Canister | 3,511.1 | 3,511.1 | +0.0 | balanced |
| Packaged Turbofuel | 3,511.1 | 3,511.1 | -0.0 | balanced |
| Steel Ingot | 3,344.6 | 3,344.6 | -0.0 | balanced |
| Time Crystal | 2,633.3 | 2,633.3 | -0.0 | balanced |
| Reanimated SAM | 2,550.0 | 2,550.0 | -0.0 | balanced |
| Non-Fissile Uranium | 2,520.0 | 2,520.0 | +0.0 | balanced |
| Uranium Waste | 2,520.0 | 2,520.0 | +0.0 | balanced |
| Uranium | 2,100.0 | 2,100.0 | +0.0 | balanced |
| Nitric Acid | 1,727.0 | 1,727.0 | +0.0 | balanced |
| Battery | 1,700.5 | 1,700.5 | +0.0 | balanced |
| Encased Uranium Cell | 1,680.0 | 1,680.0 | +0.0 | balanced |
| Ficsite Trigon | 1,450.0 | 1,450.0 | +0.0 | balanced |
| Stator | 1,356.3 | 1,356.3 | +0.0 | balanced |
| Sulfuric Acid | 1,276.5 | 1,276.5 | +0.0 | balanced |
| Steel Beam | 1,254.2 | 1,254.2 | -0.0 | balanced |
| Computer | 983.1 | 983.1 | +0.0 | balanced |
| Compacted Coal | 962.1 | 962.1 | -0.0 | balanced |
| Rotor | 907.3 | 907.3 | -0.0 | balanced |
| Encased Industrial Beam | 839.7 | 839.7 | +0.0 | balanced |
| Electromagnetic Control Rod | 819.8 | 819.8 | -0.0 | balanced |
| Modular Frame | 792.6 | 792.6 | +0.0 | balanced |
| Plutonium Pellet | 756.0 | 756.0 | +0.0 | balanced |
| Automated Wiring | 733.8 | 733.8 | +0.0 | balanced |
| Reinforced Iron Plate | 678.4 | 678.4 | +0.0 | balanced |
| High-Speed Connector | 544.9 | 544.9 | +0.0 | balanced |
| Motor | 519.9 | 519.9 | +0.0 | balanced |
| Heat Sink | 486.0 | 486.0 | +0.0 | balanced |
| Ficsite Ingot | 483.3 | 483.3 | -0.0 | balanced |
| AI Limiter | 453.8 | 453.8 | +0.0 | balanced |
| Encased Plutonium Cell | 378.0 | 378.0 | +0.0 | balanced |
| Empty Fluid Tank | 363.2 | 363.2 | +0.0 | balanced |
| Packaged Nitrogen Gas | 363.2 | 363.2 | -0.0 | balanced |
| Crystal Oscillator | 356.8 | 356.8 | -0.0 | balanced |
| Singularity Cell | 300.0 | 300.0 | +0.0 | balanced |
| Smart Plating | 300.0 | 300.0 | +0.0 | balanced |
| Heavy Modular Frame | 251.9 | 251.9 | +0.0 | balanced |
| Versatile Framework | 241.7 | 241.7 | +0.0 | balanced |
| Superposition Oscillator | 216.7 | 216.7 | +0.0 | balanced |
| Cooling System | 180.0 | 180.0 | +0.0 | balanced |
| Radio Control Unit | 179.5 | 179.5 | +0.0 | balanced |
| Supercomputer | 170.0 | 170.0 | +0.0 | balanced |
| Modular Engine | 150.0 | 150.0 | +0.0 | balanced |
| Adaptive Control Unit | 146.8 | 146.8 | +0.0 | balanced |
| Ballistic Warp Drive | 120.0 | 0.0 | +120.0 | → Awesome Sink (120.0/min) |
| AI Expansion Server | 116.7 | 0.0 | +116.7 | → Awesome Sink (116.7/min) |
| Fused Modular Frame | 105.1 | 105.1 | +0.0 | balanced |
| Neural-Quantum Processor | 96.7 | 96.7 | +0.0 | balanced |
| Magnetic Field Generator | 96.7 | 96.7 | -0.0 | balanced |
| Assembly Director System | 73.4 | 0.0 | +73.4 | → Awesome Sink (73.4/min) |
| Thermal Propulsion Rocket | 60.0 | 60.0 | +0.0 | balanced |
| Turbo Motor | 60.0 | 60.0 | +0.0 | balanced |
| Uranium Fuel Rod | 50.4 | 50.4 | +0.0 | balanced |
| Pressure Conversion Cube | 45.1 | 45.1 | +0.0 | balanced |
| Nuclear Pasta | 30.0 | 30.0 | +0.0 | balanced |
| Plutonium Fuel Rod | 12.6 | 0.0 | +12.6 | → Awesome Sink (12.6/min) |

---

# All used recipes

99 production recipe rows from 98 distinct recipes (rows repeat a recipe when sloop grades or clocks differ); extractors are listed in the Resource extraction table underneath. `count` is the machines to build, with the raw fractional count in brackets; `clock` shows how to split that build into whole machines at the clock tier plus one trimmed remainder (e.g. `10@100% + 1@50%`); `equivalent all-machine clock` is the single uniform clock that reproduces the same throughput. A row whose equivalent clock sits below the tier is an exact-balance remnant, not a choice.

| Recipe | machine | count | clock | equivalent all-machine clock |
|---|---|---:|---:|---:|
| Alternate: Dark Matter Trap | accelerator | 144 (143.3333) | 143@50% + 1@16.7% | 49.8% |
| Alternate: Turbo Diamonds | accelerator | 71 (70.2222) | 70@125% + 1@27.8% | 123.6% |
| Nuclear Pasta | accelerator | 120 (120.0000) | 120@50% | 50.0% |
| Plutonium Pellet | accelerator | 34 (33.6000) | 33@75% + 1@45% | 74.1% |
| AI Limiter | assembler | 37 (36.3012) | 36@250% + 1@75.3% | 245.3% |
| Alclad Aluminum Sheet | assembler | 66 (65.6782) | 65@250% + 1@169.6% | 248.8% |
| Alternate: Alclad Casing | assembler | 16 (15.3937) | 15@250% + 1@98.4% | 240.5% |
| Alternate: Cheap Silica | assembler | 159 (158.4456) | 158@250% + 1@111.4% | 249.1% |
| Alternate: Coated Iron Plate | assembler | 32 (31.1302) | 31@250% + 1@32.5% | 243.2% |
| Alternate: Copper Rotor | assembler | 33 (32.2592) | 32@250% + 1@64.8% | 244.4% |
| Alternate: Electric Motor | assembler | 28 (27.7286) | 27@250% + 1@182.2% | 247.6% |
| Alternate: Electromagnetic Connection Rod | assembler | 37 (36.1432) | 36@250% + 1@35.8% | 244.2% |
| Alternate: Encased Industrial Pipe | assembler | 84 (83.9663) | 83@250% + 1@241.6% | 249.9% |
| Alternate: Fused Quickwire | assembler | 203 (202.1601) | 202@250% + 1@40% | 249.0% |
| Alternate: Fused Wire | assembler | 61 (60.8456) | 60@250% + 1@211.4% | 249.4% |
| Alternate: Heat Exchanger | assembler | 20 (19.4400) | 19@250% + 1@110% | 243.0% |
| Alternate: Silicon Circuit Board | assembler | 167 (166.7618) | 166@250% + 1@190.5% | 249.6% |
| Alternate: Steeled Frame | assembler | 106 (105.6751) | 105@250% + 1@168.8% | 249.2% |
| Alternate: Stitched Iron Plate | assembler | 49 (48.2400) | 48@250% + 1@60% | 246.1% |
| Assembly Director System | assembler | 40 (39.1375) | 39@250% + 1@34.4% | 244.6% |
| Electromagnetic Control Rod | assembler | 10 (9.6964) | 9@250% + 1@174.1% | 242.4% |
| Encased Plutonium Cell | assembler | 31 (30.2400) | 30@250% + 1@60% | 243.9% |
| Magnetic Field Generator | assembler | 39 (38.6667) | 38@250% + 1@166.7% | 247.9% |
| Pressure Conversion Cube | assembler | 19 (18.0532) | 18@250% + 1@13.3% | 237.5% |
| Stator | assembler | 109 (108.5032) | 108@250% + 1@125.8% | 248.9% |
| Alternate: Cooling Device | blender | 15 (14.4000) | 14@250% + 1@100% | 240.0% |
| Alternate: Diluted Fuel | blender | 88 (87.6558) | 87@250% + 1@164% | 249.0% |
| Alternate: Heat-Fused Frame | blender | 15 (14.0177) | 14@250% + 1@4.4% | 233.6% |
| Alternate: Nitro Rocket Fuel | blender | 14 (13.3150) | 13@250% + 1@78.8% | 237.8% |
| Alternate: Turbo Blend Fuel | blender | 28 (27.4486) | 27@250% + 1@112.2% | 245.1% |
| Nitric Acid | blender | 24 (23.0264) | 23@250% + 1@6.6% | 239.9% |
| Non-Fissile Uranium | blender | 21 (20.1600) | 20@250% + 1@40% | 240.0% |
| Rocket Fuel | blender | 6 (5.1966) | 5@250% + 1@49.2% | 216.5% |
| Alternate: Iron Pipe | constructor | 237 (236.3441) | 236@250% + 1@86% | 249.3% |
| Alternate: Iron Wire | constructor | 327 (326.6410) | 326@250% + 1@160.3% | 249.7% |
| Alternate: Steel Screws | constructor | 25 (24.1944) | 24@250% + 1@48.6% | 241.9% |
| Copper Powder | constructor | 48 (48.0000) | 48@250% | 250.0% |
| Empty Canister | constructor | 24 (23.4074) | 23@250% + 1@101.9% | 243.8% |
| Empty Fluid Tank | constructor | 3 (2.4213) | 2@250% + 1@105.3% | 201.8% |
| Ficsite Trigon | constructor | 20 (19.3333) | 19@250% + 1@83.3% | 241.7% |
| Reanimated SAM | constructor | 34 (34.0000) | 34@250% | 250.0% |
| Bauxite (Caterium) | converter | 31 (30.9406) | 30@125% + 1@117.6% | 124.8% |
| Bauxite (Copper) | converter | 9 (8.7374) | 8@125% + 1@92.2% | 121.4% |
| Coal (Iron) | converter | 81 (80.2070) | 80@125% + 1@25.9% | 123.8% |
| Excited Photonic Matter | converter | 41 (41.0000) | 41@125% | 125.0% |
| Ficsite Ingot (Aluminum) | converter | 13 (12.8889) | 12@125% + 1@111.1% | 123.9% |
| Nitrogen Gas (Caterium) | converter | 7 (6.7818) | 6@125% + 1@97.7% | 121.1% |
| Time Crystal | converter | 352 (351.1111) | 351@125% + 1@13.9% | 124.7% |
| Alternate: Coke Steel Ingot | foundry | 14 (13.3785) | 13@250% + 1@94.6% | 238.9% |
| Alternate: Copper Alloy Ingot | foundry | 168 (167.6926) | 167@250% + 1@173.2% | 249.5% |
| Alternate: Molded Beam | foundry | 12 (11.1487) | 11@250% + 1@37.2% | 232.3% |
| Rocket Fuel Power | fuel_generator | 605 (604.0590) | 604@250% + 1@14.8% | 249.6% |
| Geothermal Power (Impure) | geothermal_generator | 9 (9.0000) | 9@100% | 100.0% |
| Geothermal Power (Normal) | geothermal_generator | 13 (13.0000) | 13@100% | 100.0% |
| Geothermal Power (Pure) | geothermal_generator | 9 (9.0000) | 9@100% | 100.0% |
| Adaptive Control Unit | manufacturer | 59 (58.7063) | 58@250% + 1@176.6% | 248.8% |
| Alternate: Automated Speed Wiring | manufacturer | 40 (39.1375) | 39@250% + 1@34.4% | 244.6% |
| Alternate: Caterium Computer | manufacturer | 105 (104.8691) | 104@250% + 1@217.3% | 249.7% |
| Alternate: Classic Battery | manufacturer | 23 (22.6733) | 22@250% + 1@168.3% | 246.4% |
| Alternate: Flexible Framework | manufacturer | 13 (12.8889) | 12@250% + 1@222.2% | 247.9% |
| Alternate: Heavy Encased Frame | manufacturer | 36 (35.8256) | 35@250% + 1@206.4% | 248.8% |
| Alternate: Infused Uranium Cell | manufacturer | 34 (33.6000) | 33@250% + 1@150% | 247.1% |
| Alternate: Insulated Crystal Oscillator | manufacturer | 77 (76.1174) | 76@250% + 1@29.4% | 247.1% |
| Alternate: Plastic Smart Plating | manufacturer | 24 (24.0000) | 24@250% | 250.0% |
| Alternate: Silicon High-Speed Connector | manufacturer | 73 (72.6519) | 72@250% + 1@163% | 248.8% |
| Alternate: Super-State Computer | manufacturer | 29 (28.3416) | 28@250% + 1@85.4% | 244.3% |
| Alternate: Turbo Electric Motor | manufacturer | 5 (4.2288) | 4@250% + 1@57.2% | 211.4% |
| Alternate: Turbo Pressure Motor | manufacturer | 4 (3.2284) | 3@250% + 1@57.1% | 201.8% |
| Alternate: Uranium Fuel Unit | manufacturer | 34 (33.6000) | 33@250% + 1@150% | 247.1% |
| Ballistic Warp Drive (4 sloops) | manufacturer | 24 (24.0000) | 24@250% | 250.0% |
| Modular Engine | manufacturer | 60 (60.0000) | 60@250% | 250.0% |
| Plutonium Fuel Rod | manufacturer | 21 (20.1600) | 20@250% + 1@40% | 240.0% |
| Radio Control Unit | manufacturer | 29 (28.7148) | 28@250% + 1@178.7% | 247.5% |
| Singularity Cell | manufacturer | 12 (12.0000) | 12@250% | 250.0% |
| Thermal Propulsion Rocket | manufacturer | 24 (24.0000) | 24@250% | 250.0% |
| Nuclear Power (Uranium) | nuclear_power_plant | 101 (100.8000) | 100@250% + 1@200% | 249.5% |
| Packaged Nitrogen Gas | packager | 3 (2.4213) | 2@250% + 1@105.3% | 201.8% |
| Packaged Turbofuel | packager | 71 (70.2222) | 70@250% + 1@55.6% | 247.3% |
| AI Expansion Server | quantum_encoder | 29 (28.3333) | 28@50% + 1@16.7% | 48.9% |
| AI Expansion Server (2 sloops) | quantum_encoder | 4 (4.0000) | 4@250% | 250.0% |
| Neural-Quantum Processor | quantum_encoder | 65 (64.4444) | 64@50% + 1@22.2% | 49.6% |
| Superposition Oscillator | quantum_encoder | 87 (86.6667) | 86@50% + 1@33.3% | 49.8% |
| Alternate: Electrode Aluminum Scrap | refinery | 49 (48.6712) | 48@250% + 1@167.8% | 248.3% |
| Alternate: Heavy Oil Residue | refinery | 168 (168.0000) | 168@250% | 250.0% |
| Alternate: Leached Caterium Ingot | refinery | 7 (6.9402) | 6@250% + 1@235.1% | 247.9% |
| Alternate: Pure Caterium Ingot | refinery | 121 (120.7408) | 120@250% + 1@185.2% | 249.5% |
| Alternate: Pure Copper Ingot | refinery | 373 (372.6004) | 372@250% + 1@150.1% | 249.7% |
| Alternate: Pure Iron Ingot | refinery | 445 (444.3817) | 444@250% + 1@95.4% | 249.7% |
| Alternate: Pure Quartz Crystal | refinery | 28 (27.1848) | 27@250% + 1@46.2% | 242.7% |
| Alternate: Recycled Plastic | refinery | 95 (94.4517) | 94@250% + 1@112.9% | 248.6% |
| Alternate: Recycled Rubber | refinery | 107 (106.3669) | 106@250% + 1@91.7% | 248.5% |
| Alternate: Sloppy Alumina | refinery | 37 (36.5034) | 36@250% + 1@125.8% | 246.6% |
| Alternate: Steamed Copper Sheet | refinery | 277 (276.4139) | 276@250% + 1@103.5% | 249.5% |
| Alternate: Wet Concrete | refinery | 79 (78.9366) | 78@250% + 1@234.1% | 249.8% |
| Petroleum Coke | refinery | 38 (37.8437) | 37@250% + 1@210.9% | 249.0% |
| Residual Rubber | refinery | 84 (84.0000) | 84@250% | 250.0% |
| Sulfuric Acid | refinery | 11 (10.2121) | 10@250% + 1@53% | 232.1% |
| Turbofuel | refinery | 26 (25.6561) | 25@250% + 1@164% | 246.7% |
| Alternate: Pure Aluminum Ingot | smelter | 244 (243.3559) | 243@250% + 1@89% | 249.3% |

### Resource extraction

Miners, water/oil extractors and pressure wells pulled out of All used recipes — every tapped node group at its planned count/clock. (Per-node grouping is further down in the dedicated Resource extraction section.)

| Recipe | machine | count | clock | equivalent all-machine clock |
|---|---|---:|---:|---:|
| Bauxite (Impure) Mk.3 | miner_mk3 | 5 (5.0000) | 5@250% | 250.0% |
| Bauxite (Normal) Mk.3 | miner_mk3 | 6 (6.0000) | 6@250% | 250.0% |
| Bauxite (Pure) Mk.3 | miner_mk3 | 6 (6.0000) | 6@250% | 250.0% |
| Caterium Ore (Normal) Mk.3 | miner_mk3 | 9 (9.0000) | 9@250% | 250.0% |
| Caterium Ore (Pure) Mk.3 | miner_mk3 | 8 (8.0000) | 8@250% | 250.0% |
| Coal (Impure) Mk.3 | miner_mk3 | 15 (15.0000) | 15@250% | 250.0% |
| Coal (Normal) Mk.3 | miner_mk3 | 31 (31.0000) | 31@250% | 250.0% |
| Coal (Pure) Mk.3 | miner_mk3 | 16 (16.0000) | 16@250% | 250.0% |
| Copper Ore (Impure) Mk.3 | miner_mk3 | 13 (13.0000) | 13@250% | 250.0% |
| Copper Ore (Normal) Mk.3 | miner_mk3 | 29 (29.0000) | 29@250% | 250.0% |
| Copper Ore (Pure) Mk.3 | miner_mk3 | 13 (13.0000) | 13@250% | 250.0% |
| Iron Ore (Normal) Mk.3 | miner_mk3 | 42 (42.0000) | 42@250% | 250.0% |
| Iron Ore (Pure) Mk.3 | miner_mk3 | 46 (46.0000) | 46@250% | 250.0% |
| Limestone (Normal) Mk.3 | miner_mk3 | 7 (6.2254) | 6@250% + 1@56.4% | 222.3% |
| Limestone (Pure) Mk.3 | miner_mk3 | 29 (29.0000) | 29@250% | 250.0% |
| Quartz (Impure) Mk.3 | miner_mk3 | 3 (3.0000) | 3@250% | 250.0% |
| Quartz (Normal) Mk.3 | miner_mk3 | 7 (7.0000) | 7@250% | 250.0% |
| Quartz (Pure) Mk.3 | miner_mk3 | 7 (7.0000) | 7@250% | 250.0% |
| SAM (Impure) Mk.3 | miner_mk3 | 10 (10.0000) | 10@250% | 250.0% |
| SAM (Normal) Mk.3 | miner_mk3 | 6 (6.0000) | 6@250% | 250.0% |
| SAM (Pure) Mk.3 | miner_mk3 | 3 (3.0000) | 3@250% | 250.0% |
| Sulfur (Impure) Mk.3 | miner_mk3 | 6 (6.0000) | 6@250% | 250.0% |
| Sulfur (Normal) Mk.3 | miner_mk3 | 5 (5.0000) | 5@250% | 250.0% |
| Sulfur (Pure) Mk.3 | miner_mk3 | 5 (5.0000) | 5@250% | 250.0% |
| Uranium (Impure) Mk.3 | miner_mk3 | 3 (3.0000) | 3@250% | 250.0% |
| Uranium (Normal) Mk.3 | miner_mk3 | 2 (2.0000) | 2@250% | 250.0% |
| Crude Oil (Impure) | oil_extractor | 10 (10.0000) | 10@250% | 250.0% |
| Crude Oil (Normal) | oil_extractor | 12 (12.0000) | 12@250% | 250.0% |
| Crude Oil (Pure) | oil_extractor | 8 (8.0000) | 8@250% | 250.0% |
| Central Nitrogen Gas Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Crater Lakes Oil Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Northern Nitrogen Gas Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Northwestern Nitrogen Gas Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Southeastern Nitrogen Gas Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Southern Nitrogen Gas Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Southwestern Nitrogen Gas Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Spire Coast Oil Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Swamp Oil Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Water Extraction | water_extractor | 584 (583.7550) | 583@250% + 1@188.7% | 249.9% |

---

# Per item breakdown

For every item this plan produces, the recipes that make it — with the plan's whole-machine count, clock, sloop grade, and the share of the item's total that each recipe supplies.

## Water — 188,658.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Water Extraction | water_extractor | 584 | 249.9% | — | 175,126.5 | 92.8% |
| Alternate: Electrode Aluminum Scrap | refinery | 49 | 248.3% | — | 12,776.2 | 6.8% |
| Non-Fissile Uranium | blender | 21 | 240.0% | — | 756.0 | 0.4% |

## Iron Ore — 80,400.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Iron Ore (Pure) Mk.3 | miner_mk3 | 46 | 250.0% | — | 55,200.0 | 68.7% |
| Iron Ore (Normal) Mk.3 | miner_mk3 | 42 | 250.0% | — | 25,200.0 | 31.3% |

## Copper Ingot — 76,854.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Copper Alloy Ingot | foundry | 168 | 249.5% | — | 41,923.2 | 54.5% |
| Alternate: Pure Copper Ingot | refinery | 373 | 249.7% | — | 34,931.3 | 45.5% |

## Iron Ingot — 72,212.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Iron Ingot | refinery | 445 | 249.7% | — | 72,212.0 | 100.0% |

## Coal — 54,331.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Coal (Pure) Mk.3 | miner_mk3 | 16 | 250.0% | — | 19,200.0 | 35.3% |
| Coal (Normal) Mk.3 | miner_mk3 | 31 | 250.0% | — | 18,600.0 | 34.2% |
| Coal (Iron) | converter | 81 | 123.8% | — | 12,031.0 | 22.1% |
| Coal (Impure) Mk.3 | miner_mk3 | 15 | 250.0% | — | 4,500.0 | 8.3% |

## Quickwire — 45,486.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Fused Quickwire | assembler | 203 | 249.0% | — | 45,486.0 | 100.0% |

## Limestone — 38,535.2/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Limestone (Pure) Mk.3 | miner_mk3 | 29 | 250.0% | — | 34,800.0 | 90.3% |
| Limestone (Normal) Mk.3 | miner_mk3 | 7 | 222.3% | — | 3,735.2 | 9.7% |

## Copper Ore — 36,900.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Copper Ore (Normal) Mk.3 | miner_mk3 | 29 | 250.0% | — | 17,400.0 | 47.2% |
| Copper Ore (Pure) Mk.3 | miner_mk3 | 13 | 250.0% | — | 15,600.0 | 42.3% |
| Copper Ore (Impure) Mk.3 | miner_mk3 | 13 | 250.0% | — | 3,900.0 | 10.6% |

## Aluminum Scrap — 36,503.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Electrode Aluminum Scrap | refinery | 49 | 248.3% | — | 36,503.4 | 100.0% |

## Wire — 32,063.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Iron Wire | constructor | 327 | 249.7% | — | 18,373.6 | 57.3% |
| Alternate: Fused Wire | assembler | 61 | 249.4% | — | 13,690.3 | 42.7% |

## Fuel — 21,914.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Diluted Fuel | blender | 88 | 249.0% | — | 21,914.0 | 100.0% |

## Alumina Solution — 21,902.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Sloppy Alumina | refinery | 37 | 246.6% | — | 21,902.0 | 100.0% |

## Silica — 20,796.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Cheap Silica | assembler | 159 | 249.1% | — | 20,796.0 | 100.0% |

## Rubber — 20,155.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Recycled Rubber | refinery | 107 | 248.5% | — | 15,955.0 | 79.2% |
| Residual Rubber | refinery | 84 | 250.0% | — | 4,200.0 | 20.8% |

## Bauxite — 18,251.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Bauxite (Pure) Mk.3 | miner_mk3 | 6 | 250.0% | — | 7,200.0 | 39.4% |
| Bauxite (Caterium) | converter | 31 | 124.8% | — | 4,641.1 | 25.4% |
| Bauxite (Normal) Mk.3 | miner_mk3 | 6 | 250.0% | — | 3,600.0 | 19.7% |
| Bauxite (Impure) Mk.3 | miner_mk3 | 5 | 250.0% | — | 1,500.0 | 8.2% |
| Bauxite (Copper) | converter | 9 | 121.4% | — | 1,310.6 | 7.2% |

## Aluminum Ingot — 18,251.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Aluminum Ingot | smelter | 244 | 249.3% | — | 18,251.7 | 100.0% |

## Heavy Oil Residue — 16,800.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heavy Oil Residue | refinery | 168 | 250.0% | — | 16,800.0 | 100.0% |

## Concrete — 15,787.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Wet Concrete | refinery | 79 | 249.8% | — | 15,787.3 | 100.0% |

## Screws — 15,726.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Steel Screws | constructor | 25 | 241.9% | — | 15,726.4 | 100.0% |

## Copper Sheet — 15,548.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Steamed Copper Sheet | refinery | 277 | 249.5% | — | 15,548.3 | 100.0% |

## Caterium Ore — 15,000.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Caterium Ore (Pure) Mk.3 | miner_mk3 | 8 | 250.0% | — | 9,600.0 | 64.0% |
| Caterium Ore (Normal) Mk.3 | miner_mk3 | 9 | 250.0% | — | 5,400.0 | 36.0% |

## Steel Pipe — 14,771.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Iron Pipe | constructor | 237 | 249.3% | — | 14,771.5 | 100.0% |

## Plastic — 14,167.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Recycled Plastic | refinery | 95 | 248.6% | — | 14,167.8 | 100.0% |

## Raw Quartz — 13,500.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Quartz (Pure) Mk.3 | miner_mk3 | 7 | 250.0% | — | 8,400.0 | 62.2% |
| Quartz (Normal) Mk.3 | miner_mk3 | 7 | 250.0% | — | 4,200.0 | 31.1% |
| Quartz (Impure) Mk.3 | miner_mk3 | 3 | 250.0% | — | 900.0 | 6.7% |

## Nitrogen Gas — 13,017.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Central Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 3,000.0 | 23.0% |
| Southwestern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 2,100.0 | 16.1% |
| Northwestern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 1,950.0 | 15.0% |
| Northern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 1,800.0 | 13.8% |
| Southeastern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 1,650.0 | 12.7% |
| Southern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 1,500.0 | 11.5% |
| Nitrogen Gas (Caterium) | converter | 7 | 121.1% | — | 1,017.3 | 7.8% |

## Crude Oil — 12,600.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Crude Oil (Pure) | oil_extractor | 8 | 250.0% | — | 4,800.0 | 38.1% |
| Crude Oil (Normal) | oil_extractor | 12 | 250.0% | — | 3,600.0 | 28.6% |
| Crude Oil (Impure) | oil_extractor | 10 | 250.0% | — | 1,500.0 | 11.9% |
| Crater Lakes Oil Well | resource_well_pressurizer | 1 | 250.0% | — | 1,350.0 | 10.7% |
| Spire Coast Oil Well | resource_well_pressurizer | 1 | 250.0% | — | 900.0 | 7.1% |
| Swamp Oil Well | resource_well_pressurizer | 1 | 250.0% | — | 450.0 | 3.6% |

## Petroleum Coke — 11,353.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Petroleum Coke | refinery | 38 | 249.0% | — | 11,353.1 | 100.0% |

## Sulfur — 10,800.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Sulfur (Pure) Mk.3 | miner_mk3 | 5 | 250.0% | — | 6,000.0 | 55.6% |
| Sulfur (Normal) Mk.3 | miner_mk3 | 5 | 250.0% | — | 3,000.0 | 27.8% |
| Sulfur (Impure) Mk.3 | miner_mk3 | 6 | 250.0% | — | 1,800.0 | 16.7% |

## Dark Matter Residue — 10,750.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Superposition Oscillator | quantum_encoder | 87 | 49.8% | — | 5,416.7 | 50.4% |
| Neural-Quantum Processor | quantum_encoder | 65 | 49.6% | — | 2,416.7 | 22.5% |
| AI Expansion Server | quantum_encoder | 4 | 250.0% | 2 | 1,500.0 | 14.0% |
| AI Expansion Server | quantum_encoder | 29 | 48.9% | — | 1,416.7 | 13.2% |

## Excited Photonic Matter — 10,250.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Excited Photonic Matter | converter | 41 | 125.0% | — | 10,250.0 | 100.0% |

## SAM — 10,200.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| SAM (Normal) Mk.3 | miner_mk3 | 6 | 250.0% | — | 3,600.0 | 35.3% |
| SAM (Pure) Mk.3 | miner_mk3 | 3 | 250.0% | — | 3,600.0 | 35.3% |
| SAM (Impure) Mk.3 | miner_mk3 | 10 | 250.0% | — | 3,000.0 | 29.4% |

## Polymer Resin — 8,400.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heavy Oil Residue | refinery | 168 | 250.0% | — | 8,400.0 | 100.0% |

## Rocket Fuel — 6,292.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Nitro Rocket Fuel | blender | 14 | 237.8% | — | 4,993.1 | 79.4% |
| Rocket Fuel | blender | 6 | 216.5% | — | 1,299.2 | 20.6% |

## Copper Powder — 6,000.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Copper Powder | constructor | 48 | 250.0% | — | 6,000.0 | 100.0% |

## Iron Plate — 5,836.9/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Coated Iron Plate | assembler | 32 | 243.2% | — | 5,836.9 | 100.0% |

## Diamonds — 5,266.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Turbo Diamonds | accelerator | 71 | 123.6% | — | 5,266.7 | 100.0% |

## Circuit Board — 5,211.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Silicon Circuit Board | assembler | 167 | 249.6% | — | 5,211.3 | 100.0% |

## Alclad Aluminum Sheet — 4,925.9/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alclad Aluminum Sheet | assembler | 66 | 248.8% | — | 4,925.9 | 100.0% |

## Aluminum Casing — 4,329.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Alclad Casing | assembler | 16 | 240.5% | — | 4,329.5 | 100.0% |

## Dark Matter Crystal — 4,300.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Dark Matter Trap | accelerator | 144 | 49.8% | — | 4,300.0 | 100.0% |

## Turbofuel — 4,290.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Turbo Blend Fuel | blender | 28 | 245.1% | — | 3,088.0 | 72.0% |
| Turbofuel | refinery | 26 | 246.7% | — | 1,202.6 | 28.0% |

## Caterium Ingot — 4,246.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Caterium Ingot | refinery | 121 | 249.5% | — | 3,622.2 | 85.3% |
| Alternate: Leached Caterium Ingot | refinery | 7 | 247.9% | — | 624.6 | 14.7% |

## Quartz Crystal — 3,568.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Quartz Crystal | refinery | 28 | 242.7% | — | 3,568.0 | 100.0% |

## Empty Canister — 3,511.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Empty Canister | constructor | 24 | 243.8% | — | 3,511.1 | 100.0% |

## Packaged Turbofuel — 3,511.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Packaged Turbofuel | packager | 71 | 247.3% | — | 3,511.1 | 100.0% |

## Steel Ingot — 3,344.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Coke Steel Ingot | foundry | 14 | 238.9% | — | 3,344.6 | 100.0% |

## Time Crystal — 2,633.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Time Crystal | converter | 352 | 124.7% | — | 2,633.3 | 100.0% |

## Reanimated SAM — 2,550.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Reanimated SAM | constructor | 34 | 250.0% | — | 2,550.0 | 100.0% |

## Non-Fissile Uranium — 2,520.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Non-Fissile Uranium | blender | 21 | 240.0% | — | 2,520.0 | 100.0% |

## Uranium Waste — 2,520.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Nuclear Power (Uranium) | nuclear_power_plant | 101 | 249.5% | — | 2,520.0 | 100.0% |

## Uranium — 2,100.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Uranium (Normal) Mk.3 | miner_mk3 | 2 | 250.0% | — | 1,200.0 | 57.1% |
| Uranium (Impure) Mk.3 | miner_mk3 | 3 | 250.0% | — | 900.0 | 42.9% |

## Nitric Acid — 1,727.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Nitric Acid | blender | 24 | 239.9% | — | 1,727.0 | 100.0% |

## Battery — 1,700.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Classic Battery | manufacturer | 23 | 246.4% | — | 1,700.5 | 100.0% |

## Encased Uranium Cell — 1,680.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Infused Uranium Cell | manufacturer | 34 | 247.1% | — | 1,680.0 | 100.0% |

## Ficsite Trigon — 1,450.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Ficsite Trigon | constructor | 20 | 241.7% | — | 1,450.0 | 100.0% |

## Stator — 1,356.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Stator | assembler | 109 | 248.9% | — | 1,356.3 | 100.0% |

## Sulfuric Acid — 1,276.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Sulfuric Acid | refinery | 11 | 232.1% | — | 1,276.5 | 100.0% |

## Steel Beam — 1,254.2/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Molded Beam | foundry | 12 | 232.3% | — | 1,254.2 | 100.0% |

## Computer — 983.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Caterium Computer | manufacturer | 105 | 249.7% | — | 983.1 | 100.0% |

## Compacted Coal — 962.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Nitro Rocket Fuel | blender | 14 | 237.8% | — | 832.2 | 86.5% |
| Rocket Fuel | blender | 6 | 216.5% | — | 129.9 | 13.5% |

## Rotor — 907.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Copper Rotor | assembler | 33 | 244.4% | — | 907.3 | 100.0% |

## Encased Industrial Beam — 839.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Encased Industrial Pipe | assembler | 84 | 249.9% | — | 839.7 | 100.0% |

## Electromagnetic Control Rod — 819.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Electromagnetic Connection Rod | assembler | 37 | 244.2% | — | 722.9 | 88.2% |
| Electromagnetic Control Rod | assembler | 10 | 242.4% | — | 97.0 | 11.8% |

## Modular Frame — 792.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Steeled Frame | assembler | 106 | 249.2% | — | 792.6 | 100.0% |

## Plutonium Pellet — 756.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Plutonium Pellet | accelerator | 34 | 74.1% | — | 756.0 | 100.0% |

## Automated Wiring — 733.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Automated Speed Wiring | manufacturer | 40 | 244.6% | — | 733.8 | 100.0% |

## Reinforced Iron Plate — 678.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Stitched Iron Plate | assembler | 49 | 246.1% | — | 678.4 | 100.0% |

## High-Speed Connector — 544.9/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Silicon High-Speed Connector | manufacturer | 73 | 248.8% | — | 544.9 | 100.0% |

## Motor — 519.9/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Electric Motor | assembler | 28 | 247.6% | — | 519.9 | 100.0% |

## Heat Sink — 486.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heat Exchanger | assembler | 20 | 243.0% | — | 486.0 | 100.0% |

## Ficsite Ingot — 483.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Ficsite Ingot (Aluminum) | converter | 13 | 123.9% | — | 483.3 | 100.0% |

## AI Limiter — 453.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| AI Limiter | assembler | 37 | 245.3% | — | 453.8 | 100.0% |

## Encased Plutonium Cell — 378.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Encased Plutonium Cell | assembler | 31 | 243.9% | — | 378.0 | 100.0% |

## Empty Fluid Tank — 363.2/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Empty Fluid Tank | constructor | 3 | 201.8% | — | 363.2 | 100.0% |

## Packaged Nitrogen Gas — 363.2/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Packaged Nitrogen Gas | packager | 3 | 201.8% | — | 363.2 | 100.0% |

## Crystal Oscillator — 356.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Insulated Crystal Oscillator | manufacturer | 77 | 247.1% | — | 356.8 | 100.0% |

## Singularity Cell — 300.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Singularity Cell | manufacturer | 12 | 250.0% | — | 300.0 | 100.0% |

## Smart Plating — 300.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Plastic Smart Plating | manufacturer | 24 | 250.0% | — | 300.0 | 100.0% |

## Heavy Modular Frame — 251.9/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heavy Encased Frame | manufacturer | 36 | 248.8% | — | 251.9 | 100.0% |

## Versatile Framework — 241.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Flexible Framework | manufacturer | 13 | 247.9% | — | 241.7 | 100.0% |

## Superposition Oscillator — 216.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Superposition Oscillator | quantum_encoder | 87 | 49.8% | — | 216.7 | 100.0% |

## Cooling System — 180.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Cooling Device | blender | 15 | 240.0% | — | 180.0 | 100.0% |

## Radio Control Unit — 179.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Radio Control Unit | manufacturer | 29 | 247.5% | — | 179.5 | 100.0% |

## Supercomputer — 170.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Super-State Computer | manufacturer | 29 | 244.3% | — | 170.0 | 100.0% |

## Modular Engine — 150.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Modular Engine | manufacturer | 60 | 250.0% | — | 150.0 | 100.0% |

## Adaptive Control Unit — 146.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Adaptive Control Unit | manufacturer | 59 | 248.8% | — | 146.8 | 100.0% |

## Ballistic Warp Drive — 120.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Ballistic Warp Drive | manufacturer | 24 | 250.0% | 4 | 120.0 | 100.0% |

## AI Expansion Server — 116.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| AI Expansion Server | quantum_encoder | 4 | 250.0% | 2 | 60.0 | 51.4% |
| AI Expansion Server | quantum_encoder | 29 | 48.9% | — | 56.7 | 48.6% |

## Fused Modular Frame — 105.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heat-Fused Frame | blender | 15 | 233.6% | — | 105.1 | 100.0% |

## Neural-Quantum Processor — 96.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Neural-Quantum Processor | quantum_encoder | 65 | 49.6% | — | 96.7 | 100.0% |

## Magnetic Field Generator — 96.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Magnetic Field Generator | assembler | 39 | 247.9% | — | 96.7 | 100.0% |

## Assembly Director System — 73.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Assembly Director System | assembler | 40 | 244.6% | — | 73.4 | 100.0% |

## Thermal Propulsion Rocket — 60.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Thermal Propulsion Rocket | manufacturer | 24 | 250.0% | — | 60.0 | 100.0% |

## Turbo Motor — 60.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Turbo Pressure Motor | manufacturer | 4 | 201.8% | — | 30.3 | 50.4% |
| Alternate: Turbo Electric Motor | manufacturer | 5 | 211.4% | — | 29.7 | 49.6% |

## Uranium Fuel Rod — 50.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Uranium Fuel Unit | manufacturer | 34 | 247.1% | — | 50.4 | 100.0% |

## Pressure Conversion Cube — 45.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Pressure Conversion Cube | assembler | 19 | 237.5% | — | 45.1 | 100.0% |

## Nuclear Pasta — 30.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Nuclear Pasta | accelerator | 120 | 50.0% | — | 30.0 | 100.0% |

## Plutonium Fuel Rod — 12.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Plutonium Fuel Rod | manufacturer | 21 | 240.0% | — | 12.6 | 100.0% |

---

# Per-machine breakdown

One section per machine type in the plan: the recipes it runs, the whole-machine count, clock and sloop grade, and aggregate inputs/outputs per minute.

## Refinery — 1,945 machines · 195,115 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Pure Iron Ingot | 445 | 249.7% | — | Iron Ore 38,883.4 + Water 22,219.1 | Iron Ingot 72,212.0 |
| Alternate: Pure Copper Ingot | 373 | 249.7% | — | Copper Ore 13,972.5 + Water 9,315.0 | Copper Ingot 34,931.3 |
| Alternate: Steamed Copper Sheet | 277 | 249.5% | — | Copper Ingot 15,548.3 + Water 15,548.3 | Copper Sheet 15,548.3 |
| Alternate: Heavy Oil Residue | 168 | 250.0% | — | Crude Oil 12,600.0 | Heavy Oil Residue 16,800.0 + Polymer Resin 8,400.0 |
| Alternate: Pure Caterium Ingot | 121 | 249.5% | — | Caterium Ore 7,244.4 + Water 7,244.4 | Caterium Ingot 3,622.2 |
| Alternate: Recycled Rubber | 107 | 248.5% | — | Fuel 7,977.5 + Plastic 7,977.5 | Rubber 15,955.0 |
| Alternate: Recycled Plastic | 95 | 248.6% | — | Fuel 7,083.9 + Rubber 7,083.9 | Plastic 14,167.8 |
| Residual Rubber | 84 | 250.0% | — | Polymer Resin 8,400.0 + Water 8,400.0 | Rubber 4,200.0 |
| Alternate: Wet Concrete | 79 | 249.8% | — | Limestone 23,681.0 + Water 19,734.1 | Concrete 15,787.3 |
| Alternate: Electrode Aluminum Scrap | 49 | 248.3% | — | Alumina Solution 21,902.0 + Petroleum Coke 7,300.7 | Aluminum Scrap 36,503.4 + Water 12,776.2 |
| Petroleum Coke | 38 | 249.0% | — | Heavy Oil Residue 3,784.4 | Petroleum Coke 11,353.1 |
| Alternate: Sloppy Alumina | 37 | 246.6% | — | Bauxite 18,251.7 + Water 18,251.7 | Alumina Solution 21,902.0 |
| Alternate: Pure Quartz Crystal | 28 | 242.7% | — | Raw Quartz 4,587.4 + Water 2,548.6 | Quartz Crystal 3,568.0 |
| Turbofuel | 26 | 246.7% | — | Compacted Coal 962.1 + Fuel 1,443.2 | Turbofuel 1,202.6 |
| Sulfuric Acid | 11 | 232.1% | — | Sulfur 1,276.5 + Water 1,276.5 | Sulfuric Acid 1,276.5 |
| Alternate: Leached Caterium Ingot | 7 | 247.9% | — | Caterium Ore 936.9 + Sulfuric Acid 520.5 | Caterium Ingot 624.6 |

## Assembler — 1,346 machines · 67,028 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Fused Quickwire | 203 | 249.0% | — | Caterium Ingot 3,790.5 + Copper Ingot 18,952.5 | Quickwire 45,486.0 |
| Alternate: Silicon Circuit Board | 167 | 249.6% | — | Copper Sheet 11,464.9 + Silica 11,464.9 | Circuit Board 5,211.3 |
| Alternate: Cheap Silica | 159 | 249.1% | — | Limestone 14,854.3 + Raw Quartz 8,912.6 | Silica 20,796.0 |
| Stator | 109 | 248.9% | — | Steel Pipe 4,068.9 + Wire 10,850.3 | Stator 1,356.3 |
| Alternate: Steeled Frame | 106 | 249.2% | — | Reinforced Iron Plate 528.4 + Steel Pipe 2,641.9 | Modular Frame 792.6 |
| Alternate: Encased Industrial Pipe | 84 | 249.9% | — | Concrete 4,198.3 + Steel Pipe 5,038.0 | Encased Industrial Beam 839.7 |
| Alclad Aluminum Sheet | 66 | 248.8% | — | Aluminum Ingot 4,925.9 + Copper Ingot 1,642.0 | Alclad Aluminum Sheet 4,925.9 |
| Alternate: Fused Wire | 61 | 249.4% | — | Caterium Ingot 456.3 + Copper Ingot 1,825.4 | Wire 13,690.3 |
| Alternate: Stitched Iron Plate | 49 | 246.1% | — | Iron Plate 2,261.3 + Wire 4,522.5 | Reinforced Iron Plate 678.4 |
| Assembly Director System | 40 | 244.6% | — | Adaptive Control Unit 146.8 + Supercomputer 73.4 | Assembly Director System 73.4 |
| Magnetic Field Generator | 39 | 247.9% | — | Electromagnetic Control Rod 96.7 + Versatile Framework 241.7 | Magnetic Field Generator 96.7 |
| AI Limiter | 37 | 245.3% | — | Copper Sheet 2,268.8 + Quickwire 9,075.3 | AI Limiter 453.8 |
| Alternate: Electromagnetic Connection Rod | 37 | 244.2% | — | High-Speed Connector 361.4 + Stator 722.9 | Electromagnetic Control Rod 722.9 |
| Alternate: Copper Rotor | 33 | 244.4% | — | Copper Sheet 1,814.6 + Screws 15,726.4 | Rotor 907.3 |
| Alternate: Coated Iron Plate | 32 | 243.2% | — | Iron Ingot 2,918.5 + Plastic 583.7 | Iron Plate 5,836.9 |
| Encased Plutonium Cell | 31 | 243.9% | — | Concrete 1,512.0 + Plutonium Pellet 756.0 | Encased Plutonium Cell 378.0 |
| Alternate: Electric Motor | 28 | 247.6% | — | Electromagnetic Control Rod 260.0 + Rotor 519.9 | Motor 519.9 |
| Alternate: Heat Exchanger | 20 | 243.0% | — | Aluminum Casing 1,458.0 + Rubber 1,458.0 | Heat Sink 486.0 |
| Pressure Conversion Cube | 19 | 237.5% | — | Fused Modular Frame 45.1 + Radio Control Unit 90.3 | Pressure Conversion Cube 45.1 |
| Alternate: Alclad Casing | 16 | 240.5% | — | Aluminum Ingot 5,772.6 + Copper Ingot 2,886.3 | Aluminum Casing 4,329.5 |
| Electromagnetic Control Rod | 10 | 242.4% | — | AI Limiter 97.0 + Stator 145.4 | Electromagnetic Control Rod 97.0 |

## Manufacturer — 726 machines · 145,615 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Caterium Computer | 105 | 249.7% | — | Circuit Board 3,932.6 + Quickwire 13,764.1 + Rubber 5,898.9 | Computer 983.1 |
| Alternate: Insulated Crystal Oscillator | 77 | 247.1% | — | AI Limiter 356.8 + Quartz Crystal 3,568.0 + Rubber 2,497.6 | Crystal Oscillator 356.8 |
| Alternate: Silicon High-Speed Connector | 73 | 248.8% | — | Circuit Board 544.9 + Quickwire 16,346.7 + Silica 6,811.1 | High-Speed Connector 544.9 |
| Modular Engine | 60 | 250.0% | — | Motor 300.0 + Rubber 2,250.0 + Smart Plating 300.0 | Modular Engine 150.0 |
| Adaptive Control Unit | 59 | 248.8% | — | Automated Wiring 733.8 + Circuit Board 733.8 + Computer 293.5 + Heavy Modular Frame 146.8 | Adaptive Control Unit 146.8 |
| Alternate: Automated Speed Wiring | 40 | 244.6% | — | High-Speed Connector 183.5 + Stator 366.9 + Wire 7,338.3 | Automated Wiring 733.8 |
| Alternate: Heavy Encased Frame | 36 | 248.8% | — | Concrete 1,847.3 + Encased Industrial Beam 839.7 + Modular Frame 671.7 + Steel Pipe 3,022.8 | Heavy Modular Frame 251.9 |
| Alternate: Infused Uranium Cell | 34 | 247.1% | — | Quickwire 6,300.0 + Silica 1,260.0 + Sulfur 2,100.0 + Uranium 2,100.0 | Encased Uranium Cell 1,680.0 |
| Alternate: Uranium Fuel Unit | 34 | 247.1% | — | Crystal Oscillator 50.4 + Electromagnetic Control Rod 168.0 + Encased Uranium Cell 1,680.0 + Rotor 168.0 | Uranium Fuel Rod 50.4 |
| Radio Control Unit | 29 | 247.5% | — | Aluminum Casing 2,871.5 + Computer 179.5 + Crystal Oscillator 89.7 | Radio Control Unit 179.5 |
| Alternate: Super-State Computer | 29 | 244.3% | — | Battery 1,700.5 + Computer 510.1 + Electromagnetic Control Rod 170.0 + Wire 4,251.2 | Supercomputer 170.0 |
| Ballistic Warp Drive | 24 | 250.0% | 4 | Dark Matter Crystal 2,400.0 + Singularity Cell 300.0 + Superposition Oscillator 120.0 + Thermal Propulsion Rocket 60.0 | Ballistic Warp Drive 120.0 |
| Alternate: Plastic Smart Plating | 24 | 250.0% | — | Plastic 450.0 + Reinforced Iron Plate 150.0 + Rotor 150.0 | Smart Plating 300.0 |
| Thermal Propulsion Rocket | 24 | 250.0% | — | Cooling System 180.0 + Fused Modular Frame 60.0 + Modular Engine 150.0 + Turbo Motor 60.0 | Thermal Propulsion Rocket 60.0 |
| Alternate: Classic Battery | 23 | 246.4% | — | Alclad Aluminum Sheet 2,975.9 + Plastic 3,401.0 + Sulfur 2,550.7 + Wire 5,101.5 | Battery 1,700.5 |
| Plutonium Fuel Rod | 21 | 240.0% | — | Electromagnetic Control Rod 75.6 + Encased Plutonium Cell 378.0 + Heat Sink 126.0 + Steel Beam 226.8 | Plutonium Fuel Rod 12.6 |
| Alternate: Flexible Framework | 13 | 247.9% | — | Modular Frame 120.8 + Rubber 966.7 + Steel Beam 725.0 | Versatile Framework 241.7 |
| Singularity Cell | 12 | 250.0% | — | Concrete 6,000.0 + Dark Matter Crystal 600.0 + Iron Plate 3,000.0 + Nuclear Pasta 30.0 | Singularity Cell 300.0 |
| Alternate: Turbo Electric Motor | 5 | 211.4% | — | Electromagnetic Control Rod 49.6 + Motor 69.4 + Radio Control Unit 89.2 + Rotor 69.4 | Turbo Motor 29.7 |
| Alternate: Turbo Pressure Motor | 4 | 201.8% | — | Motor 60.5 + Packaged Nitrogen Gas 363.2 + Pressure Conversion Cube 15.1 + Stator 121.1 | Turbo Motor 30.3 |

## Constructor — 718 machines · 9,579 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Iron Wire | 327 | 249.7% | — | Iron Ingot 10,207.5 | Wire 18,373.6 |
| Alternate: Iron Pipe | 237 | 249.3% | — | Iron Ingot 59,086.0 | Steel Pipe 14,771.5 |
| Copper Powder | 48 | 250.0% | — | Copper Ingot 36,000.0 | Copper Powder 6,000.0 |
| Reanimated SAM | 34 | 250.0% | — | SAM 10,200.0 | Reanimated SAM 2,550.0 |
| Alternate: Steel Screws | 25 | 241.9% | — | Steel Beam 302.4 | Screws 15,726.4 |
| Empty Canister | 24 | 243.8% | — | Plastic 1,755.6 | Empty Canister 3,511.1 |
| Ficsite Trigon | 20 | 241.7% | — | Ficsite Ingot 483.3 | Ficsite Trigon 1,450.0 |
| Empty Fluid Tank | 3 | 201.8% | — | Aluminum Ingot 363.2 | Empty Fluid Tank 363.2 |

## Converter — 534 machines · 178,270 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Time Crystal | 352 | 124.7% | — | Diamonds 5,266.7 | Time Crystal 2,633.3 |
| Coal (Iron) | 81 | 123.8% | — | Iron Ore 18,046.6 + Reanimated SAM 1,002.6 | Coal 12,031.0 |
| Excited Photonic Matter | 41 | 125.0% | — | — | Excited Photonic Matter 10,250.0 |
| Bauxite (Caterium) | 31 | 124.8% | — | Caterium Ore 5,801.4 + Reanimated SAM 386.8 | Bauxite 4,641.1 |
| Ficsite Ingot (Aluminum) | 13 | 123.9% | — | Aluminum Ingot 1,933.3 + Reanimated SAM 966.7 | Ficsite Ingot 483.3 |
| Bauxite (Copper) | 9 | 121.4% | — | Copper Ore 1,965.9 + Reanimated SAM 109.2 | Bauxite 1,310.6 |
| Nitrogen Gas (Caterium) | 7 | 121.1% | — | Caterium Ore 1,017.3 + Reanimated SAM 84.8 | Nitrogen Gas 1,017.3 |

## Accelerator — 369 machines · 140,185 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Dark Matter Trap | 144 | 49.8% | — | Dark Matter Residue 10,750.0 + Time Crystal 2,150.0 | Dark Matter Crystal 4,300.0 |
| Nuclear Pasta | 120 | 50.0% | — | Copper Powder 6,000.0 + Pressure Conversion Cube 30.0 | Nuclear Pasta 30.0 |
| Alternate: Turbo Diamonds | 71 | 123.6% | — | Coal 52,666.7 + Packaged Turbofuel 3,511.1 | Diamonds 5,266.7 |
| Plutonium Pellet | 34 | 74.1% | — | Non-Fissile Uranium 2,520.0 + Uranium Waste 630.0 | Plutonium Pellet 756.0 |

## Smelter — 244 machines · 3,266 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Pure Aluminum Ingot | 244 | 249.3% | — | Aluminum Scrap 36,503.4 | Aluminum Ingot 18,251.7 |

## Blender — 211 machines · 51,229 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Diluted Fuel | 88 | 249.0% | — | Heavy Oil Residue 10,957.0 + Water 21,914.0 | Fuel 21,914.0 |
| Alternate: Turbo Blend Fuel | 28 | 245.1% | — | Fuel 1,029.3 + Heavy Oil Residue 2,058.6 + Petroleum Coke 1,544.0 + Sulfur 1,544.0 | Turbofuel 3,088.0 |
| Nitric Acid | 24 | 239.9% | — | Iron Plate 575.7 + Nitrogen Gas 6,907.9 + Water 1,727.0 | Nitric Acid 1,727.0 |
| Non-Fissile Uranium | 21 | 240.0% | — | Nitric Acid 756.0 + Silica 1,260.0 + Sulfuric Acid 756.0 + Uranium Waste 1,890.0 | Non-Fissile Uranium 2,520.0 + Water 756.0 |
| Alternate: Cooling Device | 15 | 240.0% | — | Heat Sink 360.0 + Motor 90.0 + Nitrogen Gas 2,160.0 | Cooling System 180.0 |
| Alternate: Heat-Fused Frame | 15 | 233.6% | — | Aluminum Ingot 5,256.7 + Fuel 1,051.3 + Heavy Modular Frame 105.1 + Nitric Acid 841.1 | Fused Modular Frame 105.1 |
| Alternate: Nitro Rocket Fuel | 14 | 237.8% | — | Coal 1,664.4 + Fuel 3,328.8 + Nitrogen Gas 2,496.6 + Sulfur 3,328.8 | Compacted Coal 832.2 + Rocket Fuel 4,993.1 |
| Rocket Fuel | 6 | 216.5% | — | Nitric Acid 129.9 + Turbofuel 779.5 | Compacted Coal 129.9 + Rocket Fuel 1,299.2 |

## Foundry — 194 machines · 10,297 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Copper Alloy Ingot | 168 | 249.5% | — | Copper Ore 20,961.6 + Iron Ore 20,961.6 | Copper Ingot 41,923.2 |
| Alternate: Coke Steel Ingot | 14 | 238.9% | — | Iron Ore 2,508.5 + Petroleum Coke 2,508.5 | Steel Ingot 3,344.6 |
| Alternate: Molded Beam | 12 | 232.3% | — | Concrete 2,229.7 + Steel Ingot 3,344.6 | Steel Beam 1,254.2 |

## Quantum Encoder — 185 machines · 101,799 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Superposition Oscillator | 87 | 49.8% | — | Alclad Aluminum Sheet 1,950.0 + Crystal Oscillator 216.7 + Dark Matter Crystal 1,300.0 + Excited Photonic Matter 5,416.7 | Dark Matter Residue 5,416.7 + Superposition Oscillator 216.7 |
| Neural-Quantum Processor | 65 | 49.6% | — | Excited Photonic Matter 2,416.7 + Ficsite Trigon 1,450.0 + Supercomputer 96.7 + Time Crystal 483.3 | Dark Matter Residue 2,416.7 + Neural-Quantum Processor 96.7 |
| AI Expansion Server | 29 | 48.9% | — | Excited Photonic Matter 1,416.7 + Magnetic Field Generator 56.7 + Neural-Quantum Processor 56.7 + Superposition Oscillator 56.7 | AI Expansion Server 56.7 + Dark Matter Residue 1,416.7 |
| AI Expansion Server | 4 | 250.0% | 2 | Excited Photonic Matter 1,000.0 + Magnetic Field Generator 40.0 + Neural-Quantum Processor 40.0 + Superposition Oscillator 40.0 | AI Expansion Server 60.0 + Dark Matter Residue 1,500.0 |

## Packager — 74 machines · 2,425 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Packaged Turbofuel | 71 | 247.3% | — | Empty Canister 3,511.1 + Turbofuel 3,511.1 | Packaged Turbofuel 3,511.1 |
| Packaged Nitrogen Gas | 3 | 201.8% | — | Empty Fluid Tank 363.2 + Nitrogen Gas 1,452.8 | Packaged Nitrogen Gas 363.2 |

---

# Resource extraction

Raw-material supply: miners, water/oil extractors and pressure wells. (The high-level overview aggregates these by resource; here each node group is listed.)

## Water Extractor — 584 machines · 39,197 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Water Extraction | 584 | 249.9% | — | — | Water 175,126.5 |

## Miner Mk.3 — 332 machines · 50,013 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Iron Ore (Pure) Mk.3 | 46 | 250.0% | — | — | Iron Ore 55,200.0 |
| Iron Ore (Normal) Mk.3 | 42 | 250.0% | — | — | Iron Ore 25,200.0 |
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
| Limestone (Normal) Mk.3 | 7 | 222.3% | — | — | Limestone 3,735.2 |
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

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Crude Oil (Normal) | 12 | 250.0% | — | — | Crude Oil 3,600.0 |
| Crude Oil (Impure) | 10 | 250.0% | — | — | Crude Oil 1,500.0 |
| Crude Oil (Pure) | 8 | 250.0% | — | — | Crude Oil 4,800.0 |

## Resource Well Pressurizer — 9 machines · 4,533 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
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

| Recipe | count | clock | slps | fuel /min | output |
|---|---|---:|---:|---|---|
| Geothermal Power (Pure) | 9 | 100.0% | — | — | 3,600 MW |
| Geothermal Power (Normal) | 13 | 100.0% | — | — | 2,600 MW |
| Geothermal Power (Impure) | 9 | 100.0% | — | — | 900 MW |

## Nuclear Power Plant — 101 machines · **630,000 MW generated**

| Recipe | count | clock | slps | fuel /min | output |
|---|---|---:|---:|---|---|
| Nuclear Power (Uranium) | 101 | 249.5% | — | Uranium Fuel Rod 50.4 + Water 60,480.0 | 630,000 MW |

## Fuel Generator — 605 machines · **377,537 MW generated**

| Recipe | count | clock | slps | fuel /min | output |
|---|---|---:|---:|---|---|
| Rocket Fuel Power | 605 | 249.6% | — | Rocket Fuel 6,292.3 | 377,537 MW |

---

## Notes

- **Power rounding**: per-section draws are computed from the displayed whole-machine counts and sum to 1,002,580 MW, ~0.1% under the official 1,004,591 MW (the model also runs tiny sub-machine exact-balance slivers). Generation is clock-linear, so whole-machine sums reproduce the 1,014,637 MW exactly.
- Accelerator rows use per-recipe power draw where the spec overrides it; other machines use their machine default.
- Rates are **aggregate** at the displayed clock. Per-machine rate at that clock = aggregate ÷ `#`.
