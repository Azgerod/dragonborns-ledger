# Source Note: Miscellaneous, Favor, Bounty, and Activity Boundaries

Status: researched.

Source note ID: SN-000113

## Claim

Named miscellaneous and favor rows in the TB-018 queue are finite route objectives: complete each named row once, but do not repeat its radiant target variants. Bounty quest rows are representative by type, one each for bandit boss, dragon, Forsworn, and giant. No-journal activity/favor rows are representative once each unless a later thaneship, trophy, or checklist pass deliberately reuses the same activity for another purpose.

## Routing Relevance

This keeps `Hero of the People`, thaneship support, relationship favors, and representative activity coverage distinct from arbitrary repeated objectives. It also preserves exact gates for bounties and work activities without choosing final targets before Survival Mode and route geography are known.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000020 | Skyrim:Miscellaneous Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Miscellaneous_Quests | 2026-05-12 | Miscellaneous radiant variation and first-visit caveat. |
| SRC-000021 | Skyrim:Bounty Quests | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bounty_Quests | 2026-05-12 | Bounty repeatability, active-quest limits, type gates, and bugs. |
| SRC-000302 | Skyrim:Chop Wood | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Chop_Wood | 2026-05-12 | Repeatable firewood work activity, Hard Worker overlap, and disposition/thane effect. |
| SRC-000303 | Skyrim:Gather Wheat | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Gather_Wheat | 2026-05-12 | Repeatable crop-sale work activity and disposition/thane effect. |
| SRC-000304 | Skyrim:Mine Ore | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Mine_Ore | 2026-05-12 | Repeatable ore work activity, Hard Worker overlap, and disposition/thane effect. |
| SRC-000305 | Skyrim:Fight! Fight! | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Fight!_Fight! | 2026-05-12 | Repeatable brawl favor, disposition/thane effect, and similar-radiant blocking. |
| SRC-000306 | Skyrim:Quest all Beggars Have | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Quest_all_Beggars_Have | 2026-05-12 | Repeatable beggar favor, Gift of Charity, and disposition/thane effect. |
| SRC-000307 | Skyrim:Quest all Drunks Have | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Quest_all_Drunks_Have | 2026-05-12 | Repeatable drunk favor, disposition/thane effect, and non-Hero caveat. |
| SRC-000354 | Skyrim:Kill the Bandit Leader | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Kill_the_Bandit_Leader | 2026-05-12 | Ahtar, Annekke, Brunwulf, and Fanari target pools and caveats. |

## Evidence Summary

The Miscellaneous Quests page says many miscellaneous quests use radiant systems for dynamic assignees or targets, and it preserves the first-visit availability caveat already used by earlier bug and cell-entry passes. For TB-018, that means radiant target variance is not a separate completion objective: a named favor row is complete after its named giver/objective is successfully resolved once.

Bounty quests are repeatable indefinitely, but the source constrains them by type and active-quest state: the player can have one each of bandit boss, dragon, Forsworn, and giant bounties active at the same time, from separate holds. Dragon bounties require `Dragon Rising`, giant bounties require level 20, and Forsworn bounties are Reach-exclusive. The route should complete one representative bounty of each type, then exclude further bounty repetition except when a later route block uses a bounty as useful support.

The work/activity pages identify Chop Wood, Gather Wheat, Mine Ore, Fight! Fight!, beggar giving, and drunk giving as repeatable radiant or no-journal activity/favor systems. Chop Wood and Mine Ore can satisfy Hard Worker through the station action itself; paid turn-ins are still useful representative favor coverage. Beggar and drunk favors can be repeated indefinitely, and the drunk-favor page says it does not advance `Hero of the People`. Brawls can silently block nearby similar brawl quest givers, so the route should pick one deliberate brawl target.

The `Kill the Bandit Leader` page confirms that similarly named rows can belong to different named givers, including Fanari in Skaal Village. Each named giver row is a separate finite favor boundary, not a reason to repeat generic bandit-leader bounties.

## Confidence and Open Questions

Confidence is high for one-completion boundaries and bounty gates. Exact targets should remain deferred to route geography, NPC safety, thaneship support, and Survival Mode constraints. TB-021 should check whether any no-journal activity row should be demoted if another explicit trophy or thane step naturally covers it.

## Linked Records

`data/constraints/radiant-boundaries.md`; OBJ-000221 through OBJ-000223; OBJ-000225 through OBJ-000227; OBJ-000229; OBJ-000230; OBJ-000232; OBJ-000234; OBJ-000236 through OBJ-000239; OBJ-000241 through OBJ-000245; OBJ-000247; OBJ-000249; OBJ-000252 through OBJ-000254; OBJ-000256; OBJ-000261 through OBJ-000267; OBJ-000274; OBJ-000278 through OBJ-000280; OBJ-000282 through OBJ-000284; OBJ-000320; OBJ-000321; OBJ-000327; OBJ-000329 through OBJ-000335; OBJ-000438; OBJ-002762 through OBJ-002767.
