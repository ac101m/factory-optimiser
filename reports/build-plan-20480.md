# Satisfactory Factory Optimiser — Build Plan

**Official optimum** — **483,722,303 pts/min** (overclock tiers 25%, 50%, 75%, 100%, 125%, 150%, 175%, 200%, 225%, 250%; Auto-solved (augmenter sweep)). All rates are per minute.

## High-level overview

| Metric | Value | Notes |
|---|---|---|
| **Sink points** | **483,722,303 pts/min** | 0 augmenter(s), 1.00x power |
| **Power load** | **970,385 MW** | what consumers actually draw |
| **Power supplied** | 980,089 MW | load x1.01 (1% reserve) |
| **Machines** | **20,519** (cap 20,480 — binding) | 142 recipe rows across 18 machine types |
| **Somersloops** | 104 / 104 | see overclock notes |
| **Sink throughput** | 378.5 items/min | one Awesome Sink covers it (1200/min cap, 30 MW) |

### Sink flows

| Sink item | pts/item | /min | pts/min | share |
|---|---:|---:|---:|---:|
| Ballistic Warp Drive | 2,895,334 | 120.0 | 347,440,080 | 71.8% |
| AI Expansion Server | 597,652 | 116.7 | 69,726,067 | 14.4% |
| Assembly Director System | 500,176 | 129.2 | 64,626,038 | 13.4% |
| Plutonium Fuel Rod | 153,184 | 12.6 | 1,930,118 | 0.4% |
| **TOTAL** | | | **483,722,303** | 100% |

### Map resources extracted

Miners are shown at their planned 250% clock; every tapped node group is maxed.

| Resource | extractors | /min |
|---|---:|---:|
| Water | 1,082 | 227,151 |
| Iron Ore | 127 | 92,100 |
| Limestone | 94 | 69,300 |
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
| Water | 241,744.8 | 241,744.8 | +0.0 | balanced |
| Iron Ingot | 164,372.0 | 164,372.0 | -0.0 | balanced |
| Wire | 96,783.6 | 96,783.6 | +0.0 | balanced |
| Iron Ore | 92,100.0 | 92,100.0 | +0.0 | balanced |
| Copper Ingot | 84,354.6 | 84,354.6 | -0.0 | balanced |
| Limestone | 69,300.0 | 69,300.0 | +0.0 | balanced |
| Coal | 53,744.0 | 53,744.0 | +0.0 | balanced |
| Quickwire | 49,775.6 | 49,775.6 | +0.0 | balanced |
| Aluminum Scrap | 39,537.4 | 39,537.4 | +0.0 | balanced |
| Copper Ore | 36,900.0 | 36,900.0 | +0.0 | balanced |
| Cable | 25,841.3 | 25,841.3 | +0.0 | balanced |
| Steel Pipe | 24,607.1 | 24,607.1 | +0.0 | balanced |
| Alumina Solution | 23,722.4 | 23,722.4 | +0.0 | balanced |
| Copper Sheet | 22,719.3 | 22,719.3 | +0.0 | balanced |
| Rubber | 20,266.1 | 20,266.1 | +0.0 | balanced |
| Fuel | 20,032.8 | 20,032.8 | +0.0 | balanced |
| Aluminum Ingot | 19,768.7 | 19,768.7 | -0.0 | balanced |
| Bauxite | 19,768.7 | 19,768.7 | +0.0 | balanced |
| Concrete | 18,169.1 | 18,169.1 | -0.0 | balanced |
| Heavy Oil Residue | 16,800.0 | 16,800.0 | -0.0 | balanced |
| Silica | 15,948.6 | 15,948.6 | +0.0 | balanced |
| Caterium Ore | 15,000.0 | 15,000.0 | +0.0 | balanced |
| Plastic | 14,306.1 | 14,306.1 | +0.0 | balanced |
| Raw Quartz | 13,500.0 | 13,500.0 | +0.0 | balanced |
| Crude Oil | 12,600.0 | 12,600.0 | +0.0 | balanced |
| Nitrogen Gas | 12,000.0 | 12,000.0 | +0.0 | balanced |
| Sulfur | 10,887.3 | 10,887.3 | +0.0 | balanced |
| Dark Matter Residue | 10,750.0 | 10,750.0 | +0.0 | balanced |
| Petroleum Coke | 10,396.1 | 10,396.1 | -0.0 | balanced |
| Excited Photonic Matter | 10,250.0 | 10,250.0 | +0.0 | balanced |
| SAM | 10,200.0 | 10,200.0 | +0.0 | balanced |
| Polymer Resin | 8,400.0 | 8,400.0 | -0.0 | balanced |
| Alclad Aluminum Sheet | 8,332.8 | 8,332.8 | +0.0 | balanced |
| Iron Plate | 6,997.0 | 6,997.0 | +0.0 | balanced |
| Screws | 6,717.1 | 6,717.1 | +0.0 | balanced |
| Circuit Board | 6,103.9 | 6,103.9 | +0.0 | balanced |
| Copper Powder | 6,000.0 | 6,000.0 | +0.0 | balanced |
| Rocket Fuel | 5,716.5 | 5,716.5 | +0.0 | balanced |
| Diamonds | 5,266.7 | 5,266.7 | +0.0 | balanced |
| Quartz Crystal | 5,183.8 | 5,183.8 | -0.0 | balanced |
| Turbofuel | 5,001.9 | 5,001.9 | +0.0 | balanced |
| Dark Matter Crystal | 4,300.0 | 4,300.0 | +0.0 | balanced |
| Caterium Ingot | 4,148.0 | 4,148.0 | +0.0 | balanced |
| Empty Canister | 3,511.1 | 3,511.1 | +0.0 | balanced |
| Packaged Turbofuel | 3,511.1 | 3,511.1 | +0.0 | balanced |
| Aluminum Casing | 3,176.9 | 3,176.9 | +0.0 | balanced |
| Steel Ingot | 3,069.8 | 3,069.8 | -0.0 | balanced |
| Stator | 2,714.7 | 2,714.7 | +0.0 | balanced |
| Time Crystal | 2,633.3 | 2,633.3 | +0.0 | balanced |
| Reanimated SAM | 2,550.0 | 2,550.0 | +0.0 | balanced |
| Non-Fissile Uranium | 2,520.0 | 2,520.0 | +0.0 | balanced |
| Uranium Waste | 2,520.0 | 2,520.0 | +0.0 | balanced |
| Battery | 2,258.7 | 2,258.7 | +0.0 | balanced |
| Uranium | 2,100.0 | 2,100.0 | +0.0 | balanced |
| Nitric Acid | 1,807.3 | 1,807.3 | +0.0 | balanced |
| Encased Uranium Cell | 1,680.0 | 1,680.0 | +0.0 | balanced |
| Ficsite Trigon | 1,450.0 | 1,450.0 | +0.0 | balanced |
| AI Limiter | 1,411.5 | 1,411.5 | +0.0 | balanced |
| Computer | 1,393.0 | 1,393.0 | +0.0 | balanced |
| Automated Wiring | 1,292.1 | 1,292.1 | +0.0 | balanced |
| Encased Industrial Beam | 1,195.9 | 1,195.9 | +0.0 | balanced |
| Steel Beam | 1,151.2 | 1,151.2 | +0.0 | balanced |
| Rotor | 1,082.7 | 1,082.7 | +0.0 | balanced |
| Modular Frame | 1,077.6 | 1,077.6 | +0.0 | balanced |
| Reinforced Iron Plate | 1,018.4 | 1,018.4 | +0.0 | balanced |
| Electromagnetic Control Rod | 893.1 | 893.1 | -0.0 | balanced |
| Compacted Coal | 787.1 | 787.1 | +0.0 | balanced |
| Plutonium Pellet | 756.0 | 756.0 | +0.0 | balanced |
| Sulfuric Acid | 756.0 | 756.0 | +0.0 | balanced |
| Motor | 523.1 | 523.1 | +0.0 | balanced |
| Crystal Oscillator | 518.4 | 518.4 | -0.0 | balanced |
| Heat Sink | 486.0 | 486.0 | +0.0 | balanced |
| Ficsite Ingot | 483.3 | 483.3 | +0.0 | balanced |
| Encased Plutonium Cell | 378.0 | 378.0 | +0.0 | balanced |
| Heavy Modular Frame | 358.8 | 358.8 | +0.0 | balanced |
| Singularity Cell | 300.0 | 300.0 | +0.0 | balanced |
| Smart Plating | 300.0 | 300.0 | +0.0 | balanced |
| Adaptive Control Unit | 258.4 | 258.4 | +0.0 | balanced |
| Empty Fluid Tank | 248.7 | 248.7 | +0.0 | balanced |
| Packaged Nitrogen Gas | 248.7 | 248.7 | +0.0 | balanced |
| Versatile Framework | 241.7 | 241.7 | -0.0 | balanced |
| Supercomputer | 225.9 | 225.9 | +0.0 | balanced |
| Superposition Oscillator | 216.7 | 216.7 | +0.0 | balanced |
| Radio Control Unit | 198.6 | 198.6 | +0.0 | balanced |
| Cooling System | 180.0 | 180.0 | +0.0 | balanced |
| Modular Engine | 150.0 | 150.0 | +0.0 | balanced |
| Assembly Director System | 129.2 | 0.0 | +129.2 | → Awesome Sink (129.2/min) |
| Ballistic Warp Drive | 120.0 | 0.0 | +120.0 | → Awesome Sink (120.0/min) |
| AI Expansion Server | 116.7 | 0.0 | +116.7 | → Awesome Sink (116.7/min) |
| Fused Modular Frame | 100.4 | 100.4 | +0.0 | balanced |
| Magnetic Field Generator | 96.7 | 96.7 | +0.0 | balanced |
| Neural-Quantum Processor | 96.7 | 96.7 | -0.0 | balanced |
| Thermal Propulsion Rocket | 60.0 | 60.0 | +0.0 | balanced |
| Turbo Motor | 60.0 | 60.0 | +0.0 | balanced |
| Uranium Fuel Rod | 50.4 | 50.4 | +0.0 | balanced |
| Pressure Conversion Cube | 40.4 | 40.4 | +0.0 | balanced |
| Nuclear Pasta | 30.0 | 30.0 | +0.0 | balanced |
| Plutonium Fuel Rod | 12.6 | 0.0 | +12.6 | → Awesome Sink (12.6/min) |

---

# All used recipes

142 recipe rows from 139 distinct recipes (rows repeat a recipe when sloop grades or clocks differ). `count` is the machines to build, with the raw fractional count in brackets; `clock` shows how to split that build into whole machines at the clock tier plus one trimmed remainder (e.g. `10@100% + 1@50%`); `equivalent all-machine clock` is the single uniform clock that reproduces the same throughput. A row whose equivalent clock sits below the tier is an exact-balance remnant, not a choice.

| Recipe | machine | count | clock | equivalent all-machine clock |
|---|---|---:|---:|---:|
| Alternate: Dark Matter Trap | accelerator | 287 (286.6667) | 286@25% + 1@16.7% | 25.0% |
| Alternate: Turbo Diamonds | accelerator | 352 (351.1111) | 351@25% + 1@2.8% | 24.9% |
| Nuclear Pasta | accelerator | 240 (240.0000) | 240@25% | 25.0% |
| Plutonium Pellet | accelerator | 101 (100.8000) | 100@25% + 1@20% | 25.0% |
| AI Limiter | assembler | 126 (125.4694) | 125@225% + 1@105.6% | 224.1% |
| Alclad Aluminum Sheet | assembler | 124 (123.4486) | 123@225% + 1@100.9% | 224.0% |
| Alternate: Alclad Casing | assembler | 13 (12.5507) | 12@225% + 1@123.9% | 217.2% |
| Alternate: Cheap Silica | assembler | 136 (135.0142) | 135@225% + 1@3.2% | 223.4% |
| Alternate: Copper Rotor | assembler | 16 (15.3097) | 15@225% + 1@69.7% | 215.3% |
| Alternate: Crystal Computer | assembler | 41 (40.5432) | 40@225% + 1@122.2% | 222.5% |
| Alternate: Electric Motor | assembler | 31 (30.9981) | 30@225% + 1@224.6% | 225.0% |
| Alternate: Encased Industrial Pipe | assembler | 133 (132.8794) | 132@225% + 1@197.9% | 224.8% |
| Alternate: Fused Quickwire | assembler | 246 (245.8054) | 245@225% + 1@181.2% | 224.8% |
| Alternate: Silicon Circuit Board | assembler | 218 (217.0271) | 217@225% + 1@6.1% | 224.0% |
| Alternate: Steel Rotor | assembler | 62 (61.7969) | 61@225% + 1@179.3% | 224.3% |
| Alternate: Steeled Frame | assembler | 160 (159.6392) | 159@225% + 1@143.8% | 224.5% |
| Alternate: Stitched Iron Plate | assembler | 81 (80.4643) | 80@225% + 1@104.5% | 223.5% |
| Assembly Director System | assembler | 77 (76.5669) | 76@225% + 1@127.5% | 223.7% |
| Automated Wiring | assembler | 230 (229.7006) | 229@225% + 1@157.6% | 224.7% |
| Electromagnetic Control Rod | assembler | 100 (99.2388) | 99@225% + 1@53.7% | 223.3% |
| Encased Plutonium Cell | assembler | 34 (33.6000) | 33@225% + 1@135% | 222.4% |
| Heat Sink | assembler | 29 (28.8000) | 28@225% + 1@180% | 223.4% |
| Magnetic Field Generator | assembler | 43 (42.9630) | 42@225% + 1@216.7% | 224.8% |
| Pressure Conversion Cube | assembler | 18 (17.9383) | 17@225% + 1@211.1% | 224.2% |
| Smart Plating | assembler | 67 (66.6667) | 66@225% + 1@150% | 223.9% |
| Stator | assembler | 242 (241.3048) | 241@225% + 1@68.6% | 224.4% |
| Versatile Framework | assembler | 6 (5.9079) | 5@225% + 1@204.3% | 221.5% |
| Alternate: Cooling Device | blender | 48 (48.0000) | 48@75% | 75.0% |
| Alternate: Diluted Fuel | blender | 268 (267.1045) | 267@75% + 1@7.8% | 74.7% |
| Alternate: Heat-Fused Frame | blender | 45 (44.6049) | 44@75% + 1@45.4% | 74.3% |
| Alternate: Nitro Rocket Fuel | blender | 29 (28.7279) | 28@75% + 1@54.6% | 74.3% |
| Alternate: Turbo Blend Fuel | blender | 148 (147.4757) | 147@75% + 1@35.7% | 74.7% |
| Nitric Acid | blender | 81 (80.3265) | 80@75% + 1@24.5% | 74.4% |
| Non-Fissile Uranium | blender | 68 (67.2000) | 67@75% + 1@15% | 74.1% |
| Rocket Fuel | blender | 34 (33.1278) | 33@75% + 1@9.6% | 73.1% |
| Alternate: Cast Screws | constructor | 54 (53.7369) | 53@250% + 1@184.2% | 248.8% |
| Alternate: Iron Pipe | constructor | 394 (393.7140) | 393@250% + 1@178.5% | 249.8% |
| Alternate: Iron Wire | constructor | 1,721 (1720.5967) | 1720@250% + 1@149.2% | 249.9% |
| Cable | constructor | 345 (344.5509) | 344@250% + 1@137.7% | 249.7% |
| Copper Powder | constructor | 48 (48.0000) | 48@250% | 250.0% |
| Empty Canister | constructor | 24 (23.4074) | 23@250% + 1@101.9% | 243.8% |
| Empty Fluid Tank | constructor | 2 (1.6578) | 1@250% + 1@164.4% | 207.2% |
| Ficsite Trigon | constructor | 20 (19.3333) | 19@250% + 1@83.3% | 241.7% |
| Iron Plate | constructor | 140 (139.9407) | 139@250% + 1@235.2% | 249.9% |
| Reanimated SAM | constructor | 34 (34.0000) | 34@250% | 250.0% |
| Bauxite (Caterium) | converter | 179 (178.7751) | 178@25% + 1@19.4% | 25.0% |
| Bauxite (Copper) | converter | 71 (70.1812) | 70@25% + 1@4.5% | 24.7% |
| Coal (Iron) | converter | 41 (40.8604) | 40@25% + 1@21.5% | 24.9% |
| Coal (Limestone) | converter | 341 (340.6050) | 340@25% + 1@15.1% | 25.0% |
| Excited Photonic Matter | converter | 205 (205.0000) | 205@25% | 25.0% |
| Ficsite Ingot (Aluminum) | converter | 65 (64.4444) | 64@25% + 1@11.1% | 24.8% |
| Sulfur (Iron) | converter | 3 (2.9115) | 2@25% + 1@22.8% | 24.3% |
| Time Crystal | converter | 1,756 (1755.5556) | 1755@25% + 1@13.9% | 25.0% |
| Alternate: Compacted Steel Ingot | foundry | 137 (136.4377) | 136@225% + 1@98.5% | 224.1% |
| Alternate: Molded Beam | foundry | 12 (11.3698) | 11@225% + 1@83.2% | 213.2% |
| Rocket Fuel Power | fuel_generator | 549 (548.7817) | 548@250% + 1@195.4% | 249.9% |
| Geothermal Power (Impure) | geothermal_generator | 9 (9.0000) | 9@100% | 100.0% |
| Geothermal Power (Normal) | geothermal_generator | 13 (13.0000) | 13@100% | 100.0% |
| Geothermal Power (Pure) | geothermal_generator | 9 (9.0000) | 9@100% | 100.0% |
| Adaptive Control Unit | manufacturer | 259 (258.4132) | 258@100% + 1@41.3% | 99.8% |
| Alternate: Caterium Computer | manufacturer | 291 (290.3807) | 290@100% + 1@38.1% | 99.8% |
| Alternate: Classic Battery | manufacturer | 76 (75.2911) | 75@100% + 1@29.1% | 99.1% |
| Alternate: Flexible Framework | manufacturer | 24 (23.3603) | 23@100% + 1@36% | 97.3% |
| Alternate: Heavy Encased Frame | manufacturer | 128 (127.5642) | 127@100% + 1@56.4% | 99.7% |
| Alternate: Infused Uranium Cell | manufacturer | 84 (84.0000) | 84@100% | 100.0% |
| Alternate: Insulated Crystal Oscillator | manufacturer | 277 (276.4702) | 276@100% + 1@47% | 99.8% |
| Alternate: Super-State Computer | manufacturer | 95 (94.1139) | 94@100% + 1@11.4% | 99.1% |
| Alternate: Turbo Electric Motor | manufacturer | 14 (13.9654) | 13@100% + 1@96.5% | 99.8% |
| Alternate: Turbo Pressure Motor | manufacturer | 6 (5.5259) | 5@100% + 1@52.6% | 92.1% |
| Alternate: Uranium Fuel Unit | manufacturer | 84 (84.0000) | 84@100% | 100.0% |
| Ballistic Warp Drive (4 sloops) | manufacturer | 24 (24.0000) | 24@250% | 250.0% |
| Modular Engine | manufacturer | 150 (150.0000) | 150@100% | 100.0% |
| Plutonium Fuel Rod | manufacturer | 51 (50.4000) | 50@100% + 1@40% | 98.8% |
| Radio Control Unit | manufacturer | 80 (79.4222) | 79@100% + 1@42.2% | 99.3% |
| Singularity Cell | manufacturer | 30 (30.0000) | 30@100% | 100.0% |
| Thermal Propulsion Rocket | manufacturer | 60 (60.0000) | 60@100% | 100.0% |
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
| Limestone (Impure) Mk.3 | miner_mk3 | 15 (15.0000) | 15@250% | 250.0% |
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
| Nuclear Power (Uranium) | nuclear_power_plant | 101 (100.8000) | 100@250% + 1@200% | 249.5% |
| Crude Oil (Impure) | oil_extractor | 10 (10.0000) | 10@250% | 250.0% |
| Crude Oil (Normal) | oil_extractor | 12 (12.0000) | 12@250% | 250.0% |
| Crude Oil (Pure) | oil_extractor | 8 (8.0000) | 8@250% | 250.0% |
| Packaged Nitrogen Gas | packager | 2 (1.6578) | 1@250% + 1@164.4% | 207.2% |
| Packaged Turbofuel | packager | 71 (70.2222) | 70@250% + 1@55.6% | 247.3% |
| AI Expansion Server | quantum_encoder | 67 (66.6667) | 66@25% + 1@16.7% | 24.9% |
| AI Expansion Server (2 sloops) | quantum_encoder | 1 (1.0000) | 1@250% | 250.0% |
| AI Expansion Server (3 sloops) | quantum_encoder | 2 (2.0000) | 2@250% | 250.0% |
| Neural-Quantum Processor | quantum_encoder | 129 (128.8889) | 128@25% + 1@22.2% | 25.0% |
| Superposition Oscillator | quantum_encoder | 174 (173.3333) | 173@25% + 1@8.3% | 24.9% |
| Alternate: Electrode Aluminum Scrap | refinery | 106 (105.4330) | 105@125% + 1@54.1% | 124.3% |
| Alternate: Heavy Oil Residue | refinery | 336 (336.0000) | 336@125% | 125.0% |
| Alternate: Pure Caterium Ingot | refinery | 277 (276.5311) | 276@125% + 1@66.4% | 124.8% |
| Alternate: Pure Copper Ingot | refinery | 1,800 (1799.5651) | 1799@125% + 1@70.6% | 125.0% |
| Alternate: Pure Iron Ingot | refinery | 2,024 (2023.0398) | 2023@125% + 1@5% | 124.9% |
| Alternate: Pure Quartz Crystal | refinery | 79 (78.9915) | 78@125% + 1@123.9% | 125.0% |
| Alternate: Recycled Plastic | refinery | 191 (190.7474) | 190@125% + 1@93.4% | 124.8% |
| Alternate: Recycled Rubber | refinery | 23 (22.7977) | 22@125% + 1@99.7% | 123.9% |
| Alternate: Recycled Rubber | refinery | 160 (159.5138) | 159@150% + 1@77.1% | 149.5% |
| Alternate: Sloppy Alumina | refinery | 80 (79.0748) | 79@125% + 1@9.3% | 123.6% |
| Alternate: Steamed Copper Sheet | refinery | 808 (807.7958) | 807@125% + 1@99.5% | 125.0% |
| Alternate: Wet Concrete | refinery | 182 (181.6915) | 181@125% + 1@86.4% | 124.8% |
| Petroleum Coke | refinery | 70 (69.3075) | 69@125% + 1@38.4% | 123.8% |
| Residual Rubber | refinery | 168 (168.0000) | 168@125% | 125.0% |
| Sulfuric Acid | refinery | 13 (12.0960) | 12@125% + 1@12% | 116.3% |
| Turbofuel | refinery | 2 (1.0477) | 1@125% + 1@6% | 65.5% |
| Central Nitrogen Gas Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Crater Lakes Oil Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Northern Nitrogen Gas Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Northwestern Nitrogen Gas Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Southeastern Nitrogen Gas Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Southern Nitrogen Gas Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Southwestern Nitrogen Gas Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Spire Coast Oil Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Swamp Oil Well | resource_well_pressurizer | 1 (1.0000) | 1@250% | 250.0% |
| Alternate: Pure Aluminum Ingot | smelter | 264 (263.5825) | 263@250% + 1@145.6% | 249.6% |
| Water Extraction | water_extractor | 1,082 (1081.6700) | 1081@175% + 1@117.3% | 174.9% |

---

# Per item breakdown

For every item this plan produces, the recipes that make it — with the plan's whole-machine count, clock, sloop grade, and the share of the item's total that each recipe supplies.

## Water — 241,744.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Water Extraction | water_extractor | 1,082 | 174.9% | — | 227,150.7 | 94.0% |
| Alternate: Electrode Aluminum Scrap | refinery | 106 | 124.3% | — | 13,838.1 | 5.7% |
| Non-Fissile Uranium | blender | 68 | 74.1% | — | 756.0 | 0.3% |

## Iron Ingot — 164,372.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Iron Ingot | refinery | 2,024 | 124.9% | — | 164,372.0 | 100.0% |

## Wire — 96,783.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Iron Wire | constructor | 1,721 | 249.9% | — | 96,783.6 | 100.0% |

## Iron Ore — 92,100.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Iron Ore (Pure) Mk.3 | miner_mk3 | 46 | 250.0% | — | 55,200.0 | 59.9% |
| Iron Ore (Normal) Mk.3 | miner_mk3 | 42 | 250.0% | — | 25,200.0 | 27.4% |
| Iron Ore (Impure) Mk.3 | miner_mk3 | 39 | 250.0% | — | 11,700.0 | 12.7% |

## Copper Ingot — 84,354.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Copper Ingot | refinery | 1,800 | 125.0% | — | 84,354.6 | 100.0% |

## Limestone — 69,300.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Limestone (Pure) Mk.3 | miner_mk3 | 29 | 250.0% | — | 34,800.0 | 50.2% |
| Limestone (Normal) Mk.3 | miner_mk3 | 50 | 250.0% | — | 30,000.0 | 43.3% |
| Limestone (Impure) Mk.3 | miner_mk3 | 15 | 250.0% | — | 4,500.0 | 6.5% |

## Coal — 53,744.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Coal (Pure) Mk.3 | miner_mk3 | 16 | 250.0% | — | 19,200.0 | 35.7% |
| Coal (Normal) Mk.3 | miner_mk3 | 31 | 250.0% | — | 18,600.0 | 34.6% |
| Coal (Limestone) | converter | 341 | 25.0% | — | 10,218.2 | 19.0% |
| Coal (Impure) Mk.3 | miner_mk3 | 15 | 250.0% | — | 4,500.0 | 8.4% |
| Coal (Iron) | converter | 41 | 24.9% | — | 1,225.8 | 2.3% |

## Quickwire — 49,775.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Fused Quickwire | assembler | 246 | 224.8% | — | 49,775.6 | 100.0% |

## Aluminum Scrap — 39,537.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Electrode Aluminum Scrap | refinery | 106 | 124.3% | — | 39,537.4 | 100.0% |

## Copper Ore — 36,900.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Copper Ore (Normal) Mk.3 | miner_mk3 | 29 | 250.0% | — | 17,400.0 | 47.2% |
| Copper Ore (Pure) Mk.3 | miner_mk3 | 13 | 250.0% | — | 15,600.0 | 42.3% |
| Copper Ore (Impure) Mk.3 | miner_mk3 | 13 | 250.0% | — | 3,900.0 | 10.6% |

## Cable — 25,841.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Cable | constructor | 345 | 249.7% | — | 25,841.3 | 100.0% |

## Steel Pipe — 24,607.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Iron Pipe | constructor | 394 | 249.8% | — | 24,607.1 | 100.0% |

## Alumina Solution — 23,722.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Sloppy Alumina | refinery | 80 | 123.6% | — | 23,722.4 | 100.0% |

## Copper Sheet — 22,719.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Steamed Copper Sheet | refinery | 808 | 125.0% | — | 22,719.3 | 100.0% |

## Rubber — 20,266.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Recycled Rubber | refinery | 160 | 149.5% | — | 14,356.2 | 70.8% |
| Residual Rubber | refinery | 168 | 125.0% | — | 4,200.0 | 20.7% |
| Alternate: Recycled Rubber | refinery | 23 | 123.9% | — | 1,709.8 | 8.4% |

## Fuel — 20,032.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Diluted Fuel | blender | 268 | 74.7% | — | 20,032.8 | 100.0% |

## Aluminum Ingot — 19,768.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Aluminum Ingot | smelter | 264 | 249.6% | — | 19,768.7 | 100.0% |

## Bauxite — 19,768.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Bauxite (Pure) Mk.3 | miner_mk3 | 6 | 250.0% | — | 7,200.0 | 36.4% |
| Bauxite (Caterium) | converter | 179 | 25.0% | — | 5,363.3 | 27.1% |
| Bauxite (Normal) Mk.3 | miner_mk3 | 6 | 250.0% | — | 3,600.0 | 18.2% |
| Bauxite (Copper) | converter | 71 | 24.7% | — | 2,105.4 | 10.7% |
| Bauxite (Impure) Mk.3 | miner_mk3 | 5 | 250.0% | — | 1,500.0 | 7.6% |

## Concrete — 18,169.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Wet Concrete | refinery | 182 | 124.8% | — | 18,169.1 | 100.0% |

## Heavy Oil Residue — 16,800.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heavy Oil Residue | refinery | 336 | 125.0% | — | 16,800.0 | 100.0% |

## Silica — 15,948.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Cheap Silica | assembler | 136 | 223.4% | — | 15,948.6 | 100.0% |

## Caterium Ore — 15,000.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Caterium Ore (Pure) Mk.3 | miner_mk3 | 8 | 250.0% | — | 9,600.0 | 64.0% |
| Caterium Ore (Normal) Mk.3 | miner_mk3 | 9 | 250.0% | — | 5,400.0 | 36.0% |

## Plastic — 14,306.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Recycled Plastic | refinery | 191 | 124.8% | — | 14,306.1 | 100.0% |

## Raw Quartz — 13,500.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Quartz (Pure) Mk.3 | miner_mk3 | 7 | 250.0% | — | 8,400.0 | 62.2% |
| Quartz (Normal) Mk.3 | miner_mk3 | 7 | 250.0% | — | 4,200.0 | 31.1% |
| Quartz (Impure) Mk.3 | miner_mk3 | 3 | 250.0% | — | 900.0 | 6.7% |

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

## Sulfur — 10,887.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Sulfur (Pure) Mk.3 | miner_mk3 | 5 | 250.0% | — | 6,000.0 | 55.1% |
| Sulfur (Normal) Mk.3 | miner_mk3 | 5 | 250.0% | — | 3,000.0 | 27.6% |
| Sulfur (Impure) Mk.3 | miner_mk3 | 6 | 250.0% | — | 1,800.0 | 16.5% |
| Sulfur (Iron) | converter | 3 | 24.3% | — | 87.3 | 0.8% |

## Dark Matter Residue — 10,750.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Superposition Oscillator | quantum_encoder | 174 | 24.9% | — | 5,416.7 | 50.4% |
| Neural-Quantum Processor | quantum_encoder | 129 | 25.0% | — | 2,416.7 | 22.5% |
| AI Expansion Server | quantum_encoder | 67 | 24.9% | — | 1,666.7 | 15.5% |
| AI Expansion Server | quantum_encoder | 2 | 250.0% | 3 | 875.0 | 8.1% |
| AI Expansion Server | quantum_encoder | 1 | 250.0% | 2 | 375.0 | 3.5% |

## Petroleum Coke — 10,396.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Petroleum Coke | refinery | 70 | 123.8% | — | 10,396.1 | 100.0% |

## Excited Photonic Matter — 10,250.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Excited Photonic Matter | converter | 205 | 25.0% | — | 10,250.0 | 100.0% |

## SAM — 10,200.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| SAM (Normal) Mk.3 | miner_mk3 | 6 | 250.0% | — | 3,600.0 | 35.3% |
| SAM (Pure) Mk.3 | miner_mk3 | 3 | 250.0% | — | 3,600.0 | 35.3% |
| SAM (Impure) Mk.3 | miner_mk3 | 10 | 250.0% | — | 3,000.0 | 29.4% |

## Polymer Resin — 8,400.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heavy Oil Residue | refinery | 336 | 125.0% | — | 8,400.0 | 100.0% |

## Alclad Aluminum Sheet — 8,332.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alclad Aluminum Sheet | assembler | 124 | 224.0% | — | 8,332.8 | 100.0% |

## Iron Plate — 6,997.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Iron Plate | constructor | 140 | 249.9% | — | 6,997.0 | 100.0% |

## Screws — 6,717.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Cast Screws | constructor | 54 | 248.8% | — | 6,717.1 | 100.0% |

## Circuit Board — 6,103.9/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Silicon Circuit Board | assembler | 218 | 224.0% | — | 6,103.9 | 100.0% |

## Copper Powder — 6,000.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Copper Powder | constructor | 48 | 250.0% | — | 6,000.0 | 100.0% |

## Rocket Fuel — 5,716.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Nitro Rocket Fuel | blender | 29 | 74.3% | — | 3,231.9 | 56.5% |
| Rocket Fuel | blender | 34 | 73.1% | — | 2,484.6 | 43.5% |

## Diamonds — 5,266.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Turbo Diamonds | accelerator | 352 | 24.9% | — | 5,266.7 | 100.0% |

## Quartz Crystal — 5,183.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Quartz Crystal | refinery | 79 | 125.0% | — | 5,183.8 | 100.0% |

## Turbofuel — 5,001.9/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Turbo Blend Fuel | blender | 148 | 74.7% | — | 4,977.3 | 99.5% |
| Turbofuel | refinery | 2 | 65.5% | — | 24.6 | 0.5% |

## Dark Matter Crystal — 4,300.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Dark Matter Trap | accelerator | 287 | 25.0% | — | 4,300.0 | 100.0% |

## Caterium Ingot — 4,148.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Caterium Ingot | refinery | 277 | 124.8% | — | 4,148.0 | 100.0% |

## Empty Canister — 3,511.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Empty Canister | constructor | 24 | 243.8% | — | 3,511.1 | 100.0% |

## Packaged Turbofuel — 3,511.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Packaged Turbofuel | packager | 71 | 247.3% | — | 3,511.1 | 100.0% |

## Aluminum Casing — 3,176.9/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Alclad Casing | assembler | 13 | 217.2% | — | 3,176.9 | 100.0% |

## Steel Ingot — 3,069.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Compacted Steel Ingot | foundry | 137 | 224.1% | — | 3,069.8 | 100.0% |

## Stator — 2,714.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Stator | assembler | 242 | 224.4% | — | 2,714.7 | 100.0% |

## Time Crystal — 2,633.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Time Crystal | converter | 1,756 | 25.0% | — | 2,633.3 | 100.0% |

## Reanimated SAM — 2,550.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Reanimated SAM | constructor | 34 | 250.0% | — | 2,550.0 | 100.0% |

## Non-Fissile Uranium — 2,520.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Non-Fissile Uranium | blender | 68 | 74.1% | — | 2,520.0 | 100.0% |

## Uranium Waste — 2,520.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Nuclear Power (Uranium) | nuclear_power_plant | 101 | 249.5% | — | 2,520.0 | 100.0% |

## Battery — 2,258.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Classic Battery | manufacturer | 76 | 99.1% | — | 2,258.7 | 100.0% |

## Uranium — 2,100.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Uranium (Normal) Mk.3 | miner_mk3 | 2 | 250.0% | — | 1,200.0 | 57.1% |
| Uranium (Impure) Mk.3 | miner_mk3 | 3 | 250.0% | — | 900.0 | 42.9% |

## Nitric Acid — 1,807.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Nitric Acid | blender | 81 | 74.4% | — | 1,807.3 | 100.0% |

## Encased Uranium Cell — 1,680.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Infused Uranium Cell | manufacturer | 84 | 100.0% | — | 1,680.0 | 100.0% |

## Ficsite Trigon — 1,450.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Ficsite Trigon | constructor | 20 | 241.7% | — | 1,450.0 | 100.0% |

## AI Limiter — 1,411.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| AI Limiter | assembler | 126 | 224.1% | — | 1,411.5 | 100.0% |

## Computer — 1,393.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Caterium Computer | manufacturer | 291 | 99.8% | — | 1,088.9 | 78.2% |
| Alternate: Crystal Computer | assembler | 41 | 222.5% | — | 304.1 | 21.8% |

## Automated Wiring — 1,292.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Automated Wiring | assembler | 230 | 224.7% | — | 1,292.1 | 100.0% |

## Encased Industrial Beam — 1,195.9/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Encased Industrial Pipe | assembler | 133 | 224.8% | — | 1,195.9 | 100.0% |

## Steel Beam — 1,151.2/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Molded Beam | foundry | 12 | 213.2% | — | 1,151.2 | 100.0% |

## Rotor — 1,082.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Steel Rotor | assembler | 62 | 224.3% | — | 695.2 | 64.2% |
| Alternate: Copper Rotor | assembler | 16 | 215.3% | — | 387.5 | 35.8% |

## Modular Frame — 1,077.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Steeled Frame | assembler | 160 | 224.5% | — | 1,077.6 | 100.0% |

## Reinforced Iron Plate — 1,018.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Stitched Iron Plate | assembler | 81 | 223.5% | — | 1,018.4 | 100.0% |

## Electromagnetic Control Rod — 893.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Electromagnetic Control Rod | assembler | 100 | 223.3% | — | 893.1 | 100.0% |

## Compacted Coal — 787.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Nitro Rocket Fuel | blender | 29 | 74.3% | — | 538.6 | 68.4% |
| Rocket Fuel | blender | 34 | 73.1% | — | 248.5 | 31.6% |

## Plutonium Pellet — 756.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Plutonium Pellet | accelerator | 101 | 25.0% | — | 756.0 | 100.0% |

## Sulfuric Acid — 756.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Sulfuric Acid | refinery | 13 | 116.3% | — | 756.0 | 100.0% |

## Motor — 523.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Electric Motor | assembler | 31 | 225.0% | — | 523.1 | 100.0% |

## Crystal Oscillator — 518.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Insulated Crystal Oscillator | manufacturer | 277 | 99.8% | — | 518.4 | 100.0% |

## Heat Sink — 486.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Heat Sink | assembler | 29 | 223.4% | — | 486.0 | 100.0% |

## Ficsite Ingot — 483.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Ficsite Ingot (Aluminum) | converter | 65 | 24.8% | — | 483.3 | 100.0% |

## Encased Plutonium Cell — 378.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Encased Plutonium Cell | assembler | 34 | 222.4% | — | 378.0 | 100.0% |

## Heavy Modular Frame — 358.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heavy Encased Frame | manufacturer | 128 | 99.7% | — | 358.8 | 100.0% |

## Singularity Cell — 300.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Singularity Cell | manufacturer | 30 | 100.0% | — | 300.0 | 100.0% |

## Smart Plating — 300.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Smart Plating | assembler | 67 | 223.9% | — | 300.0 | 100.0% |

## Adaptive Control Unit — 258.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Adaptive Control Unit | manufacturer | 259 | 99.8% | — | 258.4 | 100.0% |

## Empty Fluid Tank — 248.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Empty Fluid Tank | constructor | 2 | 207.2% | — | 248.7 | 100.0% |

## Packaged Nitrogen Gas — 248.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Packaged Nitrogen Gas | packager | 2 | 207.2% | — | 248.7 | 100.0% |

## Versatile Framework — 241.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Flexible Framework | manufacturer | 24 | 97.3% | — | 175.2 | 72.5% |
| Versatile Framework | assembler | 6 | 221.5% | — | 66.5 | 27.5% |

## Supercomputer — 225.9/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Super-State Computer | manufacturer | 95 | 99.1% | — | 225.9 | 100.0% |

## Superposition Oscillator — 216.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Superposition Oscillator | quantum_encoder | 174 | 24.9% | — | 216.7 | 100.0% |

## Radio Control Unit — 198.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Radio Control Unit | manufacturer | 80 | 99.3% | — | 198.6 | 100.0% |

## Cooling System — 180.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Cooling Device | blender | 48 | 75.0% | — | 180.0 | 100.0% |

## Modular Engine — 150.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Modular Engine | manufacturer | 150 | 100.0% | — | 150.0 | 100.0% |

## Assembly Director System — 129.2/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Assembly Director System | assembler | 77 | 223.7% | — | 129.2 | 100.0% |

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

## Fused Modular Frame — 100.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heat-Fused Frame | blender | 45 | 74.3% | — | 100.4 | 100.0% |

## Magnetic Field Generator — 96.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Magnetic Field Generator | assembler | 43 | 224.8% | — | 96.7 | 100.0% |

## Neural-Quantum Processor — 96.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Neural-Quantum Processor | quantum_encoder | 129 | 25.0% | — | 96.7 | 100.0% |

## Thermal Propulsion Rocket — 60.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Thermal Propulsion Rocket | manufacturer | 60 | 100.0% | — | 60.0 | 100.0% |

## Turbo Motor — 60.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Turbo Electric Motor | manufacturer | 14 | 99.8% | — | 39.3 | 65.5% |
| Alternate: Turbo Pressure Motor | manufacturer | 6 | 92.1% | — | 20.7 | 34.5% |

## Uranium Fuel Rod — 50.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Uranium Fuel Unit | manufacturer | 84 | 100.0% | — | 50.4 | 100.0% |

## Pressure Conversion Cube — 40.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Pressure Conversion Cube | assembler | 18 | 224.2% | — | 40.4 | 100.0% |

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

## Refinery — 6,319 machines · 255,974 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Pure Iron Ingot | 2,024 | 124.9% | — | Iron Ore 88,508.0 + Water 50,576.0 | Iron Ingot 164,372.0 |
| Alternate: Pure Copper Ingot | 1,800 | 125.0% | — | Copper Ore 33,741.8 + Water 22,494.6 | Copper Ingot 84,354.6 |
| Alternate: Steamed Copper Sheet | 808 | 125.0% | — | Copper Ingot 22,719.3 + Water 22,719.3 | Copper Sheet 22,719.3 |
| Alternate: Heavy Oil Residue | 336 | 125.0% | — | Crude Oil 12,600.0 | Heavy Oil Residue 16,800.0 + Polymer Resin 8,400.0 |
| Alternate: Pure Caterium Ingot | 277 | 124.8% | — | Caterium Ore 8,295.9 + Water 8,295.9 | Caterium Ingot 4,148.0 |
| Alternate: Recycled Plastic | 191 | 124.8% | — | Fuel 7,153.0 + Rubber 7,153.0 | Plastic 14,306.1 |
| Alternate: Wet Concrete | 182 | 124.8% | — | Limestone 27,253.7 + Water 22,711.4 | Concrete 18,169.1 |
| Residual Rubber | 168 | 125.0% | — | Polymer Resin 8,400.0 + Water 8,400.0 | Rubber 4,200.0 |
| Alternate: Recycled Rubber | 160 | 149.5% | — | Fuel 7,178.1 + Plastic 7,178.1 | Rubber 14,356.2 |
| Alternate: Electrode Aluminum Scrap | 106 | 124.3% | — | Alumina Solution 23,722.4 + Petroleum Coke 7,907.5 | Aluminum Scrap 39,537.4 + Water 13,838.1 |
| Alternate: Sloppy Alumina | 80 | 123.6% | — | Bauxite 19,768.7 + Water 19,768.7 | Alumina Solution 23,722.4 |
| Alternate: Pure Quartz Crystal | 79 | 125.0% | — | Raw Quartz 6,664.9 + Water 3,702.7 | Quartz Crystal 5,183.8 |
| Petroleum Coke | 70 | 123.8% | — | Heavy Oil Residue 3,465.4 | Petroleum Coke 10,396.1 |
| Alternate: Recycled Rubber | 23 | 123.9% | — | Fuel 854.9 + Plastic 854.9 | Rubber 1,709.8 |
| Sulfuric Acid | 13 | 116.3% | — | Sulfur 756.0 + Water 756.0 | Sulfuric Acid 756.0 |
| Turbofuel | 2 | 65.5% | — | Compacted Coal 19.6 + Fuel 29.5 | Turbofuel 24.6 |

## Constructor — 2,782 machines · 37,311 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Iron Wire | 1,721 | 249.9% | — | Iron Ingot 53,768.6 | Wire 96,783.6 |
| Alternate: Iron Pipe | 394 | 249.8% | — | Iron Ingot 98,428.5 | Steel Pipe 24,607.1 |
| Cable | 345 | 249.7% | — | Wire 51,682.6 | Cable 25,841.3 |
| Iron Plate | 140 | 249.9% | — | Iron Ingot 10,495.6 | Iron Plate 6,997.0 |
| Alternate: Cast Screws | 54 | 248.8% | — | Iron Ingot 1,679.3 | Screws 6,717.1 |
| Copper Powder | 48 | 250.0% | — | Copper Ingot 36,000.0 | Copper Powder 6,000.0 |
| Reanimated SAM | 34 | 250.0% | — | SAM 10,200.0 | Reanimated SAM 2,550.0 |
| Empty Canister | 24 | 243.8% | — | Plastic 1,755.6 | Empty Canister 3,511.1 |
| Ficsite Trigon | 20 | 241.7% | — | Ficsite Ingot 483.3 | Ficsite Trigon 1,450.0 |
| Empty Fluid Tank | 2 | 207.2% | — | Aluminum Ingot 248.7 | Empty Fluid Tank 248.7 |

## Converter — 2,661 machines · 106,299 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Time Crystal | 1,756 | 25.0% | — | Diamonds 5,266.7 | Time Crystal 2,633.3 |
| Coal (Limestone) | 341 | 25.0% | — | Limestone 30,654.5 + Reanimated SAM 851.5 | Coal 10,218.2 |
| Excited Photonic Matter | 205 | 25.0% | — | — | Excited Photonic Matter 10,250.0 |
| Bauxite (Caterium) | 179 | 25.0% | — | Caterium Ore 6,704.1 + Reanimated SAM 446.9 | Bauxite 5,363.3 |
| Bauxite (Copper) | 71 | 24.7% | — | Copper Ore 3,158.2 + Reanimated SAM 175.5 | Bauxite 2,105.4 |
| Ficsite Ingot (Aluminum) | 65 | 24.8% | — | Aluminum Ingot 1,933.3 + Reanimated SAM 966.7 | Ficsite Ingot 483.3 |
| Coal (Iron) | 41 | 24.9% | — | Iron Ore 1,838.7 + Reanimated SAM 102.2 | Coal 1,225.8 |
| Sulfur (Iron) | 3 | 24.3% | — | Iron Ore 218.4 + Reanimated SAM 7.3 | Sulfur 87.3 |

## Assembler — 2,233 machines · 97,304 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Fused Quickwire | 246 | 224.8% | — | Caterium Ingot 4,148.0 + Copper Ingot 20,739.8 | Quickwire 49,775.6 |
| Stator | 242 | 224.4% | — | Steel Pipe 8,144.0 + Wire 21,717.4 | Stator 2,714.7 |
| Automated Wiring | 230 | 224.7% | — | Cable 25,841.3 + Stator 1,292.1 | Automated Wiring 1,292.1 |
| Alternate: Silicon Circuit Board | 218 | 224.0% | — | Copper Sheet 13,428.6 + Silica 13,428.6 | Circuit Board 6,103.9 |
| Alternate: Steeled Frame | 160 | 224.5% | — | Reinforced Iron Plate 718.4 + Steel Pipe 3,591.9 | Modular Frame 1,077.6 |
| Alternate: Cheap Silica | 136 | 223.4% | — | Limestone 11,391.8 + Raw Quartz 6,835.1 | Silica 15,948.6 |
| Alternate: Encased Industrial Pipe | 133 | 224.8% | — | Concrete 5,979.6 + Steel Pipe 7,175.5 | Encased Industrial Beam 1,195.9 |
| AI Limiter | 126 | 224.1% | — | Copper Sheet 7,057.7 + Quickwire 28,230.6 | AI Limiter 1,411.5 |
| Alclad Aluminum Sheet | 124 | 224.0% | — | Aluminum Ingot 8,332.8 + Copper Ingot 2,777.6 | Alclad Aluminum Sheet 8,332.8 |
| Electromagnetic Control Rod | 100 | 223.3% | — | AI Limiter 893.1 + Stator 1,339.7 | Electromagnetic Control Rod 893.1 |
| Alternate: Stitched Iron Plate | 81 | 223.5% | — | Iron Plate 3,394.6 + Wire 6,789.2 | Reinforced Iron Plate 1,018.4 |
| Assembly Director System | 77 | 223.7% | — | Adaptive Control Unit 258.4 + Supercomputer 129.2 | Assembly Director System 129.2 |
| Smart Plating | 67 | 223.9% | — | Reinforced Iron Plate 300.0 + Rotor 300.0 | Smart Plating 300.0 |
| Alternate: Steel Rotor | 62 | 224.3% | — | Steel Pipe 1,390.4 + Wire 4,171.3 | Rotor 695.2 |
| Magnetic Field Generator | 43 | 224.8% | — | Electromagnetic Control Rod 96.7 + Versatile Framework 241.7 | Magnetic Field Generator 96.7 |
| Alternate: Crystal Computer | 41 | 222.5% | — | Circuit Board 456.1 + Crystal Oscillator 152.0 | Computer 304.1 |
| Encased Plutonium Cell | 34 | 222.4% | — | Concrete 1,512.0 + Plutonium Pellet 756.0 | Encased Plutonium Cell 378.0 |
| Alternate: Electric Motor | 31 | 225.0% | — | Electromagnetic Control Rod 261.5 + Rotor 523.1 | Motor 523.1 |
| Heat Sink | 29 | 223.4% | — | Alclad Aluminum Sheet 2,430.0 + Copper Sheet 1,458.0 | Heat Sink 486.0 |
| Pressure Conversion Cube | 18 | 224.2% | — | Fused Modular Frame 40.4 + Radio Control Unit 80.7 | Pressure Conversion Cube 40.4 |
| Alternate: Copper Rotor | 16 | 215.3% | — | Copper Sheet 775.1 + Screws 6,717.1 | Rotor 387.5 |
| Alternate: Alclad Casing | 13 | 217.2% | — | Aluminum Ingot 4,235.9 + Copper Ingot 2,117.9 | Aluminum Casing 3,176.9 |
| Versatile Framework | 6 | 221.5% | — | Modular Frame 33.2 + Steel Beam 398.8 | Versatile Framework 66.5 |

## Manufacturer — 1,733 machines · 111,282 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Caterium Computer | 291 | 99.8% | — | Circuit Board 4,355.7 + Quickwire 15,245.0 + Rubber 6,533.6 | Computer 1,088.9 |
| Alternate: Insulated Crystal Oscillator | 277 | 99.8% | — | AI Limiter 518.4 + Quartz Crystal 5,183.8 + Rubber 3,628.7 | Crystal Oscillator 518.4 |
| Adaptive Control Unit | 259 | 99.8% | — | Automated Wiring 1,292.1 + Circuit Board 1,292.1 + Computer 516.8 + Heavy Modular Frame 258.4 | Adaptive Control Unit 258.4 |
| Modular Engine | 150 | 100.0% | — | Motor 300.0 + Rubber 2,250.0 + Smart Plating 300.0 | Modular Engine 150.0 |
| Alternate: Heavy Encased Frame | 128 | 99.7% | — | Concrete 2,631.0 + Encased Industrial Beam 1,195.9 + Modular Frame 956.7 + Steel Pipe 4,305.3 | Heavy Modular Frame 358.8 |
| Alternate: Super-State Computer | 95 | 99.1% | — | Battery 2,258.7 + Computer 677.6 + Electromagnetic Control Rod 225.9 + Wire 5,646.8 | Supercomputer 225.9 |
| Alternate: Infused Uranium Cell | 84 | 100.0% | — | Quickwire 6,300.0 + Silica 1,260.0 + Sulfur 2,100.0 + Uranium 2,100.0 | Encased Uranium Cell 1,680.0 |
| Alternate: Uranium Fuel Unit | 84 | 100.0% | — | Crystal Oscillator 50.4 + Electromagnetic Control Rod 168.0 + Encased Uranium Cell 1,680.0 + Rotor 168.0 | Uranium Fuel Rod 50.4 |
| Radio Control Unit | 80 | 99.3% | — | Aluminum Casing 3,176.9 + Computer 198.6 + Crystal Oscillator 99.3 | Radio Control Unit 198.6 |
| Alternate: Classic Battery | 76 | 99.1% | — | Alclad Aluminum Sheet 3,952.8 + Plastic 4,517.5 + Sulfur 3,388.1 + Wire 6,776.2 | Battery 2,258.7 |
| Thermal Propulsion Rocket | 60 | 100.0% | — | Cooling System 180.0 + Fused Modular Frame 60.0 + Modular Engine 150.0 + Turbo Motor 60.0 | Thermal Propulsion Rocket 60.0 |
| Plutonium Fuel Rod | 51 | 98.8% | — | Electromagnetic Control Rod 75.6 + Encased Plutonium Cell 378.0 + Heat Sink 126.0 + Steel Beam 226.8 | Plutonium Fuel Rod 12.6 |
| Singularity Cell | 30 | 100.0% | — | Concrete 6,000.0 + Dark Matter Crystal 600.0 + Iron Plate 3,000.0 + Nuclear Pasta 30.0 | Singularity Cell 300.0 |
| Ballistic Warp Drive | 24 | 250.0% | 4 | Dark Matter Crystal 2,400.0 + Singularity Cell 300.0 + Superposition Oscillator 120.0 + Thermal Propulsion Rocket 60.0 | Ballistic Warp Drive 120.0 |
| Alternate: Flexible Framework | 24 | 97.3% | — | Modular Frame 87.6 + Rubber 700.8 + Steel Beam 525.6 | Versatile Framework 175.2 |
| Alternate: Turbo Electric Motor | 14 | 99.8% | — | Electromagnetic Control Rod 65.5 + Motor 91.6 + Radio Control Unit 117.8 + Rotor 91.6 | Turbo Motor 39.3 |
| Alternate: Turbo Pressure Motor | 6 | 92.1% | — | Motor 41.4 + Packaged Nitrogen Gas 248.7 + Pressure Conversion Cube 10.4 + Stator 82.9 | Turbo Motor 20.7 |

## Accelerator — 980 machines · 106,341 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Turbo Diamonds | 352 | 24.9% | — | Coal 52,666.7 + Packaged Turbofuel 3,511.1 | Diamonds 5,266.7 |
| Alternate: Dark Matter Trap | 287 | 25.0% | — | Dark Matter Residue 10,750.0 + Time Crystal 2,150.0 | Dark Matter Crystal 4,300.0 |
| Nuclear Pasta | 240 | 25.0% | — | Copper Powder 6,000.0 + Pressure Conversion Cube 30.0 | Nuclear Pasta 30.0 |
| Plutonium Pellet | 101 | 25.0% | — | Non-Fissile Uranium 2,520.0 + Uranium Waste 630.0 | Plutonium Pellet 756.0 |

## Blender — 721 machines · 36,669 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Diluted Fuel | 268 | 74.7% | — | Heavy Oil Residue 10,016.4 + Water 20,032.8 | Fuel 20,032.8 |
| Alternate: Turbo Blend Fuel | 148 | 74.7% | — | Fuel 1,659.1 + Heavy Oil Residue 3,318.2 + Petroleum Coke 2,488.7 + Sulfur 2,488.7 | Turbofuel 4,977.3 |
| Nitric Acid | 81 | 74.4% | — | Iron Plate 602.4 + Nitrogen Gas 7,229.4 + Water 1,807.3 | Nitric Acid 1,807.3 |
| Non-Fissile Uranium | 68 | 74.1% | — | Nitric Acid 756.0 + Silica 1,260.0 + Sulfuric Acid 756.0 + Uranium Waste 1,890.0 | Non-Fissile Uranium 2,520.0 + Water 756.0 |
| Alternate: Cooling Device | 48 | 75.0% | — | Heat Sink 360.0 + Motor 90.0 + Nitrogen Gas 2,160.0 | Cooling System 180.0 |
| Alternate: Heat-Fused Frame | 45 | 74.3% | — | Aluminum Ingot 5,018.1 + Fuel 1,003.6 + Heavy Modular Frame 100.4 + Nitric Acid 802.9 | Fused Modular Frame 100.4 |
| Rocket Fuel | 34 | 73.1% | — | Nitric Acid 248.5 + Turbofuel 1,490.8 | Compacted Coal 248.5 + Rocket Fuel 2,484.6 |
| Alternate: Nitro Rocket Fuel | 29 | 74.3% | — | Coal 1,077.3 + Fuel 2,154.6 + Nitrogen Gas 1,615.9 + Sulfur 2,154.6 | Compacted Coal 538.6 + Rocket Fuel 3,231.9 |

## Quantum Encoder — 373 machines · 87,086 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Superposition Oscillator | 174 | 24.9% | — | Alclad Aluminum Sheet 1,950.0 + Crystal Oscillator 216.7 + Dark Matter Crystal 1,300.0 + Excited Photonic Matter 5,416.7 | Dark Matter Residue 5,416.7 + Superposition Oscillator 216.7 |
| Neural-Quantum Processor | 129 | 25.0% | — | Excited Photonic Matter 2,416.7 + Ficsite Trigon 1,450.0 + Supercomputer 96.7 + Time Crystal 483.3 | Dark Matter Residue 2,416.7 + Neural-Quantum Processor 96.7 |
| AI Expansion Server | 67 | 24.9% | — | Excited Photonic Matter 1,666.7 + Magnetic Field Generator 66.7 + Neural-Quantum Processor 66.7 + Superposition Oscillator 66.7 | AI Expansion Server 66.7 + Dark Matter Residue 1,666.7 |
| AI Expansion Server | 2 | 250.0% | 3 | Excited Photonic Matter 500.0 + Magnetic Field Generator 20.0 + Neural-Quantum Processor 20.0 + Superposition Oscillator 20.0 | AI Expansion Server 35.0 + Dark Matter Residue 875.0 |
| AI Expansion Server | 1 | 250.0% | 2 | Excited Photonic Matter 250.0 + Magnetic Field Generator 10.0 + Neural-Quantum Processor 10.0 + Superposition Oscillator 10.0 | AI Expansion Server 15.0 + Dark Matter Residue 375.0 |

## Smelter — 264 machines · 3,538 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Pure Aluminum Ingot | 264 | 249.6% | — | Aluminum Scrap 39,537.4 | Aluminum Ingot 19,768.7 |

## Foundry — 149 machines · 6,891 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Compacted Steel Ingot | 137 | 224.1% | — | Compacted Coal 767.5 + Iron Ore 1,534.9 | Steel Ingot 3,069.8 |
| Alternate: Molded Beam | 12 | 213.2% | — | Concrete 2,046.6 + Steel Ingot 3,069.8 | Steel Beam 1,151.2 |

## Packager — 73 machines · 2,402 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Packaged Turbofuel | 71 | 247.3% | — | Empty Canister 3,511.1 + Turbofuel 3,511.1 | Packaged Turbofuel 3,511.1 |
| Packaged Nitrogen Gas | 2 | 207.2% | — | Empty Fluid Tank 248.7 + Nitrogen Gas 994.7 | Packaged Nitrogen Gas 248.7 |

---

# Resource extraction

Raw-material supply: miners, water/oil extractors and pressure wells. (The high-level overview aggregates these by resource; here each node group is listed.)

## Water Extractor — 1,082 machines · 45,327 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Water Extraction | 1,082 | 174.9% | — | — | Water 227,150.7 |

## Miner Mk.3 — 429 machines · 64,821 MW

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
| Limestone (Impure) Mk.3 | 15 | 250.0% | — | — | Limestone 4,500.0 |
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

## Fuel Generator — 549 machines · **342,989 MW generated**

| Recipe | count | clock | slps | fuel /min | output |
|---|---|---:|---:|---|---|
| Rocket Fuel Power | 549 | 249.9% | — | Rocket Fuel 5,716.5 | 342,989 MW |

---

## Notes

- **Power rounding**: per-section draws are computed from the displayed whole-machine counts and sum to 969,808 MW, ~0.1% under the official 970,385 MW (the model also runs tiny sub-machine exact-balance slivers). Generation is clock-linear, so whole-machine sums reproduce the 980,089 MW exactly.
- Accelerator rows use per-recipe power draw where the spec overrides it; other machines use their machine default.
- Rates are **aggregate** at the displayed clock. Per-machine rate at that clock = aggregate ÷ `#`.
