# SN-000214 - Repairing The Phial Route

Status: researched.

Source note ID: SN-000214

## Claim

`Repairing the Phial` can be closed in the main-quest Blackreach section after `The Throat of the World` opens the summit. The route reads `Letter from Quintus Navale`, starts the repair with Quintus in Windhelm, collects Unmelting Snow from the Throat of the World, Mammoth Tusk Powder from Stonehill Bluff, and one fresh Briar Heart from a post-start Forsworn Briarheart source, then returns to Quintus to receive and preserve the restored White Phial.

## Routing Relevance

TB-038R carried `Repairing the Phial`, `Letter from Quintus Navale`, The White Phial artifact, and the related quest/unique-gear checklist rows as unresolved. The earlier Windhelm section correctly held the sequel because UESP requires both the first `The White Phial` quest and full access to the Throat of the World. The current route has that prerequisite in MR-043, so the repair belongs immediately after the summit visit and before the Blackreach dive.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001533 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Repairing_the_Phial | 2026-05-28 | Quest prerequisite, courier letter, Quintus start, three repair materials, reward choice, refill behavior, and bug warnings. |
| SRC-001534 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_White_Phial_(item) | 2026-05-28 | Artifact identity, post-repair reward state, effect choices, refill behavior, unchangeable effect, and item bugs. |
| SRC-001535 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_White_Phial_(quest) | 2026-05-28 | First quest completion boundary, sequel prerequisite, and first-Windhelm-entry/Nurelion bug context. |

## Evidence Summary

UESP states that `Repairing the Phial` can start only after the first `The White Phial` quest and after the player gains full access to the Throat of the World during the same-named main quest. A courier delivers `Letter from Quintus Navale` a few days after the failed first repair once the summit prerequisite is available.

Quintus requires three materials: Unmelting Snow from the Throat of the World, Mammoth Tusk Powder from Stonehill Bluff, and a Briar Heart from a Forsworn Briarheart. UESP distinguishes the quest's Mammoth Tusk Powder from ordinary Powdered Mammoth Tusk and notes that one Briarheart source is marked on the map.

UESP records several route-relevant bugs: the courier can fail to deliver or loiter at Sarethi Farm; carrying repair materials, especially Briar Hearts, before starting the quest can block objective updates; storing/dropping Mammoth Tusk Powder can block turn-in dialogue; and finishing with extra Briar Hearts can leave remaining hearts quest-locked. The guide therefore tells the player not to carry pre-existing Briar Hearts when starting the quest, to collect exactly one post-start Briar Heart, and not to store or use the three repair materials before turn-in.

The restored White Phial is a reusable potion reward. UESP says the chosen effect cannot be changed, the full phial becomes an empty misc item when used, and it refills after 24 hours. The guide chooses the Restore Health option as the default, then preserves the item instead of using it during the route because UESP records disappearance and empty-phial duplication bugs.

## Route Decision

Insert the repair after the Paarthurnax summit dialogue in `Blades Research, Blackreach, and The Fallen`. The route already has Throat of the World access, has previously completed the first White Phial quest, and soon passes Sarethi Farm, which gives a documented fallback check if the courier stalls there. Close `OBJ-000203`, `OBJ-001197`, `OBJ-001614`, `CHK-QUESTS-0224`, and `CHK-UNIQUE-GEAR-1698` in coverage and TB-038R repair data.

## Confidence and Open Questions

Confidence is high for normal courier delivery and ingredient collection. Residual risk remains for rare courier or quest-objective bugs on PS4; the route mitigates those with a pre-Quintus save, no pre-start Briar Hearts in inventory, exact post-start material collection, no storage/drop of repair materials, and a Sarethi Farm courier check.

## Linked Records

`OBJ-000203`; `OBJ-001197`; `OBJ-001614`; `CHK-QUESTS-0224`; `CHK-UNIQUE-GEAR-1698`; `drafts/final-guide/main-guide-v1.md`; `data/guide-coverage/main-guide-v1-coverage.csv`; `data/guide-coverage/main-guide-v1-order-delayed-task-repair.csv`.
