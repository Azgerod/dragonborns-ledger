# Source Note: Service, Investment, Training, and Favor NPC Dependencies

Status: researched.

Source note ID: SN-000108

## Claim

Merchant investment, trainer access, thane-help counts, and representative favor/activity rows depend on accessible NPCs or services, but most are service-planning constraints rather than hard branch decisions.

## Routing Relevance

The project requires all available merchant investments and all perks, while also tracking thaneships, representative favors, Hard Worker actions, marriage prerequisites, and route-convenience training. TB-016 should protect the NPC/service surfaces needed for these systems without prematurely choosing exact trainers, favor targets, or regional route order.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000296 | Skyrim:Merchants | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Merchants | 2026-05-12 | Merchant investment table, merchant replacement notes, and investable merchant rows. |
| SRC-000286 | Skyrim:Speech | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Speech | 2026-05-12 | Investor perk prerequisite and Speech perk context. |
| SRC-000391 | Skyrim:Trainers | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Trainers | 2026-05-12 | Trainer limits, trainer list, faction gates, and training bugs. |
| SRC-000242 | Skyrim:Thane | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Thane | 2026-05-12 | Thaneship process, assist-people disposition counting, Civil War Jarl replacement handling, and housecarl rewards. |
| SRC-000302 | Skyrim:Chop Wood | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Chop_Wood | 2026-05-12 | Firewood-buyer work activity. |
| SRC-000303 | Skyrim:Gather Wheat | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Gather_Wheat | 2026-05-12 | Crop/farmer work activity. |
| SRC-000304 | Skyrim:Mine Ore | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Mine_Ore | 2026-05-12 | Ore-buyer work activity and Hard Worker overlap. |
| SRC-000305 | Skyrim:Fight! Fight! | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fight!_Fight! | 2026-05-12 | Brawl activity, opponent relationship changes, and follower interference caveat. |
| SRC-000306 | Skyrim:Quest all Beggars Have | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Quest_all_Beggars_Have | 2026-05-12 | Beggar favor, Gift of Charity, and thane-help relevance. |
| SRC-000307 | Skyrim:Quest all Drunks Have | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Quest_all_Drunks_Have | 2026-05-12 | Drunk favor, disposition effect, and representative favor relevance. |
| SRC-000244 | Skyrim:Marriage | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Marriage | 2026-05-12 | Merchant-spouse and investment interaction caveats. |

## Evidence Summary

The Merchants and Speech pages support the existing merchant-investment objective set: Investor requires Speech investment planning, and the merchant table identifies source-listed investable merchants. Since these rows depend on named merchants or listed replacements, the route should keep each investable service available until investment is made, while still deferring exact investment order to TB-020 and regional routing. The Marriage page adds a caution that marrying merchant candidates can change merchant behavior or investment dialogue, so any selected spouse who is also an investable merchant should be invested in before marriage unless later testing approves the reverse order.

The Trainers page states that trainers can raise a skill by one level per lesson, up to five training sessions per character level, with trainers unable to raise skills past 90. It also lists faction-gated trainers and notes that vampire state can block the opposite Dawnguard/Volkihar trainer service until the player cures or restores the relevant state. Because the project already requires all skills/perks, trainer use is a TB-020 planning tool, not a separate TB-016 route objective, but training-dependent NPCs should not be sacrificed or alienated before the leveling plan decides whether they are needed.

The Thane page states that assisting hold citizens works by raising citizen disposition and that already-raised disposition counts toward the later assist objective; it also notes friend deaths usually do not remove progress. That supports choosing safe, accessible favor targets later rather than protecting every possible favor NPC indefinitely. The work, brawl, beggar, and drunk pages support representative rows whose exact target NPCs should be selected in TB-018/TB-019 based on safety, Survival Mode routing, and thane-help usefulness.

## Confidence and Open Questions

Confidence is high for the service-class rules. Exact trainer choices, whether to buy every possible training session, investment timing, Warmaiden's shared-store treatment, spouse/investment ordering for merchant spouses, brawl target, work/favor targets, and regional pairing with thane objectives remain downstream.

## Linked Records

`data/constraints/npc-dependencies.md`, `data/skills/merchant-investment-catalog.csv`, OBJ-001926 through OBJ-001935, OBJ-002717 through OBJ-002750, OBJ-002762 through OBJ-002767, and TB-018/TB-020 handoffs.
