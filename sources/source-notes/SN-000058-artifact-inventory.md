# Source Note: Artifact Inventory

Status: needs review.

Source note ID: SN-000058

## Claim

UESP's artifact inventories identify base-game and official DLC weapon, armor, clothing, and other artifacts that should be represented as unique-item objectives before route placement. This pass adds source-list rows for non-Creation Club artifacts that were not already represented by a more specific objective row.

## Routing Relevance

The specification requires all unique items obtainable on the main route, best-tier versions of leveled unique rewards where possible, artifact preservation, and branch handling for meaningful mutually exclusive outcomes. This source-list pass creates artifact objective rows without deciding exact route timing, branch treatment, leveled reward thresholds, cell-entry locking, safe-storage placement, or final checklist synchronization.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000012 | Skyrim:Artifacts | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Artifacts | 2026-05-11 | Artifact definition, disenchanting caveat, and artifact category overview. |
| SRC-000213 | Skyrim:Weapon Artifacts | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Weapon_Artifacts | 2026-05-11 | Weapon artifact headings. |
| SRC-000214 | Skyrim:Armor Artifacts | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Armor_Artifacts | 2026-05-11 | Armor artifact and Dragon Priest Mask artifact headings. |
| SRC-000215 | Skyrim:Clothing Artifacts | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Clothing_Artifacts | 2026-05-11 | Clothing artifact headings. |
| SRC-000216 | Skyrim:Other Artifacts | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Other_Artifacts | 2026-05-11 | Other artifact headings. |
| SRC-000217 | Skyrim:Leveled Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Leveled_Items | 2026-05-11 | Cross-check that some artifact rows need later leveled-threshold validation. |

## Evidence Summary

The artifact source pages were fetched through the UESP MediaWiki API on 2026-05-11. After excluding Creation Club artifact headings already represented by AE unique-equipment parent rows, the pages yielded 62 base-game or official DLC artifact headings.

This pass adds 60 `unique_item` objective rows. Oghma Infinium is already represented as a unique book/artifact row at `OBJ-001079`, and Skeleton Key handling is already represented by the Nocturnal artifact caveat row at `OBJ-000180`; they are not duplicated here.

The added rows cover weapon artifacts, armor artifacts, Dragon Priest Mask artifact headings, clothing artifacts, and other artifacts. Dragon Priest Mask artifact rows are also marked for later collectible-set synchronization, but the collectible-set parent and location routing belong to the collectible pass.

UESP's Leveled Items page confirms that some artifacts also belong to the leveled-item validation problem. This pass does not enter thresholds or lock rules; TB-012 must verify exact maximum-tier levels and pickup/cell-entry behavior before routing.

## Confidence and Open Questions

Confidence is high for source-list artifact membership as of 2026-05-11. Confidence is lower for route readiness because this pass intentionally does not validate acquisition details, mutually exclusive outcomes, quest prerequisites, bugs, NPC dependencies, trophy counters, leveled thresholds, or cell-entry locking.

Open questions include which artifacts are main-route acquisitions versus branch-route acquisitions, which Dragon Priest Mask rows should be synchronized with collectible-set parent rows, which artifact rewards are mutually exclusive with other rewards, and which artifact rows need hard level gates.

## Linked Records

OBJ-001555 through OBJ-001614.
