# SN-000211 - Whispering Door and Ebony Blade Route

Status: researched.

Source note ID: SN-000211

## Claim

`The Whispering Door` can be completed on the main route after level 20 and `Dragon Rising` by getting Hulda's Whiterun rumor, speaking to Balgruuf and Nelkir, listening at the Old Wooden Door in Dragonsreach, acquiring the Whispering Door Key from Balgruuf or Farengar, and retrieving the Ebony Blade. The route should take `Admonition Against Ebony` from the same room, preserve the Ebony Blade, and not power the blade by killing friendly NPCs because powering it is not required for quest completion or Oblivion Walker.

## Routing Relevance

The quest was previously held for a level-20 Whiterun/Balgruuf window. The post-Peryite support stop is already beyond `Dragon Rising`, preserves Hulda/Balgruuf/Farengar/Nelkir, and occurs before any Civil War state that could move Balgruuf. It is therefore a safe deterministic insertion point for the quest and the artifact, with a hard save before rumor/key handling.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001519 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Whispering_Door | 2026-05-28 | Level 20 and Dragon Rising prerequisites, Hulda rumor start, Balgruuf/Nelkir/door sequence, key source, Ebony Blade completion, and start bugs. |
| SRC-001520 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ebony_Blade | 2026-05-28 | Ebony Blade artifact identity, friend-kill powering mechanics, no need to power for Oblivion Walker, and storage/confiscation caveats. |
| SRC-001521 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Admonition_Against_Ebony | 2026-05-28 | `Admonition Against Ebony` location in the Dragonsreach basement room tied to The Whispering Door. |

## Evidence Summary

UESP lists `The Whispering Door` as requiring level 20, `Dragon Rising`, and the Whispering Door Key. The walkthrough starts from The Bannered Mare rumor, then sends the player through Balgruuf, Nelkir, the basement Old Wooden Door, Nelkir's key clue, and the locked room where `Admonition Against Ebony` and the Ebony Blade are on the table.

The same source records that the key can be obtained from Balgruuf or Farengar. The route uses a hidden pickpocket from Farengar rather than killing Farengar or creating Whiterun violence.

UESP's Ebony Blade page states that powering the blade requires killing friendly NPCs, but also states that powering it is not needed for the Oblivion Walker achievement. That supports preserving the artifact without routing friend kills. The page also records storage caveats: the blade can fall from weapon racks, and confiscation before ten friend kills can reset it. The route therefore stores it in a normal owned container and avoids crime/confiscation handling while carrying it.

UESP records start bugs around Hulda's rumor path. The route keeps Hulda alive, hard-saves before asking for rumors, asks again if an older rumor is given first, and does not rely on the no-console fallback.

## Route Decision

Insert a Whiterun Mephala interlude after the Peryite/Reach support stop and before the Windhelm route. Complete `The Whispering Door`, take and read `Admonition Against Ebony`, acquire the Ebony Blade, record Oblivion Walker progress, and store the artifact in a normal owned container. Close the previous route-resolution rows for `OBJ-000172`, `OBJ-001084`, and `OBJ-001563`.

## Confidence and Open Questions

Confidence is high for the main quest route and artifact acquisition. The only residual risk is the source-listed Hulda rumor bug; the guide mitigates it with a hard save and repeated rumor dialogue, but PS4 has no console fallback.

## Linked Records

`OBJ-000172`; `OBJ-001084`; `OBJ-001563`; `drafts/final-guide/main-guide-v1.md`; `data/guide-coverage/main-guide-v1-coverage.csv`; `data/guide-coverage/main-guide-v1-order-delayed-task-repair.csv`.
