# SN-000195 - High-Risk AE Route

## Sources

| Source ID | Source | Notes |
| --- | --- | --- |
| SRC-000060 | UESP, `Skyrim:Bones for a Crow` | Dragon Plate quest start, Crowstooth's Camp, Linelle's Note, Arcwind Point Crowstooth/Bjormund route, Dragonbone Mail reward set, and Castle Dour dossier placement. |
| SRC-000077 | UESP, `Skyrim:Pets of Skyrim (quest)` | Pets of Skyrim pet list and Thistle objective context. |
| SRC-000155 | UESP, `Skyrim:Umbra Items` | Umbra reward item and Champion's Rest key item membership. |
| SRC-000156 | UESP, `Skyrim:The Cause` | The Cause Creation overview. |
| SRC-000254 | UESP, `Skyrim:Alternative Armors - Dragon Plate Items` | Dragon Plate equipment member list. |
| SRC-000256 | UESP, `Skyrim:Redguard Elite Armaments Items` | Redguard Elite Armaments equipment member list. |
| SRC-000258 | UESP, `Skyrim:The Cause Items` | The Cause equipment, ingredients, shards, keys, books, and spell-tome member list. |
| SRC-000298 | UESP, `Skyrim:Atronach Forge` | Atronach Forge context for the later Conjure Ayleid Lich recipe route. |
| SRC-000323 | UESP, `Skyrim:The Cause (quest)` | Level-46 courier start, The Cause quest order, Rielle shard order, Red Scar/Vonos handoff, and bug-sensitive Janus/Great Welkynd ordering. |
| SRC-000439 | UESP, `Skyrim:Mythic Dawn Camp` | Mythic Dawn Camp stage-gated access and no-map-marker behavior. |
| SRC-000441 | UESP, `Skyrim:Deadlands` | Deadlands worldspace access, ingredients, respawn note, and Survival Mode note. |
| SRC-000713 | UESP, `Skyrim:Interception` | Redguard Elite Armaments route, Azadi, Fijeh, Josla, Sirayar, supply chest, Sunderstone caravan, Boneshaver, and completion. |
| SRC-000999 | UESP, `Skyrim:Atronach Forge` | Forge access and recipe context retained from earlier crafting pass. |
| SRC-001417 | UESP, `Skyrim:Rielle` | Rielle access, Janus' Journal, shard chamber, Great Welkynd Stone, Norion, and crypt lockout. |
| SRC-001418 | UESP, `Skyrim:Red Scar Cavern` | Red Scar location, Mythic Dawn Temple, Vonos, and Oblivion Gate transition. |
| SRC-001419 | UESP, `Skyrim:The Consequences` | Vonos' Journal, Deadlands route, Dremora Valkynaz, Scourge, Torment, Daedric Gauntlets of Negation, and Summon Daedric Horse tome. |
| SRC-001420 | UESP, `Skyrim:Broken Fang Cave` | Broken Fang clearable state, vampire lair, The Wolf Queen v1, Mystery of Talara Part 4, and nearby Shrine of Stendarr Twin Secrets copy. |
| SRC-001421 | UESP, `Skyrim:Arcwind Point` | Drain Vitality word wall and Withershins tower copy. |
| SRC-001422 | UESP, `Skyrim:Vile Whispers` | Champion's Rest quest start, puzzle solutions, Umbra vulnerability, Umbra reward, passage key, and Treasure Hunter's Journal. |
| SRC-001423 | UESP, `Skyrim:Champion's Rest` | Umbra dungeon zones and discoverable location context. |
| SRC-001424 | UESP, `Skyrim:Purewater Run` | Purewater Run Interception state, Remnant supply chest contents, and Cherim's Heart underwater chest. |
| SRC-001425 | UESP, `Skyrim:Alchemist's Shack` | Butterfly in a Jar, carrots, Thistle pet location, and Thistle taming with carrots. |
| SRC-001426 | UESP, `Skyrim:Varlais Cavern` | Varlais access relationship to Rielle and Arcwind Point. |

## Route Placement

The section is placed after the main quest finale and level-60 Dragonborn finale because The Cause is already past its level-46 courier gate, the player has high-level combat readiness, safe owned storage, and Scholar's Insight is active for selected skill-book reads.

The pass routes more than The Cause. The nearby-objective audit identified several safe objectives whose route points overlap this late high-risk AE corridor:

- Broken Fang Cave is routed before the Two Pillars because it is near The Cause's first shrine approach and now provides two selected skill-book reads under Scholar's Insight: `The Wolf Queen, v1` and `Mystery of Talara, Part 4`.
- The Shrine of Stendarr `Twin Secrets` copy replaces the previous Serpent's Bluff selection because the route naturally visits that shrine for The Cause after Scholar's Insight.
- Alchemist's Shack is routed with the Mythic Dawn Camp approach because The Cause explicitly sends the player north of the shack. The route takes Butterfly in a Jar, uses the shack carrots to tame Thistle, and stores one Thistle Branch for the later alchemy-effect pass.
- Bones for a Crow is started before the Arcwind/Rielle trip because the quest start is available from an innkeeper and its next steps are Crowstooth's Camp and Arcwind Point, both naturally colocated with the The Cause mountain route. Guard's Dossier: Bjormund Wind-Strider is retrospectively placed in the earlier Castle Dour visit because its source location was already visited during `No News is Good News`.
- Arcwind Point is routed before Varlais/Rielle because it contains the final Drain Vitality word and the selected `Withershins` copy, and Bones for a Crow also resolves there.
- Vile Whispers/Umbra is routed before Red Scar because Champion's Rest is on the same mountain system as Red Scar Cavern and the quest is combat-ready at this route state.
- Interception is routed after The Cause/Umbra and a storage break because Redguard Elite Armaments had previously been held for a dedicated AE route. At this stage Shor's Stone, Purewater Run, Karthwasten, Ivarstead, and Sunderstone Gorge can be handled as one self-contained Creation quest path without building unrelated route work around it.

## Deferrals and Exclusions

Solitude Sewers and Green Butterfly in a Jar remain held for the Saints & Seducers `Restoring Order` path. Their source context is not The Cause, and the sewers should not be treated as a generic separate-worldspace target in this AE pass.

`Spell Tome: Conjure Ayleid Lich` remains staged for a later Atronach Forge/spell-source pass. This section acquires and preserves the Great Welkynd Stone, but the final spell route should source or verify the Ruined Book and Salt Pile inputs at the forge step rather than assuming inventory state.

Craftable or unenchanted variants in the Dragon Plate and Redguard Elite item tables remain staged for later equipment/crafting reconciliation when the route audits forge outputs and unplayable item-table variants. This pass acquires the placed unique/reward versions named in the quests.

The Ayleid Crown of Rielle is excluded as unobtainable per the item table. The Weakened Sigil Stone has no deterministic executable pickup path in the current item data or route pages and remains a `NEEDS ROUTE RESOLUTION` internal row.

## Bug-Sensitive Order Used in Guide

The player-facing guide does not include technical fallback prose. It does, however, present the safer normal route order:

- read `Janus' Journal` before approaching the Great Welkynd Stone chamber;
- make a named hard save before Rielle Crypt;
- place the shards in the documented cardinal holders;
- take the Great Welkynd Stone before fighting Norion or the coffin enemies;
- do not leave Rielle Crypt until the Rielle stone, Norion, Staff of Ehlno Ede, Rielle Key, and Vigilant Enforcer's Journal sequence is complete;
- read `Vonos' Journal` after killing Vonos, then immediately continue through the Oblivion Gate for `The Consequences`.

