# Source Note: Dragonborn Finite Collectible Sets

Status: needs review.

Source note ID: SN-000063

## Claim

UESP identifies Dragonborn finite collectible sets that need objective-database coverage before route placement: East Empire Company Pendants, Kagrumez Resonance Gems, and the Black Book collection.

## Routing Relevance

The specification requires Dragonborn finite side content, all finite collectible sets, permanent Black Book powers, unique rewards, and explicit checklist synchronization. This pass records Dragonborn collectible-set coverage without deciding Solstheim route order, safe access timing, reward choice defaults, or checklist mapping.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000239 | Skyrim:Pain in the Necklace | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Pain_in_the_Necklace | 2026-05-12 | East Empire Company Pendant quest and strongbox location table. |
| SRC-000240 | Skyrim:The Kagrumez Gauntlet | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Kagrumez_Gauntlet | 2026-05-12 | Kagrumez Resonance Gem count, sources, and reward trials. |
| SRC-000200 | Skyrim:Black Book: Waking Dreams (book) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Black_Book:_Waking_Dreams_(book) | 2026-05-11 | Existing Black Book title/source row support from TB-007B4a. |
| SRC-000201 | Skyrim:Black Book: Epistolary Acumen (book) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Black_Book:_Epistolary_Acumen_(book) | 2026-05-11 | Existing Black Book title/source row support from TB-007B4a. |
| SRC-000202 | Skyrim:Black Book: Untold Legends (book) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Black_Book:_Untold_Legends_(book) | 2026-05-11 | Existing Black Book title/source row support from TB-007B4a. |
| SRC-000203 | Skyrim:Black Book: The Winds of Change (book) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Black_Book:_The_Winds_of_Change_(book) | 2026-05-11 | Existing Black Book title/source row support from TB-007B4a. |
| SRC-000204 | Skyrim:Black Book: The Sallow Regent (book) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Black_Book:_The_Sallow_Regent_(book) | 2026-05-11 | Existing Black Book title/source row support from TB-007B4a. |
| SRC-000205 | Skyrim:Black Book: Filament and Filigree (book) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Black_Book:_Filament_and_Filigree_(book) | 2026-05-11 | Existing Black Book title/source row support from TB-007B4a. |
| SRC-000206 | Skyrim:Black Book: The Hidden Twilight (book) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Black_Book:_The_Hidden_Twilight_(book) | 2026-05-11 | Existing Black Book title/source row support from TB-007B4a. |

## Evidence Summary

`Pain in the Necklace` lists East Empire Company strongbox locations for pendant collection. This pass adds one collection parent row plus 33 source-listed pendant strongbox rows.

`The Kagrumez Gauntlet` identifies five Kagrumez Resonance Gems, four of which are needed for the full trial sequence. This pass adds one parent row plus five member rows because the fifth gem can matter for completionist collection even though the quest only requires four.

Black Book title rows already exist from the book/document pass and Black Book power-choice rows already exist from the spell/power pass. This pass adds one collectible-set parent row so the seven-book collection remains visible to collectible and checklist QA without duplicating the seven existing title rows.

## Confidence and Open Questions

Confidence is high for East Empire Company Pendant and Kagrumez Resonance Gem source-list membership. Exact route timing, Raven Rock ownership/lock handling, Solstheim weather/travel sequencing, bug handling, Black Book default reward recommendations, and checklist mapping remain deferred.

## Linked Records

OBJ-001852 through OBJ-001892.
