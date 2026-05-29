# Swims Radiant Work Route

Status: researched.

Source note ID: SN-000238

## Claim

After `Fishing Legend`, the guide should treat Swims-In-Deep-Water's miscellaneous work as a small conditional radiant-work loop rather than as a reload target. The route should accept and complete assignments as they appear until it has recorded one representative `Further Study`, one `Rubbish Retrieval`, and one `Stocking Up` completion or parked turn-in.

For this pass:

- `Rubbish Retrieval` is handled when Swims gives `Bounty: Cleaning Our Waterways`.
- The player reads the bounty note immediately.
- If the assigned town is Riften, use the Riften canal Fishing Supplies beside the walkway toward Marise Aravel's house.
- If the assigned town is Markarth, use the Markarth stream Fishing Supplies below the waterfall by The Warrens, naturally matching the later Markarth Fishing route.
- If the assignment is Dawnstar or Morthal despite the source-recorded bug that makes those towns unlikely, use the active marker and the local Fishing Supplies rather than reloading for a different town.
- Use a standard Fishing Rod for the rubbish catch because the quest page says it works better.
- Fish until the objective count completes, then collect the bounty from the active Jarl or steward marker.

`Stocking Up` is handled when Swims gives one of the four supply notes:

- `Bounty: Supply of Arctic Grayling`.
- `Bounty: Supply of Brook Bass`.
- `Bounty: Supply of Catfish`.
- `Bounty: Supply of Salmon`.

Read whichever note is assigned, obtain the quest journal's requested count of that fish, then give the fish to the active innkeeper marker. Use already routed or nearby source-backed fishing controls: Dawnstar freezing water for Arctic Grayling, Riften canal or Lake Honrich temperate water for Brook Bass and Salmon, and Lucky Fishing Hat rain at Lake Honrich or another temperate lake for Catfish. If the innkeeper marker is in mainland Skyrim, complete the turn-in as a direct route chore; if it is on Solstheim, store the fish and finish the turn-in at the matching Solstheim visit.

Do not reload to force a different Swims assignment, town, fish, or innkeeper. If a parked Solstheim `Further Study` target prevents Swims from issuing more work, finish the remaining representative Swims work after the Solstheim turn-in at the next Riften return.

## Routing Relevance

This closes `OBJ-000604` Rubbish Retrieval and checklist row `CHK-QUESTS-0628`.

It closes `OBJ-000606` Stocking Up as the representative Swims supply radiant. Because `Stocking Up` can choose one of four supply notes, this also accounts for the four possible document rows without requiring duplicate-note collection:

- `Bounty: Supply of Arctic Grayling`.
- `Bounty: Supply of Brook Bass`.
- `Bounty: Supply of Catfish`.
- `Bounty: Supply of Salmon`.

The route also closes the remaining Brook Bass catch row by giving it a source-backed temperate-water catch route inside the same conditional Stocking Up handling.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001765 | Skyrim:Rubbish Retrieval | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Rubbish_Retrieval | 2026-05-29 | Used for Swims-In-Deep-Water giver, assigned city set, standard-rod guidance, four-rubbish objective, steward/Jarl turn-in, 325 gold reward, and Dawnstar/Morthal assignment bug. |
| SRC-001766 | Skyrim:Bounty: Cleaning Our Waterways | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bounty:_Cleaning_Our_Waterways | 2026-05-29 | Used for Rubbish Retrieval bounty-note identity, Swims-In-Deep-Water work source, note status, and trash-count wording. |
| SRC-001767 | Skyrim:Stocking Up | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Stocking_Up | 2026-05-29 | Used for Swims-In-Deep-Water giver, repetitive radiant status, four possible supply fish, random innkeeper target, Solstheim possibility, completion boundary, and innkeeper-death fail stage. |
| SRC-001768 | Skyrim:Bounty: Supply of Arctic Grayling | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bounty:_Supply_of_Arctic_Grayling | 2026-05-29 | Used for Stocking Up bounty-note identity, Swims-In-Deep-Water source, note status, and requested Arctic Grayling supply. |
| SRC-001769 | Skyrim:Bounty: Supply of Brook Bass | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bounty:_Supply_of_Brook_Bass | 2026-05-29 | Used for Stocking Up bounty-note identity, Swims-In-Deep-Water source, note status, and requested Brook Bass supply. |
| SRC-001770 | Skyrim:Bounty: Supply of Catfish | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bounty:_Supply_of_Catfish | 2026-05-29 | Used for Stocking Up bounty-note identity, Swims-In-Deep-Water source, note status, and requested Catfish supply. |
| SRC-001771 | Skyrim:Bounty: Supply of Salmon | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bounty:_Supply_of_Salmon | 2026-05-29 | Used for Stocking Up bounty-note identity, Swims-In-Deep-Water source, note status, and requested Salmon supply. |
| SRC-001692 | Skyrim:Fishing (activity) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fishing_(activity) | 2026-05-29 | Used for Fishing Supplies mechanics, quest-item catch support, junk mechanics, local Riften/Markarth/Morthal/Dawnstar supplies, and Brook Bass/Catfish/Salmon/Arctic Grayling catch conditions. |

## Evidence Summary

UESP's `Rubbish Retrieval` page identifies Swims-In-Deep-Water as the giver, lists Dawnstar, Markarth, Morthal, and Riften as possible locations, and describes fishing up rubbish at the assigned city's Fishing Supplies. The quick walkthrough says to keep fishing until all four items are obtained. Quest stages then send the player to collect the bounty from either the Jarl's steward or the Jarl, and the header lists a 325 gold reward. The page also records a bug: because of how the fishing supply objects were set up, Dawnstar or Morthal assignments are unlikely. The guide therefore treats those towns as possible active-marker branches rather than target outcomes to force.

UESP's `Bounty: Cleaning Our Waterways` page identifies the document as a Fishing Creation note for `Rubbish Retrieval`, value and weight 0, given by Swims-In-Deep-Water when asking for work. The note text uses the same global objective count and assigned-town alias as the quest stages.

UESP's `Stocking Up` page identifies Swims-In-Deep-Water as the giver, says this is a repetitive quest, and says Swims asks the player to supply certain fish to randomly chosen innkeepers, with Solstheim possible. The quest stages show four possible supply notes and four possible requested fish: Brook Bass, Salmon, Catfish, and Arctic Grayling. Completion is recorded after supplying the innkeeper; a fail stage exists if the innkeeper dies.

The four Stocking Up bounty-note pages each identify the document as a Fishing Creation note for `Stocking Up`, value and weight 0, given by Swims-In-Deep-Water when asking for work, and name the requested fish for that note.

UESP's Fishing activity page supports the fishing controls used in the guide. It says fishing requires a Fishing Rod and Fishing Supplies, active quests can provide a 50% chance to catch the quest item at the relevant spot, and fishing outcomes depend on biome, weather, rod, population, and time. Its location table places Fishing Supplies in the Riften canal, Markarth stream below The Warrens, Dawnstar, and Morthal. Its biome tables support Brook Bass in temperate lakes or streams, Catfish in rainy temperate lakes, Salmon in temperate lakes or streams, and Arctic Grayling in freezing waters.

## Confidence and Open Questions

Confidence is high for the Rubbish Retrieval giver, possible towns, note source, standard-rod guidance, four-rubbish completion target, active Jarl/steward turn-in, reward, and Dawnstar/Morthal assignment bug.

Confidence is high for Stocking Up's giver, repeated radiant structure, four possible supply notes, possible Solstheim innkeeper target, completion boundary, and innkeeper-death fail state.

Confidence is medium for the exact numeric fish count in `Stocking Up` because UESP exposes the count as a quest global rather than a rendered number. The guide handles that by instructing the player to use the active journal count while giving source-backed catch controls for each possible fish.

## Linked Records

OBJ-000604; OBJ-000606; OBJ-001358; OBJ-001368; OBJ-001369; OBJ-001370; OBJ-001371; OBJ-001899; CHK-QUESTS-0628; BOOKLOC-001601; BOOKLOC-001611; BOOKLOC-001612; BOOKLOC-001613; BOOKLOC-001614; ITEM-000567; `drafts/final-guide/main-guide-v1.md`; `data/objectives/objectives.csv`; `data/books/book-document-locations.csv`; `data/checklist-mapping/coverage-matrix.csv`; `data/items/ae-item-members.csv`; `data/guide-coverage/main-guide-v1-coverage.csv`.
