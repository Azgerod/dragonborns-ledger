# Source Note: Objective Database Completeness Review

Status: needs review.

Source note ID: SN-000088

## Claim

The Phase 1 objective database is structurally complete enough to run a final pre-Phase-2 cleanup. Source-list coverage now exists for the major specification areas, all objective rows have source-note citations and completion boundaries, support tables cross-reference existing objective IDs, and source notes reference bibliography IDs that exist. The review found two pre-Phase-2 follow-up tasks: reconcile no-journal activity/favor rows, and build a Phase 2 research input index.

## Routing Relevance

The project must not begin route construction or hard-constraint research with hidden Phase 1 omissions. This note supports closing TB-010 as a review task while keeping Phase 2 blocked until TB-010A and TB-010B are complete.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000300 | Skyrim:Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Quests | 2026-05-12 | High-level quest taxonomy used as a final Phase 1 category sanity check. |
| SRC-000297 | Skyrim:Activities | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Crafting | 2026-05-12 | Activities, crafting systems, work tasks, and activity-adjacent achievement check. |
| SRC-000020 | Skyrim:Miscellaneous Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Miscellaneous_Quests | 2026-05-11 | Existing miscellaneous quest and no-journal activity/favor boundary source. |
| SRC-000263 | Skyrim:Dungeons | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dungeons | 2026-05-12 | Existing clearable-location and dungeon clearing sanity check. |
| SRC-000268 | Skyrim:Skills | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Skills | 2026-05-12 | Existing skill/perk scope sanity check. |

## Evidence Summary

The local audit checked `objectives.csv`, support CSVs under `data/`, source notes, and bibliography references.

Structural results:

| Check | Result |
| --- | ---: |
| Objective rows | 2,755 |
| Gameplay rows without source-note citations | 0 |
| Objective rows with blank completion boundaries | 0 |
| Missing source-note references from data CSVs | 0 |
| Missing objective references from support CSVs | 0 |
| Source notes | 87 before this note |
| Source-note numbering gaps | 0 |
| Missing bibliography IDs referenced from source notes | 0 |

Coverage-review inputs included prior closeout artifacts for TB-007 broad collectible/reward work, TB-008 location work, and TB-009 skill/crafting work. Those artifacts report no remaining known source-list category gaps in their slices.

The only Phase 1 boundary issue found is no-journal activity/favor treatment. SN-000026 intentionally deferred activity-only favors instead of adding generic repeatable objective rows. SN-000087 then noted that Chop Wood, Gather Wheat, and Mine Ore are not practical crafting-system gaps. Before Phase 2 radiant research, TB-010A should explicitly decide whether these and similar no-journal activity/favor rows need representative/audit objective rows, or whether they remain relationship/checklist support only.

The second issue is process-oriented: Phase 2 constraint tasks should not each rediscover their candidate rows from scratch. TB-010B should create a research input index mapping objective/support rows to TB-011 through TB-020.

## Confidence and Open Questions

Confidence is high for structural completeness and source-note linkage. Confidence is intentionally lower for route readiness because Phase 2 has not yet researched hard constraints.

Open questions before Phase 2:

* Which no-journal activity/favor rows need explicit objective/audit rows before TB-018?
* Which objective IDs and support tables should seed each Phase 2 constraint table?

Open questions after Phase 2 starts:

* AE Creation start triggers and level gates;
* leveled reward thresholds and lock timing;
* cell-entry-sensitive locations/items;
* quest conflicts, missables, and hard saves;
* PS4 trophy behavior;
* NPC dependencies;
* bug-prone quests;
* radiant boundaries;
* Survival Mode constraints;
* skill/perk/leveling and crafting progression.

## Linked Records

`data/objectives/objective-database-completeness-review.md`; `docs/task-board.md`; `data/objectives/objectives.csv`; `data/objectives/aggregate-reconciliation.md`; `data/skills/skill-crafting-completeness-review.md`; `data/locations/location-completeness-review.md`.
