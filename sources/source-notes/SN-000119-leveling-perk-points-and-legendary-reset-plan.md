# Source Note: Leveling, Perk Points, and Legendary Reset Plan

Status: needs review.

Source note ID: SN-000119

## Claim

The all-perks requirement is a level-and-reset constraint, not a normal-play side effect. The route must finish with all 18 skills at 100, all 251 skill perk ranks allocated, and enough character levels gained through skill increases to supply those perk points. Legendary skill resets are therefore required, but they must be bounded, staged, and recovered to final skill-100 state rather than used as an open-ended grind.

## Routing Relevance

This note supports TB-020 progression planning and later TB-027 route integration. It does not choose exact grind locations, spell loops, perk order, or final build defaults.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000268 | Skyrim:Skills | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Skills | 2026-05-12 | Skill list, perk counts, Legendary skill reset behavior, reset warnings, and all-perks level target. |
| SRC-000422 | Skyrim:Leveling | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Leveling | 2026-05-12 | Skill XP, character XP, level-up rewards, XP bonuses, all-perks XP math, and high-level leveling behavior. |
| SRC-000415 | Skyrim:Survival Mode | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Survival_Mode | 2026-05-12 | Survival Mode sleep-gated level-up behavior. |
| SRC-000418 | Skyrim:Fatigue | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fatigue | 2026-05-12 | Survival fatigue penalties relevant to potion-supported crafting and combat readiness. |

## Evidence Summary

UESP's Skills page lists 18 skill trees with 180 perk nodes and 251 perk ranks. It states that Legendary skills can reset a skill at 100 back to 15, refunding that skill's allocated perk points and allowing character leveling beyond the old cap. The same page gives level 252 as the level needed to unlock all skill perks.

UESP's Leveling page explains that character XP comes from skill increases, that each character level-up grants one attribute choice and one perk point, and that perk points can be saved. It also gives the all-perks math: level 252 grants enough perk points for all 251 perks, and actually unlocking all perks requires every skill to be at 100, corresponding to 165 complete skill mastering cycles from standard starting skill levels.

The reset warnings are route-critical:

| Reset subject | Constraint |
| --- | --- |
| Combat and armor skills | Resetting these temporarily removes power while enemies remain scaled, so the route must not reset all active offense and defense skills at the same time. |
| Spell schools | Learned spells are retained, making prepared magic schools stronger late-reset candidates if the player has enough Magicka or cost-reduction support. |
| Weapon skills | Enchantment damage and tempering do not improve weapon-skill XP, so efficient retraining does not come from simply making weapons stronger. |
| Lockpicking | Previously picked locks do not grant XP again, and the route can eventually run out of useful locks; Lockpicking should not be a repeated Legendary reset target. |
| Speech | Speech checks are mostly one-time and losing Merchant/Fence temporarily changes selling options; repeated Speech resets should not be a baseline plan. |
| Modified skill values | A skill should not be made Legendary while a temporary Fortify Skill effect is active; wait until the displayed skill value is normal. |

Survival Mode adds two constraints: level-ups require sleeping in a bed, and fatigue can reduce the effectiveness of beneficial potions. Progression checkpoints that depend on perk allocation, crafting potions, or late combat readiness therefore need rest access and fatigue checks.

## Confidence and Open Questions

Confidence is high that all-perks requires a level-252 plan with Legendary resets and final recovery to skill 100.

Open questions for later work:

* exact Legendary reset distribution by skill;
* exact route order for skill books, trainers, quest skill rewards, and natural leveling;
* acceptable late-game grind locations or loops;
* whether any exploit-adjacent acceleration method is permitted under the project policy;
* final attribute distribution across Health, Magicka, and Stamina.

## Linked Records

`data/constraints/skill-perk-leveling-plan.md`; `data/skills/skill-perk-catalog.csv`; `data/skills/perk-rank-catalog.csv`; `data/objectives/objectives.csv` rows `OBJ-002425` through `OBJ-002465`; `docs/task-board.md`.
