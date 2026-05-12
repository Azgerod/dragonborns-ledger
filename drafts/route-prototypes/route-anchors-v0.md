# Route Anchors v0

Status: TB-023 complete; downstream defaults and checklist-source readiness refreshed in TB-031K after TB-031J.

This is an anchor-only Phase 4 planning artifact. It is not route prose, not a final route order, and not a detailed itinerary. It identifies the structural points the next route passes must preserve before flexible objectives are inserted.

No new gameplay research was performed for this pass. Gameplay claims below are carried from the source-backed objective database, route-planning index, and Phase 2 constraint tables.

## Inputs and Data Snapshot

| Input | Use in this pass |
| --- | --- |
| `docs/guide-specification.md` | Scope guard: PS4 AE, Legendary, Survival Mode on, trophies preserved, official AE bundle only, all perks, and hard-save branch policy. |
| `data/objectives/objectives.csv` | Objective identity, route placement, routing rigidity, source-note references, and broad route fields. |
| `data/objectives/route-rigidity-classification-notes.md` | TB-022 classification rules and explicit deferrals. |
| `data/route-planning/objective-route-index.csv` | One-row-per-objective workbench for fixed, windowed, branch, geography, and constraint summaries. |
| `data/route-planning/objective-constraints.csv` | Objective-to-constraint links used to locate the canonical constraint rows. |
| `data/constraints/*.md` | Canonical route laws for AE starts, leveled rewards, cell-entry locks, conflicts, trophies, NPC dependencies, bugs, radiants, Survival Mode, and progression. |

| Snapshot | Value |
| --- | ---: |
| Objective rows | 2,789 |
| `fixed_early` objectives | 6 |
| `fixed_late` objectives | 73 |
| `windowed` objectives | 211 |
| `branch_only` objectives | 39 |
| Objective-to-constraint links | 1,847 |
| Generated hard-gate links | 1,166 |
| Generated branch/hard-save links | 287 |
| Generated warning links | 121 |

## Boundary Rules

| Rule | Consequence for TB-024 and later |
| --- | --- |
| Anchors are pressure points, not final steps. | Do not convert this file directly into black-box guide prose. |
| Phase 2 constraint tables override broad category defaults. | Inspect the canonical constraint row before writing any later route instruction or warning. |
| Flexible objectives are not placed here. | `region_flexible` and `dependency_flexible` rows wait for the level skeleton, Survival geography pass, and flexible insertion pass. |
| Branch defaults are resolved outside this anchor artifact. | Use TB-028 defaults, TB-029 branch prototypes, and TB-031C checklist escalation decisions rather than choosing branch policy here. |
| Geography stays hub/corridor based. | TB-025 must use `data/locations/location-geography.csv`; hold membership alone is not a route basis. |
| Survival Mode is first-order. | No ordinary fast travel assumptions; anchors need bed, food, cold, carry, transport, and storage planning. |

## Structural Anchor Register

| Anchor | Working placement | Anchor purpose | Must preserve or delay | Source support | Later owner |
| --- | --- | --- | --- | --- | --- |
| A00 | Pre-start setup | Trophy-safe install and run-mode baseline. | Official AE bundle only, no non-AE Creations/mods, Survival Mode required for main route. | `docs/guide-specification.md`; `data/constraints/trophy-dependencies.md` (`SN-000101`); `data/constraints/ae-creation-start-triggers.md` (`SN-000090`) | TB-024, final setup prose |
| A01 | Opening escape and Riverwood start | Establish the run after `Unbound` and early Survival Mode. | `OBJ-000001`, `OBJ-000002`, `OBJ-000479`, basic food/warmth/camping support, and no Survival disable/re-enable baseline. | `data/constraints/trophy-dependencies.md` (`SN-000102`); `data/constraints/survival-mode-constraints.md` (`SN-000115`, `SN-000116`, `SN-000117`) | TB-024 |
| A02 | Early warm-core stabilization | Build minimum Legendary/Survival viability before risky travel. | Bed access, cooked food, carry relief, first storage candidate, basic crafting actions, and an early transport/mount plan. Do not start northern, mountain, or Solstheim sweeps here. | `data/constraints/survival-mode-constraints.md` (`SN-000115`, `SN-000117`, `SN-000118`); `data/constraints/skill-perk-leveling-plan.md` (`SN-000103`, `SN-000121`) | TB-024, TB-025, TB-027 |
| A03 | First Whiterun protected entry | Treat first Whiterun visit as a constrained local sweep, not a casual stop. | Handle or deliberately preserve Amren and Ysolda first-visit/favor exposure before leaving the city; stage early trophy-safe craft/work checks if route-feasible. | `data/constraints/cell-entry-locks.md` (`SN-000096`); `data/constraints/trophy-dependencies.md` (`SN-000103`); `data/constraints/radiant-boundaries.md` (`SN-000113`) | TB-024, TB-025 |
| A04 | Dragons enabled gate | Decide when `Dragon Rising` enters the world state. | Dragon souls, dragon bounties, dragon attacks, dragon soul trophy progress, and later shout planning depend on this gate. | `data/objectives/objectives.csv` (`OBJ-000004`, `OBJ-000760`, `OBJ-002779`); `data/constraints/trophy-dependencies.md` (`SN-000103`) | TB-024 |
| A05 | Early faction access without locked-depth mistakes | Open useful factions while avoiding level-locked dungeon/reward traps. | Companions and Thieves Guild can start early, but College depth must respect Saarthal/Forgotten Legend level-36 constraints; later Thieves/Nightingale rewards are separately gated. | `data/constraints/trophy-dependencies.md` (`SN-000102`); `data/constraints/leveled-unique-items.md` (`SN-000092`); `data/constraints/cell-entry-locks.md` (`SN-000094`) | TB-024 |
| A06 | Companions and transformation window | Preserve required Companions gates and werewolf timing. | Complete required Companions radiant gates, respect the post-`The Silver Hand` window, finish Totems/Purity handling, and do not permanently lose Beast Form before Werewolf Mastered planning is satisfied. | `data/constraints/radiant-boundaries.md` (`SN-000112`); `data/constraints/trophy-dependencies.md` (`SN-000102`, `SN-000105`); `data/constraints/skill-perk-leveling-plan.md` (`SN-000105`) | TB-024, TB-027 |
| A07 | Thieves Guild restoration and Erikur safety | Keep Guild restoration, Solitude special job, and Nightingale rewards coherent. | Complete `The Dainty Sload` before `Bound Until Death` makes Erikur vulnerable; route 20 restoration jobs; keep the 125-job safe/display counter as required completionist coverage for TB-031F mechanics; delay Nightingale armor/reward handoffs to their selected thresholds. | `data/constraints/bug-prone-quests.md` (`SN-000109`, `SN-000102`, `SN-000107`); `data/constraints/radiant-boundaries.md` (`SN-000112`); `data/constraints/leveled-unique-items.md` (`SN-000092`) | TB-024, TB-031F |
| A08 | Clean Bards College/Solitude window | Avoid Bards bug and Solitude state conflicts. | Do not pick up Bards instruments or King Olaf's Verse before assignment; keep saves around Bards join, instrument dungeons, and final festival; do not overlap final festival with hostile Solitude/Elisif states. | `data/constraints/bug-prone-quests.md` (`SN-000018`, `SN-000109`); `data/constraints/quest-conflicts-hard-saves.md` (`SN-000100`) | TB-024, TB-032 |
| A09 | Hearthfire, property, and household infrastructure | Secure property prerequisites and Survival logistics before irreversible NPC/faction risks. | Lakeview/Falkreath prerequisites before `Kill Helvard`; Dawnstar/Heljarchen waits for level 22; adoption only after valid housing; Hearthfire services and carriages are logistics infrastructure, not flavor. | `data/constraints/trophy-dependencies.md` (`SN-000105`, `SN-000030`); `data/constraints/npc-dependencies.md` (`SN-000100`, `SN-000107`); `data/constraints/survival-mode-constraints.md` (`SN-000116`, `SN-000117`) | TB-024, TB-025, TB-031D |
| A10 | Daedric artifact matrix | Preserve Oblivion Walker-safe outcomes and branchable alternatives. | Artifact-awarding outcomes and Hircine branch treatment now follow TB-028/TB-029; Boethiah sacrifice still needs a nonessential follower and a hard save. | `data/constraints/quest-conflicts-hard-saves.md` (`SN-000098`, `SN-000099`); `data/constraints/trophy-dependencies.md` (`SN-000104`); `data/constraints/npc-dependencies.md` (`SN-000107`) | TB-024, TB-028, TB-032 |
| A11 | Forbidden Legend and College depth gate | Hold Saarthal and linked Forbidden Legend sites until their reward/entry constraints are safe. | Do not read `Lost Legends` or approach Folgunthur, Saarthal, Geirmund's Hall, or Reachwater Rock before level 36 if preserving maximum Gauldur rewards; do not report for Mage's Circlet before level 25. | `data/constraints/leveled-unique-items.md` (`SN-000092`); `data/constraints/cell-entry-locks.md` (`SN-000094`) | TB-024 |
| A12 | Main quest midgame and Sky Haven gate | Coordinate main quest progression with Dragonbane and Civil War state. | Gate first Sky Haven Temple entry/Alduin's Wall at level 46 if preserving maximum Dragonbane; preserve Season Unending and War Hero hard-save handling. | `data/constraints/leveled-unique-items.md` (`SN-000092`); `data/constraints/cell-entry-locks.md` (`SN-000094`); `data/constraints/quest-conflicts-hard-saves.md` (`SN-000010`, `SN-000097`) | TB-024 |
| A13 | Civil War and Season Unending coordination | Preserve the Imperial main route and Stormcloak branch while protecting War Hero. | Keep pre-faction hard save; canonical route joins Imperial; do not let Season Unending skip the War Hero fort requirement without a validated trophy-safe path. | `data/constraints/quest-conflicts-hard-saves.md` (`SN-000097`); `data/constraints/trophy-dependencies.md` (`SN-000102`) | TB-024, TB-028, TB-032 |
| A14 | Dawnguard faction and Aetherium branch | Place Dawnguard/Volkihar branch gate and Dawnguard finite chains. | Hard save at `Bloodline`; canonical route refuses Harkon's gift; Volkihar branch holds branch-only radiants/rewards; complete Dawnguard finite chains; use TB-028/TB-029 Aetherium Forge default and reward branches. | `data/constraints/quest-conflicts-hard-saves.md` (`SN-000097`, `SN-000099`); `data/constraints/radiant-boundaries.md` (`SN-000114`); `data/constraints/trophy-dependencies.md` (`SN-000105`) | TB-024, TB-028, TB-029 |
| A15 | Dawnguard transformation and Auriel's Bow checks | Preserve Dawnguard trophies and transformation perk trees. | Werewolf Mastered and Vampire Mastered require deliberate access windows; shoot the sun with Auriel's Bow before risky storage/sale/post-finale delay. | `data/constraints/trophy-dependencies.md` (`SN-000105`); `data/constraints/skill-perk-leveling-plan.md` (`SN-000105`) | TB-027, TB-032 |
| A16 | Solstheim opening and Raven Rock logistics | Open Solstheim only when Survival logistics can support it. | Use Raven Rock as initial support; do not treat Solstheim as ordinary Skyrim geography; verify Severin Manor before storage; avoid broad island cleanup before cold/travel support exists. | `data/constraints/trophy-dependencies.md` (`SN-000105`); `data/constraints/survival-mode-constraints.md` (`SN-000117`, `SN-000118`); `data/constraints/bug-prone-quests.md` (`SN-000111`) | TB-024, TB-025 |
| A17 | Skaal, Thirsk, and Kolbjorn windows | Preserve Dragonborn missables, branch choices, and phase checks. | Let Deor/Fanari start `A New Source of Stalhrim` after `The Fate of the Skaal`; use the TB-028/TB-031C Nord-side Thirsk default with the Riekling side on a branch save; treat `Unearthed` as phase-gated and preserve the spare-Ralis main outcome save. | `data/constraints/bug-prone-quests.md` (`SN-000111`); `data/constraints/npc-dependencies.md` (`SN-000107`); `data/constraints/quest-conflicts-hard-saves.md` (`SN-000034`, `SN-000099`) | TB-024, TB-028, TB-032 |
| A18 | Dragonborn final and level-60 rewards | Delay Miraak finalization until maximum reward and soul/perk planning are ready. | Do not finish final Miraak battle before level 60 if preserving maximum Miraak equipment; coordinate Miraak soul-steal period, Bend Will, Black Books, Dragon Aspect, and Dragonrider. | `data/constraints/leveled-unique-items.md` (`SN-000092`); `data/constraints/trophy-dependencies.md` (`SN-000105`, `SN-000033`) | TB-024, TB-027 |
| A19 | High-level AE and late reward queue | Place AE courier gates and high-level Creation quests around power curve and reward thresholds. | Plague/Bone Wolf/Hendraheim/Bloodchill/Ebony Plate/The Cause and other AE starts must respect their hard/prerequisite gates; exact child placement waits for level, geography, bug, and checklist passes. | `data/constraints/ae-creation-start-triggers.md` (`SN-000090`, `SN-000091`); `data/constraints/bug-prone-quests.md` (`SN-000091`) | TB-024, TB-025, TB-026 |
| A20 | Late progression, Legendary Dragon, Ebony Warrior, all perks | Reserve final power and progression work for a late route block. | Level 78 for Legendary Dragon, level 80 for Ebony Warrior, level 252 for all perks, all skills restored to 100 after Legendary resets, and no exploit baseline unless user changes policy. | `data/constraints/trophy-dependencies.md` (`SN-000103`, `SN-000105`); `data/constraints/skill-perk-leveling-plan.md` (`SN-000119`, `SN-000120`, `SN-000121`) | TB-024, TB-027 |
| A21 | Final cleanup and checklist reconciliation | End with explicit counters and no implied backtracking. | Locations, clearables, shouts, books, enchantments, alchemy effects, investments, property/family/service checks, and trophy counters must map to route steps, branches, appendices, option lists, or exclusions. | `docs/guide-specification.md`; `data/constraints/README.md`; `data/constraints/trophy-dependencies.md` (`SN-000103`) | TB-026, TB-031A-TB-031J, TB-033, TB-034/TB-037 |

## Level and Reward Gate Register

These gates are anchor inputs for TB-024. They are not a complete level skeleton.

| Gate | Anchor pressure | Objectives or systems | Source support | TB-024 handling |
| --- | --- | --- | --- | --- |
| Level 5 | AE courier and trophy check. | Plague of the Dead; Apprentice trophy. | `ae-creation-start-triggers.md` (`SN-000091`); `trophy-dependencies.md` (`SN-000103`) | Mark as early gate, but do not force the courier quest before survival stability. |
| Level 8 | First Silent Moons Camp loot/clear if preserving Lunar weapon pool. | Lunar iron/steel weapons; Silent Moons enchantment source. | `leveled-unique-items.md` (`SN-000093`); `cell-entry-locks.md` (`SN-000094`) | Keep camp out of pre-level-8 travel. |
| Level 9 | Orc stronghold first-approach risk and Falkreath letter interaction. | `The Cursed Tribe`; Siddgeir/Falkreath land/favor handling. | `objectives.csv` (`SN-000015`, `SN-000016`); `npc-dependencies.md` (`SN-000100`, `SN-000107`) | Route as a warning gate, not a mandatory level-9 action. |
| Level 10 | Early Daedric/AE gates. | `A Daedra's Best Friend`; Hendraheim courier; Adept trophy. | `objectives.csv` (`SN-000015`, `SN-000016`); `trophy-dependencies.md` (`SN-000103`, `SN-000104`); `ae-creation-start-triggers.md` (`SN-000091`) | Add to early-mid band; branch Clavicus reward save later. |
| Level 12 | Early Daedric/AE gates. | `The Break of Dawn`; `The Only Cure`; Bloodchill Manor courier. | `objectives.csv` (`SN-000015`, `SN-000016`); `ae-creation-start-triggers.md` (`SN-000091`) | Do not treat courier arrival as immediate route placement. |
| Level 14 | Daedric access. | `A Night To Remember`. | `objectives.csv` (`SN-000015`, `SN-000016`) | Place with artifact phase if power/geography supports it. |
| Level 15 | Daedric and Oghma/cube warning. | `Discerning the Transmundane`. | `objectives.csv` (`SN-000015`, `SN-000016`); `quest-conflicts-hard-saves.md` (`SN-000100`); `bug-prone-quests.md` (`SN-000100`, `SN-000107`) | Do not open the cube and delay the Infinium path indefinitely. |
| Level 20 | Daedric access. | `Pieces of the Past`; `The Whispering Door`. | `objectives.csv` (`SN-000015`, `SN-000016`); `npc-dependencies.md` (`SN-000107`) | Preserve NPC/start paths before risky Whiterun or Dawnstar states. |
| Level 22 | Hearthfire land gate. | Dawnstar land/Heljarchen Hall. | `objectives.csv` (`SN-000029`, `SN-000030`, `SN-000075`); `trophy-dependencies.md` (`SN-000105`) | Place with property infrastructure, not arbitrary Pale cleanup. |
| Level 25 | Leveled College reward and trophy check. | Mage's Circlet; Expert trophy. | `leveled-unique-items.md` (`SN-000092`); `trophy-dependencies.md` (`SN-000103`) | Ensure `Good Intentions` reward report is not earlier than this if maximum tier is desired. |
| Level 27 | Leveled reward claim. | The Pale Blade. | `leveled-unique-items.md` (`SN-000092`); `cell-entry-locks.md` (`SN-000094`, `SN-000096`) | Delay claim/resolution; Frostmere Crypt still has Kharjo target risk. |
| Level 30 | Daedric access. | `Boethiah's Calling`. | `objectives.csv` (`SN-000015`, `SN-000016`); `npc-dependencies.md` (`SN-000106`, `SN-000107`) | Choose sacrifice only after follower dependency/default pass. |
| Level 32 | Quest-start reward lock and AE courier. | Nightingale Armor set; Ebony Plate courier. | `leveled-unique-items.md` (`SN-000092`); `ae-creation-start-triggers.md` (`SN-000091`) | Do not start `Trinity Restored` before this if preserving maximum armor. |
| Level 36 | Leveled reward/location-spawn gate and Dragonborn side quest. | Gauldur Blackblade/Blackbow linked dungeons; `Deathbrand`. | `objectives.csv` (`SN-000032`); `leveled-unique-items.md` (`SN-000092`); `cell-entry-locks.md` (`SN-000094`) | Make this a major midgame threshold before Saarthal/Folgunthur/Geirmund/Reachwater. |
| Level 40 | Leveled reward handoff. | Shield of Solitude from `The Wolf Queen Awakened`; Bone Wolf prerequisite follows that quest. | `leveled-unique-items.md` (`SN-000092`); `ae-creation-start-triggers.md` (`SN-000091`) | Delay final Falk reward before this; handle Bone Wolf after prerequisite. |
| Level 46 | High-value leveled reward and AE gate. | Chillrend/Riftweald Manor; Dragonbane/Sky Haven Temple; Nightingale Blade/Bow threshold; The Cause courier. | `leveled-unique-items.md` (`SN-000092`); `cell-entry-locks.md` (`SN-000094`); `ae-creation-start-triggers.md` (`SN-000091`) | Treat as a major route anchor before Sky Haven, The Pursuit, and late Thieves rewards. |
| Level 50 | Trophy check. | Master trophy. | `trophy-dependencies.md` (`SN-000103`) | Check trophy, but do not make it a completion endpoint. |
| Level 60 | Dragonborn final reward gate. | Miraak's Sword, Staff, and mask. | `leveled-unique-items.md` (`SN-000092`); `cell-entry-locks.md` (`SN-000092`) | Do not finish final Miraak battle before this if preserving maximum equipment. |
| Level 78 | Dawnguard trophy gate. | Legendary Dragon / Legend trophy. | `trophy-dependencies.md` (`SN-000105`, `SN-000103`) | Keep as late combat checkpoint with hard save. |
| Level 80 | Dragonborn late quest gate. | The Ebony Warrior. | `skill-perk-leveling-plan.md` (`SN-000032`, `SN-000119`) | Place after late combat build exists. |
| Level 252 | All-perks completion target. | All 251 skill perk ranks. | `skill-perk-leveling-plan.md` (`SN-000119`) | Final progression/grind anchor; all skills must finish at 100. |

## Branch and Hard-Save Anchor Register

This table records branch anchors already named by the constraint tables and refreshed with TB-028/TB-031C defaults. It still does not contain branch-route steps.

| Hard save | Anchor area | Main continuity | Branch or deferred handling | Source support |
| --- | --- | --- | --- | --- |
| `HS-CW-BEFORE-FACTION-OATH` | A13 | Imperial Civil War. | Stormcloak branch later. | `quest-conflicts-hard-saves.md` (`SN-000097`) |
| `HS-DG-BLOODLINE` | A14 | Dawnguard; refuse Harkon's gift. | Volkihar branch later. | `quest-conflicts-hard-saves.md` (`SN-000097`) |
| `HS-DB-ABANDONED-SHACK` | A07/A10 | Join Dark Brotherhood. | Destroy the Dark Brotherhood branch later. | `quest-conflicts-hard-saves.md` (`SN-000097`, `SN-000100`) |
| `HS-MQ-PAARTHURNAX` | A12/A13 | Preserve Paarthurnax. | Blades/Paarthurnax branch later. | `quest-conflicts-hard-saves.md` (`SN-000097`) |
| `HS-DRAGONBORN-THIRSK-CHOICE` | A17 | Nord-side `Retaking Thirsk` main continuity. | Riekling-side branch prototype in BR-006. | `quest-conflicts-hard-saves.md` (`SN-000034`, `SN-000099`) |
| `HS-AE-GHOSTS-TEMPLE` | A19 | Join/infiltrate heretic path. | Destroy-heretics branch prototype in BR-007; TB-031J maps `Reclamation Priest's Journal (AE)` there. | `quest-conflicts-hard-saves.md` (`SN-000099`); `SN-000129` |
| `HS-AE-BITTERCUP-ALTAR` | A19 | Fortune path. | Power and Nothing compact branch prototypes in BR-008A/BR-008B. | `quest-conflicts-hard-saves.md` (`SN-000099`) |
| `HS-DAEDRIC-BLACK-STAR` | A10 | The Black Star. | Azura's Star reward branch. | `quest-conflicts-hard-saves.md` (`SN-000098`) |
| `HS-DAEDRIC-CLAVICUS` | A10 | Masque of Clavicus Vile. | Rueful Axe branch only. | `quest-conflicts-hard-saves.md` (`SN-000098`) |
| `HS-DAEDRIC-HIRCINE-GROTTO` | A10 | Ring of Hircine single-artifact outcome. | Savior's Hide reward branch; dual-artifact path appendix/audit only. Bloated Man's Grotto/Bolar state still needs warning placement. | `quest-conflicts-hard-saves.md` (`SN-000095`, `SN-000098`); `cell-entry-locks.md` (`SN-000095`) |
| `HS-DAEDRIC-MEHRUNES-SHRINE` | A10 | Reforge Mehrunes' Razor. | Spare Silus branch only. | `quest-conflicts-hard-saves.md` (`SN-000098`) |
| `HS-DAEDRIC-NAMIRA-FEAST` | A10 | Ring of Namira outcome. | Non-artifact moral outcomes branch only. | `quest-conflicts-hard-saves.md` (`SN-000098`) |
| `HS-DAEDRIC-VAERMINA-SKULL` | A10 | Skull of Corruption artifact outcome. | Erandur follower outcome branch only unless TB-028 changes policy. | `quest-conflicts-hard-saves.md` (`SN-000098`) |
| `HS-DG-AETHERIUM-FORGE` | A14 | Aetherial Crown. | Aetherial Staff and Aetherial Shield reward branches. | `quest-conflicts-hard-saves.md` (`SN-000099`); `trophy-dependencies.md` (`SN-000105`) |
| `HS-RIFT-FROST-LETRUSH` | A21 | Keep Frost. | Optional outcome note only unless final checklist validation proves an uncovered alternate state. | `quest-conflicts-hard-saves.md` (`SN-000099`) |
| `HS-DRAGONBORN-UNEARTHED-RALIS` | A17 | Spare Ralis. | Optional kill-outcome note only unless final checklist validation requires it. | `quest-conflicts-hard-saves.md` (`SN-000099`); `npc-dependencies.md` (`SN-000107`) |
| `HS-COLLEGE-VELEHK-SAIN` | A11 | Release Velehk for hidden treasure. | Optional kill-outcome note only. | `quest-conflicts-hard-saves.md` (`SN-000099`) |
| `HS-AE-CIVIL-WAR-CHAMPIONS` | A13/A19 | Imperial-aligned handling. | Piggyback on Civil War branch only if TB-034/TB-037 verify side-exclusive state not otherwise covered. | `quest-conflicts-hard-saves.md` (`SN-000099`) |

## Anchor Queues for Later Passes

| Queue | What this file decided | What remains open |
| --- | --- | --- |
| Fixed early | A00-A03 must establish trophy-safe setup, Survival baseline, basic infrastructure, and first Whiterun caution. | Exact food, storage, mount, craft, and activity targets. |
| Fixed late | Level and reward locks become A11, A12, A18, A20, and the level-gate register. | Exact leveling route and whether any source-tier/practical-tier tradeoff is accepted, especially Nightingale Blade. |
| Windowed | Faction, Daedric, property, Dragonborn, and Bards windows become structural anchors. | Exact route sequence inside each window and concise warning text. |
| Branch-only | Named hard-save anchors are recorded with TB-028/TB-031C defaults. | TB-032 warning placement and TB-033 branch-state validation are complete; TB-034/TB-037 still verify final step coverage. |
| Region flexible | Not placed. | TB-025/TB-026 use corridor/geography data to insert nearby objectives. |
| Dependency flexible | Not placed except where needed as infrastructure. | TB-026/TB-027 choose exact placement after level/geography skeletons exist. |
| Option lists | TB-028/TB-031D choose defaults for spouse, children, stewards, role assignments, and isolated moral choices. | TB-035 presents non-default options without rerouting the main continuity. |
| Cleanup safe | Only A21 exists as an end anchor. | Checklist mapping and final counter validation decide exact cleanup contents. |

## Handoff to TB-024

TB-024 has turned this into `drafts/route-prototypes/level-gated-skeleton-v0.md` by assigning anchors to level bands. Later route edits should continue to:

* keep A00-A03 before broad objective routing;
* keep A11 before Saarthal/Forgotten Legend-linked dungeon placement;
* keep A12's Sky Haven/Alduin's Wall gate at level 46+ if maximum Dragonbane is preserved;
* keep A13's Civil War/Season Unending/War Hero relationship explicit;
* keep A14-A15 as Dawnguard anchors without writing branch prose;
* keep A16-A18 as Solstheim/Dragonborn anchors that respect Survival support and level-60 Miraak rewards;
* keep A20 late enough for level 78, level 80, and level 252 progression;
* continue deferring final step order and warning prose to their assigned tasks; branch defaults, skill/reset source policy, and prototype-level checklist mapping are now resolved by TB-028 through TB-031J.
