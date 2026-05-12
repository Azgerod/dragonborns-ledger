# Source Note: Non-Artifact Unique Item Inventory

Status: needs review.

Source note ID: SN-000059

## Claim

UESP's unique-item inventories identify base-game and official DLC unique weapons, armor, clothing, jewelry, and other unique items that should be represented before route placement, excluding artifacts already covered by the artifact pass, AE Creation parent-set rows, collectible-set members deferred to the collectible pass, and items outside normal PS4 AE scope.

## Routing Relevance

The specification requires all unique items obtainable on the main route, unique-item preservation, safe storage, branch handling for meaningful mutually exclusive rewards, and later checklist synchronization. This pass creates source-list rows for non-artifact unique items without deciding exact route timing, branch treatment, missability, item-specific acquisition routes, leveled reward thresholds, cell-entry locking, or safe-storage placement.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000218 | Skyrim:Unique Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Unique_Items | 2026-05-11 | Unique-item overview and links to subtype inventories. |
| SRC-000219 | Skyrim:Unique Weapons | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Unique_Weapons | 2026-05-11 | Unique weapon headings and linked item metadata. |
| SRC-000220 | Skyrim:Unique Armor | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Unique_Armor | 2026-05-11 | Unique armor headings and linked item metadata. |
| SRC-000221 | Skyrim:Unique Clothing | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Unique_Clothing | 2026-05-11 | Unique clothing headings and linked item metadata. |
| SRC-000222 | Skyrim:Unique Jewelry | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Unique_Jewelry | 2026-05-11 | Unique jewelry headings and linked item metadata. |
| SRC-000223 | Skyrim:Other Unique Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Other_Unique_Items | 2026-05-11 | Other unique item headings and linked item metadata. |

## Evidence Summary

The unique-item subtype pages were fetched through the UESP MediaWiki API on 2026-05-11. The scan found 164 source headings across unique weapons, armor, clothing, jewelry, and other unique items.

This pass adds 135 `unique_item` objective rows:

| subcategory | rows |
| --- | ---: |
| `unique_weapon` | 39 |
| `unique_armor` | 49 |
| `unique_clothing` | 13 |
| `unique_jewelry` | 26 |
| `unique_misc_item` | 8 |

By source content, the rows cover 96 base-game items, 10 Dawnguard items, and 29 Dragonborn items.

Excluded from this pass:

* 18 Creation Club headings, because AE equipment is already represented by AE parent-set rows and needs later member expansion.
* 3 artifact duplicates already represented by `SN-000058`: The Rueful Axe, Bloodskal Blade, and Ring of Hircine.
* 5 Paragon headings, because Paragons are better handled as a collectible set in TB-007D.
* Space Core and Master Sword, because source metadata identifies them as outside the allowed base/DLC/official PS4 AE scope.
* Karliah's Bow, because the source marks it unavailable through normal gameplay.

## Confidence and Open Questions

Confidence is high for source-list membership as of 2026-05-11. Confidence is lower for route readiness because this pass intentionally does not validate item-specific acquisition details, branch-only availability, missability, NPC dependencies, bugs, trophy relevance, leveled thresholds, or cell-entry locking.

Open questions include which items belong on the canonical main route versus branch routes, which items can be safely left to cleanup, which items require hard saves or faction choices, and which rows should later synchronize with collectible-set, enchantment, property-display, or checklist-specific objectives.

## Linked Records

OBJ-001615 through OBJ-001749.
