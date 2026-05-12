# Source Note: AE Creation Hard and Prerequisite-Gated Starts

Status: needs review.

Source note ID: SN-000091

## Claim

Several AE Creation package starts have hard numeric level gates or prerequisite quest gates that must block route placement until satisfied: Plague of the Dead at level 5, Hendraheim at level 10, Bloodchill Manor at level 12, Alternative Armors - Ebony Plate at level 32, The Cause at level 46, and Bone Wolf after completing The Wolf Queen Awakened.

## Routing Relevance

These gates affect the route skeleton directly. A courier-delivered start cannot be treated as available before its level or prerequisite, and a high-gated Creation such as The Cause should anchor late AE placement rather than be inserted during an early regional pass.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000099 | Skyrim:Plague of the Dead | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Plague_of_the_Dead | 2026-05-12 | Plague of the Dead level-5 courier start. |
| SRC-000319 | Skyrim:Hendraheim (quest) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Hendraheim_(quest) | 2026-05-12 | Hendraheim required level and courier start. |
| SRC-000320 | Skyrim:Warrior's Challenge | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Warrior%27s_Challenge | 2026-05-12 | Hendraheim level-10 courier note cross-check. |
| SRC-000321 | Skyrim:Dinner Invitation | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dinner_Invitation | 2026-05-12 | Bloodchill Manor level-12 courier invitation. |
| SRC-000322 | Skyrim:Heart of Crimson | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Heart_of_Crimson | 2026-05-12 | Ebony Plate required level and courier start. |
| SRC-000323 | Skyrim:The Cause (quest) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Cause_(quest) | 2026-05-12 | The Cause required level and courier start. |
| SRC-000324 | Skyrim:Let Sleeping Wolves Lie | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Let_Sleeping_Wolves_Lie | 2026-05-12 | Bone Wolf prerequisite quest and courier start. |

## Evidence Summary

UESP's Plague of the Dead page states that the Rising Dead quest begins from an Anonymous Letter delivered by courier once the player reaches level 5. The Hendraheim quest and Warrior's Challenge pages identify a level-10 courier delivery. Dinner Invitation is delivered by courier at level 12 and starts Bloodchill Manor's Guests for Dinner path. Heart of Crimson has required level 32 and starts from Letter from Tyra Blood-Fire. The Cause quest has required level 46 and starts from Stranger's Plea. Let Sleeping Wolves Lie starts from Letter from Bolgeir Bearclaw after The Wolf Queen Awakened is complete.

## Confidence and Open Questions

Confidence is high for the listed hard and prerequisite gates. These gates should be treated as availability constraints, not as recommendations that the player can ignore in a normal PS4 route. Bug behavior for missing couriers, alternate location triggers, and quest-stage failures belongs in TB-017; quest conflicts and branch implications belong in TB-014.

## Linked Records

`data/constraints/ae-creation-start-triggers.md`; OBJ-000484; OBJ-000499; OBJ-000520; OBJ-000525; OBJ-000536; OBJ-000551; OBJ-000575; OBJ-000576; OBJ-000632; OBJ-000655; OBJ-000659; OBJ-000664; OBJ-000671; OBJ-000719; OBJ-000750.
