# Source Note: Dawnguard Trophy Caveats

Status: needs review.

Source note ID: SN-000028

## Claim

Several Dawnguard objectives are directly trophy-relevant. The objective database marks the quest rows linked to `Awakening`, `Beyond Death`, `Kindred Judgement`, `Lost to the Ages`, and `A New You`. It also preserves the later need to route Auriel's Bow handling carefully because the achievement source warns that the bow can be lost after the Dawnguard main questline.

## Routing Relevance

Dawnguard quest ordering must preserve PS4 trophy eligibility and avoid losing trophy-critical objects before their trophy action is complete. This note only flags trophy relevance; platform-specific PS4 validation and exact warning placement belong in the later trophy and warning-layer passes.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000002 | Skyrim:Achievements | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Achievements | 2026-05-11 | Lists Dawnguard achievements and the Auriel's Bow missability caveat. |
| SRC-000024 | Skyrim:Dawnguard Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dawnguard_Quests | 2026-05-11 | Marks achievement-linked Dawnguard quest rows. |

## Evidence Summary

UESP's achievements page lists Dawnguard achievements for completing `Awakening`, completing `Beyond Death`, completing `Kindred Judgment`, completing `Lost to the Ages`, changing the character's face, learning all three words of Soul Tear, using Auriel's Bow's special power, mastering the Werewolf perk tree, mastering the Vampire Lord perk tree, and defeating a Legendary Dragon.

The same page notes that Auriel's Bow is no longer a quest item after `Kindred Judgment`, so the `Auriel's Bow` trophy can be missed if the item is lost or allowed to despawn before using its special power. This pass does not create the later item/power/trophy rows yet, but the caveat is retained for downstream trophy and warning-layer work.

## Confidence and Open Questions

Confidence is high for UESP achievement mapping. Later passes must validate PS4 behavior, decide whether to create separate trophy-objective rows for Soul Tear and Auriel's Bow, and place the exact route warnings.

## Linked Records

OBJ-000352, OBJ-000361, OBJ-000364, OBJ-000385, and OBJ-000389. Future trophy, power, and unique-item rows should also reference this note when created.
