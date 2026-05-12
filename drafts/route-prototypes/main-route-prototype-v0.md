# Main Route Prototype v0

Status: TB-026 complete, with machine-readable objective assignments in `data/route-planning/prototype-objective-block-map.csv`.

This is a Phase 7 flexible-objective insertion prototype. It is not final guide prose, not pathfinding, not a numbered itinerary, and not a checklist coverage matrix.

The purpose of this pass is narrower: place safe objective queues into the Survival Mode route-block frame from `drafts/route-prototypes/survival-geography-pass-v0.md`, while preserving the hard level/reward gates, branch deferrals, and later skill/checklist/warning passes.

No new gameplay research was performed for this pass. Gameplay claims and route limits are carried from the source-backed objective database, the generated route-planning index, `data/locations/location-geography.csv`, and the Phase 2 constraint tables.

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
| `data/constraints/*.md` | Canonical route laws for AE starts, leveled rewards, cell locks, conflicts, trophies, NPC dependencies, bugs, radiants, Survival Mode, and progression. |

## Data Snapshot

| Route-index slice | Rows | Prototype handling |
| --- | ---: | --- |
| Main-route objective rows | 2,685 | Eligible for this artifact unless fixed, windowed, branch-deferred, or later-pass owned. |
| `dependency_flexible` main rows | 1,542 | Insert only after prerequisites and constraint rows permit. |
| `region_flexible` main rows | 842 | Insert when the route is naturally in the corridor and Survival support exists. |
| `windowed` main rows | 206 | Keep as anchored windows; do not treat as ordinary flexible fill. |
| `fixed_late` main rows | 72 | Keep behind their level, cell-entry, quest-state, reward, or progression gates. |
| `fixed_early` main rows | 5 | Place in setup/opening only. |
| `cleanup_safe` main rows | 18 | Keep for checklist reconciliation, not as early travel targets. |

| Candidate status | Main rows | Prototype handling |
| --- | ---: | --- |
| `single_geography_point` | 443 | Assign to the primary corridor block, subject to hard gates and access validation. |
| `multiple_geography_points` | 4 | Assign to a block only after exact point validation; not final pathing. |
| `single_support_candidate` | 830 | Attach to the matching hub, quest, property, support table, or parent objective when prerequisites are valid. |
| `multiple_support_candidates` | 319 | Keep as a candidate-selection queue; later passes choose the local safe copy/source. |
| `no_route_candidate_data` | 1,089 | Place by anchor, quest dependency, faction sequence, reward timing, or later checklist mapping. |

All 447 direct geography rows in this prototype are `location` objectives. They are corridor-ready, but not final step-ready: the geography table is straight-line support data and still requires road, pass, water, quest-state, enemy, weather, and exact entrance validation before prose.

The direct geography counts below reflect source corridor membership. Gate-extracted rows such as Forbidden Legend-linked locations, Silent Moons Camp, and Sky Haven Temple remain visible in their source corridor counts, but their controlling prototype assignment is recorded separately in `prototype-objective-block-map.csv`.

Rows with blank `route_block` in `prototype-objective-block-map.csv` are intentionally deferred through `disposition`, `prototype_status`, `deferred_to`, and `reason`; blank does not mean unprocessed. G14 checklist rows are temporary checklist-reconciliation holds, and TB-030 must remap individual collectibles, counters, and checklist-only rows into corridor, quest, branch, appendix, or final cleanup placements where appropriate.

## Insertion Rules

| Rule | Effect |
| --- | --- |
| Hard gates override geography. | A nearby objective still waits if it would cross level 8, 25, 27, 32, 36, 40, 46, 60, 78, 80, or 252 gates. |
| Branch-deferred rows stay deferred. | Hircine, Aetherial, Thirsk, Bittercup, Velehk Sain, Ghosts of the Tribunal, Civil War branch handling, and similar unresolved defaults wait for TB-028. |
| Candidate support is not availability. | A candidate base, home, merchant, spell-tome source, property, or book copy is only a possible route node after acquisition, ownership, safe-storage, source, and prerequisite validation. |
| Corridor support is not fast travel. | Carriages, ferries, roads, horses, and hubs describe logistics; Survival Mode still requires food, sleep, carry, warmth, and recovery endpoints. |
| Counts are not permission. | A block count does not mean every row is safe at the block's earliest skeleton pressure; each row still needs prerequisite, hard-gate, branch, bug, NPC, source-selection, and Survival validation. |
| Books/documents use title-level coverage. | Single-copy or quest-tied titles can follow their parent block; multi-copy titles wait for candidate selection unless a quest/location already fixes the source. |
| Unique items are preserved. | Do not disenchant unique items for effects; do not grab leveled, cell-locked, or branch-sensitive unique rewards before their gate. |
| Radiants use source boundaries. | Required or representative radiants insert only where the Phase 2 radiant table allows, and exact target selection stays reviewable. |
| Skill, perk, crafting, and grind work waits for TB-027. | This file reserves slots but does not choose Legendary reset distribution, training budgets, material loops, enchantment sources, alchemy recipes, or underleveled fallbacks. |

## Direct Geography Insertion Map

This table assigns direct `location` rows to their primary route-block container. Counts are queue sizes, not final clear order.

| Block | Direct rows | Corridors consumed | Cold profile | Prototype insertion rule |
| --- | ---: | --- | --- | --- |
| G02 Central carry/storage | 62 | `riverwood_helgen_road` 15; `whiterun_central_plains` 28; `rorikstead_western_road` 19 | 58 standard; 3 regional cold; 1 high elevation/mountain | Use after G00-G01 survival setup and first Whiterun handling. Keep Silent Moons/lunar-weapon handling behind level 8 and avoid carry sprawl before storage/sell-off is established. |
| G03 Southern warm expansion | 59 | `falkreath_pine_forest` 32; `ivarstead_rift_pass` 27 | 48 standard; 7 high elevation/mountain; 4 source-listed cold interior | Use as a warm-core expansion block with horse/inn support. Do not treat Bloated Man's Grotto/Hircine-sensitive state, Bolar's Oathblade, or mountain clears as casual filler before their constraints are checked. |
| G04 Riften/southeast support | 39 | `riften_rift` 39 | 35 standard; 4 high elevation/mountain | Use for Riften-side locations, Thieves Guild support, Shadowfoot/Nchuanthumz-style candidate logistics, and southeastern objectives after prerequisites. Do not start `Trinity Restored` before 32, do not take Nightingale reward handoffs before 46, and keep Dawnguard branch handling out of this block. |
| G05 Western Reach and road inns | 38 | `old_hroldan_reach_road` 19; `markarth_reach` 19 | 38 standard | Use for Markarth/Reach and road-inn sweeps with carry and bed endpoints. Keep Sky Haven Temple/Dragonbane behind level 46 and do not let Cidhna Mine, Daedric, or property/NPC conflicts become unmarked side effects. |
| G06 Eastmarch/Windhelm ferry hub | 46 | `kynesgrove_eastmarch_road` 28; `windhelm_eastmarch` 18 | 38 standard; 7 regional cold; 1 source-listed cold interior | Use for Windhelm/Eastmarch sweeps, ferry preparation, and east-road objectives. Keep Blood on the Ice, Civil War Windhelm state, and ferry/Solstheim transitions as anchored windows, not filler. |
| G07 Solitude/northwest city/coast | 68 | `solitude_haafingar` 18; `dragon_bridge_haafingar_road` 23; `morthal_marsh` 27 | 34 standard; 33 regional cold; 1 source-listed cold interior | Use for Solitude, Haafingar, Morthal, marsh, and coastal sweeps with cold/carry prep. Keep Bards instruments uncollected before assignment, finish Erikur-sensitive Thieves work before hostile Solitude states, and delay Shield of Solitude reward handoff until level 40. |
| G08 Pale/Winterhold prepared sweep | 64 | `dawnstar_pale_coast` 19; `nightgate_pale_pass` 28; `winterhold_coast` 17 | 45 regional cold; 10 standard; 9 source-listed cold interior | Use only as prepared cold/mountain sweeps. Under current Phase 2 constraints, keep Saarthal and the Forbidden Legend-linked locations out of pre-36 route prose; TB-032 should convert the source's broad approach/spawn caution into precise warnings before any exception is attempted. |
| G11 Dawnguard expedition | 15 | `dayspring_canyon` 2; `icewater_volkihar_ferry` 13 | 9 regional cold; 4 standard; 1 source-listed cold interior; 1 high elevation/mountain | Use after Dawnguard route support exists and the `Bloodline` hard-save structure is ready. Treat Volkihar, vampire transformation, Lost Relic cycling, and coastal/castle travel as anchored expedition work. |
| G12 Solstheim/Raven Rock spine | 54 | `raven_rock_west` 20; `thirsk_central` 16; `skaal_north` 14; `tel_mithryn_east` 4 | 49 Solstheim cold region; 5 source-listed cold interior | Use after Raven Rock support is established. Treat Severin as storage only after acquisition/storage validation, keep Thirsk and Ralis outcomes deferred, and do not finish final Miraak before level 60. |
| G13 Separate-worldspace/AE high-risk | 2 | `manual_validation_required` 2 | 2 not comparable | Do not auto-route from corridor data. Use manual validation for Skuldafn, Deadlands, Apocrypha, Soul Cairn, Forgotten Vale, and similar spaces before any final prose. |

## Route-Block Prototype

| Block | Prototype placement | Flexible insertions allowed here | Held out of this block |
| --- | --- | --- | --- |
| G00 Setup | AE install/trophy-safe mode, Survival Mode baseline, run settings, and the fixed-early support rows. | `OBJ-000479` Survival Mode, `OBJ-000702` Survival Mode Food and Warmth Consumable Set, `OBJ-000705` Camping Supplies Crafting System as setup/system coverage only. Actual camping-supply crafting waits for materials, forge/anvil access, carry capacity, and Survival need validation. | Any travel, crafting grind, branch choice, or objective acquisition that depends on in-world validation. |
| G01 Opening warm core | Opening escape, Riverwood/Whiterun approach, first proper bed/food/carry plan, and first Whiterun protected-entry caution. | Only immediate support, tutorial, first-rest, food, and local low-risk objectives that do not lock rewards, trigger branch states, or create large carry debt. | Broad central location clearing; that queue moves to G02 after survival stabilization. |
| G02 Central carry/storage | First broad warm-region insertion block. | The 62 direct central location rows; Riverwood/Whiterun/Rorikstead support objectives; early merchant, home, and food/storage candidates after validation; local book/document and unique-item rows tied to already-routed objectives. | Pre-level-8 Silent Moons lock, overbroad Thieves/Companions depth, northern travel, and unvalidated property/storage assumptions. |
| G03 Southern warm expansion | Falkreath, pine forest, Ivarstead/Rift pass, and warm-core side expansion. | The 59 direct southern location rows; Falkreath and Ivarstead local favors; Lakeview/property prerequisites where constraints permit; nearby Daedric or quest windows only when their levels and NPC dependencies are open. | Hircine/Bloated Man's Grotto state, Bolar's Oathblade, and mountain/cold interiors unless their exact constraints are checked. |
| G04 Riften/southeast support | Riften hub, southeast support, and Thieves infrastructure. | The 39 direct Riften corridor rows; Riften local services, investments, property candidates, and support objectives after prerequisite checks; safe Thieves setup before reward locks. | Starting `Trinity Restored` before 32, source-tier Nightingale Blade/Bow reward handoffs before 46, Dawnguard branch routing, and unresolved Aetherial/default decisions. |
| G05 Western Reach and road inns | Markarth, Reach, Old Hroldan, road-inn loops, and western Daedric/property windows. | The 38 direct western rows; Markarth/Reach side objectives; western book, unique-item, and location rows when constraints are clear; Hendraheim-style candidates only after start/acquisition validation. | Sky Haven Temple before 46, unchecked Cidhna/Madanach outcomes, and branch-sensitive Daedric choices. |
| G06 Eastmarch/Windhelm ferry hub | East road, Windhelm services, ferry gateway, and east-side state management. | The 46 direct Eastmarch rows; Windhelm merchant/service objectives; ferry-prep objectives; east-road books/items and local favors after NPC/bug constraints. | Windhelm Civil War end-state, unmarked Blood on the Ice risk, broad Solstheim cleanup, and ferry travel without cold/rest/carry plan. |
| G07 Solitude/northwest city/coast | Solitude, Haafingar, Morthal, Dragon Bridge, marsh, and coastal prep. | The 68 direct northwest rows; Solitude/Bards/Thieves support only with instrument and Erikur constraints respected; Morthal/Haafingar property and service candidates after validation. | Shield of Solitude reward before 40, Bards instruments before assignment, hostile Solitude overlap, and coast/cold travel without expedition support. |
| G08 Pale/Winterhold prepared sweep | Dawnstar, Nightgate, Winterhold, College access, and cold-north sweeps. | The 64 direct northern rows only as prepared sweeps; Dawnstar/Winterhold service objectives; College access that does not cross the current level-36 linked-dungeon lock; cold-region books/items when the route is already there. | Pre-36 `Lost Legends`, Folgunthur, Saarthal, Geirmund's Hall, Reachwater Rock, broad College depth, and casual cold-interior detours. |
| G09 Level-36 linked-dungeon loop | Dedicated post-36 Forbidden Legend/Saarthal-linked loop. | Move the relevant linked-dungeon objectives from their regional corridors into one controlled loop after level 36, with food, bed, warmth, carry, and exact access validation. | Any pre-36 read, exterior spawn/approach, map-marker discovery, entry, loot, or quest-state lock for the linked dungeons under current constraints; TB-032 must make the exact warning triggers source-specific. |
| G10 Level-46 classic reward loop | Maximum-tier classic reward unlock block. | Riftweald/Chillrend, Sky Haven/Dragonbane, source-tier Nightingale reward handoffs, and other reward-locked objectives once level 46+ is confirmed. | Final Miraak before 60, Legendary Dragon before 78, Ebony Warrior before 80, and branch defaults. |
| G11 Dawnguard expedition | Dawnguard main-route chain, Fort Dawnguard support, Volkihar branch save, coastal/castle loops. | The 15 Dawnguard/coastal direct location rows; finite Dawnguard chains; representative/required Dawnguard radiants only within source boundaries; Fort Dawnguard service/support objectives. | Volkihar branch content in main continuity, vampire perk timing without TB-027, and Aetherial reward default before TB-028. |
| G12 Solstheim/Raven Rock spine | Raven Rock logistics, Solstheim progression, island sweeps, Black Books, Skaal/Tel Mithryn/Thirsk/Kolbjorn windows. | The 54 Solstheim direct rows; Raven Rock/Tel Mithryn/Skaal local objectives; Black Book and Dragonborn objectives as their prerequisite chain permits; island support rows after ferry and storage validation. | Final Miraak before 60, broad island cleanup before support, Thirsk default, Ralis outcome, and Severin storage before validation. |
| G13 Separate-worldspace/AE high-risk expeditions | Manually validated separate-worldspace and high-risk AE blocks. | Apocrypha, Soul Cairn, Forgotten Vale, Skuldafn, Deadlands, and high-risk AE objective bundles only after manual access, return, rest, and reward checks. | Any automatic insertion based on Skyrim/Solstheim corridor proximity. |
| G14 Late cleanup by corridor | Final corridor cleanup, counters, collection reconciliation, and late progression tail. | Remaining safe rows after TB-027, TB-028, TB-030, and TB-032 clarify skills, branch defaults, checklist coverage, and warnings. A row may enter G14 only with an explicit late-level, checklist-finalization, post-branch, post-progression, or unresolved source-selection reason. | Using cleanup as a substitute for missing route placement, underleveled gate recovery without a plan, or unsourced checklist assumptions. |

## Non-Geographic Queue Treatment

| Queue | Rows | TB-026 disposition |
| --- | ---: | --- |
| Single support candidates | 830 | Attach when the support row is already inside a safe route block. This covers many book/document titles, crafting unlock rows, skill/perk support rows, properties, merchant investments, and a few quest/unique/trophy support rows. |
| Multiple support candidates | 319 | Do not choose a canonical copy/source here. TB-027/TB-030/TB-032 should choose the local safest candidate after skill, checklist, and warning needs are known. |
| No route candidate data | 1,089 | Keep dependency-driven. Quest chains, unique-item rewards, collectible sets, AE package parents, powers, radiants, trophy counters, pets/mounts, and relationships should move with their anchor or later checklist/default pass. |
| Constraint-backed flexible rows | 887 | Do not treat flexibility as permission to route blindly. Inspect the linked constraint source before final insertion or warning text. |
| Flexible rows without linked constraints | 1,497 | Eligible for local insertion only if prerequisites, geography, and Survival support are clear. |

## Support Objective Policy

| Objective class | Prototype policy |
| --- | --- |
| Properties and bases | Place acquisition opportunities in their regional block, but do not use a candidate base as rest/storage until acquisition, ownership, safety, and storage behavior are validated. |
| Merchant investments and services | Attach to the relevant city/hub block if the merchant/service remains available and the economy route supports it; exact investment timing waits for TB-027/TB-030. |
| Skill books | Choose one copy per title later. If a skill book is fixed by a quest/location already in a block, mark it as a local pickup candidate; otherwise keep it in the candidate-selection queue. |
| Spell tomes | Vendor/multiple-source tomes wait for TB-027 skill and shopping route choices; fixed-copy tomes can follow their validated location block. |
| Quest and AE documents | Single-source quest documents follow the parent quest or location; multi-source titles wait for source selection. Oghma Infinium acquisition and read/use timing remain separated. |
| Unique items | Acquire with the parent quest/location if no leveled, cell-entry, branch, NPC, or bug constraint blocks it. Preserve unique items unless the specification later creates an explicit exception. |
| Crafting unlocks | Reserve shop/craft/disenchant/alchemy/Smithing/Enchanting/ingredient loops for TB-027. Do not use a unique-item disenchant as the baseline. |
| Radiants | Insert required radiants only inside the relevant faction/window. Representative radiants should use source-approved boundaries and local targets, not random grind assumptions. |
| Collectibles, stones, shouts, and powers | Insert opportunistically when the corridor is already safe, but checklist coverage and exact counter synchronization wait for TB-030. |
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
| Miraak equipment | Final Miraak battle/corpse appearance too early. | Level 60+. |
| Legendary Dragon | Legendary Dragon hunt too early. | Level 78+ and combat-ready block. |
| Ebony Warrior | Ebony Warrior objective too early. | Level 80+ and combat-ready block. |
| All perks | Treating cleanup as final perk completion. | Level 252 plan and post-Legendary skill recovery from TB-027/TB-030. |

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

## Handoff to TB-027

TB-027 should add the progression layer without flattening this prototype into final prose. In particular:

* assign skill, perk, training, Legendary reset, material, enchantment, alchemy, merchant, and crafting work to route blocks where it supports the next gate;
* include bounded fallback blocks for underleveled checkpoints before levels 8, 25, 27, 32, 36, 40, 46, 60, 78, 80, and 252;
* preserve the gradual difficulty curve and do not rush overpowered gear unless the specification later changes;
* do not disenchant unique items for baseline enchantment coverage;
* do not choose unresolved branch defaults or branch routes before TB-028;
* do not claim checklist completeness before TB-030.
