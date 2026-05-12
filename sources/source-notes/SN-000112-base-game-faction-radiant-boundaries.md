# Source Note: Base-Game Faction Radiant Boundaries

Status: researched.

Source note ID: SN-000112

## Claim

Base-game faction radiants should be bounded by required questline gates, finite post-quest chains, representative coverage, or failure-state exclusion. The major count constraints are four Companions interstitial radiants, two-of-three Silver Hand window radiants, three Totems of Hircine, two Companions `Purity` quests, 20 Thieves Guild city jobs for restoration, and a 125-job Thieves Guild side-job display/safe counter if full Guild display unlocks remain in checklist scope.

## Routing Relevance

This note prevents radiant rows from becoming infinite grind. It also flags where the route must not promise impossible one-save coverage, such as all three Silver Hand window radiants, and where an apparently repeatable system has completionist unlocks, such as Thieves Guild side-job trophies.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000003 | Skyrim:Companions | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Companions | 2026-05-12 | Required gates, radiant windows, finite post-quest counts, and Hired Muscle caveat. |
| SRC-000004 | Skyrim:College of Winterhold (faction) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:College_of_Winterhold_(faction) | 2026-05-12 | College repeatable quest inventory and Rejoining the College failure state. |
| SRC-000005 | Skyrim:Thieves Guild (faction) | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Thieves_Guild_(faction) | 2026-05-12 | Delvin/Vex jobs, restoration counts, side-job display thresholds, and Raven Rock caveats. |
| SRC-000006 | Skyrim:Dark Brotherhood | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dark_Brotherhood | 2026-05-12 | Dark Brotherhood radiant inventory context. |
| SRC-000397 | Skyrim:Totems of Hircine | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Totems_of_Hircine | 2026-05-12 | Three totems, werewolf prerequisite, and Aela radiant caveats. |
| SRC-000398 | Skyrim:The Words of Power | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Words_of_Power | 2026-05-12 | Arngeir word-wall radiant repeatability, target limits, Paarthurnax dependency, and Arcwind bug. |
| SRC-000399 | Skyrim:The Dark Brotherhood Forever | 2 - UESP | https://en.uesp.net/wiki/Skyrim:The_Dark_Brotherhood_Forever | 2026-05-12 | Endless Dark Brotherhood post-quest assassination radiant. |
| SRC-000405 | Skyrim:Honor Thy Family | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Honor_Thy_Family | 2026-05-12 | Dark Brotherhood membership-repair failure-state quest. |

## Evidence Summary

UESP lists Companions primary quest progress as requiring one radiant after `Take Up Arms`, one after `Proving Honor`, and two after `The Silver Hand`, with the first Silver Hand radiant coming from Aela. It also states that the Silver Hand radiant window allows only two of the three listed quests in a playthrough, and that Hired Muscle is recommended early because it becomes unavailable later.

The Companions page and Totems page bound the post-quest chains: `Totems of Hircine` can be done three times and only while the player remains a werewolf; `Purity` can be done twice for Vilkas and Farkas; `Dragon Seekers` requires `Dragon Rising` and remains representative after one completion. The Totems page adds no-console-relevant caveats around Aela, lycanthropy, and initial Aela radiant handling, so the route should keep lycanthropy and save discipline until all three totems are secured.

The College page lists repeatable College errands and identifies `Rejoining the College` as a repair state after harming a College member. The route should use one representative completion for normal College repeatables, but should not intentionally trigger the failure-state quest.

The Thieves Guild page states that Delvin/Vex jobs are repeatable, that five jobs in each of Markarth, Solitude, Whiterun, and Windhelm are required before the corresponding special reputation quest, and that Riften jobs do not count toward restoration. It also records side-job display thresholds at 5, 15, 25, 35, 45, 55, and 75 jobs, plus a safe at 125 jobs. Raven Rock can be assigned for some jobs; Raven Rock Bedlam is bugged and Solstheim has no restoration quest.

`The Dark Brotherhood Forever` is endless after the faction finale, so one representative completion is sufficient. `Honor Thy Family` is a membership repair after attacking a Dark Brotherhood member, so it should be excluded from the intentional route. `The Words of Power` is a repeatable word-wall locator; it should serve all-word-wall routing only and should not become an independent grind.

## Confidence and Open Questions

Confidence is high for the fixed counts and exclusion rules. The Hired Muscle row is seed-sensitive because UESP says the first Companions radiant is seed-fixed; TB-021 policy is to accept it if offered early, but not force a new-game restart solely for that one representative type. The 125 Thieves Guild side-job counter is source-backed as an unlock boundary, but TB-030 should decide whether those display objects become explicit checklist rows or a clearly labeled completionist grind.

## Linked Records

`data/constraints/radiant-boundaries.md`; OBJ-000026; OBJ-000048; OBJ-000102 through OBJ-000116; OBJ-000121 through OBJ-000128; OBJ-000134 through OBJ-000140; OBJ-000161; OBJ-000162; OBJ-000317; OBJ-000816.
