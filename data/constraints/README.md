# Phase 2 Constraint Tables

Status: TB-021 reviewed; TB-021B geography support added.

This directory contains the source-backed routing laws for the guide. The tables are not route prose; they define what later route passes must obey when classifying objectives, building anchors, grouping geography, adding skill/crafting progression, and placing warnings.

TB-021 reviewed the Phase 2 outputs from TB-011 through TB-020 for source-note support, internal consistency, stale placeholders, and route-phase handoffs. The review found no missing source-note links, missing bibliography links, or missing objective references in the constraint tables. TB-021A added UESP Gamemap-backed coordinate data for the location catalog, and TB-021B converted that layer into a hub/corridor geography support table for objective rigidity classification and later route placement.

## Mechanical Audit

| Check | Result | Notes |
| --- | --- | --- |
| Phase 2 constraint files present | Pass | TB-011 through TB-020 each have a constraint table output. |
| Constraint source-note references resolve | Pass | Every explicit `SN-*` reference in `data/constraints/*.md` maps to an existing source note. |
| Source-note bibliography references resolve | Pass | Every `SRC-*` reference found in source notes maps to `sources/bibliography.md`. |
| Constraint objective references resolve | Pass | Every explicit `OBJ-*` reference found in constraint tables maps to `data/objectives/objectives.csv`. |
| Source-note sequence | Pass | Source notes currently run continuously from `SN-000001` through `SN-000124`. |
| Route drafting boundary | Pass | Constraint files still avoid writing a final guide or detailed route sequence. |
| Coordinate support layer | Pass | `data/locations/location-coordinates.csv` provides coordinate rows for every location catalog row, with multi-marker, proxy, no-marker, and separate-worldspace cases flagged. |
| Hub/corridor geography layer | Pass | `data/locations/location-geography.csv` provides derived nearest services, corridor assignments, worldspace access models, cold risk, barrier flags, and confidence fields. Hold-equivalence routing is still prohibited. |

## Constraint Inventory

| Task | File | Review result | Downstream handoff |
| --- | --- | --- | --- |
| TB-011 AE Creation starts | `ae-creation-start-triggers.md` | Package-level start triggers and hard/prerequisite gates are represented for all 74 AE bundle parents. Source support is present. | Child-level conflicts, bugs, item specifics, and route timing remain owned by later constraint and route passes. |
| TB-012 leveled unique items | `leveled-unique-items.md` | Leveled reward thresholds and acquisition/lock events are represented and sourced. | TB-022/TB-024 must classify level-gated rewards as fixed-late or windowed; Nightingale Blade source-tier versus tempering utility remains a deliberate route choice. |
| TB-013 cell-entry locks | `cell-entry-locks.md` | Confirmed entry/spawn locks are separated from reward-time locks and no-confirmed-entry cases. | Warning placement belongs to TB-032 after route anchors exist. |
| TB-014 conflicts and hard saves | `quest-conflicts-hard-saves.md` | Full branches, artifact choices, option-list decisions, and sequencing warnings are separated cleanly. | TB-028 decides branch prototypes; TB-032 places concise warnings. |
| TB-015 trophy dependencies | `trophy-dependencies.md` | PS4 setup rules, trophy counters, missable trophies, branch interactions, and level trophies are represented. | Route QA must verify counters and place hard saves before one-shot trophy actions. |
| TB-016 NPC dependencies | `npc-dependencies.md` | Quest, trophy, property, role, service, investment, training, favor, and activity NPC surfaces are represented. | Exact trainer, investment, spouse, steward, child, and activity-target choices remain route/default decisions. |
| TB-017 bug-prone quests | `bug-prone-quests.md` | PS4/no-console mitigations, hard saves, platform-test rows, and excluded bug buckets are represented. | Warning layer must stay concise and placed exactly where the route creates the risk. |
| TB-018 radiant boundaries | `radiant-boundaries.md` | Required gates, finite chains, representative radiants, branch-only radiants, support-only locators, and excluded failure states are bounded. | Thieves Guild 125-job treatment and Volkihar conversion depth remain checklist/branch decisions; Hired Muscle does not require restart forcing. |
| TB-019 Survival Mode | `survival-mode-constraints.md` | Hunger, fatigue, cold, sleep, travel services, storage, food, carry, and regional risk constraints are represented. | TB-022/TB-025 must use location hub/corridor data; hold membership alone is not adequate geography. |
| TB-020 skill/perk/crafting | `skill-perk-leveling-plan.md` | All-skills/all-perks, level 252, Legendary resets, training limits, crafting power curve, investments, enchantments, alchemy, and exploit boundaries are represented. | Exact reset distribution, recipes, source items, material quantities, and final perk order remain TB-031E work before validation. |

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
| Decide first safe storage, main base, property service timing, and travel infrastructure defaults. | TB-031D. |
| Select representative no-journal activity/favor targets for geography, thaneship, economy, and relationship overlap. | TB-031D. |
| Choose exact enchantment source items and alchemy discovery recipes without sacrificing preserved uniques. | TB-031E. |
| Choose exact Legendary reset distribution, training blocks, and all-perks grind strategy. | TB-031E. |
| Validate route counters for Sideways, Hero of the People, Delver, Explorer, Reader, Thief, Snake Tongue, and trophy pop fallbacks. | TB-031F/TB-033 and final QA. |
| Decide branch depth for Stormcloak, Volkihar, Daedric alternatives, Blades/Paarthurnax, and AE branch outcomes. | TB-028/TB-029. |
| Place warnings for leveled rewards, cell-entry locks, NPC risks, trophy actions, and bug-prone quest steps. | TB-032. |

## Current Result

Phase 2 constraint facts are source-supported and internally consistent. TB-021A added coordinate support, TB-021B added hub/corridor geography support, and the next unblocked task is TB-022 objective rigidity classification. Later passes should not reopen Phase 2 facts casually; they should only add narrower source notes when a specific route placement needs detail that the Phase 2 table intentionally deferred.
