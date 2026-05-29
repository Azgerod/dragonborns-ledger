# SN-000208 - Reparations Failure-State Policy

Status: researched.

Source note ID: SN-000208

## Claim

`Reparations` is a Thieves Guild failure-state recovery quest, not intentional route content. The main route should preserve clean Thieves Guild membership, avoid the triggers, and reload a clean save if the quest starts. Paying Vex 1,000 gold is recovery only, not guide completion.

## Routing Relevance

TB-044 closes `OBJ-000142` by treating it consistently with the existing College and Dark Brotherhood membership-repair exclusions. The guide needs a player-facing warning at the first Thieves Guild membership point, because later sections depend on Vex, Delvin, Tonilia, fences, training, restoration jobs, and Guild Master services staying available.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-001515 | UESP | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Reparations | 2026-05-28 | Quest trigger, Vex 1,000-gold reinstatement path, service lockout, 48-hour hostility caveat, and confirmed false-trigger bug note. |

## Evidence Summary

UESP identifies `Reparations` as an automatic quest after offending the Thieves Guild. Listed triggers include assaulting or murdering a guild member, being caught stealing from the guild, or murdering someone during a guild quest. The penalty is expulsion: training, fencing, and normal guild conversations are restricted until the player speaks to Vex and pays 1,000 gold.

UESP also records a relevant bug: the quest may incorrectly trigger as a result of Dark Brotherhood quests. Because the PS4 route cannot use console fixes and depends on clean Thieves Guild services across many later sections, the safest player-facing policy is reload-on-trigger rather than treating the Vex payment as normal route content.

## Route Decision

Add an early Thieves Guild membership warning: keep guild membership clean, do not attack or steal from guild members, do not kill NPCs during guild jobs unless the guide explicitly instructs it, and reload the latest clean save if `Reparations` starts or guild services shut off. `OBJ-000142` is therefore an excluded failure-state objective with recovery-only instructions.

## Confidence and Open Questions

Confidence is high for the exclusion policy. The source describes a concrete recovery path, but routing that recovery would require deliberately damaging Thieves Guild state and paying an avoidable 1,000-gold penalty. No open route question remains for `OBJ-000142`.

## Linked Records

`OBJ-000142`; `data/constraints/radiant-boundaries.md`; `drafts/final-guide/main-guide-v1.md`; `data/guide-coverage/main-guide-v1-coverage.csv`.
