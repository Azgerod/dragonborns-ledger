# Source Note: Bards College Ordering and Bug Risks

Status: needs review.

Source note ID: SN-000018

## Claim

UESP records several Bards College ordering and bug risks that can affect a no-console PS4 route: the introductory investigation objective can become incompletable if started too late, instrument quests can mis-handle early pickup or quest-item removal, `Tending the Flames` can be blocked by other quest states, and `Rjorn's Drum` has a Special Edition Halldir failure risk.

## Routing Relevance

The route should avoid leaving permanent miscellaneous objectives or stuck quest items where possible, and PS4 players cannot use console fixes. These risks justify later ordering warnings and hard-save or delay decisions during the bug-risk and route-skeleton passes.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000013 | Skyrim:Bards College | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bards_College | 2026-05-11 | Summarizes instrument quest-item removal bug and investigation objective bug. |
| SRC-000014 | Skyrim:Investigate the Bards College | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Investigate_the_Bards_College | 2026-05-11 | Notes incompletion risks from starting after joining or after early King Olaf's Verse pickup. |
| SRC-000015 | Skyrim:Tending the Flames | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Tending_the_Flames | 2026-05-11 | Notes `Bound Until Death`, `Season Unending`, verse-choice, and festival/Viarmo bug risks. |
| SRC-000016 | Skyrim:Finn's Lute | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Finn%27s_Lute | 2026-05-11 | Notes early-pickup and quest-item persistence risks. |
| SRC-000017 | Skyrim:Pantea's Flute | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Pantea%27s_Flute | 2026-05-11 | Notes early-pickup, marker, turn-in, and quest-item persistence risks. |
| SRC-000018 | Skyrim:Rjorn's Drum | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Rjorn%27s_Drum | 2026-05-11 | Notes early-pickup, NPC-death, quest-item persistence, and Special Edition Halldir risks. |

## Evidence Summary

UESP notes that `Investigate the Bards College` can become stuck if it is started after joining the Bards College or after obtaining King Olaf's Verse early. For `Tending the Flames`, UESP notes that `Bound Until Death` must be completed before the last step if it is active, and that `Season Unending` can remove Elisif from the Blue Palace until that quest state is resolved. It also records multiple bug risks around King Olaf's Verse, Viarmo's performance, the festival, and a verse choice that can prevent the highest gold reward.

For the instrument quests, UESP records quest-item persistence and early-pickup problems for Finn's Lute, Pantea's Flute, and Rjorn's Drum. UESP also notes that in Special Edition, Halldir can sometimes disappear instead of splitting into clones during `Rjorn's Drum`, leaving the player locked in the room with no staff and no exit.

## Confidence and Open Questions

Confidence is moderate to high for the existence of these risks. Exact PS4 behavior, Anniversary Edition patch state, safest order, and whether to recommend avoiding pre-quest instrument pickup require later bug-risk validation.

## Linked Records

OBJ-000182 through OBJ-000186.
