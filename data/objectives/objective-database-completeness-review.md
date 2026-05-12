# Objective Database Completeness Review

Status: TB-010 complete; TB-010A complete; TB-010B complete.

This review audits the Phase 1 objective database before the project moves into Phase 2 constraint-table research.

It does not start route construction, resolve constraint-table facts, choose branch defaults, choose checklist mappings, or normalize routing rigidity. Those remain later phases by design.

## Review Inputs

| Input | Role |
| --- | --- |
| `docs/guide-specification.md` | Canonical requirement source. |
| `docs/requirements-index.md` | Atomic requirement checklist for scope coverage. |
| `docs/development-plan.md` | Confirms Phase 1 is objective database work and Phase 2 is constraint-table research. |
| `data/objectives/objectives.csv` | Primary objective database. |
| `data/objectives/aggregate-reconciliation.md` | Parent/set/placeholder reconciliation. |
| `data/objectives/tb-007-reconciliation.md` | Broad collectible/reward relationship coverage review. |
| `data/locations/location-completeness-review.md` | Location coverage closeout. |
| `data/skills/skill-crafting-completeness-review.md` | Skill/crafting coverage closeout. |
| `data/books/`, `data/items/`, `data/locations/`, `data/npc/`, `data/properties/`, `data/skills/` | Support-table cross-references. |
| `sources/source-notes/` and `sources/bibliography.md` | Source-note and bibliography coverage. |

## Database Snapshot

This snapshot reflects the TB-010 audit state before TB-010A appended activity/favor reconciliation rows.

| Check | Result |
| --- | ---: |
| Objective rows | 2,755 |
| Categories represented | 15 |
| Source notes before this review note | 87 |
| Bibliography IDs after this review source | 300 |
| Data CSV support tables checked | 25 |
| Gameplay rows without source-note citations | 0 |
| Objective rows with blank completion boundary | 0 |
| Missing source-note references from data CSVs | 0 |
| Missing objective references from data CSVs | 0 |
| Missing bibliography IDs referenced from source notes | 0 |
| Source-note numbering gaps | 0 |

## Objective Category Counts

| Category | Rows | Phase 1 review result |
| --- | ---: | --- |
| `ae_creation` | 79 | Source-list and package-child coverage represented. |
| `book_document` | 735 | Title/member coverage represented; duplicate copies remain acquisition candidates. |
| `collectible` | 146 | Major finite set/member coverage represented. |
| `crafting_unlock` | 301 | Skills/crafting support-table coverage represented. |
| `location` | 467 | Clearable, discoverable, duplicate-marker, secondary-marker, and AE place coverage represented. |
| `misc_objective` | 168 | Source-listed objective-bearing misc/favor rows represented; no-journal activities need the follow-up task below. |
| `npc_relationship` | 31 | Unlock rows and option-set rows represented; candidate table coverage exists. |
| `pet_mount` | 27 | Pet, mount, horse, and equipment coverage represented. |
| `property` | 21 | Home, homestead, farm, furnishing, and property-system coverage represented. |
| `quest` | 336 | Main, faction, side, DLC, and AE quest coverage represented at source-list level. |
| `radiant` | 58 | Known source-listed faction, bounty, property-defense, word-wall, and branch radiant placeholders represented; boundary research remains Phase 2. |
| `skill_perk` | 40 | All-skill, all-perk, skill-100, perk-tree, perk-point, and Legendary reset rows represented. |
| `spell_power` | 62 | Shouts, powers, abilities, transformations, and choice sets represented. |
| `trophy` | 18 | Trophy tracker coverage represented as validation overlays. |
| `unique_item` | 266 | Base/DLC unique item rows, leveled reward parent rows, artifact rows, and AE parent sets represented. |

## Scope Coverage Matrix

| Specification area | Phase 1 coverage | Result | Later destination |
| --- | --- | --- | --- |
| Setup and allowed content | Governance docs, AE manifest, package rows | Covered for Phase 1 | TB-011 and final setup prose validate current AE start/install behavior. |
| Main quest | Main and optional main-quest rows | Covered | TB-014/TB-015 handle Season Unending, Paarthurnax, and trophy interactions. |
| Civil War | Imperial main route and Stormcloak branch rows | Covered | TB-014/TB-015/TB-028 handle branch and War Hero risks. |
| Major factions | Companions, College, Thieves Guild, Dark Brotherhood rows plus radiants/contracts | Covered | TB-018 handles radiant boundaries; TB-014/TB-017 handle conflicts/bugs. |
| Bards College | Quest and instrument rows | Covered | TB-017/TB-031B handle bugs/checklist. |
| Daedric quests | Quest rows, trophy tracker, artifact handling | Covered | TB-014/TB-015/TB-017/TB-028 handle choices, bugs, and branches. |
| Official DLC | Dawnguard, Hearthfire, Dragonborn quest/property/system rows | Covered | TB-014 through TB-020 handle constraints. |
| Official AE Creation bundle | Package manifest, quest rows, property/pet/mount/item/member support data | Covered | TB-011 validates triggers/gates; TB-014/TB-017 handle choices/bugs. |
| Named side quests | Base/DLC side quest source-list rows | Covered | TB-014/TB-017/TB-031B handle conflicts, bugs, and checklist. |
| Miscellaneous objectives and favors | Objective-bearing misc/favor rows covered | Follow-up needed | TB-010A must reconcile no-journal activity/favor rows before Phase 2. |
| Bounded radiants | Source-listed radiant placeholders and representative rows | Covered enough for Phase 1 | TB-018 must classify boundaries. |
| Shouts and word walls | Shout rows and word-wall-related rows | Covered | TB-015/TB-018/TB-019/TB-031F handle trophy/radiant/geography/checklist. |
| Locations | Clearable/discoverable/AE place support table | Covered | TB-013/TB-015/TB-017/TB-019 provide lock, trophy, bug, and Survival inputs; TB-031G validates clear/access mechanics before route prose. |
| Collectibles | Major finite set/member rows | Covered | TB-031B/TB-031F reconcile checklist and route-counter treatment; route passes synchronize locations. |
| Unique items and leveled rewards | Base/DLC unique rows, AE member support data, leveled parent rows | Covered for Phase 1 | TB-012/TB-013/TB-014/TB-017 provide threshold, lock, conflict, and bug inputs; TB-031B/TB-031E/TB-032/TB-033 consume them for checklist, source, warning, and validation work. |
| Properties and homes | Objective rows plus property detail support table | Covered | TB-016/TB-019/TB-020 provide NPC, storage, material, and Survival inputs; TB-031D/TB-031E choose route defaults and material/storage use. |
| Pets, mounts, followers, and role options | Unlock rows plus relationship option support table | Covered | TB-031D handles defaults, route value, and role recommendations using TB-016 NPC-safety inputs. |
| Spells, powers, abilities, transformations | Spell tome, shout, power, ability, transformation rows | Covered | TB-031D/TB-031E handle default choices and checklist. |
| Skills, perks, alchemy, enchantments, merchant investments, crafting systems | Skill/crafting support tables and closeout review | Covered | TB-015/TB-016/TB-020 provide trophy, NPC, and planning inputs; TB-031E chooses concrete sources and route execution. |

## Structural Audit Results

| Audit | Result | Notes |
| --- | --- | --- |
| Objective header and controlled values | Pass | `tools/validate_objectives.py` passes. |
| Source-note references from objectives | Pass | No objective row references a missing source note. |
| Support table objective references | Pass | No support CSV references a missing objective ID. |
| Support table source-note references | Pass | No support CSV references a missing source note. |
| Source-note source IDs | Pass | Every `SRC-######` referenced by source notes exists in `sources/bibliography.md`. |
| Source-note sequence | Pass | `SN-000001` through `SN-000087` were continuous before this review note. |
| Completion boundaries | Pass | No objective row has a blank completion boundary. |
| Gameplay citation coverage | Pass | No gameplay objective row lacks citations. |

## Expected Non-Blockers

These signals are intentionally not Phase 1 blockers:

| Signal | Count | Reason not a blocker |
| --- | ---: | --- |
| `route_placement=unclassified` | 809 | Many AE, branch, radiant, duplicate, and detail rows need Phase 2 constraints before final placement. |
| `routing_rigidity=unclassified` | 964 | Routing rigidity is explicitly Phase 3 work after hard constraints exist. |
| `cell_entry_lock_risk=unknown` | 2,512 | Cell-entry and lock timing are Phase 2 constraint-table research. |
| `bug_risk=unknown` | 2,413 | Bug validation is Phase 2 constraint-table research. |
| Notes containing `deferred` | 1,733 | These generally point to named downstream tasks, not hidden omissions. |
| Notes containing `placeholder` | 33 | These are radiant placeholder rows explicitly delegated to TB-018. |

## Pre-Phase-2 Findings

The review found two follow-up tasks that should run before Phase 2 begins:

| Finding | Why it matters | New task |
| --- | --- | --- |
| No-journal activity/favor rows need one final boundary decision before radiant research. | Earlier passes correctly avoided inflating the database with every activity-only favor. However, the Activities page explicitly lists Chop Wood, Gather Wheat, and Mine Ore as radiant tasks, and existing relationship-option rows contain activity/favor prerequisites. TB-018 will be cleaner if Phase 1 first adds explicit representative/audit rows or records a clear exclusion/support-only policy. | TB-010A |
| Phase 2 needs an input index. | The objective database is now large enough that each constraint pass should start from an explicit list of candidate objective IDs/support tables rather than ad hoc searching. This is especially important for leveled rewards, cell-entry locks, conflicts, trophies, NPC dependencies, radiants, Survival Mode, and skill/crafting planning. | TB-010B |

## Phase 2 Gate

Phase 2 may begin with TB-011 after TB-010B.

Phase 1 can now be considered closed for source-list objective database work. Remaining unknowns are constraint research, route classification, checklist mapping, recommendations, or final QA work rather than hidden Phase 1 omissions.

## Source Support

Primary support is in `sources/source-notes/SN-000088-objective-database-completeness-review.md`.
