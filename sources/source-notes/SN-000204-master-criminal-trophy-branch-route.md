# SN-000204 - Master Criminal Trophy Branch Route

Status: route-writing source note for TB-035-MR-070.

## Scope

This note supports the v1 guide section `Master Criminal Trophy Branch`. The pass converts the scaffold into a controlled trophy branch that creates 1000-gold bounties in all nine Skyrim holds, verifies the trophy, and reloads clean continuity.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000002 | Skyrim:Achievements | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Achievements | 2026-05-12 | Base-game trophy list and Master Criminal requirement. |
| SRC-001509 | Skyrim:Crime | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Crime | 2026-05-28 | Hold-separated bounty tracking, murder and shapeshift bounty amounts, guard arrest behavior, stolen-item confiscation, and Master Criminal tracking note. |

## Route Decisions

The branch remains a clean-continuity trophy branch. The guide starts from an owned home after MR-069, creates `HS-TROPHY-MASTER-CRIMINAL`, plays only the bounty-state branch, verifies the trophy, then reloads the named hard save.

UESP's Master Criminal achievement text requires a bounty of 1000 gold in all nine holds. The Crime page adds two route-critical details: bounties are tracked separately by hold and the achievement must have all nine bounties simultaneously. The guide therefore checks General Stats > Crime after each hold and again after the ninth hold.

The route is mortal after the transformation closeout, so the witnessed shapeshift shortcut is not available. The branch uses one witnessed murder bounty per hold because murder is a 1000-gold crime and avoids the uncertainty of accumulating many smaller assault or theft bounties. To reduce permanent-story risk inside the temporary branch, the target rule is one unnamed hold guard in view of another witness. The guide explicitly avoids named NPCs, services, spouses, children, followers, quest targets, and witness wipeout.

The guide uses rotating branch saves before each hold so a wrong-hold bounty, missing bounty, named-NPC death, or witness-cleared state can be retried without replaying the whole branch. The final accepted state is always the reload from `HS-TROPHY-MASTER-CRIMINAL`; the guide does not pay fines, serve jail time, or preserve any bounty branch state.

## Coverage Notes

This pass appends MR-070 coverage for `OBJ-002777`, the Master Criminal checklist/trophy row if present, and `HS-TROPHY-MASTER-CRIMINAL`. No new route-resolution rows are introduced.

Fishing species, Dragonrider's four post-Sahrotaar rides, `Note from Mogrul`, Potion of Blood, Ironwood Soup Elixir, Mysterious Potion, Corrupted Human Heart, Simon Rodayne's Heart, and Balbus's Fork remain with their documented later owners or route-resolution notes.
