# Source Note: Radiant Favor First-Visit and Nonrespawn Target Risk

Status: needs review.

Source note ID: SN-000096

## Claim

UESP identifies a class-level first-visit availability bug for some radiant miscellaneous quests, with Amren and Ysolda in Whiterun as confirmed examples. It also identifies a separate Amulet of the Moon bug where prior visits to certain nonrespawning target locations can prevent the Moon Amulet from spawning if Kharjo assigns one of those locations.

## Routing Relevance

Radiant favors are part of the objective database and can also support Hero of the People. The route needs first-visit warnings for confirmed examples and must avoid invalidating Kharjo's Amulet of the Moon target by clearing or visiting specific nonrespawning dungeons too early.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000020 | Skyrim:Miscellaneous Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Miscellaneous_Quests | 2026-05-11 | Broad radiant miscellaneous first-visit bug, with Amren and Ysolda examples. |
| SRC-000351 | Skyrim:Dungeon Delving (Bandits) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dungeon_Delving_(Bandits) | 2026-05-12 | Amren and Shahvee retrieval-favor mechanics and random bandit-hideout target selection. |
| SRC-000352 | Skyrim:Dungeon Delving (Caves) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dungeon_Delving_(Caves) | 2026-05-12 | Roggi, Queen Freydis, Runil, Noster, and Frida cave-retrieval favor mechanics. |
| SRC-000353 | Skyrim:Rare Gifts | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Rare_Gifts | 2026-05-12 | Ysolda and other rare-gift favor mechanics; only one rare-gift quest can be assigned at once. |
| SRC-000354 | Skyrim:Kill the Bandit Leader | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Kill_the_Bandit_Leader | 2026-05-12 | Annekke and Ahtar bandit-leader favor mechanics and target caveats. |
| SRC-000355 | Skyrim:Kill the Vampire | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Kill_the_Vampire | 2026-05-12 | Sybille Stentor fixed vampire target and level-10 requirement. |
| SRC-000356 | Skyrim:Amulet of the Moon | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Amulet_of_the_Moon | 2026-05-12 | Kharjo's random target list and already-visited nonrespawning location bug. |

## Evidence Summary

The Miscellaneous Quests page states that many miscellaneous quests use radiant systems and documents a confirmed bug where some radiant quests can become unavailable if not received on the first visit to the relevant location. UESP names Amren and Ysolda in Whiterun as examples.

The individual radiant pages confirm that the queued favor objectives are radiant or target-selected quests. Dungeon Delving pages cover Amren, Shahvee, Roggi, Queen Freydis, Runil, Noster, and Frida's Ring of Pure Mixtures. Rare Gifts covers Ysolda and the other rare-gift givers. Kill the Bandit Leader covers Annekke and Ahtar. Kill the Vampire is a fixed Sybille/Pinemoon Cave favor rather than a random-location radiant.

The Amulet of the Moon page adds a concrete prior-visit lock: if Kharjo sends the player to Broken Oar Grotto, Cracked Tusk Keep, or Frostmere Crypt after that location has already been visited, those nonrespawning locations can fail to spawn the Moon Amulet, forcing a reload for a different target.

## Confidence and Open Questions

Confidence is high for the Whiterun Amren/Ysolda first-visit warning and for the three Kharjo nonrespawning target locations. Confidence is lower for applying the first-visit warning to every similar favor row; TB-013 should keep the other radiant rows as class-level caution until a later bug/conflict pass confirms per-giver behavior.

## Linked Records

`data/constraints/cell-entry-locks.md`; OBJ-000221; OBJ-000223; OBJ-000226; OBJ-000234; OBJ-000237; OBJ-000242; OBJ-000247; OBJ-000252; OBJ-000256; OBJ-000265; OBJ-000320; OBJ-000327; OBJ-001992; OBJ-002006; OBJ-002046; OBJ-002393.
