# Level-Gated Skeleton v0

Status: TB-024 complete; downstream branch/default/checklist-source updates refreshed in TB-031K after TB-031J.

This is a Phase 5 planning artifact. It assigns the TB-023 route anchors to broad level bands and mandatory gates. It is not a route prototype, not detailed guide prose, and not a final objective order.

No new gameplay research was performed for this pass. Gameplay facts are carried from `drafts/route-prototypes/route-anchors-v0.md`, `data/objectives/objectives.csv`, the generated route-planning indexes, and the Phase 2 constraint tables.

## Inputs

| Input | Use |
| --- | --- |
| `drafts/route-prototypes/route-anchors-v0.md` | Structural anchors `A00` through `A21`, level/reward gate register, and branch hard-save register. |
| `data/objectives/objectives.csv` | Objective identity, hard level gates, routing rigidity, and citations. |
| `data/route-planning/objective-route-index.csv` | Generated objective workbench for fixed-late, windowed, branch-only, and constraint-backed rows. |
| `data/route-planning/objective-constraints.csv` | Links from objectives to Phase 2 constraint-table rows. |
| `data/constraints/*.md` | Canonical route laws for leveled rewards, cell-entry locks, conflicts, trophies, NPCs, bugs, radiants, Survival Mode, and progression. |

## Boundaries

| Boundary | Rule for later route passes |
| --- | --- |
| Level bands are not exact route sections. | TB-025 may move flexible content within or across bands for Survival Mode geography, but must not violate hard gates. |
| No detailed route steps here. | Later files should convert bands into route blocks only after geography, flexible insertion, branches, and warnings are ready. |
| Branch defaults are external to this skeleton. | Use TB-028 defaults, TB-029 branch prototypes, and TB-031C checklist escalation decisions instead of choosing branch policy here. |
| Source-tier reward policy remains conservative. | Use maximum-tier leveled reward gates unless a later explicit decision accepts a documented tradeoff such as Nightingale Blade utility. |
| Conservative does not mean optimal. | These gates optimize permanent/recoverable completion value over short-term power, convenience, or natural quest flow; later route passes may recommend documented tradeoffs only where the specification permits them. |
| Survival Mode remains first-order. | Each band assumes food, sleep, carry, cold, storage, and transport checks will be added in TB-025. |
| Power curve remains gradual. | Do not use all-perks leveling or final crafting power to justify rushing high-risk late content. |

## Level-Band Skeleton

| Skeleton band | Level range / gate | Anchor coverage | Route role | Must delay or preserve | Later owner |
| --- | --- | --- | --- | --- | --- |
| S00 | Pre-start and setup | A00 | Establish trophy-safe install scope and run rules. | Official AE bundle only; no non-AE Creations/mods; Survival Mode is the main-route baseline. | Final setup prose |
| S01 | Level 1-4 | A01, A02, A03 | Opening, Riverwood/Whiterun warm-core stabilization, first bed/food/carry/storage planning, and first Whiterun protected-entry handling. | Do not start broad cold-region, mountain, Solstheim, or heavy collection sweeps. Do not treat level-1 Daedric access as a reason to route Daedric content before stabilization. | TB-025, TB-027 |
| S02 | Level 5-7 | A02, A03, A04, A19 | Early stability plus first level/courier awareness. Apprentice trophy and level-5 AE starts become possible. | Do not force Plague of the Dead or other courier content immediately; do not approach/loot Silent Moons Camp before level 8 if preserving the Lunar weapon pool. | TB-025, TB-026 |
| S03 | Level 8-9 | A03, A04, A09, A10, A19 | First low-level reward gates and risk warnings become active. Silent Moons can be placed if geography/power supports it; Largashbur and Falkreath-level-9 caveats become visible. | Avoid casual Largashbur approach unless ready to protect Orc NPCs. Preserve Falkreath land/favor handling before later Dark Brotherhood Helvard fallout. | TB-025, TB-032 |
| S04 | Level 10-14 | A04, A05, A09, A10, A19 | Early-mid expansion: first faction introductions, first properties/AE systems where safe, and early Daedric eligibility. | Clavicus, Meridia, Peryite, Hendraheim, Bloodchill, and `A Night To Remember` are eligible by gate but still require power, geography, and branch/warning validation. | TB-025, TB-026, TB-032 |
| S05 | Level 15-19 | A05, A06, A07, A08, A10 | Controlled early faction depth and Septimus / `Discerning the Transmundane` staging window. | If `Discerning the Transmundane` reaches the cube/opened-outpost state, do not leave the Oghma path for long-term delay. Acquire the Oghma Infinium only when the path is being resolved; TB-027 keeps read/use timing late, TB-031E assigns the source/timing policy, and TB-033 validates final skill math. Keep Bards instruments uncollected before assignment. | TB-025, TB-026, TB-027, TB-032 |
| S06 | Level 20-24 | A06, A07, A08, A09, A10 | Midgame faction/property/artifact staging. `Pieces of the Past`, `The Whispering Door`, and Dawnstar land access become available by gate. | Do not kill Helvard before Lakeview/Falkreath prerequisites are secured. Preserve Whiterun and Dawnstar NPC start paths before risky violence or faction-state changes. | TB-025, TB-028, TB-032 |
| S07 | Level 25-31 | A05, A07, A09, A10, A11 | First major reward threshold band. Mage's Circlet and The Pale Blade can be safely timed; Boethiah becomes eligible at 30. | Do not start `Trinity Restored` before 32. Do not read `Lost Legends` or approach Folgunthur, Saarthal, Geirmund's Hall, or Reachwater Rock before 36. Choose Boethiah sacrifice only after the follower/default pass. | TB-027, TB-028, TB-032 |
| S08 | Level 32-35 | A06, A07, A09, A10, A11, A19 | Nightingale armor-safe threshold and Alternative Armors - Ebony Plate courier gate. Midgame faction development can deepen if it does not cross later reward locks. | Level 32 is only the Nightingale armor minimum; if maximum source-tier Nightingale Blade/Bow policy is kept, late Thieves Guild reward handoffs still wait for 46+. | TB-025, TB-026, TB-032 |
| S09 | Level 36-39 | A05, A07, A10, A11, A16 | Forbidden Legend linked-dungeon gate opens; `Deathbrand` becomes eligible. | Current source-backed constraints include Saarthal in the level-36 linked-dungeon lock; do not route pre-36 College/Saarthal depth unless a later pass explicitly reopens that constraint. Do not take Falk's final Shield of Solitude reward before 40. Do not enter Sky Haven Temple or Riftweald Manor before 46. | TB-025, TB-026 |
| S10 | Level 40-45 | A07, A08, A09, A12, A13, A19 | Shield of Solitude-safe phase and preparation for Civil War/main-quest coordination, late Thieves rewards, Dawnguard, Dragonborn, and high-level AE. | Preserve War Hero/Season Unending hard-save handling. Keep Sky Haven Temple, Riftweald Manor, Chillrend, Dragonbane, and source-tier Nightingale reward gates closed until 46+. | TB-025, TB-026, TB-032 |
| S11 | Level 46-59 | A07, A12, A13, A14, A15, A16, A17, A19 | Maximum-tier classic reward phase: Sky Haven/Dragonbane, Riftweald/Chillrend, late Thieves rewards, Civil War/main-quest coordination, Dawnguard branch gate, prepared Solstheim opening, and high-level AE such as The Cause. | Do not finish final Miraak battle before 60. Keep Dawnguard/Volkihar, Civil War, Dark Brotherhood, Paarthurnax, Aetherium, and AE branch saves as anchors, not branch prose. | TB-025, TB-028, TB-029, TB-032 |
| S12 | Level 60-77 | A16, A17, A18, A19, A20 | Dragonborn finalization and maximum Miraak equipment become safe by level. Late Solstheim, Black Book, Dragon Aspect, Dragonrider, Karstaag, high-risk AE, and mythic content can consolidate here if power/geography supports them. | Legendary Dragon remains locked until 78. Ebony Warrior remains locked until 80. Do not start final all-perks cleanup until the combat build and infrastructure can survive skill resets. | TB-025, TB-027, TB-032 |
| S13 | Level 78-79 | A20 | Legend trophy checkpoint. | Use a late combat-ready Legendary Dragon block; do not treat this as all late progression completion. Ebony Warrior still waits for 80. | TB-027, TB-032 |
| S14 | Level 80-251 | A20, A21 | Ebony Warrior, late counters, remaining high-risk objectives, and controlled progression toward all perks. | TB-027 provides the Legendary reset baseline and fallback structure; TB-031E has selected progression sources and reset distribution. Exact numeric reset counts, final perk allocation, and observed completion validation remain TB-033. | TB-027, TB-031E, TB-033 |
| S15 | Level 252+ / final completion state | A20, A21 | All-perks and final reconciliation band. | Final state must restore all skills to 100 after Legendary resets, allocate all 251 skill perk ranks, preserve unique-item policy, and map every objective/checklist row to a route, branch, option list, appendix, or exclusion. | TB-033, TB-036, TB-037 |

## Mandatory Gate Checklist

These are hard or conservative skeleton checks that later route files must preserve.

| Gate | Do not cross before | Primary reason | Source support |
| --- | --- | --- | --- |
| Setup gate | New game / loaded save | Trophy-safe official AE scope and Survival baseline. | `docs/guide-specification.md`; `trophy-dependencies.md` (`SN-000101`); `survival-mode-constraints.md` (`SN-000115`) |
| First Whiterun entry | Leaving first Whiterun visit | Preserve Amren/Ysolda first-visit handling. | `cell-entry-locks.md` (`SN-000096`) |
| Level 8 | Silent Moons Camp first loot/clear | Preserve best Lunar weapon candidate pool. | `leveled-unique-items.md` (`SN-000093`); `cell-entry-locks.md` (`SN-000094`) |
| Level 25 | `Good Intentions` reward report | Preserve Mage's Circlet timing. | `leveled-unique-items.md` (`SN-000092`) |
| Level 27 | The Pale Blade claim/resolution | Preserve leveled reward target; Frostmere still has separate Kharjo target risk. | `leveled-unique-items.md` (`SN-000092`); `cell-entry-locks.md` (`SN-000096`) |
| Level 32 | `Trinity Restored` start | Preserve maximum Nightingale armor set. | `leveled-unique-items.md` (`SN-000092`) |
| Level 36 | Read `Lost Legends` or approach Folgunthur, Saarthal, Geirmund's Hall, or Reachwater Rock | Preserve Gauldur Blackblade/Blackbow linked-dungeon level state. | `leveled-unique-items.md` (`SN-000092`); `cell-entry-locks.md` (`SN-000094`) |
| Level 40 | Falk reward at end of `The Wolf Queen Awakened` | Preserve Shield of Solitude tier. | `leveled-unique-items.md` (`SN-000092`) |
| Level 46 | Riftweald Manor first entry | Preserve maximum Chillrend. | `leveled-unique-items.md` (`SN-000092`); `cell-entry-locks.md` (`SN-000094`) |
| Level 46 | Sky Haven Temple first entry during `Alduin's Wall` | Preserve maximum Dragonbane. | `leveled-unique-items.md` (`SN-000092`); `cell-entry-locks.md` (`SN-000094`) |
| Level 46 | Accept the Nightingale Blade reward from `Hard Answers` or complete the Nightingale Bow reward handoff after `Blindsighted` | Preserve maximum source-listed tiers unless later review accepts a practical-tier tradeoff. | `leveled-unique-items.md` (`SN-000092`) |
| Level 60 | Final Miraak battle / corpse appearance | Preserve maximum Miraak Sword, Staff, and mask. | `leveled-unique-items.md` (`SN-000092`); `cell-entry-locks.md` (`SN-000092`) |
| Level 78 | Legendary Dragon hunt | Satisfy Legend trophy gate. | `trophy-dependencies.md` (`SN-000105`, `SN-000103`) |
| Level 80 | Ebony Warrior | Satisfy encounter gate. | `skill-perk-leveling-plan.md` (`SN-000032`, `SN-000119`) |
| Level 252 | All-perks finalization | Acquire enough perk points for all 251 skill perk ranks. | `skill-perk-leveling-plan.md` (`SN-000119`) |

## Branch Gate Placement

Branch anchors started as placeholders for TB-028/TB-029. After TB-031K, this table reflects resolved defaults while still assigning only broad hard-save pressure, not final route steps.

| Branch gate | Earliest eligible band | Preferred placement pressure | Must preserve before choosing | Deferred work |
| --- | --- | --- | --- | --- |
| Civil War faction oath | S10 | S10-S11, when Season Unending and War Hero pressure can be managed. | Imperial main route, pre-faction hard save, War Hero-safe Civil War/Main Quest state. | TB-028 builds Stormcloak branch scope; TB-032 places Season Unending/War Hero warnings. |
| Dawnguard `Bloodline` | S11 | S11, after level-46 reward gates and with Dawnguard/Volkihar branch save ready. | Dawnguard main route, Volkihar branch save, transformation/trophy planning. | TB-028/TB-029 build Volkihar branch depth, including branch radiants and rewards. |
| Dark Brotherhood Abandoned Shack | S06 | S06-S11, after dependency checks rather than on first eligibility. | `Delayed Burial`, Erikur / `The Dainty Sload`, Helvard/property, Vittoria-linked objectives, and join/destroy hard save. | Destroy branch later; exact placement waits for dependency and warning layers. |
| Paarthurnax | S11 | S11 or later main-quest band. | Paarthurnax-preserve main route and Blades/Greybeards branch save. | TB-028/TB-029 build Blades/Paarthurnax alternate if retained. |
| Aetherium Forge | S11 | S11 or later Dawnguard-compatible band. | Aetherial Crown main default, Staff/Shield reward branches, and forge hard save. | TB-029 reward branch prototype exists; TB-032 places the forge-save warning. |
| Hircine / Bloated Man's Grotto | S04 | S04-S10 only after Bolar/grotto state and artifact policy are settled. | Ring of Hircine single-artifact main default, Savior's Hide reward branch, Bolar's Oathblade / grotto-state policy, and branch save. | TB-032 places grotto/cell-state warning. |
| Thirsk Mead Hall | S11 | S11-S12 Solstheim band. | Nord-side main default, Thirsk side-choice save, and Riekling branch-exclusive NPC/favor state. | TB-029 Riekling branch prototype exists; TB-032 places the choice warning. |
| Bittercup altar | S04 | S04-S11 only after the route can support the branch attempts. | Fortune main default, Power and Nothing branch attempts, and altar hard save. | TB-029 compact branch prototypes exist; TB-032 places the branch-save/reload warning. |
| Ghosts of the Tribunal | S12 | S12 Solstheim band unless a later route prototype proves an earlier Solstheim block is practical. | Join/infiltrate main default, destroy-heretics branch save, and BR-007 coverage for `Reclamation Priest's Journal (AE)`. | TB-029 branch prototype and TB-031J source-readiness mapping exist; TB-032 places the Temple-state warning. |
| Velehk Sain, Frost, Ralis, Civil War Champions | Parent-route dependent | Place with their parent route blocks. | Use TB-028/TB-031C defaults: release Velehk, keep Frost, spare Ralis, and align Battle of the Champions with Imperial handling unless TB-033 proves a checklist gap. | TB-034 places parent-route steps; TB-033/TB-037 validate coverage. |

## Progression and Power-Curve Handoff

| Layer | Skeleton decision | Deferred detail |
| --- | --- | --- |
| Early progression | S01-S04 should build practical survival, carry, bed, food, and basic combat competence before route expansion. | Exact attributes, combat style, food, first storage, mount, and crafting materials. |
| Midgame progression | S05-S10 should deepen factions and properties without using final overpowered crafting as a crutch. | Exact training targets, faction order, and regional objective packing. |
| Late progression | S11-S14 should support Dawnguard, Dragonborn, high-level AE, Legendary Dragon, and Ebony Warrior. | Exact combat readiness checks, transformation perk grinds, and late route fallback blocks. |
| All-perks progression | S14-S15 reserve level 252 and Legendary reset recovery for the endgame. | TB-027 sets the reset baseline and TB-031E sets source/reset policy; exact reset counts, skill recovery loops, final perk order, and final checklist validation remain TB-033/TB-037. |
| Crafting and economy | Early trophy crafts can occur before final crafting power; final crafting/investment/enchantment/alchemy should wait for their own layer. | TB-027 sets the block-level policy and TB-031E selects source families/circuits/material defaults; final physical availability and route-step validation remain TB-033/TB-034. |

## Handoff to TB-025

TB-025 has reshaped this skeleton around Survival Mode geography without violating the gates above. Later route edits should continue to:

* use `data/locations/location-geography.csv` and not hold-level equivalence;
* turn S01-S04 into practical warm-core and early transport/storage route blocks;
* group northern, mountain, coastal, and Solstheim objectives into prepared sweeps;
* attach beds, inns, food/restock, carry relief, carriages, ferries, horses, homes, and camps to each broad route block;
* preserve all S09-S12 reward gates when grouping objectives by corridor;
* leave final warning prose, detailed route placement, and final validation to their assigned tasks; branch defaults, flexible objective insertion, skill-reset distribution, and prototype-level checklist mapping are now resolved by TB-026 through TB-031J.
