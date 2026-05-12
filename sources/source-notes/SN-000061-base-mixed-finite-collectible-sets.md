# Source Note: Base and Mixed Finite Collectible Sets

Status: needs review.

Source note ID: SN-000061

## Claim

UESP identifies several finite collectible sets that need objective-database coverage before routing: Stones of Barenziah, Crimson Nirnroot, Dragon Priest Masks, Dragon Claws, Treasure Maps, and Bugs in a Jar.

## Routing Relevance

The specification requires all finite collectible sets, all unique items obtainable on the main route, checklist synchronization, and explicit later routing for appendix-backed collectible objectives. This pass creates source-list objective rows without deciding route order, safe first-entry timing, ownership/crime handling, bug mitigations, or final checklist mapping.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000225 | Skyrim:No Stone Unturned | 2 - UESP | https://en.uesp.net/wiki/Skyrim:No_Stone_Unturned | 2026-05-12 | Stones of Barenziah quest and 24 source-listed gem locations. |
| SRC-000226 | Skyrim:A Return To Your Roots | 2 - UESP | https://en.uesp.net/wiki/Skyrim:A_Return_To_Your_Roots | 2026-05-12 | Thirty-sample Crimson Nirnroot requirement and Blackreach sample count. |
| SRC-000214 | Skyrim:Armor Artifacts | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Armor_Artifacts | 2026-05-11 | Dragon Priest Mask artifact headings already represented by unique-item artifact rows. |
| SRC-000227 | Skyrim:Quest Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Quest_Items | 2026-05-12 | Dragon Claw table. |
| SRC-000228 | Skyrim:Treasure Maps | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Treasure_Maps | 2026-05-12 | Treasure Map inventory, map locations, and chest areas. |
| SRC-000229 | Skyrim:Miscellaneous Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Miscellaneous_Items | 2026-05-12 | Bugs in a Jar inventory and locations. |

## Evidence Summary

The `No Stone Unturned` page lists 24 Stone of Barenziah locations and the Crown recovery step. This pass adds one set parent row plus 24 member rows.

The `A Return To Your Roots` page requires 30 Crimson Nirnroot samples and notes more available plants in Blackreach than the quest requires. This pass adds a count-based parent row rather than arbitrary plant-member rows; route planning can later choose a practical 30-sample path.

Dragon Priest Mask item rows already exist in the artifact inventory from `SN-000058`. This pass adds a collectible-set parent row so the mask set and Konahrik synchronization are visible without duplicating the existing mask item rows.

The `Quest Items` Dragon Claws table lists 12 claw entries, including the two Dragonborn Amethyst Claw halves. This pass adds one parent row plus 12 member rows.

The `Treasure Maps` table lists 13 treasure maps, including Deathbrand Treasure Map. This pass adds one parent row plus 13 member rows that track both obtaining and resolving each map.

The `Miscellaneous Items` Bugs in a Jar table lists eight jar entries, including five base-game jars and three AE Creation jar items. This pass adds one parent row plus eight member rows.

## Confidence and Open Questions

Confidence is high for source-list membership as of 2026-05-12. Exact route timing remains open for locked/interior locations, quest-state access, ownership, missability, cell-entry risk, bug risk, Survival Mode burden, and checklist row mapping.

The Crimson Nirnroot row is intentionally count-based because the quest requires 30 samples while the source identifies more possible plants. If a later checklist requires every source-listed plant location rather than quest completion, TB-007G or checklist mapping should expand it.

## Linked Records

OBJ-001773 through OBJ-001835.
