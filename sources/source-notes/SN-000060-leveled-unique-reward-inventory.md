# Source Note: Leveled Unique Reward Inventory

Status: needs review.

Source note ID: SN-000060

## Claim

UESP's leveled-item inventory identifies source-listed level/version-sensitive rewards and items that need later maximum-tier threshold, version-mechanic, and lock-timing validation before route placement.

## Routing Relevance

The specification requires best-tier versions of leveled unique rewards wherever possible and treats leveled reward timing and cell-entry locking as hard routing constraints. This pass adds source-list parent rows only. It does not decide exact level thresholds, pickup versus cell-entry locking, hard-save placement, branch placement, or final route timing.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000217 | Skyrim:Leveled Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Leveled_Items | 2026-05-11 | Leveled item overview and source-list headings. |
| SRC-000224 | Skyrim:Tsun's Battle Axe | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Tsun%27s_Battle_Axe | 2026-05-11 | Console-only and unplayable item exclusion. |

## Evidence Summary

The UESP Leveled Items page was fetched through the MediaWiki API on 2026-05-11. It explains that leveled items are generally scaled by player level when the reward is given and do not improve afterward as the character levels.

The source page contains 24 item headings. This pass adds 23 `unique_item` parent rows:

| subcategory | rows |
| --- | ---: |
| `leveled_weapon_reward_parent` | 15 |
| `leveled_armor_reward_parent` | 6 |
| `leveled_clothing_reward_parent` | 2 |

By source content, the rows cover 20 base-game items and 3 Dragonborn items.

Some parent rows overlap existing artifact rows: Chillrend, Dragonbane, Miraak's Sword, Miraak's Staff, Nightingale Blade, Nightingale Bow, Miraak's Dragon Priest Mask, and Amulet of Articulation. The parent rows are retained as threshold-validation markers for TB-012; they do not replace the item-acquisition rows.

Excluded from required rows:

* Tsun's Battle Axe, because the linked UESP item page identifies it as unobtainable except through console use and unplayable even if added.

## Confidence and Open Questions

Confidence is high for the source-list inventory as of 2026-05-11. Confidence is intentionally unresolved for final routing because this pass does not validate exact maximum thresholds, version mechanics, pickup timing, cell-entry locking, missability, bug risk, or faction/branch dependencies.

Open questions for TB-012 include exact maximum-tier levels, whether each item locks on pickup, reward grant, quest stage, or cell entry, whether any source-listed item has non-level randomization rather than true level scaling, and how overlapping artifact rows should be synchronized with the final unique-item checklist.

## Linked Records

OBJ-001750 through OBJ-001772.
