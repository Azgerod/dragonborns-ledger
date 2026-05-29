# SN-000212 - Black Star Ilinalta Route

Status: researched.

Source note ID: SN-000212

## Claim

`The Black Star` can be completed after the Shrine of Azura and Nelacar leads by clearing Ilinalta's Deep and Ilinalta's Deluge while the quest points there, taking the Broken Azura's Star and Malyn Varen's Grimoire from the final room, then using a hard save to branch Azura's Star/Aranea before reloading and keeping The Black Star through Nelacar. `A Scrawled Note` remains a random post-quest necromancer encounter item rather than a deterministic route stop.

## Routing Relevance

The guide already starts the quest in the Winterhold/College section, but it previously left the Ilinalta completion, reward fork, artifact preservation, and Malyn Varen's Grimoire unresolved. The source-backed route also repairs an earlier Falkreath clear cue: Ilinalta's Deluge is blocked by the quest boulder until `The Black Star` has pointed there, so the full clear belongs with the active quest, not the first warm Falkreath sweep.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001522 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Black_Star | 2026-05-28 | Quest start, Ilinalta objective, final reward fork, Azura's Star Interior sequence, bugs, and postquest necromancer note. |
| SRC-001523 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Black_Star_(item) | 2026-05-28 | The Black Star artifact identity, reusable black soul gem function, and Nelacar reward route. |
| SRC-001524 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Azura%27s_Star | 2026-05-28 | Azura's Star reward route, Aranea follower outcome, and alternative to The Black Star. |
| SRC-001525 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ilinalta%27s_Deep | 2026-05-28 | Ilinalta's Deep/Deluge zones, quest-gated boulder, final-room contents, clearable-location context, and bug notes. |
| SRC-001526 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Azura%27s_Star_Interior | 2026-05-28 | One-way Star interior, no follower access, Malyn/Dremora fight, and loot-before-kill warning. |
| SRC-001527 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Malyn_Varen%27s_Grimoire | 2026-05-28 | Malyn Varen's Grimoire location in Ilinalta's Deluge by the exit. |
| SRC-001528 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:A_Scrawled_Note | 2026-05-28 | Postquest necromancer-carried note after Malyn is slain. |

## Evidence Summary

UESP's quest walkthrough sends the player from the Shrine of Azura to Nelacar, then to Ilinalta's Deep for the Broken Azura's Star, then to either Aranea/Azura or Nelacar for the final cleansing route. The artifact choice is mutually exclusive on the continuing save: returning to Aranea produces Azura's Star and Aranea follower access, while returning to Nelacar produces The Black Star. The guide therefore branches Azura's Star first from `HS-DAEDRIC-BLACK-STAR`, reloads, and keeps The Black Star on the main route.

UESP's Ilinalta's Deep page records that Ilinalta's Deluge is blocked by a boulder if `The Black Star` has not started, and that the final room contains Malyn Varen's skeleton, the star, Malyn Varen's Grimoire, a chest, and the ladder exit. It also records boulder and trapdoor bugs. The route leaves Ilinalta out of the early Falkreath full-clear loop, returns once the quest points there, and uses exit/re-enter or leave/return-from-nearby support handling if the quest boulder or exterior trapdoor misbehaves.

UESP's Azura's Star Interior page records that followers cannot accompany the player, that the worldspace cannot be revisited after Malyn is defeated, and that three Dremora plus Malyn are fought inside. The route tells the player to loot desired Dremora items before killing Malyn in each branch.

UESP records `A Scrawled Note` as carried by one of two necromancers that may attack after the quest. Because the source does not provide a deterministic route trigger or safe wait-loop, the guide only tells the player to take and read the note if the encounter happens naturally and keeps the row unresolved for a later random-encounter policy.

## Route Decision

Insert a new `The Black Star And Ilinalta's Deep` section after Winterhold/College support and before the return to Dawnstar. Repair the early Falkreath loop so it does not claim Ilinalta's Deep as fully cleared before the quest. Close `OBJ-000165`, `OBJ-001612`, `OBJ-001613`, `OBJ-001212`, `OBJ-002076`, `CHK-QUESTS-0163`, `CHK-UNIQUE-GEAR-1561`, `CHK-UNIQUE-GEAR-1562`, `CHK-BOOKS-2007`, `CHK-LOCATIONS-1108`, and the Oblivion Walker counter after the Oghma checkpoint. Keep `OBJ-001258` unresolved as random postquest encounter policy.

## Confidence and Open Questions

Confidence is high for the quest, artifact-branch, grimoire, and Ilinalta clear route. The remaining open question is how the final guide should handle random postquest hunter/assassin-style book drops such as `A Scrawled Note` without encouraging wait-looping or RNG manipulation.

## Linked Records

`OBJ-000165`; `OBJ-000181`; `OBJ-001212`; `OBJ-001258`; `OBJ-001612`; `OBJ-001613`; `OBJ-002076`; `CHK-QUESTS-0163`; `CHK-UNIQUE-GEAR-1561`; `CHK-UNIQUE-GEAR-1562`; `CHK-BOOKS-2007`; `CHK-LOCATIONS-1108`; `HS-DAEDRIC-BLACK-STAR`; `drafts/final-guide/main-guide-v1.md`; `data/guide-coverage/main-guide-v1-coverage.csv`.
