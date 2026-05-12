# Main Route Prototype v0

Status: TB-033 validated as a block-level progression, counter-mechanics, location route-validation, checklist source-readiness, warning, and hard-save overlay, with machine-readable objective assignments in `data/route-planning/prototype-objective-block-map.csv`.

This is a Phase 7 flexible-objective insertion prototype with the Phase 8 progression overlay and Phase 10 counter/location-validation overlays. It is not final guide prose, not pathfinding, not a numbered itinerary, and not a checklist coverage matrix.

The purpose of this pass is narrower: place safe objective queues into the Survival Mode route-block frame from `drafts/route-prototypes/survival-geography-pass-v0.md`, add block-level skill, perk, training, crafting, and grind pressure, record counter/action checkpoints, capture location clear/discovery mechanics, incorporate TB-031J checklist source-readiness resolutions, and add concise warning/hard-save placement rules while preserving the hard level/reward gates, branch deferrals, and later validation/final-route passes.

This file does not independently introduce uncited gameplay research. Gameplay claims and route limits are carried from the source-backed objective database, the generated route-planning index, `data/locations/location-geography.csv`, `data/locations/location-route-validation.md`, the Phase 2 constraint tables, and `data/checklist-mapping/counter-coverage-plan.md`.

## Inputs

| Input | Use in this pass |
| --- | --- |
| `docs/guide-specification.md` | Scope guard: PS4 AE, Legendary, Survival Mode, trophy-safe official content, all perks, and branch policy. |
| `drafts/route-prototypes/route-anchors-v0.md` | Anchor register `A00` through `A21`, branch hard-save names, and non-final route boundaries. |
| `drafts/route-prototypes/level-gated-skeleton-v0.md` | Level bands `S00` through `S15` and mandatory do-not-cross gates. |
| `drafts/route-prototypes/survival-geography-pass-v0.md` | Route-block frame `G00` through `G14`, corridor support, prepared sweep rules, and Survival logistics vocabulary. |
| `data/objectives/objectives.csv` | Canonical objective rows, current route placement, and current routing rigidity. |
| `data/route-planning/objective-route-index.csv` | Generated per-objective workbench for corridor, support candidate, and constraint summaries. |
| `data/route-planning/objective-constraints.csv` | Generated objective-to-constraint links; inspect source tables before final route prose. |
| `data/route-planning/prototype-objective-block-map.csv` | Generated one-row-per-objective TB-026 audit map with route block, disposition, status, threshold, parent link, defer owner, and reason. |
| `data/locations/location-geography.csv` | Hub/corridor geography, rest/transport/cold/candidate-base support, and confidence flags. |
| `data/locations/location-route-validation.md` | TB-031G route-validation layer for Delver/Explorer mechanics, clear-trigger class, duplicate/secondary markers, content-location treatment, no-marker exclusions, and coordinate exception use. |
| `data/constraints/*.md` | Canonical route laws for AE starts, leveled rewards, cell locks, conflicts, trophies, NPC dependencies, bugs, radiants, Survival Mode, and progression. |
| `drafts/branch-routes/*.md` | TB-029 branch prototype hard saves, branch-exclusive objective queues, reload rules, and branch-verification handoffs. |
| `data/constraints/skill-perk-leveling-plan.md` | TB-027 block-level progression overlay for all-skills/all-perks, Legendary resets, training, crafting, investments, enchantment learning, alchemy effects, and underleveled fallbacks. TB-031E supplies source-selection defaults; exact reset counts and final skill-state validation remain TB-033. |
| `data/checklist-mapping/counter-coverage-plan.md` | TB-031F counter/action overlay for trophy counters, Thieves Guild side jobs, Dawnguard Lost Relic fillers, Fishing, work actions, trophy-pop fallbacks, and counter-owned source-readiness rows. |
| `data/checklist-mapping/source-readiness-resolutions.csv` | TB-031J source-readiness overlay: 75 checklist rows map to main-route handling, 1 maps to BR-007 branch coverage, and 2 are explicit exclusions. |

## Data Snapshot

| Route-index slice | Rows | Prototype handling |
| --- | ---: | --- |
| Main-route objective rows | 2,694 | Eligible for this artifact unless fixed, windowed, branch-deferred, or later-pass owned. |
| `dependency_flexible` main rows | 1,548 | Insert only after prerequisites and constraint rows permit. |
| `region_flexible` main rows | 842 | Insert when the route is naturally in the corridor and Survival support exists. |
| `windowed` main rows | 208 | Keep as anchored windows; do not treat as ordinary flexible fill. |
| `fixed_late` main rows | 72 | Keep behind their level, cell-entry, quest-state, reward, or progression gates. |
| `fixed_early` main rows | 6 | Place in setup/opening only. |
| `cleanup_safe` main rows | 18 | Keep for checklist reconciliation, not as early travel targets. |

| Progression queue | Rows | TB-027 handling |
| --- | ---: | --- |
| `skill_perk` objective rows | 40 | Integrated at route-block level. Final route must reach all skills 100, level 252+, and all 251 normal perk ranks assigned, with post-reset recovery. |
| `crafting_unlock` objective rows | 301 | Integrated as staged crafting, enchantment, alchemy, investment, and practical-system pressure. TB-031E supplies source-selection defaults; exact physical source-item availability and final validation remain downstream. |
| Skill book objective rows | 90 | Preserved as title-level progression/checklist rows. TB-031E supplies copy/read policy unless a parent quest/location fixes the pickup. |
| Transformation perk objectives | 4 | Remain faction/state-window work. They are separate from the 251 normal skill perk ranks. |

| Candidate status | Main rows | Prototype handling |
| --- | ---: | --- |
| `single_geography_point` | 443 | Assign to the primary corridor block, subject to hard gates and access validation. |
| `multiple_geography_points` | 4 | Assign to a block only after exact point validation; not final pathing. |
| `single_support_candidate` | 830 | Attach to the matching hub, quest, property, support table, or parent objective when prerequisites are valid. |
| `multiple_support_candidates` | 319 | Keep as a candidate-selection queue; later passes choose the local safe copy/source. |
| `no_route_candidate_data` | 1,098 | Place by anchor, quest dependency, faction sequence, reward timing, or later checklist mapping. |

All 447 direct geography rows in this prototype are `location` objectives. They are corridor-ready, but not final step-ready: the geography table is straight-line support data and still requires road, pass, water, quest-state, enemy, weather, and exact entrance validation before prose.

The direct geography counts below reflect current prototype-block assignment after gate extraction. The corridors column preserves source-corridor provenance for rows moved into control blocks such as G09 and G10.

Rows with blank `route_block` in `prototype-objective-block-map.csv` are intentionally assigned through `disposition`, `prototype_status`, `deferred_to`, and `reason`; blank does not mean unprocessed. TB-031A through TB-031J have assigned review buckets, counters, checklist-only rows, location-validation rows, source-readiness rows, and readiness-audit rows to explicit route, branch, appendix, validation, or final-guide owners. After TB-031J, no checklist row remains in `source_readiness_required`.

TB-031G validates the location counter classes behind this direct-geography layer: 236 independent clearable rows are Delver-countable planning rows, Angarvunde and Mistwatch are atypical clearable-but-non-counting exceptions, 10 duplicate marker rows are discovery/Explorer candidates tied to primary clearable locations, 4 secondary markers are inherited clear-state caveats, 16 AE content locations follow parent quest/property/content timing rather than Delver handling, and the checklist-only `The Chill*` row is explicitly excluded from official PS4 AE discovery/clear coverage.

## Insertion Rules

| Rule | Effect |
| --- | --- |
| Hard gates override geography. | A nearby objective still waits if it would cross level 8, 25, 27, 32, 36, 40, 46, 60, 78, 80, or 252 gates. |
| Branch-deferred rows stay in branch handling. | Hircine, Aetherial, Thirsk, Bittercup, Velehk Sain, Ghosts of the Tribunal, Civil War branch handling, and similar alternate outcomes use the TB-028 defaults and TB-029 branch prototypes rather than main-route insertion. |
| Candidate support is not availability. | A candidate base, home, merchant, spell-tome source, property, or book copy is only a possible route node after acquisition, ownership, safe-storage, source, and prerequisite validation. |
| Corridor support is not fast travel. | Carriages, ferries, roads, horses, and hubs describe logistics; Survival Mode still requires food, sleep, carry, warmth, and recovery endpoints. |
| Counts are not permission. | A block count does not mean every row is safe at the block's earliest skeleton pressure; each row still needs prerequisite, hard-gate, branch, bug, NPC, source-selection, and Survival validation. |
| Warnings are triggers, not route prose. | TB-032 records where a warning or save belongs; TB-034 still turns those triggers into numbered route steps. |
| Books/documents use title-level coverage. | Single-copy or quest-tied titles can follow their parent block; multi-copy titles wait for candidate selection unless a quest/location already fixes the source. |
| Unique items are preserved. | Do not disenchant unique items for effects; do not grab leveled, cell-locked, or branch-sensitive unique rewards before their gate. |
| Radiants use source boundaries. | Required or representative radiants insert only where the Phase 2 radiant table allows, and exact target selection stays reviewable. |
| Skill, perk, crafting, and grind work follows the TB-027/TB-031E overlay. | Route blocks now include progression slots, reset policy, underleveled fallbacks, and source-selection defaults. Exact warnings, physical availability checks, and final validation remain downstream. |

## Direct Geography Insertion Map

This table assigns direct `location` rows to their primary route-block container. Counts are queue sizes, not final clear order.

| Block | Direct rows | Corridors consumed | Cold profile | Prototype insertion rule |
| --- | ---: | --- | --- | --- |
| G02 Central carry/storage | 62 | `riverwood_helgen_road` 15; `whiterun_central_plains` 28; `rorikstead_western_road` 19 | 58 standard; 3 regional cold; 1 high elevation/mountain | Use after G00-G01 survival setup and first Whiterun handling. Keep Silent Moons/lunar-weapon handling behind level 8 and avoid carry sprawl before storage/sell-off is established. |
| G03 Southern warm expansion | 58 | `falkreath_pine_forest` 32; `ivarstead_rift_pass` 26 | 47 standard; 7 high elevation/mountain; 4 source-listed cold interior | Use as a warm-core expansion block with horse/inn support. Do not treat Bloated Man's Grotto/Hircine-sensitive state, Bolar's Oathblade, or mountain clears as casual filler before their constraints are checked. |
| G04 Riften/southeast support | 39 | `riften_rift` 39 | 35 standard; 4 high elevation/mountain | Use for Riften-side locations, Thieves Guild support, Shadowfoot/Nchuanthumz-style candidate logistics, and southeastern objectives after prerequisites. Do not start `Trinity Restored` before 32, do not take Nightingale reward handoffs before 46, and keep Dawnguard branch handling out of this block. |
| G05 Western Reach and road inns | 36 | `old_hroldan_reach_road` 18; `markarth_reach` 18 | 36 standard | Use for Markarth/Reach and road-inn sweeps with carry and bed endpoints. Keep Sky Haven Temple/Dragonbane behind level 46 and do not let Cidhna Mine, Daedric, or property/NPC conflicts become unmarked side effects. |
| G06 Eastmarch/Windhelm ferry hub | 46 | `kynesgrove_eastmarch_road` 28; `windhelm_eastmarch` 18 | 38 standard; 7 regional cold; 1 source-listed cold interior | Use for Windhelm/Eastmarch sweeps, ferry preparation, and east-road objectives. Keep Blood on the Ice, Civil War Windhelm state, and ferry/Solstheim transitions as anchored windows, not filler. |
| G07 Solitude/northwest city/coast | 67 | `solitude_haafingar` 17; `dragon_bridge_haafingar_road` 23; `morthal_marsh` 27 | 34 standard; 32 regional cold; 1 source-listed cold interior | Use for Solitude, Haafingar, Morthal, marsh, and coastal sweeps with cold/carry prep. Keep Bards instruments uncollected before assignment, finish Erikur-sensitive Thieves work before hostile Solitude states, and delay Shield of Solitude reward handoff until level 40. |
| G08 Pale/Winterhold prepared sweep | 63 | `dawnstar_pale_coast` 19; `nightgate_pale_pass` 28; `winterhold_coast` 16 | 44 regional cold; 10 standard; 9 source-listed cold interior | Use only as prepared cold/mountain sweeps. Under current Phase 2 constraints, keep Saarthal and the Forbidden Legend-linked locations out of pre-36 route prose; TB-032 should convert the source's broad approach/spawn caution into precise warnings before any exception is attempted. |
| G09 Level-36 linked-dungeon loop | 4 | `solitude_haafingar` 1; `ivarstead_rift_pass` 1; `old_hroldan_reach_road` 1; `winterhold_coast` 1 | 2 regional cold; 2 standard | Dedicated post-36 gate-extracted loop for the current Forbidden Legend/Saarthal-linked objectives; do not treat the source corridor as permission for earlier placement. |
| G10 Level-46 classic reward loop | 1 | `markarth_reach` 1 | 1 standard | Dedicated level-46 gate-extracted row for Sky Haven/Dragonbane-style handling; source corridor remains visible, but warning placement controls access. |
| G11 Dawnguard expedition | 15 | `dayspring_canyon` 2; `icewater_volkihar_ferry` 13 | 9 regional cold; 4 standard; 1 source-listed cold interior; 1 high elevation/mountain | Use after Dawnguard route support exists and the `Bloodline` hard-save structure is ready. Treat Volkihar, vampire transformation, Lost Relic cycling, and coastal/castle travel as anchored expedition work. |
| G12 Solstheim/Raven Rock spine | 54 | `raven_rock_west` 20; `thirsk_central` 16; `skaal_north` 14; `tel_mithryn_east` 4 | 49 Solstheim cold region; 5 source-listed cold interior | Use after Raven Rock support is established. Treat Severin as storage only after acquisition/storage validation, use TB-028/TB-031C Thirsk and Ralis treatment, and do not finish final Miraak before level 60. |
| G13 Separate-worldspace/AE high-risk | 2 | `manual_validation_required` 2 | 2 not comparable | Do not auto-route from corridor data. Use manual validation for Skuldafn, Deadlands, Apocrypha, Soul Cairn, Forgotten Vale, and similar spaces before any final prose. |

## Location Route Validation Overlay

TB-031G adds location clear/discovery mechanics without choosing final path order. Use `data/locations/location-route-validation.md` as the controlling route-planning artifact for these rows.

| Location family | Prototype treatment | Later validation |
| --- | --- | --- |
| Normal clearable locations | Route until the in-game `Cleared` tag appears; when a row is used for Delver, verify the `Dungeons Cleared` statistic unless the row is a documented exception. | TB-032 records concise warnings for quest/boss/report-back risks; TB-033 validates final counters. |
| Angarvunde and Mistwatch | Route for dungeon, quest, word-wall, or checklist value, but do not count toward Delver. | TB-033 validates final Delver padding without these rows. |
| Discoverable and duplicate markers | Source-listed discoverable markers can support `Explorer`; duplicate entrances are discovery candidates but share one parent clear. | TB-034 chooses entrance order; TB-033 validates `Locations Discovered`. |
| Secondary cleared markers | Giant's Grove, Klimmek's House, Shalidor's Maze, and Sundered Towers are not independent clear objectives. | TB-034 may mention them only where the parent route naturally visits the area. |
| AE content locations and no-marker rows | Follow parent quest, property, branch, or content-package timing; no-marker rows are not Explorer padding. | TB-032/TB-034 place warnings and steps from parent content, not corridor distance alone. |
| Separate worldspaces | Skuldafn, Deadlands, Apocrypha, Soul Cairn, Forgotten Vale, and similar spaces need manual access/return/recovery planning. | TB-034 final route placement; TB-033 route-state validation. |

## Route-Block Prototype

| Block | Prototype placement | Flexible insertions allowed here | Held out of this block |
| --- | --- | --- | --- |
| G00 Setup | AE install/trophy-safe mode, Survival Mode baseline, run settings, and the fixed-early support rows. | `OBJ-000479` Survival Mode, `OBJ-000702` Survival Mode Food and Warmth Consumable Set, `OBJ-000705` Camping Supplies Crafting System as setup/system coverage only. Actual camping-supply crafting waits for materials, forge/anvil access, carry capacity, and Survival need validation. | Any travel, crafting grind, branch choice, or objective acquisition that depends on in-world validation. |
| G01 Opening warm core | Opening escape, Riverwood/Whiterun approach, first proper bed/food/carry plan, and first Whiterun protected-entry caution. | Only immediate support, tutorial, first-rest, food, and local low-risk objectives that do not lock rewards, trigger branch states, or create large carry debt. | Broad central location clearing; that queue moves to G02 after survival stabilization. |
| G02 Central carry/storage | First broad warm-region insertion block. | The 62 direct central location rows; Riverwood/Whiterun/Rorikstead support objectives; early merchant, home, and food/storage candidates after validation; local book/document and unique-item rows tied to already-routed objectives. | Pre-level-8 Silent Moons lock, overbroad Thieves/Companions depth, northern travel, and unvalidated property/storage assumptions. |
| G03 Southern warm expansion | Falkreath, pine forest, Ivarstead/Rift pass, and warm-core side expansion. | The 58 direct southern location rows; Falkreath and Ivarstead local favors; Lakeview/property prerequisites where constraints permit; nearby Daedric or quest windows only when their levels and NPC dependencies are open. | Hircine/Bloated Man's Grotto state, Bolar's Oathblade, and mountain/cold interiors unless their exact constraints are checked. |
| G04 Riften/southeast support | Riften hub, southeast support, and Thieves infrastructure. | The 39 direct Riften corridor rows; Riften local services, investments, property candidates, and support objectives after prerequisite checks; safe Thieves setup before reward locks. | Starting `Trinity Restored` before 32, source-tier Nightingale Blade/Bow reward handoffs before 46, Dawnguard branch routing, and Aetherial branch/default handling from TB-028/TB-029. |
| G05 Western Reach and road inns | Markarth, Reach, Old Hroldan, road-inn loops, and western Daedric/property windows. | The 36 direct western rows; Markarth/Reach side objectives; western book, unique-item, and location rows when constraints are clear; Hendraheim-style candidates only after start/acquisition validation. | Sky Haven Temple before 46, unchecked Cidhna/Madanach outcomes, and branch-sensitive Daedric choices. |
| G06 Eastmarch/Windhelm ferry hub | East road, Windhelm services, ferry gateway, and east-side state management. | The 46 direct Eastmarch rows; Windhelm merchant/service objectives; ferry-prep objectives; east-road books/items and local favors after NPC/bug constraints. | Windhelm Civil War end-state, unmarked Blood on the Ice risk, broad Solstheim cleanup, and ferry travel without cold/rest/carry plan. |
| G07 Solitude/northwest city/coast | Solitude, Haafingar, Morthal, Dragon Bridge, marsh, and coastal prep. | The 67 direct northwest rows; Solitude/Bards/Thieves support only with instrument and Erikur constraints respected; Morthal/Haafingar property and service candidates after validation. | Shield of Solitude reward before 40, Bards instruments before assignment, hostile Solitude overlap, and coast/cold travel without expedition support. |
| G08 Pale/Winterhold prepared sweep | Dawnstar, Nightgate, Winterhold, College access, and cold-north sweeps. | The 63 direct northern rows only as prepared sweeps; Dawnstar/Winterhold service objectives; College access that does not cross the current level-36 linked-dungeon lock; cold-region books/items when the route is already there. | Pre-36 `Lost Legends`, Folgunthur, Saarthal, Geirmund's Hall, Reachwater Rock, broad College depth, and casual cold-interior detours. |
| G09 Level-36 linked-dungeon loop | Dedicated post-36 Forbidden Legend/Saarthal-linked loop. | Move the relevant linked-dungeon objectives from their regional corridors into one controlled loop after level 36, with food, bed, warmth, carry, and exact access validation. | Any pre-36 read, exterior spawn/approach, map-marker discovery, entry, loot, or quest-state lock for the linked dungeons under current constraints; TB-032 records the exact warning triggers. |
| G10 Level-46 classic reward loop | Maximum-tier classic reward unlock block. | Riftweald/Chillrend, Sky Haven/Dragonbane, source-tier Nightingale reward handoffs, and other reward-locked objectives once level 46+ is confirmed. | Final Miraak before 60, Legendary Dragon before 78, Ebony Warrior before 80, and branch defaults. |
| G11 Dawnguard expedition | Dawnguard main-route chain, Fort Dawnguard support, Volkihar branch save, coastal/castle loops. | The 15 Dawnguard/coastal direct location rows; finite Dawnguard chains; representative/required Dawnguard radiants only within source boundaries; Fort Dawnguard service/support objectives. | Volkihar branch content in main continuity, vampire perk timing without TB-027, and Aetherial reward branches without TB-028/TB-029 hard-save handling. |
| G12 Solstheim/Raven Rock spine | Raven Rock logistics, Solstheim progression, island sweeps, Black Books, Skaal/Tel Mithryn/Thirsk/Kolbjorn windows. | The 54 Solstheim direct rows; Raven Rock/Tel Mithryn/Skaal local objectives; Black Book and Dragonborn objectives as their prerequisite chain permits; island support rows after ferry and storage validation. | Final Miraak before 60, broad island cleanup before support, Thirsk default, Ralis outcome, and Severin storage before validation. |
| G13 Separate-worldspace/AE high-risk expeditions | Manually validated separate-worldspace and high-risk AE blocks. | Apocrypha, Soul Cairn, Forgotten Vale, Skuldafn, Deadlands, and high-risk AE objective bundles only after manual access, return, rest, and reward checks. | Any automatic insertion based on Skyrim/Solstheim corridor proximity. |
| G14 Late cleanup by corridor | Final corridor cleanup, counters, collection reconciliation, and late progression tail. | Remaining safe rows after TB-027, TB-028, and TB-031A-TB-031J clarify skills, branch defaults, checklist coverage, and source readiness; TB-032 still places warning text. A row may enter G14 only with an explicit late-level, checklist-finalization, post-branch, post-progression, or source-selection reason. | Using cleanup as a substitute for missing route placement, underleveled gate recovery without a plan, unresolved checklist source-readiness, or unsourced checklist assumptions. |

## Progression Overlay

TB-027 adds progression pressure to the existing `G00` through `G14` frame without turning this file into a final route. The route should place planned level-ups at verified proper beds, put crafting blocks near storage/stations/merchants, and keep hard reward gates visible when adding any training or grind block.

| Block | Progression slot | Allowed support | Do not do here |
| --- | --- | --- | --- |
| G00 | Setup only. | Establish official AE, Survival, Legendary, and trophy-safe rules. | No in-world crafting, leveling, grinding, or objective acquisition. |
| G01 | Opening survival and basic combat competence. | Food, first bed, first sell-off, tutorial-scale crafting, and first carry discipline. | Broad crafting grind, skill-book sweep, cold travel, or AE difficulty spike routing. |
| G02 | First central training/crafting/storage block. | Low-risk Artificer/Hard Worker actions, basic food/crafting, first material and disposable-source storage, light paid training after sleep. | Pre-level-8 Silent Moons handling or final-max crafting. |
| G03 | Warm-route durability and material staging. | Southern inns/vendors, safe local training, food, ore/wood/cooking support, property-material staging after constraints. | Hircine/Bloated Man's Grotto state or Bolar's Oathblade as casual grind support. |
| G04 | Riften economy and stealth support. | Sneak, Pickpocket, Speech, Thieves support, sales loops, and later investment preparation. | `Trinity Restored` before 32, repeated Speech reset, or investment sweep before Speech 70/Investor. |
| G05 | Western material/combat readiness. | Markarth services, storage/sell-off, Smithing/material staging, and road-inn recovery. | Sky Haven/Dragonbane, unchecked Cidhna/Daedric branch states, or combat-skill resets before hard Reach content. |
| G06 | Eastmarch services and ferry preparation. | Windhelm services, merchant/training review, ferry gold, hot soup ingredients, and carry relief. | Solstheim broad cleanup or any reset immediately before ferry/cold travel. |
| G07 | Solitude Speech/service and coastal readiness. | Speech/Bards/service support, coastal cold prep, and investment preconditions after NPC checks. | Falk reward before 40, Bards instrument pickup before assignment, or Speech reset before selling/investment work. |
| G08 | College/mage and cold-region preparation. | Magic training, spell acquisition, cold expedition prep, and Oghma acquisition staging if the quest path is being resolved. | Oghma read/use, pre-36 linked-dungeon handling, or casual cold-interior detours. |
| G09 | Post-36 linked-dungeon progression block. | Rested/fed/warm dungeon loops, carry emptying, and post-loop sell-off/training. | Any reset or pre-36 linked-dungeon state change. |
| G10 | Post-46 classic reward and late build review. | Maximum-tier reward acquisition, bed/storage/merchant review, moderate crafting updates, and late reset infrastructure evaluation. | Resets before reward dungeons or final crafting that flattens the intended difficulty curve. |
| G11 | Dawnguard, transformation, and late combat support. | Dawnguard services, Restoration/Archery growth, source-bounded radiants, and werewolf/vampire perk work inside validated state windows. | Resetting active offense, armor, Restoration, or transformation support before hard Dawnguard content. |
| G12 | Solstheim systems and late magic/crafting. | Raven Rock restock, Staff Enchanter, Imbuing Chamber, Black Book systems, island ingredients, and first cautious late reset cycles after infrastructure. | Final Miraak before 60 or Severin storage before validation. |
| G13 | Manual high-risk expedition support. | Sleep before entry, exact access/exit plan, light inventory, recovery endpoint, and manual objective validation. | Resets immediately before or inside separate-worldspace/high-risk expeditions. |
| G14 | Final all-perks and completion progression. | Repeated Legendary reset loop, final skill recovery, level 252, all 251 perk ranks, investments, enchantment learning, alchemy effects, final crafting, skill-book/Oghma finishers, and checklist synchronization. | Treating cleanup as a substitute for route placement, ending with any reset skill below 100, or using excluded exploit loops as baseline. |

## Counter Mechanics Overlay

TB-031F adds counter/action checkpoints without choosing final step numbers. Use `data/checklist-mapping/counter-coverage-plan.md` as the controlling route-planning artifact for these rows.

| Counter/action family | Prototype treatment | Later validation |
| --- | --- | --- |
| Side/misc/trophy counters | Track `Sideways`, `Hero of the People`, `Thief`, `Snake Tongue`, `Golden Touch`, `Dragon Hunter`, `Standing Stones`, and trophy-pop fallback saves as explicit checkpoints, not incidental expectations. | TB-032 records warnings and saves; TB-033 validates final counter totals and trophy pops. |
| Location counters | Route enough clearable/discoverable locations for `Delver`, `Explorer`, and Solstheim Explorer, but mark completion only after observed clear/discovery increments. | TB-031G has validated clear/discovery mechanics; TB-033 validates final observed totals. |
| Skill-book and progression counters | Reader follows TB-031E copy/read policy and all 90 skill-book objectives; trophy check occurs after 50 unique titles. | TB-033 validates Reader plus final all-skills/all-perks state. |
| Radiant and faction counters | Thieves Guild restoration uses city tallies plus a separate 125-job total; Dawnguard `Lost Relic` records all filler radiants until all three relics are obtained. | TB-034 places loops; TB-033 verifies restoration, safe/display, relic, and filler records. |
| Activity systems | Hard Worker, Artificer, Fishing, cutting lumber, and milling are route-planning actions tied to existing support blocks; lumber and milling remain support-only unless final checklist proof needs cues. | TB-034/TB-037 turn them into checklist cues only where needed. |
| TB-031F/TB-031J source-readiness rows | `Rebuilding the Blades` and `Dragon Hunting` are branch-only Blades rows; `Archery Practice`, `Scare My Enemy`, `Firebrand Wine Case`, and `Map of Dragon Burials` now have source-backed main-route handling. TB-031J resolves the remaining queue: 75 main-route mappings, 1 BR-007 branch mapping for `Reclamation Priest's Journal (AE)`, and 2 explicit exclusions. | TB-033 validates branch/main continuity and final checklist coverage; no `source_readiness_required` checklist rows remain. |

## Warning and Hard-Save Overlay

TB-032 adds warning placement at the route-block level without writing final itinerary steps. A warning row is eligible only when an existing source-backed constraint, branch prototype, counter plan, or location-validation rule already supports it.

| Warning rule | Route handling |
| --- | --- |
| Save before irreversible or branch state. | Name the hard save before the choice, play any branch first, verify branch-exclusive state, reload, then continue canonical continuity. |
| Use exact trigger verbs. | Prefer `first enter`, `read`, `start`, `accept reward`, `loot/claim`, `complete battle`, `assign role`, `consume item`, and `verify trophy` over broad wording. |
| Keep warning text local. | Place the warning immediately before the action that can cross the gate, not at the beginning of a distant section. |
| Separate warnings from final pathing. | TB-032 records trigger placement; TB-034 still decides road/entrance order, step numbers, restock stops, and checklist cues. |
| Do not invent unsourced hazards. | If a row lacks a source-backed constraint, do not create a speculative warning. Mark it for TB-033 validation instead. |
| Preserve clean continuity. | Branch and trophy saves must reload back to the canonical state before the main route continues. |

### Gate and Entry Warnings

| Route block | Trigger | Warning placement | Source support |
| --- | --- | --- | --- |
| G00 | Setup before gameplay | Confirm official AE bundle, no non-AE Creations/mods, Legendary, Survival Mode, and trophy-safe save before routing any objective. | `SN-000101`, `SN-000115` |
| G01-G02 | First Whiterun visit | Before leaving first Whiterun visit, handle or deliberately preserve Amren/Ysolda first-visit favor dialogue; do not treat broader favor rows as proven locks. | `SN-000096` |
| G02 | Silent Moons Camp | Do not first loot/clear Silent Moons before level 8+; if touched too early, require respawn/reset validation before Lunar weapon collection. | `SN-000093`, `SN-000094` |
| G03 | Bloated Man's Grotto / Hircine | Acquire Bolar's Oathblade and normal grotto clear state before starting `Ill Met By Moonlight` if preserving Sinding/Ring continuity. | `SN-000095`, `SN-000098` |
| G03 | Largashbur | Do not casually approach at level 9+ unless ready to protect the Orc NPCs during the opening giant attack. | `SN-000100`, `SN-000107` |
| G04 | `Trinity Restored` | Do not start the quest before level 32 if preserving maximum Nightingale Armor. | `SN-000092` |
| G04/G10 | Nightingale Blade/Bow rewards | Do not accept the `Hard Answers` or `Blindsighted` reward handoffs before level 46 unless a later explicit tradeoff is accepted. | `SN-000092` |
| G04/G14 | Amulet of Articulation | Make `HS-TG-ARTICULATION-REWARD` before Brynjolf's Guild Master reward conversation; reload until the selected strongest version is awarded, or record an explicit final-route tradeoff if accepting a random version. | `SN-000092` |
| G05/G10 | Sky Haven Temple | Do not first enter Sky Haven Temple before level 46 if preserving maximum Dragonbane. | `SN-000092`, `SN-000094` |
| G05 | Cidhna Mine | Before Shrine of Talos arrest, report active Thieves Guild special jobs, dismiss vulnerable pets/animals, hard save, and verify inventory/quest state afterward. | `SN-000109` |
| G06 | Blood on the Ice / Hjerim | Keep Blood on the Ice in one controlled Windhelm block before Civil War Windhelm end-state, Dragonborn main start, or Dark Brotherhood Nilsine fallout; save before Hjerim entry and purchase/furnishing. | `SN-000109`, `SN-000066`, `SN-000074` |
| G07 | Shield of Solitude | Do not take Falk's final reward for `The Wolf Queen Awakened` before level 40. | `SN-000092` |
| G07 | Bards College instruments | Do not collect King Olaf's Verse, Finn's Lute, Pantea's Flute, or Rjorn's Drum before assignment; save before induction and each instrument dungeon. | `SN-000018`, `SN-000109` |
| G08-G09 | Forbidden Legend linked state | Do not read `Lost Legends`, approach/spawn, enter, loot, or clear Folgunthur, Saarthal, Geirmund's Hall, or Reachwater Rock before level 36 under current constraints. | `SN-000092`, `SN-000094` |
| G08 | Mage's Circlet | Do not report/claim `Good Intentions` reward from Savos before level 25. | `SN-000092` |
| G08 | The Pale Blade / Frostmere | Do not claim/resolve The Pale Blade before level 27; treat Frostmere Crypt separately as a Kharjo nonrespawning-target warning, not as a confirmed Pale Blade cell-entry lock. | `SN-000092`, `SN-000094`, `SN-000096` |
| G10 | Riftweald Manor | Do not first enter Riftweald Manor before level 46 if preserving maximum Chillrend. | `SN-000092`, `SN-000094` |
| G12-G13 | Miraak finale | Do not finish the final Miraak battle or make the corpse appear before level 60 if preserving maximum Miraak equipment. | `SN-000092`, `SN-000094` |
| G14 | Legendary Dragon / Ebony Warrior | Do not hunt Legendary Dragons before level 78 or engage Ebony Warrior before level 80; save before each late one-shot combat/trophy action. | `SN-000103`, `SN-000105` |
| G14 | All-perks completion | Do not treat all-perks cleanup as complete until level 252+, all 251 normal perk ranks, all skills recovered to 100 after Legendary resets, and final progression validation pass. | `SN-000119` through `SN-000122`, `SN-000126` |

### Branch and Outcome Saves

| Hard save | Trigger placement | Canonical continuation after branch audit | Source support |
| --- | --- | --- | --- |
| `HS-CW-BEFORE-FACTION-OATH` | Before irreversible Civil War faction oath/commitment. | Reload and join Imperial; preserve War Hero/Season Unending saves. | `SN-000097`, `SN-000102` |
| `HS-DG-BLOODLINE` | Before Lord Harkon's `Bloodline` faction choice. | Reload and refuse the gift for Dawnguard; Volkihar branch must verify spouse-state dependency for `The Gift` or mark it conditional. | `SN-000097`, `SN-000105`, `SN-000114` |
| `HS-DB-ABANDONED-SHACK` | Before Abandoned Shack commitment. | Reload and join Dark Brotherhood; complete/skip `Delayed Burial` intentionally before commitment. | `SN-000097`, `SN-000100`, `SN-000102` |
| `HS-MQ-PAARTHURNAX` | Before killing Paarthurnax. | Reload and preserve Paarthurnax; Blades rebuilding and dragon hunt remain branch-only checklist rows. | `SN-000097`, `SN-000112`, `SN-000127` |
| `HS-DRAGONBORN-THIRSK-CHOICE` | Before Mead Hall side choice and before hall assault. | Reload and complete Nord-side `Retaking Thirsk`; verify Riekling branch occupant/follower state before reload. | `SN-000034`, `SN-000099`, `SN-000111` |
| `HS-AE-GHOSTS-TEMPLE` | Before Ghosts heretic join/infiltrate versus destruction commitment. | Reload and keep join/infiltrate path; branch records destroy-heretics state and `Reclamation Priest's Journal (AE)` coverage. | `SN-000099`, `SN-000129` |
| `HS-AE-BITTERCUP-ALTAR` | Before Bittercup altar path choice. | Branch Power, reload; branch Nothing, reload; continue Fortune on main save for Master Transmute coverage. | `SN-000099` |
| `HS-DAEDRIC-BLACK-STAR` | Before final star reward choice. | Reload and keep The Black Star; record Azura's Star/Aranea outcome on branch. | `SN-000098`, `SN-000104` |
| `HS-DAEDRIC-CLAVICUS` | Before final Barbas choice. | Reload, spare Barbas, take Masque; do not count Rueful Axe for Oblivion Walker. | `SN-000098`, `SN-000104` |
| `HS-DAEDRIC-HIRCINE-GROTTO` | Before Hircine outcome after preserving Bolar/grotto state if needed. | Reload and keep Ring of Hircine; Savior's Hide is branch, dual-artifact method is appendix/audit only. | `SN-000095`, `SN-000098`, `SN-000104` |
| `HS-DAEDRIC-MEHRUNES-SHRINE` | Before Silus shrine decision. | Reload and kill Silus/reforge Mehrunes' Razor on main save. | `SN-000098`, `SN-000104`, `SN-000107` |
| `HS-DAEDRIC-NAMIRA-FEAST` | Before Namira feast / Verulus outcome. | Reload and complete artifact-safe Ring of Namira path. | `SN-000098`, `SN-000104`, `SN-000107` |
| `HS-DAEDRIC-VAERMINA-SKULL` | Before Erandur final choice. | Reload and take Skull of Corruption on main save. | `SN-000098`, `SN-000104`, `SN-000107` |
| `HS-DG-AETHERIUM-FORGE` | Before forging the one Aetherial reward. | Audit Staff and Shield on branches, reload, craft Aetherial Crown on main save. | `SN-000099`, `SN-000105` |
| `HS-TROPHY-MASTER-CRIMINAL` | Before deliberate all-holds bounty escalation. | Stage controlled 1000-gold bounties in all nine holds without killing quest-critical NPCs, verify trophy pop, reload clean continuity. | `SN-000103`, `SN-000127` |
| `HS-RIFT-FROST-LETRUSH` | Before Frost handoff/outcome. | Keep Frost on main save; alternate handoff remains optional unless TB-033 finds a checklist gap. | `SN-000099`, `SN-000107` |
| `HS-DRAGONBORN-UNEARTHED-RALIS` | Before Ralis final outcome. | Spare Ralis on main save; kill outcome remains optional unless TB-033 finds a checklist gap. | `SN-000099`, `SN-000107`, `SN-000111` |
| `HS-COLLEGE-VELEHK-SAIN` | Before Velehk Sain outcome. | Release Velehk for hidden treasure path; kill outcome remains optional note. | `SN-000099` |
| `HS-AE-CIVIL-WAR-CHAMPIONS` | Before Battle of the Champions side/outcome if final route separates it. | Keep Imperial-aligned handling with Civil War main route; TB-033 verifies equipment availability. | `SN-000099` |

### Quest, NPC, Bug, and Counter Warnings

| Route area | Trigger | Warning placement | Source support |
| --- | --- | --- | --- |
| Civil War/main quest | Season Unending or hold handoff | Hard save before any Season Unending or Civil War hold handoff that could skip the War Hero fort battle. | `SN-000010`, `SN-000097`, `SN-000102` |
| Companions | Post-`The Silver Hand` radiants | Complete the selected two windowed representative radiants before `Blood's Honor`; do not force a restart solely for Hired Muscle. | `SN-000112`, `SN-000127` |
| Companions | Werewolf cure or Vampire Lord conversion | Finish werewolf perk/totem work before permanent cure or vampire conversion; final mortal state waits until both transformation systems are complete. | `SN-000105`, `SN-000112` |
| Thieves Guild | `The Dainty Sload` and Solitude restoration | Complete Solitude special job and Erikur-dependent work before `Bound Until Death`; save before Delvin job start, Balmora Blue pickup, ship boarding, and final returns. | `SN-000102`, `SN-000107`, `SN-000109` |
| Solitude NPC dependencies | Vittoria Vici and Captain Aldis favors | Complete `The Spiced Wine` before `Bound Until Death`; complete Captain Aldis-linked favors before the Stormcloak branch reaches Battle for Solitude, and do not leave either as late cleanup. | `SN-000100`, `SN-000107` |
| Thieves Guild | Delvin/Vex side jobs | Save before requesting jobs; reject/reload non-target city jobs during restoration, reject/reload Raven Rock Bedlam, track 125-job total separately. | `SN-000112`, `SN-000127` |
| Dark Brotherhood/Falkreath | Helvard contract | Secure Lakeview/Falkreath land prerequisites before killing Helvard; hard save if property state is not verified. | `SN-000100`, `SN-000107` |
| Falkreath property/favor | Siddgeir rare gift and Hearthfire letter | Handle Siddgeir's Black-Briar Mead favor, or consciously skip it, before the level-9 Hearthfire letter and land chain can replace the favor path; secure Lakeview state before Helvard. | `SN-000100`, `SN-000107` |
| Whiterun quest start | `The Whispering Door` | Start or secure the Hulda/Ysolda/Balgruuf/Nelkir route before risky Whiterun violence, civil-war disruption, or long-delayed cleanup. | `SN-000100`, `SN-000107` |
| Main quest follow-up | Malborn after `Diplomatic Immunity` | Complete Malborn's Windhelm follow-up during the Eastmarch pass after `Diplomatic Immunity`; do not defer it to late cleanup. | `SN-000021`, `SN-000107` |
| Daedric | Boethiah sacrifice | Pick a deliberate nonessential sacrifice, strip inventory, avoid Companion leaders and service-critical NPCs, and save at the Sacellum. | `SN-000100`, `SN-000106`, `SN-000107` |
| Daedric | Logrolf / Molag Bal | Save before freeing Logrolf and before Abandoned House finale; do not kill him while captive. | `SN-000100`, `SN-000107`, `SN-000109` |
| Daedric/College | Septimus / Oghma | Do not attack Septimus; after opening the cube, resolve Oghma acquisition before long delay or cell-respawn exposure; read/use timing follows TB-031E/TB-033. | `SN-000100`, `SN-000107`, `SN-000126` |
| Dawnguard | Auriel's Bow trophy action | After acquiring Auriel's Bow, save and shoot the sun with valid special arrows before risky storage, sale, arrest, or long post-finale delay. | `SN-000105` |
| Dawnguard | Lost Relic cycling | Record actual filler radiants until all three relics are obtained; avoid Movarth's Lair for `Cleansing Light` if possible. | `SN-000114`, `SN-000127` |
| Dawnguard | `A New You` | Route face change before Vampire Lord phase or after curing vampirism. | `SN-000105` |
| Solstheim | `A New Source of Stalhrim` | On first return after `The Fate of the Skaal`, let Deor/Fanari finish, start/secure the quest, save before Abandoned Lodge, and verify stalhrim crafting unlock. | `SN-000100`, `SN-000105`, `SN-000107`, `SN-000111` |
| Solstheim | `Served Cold` / Severin Manor | Save before Ulen tomb surveillance, Severin infiltration, and finale; verify ownership, beds, containers, and storage before using Severin as a base. | `SN-000105`, `SN-000111` |
| Solstheim | `Reluctant Steward` / Varona | Save before asking Neloth and before body search; follow marker immediately and verify staff enchanter/Black Book access. | `SN-000111` |
| Solstheim | `Old Friends` | Save before Neloth locator and Ildari confrontation; verify marker and heart-objective progression. | `SN-000111` |
| Solstheim | `Unearthed` | Save before each excavation payment and re-entry; collect phase relics before funding next stage; leave final barrow only after Black Book/relic/word-wall verification. | `SN-000111`, `SN-000099` |
| Dragonborn counter | Dragonrider | Save before each Bend Will ride, use only valid rideable dragons/worldspaces, and verify dismount/camera/counter before counting. | `SN-000105`, `SN-000111`, `SN-000127` |
| Hearthfire | Construction, stewards, bards, furnishings | Save before steward assignment, bard hire, major wing construction, Small House remodel, and steward furnishing; verify services before relying on them. | `SN-000075`, `SN-000106`, `SN-000110` |
| Family | Marriage, adoption, moves, child pets | Prepare valid child room first; save before marriage/adoption/move/pet dialogues and verify spouse/children arrive at Tundra Homestead. | `SN-000030`, `SN-000106`, `SN-000110` |
| AE pets | Elytra nymphs | Save before freeing each nymph and verify recruit/follower dialogue immediately; keep PS4 AE route-test flag for TB-033. | `SN-000038`, `SN-000111` |
| Kharjo/favors | Amulet of the Moon target locations | Accept/resolve or reroll Kharjo before clearing Broken Oar Grotto, Cracked Tusk Keep, or Frostmere Crypt. | `SN-000096`, `SN-000107` |
| Counters | Trophy-pop fallback | Save before one-shot or long-counter completions; if the trophy does not pop, reload and repeat the verified action instead of continuing silently. | `SN-000101`, `SN-000103`, `SN-000127` |
| Counters | `Snake Tongue`, `Thief`, `Hard Worker`, `Artificer` | Label reserved action slots and verify counters/trophies after the specific action types, not from incidental progress. | `SN-000103`, `SN-000127` |
| Counters | Representative brawl | Complete the selected brawl in a controlled no-follower Whiterun window and verify post-fight dialogue so the route does not turn the brawl into combat or crime. | `SN-000089`, `SN-000108`, `SN-000113` |
| Locations | Delver / Explorer | Count observed clear/discovery increments; do not count Angarvunde or Mistwatch for Delver and do not double-count duplicate entrances as extra clears. | `SN-000077`, `SN-000078`, `SN-000128` |
| Survival | Prepared sweeps | Before cold, mountain, coastal, separate-worldspace, or long-dungeon blocks, require sleep, food/hot soup, warmth, cure/healing, carry space, and a return/rest endpoint. | `SN-000115` through `SN-000118` |

## Underleveled Fallback Policy

Use fallback blocks only when the player reaches a gate underleveled. Each fallback must preserve the trigger listed in the Mandatory Holds table.

| Gate | Preferred fallback | Still forbidden |
| --- | --- | --- |
| Level 8 | G02 local objectives, early bed/training, low-risk food/crafting/material work. | Silent Moons first loot/clear. |
| Level 25 | Warm G02-G04 filler, safe faction setup, modest crafting/sales, and slept training. | `Good Intentions` reward report or Oghma read/use. |
| Level 27 | Continue safe warm/city-backed filler and training. | The Pale Blade claim/resolution or unvalidated Frostmere/Kharjo handling. |
| Level 32 | Riften/Thieves support that stops before the gate, plus city services and safe regional objectives. | Starting `Trinity Restored`. |
| Level 36 | Warm/city-backed objectives, safe non-linked College support, crafting/training near beds. | `Lost Legends` or linked-dungeon read/approach/entry/loot state under current constraints. |
| Level 40 | G09 post-36 work, Solitude support, and safe regional/faction objectives. | Falk's final Shield of Solitude handoff. |
| Level 46 | Post-40 city/faction/regional support and modest crafting, while late reward locations remain closed. | Riftweald Manor, Sky Haven Temple, and Nightingale Blade/Bow handoffs. |
| Level 60 | G10 rewards, Dawnguard, supported Solstheim side work, high-level AE after access checks, and bounded training/crafting. | Final Miraak battle/corpse appearance. |
| Level 78 | Post-60 Dragonborn/AE/Black Book work, transformation perk work, late crafting, and first repeatable reset cycles if infrastructure exists. | Legendary Dragon hunt or resets that remove combat readiness. |
| Level 80 | Short late training/crafting/cleanup or continued safe reset recovery. | Ebony Warrior trigger/engagement. |
| Level 252 | G14 reset loop, final training below 90, skill-book/Oghma finishers, crafting/sales, and checklist-safe cleanup. | Repeated Lockpicking/Speech reset baseline, exploit loops, or incomplete post-reset skill recovery. |

## Legendary Reset Policy

| Reset group | Skills | Prototype treatment |
| --- | --- | --- |
| Preferred repeated pool | Alchemy, Smithing, Enchanting, Alteration, Conjuration, Illusion | Use late, mainly G14, after materials, spells, gold, beds, storage, and alternate combat options exist. |
| Conditional pool | Restoration, Sneak, Pickpocket | Use only after faction/trophy/state risks are controlled and safer reset pools are not enough. |
| Emergency combat/defense pool | Archery, One-handed, Two-handed, Destruction, Block, Heavy Armor, Light Armor | Avoid repeated resets; never hollow out active offense and defense before hard combat. |
| Avoid repeated baseline | Lockpicking, Speech | Do not use as the normal all-perks engine; at most one late explicit exception after route proof. |

## Non-Geographic Queue Treatment

| Queue | Rows | TB-026 disposition |
| --- | ---: | --- |
| Single support candidates | 830 | Attach when the support row is already inside a safe route block. This covers many book/document titles, crafting unlock rows, skill/perk support rows, properties, merchant investments, and a few quest/unique/trophy support rows. |
| Multiple support candidates | 319 | Do not choose a canonical copy/source here unless TB-031E already selected it. Later location/readiness/validation/final-route passes choose the local safest remaining candidate after skill, checklist, and warning needs are known. |
| No route candidate data | 1,098 | Keep dependency-driven. Quest chains, unique-item rewards, collectible sets, AE package parents, powers, radiants, trophy counters, pets/mounts, and relationships should move with their anchor or later checklist/default pass. |
| Constraint-backed flexible rows | 1,082 | Do not treat flexibility as permission to route blindly. Inspect the linked constraint source before final insertion or warning text. |
| Flexible rows without linked constraints | 1,534 | Eligible for local insertion only if prerequisites, geography, and Survival support are clear. |

## Support Objective Policy

| Objective class | Prototype policy |
| --- | --- |
| Properties and bases | Place acquisition opportunities in their regional block, but do not use a candidate base as rest/storage until acquisition, ownership, safety, and storage behavior are validated. |
| Merchant investments and services | Attach to the relevant city/hub block if the merchant/service remains available and the economy route supports it; TB-027 places them after Speech 70/Investor and before any Speech reset, while TB-031E chooses the exact merchant circuit. |
| Skill books | Choose one copy per title later. If a skill book is fixed by a quest/location already in a block, mark it as a local pickup candidate; otherwise keep it in the candidate-selection queue. |
| Spell tomes | Vendor/multiple-source tomes use TB-031E shopping/source choices inside the TB-027 skill plan; fixed-copy tomes can follow their validated location block. |
| Quest and AE documents | Single-source quest documents follow the parent quest or location; multi-source titles wait for source selection. Oghma Infinium acquisition and read/use timing remain separated. |
| Unique items | Acquire with the parent quest/location if no leveled, cell-entry, branch, NPC, or bug constraint blocks it. Preserve unique items unless the specification later creates an explicit exception. |
| Crafting unlocks | Use the TB-027 block overlay and TB-031E source-selection defaults for shop/craft/disenchant/alchemy/Smithing/Enchanting/ingredient loops. Do not use a unique-item disenchant as the baseline; final route still validates physical source-item availability. |
| Radiants | Insert required radiants only inside the relevant faction/window. Representative radiants should use source-approved boundaries and local targets, not random grind assumptions. |
| Collectibles, stones, shouts, and powers | Insert opportunistically when the corridor is already safe. TB-031F supplies counter checkpoint rules and TB-031G supplies location validation mechanics; final route placement and checklist synchronization remain TB-033/TB-034/TB-037. |
| AE Creations | Respect `ae-creation-start-triggers.md`. Vendor/crafting/content-package rows can attach to support blocks; courier, high-level, prerequisite, bug-sensitive, or branch-sensitive rows wait for their gate. |

## Mandatory Holds

| Hold | Trigger to avoid before release | Release condition |
| --- | --- | --- |
| Silent Moons/Lunar weapon pool | First loot/clear state that can affect Lunar weapon availability. | Level 8+ and exact camp/item handling validated. |
| Mage's Circlet | Reward report/claim before maximum-tier threshold. | Level 25+ if preserving maximum tier. |
| The Pale Blade | Reward claim/resolution before maximum-tier threshold. | Level 27+ if preserving maximum tier and Kharjo/target risks are clear. |
| Nightingale Armor | Starting `Trinity Restored` too early. | Level 32+. |
| Forbidden Legend linked dungeons | Reading `Lost Legends` or approaching Folgunthur, Saarthal, Geirmund's Hall, or Reachwater Rock too early under current constraints. | Level 36+ or later explicit source review changes the policy. |
| Shield of Solitude | Final Falk reward handoff too early. | Level 40+. |
| Chillrend and Dragonbane | First entering Riftweald Manor or Sky Haven Temple too early. | Level 46+. |
| Nightingale Blade/Bow | Accepting source-tier reward handoffs too early. | Level 46+ unless a later explicit tradeoff changes the policy. |
| Amulet of Articulation | Brynjolf reward conversation without a save/reload or accepted random-version policy. | `HS-TG-ARTICULATION-REWARD` before the reward conversation, unless final route explicitly accepts a random version tradeoff. |
| Miraak equipment | Final Miraak battle/corpse appearance too early. | Level 60+. |
| Legendary Dragon | Legendary Dragon hunt too early. | Level 78+ and combat-ready block. |
| Ebony Warrior | Ebony Warrior objective too early. | Level 80+ and combat-ready block. |
| All perks | Treating cleanup as final perk completion. | Level 252 plan and post-Legendary skill recovery from TB-027/TB-031E. |

## Source Support

| Claim family | Source support |
| --- | --- |
| Hub/corridor geography and cold/access support | `data/locations/location-geography.csv`; `sources/source-notes/SN-000124-hub-corridor-geography-support.md` |
| Survival Mode food, sleep, cold, carry, and travel-service constraints | `data/constraints/survival-mode-constraints.md` (`SN-000115` through `SN-000118`) |
| Leveled reward thresholds and reward timing | `data/constraints/leveled-unique-items.md` (`SN-000092`, `SN-000093`) |
| Cell-entry, location-spawn, quest-start, and reward-lock warnings | `data/constraints/cell-entry-locks.md` (`SN-000094` through `SN-000096`) |
| AE Creation start and prerequisite gates | `data/constraints/ae-creation-start-triggers.md` (`SN-000090`, `SN-000091`) |
| Branch, conflict, and hard-save treatment | `data/constraints/quest-conflicts-hard-saves.md` (`SN-000097` through `SN-000100`) |
| Trophy dependencies and counter pressure | `data/constraints/trophy-dependencies.md` (`SN-000101` through `SN-000105`) |
| NPC, role, service, trainer, property, and favor dependencies | `data/constraints/npc-dependencies.md` (`SN-000106` through `SN-000108`) |
| Bug-prone quest mitigation | `data/constraints/bug-prone-quests.md` (`SN-000109` through `SN-000111`) |
| Radiant quest boundaries | `data/constraints/radiant-boundaries.md` (`SN-000112` through `SN-000114`) |
| Skill, perk, leveling, crafting, and all-perks planning | `data/constraints/skill-perk-leveling-plan.md` (`SN-000119` through `SN-000122`) |
| Checklist/trophy counter mechanics and route actions | `data/checklist-mapping/counter-coverage-plan.md`; `sources/source-notes/SN-000127-checklist-counter-route-mechanics.md` |
| Location route validation and Delver/Explorer mechanics | `data/locations/location-route-validation.md`; `sources/source-notes/SN-000128-location-route-validation.md` |
| Checklist source-readiness resolutions | `data/checklist-mapping/source-readiness-resolutions.csv`; `sources/source-notes/SN-000129-checklist-source-readiness-forward-review.md` |

## Handoff to Later Passes

TB-027 is integrated at the block layer. Later passes should not treat that as final route prose.

* TB-028/TB-029 have chosen branch defaults and branch prototypes; use those files for branch-sensitive artifact, transformation, faction-state, or alternate-reward windows.
* TB-031E has chosen exact skill-book copies, spell-tome sources, disposable enchantment source families, alchemy source methods, investment circuit, crafting outputs, and progression cues.
* TB-031F has chosen counter/action policy, and TB-031G has validated location clear/discovery mechanics, duplicate/secondary markers, content-location treatment, and coordinate exception rules. Final entrance/path order still belongs to TB-034, and final observed totals still belong to TB-033.
* TB-031J has resolved the remaining checklist source-readiness rows; do not route from any historical `source_readiness_required` bucket.
* TB-032 has added the warning and hard-save overlay above. TB-034 still turns those warning triggers into step-numbered route instructions.
* TB-033 must validate the finished prototype against all constraints, including level gates, skill 100 recovery after Legendary resets, level 252+, all 251 perk ranks, investments, enchantment learning, alchemy effects, practical crafting systems, and Survival logistics.
