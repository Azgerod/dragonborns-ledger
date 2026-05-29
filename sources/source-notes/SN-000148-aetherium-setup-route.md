# SN-000148 - Aetherium Setup Route

Status: route-writing source note for TB-035-MR-020.

## Scope

This note supports the v1 guide section `Arkngthamz And The First Aetherium Shards`. The section replaces the old Aetherium setup scaffold with a concrete first Aetherium pass: read `The Aetherium Wars`, start `Lost to the Ages`, complete Arkngthamz through Zephyr and the first shard, collect the Deep Folk Crossing shard, and stop before the Raldbthar, Mzulft/Dwarven Storeroom, and Aetherium Forge reward boundaries.

## Sources

| Source ID | Title | Tier | URL | Accessed | Used for |
| --- | --- | --- | --- | --- | --- |
| SRC-000231 | Skyrim:Lost to the Ages | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Lost_to_the_Ages | 2026-05-12 | Quest start options, shard locations, Zephyr reward, Aetherial reward exclusivity, trophy timing, Raldbthar/Dwarven Storeroom bug notes, and forge bugs. |
| SRC-000719 | Skyrim:Arkngthamz | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Arkngthamz | 2026-05-13 | Arkngthamz route, Katria's Journal, Zephyr placement, tonal-lock behavior, Aetherium Wars quest-item behavior, and clearability caveat. |
| SRC-000720 | Skyrim:Deep Folk Crossing | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Deep_Folk_Crossing | 2026-05-13 | Deep Folk Crossing marker, shard placement on the north plinth, Dwemer convector, and nearby adventurer/book context. |
| SRC-000721 | Skyrim:Raldbthar | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Raldbthar | 2026-05-13 | Raldbthar shard location, Alain Dufont overlap, Great Lift, Aegisbane, and book placement. |
| SRC-000722 | Skyrim:Mzulft | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Mzulft | 2026-05-13 | Dwarven Storeroom separation, Mzulft College quest lock risk, Dwemer convector, and Mzulft book/spell support rows. |
| SRC-000723 | Skyrim:The Aetherium Forge | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Aetherium_Forge | 2026-05-13 | Forge access, one-reward crafting boundary, Forgemaster arena, and reward-material context. |
| SRC-000724 | Skyrim:The Aetherium Wars | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Aetherium_Wars | 2026-05-13 | Book-copy placement, especially the Dwemer Museum copy. |
| SRC-000725 | Skyrim:Light Armor Forging | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Light_Armor_Forging | 2026-05-13 | Nearby Arkngthamz skill-book candidate audit. |

## Route Decisions

The guide reads `The Aetherium Wars` in the Dwemer Museum because the player already has Calcelmo's museum access from the earlier Markarth/Nchuand-Zel route, and the UESP book page places a copy on a table in the southwestern museum corner. The player reads it in place rather than stealing or carrying it. This cleanly satisfies the quest-book row and starts the Arkngthamz objective before visiting Deep Folk Crossing.

Arkngthamz is routed now because the route is already in the Reach, the quest's suggested level is 16, and the dungeon is the coherent start point for Katria, Zephyr, Katria's Journal, the tonal lock, and the Arkngthamz Aetherium Shard. The player-facing guide uses an exterior rotating save before entry because UESP records tonal-lock door bugs that may be resolved by reloading a pre-entry save and avoiding reliance on mid-dungeon saves. The route does not attempt to force Arkngthamz's bugged cleared tag by deliberately triggering additional tonal-lock traps; the player completes the route-relevant dungeon content through the shard treasury.

Deep Folk Crossing is routed immediately after Arkngthamz because it is a non-clearable landmark in the same broad Reach phase and its Aetherium Shard is on an exterior plinth rather than deep in a dungeon. The guide explicitly discovers the landmark, takes the shard, and leaves the Dwemer convector alone for the later College/Arniel route.

Raldbthar is not routed in this pass. UESP ties Raldbthar to Alain Dufont and the Dark Brotherhood quest `Mourning Never Comes`; it also places the shard at the end of Raldbthar Deep Market and records Lost to the Ages bugs if the player leaves Raldbthar before taking the shard or if the shard fails to update. The Raldbthar pass should bundle Alain Dufont, Aegisbane, Raldbthar clear/location handling, Great Lift at Raldbthar, `2920, Last Seed, v8` handling, and the Raldbthar shard.

The Dwarven Storeroom shard is not routed in this pass even though the storeroom itself has no enemies. UESP records a bug workaround to pick up the Dwarven Storeroom shard last if the Raldbthar shard misidentifies or fails to update. Mzulft also has a separate main-ruin bug if cleared before `Revealing the Unseen`, and the broader Mzulft support rows include College, spell-tome, skill-book, Dwemer convector, and clearable-location work. The safer sequence is Raldbthar first, then Dwarven Storeroom/Mzulft in the later Eastmarch/College bundle.

The Aetherium Forge remains held for `HS-AETHERIUM-FORGE`. The reward is mutually exclusive: Aetherial Crown is the canonical main-route reward, while Aetherial Staff and Aetherial Shield require branch capture and reload. Taron Dreth's Robes also require a completed Aetherial reward and therefore stay with the later Forge/follow-up pass.

The nearby `Light Armor Forging` copy northeast of Arkngthamz was audited but not routed here. Its objective is to read a skill book, not merely to possess a duplicate copy, and the route is preserving skill-book reads for the Scholar's Insight window. Because the copy is a duplicate source in a chest rather than a unique quest item, the guide does not add a separate unmarked detour or ask the player to carry an unread skill book for many sections.

## Coverage Notes

This pass directly places `The Aetherium Wars`, Zephyr, Arkngthamz discovery/exploration, Deep Folk Crossing discovery, the Arkngthamz Aetherium Shard, and the Deep Folk Crossing Aetherium Shard in the player-facing guide. It starts `Lost to the Ages` and advances the Aetherium Shards parent set to 2 of 4 without completing the quest.

Held rows are deliberately mapped to later route bundles rather than left vague: Raldbthar shard/clear/Great Lift/Aegisbane/Alain Dufont, Dwarven Storeroom/Mzulft/College support, Forge reward branches, canonical Aetherial Crown, and Taron Dreth's Robes. No TB-035-MR-020 `NEEDS ROUTE RESOLUTION` notes remain.
