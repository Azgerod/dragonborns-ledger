# Source Note: Leveled Quest Reward Thresholds and Locks

Status: needs review.

Source note ID: SN-000092

## Claim

UESP identifies the maximum thresholds and several nonstandard lock events for quest-related or placed leveled unique rewards. Most reward items scale when the reward is given, but Chillrend, Dragonbane, the Gauldur weapons, the Nightingale armor set, the Amulet of Articulation, and Miraak's equipment need special handling.

## Routing Relevance

The guide specification requires best-tier versions of leveled unique rewards wherever possible. These thresholds therefore anchor route timing before the level skeleton is drafted, and confirmed cell-entry or quest-start locks must be preserved for TB-013 and later warning placement.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000217 | Skyrim:Leveled Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Leveled_Items | 2026-05-11 | General leveled-item behavior: scaled by player level when reward is given and does not improve afterward. |
| SRC-000325 | Skyrim:Leveled Item Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Leveled_Item_Quests | 2026-05-12 | Strongest-at thresholds, reward sources, and special notes for Chillrend, Trinity Restored, and Amulet of Articulation. |
| SRC-000326 | Skyrim:Alduin's Wall | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Alduin%27s_Wall | 2026-05-12 | Dragonbane route warning not to enter Sky Haven Temple before level 46. |
| SRC-000327 | Skyrim:Forbidden Legend | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Forbidden_Legend | 2026-05-12 | Gauldur Blackblade and Blackbow level setting through shared dungeon spawn behavior. |
| SRC-000328 | Skyrim:Hard Answers | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Hard_Answers | 2026-05-12 | Nightingale Blade reward and highest-tier tempering caveat. |
| SRC-000329 | Skyrim:At the Summit of Apocrypha | 2 - UESP | https://en.uesp.net/wiki/Skyrim:At_the_Summit_of_Apocrypha | 2026-05-12 | Miraak equipment level is determined only after Miraak's corpse appears. |
| SRC-000337 | Skyrim:Amulet of Articulation | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Amulet_of_Articulation | 2026-05-12 | Seven Amulet of Articulation versions are equally likely at all levels. |
| SRC-000338 | Skyrim:Nightingale Armor | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Nightingale_Armor | 2026-05-12 | Nightingale Armor set level registers at the start of Trinity Restored. |
| SRC-000339 | Skyrim:Shield of Solitude | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Shield_of_Solitude | 2026-05-12 | Shield of Solitude maximum threshold and level-32-39 duplicate-stat caveat. |
| SRC-000340 | Skyrim:Nightingale Boots | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Nightingale_Boots | 2026-05-12 | Highest-tier Muffle magnitude utility caveat. |
| SRC-000341 | Skyrim:The Wolf Queen Awakened | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Wolf_Queen_Awakened | 2026-05-12 | Shield of Solitude reward timing at final report to Falk. |
| SRC-000342 | Skyrim:The Pale Lady | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Pale_Lady | 2026-05-12 | Pale Blade strongest threshold and Ra'jirr reward context. |
| SRC-000343 | Skyrim:Good Intentions | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Good_Intentions | 2026-05-12 | Mage's Circlet reward from Savos Aren. |
| SRC-000344 | Skyrim:Blindsighted | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Blindsighted | 2026-05-12 | Nightingale Bow reward from Karliah after escaping Irkngthand. |
| SRC-000345 | Skyrim:Trinity Restored | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Trinity_Restored | 2026-05-12 | Nightingale Armor set is placed in inventory during the quest sequence. |
| SRC-000346 | Skyrim:Under New Management | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Under_New_Management | 2026-05-12 | Amulet reward is handed over by Brynjolf after the Guild Master ceremony. |
| SRC-000347 | Skyrim:The Pursuit | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Pursuit | 2026-05-12 | Chillrend location and Riftweald Manor early-entry caveat context. |

## Evidence Summary

UESP's Leveled Items page gives the general rule that leveled items are scaled at reward time and do not upgrade later. The Leveled Item Quests page provides the strongest-at thresholds for the quest-related queue: Dragonbane, Chillrend, Nightingale Blade, Nightingale Bow, Mage's Circlet, The Pale Blade, Shield of Solitude, the Nightingale armor set, the Amulet of Articulation, and Miraak's equipment.

Several items are not simple final-reward locks:

* Chillrend's level is determined when Riftweald Manor is first entered.
* Dragonbane should be protected by not entering Sky Haven Temple before level 46.
* Gauldur Blackblade and Gauldur Blackbow reach their strongest versions at level 36+, but Forbidden Legend notes that reading Lost Legends or approaching any of the related dungeons can spawn all four linked dungeons and set the bosses' levels.
* Nightingale Armor, Boots, Gloves, and Hood reach their strongest tier at level 32+, but their level registers at the start of Trinity Restored rather than when the armor is picked up.
* Miraak's Sword, Staff, and mask reach their strongest tier at level 60+, and the At the Summit of Apocrypha page states that their level is determined after Miraak's corpse appears.
* The Amulet of Articulation is random rather than level-gated; all seven player versions are equally likely at all levels.

Two useful-version caveats should survive later review. The highest Nightingale Blade tier is the source-listed maximum, but UESP's Hard Answers page says the level 46+ blade cannot be tempered, making the level 36-45 blade the better practical version if tempering matters. Nightingale Boots have a highest-tier Muffle magnitude caveat, but the table still keeps the level 32+ tier as the collection-safe maximum unless the route later chooses a different utility definition.

## Confidence and Open Questions

Confidence is high for the numeric thresholds and the confirmed special lock events listed above. The route still needs a project decision on whether Nightingale Blade should prioritize the 46+ maximum stat tier or the 36-45 temperable practical tier. TB-013 should harden the cell-entry warnings for Riftweald Manor, Sky Haven Temple, Forbidden Legend dungeon approaches, and any unconfirmed first-entry cases such as Frostmere Crypt.

## Linked Records

`data/constraints/leveled-unique-items.md`; OBJ-000198; OBJ-001750; OBJ-001751; OBJ-001752; OBJ-001753; OBJ-001760; OBJ-001761; OBJ-001762; OBJ-001763; OBJ-001764; OBJ-001765; OBJ-001766; OBJ-001767; OBJ-001768; OBJ-001769; OBJ-001770; OBJ-001771; OBJ-001772.
