# SN-000165 - Mzulft and Winterhold Crisis Route

## Scope

Supports the v1 guide section `Mzulft And The Winterhold Crisis`.

This pass pulls the active College route forward ahead of the remaining Gauldur finale. `Good Intentions` has already started `Revealing the Unseen`, Mirabelle's Mzulft lead is immediately available, and returning from Mzulft triggers `Containment`, which temporarily disrupts College services until the Staff/Eye sequence is resolved. The guide therefore routes Mzulft, the Dwarven Storeroom shard, Arniel's cog turn-in, `Revealing the Unseen`, and `Containment` before returning to the remaining optional College/Gauldur work.

## Sources

| Source ID | Title | Tier | URL | Date | Use |
| --- | --- | --- | --- | --- | --- |
| SRC-001038 | Skyrim:Revealing the Unseen | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Revealing_the_Unseen | 2026-05-13 | Mirabelle briefing, Mzulft route, Gavros, Research Log, Focusing Crystal, Oculory tomes, puzzle sequence, trophy, and Mzulft/Oculory bug notes. |
| SRC-000722 | Skyrim:Mzulft | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Mzulft | 2026-05-13 | Mzulft access lock, Dwarven Storeroom, Dwarven Cogs, fixed Oculory spell tomes, `The Lunar Lorkhan` copy, and pre-clear risk. |
| SRC-001037 | Skyrim:Arniel's Endeavor | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Arniel%27s_Endeavor | 2026-05-13 | Ten-cog stage, Mzulft cog source, later Staff of Tandil random target, later convector stages, and reward spell timing. |
| SRC-000231 | Skyrim:Lost to the Ages | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Lost_to_the_Ages | 2026-05-12 | Four shard locations, reward exclusivity, Forge route, and Aetherial branch handling. |
| SRC-000915 | Skyrim:Lost to the Ages | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Lost_to_the_Ages | 2026-05-13 | Dwarven Storeroom shard timing and Raldbthar-last/Storeroom-last bug workaround support from the later Raldbthar route. |
| SRC-001039 | Skyrim:Containment | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Containment | 2026-05-13 | Winterhold anomaly fight, ten-anomaly counter, Savos Aren's Amulet, Torc of Labyrinthian, Staff of Magnus start, horse risk, and College-service disruption. |
| SN-000148 | Aetherium setup route | Project note | sources/source-notes/SN-000148-aetherium-setup-route.md | 2026-05-13 | Prior shard route state and Aetherium Forge branch policy. |
| SN-000164 | Fellglow and Good Intentions route | Project note | sources/source-notes/SN-000164-fellglow-good-intentions-route.md | 2026-05-13 | Active handoff into `Revealing the Unseen`, Arniel part-one start, and current College state. |

## Route Decisions

`Revealing the Unseen` is routed immediately because it is already active after `Good Intentions`, and UESP records Mzulft as the next destination from Mirabelle's briefing. The guide does not interpose the Gauldur finale here because the College chain is in a fragile active state and the next quest, `Containment`, affects College services.

Mzulft is entered only after `Revealing the Unseen` sends the player there. UESP records that most of the ruin is locked before the quest and that entering/clearing Mzulft early can prevent the quest from starting or activating.

The Dwarven Storeroom shard is routed before the main ruin because it is immediately south of Mzulft, has no enemies, and the Raldbthar shard has already been collected in the Dark Brotherhood/Raldbthar pass. This makes the Storeroom shard the fourth shard and satisfies the earlier Lost to the Ages workaround to take the Storeroom shard after Raldbthar if necessary. The guide records Aetherium Shards at 4 of 4 but leaves the Aetherium Forge for the later named-save reward route because the Forge has mutually exclusive rewards and the College crisis is now active.

Arniel's ten Dwemer Cogs are collected in Mzulft because UESP records that Mzulft has more than ten cogs and the player already started Arniel's first stage after `Hitting the Books`. The guide turns the cogs in before entering the Hall of the Elements for the `Revealing the Unseen` completion scene, because `Containment` temporarily disrupts College services and dialogue. Arniel's second stage is not started here because it creates a random Staff of Tandil target, can overlap `Onmund's Request`, and can be broken by prior boss kills in the selected target.

`Spell Tome: Flames` and `Spell Tome: Frostbite` now use the fixed Mzulft Aedrome copies as their selected sources in `data/constraints/progression-source-selections.csv`. The Oculory puzzle sends the player to the table near the controls, and the Frostbite spell is useful for solving the puzzle. Flames is already known from character creation, but the fixed tome satisfies the spell-tome/book row without relying on vendor stock.

`Research Log` is acquired from Gavros at the Mzulft entrance because it is directly on the quest path and source-listed for `Revealing the Unseen`.

The Mzulft `The Lunar Lorkhan` copy is not selected. It is a duplicate skill-book candidate behind a master-locked side room, and the current selected copy remains Cragwallow Slope pending the later skill-book/Scholar's Insight route. The guide includes only a concise local warning because the room is in the routed dungeon.

`Containment` is included in this section because it begins automatically after the Hall of the Elements scene that completes `Revealing the Unseen`. The guide routes the Savos Aren body scene, ten Winterhold magic anomalies, Mirabelle turn-in, Savos Aren's Amulet, Torc of Labyrinthian, and the start of `The Staff of Magnus`. Labyrinthian itself waits for the next guide section, but only as the next immediate quest block rather than as a distant theme bucket.

Nearby Eastmarch/Kynesgrove corridor rows were audited. Already-routed locations remain complete in prior sections, while remaining clearables, standing stones, mines, mills, and target-pool candidates are not pulled into this pass because they are not on the exact Mzulft execution path or are better handled in target-aware routes. The player-facing guide does not warn about them.

## Coverage Summary

This pass places `Revealing the Unseen`, Mzulft discovery/clear, `Research Log`, Dwarven Storeroom shard, Aetherium Shards 4 of 4, the fixed Mzulft `Spell Tome: Flames` and `Spell Tome: Frostbite` sources, Arniel part-one cog turn-in, `Containment`, and Savos Aren's Amulet.

Rows intentionally staged with concrete reasons: Aetherium Forge and its three mutually exclusive rewards, Ruins of Bthalft, Arniel's later stages and reward spells, `Onmund's Request`, `The Lunar Lorkhan`, and other non-exact-path Eastmarch corridor objectives.

No TB-035-MR-035 `NEEDS ROUTE RESOLUTION` rows remain.
