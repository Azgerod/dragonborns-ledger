# Phase 2 Constraint Tables

Status: TB-021 reviewed; TB-021B geography support added; TB-031G location route-validation, TB-031J checklist source-readiness, TB-031K downstream refresh, and TB-032 warning layers complete.

This directory contains the source-backed routing laws for the guide. The tables are not route prose; they define what later route passes must obey when classifying objectives, building anchors, grouping geography, adding skill/crafting progression, placing warnings, and validating the prototype.

TB-021 reviewed the Phase 2 outputs from TB-011 through TB-020 for source-note support, internal consistency, stale placeholders, and route-phase handoffs. The review found no missing source-note links, missing bibliography links, or missing objective references in the constraint tables. TB-021A added UESP Gamemap-backed coordinate data for the location catalog, TB-021B converted that layer into a hub/corridor geography support table for objective rigidity classification and later route placement, TB-031G added a route-validation layer for location clear/discovery mechanics, TB-031J resolved the remaining checklist-only source-readiness rows before warning/final route work, and TB-032 added the route warning/hard-save trigger overlay.

## Mechanical Audit

| Check | Result | Notes |
| --- | --- | --- |
| Phase 2 constraint files present | Pass | TB-011 through TB-020 each have a constraint table output. |
| Constraint source-note references resolve | Pass | Every explicit `SN-*` reference in `data/constraints/*.md` maps to an existing source note. |
| Source-note bibliography references resolve | Pass | Every `SRC-*` reference found in source notes maps to `sources/bibliography.md`. |
| Constraint objective references resolve | Pass | Every explicit `OBJ-*` reference found in constraint tables maps to `data/objectives/objectives.csv`. |
| Source-note sequence | Pass | Source notes currently run continuously from `SN-000001` through `SN-000129`. |
| Route drafting boundary | Pass | Constraint files still avoid writing a final guide or detailed route sequence. |
| Coordinate support layer | Pass | `data/locations/location-coordinates.csv` provides coordinate rows for every location catalog row, with multi-marker, proxy, no-marker, and separate-worldspace cases flagged. |
| Hub/corridor geography layer | Pass | `data/locations/location-geography.csv` provides derived nearest services, corridor assignments, worldspace access models, cold risk, barrier flags, and confidence fields. Hold-equivalence routing is still prohibited. |
| Checklist source-readiness layer | Pass | TB-031J added `source-readiness-resolutions.csv` and `SN-000129`; no generated checklist row remains in `source_readiness_required`. |
| Warning/hard-save trigger layer | Pass | TB-032 added source-backed warning and save triggers to the main prototype and hard-save register without adding new gameplay research. |

## Constraint Inventory

| Task | File | Review result | Downstream handoff |
| --- | --- | --- | --- |
| TB-011 AE Creation starts | `ae-creation-start-triggers.md` | Package-level start triggers and hard/prerequisite gates are represented for all 74 AE bundle parents. Source support is present. | Child-level conflicts, bugs, item specifics, and route timing remain owned by later route/warning/validation passes; TB-031J closed the checklist source-readiness queue. |
| TB-012 leveled unique items | `leveled-unique-items.md` | Leveled reward thresholds and acquisition/lock events are represented and sourced. | TB-022/TB-024 must classify level-gated rewards as fixed-late or windowed; Nightingale Blade source-tier versus tempering utility remains a deliberate route choice. |
| TB-013 cell-entry locks | `cell-entry-locks.md` | Confirmed entry/spawn locks are separated from reward-time locks and no-confirmed-entry cases. | TB-032 has placed concise warning triggers; TB-033 validates coverage. |
| TB-014 conflicts and hard saves | `quest-conflicts-hard-saves.md` | Full branches, artifact choices, option-list decisions, and sequencing warnings are separated cleanly. | TB-028/TB-029 decided branch defaults and prototypes; TB-032 placed concise warnings. |
| TB-015 trophy dependencies | `trophy-dependencies.md` | PS4 setup rules, trophy counters, missable trophies, branch interactions, and level trophies are represented. | Route QA must verify counters and place hard saves before one-shot trophy actions. |
| TB-016 NPC dependencies | `npc-dependencies.md` | Quest, trophy, property, role, service, investment, training, favor, and activity NPC surfaces are represented. | TB-031D/TB-031E selected route defaults and progression/investment policy; exact route steps and validation remain TB-034/TB-033. |
| TB-017 bug-prone quests | `bug-prone-quests.md` | PS4/no-console mitigations, hard saves, platform-test rows, and excluded bug buckets are represented. | TB-032 placed concise warning triggers; TB-033 validates that they cover route-created risks. |
| TB-018 radiant boundaries | `radiant-boundaries.md` | Required gates, finite chains, representative radiants, branch-only radiants, support-only locators, and excluded failure states are bounded. | TB-031C/TB-031F resolved 125-job, representative-radiant, conversion-depth, and Hired Muscle counter mechanics; final step placement and validation remain downstream. |
| TB-019 Survival Mode | `survival-mode-constraints.md` | Hunger, fatigue, cold, sleep, travel services, storage, food, carry, and regional risk constraints are represented. | TB-022/TB-025 must use location hub/corridor data; hold membership alone is not adequate geography. |
| TB-020 skill/perk/crafting | `skill-perk-leveling-plan.md`; `progression-source-selection.md`; `progression-source-selections.csv` | All-skills/all-perks, level 252, Legendary resets, training limits, crafting power curve, investments, enchantments, alchemy, exploit boundaries, and TB-031E source-selection defaults are represented. | Final numeric reset counts, exact final physical random/vendor source items, step placement, and final perk order remain TB-033/TB-034 validation and route-prototype work. |

## Review Decisions

| Topic | TB-021 disposition | Reason |
| --- | --- | --- |
| Geography routing | Coordinate prerequisite implemented in TB-021A; hub/corridor table implemented in TB-021B. | Coordinates enable nearest-service and corridor calculations. The geography support layer adds transport, cold, barrier, access-model, and confidence filters, but road, mountain, water, access-state, and portal costs still need route-specific validation. |
| Companions Hired Muscle | Do not require new-game restart forcing. Route it if the seed offers it early; otherwise continue and mark the representative type as unavailable in that seed. | The representative radiant value is not worth forcing an otherwise clean run restart. Required Companions gates still route normally. |
| Thieves Guild 125 side jobs | Keep as a source-backed completionist counter candidate pending checklist mapping. | The display/safe boundary is finite and source-backed, but whether it becomes required guide content depends on checklist expectations and review tolerance for a large radiant grind. |
| Volkihar `New Allegiances` | Keep branch-depth decision for TB-028. | One conversion gives representative branch coverage; all three named conversions may matter only if checklist mapping treats each as meaningful. |
| Warmaiden's duplicate investment rows | Keep as route-validation issue, not a Phase 2 blocker. | The support table preserves source-listed rows for Adrianne and the shared store; official PS4 AE behavior should be tested or annotated before checklist closure. |
| Unknown AE investment audit rows | Keep audit-only until validated. | The catalog marks four AE investment rows as unknown; they must not be routed as hard requirements without official PS4 AE validation. |
| Exploit-adjacent leveling/crafting | Keep excluded or deferred baseline from TB-020. | This matches the specification's power-curve rule and the decisions log's unresolved exploit-default status. |

## Phase 3 Handoff

TB-022 should classify objectives using the constraint tables as follows:

| Classification pressure | Source tables to consult |
| --- | --- |
| Fixed early | AE start triggers, NPC dependencies, bug-prone quests, Survival infrastructure, trophy setup rules. |
| Fixed late | Leveled unique items, cell-entry locks, late trophy gates, high-level AE gates, all-perks cleanup. |
| Windowed | Quest/faction conflicts, Companions radiant windows, Daedric/Aetherial choices, transformation-state windows. |
| Region-flexible | Location objectives, local favors, clearable dungeons, collectables, skill books, and safe nearby AE starts after geography support exists. |
| Dependency-flexible | Properties, investments, training, crafting systems, skill/perk milestones, and Dragonborn/Solstheim infrastructure. |
| Branch-only | Stormcloak, Volkihar, Destroy the Dark Brotherhood, Blades/Paarthurnax alternate, Daedric alternate outcomes, and branch-exclusive AE/faction content. |
| Option-list | Spouse, children, stewards, house decoration, isolated moral choices, and non-propagating preferences. |
| Cleanup-safe | Final checks for locations, collectibles, remaining investments, remaining skill/perk/crafting objectives, and counters that do not affect earlier route safety. |
| Excluded/unbounded | Infinite radiants, failure-state repair quests, arbitrary repeats, non-trophy-safe content, unsupported exploits, and random/reactive events that require route-warping behavior. |

## Open Items

These are not Phase 2 source-support blockers, but they must remain visible:

| Item | Owner |
| --- | --- |
| Use `data/locations/location-geography.csv` for geography-sensitive classification and later regional insertion; do not fall back to hold-equivalence routing. | TB-022/TB-025. |
| Decide first safe storage, main base, property service timing, and travel infrastructure defaults. | Complete in TB-031D; warning triggers are recorded in TB-032; route steps remain TB-034. |
| Select representative no-journal activity/favor targets for geography, thaneship, economy, and relationship overlap. | Complete in TB-031D; exact route steps remain TB-034. |
| Choose enchantment source families, alchemy discovery source methods, representative crafting outputs, training blocks, and reset distribution without sacrificing preserved uniques or gradual power curve. | Complete in TB-031E; final physical source-item and numeric reset validation remain TB-033. |
| Validate route counters for Sideways, Hero of the People, Delver, Explorer, Reader, Thief, Snake Tongue, and trophy pop fallbacks. | Counter policy complete in TB-031F; Delver/Explorer clear/discovery mechanics complete in TB-031G; final totals/trophy pops remain TB-033/final QA. |
| Decide branch depth for Stormcloak, Volkihar, Daedric alternatives, Blades/Paarthurnax, and AE branch outcomes. | Complete in TB-028/TB-029; TB-032 placed hard-save warnings and TB-033 validates branch state. |
| Place warnings for leveled rewards, cell-entry locks, NPC risks, trophy actions, and bug-prone quest steps. | Complete in TB-032; TB-033 validates coverage. |

## Current Result

Phase 2 constraint facts are source-supported and internally consistent. TB-021A added coordinate support, TB-021B added hub/corridor geography support, TB-031G added location route-validation mechanics, TB-031J closed the checklist source-readiness queue for later route placement, and TB-032 added the warning/hard-save trigger layer. Later passes should not reopen Phase 2 facts casually; they should only add narrower source notes when a specific route placement needs detail that the Phase 2 table intentionally deferred.
