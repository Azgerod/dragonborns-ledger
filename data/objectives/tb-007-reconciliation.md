# TB-007 Reconciliation

Status: TB-007F complete; TB-007G complete.

This file reconciles the broad TB-007 source-list passes before the project moves into remaining aggregate member expansion, location coverage, skill/perk/crafting coverage, and constraint-table research.

This is not route prose and does not introduce new gameplay claims. It summarizes rows and source-note coverage that already exist in the objective database and related tables.

## Current Source-List Coverage

| Slice | Objective rows | Row count | Related source notes | Current treatment |
| --- | --- | ---: | --- | --- |
| TB-007A powers, shouts, abilities, and transformations | `OBJ-000760` through `OBJ-000818` | 59 | `SN-000046` through `SN-000050` | Covered at source-list level. Route timing, default power choices, word-wall synchronization, and warnings remain downstream work. |
| TB-007B books and documents | `OBJ-000819` through `OBJ-001554` | 736 | `SN-000051` through `SN-000057` | Covered at title/member level for current scope. Copy/location candidates live in `data/books/`; checklist-only exceptions remain deferred until checklist mapping. |
| TB-007C artifacts, unique items, and leveled reward parent rows | `OBJ-001555` through `OBJ-001772` | 218 | `SN-000058` through `SN-000060` | Covered for base game, Dawnguard, and Dragonborn source-list rows. AE equipment parent sets and leveled reward thresholds remain separate follow-up work. |
| TB-007D finite collectible sets | `OBJ-001773` through `OBJ-001918` | 146 | `SN-000061` through `SN-000064` | Covered at finite set/member level for the current source-list pass. Exact route order, location synchronization, bugs, and checklist mapping remain downstream work. |
| TB-007E property, relationship, pet, mount, and role-option leftovers | `OBJ-001919` through `OBJ-001957` | 39 | `SN-000065` through `SN-000068` | Covered at source-list or option-list level. `data/npc/relationship-options.csv` carries 240 candidate rows for later default recommendations and NPC validation. |

Current objective database state: 1,957 objective rows, ending at `OBJ-001957`.

## Spec Requirement Disposition

| Specification requirement area | Current disposition | Remaining action |
| --- | --- | --- |
| Full unique item checklist | Partially covered at source-list/member-table level. Base-game, Dawnguard, and Dragonborn unique items are represented as objective rows; AE equipment parent rows now have member coverage in `data/items/ae-item-members.csv` through TB-007G2. Aggregate status is reconciled in `data/objectives/aggregate-reconciliation.md`. | Validate leveled thresholds, route timing, preservation policy, and checklist mapping in TB-012, TB-020, and TB-030. |
| Full collectible checklist | Major finite sets have objective coverage at this stage. | Synchronize with location/clearable data in TB-008 and checklist rows in TB-030. |
| Full spell, power, enchantment, and alchemy checklist | Powers, shouts, Black Book power systems, transformations, and spell tomes have source-list coverage. AE spell/staff, item, ingredient, and crafting parent sets have member-table coverage through TB-007G2; enchantments, alchemy effects, and system decisions remain open. | Handle skill/perk/enchantment/alchemy/crafting systems in TB-009 and TB-020. |
| Full property, home, and upgrade checklist | City homes, Severin Manor, Hearthfire land/home rows, AE homes, and Goldenhills ownership/system rows exist; supporting detail coverage now lives in `data/properties/property-details.csv`. | Validate exact route timing, safe-storage recommendations, display/checklist selections, family defaults, bug mitigations, and material/economy planning in later constraint and route passes. |
| Full follower, pet, mount, housecarl, steward, and spouse list | Main unlock rows and option/candidate table coverage exist. | Validate defaults, NPC safety, route timing, and checklist synchronization in later recommendation and constraint passes. |
| Books and documents policy | Current required title rows have acquisition/location candidate rows. Duplicate copies are route candidates, not separate objectives. TB-007G4 found no open book/document aggregate placeholder rows. | Re-open only if checklist mapping supplies unique book/note rows not already represented. |

## Residual Work That Is Not A Source-List Gap

The following work remains necessary, but it is intentionally downstream of TB-007F rather than evidence of a missing TB-007 source-list category:

| Remaining work | Destination |
| --- | --- |
| Map-marked locations, discovered state, clearable state, and route-candidate location synchronization | TB-008 |
| Skills to 100, all perks, enchantments, alchemy effects, merchant investments, crafting progression, and grind blocks | TB-009 and TB-020 |
| AE Creation start triggers and level gates | TB-011 |
| Leveled unique item thresholds, maximum-tier timing, and cell-entry or pickup locking | TB-012 and TB-013 |
| Quest conflicts, missables, trophy dependencies, NPC dependencies, bugs, radiants, and Survival Mode constraints | TB-014 through TB-019 |
| Spreadsheet checklist row mapping and coverage validation | TB-030 and TB-031 |

## TB-007G Input List

TB-007G should not be treated as one large undefined cleanup task. The remaining aggregate/member-expansion work should be split into focused slices:

| Follow-up slice | Current parent rows or tables | Required outcome |
| --- | --- | --- |
| AE magic, ingredients, consumables, materials, and practical equipment | `OBJ-000693` through `OBJ-000712` | Complete in TB-007G1. Member coverage now lives in `data/items/ae-item-members.csv`; see `data/items/ae-item-member-reconciliation.md`. |
| AE Alternative Armor and unique/named equipment | `OBJ-000713` through `OBJ-000759` | Complete in TB-007G2. Member coverage now lives in `data/items/ae-item-members.csv`; see `data/items/ae-item-member-reconciliation.md`. |
| Property, home upgrade, furnishing, and service details | Existing property/home/farm rows plus Hearthfire, Dragonborn, and AE property systems | Complete in TB-007G3. Detail coverage now lives in `data/properties/property-details.csv`; see `data/properties/property-detail-reconciliation.md`. |
| Final aggregate reconciliation | `objectives.csv`, `data/books/`, `data/npc/`, `data/items/`, and `data/properties/` | Complete in TB-007G4. See `data/objectives/aggregate-reconciliation.md`; every known aggregate-style row is expanded, table-linked, explicitly parent-only, or delegated to a named downstream task. |

## Result

No obvious additional TB-007 source-list category gap is open after reconciling powers, books/documents, unique items/rewards, finite collectibles, properties, pets, mounts, followers, role assignments, and remaining aggregate rows.

The remaining objective-database gaps before TB-010 are planned work, not hidden TB-007G leftovers:

* TB-008: location and clearable-location objectives.
* TB-009: skill, perk, enchantment, alchemy, merchant-investment, and broader crafting-system objectives.

The next project step should be TB-008: research and enter location and clearable-location objectives.
