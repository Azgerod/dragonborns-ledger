# SN-000155 - Potema, Shield Of Solitude, And Bone Wolf Route

Status: route-writing source note for TB-035-MR-027.

## Scope

This note supports the v1 guide section `Potema, Shield Of Solitude, And Bone Wolf`. The section routes `Letter from Falk Firebeard`, `The Wolf Queen Awakened`, Styrr's `Turn Undead` spell tome reward, Potema's Catacombs, the level-40 Shield of Solitude handoff, Blue Palace `Lost Legends`, Folgunthur, Mikrul's Gauldur fragment, `Letter from Bolgeir Bearclaw`, `Let Sleeping Wolves Lie`, `Necromancer's Journal`, Bone Wolf, and the `Teleport Pet: Bone Wolf` spell.

## Sources

| Source ID | Title | Tier | URL | Accessed | Used for |
| --- | --- | --- | --- | --- | --- |
| SRC-000825 | Skyrim:The Wolf Queen Awakened | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Wolf_Queen_Awakened | 2026-05-13 | Falk letter trigger, Styrr dialogue/reward, Potema route, Shield of Solitude reward, Bone Wolf follow-up, and quest bugs. |
| SRC-000849 | Skyrim:Shield of Solitude | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Shield_of_Solitude | 2026-05-13 | Level-40 strongest version, level-32-to-39 duplicate-stat caveat, reward stats, and enchantment identity. |
| SRC-000850 | Skyrim:Potema's Catacombs | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Potema%27s_Catacombs | 2026-05-13 | Dungeon zones, Potema route, `Surfeit of Thieves`, and `Legend of Krately House` boss-chest copy. |
| SRC-000851 | Skyrim:Let Sleeping Wolves Lie | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Let_Sleeping_Wolves_Lie | 2026-05-13 | Courier start, camp location, necromancer loot, Totem Bone handoff, Bone Wolf reward, and bug fallback. |
| SRC-000852 | Skyrim:Bone Wolf | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bone_Wolf | 2026-05-13 | Creation overview, pet behavior, carrying, and Bone Wolf's Revenge context. |
| SRC-000853 | Skyrim:Letter from Falk Firebeard | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Letter_from_Falk_Firebeard | 2026-05-13 | Falk courier document identity. |
| SRC-000854 | Skyrim:Letter from Bolgeir Bearclaw | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Letter_from_Bolgeir_Bearclaw | 2026-05-13 | Bone Wolf courier document identity. |
| SRC-000855 | Skyrim:Necromancer's Journal (Bone Wolf) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Necromancer%27s_Journal_(Bone_Wolf) | 2026-05-13 | Bone Wolf journal title and checklist document identity. |
| SN-000092 | Leveled quest reward thresholds and locks | Project source note | sources/source-notes/SN-000092-leveled-quest-reward-thresholds-and-locks.md | 2026-05-13 | Project-level Shield of Solitude reward-time gate and Gauldur level-36 threshold. |
| SRC-000327 | Skyrim:Forbidden Legend | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Forbidden_Legend | 2026-05-13 | Lost Legends start, Folgunthur stage, Gauldur Blackblade/Blackbow level lock, Daynas journal bug, and remaining Gauldur chain ordering. |
| SRC-000977 | Skyrim:Folgunthur | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Folgunthur | 2026-05-13 | Folgunthur dungeon route, Daynas camp, Ivory Dragon Claw, Gauldur Blackblade, Writ of Sealing, Frost Breath word wall, and local skill books. |

## Route Decisions

`The Wolf Queen Awakened` is placed here because prior Solitude work completed `The Man Who Cried Wolf`, held the courier follow-up, and the route has now reached the project Shield of Solitude threshold. UESP records the Shield as Falk's final reward for `The Wolf Queen Awakened`, and the project leveled-reward table requires the handoff at level 40+. The guide therefore checks level 40 before speaking to Falk about the letter and again before the final report.

`HS-SOLITUDE-SHIELD-LEVEL40` protects two adjacent risks: the Shield of Solitude's max-tier reward and the Bone Wolf courier follow-up. UESP records a level-32-to-39 Shield caveat, and the Bone Wolf pages record courier and spawn bugs. The hard save is not a branch save; it is a reward/courier recovery point.

Styrr's `Spell Tome: Turn Undead` is now the selected deterministic source for the Turn Undead spell-tome objective. The previous progression-source default pointed to College vendor stock, but this quest gives the tome directly during required route play. The source selection table is updated accordingly.

Potema's Catacombs is routed as a single quest dungeon. `Surfeit of Thieves` is left closed because it is an in-world skill-book copy reached before the Scholar's Insight reading window. `Legend of Krately House` is changed to the selected copy for that title because UESP places it in Potema's boss chest; a container copy can be taken without opening it, and the route is already clearing the dungeon for Potema. The skill-book read remains staged for Scholar's Insight.

Returning Potema's Skull to Styrr is recorded as Haafingar help progress, while final quest completion and Sideways progress are recorded at Falk's reward handoff. The guide tells the player to preserve the Shield of Solitude rather than disenchant it. The Resist Magic enchantment row remains staged for a disposable source because the project unique-item policy preserves unique rewards.

Bone Wolf is routed immediately after `The Wolf Queen Awakened` because UESP ties `Letter from Bolgeir Bearclaw` directly to that quest completion, and the camp route is a compact Haafingar/Hjaalmarch follow-up. The guide prioritizes receiving the courier letter before using the camp fallback because the letter is a tracked document row. The camp route then acquires `Necromancer's Journal`, the cage key, Totem Bone, Bone Wolf, and the associated teleport spell in one pass.

The retrospective nearby-objective audit moves `Lost Legends` and Folgunthur into this section. The route is level 40+, the Blue Palace has a source-listed city copy of `Lost Legends`, and the Bone Wolf camp sends the player directly to the Folgunthur area. Holding Folgunthur only because "Gauldur chain later" was theme bucketing rather than a real constraint. The guide therefore reads `Lost Legends` in the Blue Palace, avoids the source-listed Daynas Valen's Journal bad-order bug, clears Folgunthur, acquires the Ivory Dragon Claw, Daynas Valen's Notes, Writ of Sealing (Mikrul), the max-tier Gauldur Blackblade, and Frost Breath: Krah, then continues to the Bone Wolf camp.

The remaining Gauldur work still stays intact where splitting would be artificial: Saarthal remains with the College `Under Saarthal` route, Geirmund's Hall remains with the later linked-dungeon route, and Reachwater Rock remains the final reforge after all fragments are in hand. This is quest-chain integrity rather than hold/theme bucketing.

Most Solitude miscellaneous favors are not repeated here because the forced Solitude visit in MR-015 already completed Octieve, Return to Grace, Sorex, Spiced Wine, No News is Good News, and related first-Solitude favor work. Proudspire remains a property/economy objective because its 25,000-gold purchase and furnishing scope need a later house-buying block. Captain Aldis, Ahtar, Noster, Broken Oar, and `The Dainty Sload` remain with their previously recorded target-aware, Civil War, or Thieves Guild bundles. Sybille's fixed Pinemoon vampire favor is left for the next Haafingar cave sweep.

The Expanded Crossbow Pack is audited but not inserted into this Potema section. It is a Fletcher purchase/crafting set with source-listed member coverage still requiring exact route/checklist treatment, and this section does not otherwise send the player to Fletcher. Keep it with the later Dawnguard/crossbow/crafting equipment pass rather than turning the Shield gate into a shopping list.

## Coverage Notes

This pass directly places `Letter from Falk Firebeard`, `The Wolf Queen Awakened`, `Spell Tome: Turn Undead`, the Turn Undead learned spell, `Legend of Krately House` selected-copy acquisition for later reading, Shield of Solitude, `Letter from Bolgeir Bearclaw`, `Let Sleeping Wolves Lie`, `Necromancer's Journal (Bone Wolf)`, Bone Wolf, `Teleport Pet: Bone Wolf`, and related Sideways/Haafingar help progress.

Held or staged rows are mapped in coverage rather than exposed as player-facing warning lists: `Surfeit of Thieves`, `Legend of Krately House` read completion, `Fire and Darkness` read completion, Resist Magic enchantment learning, Absorb Health enchantment learning from a disposable source, remaining `Forbidden Legend` stages after Folgunthur, Proudspire/Thane/Jordis, Captain Aldis, Ahtar, Noster, Sybille's Pinemoon favor, Broken Oar, `The Dainty Sload`, and Expanded Crossbow Pack.

No TB-035-MR-027 `NEEDS ROUTE RESOLUTION` notes remain.
