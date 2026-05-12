# Source Note: Dawnguard Finite Collectible Sets

Status: needs review.

Source note ID: SN-000062

## Claim

UESP identifies Dawnguard finite collectible sets that need objective-database coverage before route placement: Jiub's Opus pages, Aetherium Shards, Paragons, and Reaper Gem Fragments.

## Routing Relevance

The specification requires finite collectible sets, Dawnguard finite side content, trophy preservation, unique reward handling, and explicit later route instructions for collectible cleanup. This pass records Dawnguard collectible-set coverage without deciding exact route order, bug mitigations, cell-entry timing, or branch treatment.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000230 | Skyrim:Impatience of a Saint | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Impatience_of_a_Saint | 2026-05-12 | Jiub's Opus page collection and page-location table. |
| SRC-000231 | Skyrim:Lost to the Ages | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Lost_to_the_Ages | 2026-05-12 | Four Aetherium Shards and Lost to the Ages quest structure. |
| SRC-000232 | Skyrim:Amethyst Paragon | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Amethyst_Paragon | 2026-05-12 | Amethyst Paragon location and platform use. |
| SRC-000233 | Skyrim:Diamond Paragon | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Diamond_Paragon | 2026-05-12 | Diamond Paragon location and platform use. |
| SRC-000234 | Skyrim:Emerald Paragon | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Emerald_Paragon | 2026-05-12 | Emerald Paragon location and platform use. |
| SRC-000235 | Skyrim:Ruby Paragon | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Ruby_Paragon | 2026-05-12 | Ruby Paragon location and platform use. |
| SRC-000236 | Skyrim:Sapphire Paragon | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Sapphire_Paragon | 2026-05-12 | Sapphire Paragon location and platform use. |
| SRC-000237 | Skyrim:Reaper's Lair | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Reaper%27s_Lair | 2026-05-12 | Reaper Gem Fragment receptacle use and Reaper encounter context. |
| SRC-000238 | Skyrim:Soul Cairn | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Soul_Cairn | 2026-05-12 | Soul Cairn Reaper Gem Fragment and Jiub-page location context. |
| SRC-000227 | Skyrim:Quest Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Quest_Items | 2026-05-12 | Reaper Gem Fragment quest-item entry. |

## Evidence Summary

The `Impatience of a Saint` page lists 10 Jiub's Opus pages. The individual page title rows already exist from the book/document pass, so this pass adds only a collectible-set parent row that points later routing and checklist work back to those member rows.

The `Lost to the Ages` page requires four Aetherium Shards and identifies the shard sources at Arkngthamz, Deep Folk Crossing, Raldbthar, and the Dwarven Storeroom near Mzulft. This pass adds one parent row plus four member rows.

The Paragon pages identify five Paragons in the Forgotten Vale and their use with the Paragon Platform. This pass adds one parent row plus five member rows.

`Reaper's Lair`, `Soul Cairn`, and `Quest Items` support a three-fragment Reaper Gem Fragment set used at the Reaper Shard Receptacle. This pass adds one parent row plus three fragment rows; exact Soul Cairn micro-routing remains deferred.

## Confidence and Open Questions

Confidence is high for the source-list collectible membership. Exact route placement, Soul Cairn traversal order, Forgotten Vale one-way/access implications, bug risk, and final checklist cue placement remain open.

Jiub's Opus members are not duplicated here because title-level rows already exist in `data/objectives/objectives.csv`; this source note adds only the set-completion parent.

## Linked Records

OBJ-001836 through OBJ-001851.
