# Satisfactory Factory Optimiser — Build Plan

**Official optimum** — **479,272,805 pts/min** (overclock tiers 25%, 50%, 75%, 100%, 125%, 150%, 175%, 200%, 225%, 250%; Auto-solved (augmenter sweep)). All rates are per minute.

## High-level overview

| Metric | Value | Notes |
|---|---|---|
| **Sink points** | **479,272,805 pts/min** | 0 augmenter(s), 1.00x power |
| **Power load** | **1,020,846 MW** | what consumers actually draw |
| **Power supplied** | 1,031,055 MW | load x1.01 (1% reserve) |
| **Machines** | **16,425** (cap 16,384 — binding) | 140 recipe rows across 18 machine types |
| **Somersloops** | 104 / 104 | see overclock notes |
| **Sink throughput** | 369.6 items/min | one Awesome Sink covers it (1200/min cap, 30 MW) |

### Sink flows

| Sink item | pts/item | /min | pts/min | share |
|---|---:|---:|---:|---:|
| Ballistic Warp Drive | 2,895,334 | 120.0 | 347,440,080 | 72.5% |
| AI Expansion Server | 597,652 | 116.7 | 69,726,067 | 14.5% |
| Assembly Director System | 500,176 | 120.3 | 60,176,540 | 12.6% |
| Plutonium Fuel Rod | 153,184 | 12.6 | 1,930,118 | 0.4% |
| **TOTAL** | | | **479,272,805** | 100% |

### Map resources extracted

Miners are shown at their planned 250% clock; every tapped node group is maxed.

| Resource | extractors | /min |
|---|---:|---:|
| Water | 819 | 220,945 |
| Iron Ore | 127 | 92,100 |
| Limestone | 79 | 64,800 |
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
| Water | 235,985.1 | 235,985.1 | +0.0 | balanced |
| Iron Ingot | 159,467.8 | 159,467.8 | -0.0 | balanced |
| Wire | 93,510.0 | 93,510.0 | +0.0 | balanced |
| Iron Ore | 92,100.0 | 92,100.0 | +0.0 | balanced |
| Copper Ingot | 82,645.7 | 82,645.7 | +0.0 | balanced |
| Limestone | 64,800.0 | 64,800.0 | -0.0 | balanced |
| Coal | 53,277.7 | 53,277.7 | -0.0 | balanced |
| Quickwire | 49,041.1 | 49,041.1 | -0.0 | balanced |
| Aluminum Scrap | 40,064.5 | 40,064.5 | +0.0 | balanced |
| Copper Ore | 36,900.0 | 36,900.0 | +0.0 | balanced |
| Alumina Solution | 24,386.8 | 24,386.8 | +0.0 | balanced |
| Steel Pipe | 24,277.7 | 24,277.7 | +0.0 | balanced |
| Cable | 24,062.1 | 24,062.1 | -0.0 | balanced |
| Copper Sheet | 21,274.5 | 21,274.5 | -0.0 | balanced |
| Bauxite | 20,322.3 | 20,322.3 | -0.0 | balanced |
| Aluminum Ingot | 20,032.3 | 20,032.3 | +0.0 | balanced |
| Rubber | 18,563.4 | 18,563.4 | +0.0 | balanced |
| Fuel | 18,122.3 | 18,122.3 | -0.0 | balanced |
| Concrete | 17,795.1 | 17,795.1 | +0.0 | balanced |
| Heavy Oil Residue | 16,800.0 | 16,800.0 | +0.0 | balanced |
| Silica | 15,271.1 | 15,271.1 | -0.0 | balanced |
| Caterium Ore | 15,000.0 | 15,000.0 | +0.0 | balanced |
| Raw Quartz | 13,500.0 | 13,500.0 | +0.0 | balanced |
| Plastic | 12,907.7 | 12,907.7 | +0.0 | balanced |
| Crude Oil | 12,600.0 | 12,600.0 | +0.0 | balanced |
| Nitrogen Gas | 12,000.0 | 12,000.0 | +0.0 | balanced |
| Petroleum Coke | 11,053.6 | 11,053.6 | -0.0 | balanced |
| Sulfur | 10,800.0 | 10,800.0 | -0.0 | balanced |
| Dark Matter Residue | 10,750.0 | 10,750.0 | +0.0 | balanced |
| Excited Photonic Matter | 10,250.0 | 10,250.0 | -0.0 | balanced |
| SAM | 10,200.0 | 10,200.0 | +0.0 | balanced |
| Polymer Resin | 8,400.0 | 8,400.0 | -0.0 | balanced |
| Alclad Aluminum Sheet | 7,872.5 | 7,872.5 | +0.0 | balanced |
| Iron Plate | 6,938.0 | 6,938.0 | +0.0 | balanced |
| Rocket Fuel | 6,565.9 | 6,565.9 | +0.0 | balanced |
| Turbofuel | 6,081.4 | 6,081.4 | -0.0 | balanced |
| Copper Powder | 6,000.0 | 6,000.0 | +0.0 | balanced |
| Circuit Board | 5,796.0 | 5,796.0 | +0.0 | balanced |
| Quartz Crystal | 5,409.6 | 5,409.6 | -0.0 | balanced |
| Diamonds | 5,266.7 | 5,266.7 | +0.0 | balanced |
| Dark Matter Crystal | 4,300.0 | 4,300.0 | +0.0 | balanced |
| Caterium Ingot | 4,086.8 | 4,086.8 | +0.0 | balanced |
| Aluminum Casing | 3,469.8 | 3,469.8 | +0.0 | balanced |
| Empty Canister | 3,469.0 | 3,469.0 | +0.0 | balanced |
| Packaged Turbofuel | 3,469.0 | 3,469.0 | +0.0 | balanced |
| Steel Ingot | 3,216.2 | 3,216.2 | +0.0 | balanced |
| Time Crystal | 2,633.3 | 2,633.3 | -0.0 | balanced |
| Stator | 2,607.7 | 2,607.7 | +0.0 | balanced |
| Reanimated SAM | 2,550.0 | 2,550.0 | -0.0 | balanced |
| Non-Fissile Uranium | 2,520.0 | 2,520.0 | -0.0 | balanced |
| Uranium Waste | 2,520.0 | 2,520.0 | +0.0 | balanced |
| Battery | 2,169.8 | 2,169.8 | -0.0 | balanced |
| Uranium | 2,100.0 | 2,100.0 | -0.0 | balanced |
| Nitric Acid | 1,979.4 | 1,979.4 | +0.0 | balanced |
| Encased Uranium Cell | 1,680.0 | 1,680.0 | +0.0 | balanced |
| Steel Beam | 1,676.8 | 1,676.8 | +0.0 | balanced |
| Ficsite Trigon | 1,450.0 | 1,450.0 | +0.0 | balanced |
| AI Limiter | 1,413.1 | 1,413.1 | +0.0 | balanced |
| Computer | 1,338.2 | 1,338.2 | -0.0 | balanced |
| Automated Wiring | 1,203.1 | 1,203.1 | +0.0 | balanced |
| Sulfuric Acid | 1,191.1 | 1,191.1 | +0.0 | balanced |
| Encased Industrial Beam | 1,130.4 | 1,130.4 | +0.0 | balanced |
| Rotor | 1,092.6 | 1,092.6 | +0.0 | balanced |
| Modular Frame | 1,025.2 | 1,025.2 | +0.0 | balanced |
| Reinforced Iron Plate | 983.4 | 983.4 | +0.0 | balanced |
| Electromagnetic Control Rod | 891.1 | 891.1 | +0.0 | balanced |
| Compacted Coal | 804.0 | 804.0 | +0.0 | balanced |
| Plutonium Pellet | 756.0 | 756.0 | +0.0 | balanced |
| Motor | 524.3 | 524.3 | +0.0 | balanced |
| Crystal Oscillator | 522.0 | 522.0 | -0.0 | balanced |
| Heat Sink | 486.0 | 486.0 | +0.0 | balanced |
| Ficsite Ingot | 483.3 | 483.3 | -0.0 | balanced |
| Encased Plutonium Cell | 378.0 | 378.0 | +0.0 | balanced |
| Heavy Modular Frame | 339.1 | 339.1 | +0.0 | balanced |
| Smart Plating | 300.0 | 300.0 | +0.0 | balanced |
| Singularity Cell | 300.0 | 300.0 | -0.0 | balanced |
| Versatile Framework | 241.7 | 241.7 | +0.0 | balanced |
| Adaptive Control Unit | 240.6 | 240.6 | +0.0 | balanced |
| Supercomputer | 217.0 | 217.0 | +0.0 | balanced |
| Superposition Oscillator | 216.7 | 216.7 | +0.0 | balanced |
| Radio Control Unit | 206.0 | 206.0 | +0.0 | balanced |
| Empty Fluid Tank | 204.1 | 204.1 | +0.0 | balanced |
| Packaged Nitrogen Gas | 204.1 | 204.1 | +0.0 | balanced |
| Cooling System | 180.0 | 180.0 | -0.0 | balanced |
| Modular Engine | 150.0 | 150.0 | -0.0 | balanced |
| Assembly Director System | 120.3 | 0.0 | +120.3 | → Awesome Sink (120.3/min) |
| Ballistic Warp Drive | 120.0 | 0.0 | +120.0 | → Awesome Sink (120.0/min) |
| AI Expansion Server | 116.7 | 0.0 | +116.7 | → Awesome Sink (116.7/min) |
| Fused Modular Frame | 98.5 | 98.5 | -0.0 | balanced |
| Neural-Quantum Processor | 96.7 | 96.7 | +0.0 | balanced |
| Magnetic Field Generator | 96.7 | 96.7 | -0.0 | balanced |
| Thermal Propulsion Rocket | 60.0 | 60.0 | +0.0 | balanced |
| Turbo Motor | 60.0 | 60.0 | -0.0 | balanced |
| Uranium Fuel Rod | 50.4 | 50.4 | -0.0 | balanced |
| Pressure Conversion Cube | 38.5 | 38.5 | +0.0 | balanced |
| Nuclear Pasta | 30.0 | 30.0 | +0.0 | balanced |
| Plutonium Fuel Rod | 12.6 | 0.0 | +12.6 | → Awesome Sink (12.6/min) |

---

# All used recipes

100 production recipe rows from 97 distinct recipes (rows repeat a recipe when sloop grades or clocks differ); extractors are listed in the Resource extraction table underneath. `count` is the machines to build, with the raw fractional count in brackets; `clock` shows how to split that build into whole machines at the clock tier plus one trimmed remainder (e.g. `10@100% + 1@50%`); `equivalent all-machine clock` is the single uniform clock that reproduces the same throughput. A row whose equivalent clock sits below the tier is an exact-balance remnant, not a choice.

| Recipe | machine | count | clock | equivalent all-machine clock |
|---|---|---:|---:|---:|
| Alternate: Dark Matter Trap | accelerator | 287 (286.6667) | 286@25% + 1@16.7% | 25.0% |
| Alternate: Turbo Diamonds | accelerator | 174 (173.4506) | 173@50% + 1@22.5% | 49.8% |
| Nuclear Pasta | accelerator | 240 (240.0000) | 240@25% | 25.0% |
| Plutonium Pellet | accelerator | 101 (100.8000) | 100@25% + 1@20% | 25.0% |
| AI Limiter | assembler | 114 (113.0467) | 113@250% + 1@11.7% | 247.9% |
| Alclad Aluminum Sheet | assembler | 105 (104.9671) | 104@250% + 1@241.8% | 249.9% |
| Alternate: Alclad Casing | assembler | 13 (12.3371) | 12@250% + 1@84.3% | 237.3% |
| Alternate: Cheap Silica | assembler | 117 (116.3513) | 116@250% + 1@87.8% | 248.6% |
| Alternate: Crystal Computer | assembler | 37 (36.4702) | 36@250% + 1@117.5% | 246.4% |
| Alternate: Electric Motor | assembler | 28 (27.9643) | 27@250% + 1@241.1% | 249.7% |
| Alternate: Encased Industrial Pipe | assembler | 114 (113.0417) | 113@250% + 1@10.4% | 247.9% |
| Alternate: Fused Quickwire | assembler | 218 (217.9603) | 217@250% + 1@240.1% | 250.0% |
| Alternate: Silicon Circuit Board | assembler | 186 (185.4706) | 185@250% + 1@117.7% | 249.3% |
| Alternate: Steel Rotor | assembler | 88 (87.4118) | 87@250% + 1@103% | 248.3% |
| Alternate: Steeled Frame | assembler | 137 (136.6889) | 136@250% + 1@172.2% | 249.4% |
| Alternate: Stitched Iron Plate | assembler | 70 (69.9338) | 69@250% + 1@233.5% | 249.8% |
| Assembly Director System | assembler | 65 (64.1657) | 64@250% + 1@41.4% | 246.8% |
| Automated Wiring | assembler | 193 (192.4972) | 192@250% + 1@124.3% | 249.3% |
| Electromagnetic Control Rod | assembler | 90 (89.1065) | 89@250% + 1@26.6% | 247.5% |
| Encased Plutonium Cell | assembler | 31 (30.2400) | 30@250% + 1@60% | 243.9% |
| Heat Sink | assembler | 26 (25.9200) | 25@250% + 1@230% | 249.2% |
| Magnetic Field Generator | assembler | 39 (38.6667) | 38@250% + 1@166.7% | 247.9% |
| Pressure Conversion Cube | assembler | 16 (15.4014) | 15@250% + 1@100.3% | 240.6% |
| Smart Plating | assembler | 60 (60.0000) | 60@250% | 250.0% |
| Stator | assembler | 209 (208.6186) | 208@250% + 1@154.6% | 249.5% |
| Versatile Framework | assembler | 20 (19.3333) | 19@250% + 1@83.3% | 241.7% |
| Alternate: Cooling Device | blender | 36 (36.0000) | 36@100% | 100.0% |
| Alternate: Diluted Fuel | blender | 182 (181.2233) | 181@100% + 1@22.3% | 99.6% |
| Alternate: Heat-Fused Frame | blender | 33 (32.8345) | 32@100% + 1@83.4% | 99.5% |
| Alternate: Nitro Rocket Fuel | blender | 15 (14.7458) | 14@100% + 1@74.6% | 98.3% |
| Alternate: Turbo Blend Fuel | blender | 136 (135.1431) | 135@100% + 1@14.3% | 99.4% |
| Battery | blender | 9 (8.7020) | 8@100% + 1@70.2% | 96.7% |
| Nitric Acid | blender | 66 (65.9811) | 65@100% + 1@98.1% | 100.0% |
| Non-Fissile Uranium | blender | 51 (50.4000) | 50@100% + 1@40% | 98.8% |
| Rocket Fuel | blender | 44 (43.5405) | 43@100% + 1@54% | 99.0% |
| Alternate: Aluminum Beam | constructor | 9 (8.3685) | 8@250% + 1@92.1% | 232.5% |
| Alternate: Iron Pipe | constructor | 389 (388.4434) | 388@250% + 1@110.9% | 249.6% |
| Alternate: Iron Wire | constructor | 1,663 (1662.3995) | 1662@250% + 1@99.9% | 249.9% |
| Cable | constructor | 321 (320.8286) | 320@250% + 1@207.2% | 249.9% |
| Copper Powder | constructor | 48 (48.0000) | 48@250% | 250.0% |
| Empty Canister | constructor | 24 (23.1267) | 23@250% + 1@31.7% | 240.9% |
| Empty Fluid Tank | constructor | 2 (1.3606) | 1@250% + 1@90.1% | 170.1% |
| Ficsite Trigon | constructor | 20 (19.3333) | 19@250% + 1@83.3% | 241.7% |
| Iron Plate | constructor | 139 (138.7592) | 138@250% + 1@189.8% | 249.6% |
| Reanimated SAM | constructor | 34 (34.0000) | 34@250% | 250.0% |
| Alternate: Pink Diamonds | converter | 9 (8.4198) | 8@50% + 1@21% | 46.8% |
| Bauxite (Caterium) | converter | 92 (91.0198) | 91@50% + 1@1% | 49.5% |
| Bauxite (Copper) | converter | 86 (85.3716) | 85@25% + 1@9.3% | 24.8% |
| Coal (Iron) | converter | 64 (63.7068) | 63@25% + 1@17.7% | 24.9% |
| Coal (Limestone) | converter | 152 (151.1076) | 151@50% + 1@5.4% | 49.7% |
| Excited Photonic Matter | converter | 103 (102.5000) | 102@50% + 1@25% | 49.8% |
| Ficsite Ingot (Aluminum) | converter | 33 (32.2222) | 32@50% + 1@11.1% | 48.8% |
| Time Crystal | converter | 66 (65.7000) | 65@25% + 1@17.5% | 24.9% |
| Time Crystal | converter | 845 (844.9278) | 844@50% + 1@46.4% | 50.0% |
| Alternate: Compacted Steel Ingot | foundry | 129 (128.6479) | 128@250% + 1@162% | 249.3% |
| Alternate: Molded Beam | foundry | 11 (10.7207) | 10@250% + 1@180.2% | 243.7% |
| Rocket Fuel Power | fuel_generator | 631 (630.3279) | 630@250% + 1@82% | 249.7% |
| Geothermal Power (Impure) | geothermal_generator | 9 (9.0000) | 9@100% | 100.0% |
| Geothermal Power (Normal) | geothermal_generator | 13 (13.0000) | 13@100% | 100.0% |
| Geothermal Power (Pure) | geothermal_generator | 9 (9.0000) | 9@100% | 100.0% |
| Adaptive Control Unit | manufacturer | 241 (240.6215) | 240@100% + 1@62.1% | 99.8% |
| Alternate: Caterium Computer | manufacturer | 276 (275.7982) | 275@100% + 1@79.8% | 99.9% |
| Alternate: Classic Battery | manufacturer | 67 (66.5245) | 66@100% + 1@52.4% | 99.3% |
| Alternate: Heavy Encased Frame | manufacturer | 121 (120.5778) | 120@100% + 1@57.8% | 99.7% |
| Alternate: Infused Uranium Cell | manufacturer | 84 (84.0000) | 84@100% | 100.0% |
| Alternate: Insulated Crystal Oscillator | manufacturer | 279 (278.4100) | 278@100% + 1@41% | 99.8% |
| Alternate: Super-State Computer | manufacturer | 91 (90.4072) | 90@100% + 1@40.7% | 99.3% |
| Alternate: Turbo Electric Motor | manufacturer | 16 (15.2864) | 15@100% + 1@28.6% | 95.5% |
| Alternate: Turbo Pressure Motor | manufacturer | 5 (4.5352) | 4@100% + 1@53.5% | 90.7% |
| Alternate: Uranium Fuel Unit | manufacturer | 84 (84.0000) | 84@100% | 100.0% |
| Ballistic Warp Drive (4 sloops) | manufacturer | 24 (24.0000) | 24@250% | 250.0% |
| Modular Engine | manufacturer | 150 (150.0000) | 150@100% | 100.0% |
| Plutonium Fuel Rod | manufacturer | 51 (50.4000) | 50@100% + 1@40% | 98.8% |
| Radio Control Unit | manufacturer | 83 (82.3944) | 82@100% + 1@39.4% | 99.3% |
| Singularity Cell | manufacturer | 30 (30.0000) | 30@100% | 100.0% |
| Thermal Propulsion Rocket | manufacturer | 60 (60.0000) | 60@100% | 100.0% |
| Nuclear Power (Uranium) | nuclear_power_plant | 101 (100.8000) | 100@250% + 1@200% | 249.5% |
| Packaged Nitrogen Gas | packager | 2 (1.3606) | 1@250% + 1@90.1% | 170.1% |
| Packaged Turbofuel | packager | 70 (69.3802) | 69@250% + 1@95.1% | 247.8% |
| AI Expansion Server | quantum_encoder | 67 (66.6667) | 66@25% + 1@16.7% | 24.9% |
| AI Expansion Server (2 sloops) | quantum_encoder | 1 (1.0000) | 1@250% | 250.0% |
| AI Expansion Server (3 sloops) | quantum_encoder | 2 (2.0000) | 2@250% | 250.0% |
| Neural-Quantum Processor | quantum_encoder | 129 (128.8889) | 128@25% + 1@22.2% | 25.0% |
| Superposition Oscillator | quantum_encoder | 174 (173.3333) | 173@25% + 1@8.3% | 24.9% |
| Alternate: Electrode Aluminum Scrap | refinery | 77 (76.3134) | 76@175% + 1@54.8% | 173.4% |
| Alternate: Heavy Oil Residue | refinery | 240 (240.0000) | 240@175% | 175.0% |
| Alternate: Pure Caterium Ingot | refinery | 195 (194.6074) | 194@175% + 1@106.3% | 174.6% |
| Alternate: Pure Copper Ingot | refinery | 1,260 (1259.3629) | 1259@175% + 1@63.5% | 174.9% |
| Alternate: Pure Iron Ingot | refinery | 1,369 (1368.4319) | 1368@175% + 1@75.6% | 174.9% |
| Alternate: Pure Quartz Crystal | refinery | 59 (58.8803) | 58@175% + 1@154.1% | 174.6% |
| Alternate: Recycled Plastic | refinery | 123 (122.9304) | 122@175% + 1@162.8% | 174.9% |
| Alternate: Recycled Rubber | refinery | 137 (136.7946) | 136@175% + 1@139.1% | 174.7% |
| Alternate: Sloppy Alumina | refinery | 59 (58.0638) | 58@175% + 1@11.2% | 172.2% |
| Alternate: Steamed Copper Sheet | refinery | 541 (540.3053) | 540@175% + 1@53.4% | 174.8% |
| Alternate: Wet Concrete | refinery | 128 (127.1081) | 127@175% + 1@18.9% | 173.8% |
| Petroleum Coke | refinery | 53 (52.6363) | 52@175% + 1@111.4% | 173.8% |
| Residual Rubber | refinery | 120 (120.0000) | 120@175% | 175.0% |
| Sulfuric Acid | refinery | 14 (13.6126) | 13@175% + 1@107.2% | 170.2% |
| Alternate: Pure Aluminum Ingot | smelter | 268 (267.0970) | 267@250% + 1@24.2% | 249.2% |
| Iron Ingot | smelter | 51 (50.7819) | 50@250% + 1@195.5% | 248.9% |

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
| Iron Ore (Impure) Mk.3 | miner_mk3 | 39 (39.0000) | 39@250% | 250.0% |
| Iron Ore (Normal) Mk.3 | miner_mk3 | 42 (42.0000) | 42@250% | 250.0% |
| Iron Ore (Pure) Mk.3 | miner_mk3 | 46 (46.0000) | 46@250% | 250.0% |
| Limestone (Normal) Mk.3 | miner_mk3 | 50 (50.0000) | 50@250% | 250.0% |
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
| Water Extraction | water_extractor | 819 (818.3166) | 818@225% + 1@71.2% | 224.8% |

---

# Per item breakdown

For every item this plan produces, the recipes that make it — with the plan's whole-machine count, clock, sloop grade, and the share of the item's total that each recipe supplies.

## Water — 235,985.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Water Extraction | water_extractor | 819 | 224.8% | — | 220,945.5 | 93.6% |
| Alternate: Electrode Aluminum Scrap | refinery | 77 | 173.4% | — | 14,022.6 | 5.9% |
| Non-Fissile Uranium | blender | 51 | 98.8% | — | 756.0 | 0.3% |
| Battery | blender | 9 | 96.7% | — | 261.1 | 0.1% |

## Iron Ingot — 159,467.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Iron Ingot | refinery | 1,369 | 174.9% | — | 155,659.1 | 97.6% |
| Iron Ingot | smelter | 51 | 248.9% | — | 3,808.6 | 2.4% |

## Wire — 93,510.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Iron Wire | constructor | 1,663 | 249.9% | — | 93,510.0 | 100.0% |

## Iron Ore — 92,100.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Iron Ore (Pure) Mk.3 | miner_mk3 | 46 | 250.0% | — | 55,200.0 | 59.9% |
| Iron Ore (Normal) Mk.3 | miner_mk3 | 42 | 250.0% | — | 25,200.0 | 27.4% |
| Iron Ore (Impure) Mk.3 | miner_mk3 | 39 | 250.0% | — | 11,700.0 | 12.7% |

## Copper Ingot — 82,645.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Copper Ingot | refinery | 1,260 | 174.9% | — | 82,645.7 | 100.0% |

## Limestone — 64,800.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Limestone (Pure) Mk.3 | miner_mk3 | 29 | 250.0% | — | 34,800.0 | 53.7% |
| Limestone (Normal) Mk.3 | miner_mk3 | 50 | 250.0% | — | 30,000.0 | 46.3% |

## Coal — 53,277.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Coal (Pure) Mk.3 | miner_mk3 | 16 | 250.0% | — | 19,200.0 | 36.0% |
| Coal (Normal) Mk.3 | miner_mk3 | 31 | 250.0% | — | 18,600.0 | 34.9% |
| Coal (Limestone) | converter | 152 | 49.7% | — | 9,066.5 | 17.0% |
| Coal (Impure) Mk.3 | miner_mk3 | 15 | 250.0% | — | 4,500.0 | 8.4% |
| Coal (Iron) | converter | 64 | 24.9% | — | 1,911.2 | 3.6% |

## Quickwire — 49,041.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Fused Quickwire | assembler | 218 | 250.0% | — | 49,041.1 | 100.0% |

## Aluminum Scrap — 40,064.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Electrode Aluminum Scrap | refinery | 77 | 173.4% | — | 40,064.5 | 100.0% |

## Copper Ore — 36,900.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Copper Ore (Normal) Mk.3 | miner_mk3 | 29 | 250.0% | — | 17,400.0 | 47.2% |
| Copper Ore (Pure) Mk.3 | miner_mk3 | 13 | 250.0% | — | 15,600.0 | 42.3% |
| Copper Ore (Impure) Mk.3 | miner_mk3 | 13 | 250.0% | — | 3,900.0 | 10.6% |

## Alumina Solution — 24,386.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Sloppy Alumina | refinery | 59 | 172.2% | — | 24,386.8 | 100.0% |

## Steel Pipe — 24,277.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Iron Pipe | constructor | 389 | 249.6% | — | 24,277.7 | 100.0% |

## Cable — 24,062.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Cable | constructor | 321 | 249.9% | — | 24,062.1 | 100.0% |

## Copper Sheet — 21,274.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Steamed Copper Sheet | refinery | 541 | 174.8% | — | 21,274.5 | 100.0% |

## Bauxite — 20,322.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Bauxite (Pure) Mk.3 | miner_mk3 | 6 | 250.0% | — | 7,200.0 | 35.4% |
| Bauxite (Caterium) | converter | 92 | 49.5% | — | 5,461.2 | 26.9% |
| Bauxite (Normal) Mk.3 | miner_mk3 | 6 | 250.0% | — | 3,600.0 | 17.7% |
| Bauxite (Copper) | converter | 86 | 24.8% | — | 2,561.1 | 12.6% |
| Bauxite (Impure) Mk.3 | miner_mk3 | 5 | 250.0% | — | 1,500.0 | 7.4% |

## Aluminum Ingot — 20,032.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Aluminum Ingot | smelter | 268 | 249.2% | — | 20,032.3 | 100.0% |

## Rubber — 18,563.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Recycled Rubber | refinery | 137 | 174.7% | — | 14,363.4 | 77.4% |
| Residual Rubber | refinery | 120 | 175.0% | — | 4,200.0 | 22.6% |

## Fuel — 18,122.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Diluted Fuel | blender | 182 | 99.6% | — | 18,122.3 | 100.0% |

## Concrete — 17,795.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Wet Concrete | refinery | 128 | 173.8% | — | 17,795.1 | 100.0% |

## Heavy Oil Residue — 16,800.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heavy Oil Residue | refinery | 240 | 175.0% | — | 16,800.0 | 100.0% |

## Silica — 15,271.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Cheap Silica | assembler | 117 | 248.6% | — | 15,271.1 | 100.0% |

## Caterium Ore — 15,000.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Caterium Ore (Pure) Mk.3 | miner_mk3 | 8 | 250.0% | — | 9,600.0 | 64.0% |
| Caterium Ore (Normal) Mk.3 | miner_mk3 | 9 | 250.0% | — | 5,400.0 | 36.0% |

## Raw Quartz — 13,500.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Quartz (Pure) Mk.3 | miner_mk3 | 7 | 250.0% | — | 8,400.0 | 62.2% |
| Quartz (Normal) Mk.3 | miner_mk3 | 7 | 250.0% | — | 4,200.0 | 31.1% |
| Quartz (Impure) Mk.3 | miner_mk3 | 3 | 250.0% | — | 900.0 | 6.7% |

## Plastic — 12,907.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Recycled Plastic | refinery | 123 | 174.9% | — | 12,907.7 | 100.0% |

## Crude Oil — 12,600.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Crude Oil (Pure) | oil_extractor | 8 | 250.0% | — | 4,800.0 | 38.1% |
| Crude Oil (Normal) | oil_extractor | 12 | 250.0% | — | 3,600.0 | 28.6% |
| Crude Oil (Impure) | oil_extractor | 10 | 250.0% | — | 1,500.0 | 11.9% |
| Crater Lakes Oil Well | resource_well_pressurizer | 1 | 250.0% | — | 1,350.0 | 10.7% |
| Spire Coast Oil Well | resource_well_pressurizer | 1 | 250.0% | — | 900.0 | 7.1% |
| Swamp Oil Well | resource_well_pressurizer | 1 | 250.0% | — | 450.0 | 3.6% |

## Nitrogen Gas — 12,000.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Central Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 3,000.0 | 25.0% |
| Southwestern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 2,100.0 | 17.5% |
| Northwestern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 1,950.0 | 16.2% |
| Northern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 1,800.0 | 15.0% |
| Southeastern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 1,650.0 | 13.8% |
| Southern Nitrogen Gas Well | resource_well_pressurizer | 1 | 250.0% | — | 1,500.0 | 12.5% |

## Petroleum Coke — 11,053.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Petroleum Coke | refinery | 53 | 173.8% | — | 11,053.6 | 100.0% |

## Sulfur — 10,800.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Sulfur (Pure) Mk.3 | miner_mk3 | 5 | 250.0% | — | 6,000.0 | 55.6% |
| Sulfur (Normal) Mk.3 | miner_mk3 | 5 | 250.0% | — | 3,000.0 | 27.8% |
| Sulfur (Impure) Mk.3 | miner_mk3 | 6 | 250.0% | — | 1,800.0 | 16.7% |

## Dark Matter Residue — 10,750.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Superposition Oscillator | quantum_encoder | 174 | 24.9% | — | 5,416.7 | 50.4% |
| Neural-Quantum Processor | quantum_encoder | 129 | 25.0% | — | 2,416.7 | 22.5% |
| AI Expansion Server | quantum_encoder | 67 | 24.9% | — | 1,666.7 | 15.5% |
| AI Expansion Server | quantum_encoder | 2 | 250.0% | 3 | 875.0 | 8.1% |
| AI Expansion Server | quantum_encoder | 1 | 250.0% | 2 | 375.0 | 3.5% |

## Excited Photonic Matter — 10,250.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Excited Photonic Matter | converter | 103 | 49.8% | — | 10,250.0 | 100.0% |

## SAM — 10,200.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| SAM (Normal) Mk.3 | miner_mk3 | 6 | 250.0% | — | 3,600.0 | 35.3% |
| SAM (Pure) Mk.3 | miner_mk3 | 3 | 250.0% | — | 3,600.0 | 35.3% |
| SAM (Impure) Mk.3 | miner_mk3 | 10 | 250.0% | — | 3,000.0 | 29.4% |

## Polymer Resin — 8,400.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heavy Oil Residue | refinery | 240 | 175.0% | — | 8,400.0 | 100.0% |

## Alclad Aluminum Sheet — 7,872.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alclad Aluminum Sheet | assembler | 105 | 249.9% | — | 7,872.5 | 100.0% |

## Iron Plate — 6,938.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Iron Plate | constructor | 139 | 249.6% | — | 6,938.0 | 100.0% |

## Rocket Fuel — 6,565.9/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Rocket Fuel | blender | 44 | 99.0% | — | 4,354.0 | 66.3% |
| Alternate: Nitro Rocket Fuel | blender | 15 | 98.3% | — | 2,211.9 | 33.7% |

## Turbofuel — 6,081.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Turbo Blend Fuel | blender | 136 | 99.4% | — | 6,081.4 | 100.0% |

## Copper Powder — 6,000.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Copper Powder | constructor | 48 | 250.0% | — | 6,000.0 | 100.0% |

## Circuit Board — 5,796.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Silicon Circuit Board | assembler | 186 | 249.3% | — | 5,796.0 | 100.0% |

## Quartz Crystal — 5,409.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Quartz Crystal | refinery | 59 | 174.6% | — | 5,409.6 | 100.0% |

## Diamonds — 5,266.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Turbo Diamonds | accelerator | 174 | 49.8% | — | 5,203.5 | 98.8% |
| Alternate: Pink Diamonds | converter | 9 | 46.8% | — | 63.1 | 1.2% |

## Dark Matter Crystal — 4,300.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Dark Matter Trap | accelerator | 287 | 25.0% | — | 4,300.0 | 100.0% |

## Caterium Ingot — 4,086.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Caterium Ingot | refinery | 195 | 174.6% | — | 4,086.8 | 100.0% |

## Aluminum Casing — 3,469.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Alclad Casing | assembler | 13 | 237.3% | — | 3,469.8 | 100.0% |

## Empty Canister — 3,469.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Empty Canister | constructor | 24 | 240.9% | — | 3,469.0 | 100.0% |

## Packaged Turbofuel — 3,469.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Packaged Turbofuel | packager | 70 | 247.8% | — | 3,469.0 | 100.0% |

## Steel Ingot — 3,216.2/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Compacted Steel Ingot | foundry | 129 | 249.3% | — | 3,216.2 | 100.0% |

## Time Crystal — 2,633.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Time Crystal | converter | 845 | 50.0% | — | 2,534.8 | 96.3% |
| Time Crystal | converter | 66 | 24.9% | — | 98.5 | 3.7% |

## Stator — 2,607.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Stator | assembler | 209 | 249.5% | — | 2,607.7 | 100.0% |

## Reanimated SAM — 2,550.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Reanimated SAM | constructor | 34 | 250.0% | — | 2,550.0 | 100.0% |

## Non-Fissile Uranium — 2,520.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Non-Fissile Uranium | blender | 51 | 98.8% | — | 2,520.0 | 100.0% |

## Uranium Waste — 2,520.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Nuclear Power (Uranium) | nuclear_power_plant | 101 | 249.5% | — | 2,520.0 | 100.0% |

## Battery — 2,169.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Classic Battery | manufacturer | 67 | 99.3% | — | 1,995.7 | 92.0% |
| Battery | blender | 9 | 96.7% | — | 174.0 | 8.0% |

## Uranium — 2,100.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Uranium (Normal) Mk.3 | miner_mk3 | 2 | 250.0% | — | 1,200.0 | 57.1% |
| Uranium (Impure) Mk.3 | miner_mk3 | 3 | 250.0% | — | 900.0 | 42.9% |

## Nitric Acid — 1,979.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Nitric Acid | blender | 66 | 100.0% | — | 1,979.4 | 100.0% |

## Encased Uranium Cell — 1,680.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Infused Uranium Cell | manufacturer | 84 | 100.0% | — | 1,680.0 | 100.0% |

## Steel Beam — 1,676.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Molded Beam | foundry | 11 | 243.7% | — | 1,206.1 | 71.9% |
| Alternate: Aluminum Beam | constructor | 9 | 232.5% | — | 470.7 | 28.1% |

## Ficsite Trigon — 1,450.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Ficsite Trigon | constructor | 20 | 241.7% | — | 1,450.0 | 100.0% |

## AI Limiter — 1,413.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| AI Limiter | assembler | 114 | 247.9% | — | 1,413.1 | 100.0% |

## Computer — 1,338.2/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Caterium Computer | manufacturer | 276 | 99.9% | — | 1,034.2 | 77.3% |
| Alternate: Crystal Computer | assembler | 37 | 246.4% | — | 303.9 | 22.7% |

## Automated Wiring — 1,203.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Automated Wiring | assembler | 193 | 249.3% | — | 1,203.1 | 100.0% |

## Sulfuric Acid — 1,191.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Sulfuric Acid | refinery | 14 | 170.2% | — | 1,191.1 | 100.0% |

## Encased Industrial Beam — 1,130.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Encased Industrial Pipe | assembler | 114 | 247.9% | — | 1,130.4 | 100.0% |

## Rotor — 1,092.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Steel Rotor | assembler | 88 | 248.3% | — | 1,092.6 | 100.0% |

## Modular Frame — 1,025.2/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Steeled Frame | assembler | 137 | 249.4% | — | 1,025.2 | 100.0% |

## Reinforced Iron Plate — 983.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Stitched Iron Plate | assembler | 70 | 249.8% | — | 983.4 | 100.0% |

## Electromagnetic Control Rod — 891.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Electromagnetic Control Rod | assembler | 90 | 247.5% | — | 891.1 | 100.0% |

## Compacted Coal — 804.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Rocket Fuel | blender | 44 | 99.0% | — | 435.4 | 54.2% |
| Alternate: Nitro Rocket Fuel | blender | 15 | 98.3% | — | 368.6 | 45.8% |

## Plutonium Pellet — 756.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Plutonium Pellet | accelerator | 101 | 25.0% | — | 756.0 | 100.0% |

## Motor — 524.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Electric Motor | assembler | 28 | 249.7% | — | 524.3 | 100.0% |

## Crystal Oscillator — 522.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Insulated Crystal Oscillator | manufacturer | 279 | 99.8% | — | 522.0 | 100.0% |

## Heat Sink — 486.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Heat Sink | assembler | 26 | 249.2% | — | 486.0 | 100.0% |

## Ficsite Ingot — 483.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Ficsite Ingot (Aluminum) | converter | 33 | 48.8% | — | 483.3 | 100.0% |

## Encased Plutonium Cell — 378.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Encased Plutonium Cell | assembler | 31 | 243.9% | — | 378.0 | 100.0% |

## Heavy Modular Frame — 339.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heavy Encased Frame | manufacturer | 121 | 99.7% | — | 339.1 | 100.0% |

## Smart Plating — 300.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Smart Plating | assembler | 60 | 250.0% | — | 300.0 | 100.0% |

## Singularity Cell — 300.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Singularity Cell | manufacturer | 30 | 100.0% | — | 300.0 | 100.0% |

## Versatile Framework — 241.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Versatile Framework | assembler | 20 | 241.7% | — | 241.7 | 100.0% |

## Adaptive Control Unit — 240.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Adaptive Control Unit | manufacturer | 241 | 99.8% | — | 240.6 | 100.0% |

## Supercomputer — 217.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Super-State Computer | manufacturer | 91 | 99.3% | — | 217.0 | 100.0% |

## Superposition Oscillator — 216.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Superposition Oscillator | quantum_encoder | 174 | 24.9% | — | 216.7 | 100.0% |

## Radio Control Unit — 206.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Radio Control Unit | manufacturer | 83 | 99.3% | — | 206.0 | 100.0% |

## Empty Fluid Tank — 204.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Empty Fluid Tank | constructor | 2 | 170.1% | — | 204.1 | 100.0% |

## Packaged Nitrogen Gas — 204.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Packaged Nitrogen Gas | packager | 2 | 170.1% | — | 204.1 | 100.0% |

## Cooling System — 180.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Cooling Device | blender | 36 | 100.0% | — | 180.0 | 100.0% |

## Modular Engine — 150.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Modular Engine | manufacturer | 150 | 100.0% | — | 150.0 | 100.0% |

## Assembly Director System — 120.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Assembly Director System | assembler | 65 | 246.8% | — | 120.3 | 100.0% |

## Ballistic Warp Drive — 120.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Ballistic Warp Drive | manufacturer | 24 | 250.0% | 4 | 120.0 | 100.0% |

## AI Expansion Server — 116.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| AI Expansion Server | quantum_encoder | 67 | 24.9% | — | 66.7 | 57.1% |
| AI Expansion Server | quantum_encoder | 2 | 250.0% | 3 | 35.0 | 30.0% |
| AI Expansion Server | quantum_encoder | 1 | 250.0% | 2 | 15.0 | 12.9% |

## Fused Modular Frame — 98.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heat-Fused Frame | blender | 33 | 99.5% | — | 98.5 | 100.0% |

## Neural-Quantum Processor — 96.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Neural-Quantum Processor | quantum_encoder | 129 | 25.0% | — | 96.7 | 100.0% |

## Magnetic Field Generator — 96.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Magnetic Field Generator | assembler | 39 | 247.9% | — | 96.7 | 100.0% |

## Thermal Propulsion Rocket — 60.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Thermal Propulsion Rocket | manufacturer | 60 | 100.0% | — | 60.0 | 100.0% |

## Turbo Motor — 60.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Turbo Electric Motor | manufacturer | 16 | 95.5% | — | 43.0 | 71.7% |
| Alternate: Turbo Pressure Motor | manufacturer | 5 | 90.7% | — | 17.0 | 28.3% |

## Uranium Fuel Rod — 50.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Uranium Fuel Unit | manufacturer | 84 | 100.0% | — | 50.4 | 100.0% |

## Pressure Conversion Cube — 38.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Pressure Conversion Cube | assembler | 16 | 240.6% | — | 38.5 | 100.0% |

## Nuclear Pasta — 30.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Nuclear Pasta | accelerator | 240 | 25.0% | — | 30.0 | 100.0% |

## Plutonium Fuel Rod — 12.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Plutonium Fuel Rod | manufacturer | 51 | 98.8% | — | 12.6 | 100.0% |

---

# Per-machine breakdown

One section per machine type in the plan: the recipes it runs, the whole-machine count, clock and sloop grade, and aggregate inputs/outputs per minute.

## Refinery — 4,375 machines · 274,535 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Pure Iron Ingot | 1,369 | 174.9% | — | Iron Ore 83,816.5 + Water 47,895.1 | Iron Ingot 155,659.1 |
| Alternate: Pure Copper Ingot | 1,260 | 174.9% | — | Copper Ore 33,058.3 + Water 22,038.9 | Copper Ingot 82,645.7 |
| Alternate: Steamed Copper Sheet | 541 | 174.8% | — | Copper Ingot 21,274.5 + Water 21,274.5 | Copper Sheet 21,274.5 |
| Alternate: Heavy Oil Residue | 240 | 175.0% | — | Crude Oil 12,600.0 | Heavy Oil Residue 16,800.0 + Polymer Resin 8,400.0 |
| Alternate: Pure Caterium Ingot | 195 | 174.6% | — | Caterium Ore 8,173.5 + Water 8,173.5 | Caterium Ingot 4,086.8 |
| Alternate: Recycled Rubber | 137 | 174.7% | — | Fuel 7,181.7 + Plastic 7,181.7 | Rubber 14,363.4 |
| Alternate: Wet Concrete | 128 | 173.8% | — | Limestone 26,692.7 + Water 22,243.9 | Concrete 17,795.1 |
| Alternate: Recycled Plastic | 123 | 174.9% | — | Fuel 6,453.8 + Rubber 6,453.8 | Plastic 12,907.7 |
| Residual Rubber | 120 | 175.0% | — | Polymer Resin 8,400.0 + Water 8,400.0 | Rubber 4,200.0 |
| Alternate: Electrode Aluminum Scrap | 77 | 173.4% | — | Alumina Solution 24,038.7 + Petroleum Coke 8,012.9 | Aluminum Scrap 40,064.5 + Water 14,022.6 |
| Alternate: Pure Quartz Crystal | 59 | 174.6% | — | Raw Quartz 6,955.2 + Water 3,864.0 | Quartz Crystal 5,409.6 |
| Alternate: Sloppy Alumina | 59 | 172.2% | — | Bauxite 20,322.3 + Water 20,322.3 | Alumina Solution 24,386.8 |
| Petroleum Coke | 53 | 173.8% | — | Heavy Oil Residue 3,684.5 | Petroleum Coke 11,053.6 |
| Sulfuric Acid | 14 | 170.2% | — | Sulfur 1,191.1 + Water 1,191.1 | Sulfuric Acid 1,191.1 |

## Constructor — 2,649 machines · 35,502 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Iron Wire | 1,663 | 249.9% | — | Iron Ingot 51,950.0 | Wire 93,510.0 |
| Alternate: Iron Pipe | 389 | 249.6% | — | Iron Ingot 97,110.9 | Steel Pipe 24,277.7 |
| Cable | 321 | 249.9% | — | Wire 48,124.3 | Cable 24,062.1 |
| Iron Plate | 139 | 249.6% | — | Iron Ingot 10,406.9 | Iron Plate 6,938.0 |
| Copper Powder | 48 | 250.0% | — | Copper Ingot 36,000.0 | Copper Powder 6,000.0 |
| Reanimated SAM | 34 | 250.0% | — | SAM 10,200.0 | Reanimated SAM 2,550.0 |
| Empty Canister | 24 | 240.9% | — | Plastic 1,734.5 | Empty Canister 3,469.0 |
| Ficsite Trigon | 20 | 241.7% | — | Ficsite Ingot 483.3 | Ficsite Trigon 1,450.0 |
| Alternate: Aluminum Beam | 9 | 232.5% | — | Aluminum Ingot 470.7 | Steel Beam 470.7 |
| Empty Fluid Tank | 2 | 170.1% | — | Aluminum Ingot 204.1 | Empty Fluid Tank 204.1 |

## Assembler — 1,976 machines · 98,832 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Fused Quickwire | 218 | 250.0% | — | Caterium Ingot 4,086.8 + Copper Ingot 20,433.8 | Quickwire 49,041.1 |
| Stator | 209 | 249.5% | — | Steel Pipe 7,823.2 + Wire 20,861.9 | Stator 2,607.7 |
| Automated Wiring | 193 | 249.3% | — | Cable 24,062.1 + Stator 1,203.1 | Automated Wiring 1,203.1 |
| Alternate: Silicon Circuit Board | 186 | 249.3% | — | Copper Sheet 12,751.1 + Silica 12,751.1 | Circuit Board 5,796.0 |
| Alternate: Steeled Frame | 137 | 249.4% | — | Reinforced Iron Plate 683.4 + Steel Pipe 3,417.2 | Modular Frame 1,025.2 |
| Alternate: Cheap Silica | 117 | 248.6% | — | Limestone 10,907.9 + Raw Quartz 6,544.8 | Silica 15,271.1 |
| AI Limiter | 114 | 247.9% | — | Copper Sheet 7,065.4 + Quickwire 28,261.7 | AI Limiter 1,413.1 |
| Alternate: Encased Industrial Pipe | 114 | 247.9% | — | Concrete 5,652.1 + Steel Pipe 6,782.5 | Encased Industrial Beam 1,130.4 |
| Alclad Aluminum Sheet | 105 | 249.9% | — | Aluminum Ingot 7,872.5 + Copper Ingot 2,624.2 | Alclad Aluminum Sheet 7,872.5 |
| Electromagnetic Control Rod | 90 | 247.5% | — | AI Limiter 891.1 + Stator 1,336.6 | Electromagnetic Control Rod 891.1 |
| Alternate: Steel Rotor | 88 | 248.3% | — | Steel Pipe 2,185.3 + Wire 6,555.9 | Rotor 1,092.6 |
| Alternate: Stitched Iron Plate | 70 | 249.8% | — | Iron Plate 3,278.1 + Wire 6,556.3 | Reinforced Iron Plate 983.4 |
| Assembly Director System | 65 | 246.8% | — | Adaptive Control Unit 240.6 + Supercomputer 120.3 | Assembly Director System 120.3 |
| Smart Plating | 60 | 250.0% | — | Reinforced Iron Plate 300.0 + Rotor 300.0 | Smart Plating 300.0 |
| Magnetic Field Generator | 39 | 247.9% | — | Electromagnetic Control Rod 96.7 + Versatile Framework 241.7 | Magnetic Field Generator 96.7 |
| Alternate: Crystal Computer | 37 | 246.4% | — | Circuit Board 455.9 + Crystal Oscillator 152.0 | Computer 303.9 |
| Encased Plutonium Cell | 31 | 243.9% | — | Concrete 1,512.0 + Plutonium Pellet 756.0 | Encased Plutonium Cell 378.0 |
| Alternate: Electric Motor | 28 | 249.7% | — | Electromagnetic Control Rod 262.2 + Rotor 524.3 | Motor 524.3 |
| Heat Sink | 26 | 249.2% | — | Alclad Aluminum Sheet 2,430.0 + Copper Sheet 1,458.0 | Heat Sink 486.0 |
| Versatile Framework | 20 | 241.7% | — | Modular Frame 120.8 + Steel Beam 1,450.0 | Versatile Framework 241.7 |
| Pressure Conversion Cube | 16 | 240.6% | — | Fused Modular Frame 38.5 + Radio Control Unit 77.0 | Pressure Conversion Cube 38.5 |
| Alternate: Alclad Casing | 13 | 237.3% | — | Aluminum Ingot 4,626.4 + Copper Ingot 2,313.2 | Aluminum Casing 3,469.8 |

## Manufacturer — 1,662 machines · 107,453 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Insulated Crystal Oscillator | 279 | 99.8% | — | AI Limiter 522.0 + Quartz Crystal 5,220.2 + Rubber 3,654.1 | Crystal Oscillator 522.0 |
| Alternate: Caterium Computer | 276 | 99.9% | — | Circuit Board 4,137.0 + Quickwire 14,479.4 + Rubber 6,205.5 | Computer 1,034.2 |
| Adaptive Control Unit | 241 | 99.8% | — | Automated Wiring 1,203.1 + Circuit Board 1,203.1 + Computer 481.2 + Heavy Modular Frame 240.6 | Adaptive Control Unit 240.6 |
| Modular Engine | 150 | 100.0% | — | Motor 300.0 + Rubber 2,250.0 + Smart Plating 300.0 | Modular Engine 150.0 |
| Alternate: Heavy Encased Frame | 121 | 99.7% | — | Concrete 2,486.9 + Encased Industrial Beam 1,130.4 + Modular Frame 904.3 + Steel Pipe 4,069.5 | Heavy Modular Frame 339.1 |
| Alternate: Super-State Computer | 91 | 99.3% | — | Battery 2,169.8 + Computer 650.9 + Electromagnetic Control Rod 217.0 + Wire 5,424.4 | Supercomputer 217.0 |
| Alternate: Infused Uranium Cell | 84 | 100.0% | — | Quickwire 6,300.0 + Silica 1,260.0 + Sulfur 2,100.0 + Uranium 2,100.0 | Encased Uranium Cell 1,680.0 |
| Alternate: Uranium Fuel Unit | 84 | 100.0% | — | Crystal Oscillator 50.4 + Electromagnetic Control Rod 168.0 + Encased Uranium Cell 1,680.0 + Rotor 168.0 | Uranium Fuel Rod 50.4 |
| Radio Control Unit | 83 | 99.3% | — | Aluminum Casing 3,295.8 + Computer 206.0 + Crystal Oscillator 103.0 | Radio Control Unit 206.0 |
| Alternate: Classic Battery | 67 | 99.3% | — | Alclad Aluminum Sheet 3,492.5 + Plastic 3,991.5 + Sulfur 2,993.6 + Wire 5,987.2 | Battery 1,995.7 |
| Thermal Propulsion Rocket | 60 | 100.0% | — | Cooling System 180.0 + Fused Modular Frame 60.0 + Modular Engine 150.0 + Turbo Motor 60.0 | Thermal Propulsion Rocket 60.0 |
| Plutonium Fuel Rod | 51 | 98.8% | — | Electromagnetic Control Rod 75.6 + Encased Plutonium Cell 378.0 + Heat Sink 126.0 + Steel Beam 226.8 | Plutonium Fuel Rod 12.6 |
| Singularity Cell | 30 | 100.0% | — | Concrete 6,000.0 + Dark Matter Crystal 600.0 + Iron Plate 3,000.0 + Nuclear Pasta 30.0 | Singularity Cell 300.0 |
| Ballistic Warp Drive | 24 | 250.0% | 4 | Dark Matter Crystal 2,400.0 + Singularity Cell 300.0 + Superposition Oscillator 120.0 + Thermal Propulsion Rocket 60.0 | Ballistic Warp Drive 120.0 |
| Alternate: Turbo Electric Motor | 16 | 95.5% | — | Electromagnetic Control Rod 71.7 + Motor 100.3 + Radio Control Unit 129.0 + Rotor 100.3 | Turbo Motor 43.0 |
| Alternate: Turbo Pressure Motor | 5 | 90.7% | — | Motor 34.0 + Packaged Nitrogen Gas 204.1 + Pressure Conversion Cube 8.5 + Stator 68.0 | Turbo Motor 17.0 |

## Converter — 1,450 machines · 131,474 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Time Crystal | 845 | 50.0% | — | Diamonds 5,069.6 | Time Crystal 2,534.8 |
| Coal (Limestone) | 152 | 49.7% | — | Limestone 27,199.4 + Reanimated SAM 755.5 | Coal 9,066.5 |
| Excited Photonic Matter | 103 | 49.8% | — | — | Excited Photonic Matter 10,250.0 |
| Bauxite (Caterium) | 92 | 49.5% | — | Caterium Ore 6,826.5 + Reanimated SAM 455.1 | Bauxite 5,461.2 |
| Bauxite (Copper) | 86 | 24.8% | — | Copper Ore 3,841.7 + Reanimated SAM 213.4 | Bauxite 2,561.1 |
| Time Crystal | 66 | 24.9% | — | Diamonds 197.1 | Time Crystal 98.5 |
| Coal (Iron) | 64 | 24.9% | — | Iron Ore 2,866.8 + Reanimated SAM 159.3 | Coal 1,911.2 |
| Ficsite Ingot (Aluminum) | 33 | 48.8% | — | Aluminum Ingot 1,933.3 + Reanimated SAM 966.7 | Ficsite Ingot 483.3 |
| Alternate: Pink Diamonds | 9 | 46.8% | — | Coal 505.2 + Quartz Crystal 189.4 | Diamonds 63.1 |

## Accelerator — 802 machines · 109,636 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Dark Matter Trap | 287 | 25.0% | — | Dark Matter Residue 10,750.0 + Time Crystal 2,150.0 | Dark Matter Crystal 4,300.0 |
| Nuclear Pasta | 240 | 25.0% | — | Copper Powder 6,000.0 + Pressure Conversion Cube 30.0 | Nuclear Pasta 30.0 |
| Alternate: Turbo Diamonds | 174 | 49.8% | — | Coal 52,035.2 + Packaged Turbofuel 3,469.0 | Diamonds 5,203.5 |
| Plutonium Pellet | 101 | 25.0% | — | Non-Fissile Uranium 2,520.0 + Uranium Waste 630.0 | Plutonium Pellet 756.0 |

## Blender — 572 machines · 42,561 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Diluted Fuel | 182 | 99.6% | — | Heavy Oil Residue 9,061.2 + Water 18,122.3 | Fuel 18,122.3 |
| Alternate: Turbo Blend Fuel | 136 | 99.4% | — | Fuel 2,027.1 + Heavy Oil Residue 4,054.3 + Petroleum Coke 3,040.7 + Sulfur 3,040.7 | Turbofuel 6,081.4 |
| Nitric Acid | 66 | 100.0% | — | Iron Plate 659.8 + Nitrogen Gas 7,917.7 + Water 1,979.4 | Nitric Acid 1,979.4 |
| Non-Fissile Uranium | 51 | 98.8% | — | Nitric Acid 756.0 + Silica 1,260.0 + Sulfuric Acid 756.0 + Uranium Waste 1,890.0 | Non-Fissile Uranium 2,520.0 + Water 756.0 |
| Rocket Fuel | 44 | 99.0% | — | Nitric Acid 435.4 + Turbofuel 2,612.4 | Compacted Coal 435.4 + Rocket Fuel 4,354.0 |
| Alternate: Cooling Device | 36 | 100.0% | — | Heat Sink 360.0 + Motor 90.0 + Nitrogen Gas 2,160.0 | Cooling System 180.0 |
| Alternate: Heat-Fused Frame | 33 | 99.5% | — | Aluminum Ingot 4,925.2 + Fuel 985.0 + Heavy Modular Frame 98.5 + Nitric Acid 788.0 | Fused Modular Frame 98.5 |
| Alternate: Nitro Rocket Fuel | 15 | 98.3% | — | Coal 737.3 + Fuel 1,474.6 + Nitrogen Gas 1,105.9 + Sulfur 1,474.6 | Compacted Coal 368.6 + Rocket Fuel 2,211.9 |
| Battery | 9 | 96.7% | — | Alumina Solution 348.1 + Aluminum Casing 174.0 + Sulfuric Acid 435.1 | Battery 174.0 + Water 261.1 |

## Quantum Encoder — 373 machines · 87,086 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Superposition Oscillator | 174 | 24.9% | — | Alclad Aluminum Sheet 1,950.0 + Crystal Oscillator 216.7 + Dark Matter Crystal 1,300.0 + Excited Photonic Matter 5,416.7 | Dark Matter Residue 5,416.7 + Superposition Oscillator 216.7 |
| Neural-Quantum Processor | 129 | 25.0% | — | Excited Photonic Matter 2,416.7 + Ficsite Trigon 1,450.0 + Supercomputer 96.7 + Time Crystal 483.3 | Dark Matter Residue 2,416.7 + Neural-Quantum Processor 96.7 |
| AI Expansion Server | 67 | 24.9% | — | Excited Photonic Matter 1,666.7 + Magnetic Field Generator 66.7 + Neural-Quantum Processor 66.7 + Superposition Oscillator 66.7 | AI Expansion Server 66.7 + Dark Matter Residue 1,666.7 |
| AI Expansion Server | 2 | 250.0% | 3 | Excited Photonic Matter 500.0 + Magnetic Field Generator 20.0 + Neural-Quantum Processor 20.0 + Superposition Oscillator 20.0 | AI Expansion Server 35.0 + Dark Matter Residue 875.0 |
| AI Expansion Server | 1 | 250.0% | 2 | Excited Photonic Matter 250.0 + Magnetic Field Generator 10.0 + Neural-Quantum Processor 10.0 + Superposition Oscillator 10.0 | AI Expansion Server 15.0 + Dark Matter Residue 375.0 |

## Smelter — 319 machines · 4,265 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Pure Aluminum Ingot | 268 | 249.2% | — | Aluminum Scrap 40,064.5 | Aluminum Ingot 20,032.3 |
| Iron Ingot | 51 | 248.9% | — | Iron Ore 3,808.6 | Iron Ingot 3,808.6 |

## Foundry — 140 machines · 7,477 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Compacted Steel Ingot | 129 | 249.3% | — | Compacted Coal 804.0 + Iron Ore 1,608.1 | Steel Ingot 3,216.2 |
| Alternate: Molded Beam | 11 | 243.7% | — | Concrete 2,144.1 + Steel Ingot 3,216.2 | Steel Beam 1,206.1 |

## Packager — 72 machines · 2,363 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Packaged Turbofuel | 70 | 247.8% | — | Empty Canister 3,469.0 + Turbofuel 3,469.0 | Packaged Turbofuel 3,469.0 |
| Packaged Nitrogen Gas | 2 | 170.1% | — | Empty Fluid Tank 204.1 + Nitrogen Gas 816.3 | Packaged Nitrogen Gas 204.1 |

---

# Resource extraction

Raw-material supply: miners, water/oil extractors and pressure wells. (The high-level overview aggregates these by resource; here each node group is listed.)

## Water Extractor — 819 machines · 47,796 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Water Extraction | 819 | 224.8% | — | — | Water 220,945.5 |

## Miner Mk.3 — 414 machines · 62,555 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
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

## Fuel Generator — 631 machines · **393,955 MW generated**

| Recipe | count | clock | slps | fuel /min | output |
|---|---|---:|---:|---|---|
| Rocket Fuel Power | 631 | 249.7% | — | Rocket Fuel 6,565.9 | 393,955 MW |

---

## Notes

- **Power rounding**: per-section draws are computed from the displayed whole-machine counts and sum to 1,020,097 MW, ~0.1% under the official 1,020,846 MW (the model also runs tiny sub-machine exact-balance slivers). Generation is clock-linear, so whole-machine sums reproduce the 1,031,055 MW exactly.
- Accelerator rows use per-recipe power draw where the spec overrides it; other machines use their machine default.
- Rates are **aggregate** at the displayed clock. Per-machine rate at that clock = aggregate ÷ `#`.
