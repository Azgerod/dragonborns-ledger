# Source Note: Training and Skill Boost Constraints

Status: needs review.

Source note ID: SN-000120

## Claim

Skill training is useful for the all-skills/all-perks plan but cannot replace normal leveling. The route can buy only five training sessions per character level, unused sessions do not carry over, trainers cannot raise a skill above 90, and faction, quest, NPC, and vampire-state gates make trainer access route-dependent.

## Routing Relevance

This note supports the TB-020 training policy and later TB-027 placement of training blocks. It does not select every trainer visit.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000391 | Skyrim:Trainers | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Trainers | 2026-05-12 | Trainer list, trainer class caps, five-session limit, no-carryover behavior, faction gates, and training bugs. |
| SRC-000422 | Skyrim:Leveling | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Leveling | 2026-05-12 | Training interaction with character XP, high-level limits, and pickpocket/training exploit caveats. |
| SRC-000268 | Skyrim:Skills | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Skills | 2026-05-12 | Skill increase sources and Legendary reset context. |

## Evidence Summary

UESP's Trainers page states that training raises skills for gold and that only five skill levels may be purchased per character level. It also states that old opportunities are lost when the character levels: unused training sessions do not carry over. Trainer classes cap at common 50, expert 75, and master 90, so the final ten levels of each skill require use, skill books, quest rewards, or other non-training sources.

The trainer table is route-dependent. Several trainers require faction access, quest completion, vampire state, Dawnguard or Volkihar progression, College access, Companions access, Thieves Guild access, Blood-Kin status, or Solstheim decisions. The Hall of the Vigilant trainer is time-sensitive with Dawnguard installed, and some AE or unofficial-patch-related trainer notes are not reliable for an official PS4 AE route.

Training should be treated as a controlled checkpoint:

| Training rule | Constraint |
| --- | --- |
| Five sessions per level | Use planned sessions soon after leveling, before accidental skill gains force the next level. |
| No carryover | Do not save training for later once a new character level has been reached. |
| Cap at 90 | Do not assign training as the sole plan for finishing skill-100 objectives. |
| XP bonuses | Training grants skill XP and can interact with skill XP bonuses, but routing must verify actual level gains. |
| Bug risk | Keep a hard save before expensive training blocks and verify the skill increased when relying on the session. |
| Exploit boundary | Follower-trainer gold recovery and trainer-gold pickpocket loops should not be baseline route tools. |

The Leveling page warns that training at high character levels supplies only a small part of the XP needed for the next level. It also describes a Pickpocket/training loop and warns that starting it early can leave the character weak in combat. Under the guide specification's gradual power curve, such loops should be treated as exploit-adjacent and deferred unless explicitly approved.

## Confidence and Open Questions

Confidence is high for the five-per-level rule, trainer caps, and no-carryover constraint.

Open questions for later work:

* which skills receive paid training before level-gated quest rewards;
* whether the route should spend all five sessions every level or only at key checkpoints;
* exact safe trainer list after NPC-dependency review;
* whether any gold-recovery shortcut is permitted as an optional late cleanup tactic.

## Linked Records

`data/constraints/skill-perk-leveling-plan.md`; `data/constraints/npc-dependencies.md`; `data/skills/skill-perk-catalog.csv`; `docs/task-board.md`.
