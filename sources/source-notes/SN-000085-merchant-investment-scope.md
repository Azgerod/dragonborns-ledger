# Source Note: Merchant Investment Scope

Status: needs review.

Source note ID: SN-000085

## Claim

UESP's merchant tables currently identify 33 source-listed merchant rows with a checked `Invest` column. These are the merchant-investment objectives entered for TB-009E. Thirteen additional rows show investment as bugged and fixed only by the Unofficial Patch, and four AE Creation rows are marked unknown; those rows remain in `data/skills/merchant-investment-catalog.csv` as audit rows, not main-route objectives.

## Routing Relevance

The specification requires all merchant investments if available under the chosen perk path and NPC survival conditions. This note supports the merchant investment objective rows without deciding final Speech perk timing, travel order, NPC safety, or whether any investment should be combined with thane, training, shopping, or regional sweep work.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000286 | Skyrim:Speech | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Speech | 2026-05-12 | Investor perk requirement and Speech perk context. |
| SRC-000296 | Skyrim:Merchants | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Merchants | 2026-05-12 | Merchant table `Invest` column, merchant gold mechanics, bug notes, and merchant location rows. |

## Evidence Summary

The Speech page lists Investor as a Speech perk requiring Speech 70 and the Merchant perk. The Merchants page states that the Investor perk lets the player invest 500 gold in certain merchants, permanently increasing that merchant's available gold by 500. It also states that the merchant table's checked `Invest` entries identify working investments, while some merchants with bugged investment dialogue are not checked.

TB-009E records these investment buckets:

| Bucket | Rows | Route treatment |
| --- | ---: | --- |
| Source-listed available investments | 33 | Main-route objective rows. |
| Bugged, Unofficial Patch-only investments | 13 | Excluded audit rows in the support table. |
| Unknown AE Creation investment status | 4 | Validation-later audit rows in the support table. |

Available investment rows by source content:

| Source content | Available rows |
| --- | ---: |
| base_game | 31 |
| dawnguard | 1 |
| dragonborn | 1 |
| **Total** | **33** |

The four unknown AE Creation rows are Ashfall's Tear merchants from Ghosts of the Tribunal. They are not entered as main-route investment objectives until later validation confirms that official PS4 AE gameplay exposes working investment behavior.

## Confidence and Open Questions

Confidence is high for the checked UESP investment rows and for excluding Unofficial Patch-only bug fixes from the main route. Confidence is lower for final route readiness because NPC survival, replacement merchant behavior, marriage/removal of investment dialogue, spouse-store behavior, and PS4 AE behavior still need downstream validation.

Open questions for later work:

* exact Speech training/perk timing for Investor and Master Trader;
* NPC dependency and survival ordering for every investable merchant;
* whether shared-store rows, such as Warmaiden's, require one or more route interactions in current PS4 AE behavior;
* whether any Ashfall's Tear AE merchants have working investment behavior;
* whether investment should be paired with thane favor counting, shopping, training, or regional sweep work.

## Linked Records

`data/objectives/objectives.csv` rows `OBJ-002717` through `OBJ-002750`; `data/skills/merchant-investment-catalog.csv`; `docs/task-board.md`.
