# SN-000252 - Fanari Bandit Leader Route

Status: targeted TB-044 route-resolution source note.

## Scope

This note closes `OBJ-000438` Kill the Bandit Leader, Fanari Strong-Voice's Skaal Village bandit-leader favor.

## Sources

| Source ID | Title | Tier | URL | Accessed | Used for |
| --- | --- | --- | --- | --- | --- |
| SRC-000354 | Skyrim:Kill the Bandit Leader | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Kill_the_Bandit_Leader | 2026-05-30 | Quest ID, radiant/favor structure, Fanari target pool, quick walkthrough, stage boundary, Solstheim reaver note, and Eastmarch-only bug caveats. |
| SRC-001863 | Skyrim:Fanari Strong-Voice | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fanari_Strong-Voice | 2026-05-30 | Fanari's Skaal Village/Greathall context, protected status, related quest list, help-the-Skaal dialogue, and turn-in dialogue. |

## Route Decisions

Fanari's row is a finite named favor, not a generic bounty grind. `SN-000113` and `SN-000114` already classify it as required once; this pass gives that boundary a concrete route.

The guide now starts the favor at Skaal Village after `A New Source of Stalhrim` is secured. This keeps Deor/Fanari scene safety first, then uses `HS-SKAAL-FANARI-BANDIT` before accepting Fanari's target-selected quest. UESP lists Fanari's possible targets as Bloodskal Barrow, Brodir Grove, Damphall Mine, Hrodulf's House, and the Wreck of the Strident Squall. It also notes that the Solstheim targets use reavers even though the journal still says bandit leader.

Bloodskal Barrow has already been consumed by the Raven Rock Mine route when Fanari is accepted. If Fanari assigns Bloodskal and the active marker still points to a live marked leader, the guide completes that target immediately. If the marker points to a dead or missing leader, the guide reloads `HS-SKAAL-FANARI-BANDIT` and accepts again, proceeding only with an assignment whose marked leader can be killed. This is blocked-target recovery for an already consumed route location, not ordinary target shopping.

The other four target sites are still naturally ahead in the route when Fanari is accepted. The guide leaves those assignments active and closes them during `Kolbjorn Excavation And Raven Rock West`, where `SN-000188` already routes Hrodulf's House, the Wreck of the Strident Squall, Brodir Grove, and Damphall Mine as full location clears. Each target step now tells the player to confirm that Fanari's marked leader dies and that the objective advances to the report-back stage. After the section, the route returns to Skaal Village to report to Fanari and complete the favor.

## Coverage Summary

This pass closes `OBJ-000438` by adding a start point, active-target policy, no-convenience-reroll language, Bloodskal-only blocked-target recovery, target-site integration, and Fanari turn-in. It leaves no additional checklist row open for the favor.

## Linked Records

OBJ-000438; `drafts/final-guide/main-guide-v1.md`; `data/objectives/objectives.csv`; `data/constraints/radiant-boundaries.md`; `data/guide-coverage/main-guide-v1-coverage.csv`.
