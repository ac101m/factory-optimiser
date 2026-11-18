# Satisfactory Factory Optimiser — Build Plan

**Official optimum** — **486,073,620 pts/min** (overclock tiers 25%, 50%, 75%, 100%, 125%, 150%, 175%, 200%, 225%, 250%; Auto-solved (augmenter sweep)). All rates are per minute.

## High-level overview

| Metric | Value | Notes |
|---|---|---|
| **Sink points** | **486,073,620 pts/min** | 0 augmenter(s), 1.00x power |
| **Power load** | **928,943 MW** | what consumers actually draw |
| **Power supplied** | 938,232 MW | load x1.01 (1% reserve) |
| **Machines** | **24,620** (cap 24,576 — binding) | 142 recipe rows across 18 machine types |
| **Somersloops** | 104 / 104 | see overclock notes |
| **Sink throughput** | 383.2 items/min | one Awesome Sink covers it (1200/min cap, 30 MW) |

### Sink flows

| Sink item | pts/item | /min | pts/min | share |
|---|---:|---:|---:|---:|
| Ballistic Warp Drive | 2,895,334 | 120.0 | 347,440,080 | 71.5% |
| AI Expansion Server | 597,652 | 116.7 | 69,726,067 | 14.3% |
| Assembly Director System | 500,176 | 133.9 | 66,977,355 | 13.8% |
| Plutonium Fuel Rod | 153,184 | 12.6 | 1,930,118 | 0.4% |
| **TOTAL** | | | **486,073,620** | 100% |

---

# Production per item

Aggregate material balance across the whole plan (production includes extraction).

| Item | produced/min | consumed/min | net | destination |
|---|---:|---:|---:|---|
| Water | 244,033.5 | 244,033.5 | +0.0 | balanced |
| Iron Ingot | 164,355.9 | 164,355.9 | -0.0 | balanced |
| Wire | 97,543.8 | 97,543.8 | +0.0 | balanced |
| Iron Ore | 92,100.0 | 92,100.0 | +0.0 | balanced |
| Copper Ingot | 85,100.6 | 85,100.6 | +0.0 | balanced |
| Limestone | 69,300.0 | 69,300.0 | +0.0 | balanced |
| Coal | 53,773.0 | 53,773.0 | +0.0 | balanced |
| Quickwire | 47,872.2 | 47,872.2 | +0.0 | balanced |
| Aluminum Scrap | 39,654.0 | 39,654.0 | +0.0 | balanced |
| Copper Ore | 36,900.0 | 36,900.0 | +0.0 | balanced |
| Cable | 26,781.5 | 26,781.5 | +0.0 | balanced |
| Steel Pipe | 24,683.5 | 24,683.5 | +0.0 | balanced |
| Copper Sheet | 24,321.0 | 24,321.0 | -0.0 | balanced |
| Alumina Solution | 23,792.4 | 23,792.4 | +0.0 | balanced |
| Screws | 22,353.3 | 22,353.3 | +0.0 | balanced |
| Rubber | 21,106.6 | 21,106.6 | +0.0 | balanced |
| Fuel | 20,761.0 | 20,761.0 | -0.0 | balanced |
| Aluminum Ingot | 19,827.0 | 19,827.0 | -0.0 | balanced |
| Bauxite | 19,827.0 | 19,827.0 | -0.0 | balanced |
| Concrete | 18,327.3 | 18,327.3 | +0.0 | balanced |
| Heavy Oil Residue | 16,800.0 | 16,800.0 | +0.0 | balanced |
| Silica | 16,378.3 | 16,378.3 | -0.0 | balanced |
| Plastic | 15,120.0 | 15,120.0 | +0.0 | balanced |
| Caterium Ore | 15,000.0 | 15,000.0 | +0.0 | balanced |
| Raw Quartz | 13,500.0 | 13,500.0 | +0.0 | balanced |
| Crude Oil | 12,600.0 | 12,600.0 | +0.0 | balanced |
| Nitrogen Gas | 12,000.0 | 12,000.0 | +0.0 | balanced |
| Sulfur | 10,800.0 | 10,800.0 | -0.0 | balanced |
| Dark Matter Residue | 10,750.0 | 10,750.0 | +0.0 | balanced |
| Excited Photonic Matter | 10,250.0 | 10,250.0 | +0.0 | balanced |
| SAM | 10,200.0 | 10,200.0 | +0.0 | balanced |
| Petroleum Coke | 10,196.3 | 10,196.3 | +0.0 | balanced |
| Alclad Aluminum Sheet | 8,415.0 | 8,415.0 | +0.0 | balanced |
| Polymer Resin | 8,400.0 | 8,400.0 | +0.0 | balanced |
| Iron Plate | 7,044.7 | 7,044.7 | +0.0 | balanced |
| Circuit Board | 6,299.2 | 6,299.2 | +0.0 | balanced |
| Copper Powder | 6,000.0 | 6,000.0 | -0.0 | balanced |
| Diamonds | 5,266.7 | 5,266.7 | +0.0 | balanced |
| Quartz Crystal | 5,040.6 | 5,040.6 | +0.0 | balanced |
| Rocket Fuel | 5,018.9 | 5,018.9 | +0.0 | balanced |
| Turbofuel | 4,531.1 | 4,531.1 | +0.0 | balanced |
| Dark Matter Crystal | 4,300.0 | 4,300.0 | +0.0 | balanced |
| Caterium Ingot | 3,989.3 | 3,989.3 | +0.0 | balanced |
| Empty Canister | 3,511.1 | 3,511.1 | +0.0 | balanced |
| Packaged Turbofuel | 3,511.1 | 3,511.1 | +0.0 | balanced |
| Stator | 3,046.7 | 3,046.7 | +0.0 | balanced |
| Aluminum Casing | 3,041.7 | 3,041.7 | +0.0 | balanced |
| Steel Ingot | 2,892.6 | 2,892.6 | +0.0 | balanced |
| Time Crystal | 2,633.3 | 2,633.3 | +0.0 | balanced |
| Reanimated SAM | 2,550.0 | 2,550.0 | +0.0 | balanced |
| Non-Fissile Uranium | 2,520.0 | 2,520.0 | +0.0 | balanced |
| Uranium Waste | 2,520.0 | 2,520.0 | +0.0 | balanced |
| Battery | 2,305.7 | 2,305.7 | +0.0 | balanced |
| Uranium | 2,100.0 | 2,100.0 | +0.0 | balanced |
| Nitric Acid | 1,745.8 | 1,745.8 | +0.0 | balanced |
| Encased Uranium Cell | 1,680.0 | 1,680.0 | +0.0 | balanced |
| Ficsite Trigon | 1,450.0 | 1,450.0 | +0.0 | balanced |
| Computer | 1,417.5 | 1,417.5 | -0.0 | balanced |
| Automated Wiring | 1,339.1 | 1,339.1 | +0.0 | balanced |
| Rotor | 1,289.6 | 1,289.6 | +0.0 | balanced |
| AI Limiter | 1,285.1 | 1,285.1 | +0.0 | balanced |
| Encased Industrial Beam | 1,234.3 | 1,234.3 | +0.0 | balanced |
| Modular Frame | 1,108.3 | 1,108.3 | +0.0 | balanced |
| Steel Beam | 1,084.7 | 1,084.7 | -0.0 | balanced |
| Reinforced Iron Plate | 1,038.8 | 1,038.8 | +0.0 | balanced |
| Electromagnetic Control Rod | 781.0 | 781.0 | +0.0 | balanced |
| Sulfuric Acid | 763.2 | 763.2 | +0.0 | balanced |
| Plutonium Pellet | 756.0 | 756.0 | +0.0 | balanced |
| Compacted Coal | 723.1 | 723.1 | +0.0 | balanced |
| Motor | 521.7 | 521.7 | +0.0 | balanced |
| Crystal Oscillator | 504.1 | 504.1 | +0.0 | balanced |
| Heat Sink | 486.0 | 486.0 | +0.0 | balanced |
| Ficsite Ingot | 483.3 | 483.3 | +0.0 | balanced |
| Encased Plutonium Cell | 378.0 | 378.0 | +0.0 | balanced |
| Heavy Modular Frame | 370.3 | 370.3 | +0.0 | balanced |
| Singularity Cell | 300.0 | 300.0 | +0.0 | balanced |
| Smart Plating | 300.0 | 300.0 | +0.0 | balanced |
| Empty Fluid Tank | 299.4 | 299.4 | +0.0 | balanced |
| Packaged Nitrogen Gas | 299.4 | 299.4 | +0.0 | balanced |
| Adaptive Control Unit | 267.8 | 267.8 | +0.0 | balanced |
| Versatile Framework | 241.7 | 241.7 | +0.0 | balanced |
| Supercomputer | 230.6 | 230.6 | -0.0 | balanced |
| Superposition Oscillator | 216.7 | 216.7 | -0.0 | balanced |
| Radio Control Unit | 190.1 | 190.1 | +0.0 | balanced |
| Cooling System | 180.0 | 180.0 | +0.0 | balanced |
| Modular Engine | 150.0 | 150.0 | +0.0 | balanced |
| Assembly Director System | 133.9 | 0.0 | +133.9 | → Awesome Sink (133.9/min) |
| Ballistic Warp Drive | 120.0 | 0.0 | +120.0 | → Awesome Sink (120.0/min) |
| AI Expansion Server | 116.7 | 0.0 | +116.7 | → Awesome Sink (116.7/min) |
| Fused Modular Frame | 102.5 | 102.5 | +0.0 | balanced |
| Magnetic Field Generator | 96.7 | 96.7 | +0.0 | balanced |
| Neural-Quantum Processor | 96.7 | 96.7 | +0.0 | balanced |
| Thermal Propulsion Rocket | 60.0 | 60.0 | +0.0 | balanced |
| Turbo Motor | 60.0 | 60.0 | +0.0 | balanced |
| Uranium Fuel Rod | 50.4 | 50.4 | +0.0 | balanced |
| Pressure Conversion Cube | 42.5 | 42.5 | -0.0 | balanced |
| Nuclear Pasta | 30.0 | 30.0 | +0.0 | balanced |
| Plutonium Fuel Rod | 12.6 | 0.0 | +12.6 | → Awesome Sink (12.6/min) |

---

# All used recipes

101 production recipe rows from 98 distinct recipes (rows repeat a recipe when sloop grades or clocks differ); extractors are listed in the Resource extraction table underneath. `count` is the machines to build, with the raw fractional count in brackets; `clock` shows how to split that build into whole machines at the clock tier plus one trimmed remainder (e.g. `10@100% + 1@50%`); `equivalent all-machine clock` is the single uniform clock that reproduces the same throughput. A row whose equivalent clock sits below the tier is an exact-balance remnant, not a choice.

| Recipe | machine | count | clock | equivalent all-machine clock |
|---|---|---:|---:|---:|
| Alternate: Dark Matter Trap | accelerator | 287 (286.6667) | 286@25% + 1@16.7% | 25.0% |
| Alternate: Turbo Diamonds | accelerator | 352 (351.1111) | 351@25% + 1@2.8% | 24.9% |
| Nuclear Pasta | accelerator | 240 (240.0000) | 240@25% | 25.0% |
| Plutonium Pellet | accelerator | 101 (100.8000) | 100@25% + 1@20% | 25.0% |
| AI Limiter | assembler | 147 (146.8680) | 146@175% + 1@151.9% | 174.8% |
| Alclad Aluminum Sheet | assembler | 161 (160.2867) | 160@175% + 1@50.2% | 174.2% |
| Alternate: Alclad Casing | assembler | 16 (15.4500) | 15@175% + 1@78.8% | 169.0% |
| Alternate: Cheap Silica | assembler | 179 (178.2676) | 178@175% + 1@46.8% | 174.3% |
| Alternate: Coated Iron Plate | assembler | 23 (22.8307) | 22@175% + 1@145.4% | 173.7% |
| Alternate: Copper Rotor | assembler | 66 (65.5040) | 65@175% + 1@88.2% | 173.7% |
| Alternate: Crystal Computer | assembler | 49 (48.6634) | 48@175% + 1@116.1% | 173.8% |
| Alternate: Electric Motor | assembler | 24 (23.1277) | 23@175% + 1@22.3% | 168.6% |
| Alternate: Encased Industrial Pipe | assembler | 177 (176.3277) | 176@175% + 1@57.4% | 174.3% |
| Alternate: Fused Quickwire | assembler | 304 (303.9502) | 303@175% + 1@166.3% | 175.0% |
| Alternate: Silicon Circuit Board | assembler | 288 (287.9654) | 287@175% + 1@168.9% | 175.0% |
| Alternate: Steeled Frame | assembler | 212 (211.0988) | 211@175% + 1@17.3% | 174.3% |
| Alternate: Stitched Iron Plate | assembler | 106 (105.5335) | 105@175% + 1@93.4% | 174.2% |
| Assembly Director System | assembler | 103 (102.0248) | 102@175% + 1@4.3% | 173.3% |
| Automated Wiring | assembler | 307 (306.0745) | 306@175% + 1@13% | 174.5% |
| Electromagnetic Control Rod | assembler | 112 (111.5770) | 111@175% + 1@101% | 174.3% |
| Encased Plutonium Cell | assembler | 44 (43.2000) | 43@175% + 1@35% | 171.8% |
| Heat Sink | assembler | 38 (37.0286) | 37@175% + 1@5% | 170.5% |
| Magnetic Field Generator | assembler | 56 (55.2381) | 55@175% + 1@41.7% | 172.6% |
| Motor | assembler | 25 (24.9296) | 24@175% + 1@162.7% | 174.5% |
| Pressure Conversion Cube | assembler | 25 (24.2703) | 24@175% + 1@47.3% | 169.9% |
| Smart Plating | assembler | 86 (85.7143) | 85@175% + 1@125% | 174.4% |
| Stator | assembler | 349 (348.1928) | 348@175% + 1@33.7% | 174.6% |
| Alternate: Cooling Device | blender | 72 (72.0000) | 72@50% | 50.0% |
| Alternate: Diluted Fuel | blender | 416 (415.2201) | 415@50% + 1@11% | 49.9% |
| Alternate: Heat-Fused Frame | blender | 69 (68.3154) | 68@50% + 1@15.8% | 49.5% |
| Alternate: Nitro Rocket Fuel | blender | 45 (44.2525) | 44@50% + 1@12.6% | 49.2% |
| Alternate: Turbo Blend Fuel | blender | 202 (201.3810) | 201@50% + 1@19.1% | 49.8% |
| Nitric Acid | blender | 117 (116.3852) | 116@50% + 1@19.3% | 49.7% |
| Non-Fissile Uranium | blender | 101 (100.8000) | 100@50% + 1@40% | 49.9% |
| Rocket Fuel | blender | 34 (33.9987) | 33@50% + 1@49.9% | 50.0% |
| Alternate: Cast Screws | constructor | 124 (123.5293) | 123@250% + 1@132.3% | 249.1% |
| Alternate: Iron Pipe | constructor | 395 (394.9362) | 394@250% + 1@234.1% | 250.0% |
| Alternate: Iron Wire | constructor | 1,735 (1734.1111) | 1734@250% + 1@27.8% | 249.9% |
| Alternate: Steel Screws | constructor | 11 (10.6340) | 10@250% + 1@158.5% | 241.7% |
| Cable | constructor | 358 (357.0869) | 357@250% + 1@21.7% | 249.4% |
| Copper Powder | constructor | 48 (48.0000) | 48@250% | 250.0% |
| Empty Canister | constructor | 24 (23.4074) | 23@250% + 1@101.9% | 243.8% |
| Empty Fluid Tank | constructor | 2 (1.9957) | 1@250% + 1@248.9% | 249.5% |
| Ficsite Trigon | constructor | 20 (19.3333) | 19@250% + 1@83.3% | 241.7% |
| Iron Plate | constructor | 81 (80.9644) | 80@250% + 1@241.1% | 249.9% |
| Reanimated SAM | constructor | 34 (34.0000) | 34@250% | 250.0% |
| Bauxite (Caterium) | converter | 188 (187.3504) | 187@25% + 1@8.8% | 24.9% |
| Bauxite (Copper) | converter | 64 (63.5503) | 63@25% + 1@13.8% | 24.8% |
| Coal (Iron) | converter | 48 (47.8747) | 47@25% + 1@21.9% | 24.9% |
| Coal (Limestone) | converter | 335 (334.5579) | 334@25% + 1@13.9% | 25.0% |
| Excited Photonic Matter | converter | 205 (205.0000) | 205@25% | 25.0% |
| Ficsite Ingot (Aluminum) | converter | 65 (64.4444) | 64@25% + 1@11.1% | 24.8% |
| Time Crystal | converter | 1,756 (1755.5556) | 1755@25% + 1@13.9% | 25.0% |
| Alternate: Compacted Steel Ingot | foundry | 193 (192.8400) | 192@150% + 1@126% | 149.9% |
| Alternate: Molded Beam | foundry | 17 (16.0700) | 16@150% + 1@10.5% | 141.8% |
| Rocket Fuel Power | fuel_generator | 482 (481.8120) | 481@250% + 1@203% | 249.9% |
| Geothermal Power (Impure) | geothermal_generator | 9 (9.0000) | 9@100% | 100.0% |
| Geothermal Power (Normal) | geothermal_generator | 13 (13.0000) | 13@100% | 100.0% |
| Geothermal Power (Pure) | geothermal_generator | 9 (9.0000) | 9@100% | 100.0% |
| Adaptive Control Unit | manufacturer | 18 (17.3748) | 17@50% + 1@18.7% | 48.3% |
| Adaptive Control Unit | manufacturer | 346 (345.5036) | 345@75% + 1@37.8% | 74.9% |
| Alternate: Caterium Computer | manufacturer | 404 (403.0544) | 403@75% + 1@4.1% | 74.8% |
| Alternate: Classic Battery | manufacturer | 103 (102.4774) | 102@75% + 1@35.8% | 74.6% |
| Alternate: Flexible Framework | manufacturer | 65 (64.4444) | 64@50% + 1@22.2% | 49.6% |
| Alternate: Heavy Encased Frame | manufacturer | 176 (175.5441) | 175@75% + 1@40.8% | 74.8% |
| Alternate: Infused Uranium Cell | manufacturer | 168 (168.0000) | 168@50% | 50.0% |
| Alternate: Insulated Crystal Oscillator | manufacturer | 359 (358.4395) | 358@75% + 1@33% | 74.9% |
| Alternate: Super-State Computer | manufacturer | 129 (128.0968) | 128@75% + 1@7.3% | 74.5% |
| Alternate: Turbo Electric Motor | manufacturer | 17 (16.6181) | 16@75% + 1@46.4% | 73.3% |
| Alternate: Turbo Pressure Motor | manufacturer | 14 (13.3046) | 13@50% + 1@15.2% | 47.5% |
| Alternate: Uranium Fuel Unit | manufacturer | 168 (168.0000) | 168@50% | 50.0% |
| Ballistic Warp Drive (4 sloops) | manufacturer | 24 (24.0000) | 24@250% | 250.0% |
| Modular Engine | manufacturer | 300 (300.0000) | 300@50% | 50.0% |
| Plutonium Fuel Rod | manufacturer | 101 (100.8000) | 100@50% + 1@40% | 49.9% |
| Radio Control Unit | manufacturer | 102 (101.3907) | 101@75% + 1@29.3% | 74.6% |
| Singularity Cell | manufacturer | 40 (40.0000) | 40@75% | 75.0% |
| Thermal Propulsion Rocket | manufacturer | 80 (80.0000) | 80@75% | 75.0% |
| Nuclear Power (Uranium) | nuclear_power_plant | 101 (100.8000) | 100@250% + 1@200% | 249.5% |
| Packaged Nitrogen Gas | packager | 3 (2.2174) | 2@225% + 1@48.9% | 166.3% |
| Packaged Turbofuel | packager | 79 (78.0247) | 78@225% + 1@5.6% | 222.2% |
| AI Expansion Server | quantum_encoder | 67 (66.6667) | 66@25% + 1@16.7% | 24.9% |
| AI Expansion Server (2 sloops) | quantum_encoder | 1 (1.0000) | 1@250% | 250.0% |
| AI Expansion Server (3 sloops) | quantum_encoder | 2 (2.0000) | 2@250% | 250.0% |
| Neural-Quantum Processor | quantum_encoder | 129 (128.8889) | 128@25% + 1@22.2% | 25.0% |
| Superposition Oscillator | quantum_encoder | 174 (173.3333) | 173@25% + 1@8.3% | 24.9% |
| Alternate: Electrode Aluminum Scrap | refinery | 133 (132.1801) | 132@100% + 1@18% | 99.4% |
| Alternate: Heavy Oil Residue | refinery | 420 (420.0000) | 420@100% | 100.0% |
| Alternate: Leached Caterium Ingot | refinery | 1 (0.2408) | 1@24.1% | 24.1% |
| Alternate: Pure Caterium Ingot | refinery | 332 (331.7231) | 331@100% + 1@72.3% | 99.9% |
| Alternate: Pure Copper Ingot | refinery | 2,270 (2269.3492) | 2269@100% + 1@34.9% | 100.0% |
| Alternate: Pure Iron Ingot | refinery | 2,529 (2528.5525) | 2528@100% + 1@55.3% | 100.0% |
| Alternate: Pure Quartz Crystal | refinery | 97 (96.0106) | 96@100% + 1@1.1% | 99.0% |
| Alternate: Recycled Plastic | refinery | 252 (251.9998) | 251@100% + 1@100% | 100.0% |
| Alternate: Recycled Rubber | refinery | 282 (281.7766) | 281@100% + 1@77.7% | 99.9% |
| Alternate: Sloppy Alumina | refinery | 100 (99.1351) | 99@100% + 1@13.5% | 99.1% |
| Alternate: Steamed Copper Sheet | refinery | 1,081 (1080.9347) | 1080@100% + 1@93.5% | 100.0% |
| Alternate: Wet Concrete | refinery | 230 (229.0915) | 229@100% + 1@9.1% | 99.6% |
| Petroleum Coke | refinery | 85 (84.9695) | 84@100% + 1@97% | 100.0% |
| Residual Rubber | refinery | 210 (210.0000) | 210@100% | 100.0% |
| Sulfuric Acid | refinery | 16 (15.2645) | 15@100% + 1@26.4% | 95.4% |
| Alternate: Pure Aluminum Ingot | smelter | 265 (264.3603) | 264@250% + 1@90.1% | 249.4% |

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
| Water Extraction | water_extractor | 1,530 (1529.3239) | 1529@125% + 1@40.5% | 124.9% |

---

# Per item breakdown

For every item this plan produces, the recipes that make it — with the plan's whole-machine count, clock, sloop grade, and the share of the item's total that each recipe supplies.

## Water — 244,033.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Water Extraction | water_extractor | 1,530 | 124.9% | — | 229,398.6 | 94.0% |
| Alternate: Electrode Aluminum Scrap | refinery | 133 | 99.4% | — | 13,878.9 | 5.7% |
| Non-Fissile Uranium | blender | 101 | 49.9% | — | 756.0 | 0.3% |

## Iron Ingot — 164,355.9/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Iron Ingot | refinery | 2,529 | 100.0% | — | 164,355.9 | 100.0% |

## Wire — 97,543.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Iron Wire | constructor | 1,735 | 249.9% | — | 97,543.8 | 100.0% |

## Iron Ore — 92,100.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Iron Ore (Pure) Mk.3 | miner_mk3 | 46 | 250.0% | — | 55,200.0 | 59.9% |
| Iron Ore (Normal) Mk.3 | miner_mk3 | 42 | 250.0% | — | 25,200.0 | 27.4% |
| Iron Ore (Impure) Mk.3 | miner_mk3 | 39 | 250.0% | — | 11,700.0 | 12.7% |

## Copper Ingot — 85,100.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Copper Ingot | refinery | 2,270 | 100.0% | — | 85,100.6 | 100.0% |

## Limestone — 69,300.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Limestone (Pure) Mk.3 | miner_mk3 | 29 | 250.0% | — | 34,800.0 | 50.2% |
| Limestone (Normal) Mk.3 | miner_mk3 | 50 | 250.0% | — | 30,000.0 | 43.3% |
| Limestone (Impure) Mk.3 | miner_mk3 | 15 | 250.0% | — | 4,500.0 | 6.5% |

## Coal — 53,773.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Coal (Pure) Mk.3 | miner_mk3 | 16 | 250.0% | — | 19,200.0 | 35.7% |
| Coal (Normal) Mk.3 | miner_mk3 | 31 | 250.0% | — | 18,600.0 | 34.6% |
| Coal (Limestone) | converter | 335 | 25.0% | — | 10,036.7 | 18.7% |
| Coal (Impure) Mk.3 | miner_mk3 | 15 | 250.0% | — | 4,500.0 | 8.4% |
| Coal (Iron) | converter | 48 | 24.9% | — | 1,436.2 | 2.7% |

## Quickwire — 47,872.2/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Fused Quickwire | assembler | 304 | 175.0% | — | 47,872.2 | 100.0% |

## Aluminum Scrap — 39,654.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Electrode Aluminum Scrap | refinery | 133 | 99.4% | — | 39,654.0 | 100.0% |

## Copper Ore — 36,900.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Copper Ore (Normal) Mk.3 | miner_mk3 | 29 | 250.0% | — | 17,400.0 | 47.2% |
| Copper Ore (Pure) Mk.3 | miner_mk3 | 13 | 250.0% | — | 15,600.0 | 42.3% |
| Copper Ore (Impure) Mk.3 | miner_mk3 | 13 | 250.0% | — | 3,900.0 | 10.6% |

## Cable — 26,781.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Cable | constructor | 358 | 249.4% | — | 26,781.5 | 100.0% |

## Steel Pipe — 24,683.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Iron Pipe | constructor | 395 | 250.0% | — | 24,683.5 | 100.0% |

## Copper Sheet — 24,321.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Steamed Copper Sheet | refinery | 1,081 | 100.0% | — | 24,321.0 | 100.0% |

## Alumina Solution — 23,792.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Sloppy Alumina | refinery | 100 | 99.1% | — | 23,792.4 | 100.0% |

## Screws — 22,353.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Cast Screws | constructor | 124 | 249.1% | — | 15,441.2 | 69.1% |
| Alternate: Steel Screws | constructor | 11 | 241.7% | — | 6,912.1 | 30.9% |

## Rubber — 21,106.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Recycled Rubber | refinery | 282 | 99.9% | — | 16,906.6 | 80.1% |
| Residual Rubber | refinery | 210 | 100.0% | — | 4,200.0 | 19.9% |

## Fuel — 20,761.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Diluted Fuel | blender | 416 | 49.9% | — | 20,761.0 | 100.0% |

## Aluminum Ingot — 19,827.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Aluminum Ingot | smelter | 265 | 249.4% | — | 19,827.0 | 100.0% |

## Bauxite — 19,827.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Bauxite (Pure) Mk.3 | miner_mk3 | 6 | 250.0% | — | 7,200.0 | 36.3% |
| Bauxite (Caterium) | converter | 188 | 24.9% | — | 5,620.5 | 28.3% |
| Bauxite (Normal) Mk.3 | miner_mk3 | 6 | 250.0% | — | 3,600.0 | 18.2% |
| Bauxite (Copper) | converter | 64 | 24.8% | — | 1,906.5 | 9.6% |
| Bauxite (Impure) Mk.3 | miner_mk3 | 5 | 250.0% | — | 1,500.0 | 7.6% |

## Concrete — 18,327.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Wet Concrete | refinery | 230 | 99.6% | — | 18,327.3 | 100.0% |

## Heavy Oil Residue — 16,800.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heavy Oil Residue | refinery | 420 | 100.0% | — | 16,800.0 | 100.0% |

## Silica — 16,378.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Cheap Silica | assembler | 179 | 174.3% | — | 16,378.3 | 100.0% |

## Plastic — 15,120.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Recycled Plastic | refinery | 252 | 100.0% | — | 15,120.0 | 100.0% |

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
| Excited Photonic Matter | converter | 205 | 25.0% | — | 10,250.0 | 100.0% |

## SAM — 10,200.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| SAM (Normal) Mk.3 | miner_mk3 | 6 | 250.0% | — | 3,600.0 | 35.3% |
| SAM (Pure) Mk.3 | miner_mk3 | 3 | 250.0% | — | 3,600.0 | 35.3% |
| SAM (Impure) Mk.3 | miner_mk3 | 10 | 250.0% | — | 3,000.0 | 29.4% |

## Petroleum Coke — 10,196.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Petroleum Coke | refinery | 85 | 100.0% | — | 10,196.3 | 100.0% |

## Alclad Aluminum Sheet — 8,415.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alclad Aluminum Sheet | assembler | 161 | 174.2% | — | 8,415.0 | 100.0% |

## Polymer Resin — 8,400.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heavy Oil Residue | refinery | 420 | 100.0% | — | 8,400.0 | 100.0% |

## Iron Plate — 7,044.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Iron Plate | constructor | 81 | 249.9% | — | 4,048.2 | 57.5% |
| Alternate: Coated Iron Plate | assembler | 23 | 173.7% | — | 2,996.5 | 42.5% |

## Circuit Board — 6,299.2/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Silicon Circuit Board | assembler | 288 | 175.0% | — | 6,299.2 | 100.0% |

## Copper Powder — 6,000.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Copper Powder | constructor | 48 | 250.0% | — | 6,000.0 | 100.0% |

## Diamonds — 5,266.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Turbo Diamonds | accelerator | 352 | 24.9% | — | 5,266.7 | 100.0% |

## Quartz Crystal — 5,040.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Quartz Crystal | refinery | 97 | 99.0% | — | 5,040.6 | 100.0% |

## Rocket Fuel — 5,018.9/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Nitro Rocket Fuel | blender | 45 | 49.2% | — | 3,318.9 | 66.1% |
| Rocket Fuel | blender | 34 | 50.0% | — | 1,699.9 | 33.9% |

## Turbofuel — 4,531.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Turbo Blend Fuel | blender | 202 | 49.8% | — | 4,531.1 | 100.0% |

## Dark Matter Crystal — 4,300.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Dark Matter Trap | accelerator | 287 | 25.0% | — | 4,300.0 | 100.0% |

## Caterium Ingot — 3,989.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Pure Caterium Ingot | refinery | 332 | 99.9% | — | 3,980.7 | 99.8% |
| Alternate: Leached Caterium Ingot | refinery | 1 | 24.1% | — | 8.7 | 0.2% |

## Empty Canister — 3,511.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Empty Canister | constructor | 24 | 243.8% | — | 3,511.1 | 100.0% |

## Packaged Turbofuel — 3,511.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Packaged Turbofuel | packager | 79 | 222.2% | — | 3,511.1 | 100.0% |

## Stator — 3,046.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Stator | assembler | 349 | 174.6% | — | 3,046.7 | 100.0% |

## Aluminum Casing — 3,041.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Alclad Casing | assembler | 16 | 169.0% | — | 3,041.7 | 100.0% |

## Steel Ingot — 2,892.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Compacted Steel Ingot | foundry | 193 | 149.9% | — | 2,892.6 | 100.0% |

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
| Non-Fissile Uranium | blender | 101 | 49.9% | — | 2,520.0 | 100.0% |

## Uranium Waste — 2,520.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Nuclear Power (Uranium) | nuclear_power_plant | 101 | 249.5% | — | 2,520.0 | 100.0% |

## Battery — 2,305.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Classic Battery | manufacturer | 103 | 74.6% | — | 2,305.7 | 100.0% |

## Uranium — 2,100.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Uranium (Normal) Mk.3 | miner_mk3 | 2 | 250.0% | — | 1,200.0 | 57.1% |
| Uranium (Impure) Mk.3 | miner_mk3 | 3 | 250.0% | — | 900.0 | 42.9% |

## Nitric Acid — 1,745.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Nitric Acid | blender | 117 | 49.7% | — | 1,745.8 | 100.0% |

## Encased Uranium Cell — 1,680.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Infused Uranium Cell | manufacturer | 168 | 50.0% | — | 1,680.0 | 100.0% |

## Ficsite Trigon — 1,450.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Ficsite Trigon | constructor | 20 | 241.7% | — | 1,450.0 | 100.0% |

## Computer — 1,417.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Caterium Computer | manufacturer | 404 | 74.8% | — | 1,133.6 | 80.0% |
| Alternate: Crystal Computer | assembler | 49 | 173.8% | — | 283.9 | 20.0% |

## Automated Wiring — 1,339.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Automated Wiring | assembler | 307 | 174.5% | — | 1,339.1 | 100.0% |

## Rotor — 1,289.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Copper Rotor | assembler | 66 | 173.7% | — | 1,289.6 | 100.0% |

## AI Limiter — 1,285.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| AI Limiter | assembler | 147 | 174.8% | — | 1,285.1 | 100.0% |

## Encased Industrial Beam — 1,234.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Encased Industrial Pipe | assembler | 177 | 174.3% | — | 1,234.3 | 100.0% |

## Modular Frame — 1,108.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Steeled Frame | assembler | 212 | 174.3% | — | 1,108.3 | 100.0% |

## Steel Beam — 1,084.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Molded Beam | foundry | 17 | 141.8% | — | 1,084.7 | 100.0% |

## Reinforced Iron Plate — 1,038.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Stitched Iron Plate | assembler | 106 | 174.2% | — | 1,038.8 | 100.0% |

## Electromagnetic Control Rod — 781.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Electromagnetic Control Rod | assembler | 112 | 174.3% | — | 781.0 | 100.0% |

## Sulfuric Acid — 763.2/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Sulfuric Acid | refinery | 16 | 95.4% | — | 763.2 | 100.0% |

## Plutonium Pellet — 756.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Plutonium Pellet | accelerator | 101 | 25.0% | — | 756.0 | 100.0% |

## Compacted Coal — 723.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Nitro Rocket Fuel | blender | 45 | 49.2% | — | 553.2 | 76.5% |
| Rocket Fuel | blender | 34 | 50.0% | — | 170.0 | 23.5% |

## Motor — 521.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Electric Motor | assembler | 24 | 168.6% | — | 303.6 | 58.2% |
| Motor | assembler | 25 | 174.5% | — | 218.1 | 41.8% |

## Crystal Oscillator — 504.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Insulated Crystal Oscillator | manufacturer | 359 | 74.9% | — | 504.1 | 100.0% |

## Heat Sink — 486.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Heat Sink | assembler | 38 | 170.5% | — | 486.0 | 100.0% |

## Ficsite Ingot — 483.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Ficsite Ingot (Aluminum) | converter | 65 | 24.8% | — | 483.3 | 100.0% |

## Encased Plutonium Cell — 378.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Encased Plutonium Cell | assembler | 44 | 171.8% | — | 378.0 | 100.0% |

## Heavy Modular Frame — 370.3/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heavy Encased Frame | manufacturer | 176 | 74.8% | — | 370.3 | 100.0% |

## Singularity Cell — 300.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Singularity Cell | manufacturer | 40 | 75.0% | — | 300.0 | 100.0% |

## Smart Plating — 300.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Smart Plating | assembler | 86 | 174.4% | — | 300.0 | 100.0% |

## Empty Fluid Tank — 299.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Empty Fluid Tank | constructor | 2 | 249.5% | — | 299.4 | 100.0% |

## Packaged Nitrogen Gas — 299.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Packaged Nitrogen Gas | packager | 3 | 166.3% | — | 299.4 | 100.0% |

## Adaptive Control Unit — 267.8/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Adaptive Control Unit | manufacturer | 346 | 74.9% | — | 259.1 | 96.8% |
| Adaptive Control Unit | manufacturer | 18 | 48.3% | — | 8.7 | 3.2% |

## Versatile Framework — 241.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Flexible Framework | manufacturer | 65 | 49.6% | — | 241.7 | 100.0% |

## Supercomputer — 230.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Super-State Computer | manufacturer | 129 | 74.5% | — | 230.6 | 100.0% |

## Superposition Oscillator — 216.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Superposition Oscillator | quantum_encoder | 174 | 24.9% | — | 216.7 | 100.0% |

## Radio Control Unit — 190.1/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Radio Control Unit | manufacturer | 102 | 74.6% | — | 190.1 | 100.0% |

## Cooling System — 180.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Cooling Device | blender | 72 | 50.0% | — | 180.0 | 100.0% |

## Modular Engine — 150.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Modular Engine | manufacturer | 300 | 50.0% | — | 150.0 | 100.0% |

## Assembly Director System — 133.9/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Assembly Director System | assembler | 103 | 173.3% | — | 133.9 | 100.0% |

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

## Fused Modular Frame — 102.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Heat-Fused Frame | blender | 69 | 49.5% | — | 102.5 | 100.0% |

## Magnetic Field Generator — 96.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Magnetic Field Generator | assembler | 56 | 172.6% | — | 96.7 | 100.0% |

## Neural-Quantum Processor — 96.7/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Neural-Quantum Processor | quantum_encoder | 129 | 25.0% | — | 96.7 | 100.0% |

## Thermal Propulsion Rocket — 60.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Thermal Propulsion Rocket | manufacturer | 80 | 75.0% | — | 60.0 | 100.0% |

## Turbo Motor — 60.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Turbo Electric Motor | manufacturer | 17 | 73.3% | — | 35.1 | 58.4% |
| Alternate: Turbo Pressure Motor | manufacturer | 14 | 47.5% | — | 24.9 | 41.6% |

## Uranium Fuel Rod — 50.4/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Alternate: Uranium Fuel Unit | manufacturer | 168 | 50.0% | — | 50.4 | 100.0% |

## Pressure Conversion Cube — 42.5/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Pressure Conversion Cube | assembler | 25 | 169.9% | — | 42.5 | 100.0% |

## Nuclear Pasta — 30.0/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Nuclear Pasta | accelerator | 240 | 25.0% | — | 30.0 | 100.0% |

## Plutonium Fuel Rod — 12.6/min

| Recipe | machine | count | clock | slps | /min | share |
|---|---|---:|---:|---:|---:|---:|
| Plutonium Fuel Rod | manufacturer | 101 | 49.9% | — | 12.6 | 100.0% |

---

# Per-machine breakdown

One section per machine type in the plan: the recipes it runs, the whole-machine count, clock and sloop grade, and aggregate inputs/outputs per minute.

## Refinery — 8,038 machines · 240,877 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Pure Iron Ingot | 2,529 | 100.0% | — | Iron Ore 88,499.3 + Water 50,571.1 | Iron Ingot 164,355.9 |
| Alternate: Pure Copper Ingot | 2,270 | 100.0% | — | Copper Ore 34,040.2 + Water 22,693.5 | Copper Ingot 85,100.6 |
| Alternate: Steamed Copper Sheet | 1,081 | 100.0% | — | Copper Ingot 24,321.0 + Water 24,321.0 | Copper Sheet 24,321.0 |
| Alternate: Heavy Oil Residue | 420 | 100.0% | — | Crude Oil 12,600.0 | Heavy Oil Residue 16,800.0 + Polymer Resin 8,400.0 |
| Alternate: Pure Caterium Ingot | 332 | 99.9% | — | Caterium Ore 7,961.4 + Water 7,961.4 | Caterium Ingot 3,980.7 |
| Alternate: Recycled Rubber | 282 | 99.9% | — | Fuel 8,453.3 + Plastic 8,453.3 | Rubber 16,906.6 |
| Alternate: Recycled Plastic | 252 | 100.0% | — | Fuel 7,560.0 + Rubber 7,560.0 | Plastic 15,120.0 |
| Alternate: Wet Concrete | 230 | 99.6% | — | Limestone 27,491.0 + Water 22,909.1 | Concrete 18,327.3 |
| Residual Rubber | 210 | 100.0% | — | Polymer Resin 8,400.0 + Water 8,400.0 | Rubber 4,200.0 |
| Alternate: Electrode Aluminum Scrap | 133 | 99.4% | — | Alumina Solution 23,792.4 + Petroleum Coke 7,930.8 | Aluminum Scrap 39,654.0 + Water 13,878.9 |
| Alternate: Sloppy Alumina | 100 | 99.1% | — | Bauxite 19,827.0 + Water 19,827.0 | Alumina Solution 23,792.4 |
| Alternate: Pure Quartz Crystal | 97 | 99.0% | — | Raw Quartz 6,480.7 + Water 3,600.4 | Quartz Crystal 5,040.6 |
| Petroleum Coke | 85 | 100.0% | — | Heavy Oil Residue 3,398.8 | Petroleum Coke 10,196.3 |
| Sulfuric Acid | 16 | 95.4% | — | Sulfur 763.2 + Water 763.2 | Sulfuric Acid 763.2 |
| Alternate: Leached Caterium Ingot | 1 | 24.1% | — | Caterium Ore 13.0 + Sulfuric Acid 7.2 | Caterium Ingot 8.7 |

## Assembler — 2,897 machines · 90,524 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Stator | 349 | 174.6% | — | Steel Pipe 9,140.1 + Wire 24,373.5 | Stator 3,046.7 |
| Automated Wiring | 307 | 174.5% | — | Cable 26,781.5 + Stator 1,339.1 | Automated Wiring 1,339.1 |
| Alternate: Fused Quickwire | 304 | 175.0% | — | Caterium Ingot 3,989.3 + Copper Ingot 19,946.7 | Quickwire 47,872.2 |
| Alternate: Silicon Circuit Board | 288 | 175.0% | — | Copper Sheet 13,858.3 + Silica 13,858.3 | Circuit Board 6,299.2 |
| Alternate: Steeled Frame | 212 | 174.3% | — | Reinforced Iron Plate 738.8 + Steel Pipe 3,694.2 | Modular Frame 1,108.3 |
| Alternate: Cheap Silica | 179 | 174.3% | — | Limestone 11,698.8 + Raw Quartz 7,019.3 | Silica 16,378.3 |
| Alternate: Encased Industrial Pipe | 177 | 174.3% | — | Concrete 6,171.5 + Steel Pipe 7,405.8 | Encased Industrial Beam 1,234.3 |
| Alclad Aluminum Sheet | 161 | 174.2% | — | Aluminum Ingot 8,415.0 + Copper Ingot 2,805.0 | Alclad Aluminum Sheet 8,415.0 |
| AI Limiter | 147 | 174.8% | — | Copper Sheet 6,425.5 + Quickwire 25,701.9 | AI Limiter 1,285.1 |
| Electromagnetic Control Rod | 112 | 174.3% | — | AI Limiter 781.0 + Stator 1,171.6 | Electromagnetic Control Rod 781.0 |
| Alternate: Stitched Iron Plate | 106 | 174.2% | — | Iron Plate 3,462.8 + Wire 6,925.6 | Reinforced Iron Plate 1,038.8 |
| Assembly Director System | 103 | 173.3% | — | Adaptive Control Unit 267.8 + Supercomputer 133.9 | Assembly Director System 133.9 |
| Smart Plating | 86 | 174.4% | — | Reinforced Iron Plate 300.0 + Rotor 300.0 | Smart Plating 300.0 |
| Alternate: Copper Rotor | 66 | 173.7% | — | Copper Sheet 2,579.2 + Screws 22,353.3 | Rotor 1,289.6 |
| Magnetic Field Generator | 56 | 172.6% | — | Electromagnetic Control Rod 96.7 + Versatile Framework 241.7 | Magnetic Field Generator 96.7 |
| Alternate: Crystal Computer | 49 | 173.8% | — | Circuit Board 425.8 + Crystal Oscillator 141.9 | Computer 283.9 |
| Encased Plutonium Cell | 44 | 171.8% | — | Concrete 1,512.0 + Plutonium Pellet 756.0 | Encased Plutonium Cell 378.0 |
| Heat Sink | 38 | 170.5% | — | Alclad Aluminum Sheet 2,430.0 + Copper Sheet 1,458.0 | Heat Sink 486.0 |
| Motor | 25 | 174.5% | — | Rotor 436.3 + Stator 436.3 | Motor 218.1 |
| Pressure Conversion Cube | 25 | 169.9% | — | Fused Modular Frame 42.5 + Radio Control Unit 84.9 | Pressure Conversion Cube 42.5 |
| Alternate: Electric Motor | 24 | 168.6% | — | Electromagnetic Control Rod 151.8 + Rotor 303.6 | Motor 303.6 |
| Alternate: Coated Iron Plate | 23 | 173.7% | — | Iron Ingot 1,498.3 + Plastic 299.7 | Iron Plate 2,996.5 |
| Alternate: Alclad Casing | 16 | 169.0% | — | Aluminum Ingot 4,055.6 + Copper Ingot 2,027.8 | Aluminum Casing 3,041.7 |

## Constructor — 2,832 machines · 37,966 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Iron Wire | 1,735 | 249.9% | — | Iron Ingot 54,191.0 | Wire 97,543.8 |
| Alternate: Iron Pipe | 395 | 250.0% | — | Iron Ingot 98,734.1 | Steel Pipe 24,683.5 |
| Cable | 358 | 249.4% | — | Wire 53,563.0 | Cable 26,781.5 |
| Alternate: Cast Screws | 124 | 249.1% | — | Iron Ingot 3,860.3 | Screws 15,441.2 |
| Iron Plate | 81 | 249.9% | — | Iron Ingot 6,072.3 | Iron Plate 4,048.2 |
| Copper Powder | 48 | 250.0% | — | Copper Ingot 36,000.0 | Copper Powder 6,000.0 |
| Reanimated SAM | 34 | 250.0% | — | SAM 10,200.0 | Reanimated SAM 2,550.0 |
| Empty Canister | 24 | 243.8% | — | Plastic 1,755.6 | Empty Canister 3,511.1 |
| Ficsite Trigon | 20 | 241.7% | — | Ficsite Ingot 483.3 | Ficsite Trigon 1,450.0 |
| Alternate: Steel Screws | 11 | 241.7% | — | Steel Beam 132.9 | Screws 6,912.1 |
| Empty Fluid Tank | 2 | 249.5% | — | Aluminum Ingot 299.4 | Empty Fluid Tank 299.4 |

## Converter — 2,661 machines · 106,299 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Time Crystal | 1,756 | 25.0% | — | Diamonds 5,266.7 | Time Crystal 2,633.3 |
| Coal (Limestone) | 335 | 25.0% | — | Limestone 30,110.2 + Reanimated SAM 836.4 | Coal 10,036.7 |
| Excited Photonic Matter | 205 | 25.0% | — | — | Excited Photonic Matter 10,250.0 |
| Bauxite (Caterium) | 188 | 24.9% | — | Caterium Ore 7,025.6 + Reanimated SAM 468.4 | Bauxite 5,620.5 |
| Ficsite Ingot (Aluminum) | 65 | 24.8% | — | Aluminum Ingot 1,933.3 + Reanimated SAM 966.7 | Ficsite Ingot 483.3 |
| Bauxite (Copper) | 64 | 24.8% | — | Copper Ore 2,859.8 + Reanimated SAM 158.9 | Bauxite 1,906.5 |
| Coal (Iron) | 48 | 24.9% | — | Iron Ore 2,154.4 + Reanimated SAM 119.7 | Coal 1,436.2 |

## Manufacturer — 2,614 machines · 101,803 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Caterium Computer | 404 | 74.8% | — | Circuit Board 4,534.4 + Quickwire 15,870.3 + Rubber 6,801.5 | Computer 1,133.6 |
| Alternate: Insulated Crystal Oscillator | 359 | 74.9% | — | AI Limiter 504.1 + Quartz Crystal 5,040.6 + Rubber 3,528.4 | Crystal Oscillator 504.1 |
| Adaptive Control Unit | 346 | 74.9% | — | Automated Wiring 1,295.6 + Circuit Board 1,295.6 + Computer 518.3 + Heavy Modular Frame 259.1 | Adaptive Control Unit 259.1 |
| Modular Engine | 300 | 50.0% | — | Motor 300.0 + Rubber 2,250.0 + Smart Plating 300.0 | Modular Engine 150.0 |
| Alternate: Heavy Encased Frame | 176 | 74.8% | — | Concrete 2,715.4 + Encased Industrial Beam 1,234.3 + Modular Frame 987.4 + Steel Pipe 4,443.5 | Heavy Modular Frame 370.3 |
| Alternate: Infused Uranium Cell | 168 | 50.0% | — | Quickwire 6,300.0 + Silica 1,260.0 + Sulfur 2,100.0 + Uranium 2,100.0 | Encased Uranium Cell 1,680.0 |
| Alternate: Uranium Fuel Unit | 168 | 50.0% | — | Crystal Oscillator 50.4 + Electromagnetic Control Rod 168.0 + Encased Uranium Cell 1,680.0 + Rotor 168.0 | Uranium Fuel Rod 50.4 |
| Alternate: Super-State Computer | 129 | 74.5% | — | Battery 2,305.7 + Computer 691.7 + Electromagnetic Control Rod 230.6 + Wire 5,764.4 | Supercomputer 230.6 |
| Alternate: Classic Battery | 103 | 74.6% | — | Alclad Aluminum Sheet 4,035.0 + Plastic 4,611.5 + Sulfur 3,458.6 + Wire 6,917.2 | Battery 2,305.7 |
| Radio Control Unit | 102 | 74.6% | — | Aluminum Casing 3,041.7 + Computer 190.1 + Crystal Oscillator 95.1 | Radio Control Unit 190.1 |
| Plutonium Fuel Rod | 101 | 49.9% | — | Electromagnetic Control Rod 75.6 + Encased Plutonium Cell 378.0 + Heat Sink 126.0 + Steel Beam 226.8 | Plutonium Fuel Rod 12.6 |
| Thermal Propulsion Rocket | 80 | 75.0% | — | Cooling System 180.0 + Fused Modular Frame 60.0 + Modular Engine 150.0 + Turbo Motor 60.0 | Thermal Propulsion Rocket 60.0 |
| Alternate: Flexible Framework | 65 | 49.6% | — | Modular Frame 120.8 + Rubber 966.7 + Steel Beam 725.0 | Versatile Framework 241.7 |
| Singularity Cell | 40 | 75.0% | — | Concrete 6,000.0 + Dark Matter Crystal 600.0 + Iron Plate 3,000.0 + Nuclear Pasta 30.0 | Singularity Cell 300.0 |
| Ballistic Warp Drive | 24 | 250.0% | 4 | Dark Matter Crystal 2,400.0 + Singularity Cell 300.0 + Superposition Oscillator 120.0 + Thermal Propulsion Rocket 60.0 | Ballistic Warp Drive 120.0 |
| Adaptive Control Unit | 18 | 48.3% | — | Automated Wiring 43.4 + Circuit Board 43.4 + Computer 17.4 + Heavy Modular Frame 8.7 | Adaptive Control Unit 8.7 |
| Alternate: Turbo Electric Motor | 17 | 73.3% | — | Electromagnetic Control Rod 58.4 + Motor 81.8 + Radio Control Unit 105.2 + Rotor 81.8 | Turbo Motor 35.1 |
| Alternate: Turbo Pressure Motor | 14 | 47.5% | — | Motor 49.9 + Packaged Nitrogen Gas 299.4 + Pressure Conversion Cube 12.5 + Stator 99.8 | Turbo Motor 24.9 |

## Blender — 1,056 machines · 31,536 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Diluted Fuel | 416 | 49.9% | — | Heavy Oil Residue 10,380.5 + Water 20,761.0 | Fuel 20,761.0 |
| Alternate: Turbo Blend Fuel | 202 | 49.8% | — | Fuel 1,510.4 + Heavy Oil Residue 3,020.7 + Petroleum Coke 2,265.5 + Sulfur 2,265.5 | Turbofuel 4,531.1 |
| Nitric Acid | 117 | 49.7% | — | Iron Plate 581.9 + Nitrogen Gas 6,983.1 + Water 1,745.8 | Nitric Acid 1,745.8 |
| Non-Fissile Uranium | 101 | 49.9% | — | Nitric Acid 756.0 + Silica 1,260.0 + Sulfuric Acid 756.0 + Uranium Waste 1,890.0 | Non-Fissile Uranium 2,520.0 + Water 756.0 |
| Alternate: Cooling Device | 72 | 50.0% | — | Heat Sink 360.0 + Motor 90.0 + Nitrogen Gas 2,160.0 | Cooling System 180.0 |
| Alternate: Heat-Fused Frame | 69 | 49.5% | — | Aluminum Ingot 5,123.7 + Fuel 1,024.7 + Heavy Modular Frame 102.5 + Nitric Acid 819.8 | Fused Modular Frame 102.5 |
| Alternate: Nitro Rocket Fuel | 45 | 49.2% | — | Coal 1,106.3 + Fuel 2,212.6 + Nitrogen Gas 1,659.5 + Sulfur 2,212.6 | Compacted Coal 553.2 + Rocket Fuel 3,318.9 |
| Rocket Fuel | 34 | 50.0% | — | Nitric Acid 170.0 + Turbofuel 1,020.0 | Compacted Coal 170.0 + Rocket Fuel 1,699.9 |

## Accelerator — 980 machines · 106,341 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Turbo Diamonds | 352 | 24.9% | — | Coal 52,666.7 + Packaged Turbofuel 3,511.1 | Diamonds 5,266.7 |
| Alternate: Dark Matter Trap | 287 | 25.0% | — | Dark Matter Residue 10,750.0 + Time Crystal 2,150.0 | Dark Matter Crystal 4,300.0 |
| Nuclear Pasta | 240 | 25.0% | — | Copper Powder 6,000.0 + Pressure Conversion Cube 30.0 | Nuclear Pasta 30.0 |
| Plutonium Pellet | 101 | 25.0% | — | Non-Fissile Uranium 2,520.0 + Uranium Waste 630.0 | Plutonium Pellet 756.0 |

## Quantum Encoder — 373 machines · 87,086 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Superposition Oscillator | 174 | 24.9% | — | Alclad Aluminum Sheet 1,950.0 + Crystal Oscillator 216.7 + Dark Matter Crystal 1,300.0 + Excited Photonic Matter 5,416.7 | Dark Matter Residue 5,416.7 + Superposition Oscillator 216.7 |
| Neural-Quantum Processor | 129 | 25.0% | — | Excited Photonic Matter 2,416.7 + Ficsite Trigon 1,450.0 + Supercomputer 96.7 + Time Crystal 483.3 | Dark Matter Residue 2,416.7 + Neural-Quantum Processor 96.7 |
| AI Expansion Server | 67 | 24.9% | — | Excited Photonic Matter 1,666.7 + Magnetic Field Generator 66.7 + Neural-Quantum Processor 66.7 + Superposition Oscillator 66.7 | AI Expansion Server 66.7 + Dark Matter Residue 1,666.7 |
| AI Expansion Server | 2 | 250.0% | 3 | Excited Photonic Matter 500.0 + Magnetic Field Generator 20.0 + Neural-Quantum Processor 20.0 + Superposition Oscillator 20.0 | AI Expansion Server 35.0 + Dark Matter Residue 875.0 |
| AI Expansion Server | 1 | 250.0% | 2 | Excited Photonic Matter 250.0 + Magnetic Field Generator 10.0 + Neural-Quantum Processor 10.0 + Superposition Oscillator 10.0 | AI Expansion Server 15.0 + Dark Matter Residue 375.0 |

## Smelter — 265 machines · 3,548 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Pure Aluminum Ingot | 265 | 249.4% | — | Aluminum Scrap 39,654.0 | Aluminum Ingot 19,827.0 |

## Foundry — 210 machines · 5,704 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Alternate: Compacted Steel Ingot | 193 | 149.9% | — | Compacted Coal 723.1 + Iron Ore 1,446.3 | Steel Ingot 2,892.6 |
| Alternate: Molded Beam | 17 | 141.8% | — | Concrete 1,928.4 + Steel Ingot 2,892.6 | Steel Beam 1,084.7 |

## Packager — 82 machines · 2,329 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Packaged Turbofuel | 79 | 222.2% | — | Empty Canister 3,511.1 + Turbofuel 3,511.1 | Packaged Turbofuel 3,511.1 |
| Packaged Nitrogen Gas | 3 | 166.3% | — | Empty Fluid Tank 299.4 + Nitrogen Gas 1,197.4 | Packaged Nitrogen Gas 299.4 |

---

# Resource extraction

Raw-material supply: miners, water/oil extractors and pressure wells. (The high-level overview aggregates these by resource; here each node group is listed.)

## Water Extractor — 1,530 machines · 41,075 MW

| Recipe | count | clock | slps | inputs /min | outputs /min |
|---|---|---:|---:|---|---|
| Water Extraction | 1,530 | 124.9% | — | — | Water 229,398.6 |

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

## Fuel Generator — 482 machines · **301,132 MW generated**

| Recipe | count | clock | slps | fuel /min | output |
|---|---|---:|---:|---|---|
| Rocket Fuel Power | 482 | 249.9% | — | Rocket Fuel 5,018.9 | 301,132 MW |

---

## Notes

- **Power rounding**: per-section draws are computed from the displayed whole-machine counts and sum to 928,470 MW, ~0.1% under the official 928,943 MW (the model also runs tiny sub-machine exact-balance slivers). Generation is clock-linear, so whole-machine sums reproduce the 938,232 MW exactly.
- Accelerator rows use per-recipe power draw where the spec overrides it; other machines use their machine default.
- Rates are **aggregate** at the displayed clock. Per-machine rate at that clock = aggregate ÷ `#`.
