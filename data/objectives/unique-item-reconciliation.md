# Unique Item Reconciliation

Status: needs review.

This file reconciles the TB-007C source-list passes before finite collectible work begins. It does not introduce new gameplay claims; it summarizes rows already supported by `SN-000058`, `SN-000059`, and `SN-000060`.

## Source-List Coverage

| Slice | Source note | Objective rows | Row count | Scope |
| --- | --- | ---: | ---: | --- |
| Artifact inventory | `SN-000058-artifact-inventory.md` | `OBJ-001555` through `OBJ-001614` | 60 | Base-game, Dawnguard, and Dragonborn artifacts outside AE parent sets. |
| Non-artifact unique item inventory | `SN-000059-unique-item-inventory.md` | `OBJ-001615` through `OBJ-001749` | 135 | Base-game, Dawnguard, and Dragonborn unique weapons, armor, clothing, jewelry, and miscellaneous items. |
| Leveled reward parent inventory | `SN-000060-leveled-unique-reward-inventory.md` | `OBJ-001750` through `OBJ-001772` | 23 | Parent rows for level/version-sensitive rewards and items that need later threshold and lock-timing validation. |

Current TB-007C source-list coverage totals 218 rows. These rows are not route-ready: route placement, branch handling, missability, safe storage, bugs, trophy effects, checklist mapping, and acquisition timing remain deferred to later constraint and route passes.

## Existing Related Rows Not Duplicated

| Subject | Existing row | Reconciliation |
| --- | --- | --- |
| Oghma Infinium | `OBJ-001079` | Already represented as a unique book/artifact row from the book pass; not duplicated as an artifact row. |
| Skeleton Key | `OBJ-000180` | Represented as Nocturnal artifact handling because it must be coordinated with Thieves Guild completion; not duplicated as a collectible artifact objective. |

## Intentional Parent/Item Overlaps

The rows below are intentional. The item row tracks acquisition/preservation; the leveled reward parent row tracks the later need to verify maximum-tier level and lock timing in TB-012.

| Item | Acquisition/preservation row | Leveled validation parent row | Later action |
| --- | --- | --- | --- |
| Chillrend | `OBJ-001571` | `OBJ-001750` | Synchronize threshold and lock rule in TB-012. |
| Dragonbane | `OBJ-001573` | `OBJ-001751` | Synchronize threshold and lock rule in TB-012. |
| Miraak's Sword | `OBJ-001575` | `OBJ-001760` | Synchronize threshold and lock rule in TB-012. |
| Miraak's Staff | `OBJ-001566` | `OBJ-001761` | Synchronize threshold and lock rule in TB-012. |
| Nightingale Blade | `OBJ-001576` | `OBJ-001762` | Synchronize threshold and lock rule in TB-012. |
| Nightingale Bow | `OBJ-001559` | `OBJ-001763` | Synchronize threshold and lock rule in TB-012. |
| Miraak's Dragon Priest Mask | `OBJ-001596` | `OBJ-001765` | Synchronize threshold, Dragon Priest Mask collectible handling, and final checklist mapping later. |
| Amulet of Articulation | `OBJ-001605` | `OBJ-001771` | Synchronize version mechanics in TB-012. |

No parent rows should be deleted merely because they overlap an acquisition row. They carry a different validation responsibility.

## Deferred Boundaries

| Boundary | Current treatment | Follow-up |
| --- | --- | --- |
| AE Creation equipment and unique items | Parent-set rows only: `OBJ-000713` through `OBJ-000759`. | Expand individual item members and acquisition rules in a later member/acquisition pass. |
| Alternative Armor parent rows | Parent rows remain AE-scoped. Their `unique_rewards` cells now use specific set names instead of one repeated generic label. | Member lists, crafting, checklist mapping, and route placement remain deferred. |
| Paragons | Deferred from unique-item inventory. | Handle as a finite collectible set in TB-007D. |
| Dragon Priest Masks | Artifact rows exist for source-listed artifact masks. | Synchronize with collectible-set parent/member handling in TB-007D. |
| Leveled thresholds and lock rules | Parent rows exist only as markers. | Validate exact levels, pickup/reward/cell-entry locking, and warning placement in TB-012. |
| Checklist-only unique items | Not fully knowable until checklist mapping. | Reconcile in checklist synchronization and later coverage QA. |

## Excluded Source-List Items

| Item | Reason | Supporting source note |
| --- | --- | --- |
| Space Core | Outside allowed base-game/DLC/official PS4 AE scope. | `SN-000059` |
| Master Sword | Outside allowed base-game/DLC/official PS4 AE scope. | `SN-000059` |
| Karliah's Bow | Source-marked unavailable through normal gameplay. | `SN-000059` |
| Tsun's Battle Axe | Source-marked console-only and unplayable even if added. | `SN-000060` |

## Reconciliation Result

The base-game, Dawnguard, and Dragonborn source-list passes for artifacts, non-artifact unique items, and leveled unique reward parents are internally reconciled for this project stage.

Remaining work before route placement:

* Expand AE parent-set item members and acquisition candidates.
* Build finite collectible-set rows, including Paragons and Dragon Priest Mask synchronization.
* Validate leveled reward thresholds and lock timing in TB-012.
* Validate missability, branch handling, conflicts, bugs, NPC dependencies, trophies, safe storage, and checklist mapping in later passes.
