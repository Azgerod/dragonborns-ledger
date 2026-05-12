# Radiant Boundaries

Status: TB-021 reviewed.

Scope: this is a constraint table, not route prose. It distinguishes required radiant gates, finite radiant chains, representative radiant types, branch-only radiants, support-only locator radiants, and excluded repetition. It does not choose exact radiant targets unless the source makes the target or count part of the constraint.

## Boundary Classes

| Class | Meaning |
| --- | --- |
| Required gate | Complete because a questline, trophy, or unlock cannot progress without it. |
| Finite chain | Repeat until the source-listed finite reward/unlock set is exhausted. |
| Representative | Complete one deliberate instance of the type, then exclude arbitrary repeats. |
| Completionist counter | Repeat to a source-listed finite display/unlock count; later checklist work may decide how prominently to route it. |
| Branch-only | Complete only inside the named hard-save branch, not on the canonical main save. |
| Support-only | Use only to support separately tracked objectives; do not treat as independent grind. |
| Excluded failure state | Do not trigger intentionally; resolve only if a mistake causes it. |

## Base-Game Faction and System Radiants

| Row(s) | Radiant/system | Class | Completion boundary | Route implications | Source notes | Status |
| --- | --- | --- | --- | --- | --- | --- |
| OBJ-000026 | Companions required radiant gates | Required gate | Complete four interstitial Companions radiants: one after `Take Up Arms`, one after `Proving Honor`, and two after `The Silver Hand`; the first Silver Hand radiant comes from Aela. | These are questline progress gates, not optional representative cleanup. | SN-000112 | Required. |
| OBJ-000102-OBJ-000108 | Companions post-`Take Up Arms` radiant pool | Representative / gate pool | Complete one instance of each type where route-feasible, with the required gate completions counting toward this pool. Hired Muscle is seed-sensitive and should be accepted if offered early, but TB-021 does not require a new-game restart solely to force it. | Do not grind arbitrary repeats after representative/gate coverage. | SN-000112 | Representative with seed caveat. |
| OBJ-000109-OBJ-000111 | Companions Silver Hand window radiants | Windowed representative pool | Complete two total before `Blood's Honor`; all three cannot normally be completed in one playthrough. | Route chooses two and marks the unchosen third as one-save-limited, not a failure. | SN-000112 | Windowed limit. |
| OBJ-000112; OBJ-000816 | Totems of Hircine and werewolf totem howl set | Finite chain | Complete all three totem retrievals while still a werewolf. | Do not cure lycanthropy or destabilize Aela follower state before all three totems and howl choices are secured. | SN-000112 | Required finite chain. |
| OBJ-000113 | Purity (Companions) | Finite chain | Complete the two available `Purity` quests for Vilkas and Farkas. | Separate from the player's final transformation-state decision. | SN-000112 | Required finite chain. |
| OBJ-000114 | Dragon Seekers | Representative | Complete one instance after `Dragon Rising` is complete. | Repeats after one representative completion are excluded. | SN-000112 | Representative. |
| OBJ-000115; OBJ-000116 | Companions parent radiant sets | Parent rows | No independent completion count beyond the Companions rows above. | Use as aggregate coverage labels only. | SN-000112 | Covered by child rows. |
| OBJ-000121-OBJ-000124; OBJ-000126-OBJ-000128 | College repeatables except `Rejoining the College` | Representative | Complete one representative instance of each listed College repeatable. | Exact errand targets remain route-geography decisions. | SN-000112 | Representative. |
| OBJ-000125 | Rejoining the College | Excluded failure state | Do not intentionally attack or murder College members to trigger the repair quest. | If triggered by mistake, resolve as recovery, not completion content. | SN-000112 | Excluded. |
| OBJ-000048 | Thieves Guild city influence and side job counter | Required gate plus completionist counter | Complete at least 20 eligible Delvin/Vex jobs: five each in Markarth, Solitude, Whiterun, and Windhelm, then complete each city reputation quest. Continue tracking total Delvin/Vex side jobs to 125 for the final Guild display/safe boundary. | Riften jobs do not count for restoration. Reject or manage non-restoration assignments, especially Raven Rock Bedlam. TB-031F chooses exact job mix and counter mechanics. | SN-000112 | Required gate plus required completionist counter after TB-031C. |
| OBJ-000134-OBJ-000140 | Thieves Guild job types | Representative / completionist counter | Complete one of each job type for representative coverage; use these job types as the selectable pool for the 125-job counter. After 125, exclude repeats. | The first 20 eligible jobs satisfy restoration; the remaining counter work should be labelled completionist grind rather than faction-restoration work. | SN-000112 | Representative plus counter. |
| OBJ-000161 | Honor Thy Family | Excluded failure state | Do not attack Dark Brotherhood members to trigger it. | Resolve only if a mistake blocks Dark Brotherhood service. | SN-000112 | Excluded. |
| OBJ-000162 | The Dark Brotherhood Forever | Representative | Complete one post-finale assassination contract. | Endless repeats after one representative completion are excluded. | SN-000112 | Representative. |
| OBJ-000317 | The Words of Power | Support-only | Use Arngeir's locator only as needed to support separately tracked word-wall/shout objectives. | Preserve Paarthurnax on the main route; avoid depending on Arcwind Point as the assigned target. | SN-000112 | Support-only. |

## Miscellaneous, Favor, Bounty, and Activity Boundaries

| Row(s) | Radiant/system | Class | Completion boundary | Route implications | Source notes | Status |
| --- | --- | --- | --- | --- | --- | --- |
| OBJ-000221-OBJ-000223; OBJ-000225-OBJ-000227; OBJ-000229; OBJ-000230; OBJ-000232; OBJ-000234; OBJ-000236-OBJ-000239; OBJ-000241-OBJ-000245; OBJ-000247; OBJ-000249; OBJ-000252-OBJ-000254; OBJ-000256; OBJ-000261-OBJ-000267; OBJ-000274; OBJ-000278-OBJ-000280; OBJ-000282-OBJ-000284; OBJ-000320; OBJ-000321; OBJ-000327; OBJ-000329-OBJ-000331 | Named miscellaneous and favor rows with radiant or target-selected elements | Finite named objectives | Complete each named row once. Radiant target variants are not separate objectives. | Exact target, item source, speech outcome, NPC safety, first-visit, and thaneship timing remain route decisions. | SN-000113 | Required once each. |
| OBJ-000332 | Bounty: Bandit Boss | Representative | Complete one bandit boss bounty. | Extra bandit bounties are optional support only. | SN-000113 | Representative. |
| OBJ-000333 | Bounty: Dragon | Representative | Complete one dragon bounty after `Dragon Rising`. | Do not rely on a dragon bounty for dragon-soul trophy progress unless the soul is verified. | SN-000113 | Representative. |
| OBJ-000334 | Bounty: Forsworn | Representative | Complete one Reach Forsworn bounty. | Keep distinct from Igmund's non-repeating Jarl favor. | SN-000113 | Representative. |
| OBJ-000335 | Bounty: Giant | Representative | Complete one giant bounty at level 20 or later. | Delay until Legendary difficulty and Survival Mode planning make the fight reasonable. | SN-000113 | Representative. |
| OBJ-002762 | Chop Wood representative activity | Representative / trophy support | Complete one player wood-chopping action for Hard Worker support and one paid firewood turn-in for favor coverage. | Follower chopping does not replace the player's trophy action. | SN-000113 | Representative. |
| OBJ-002763 | Gather Wheat representative activity | Representative | Complete one qualifying crop sale to a farmer. | Exact crop and farmer should be chosen for route geography or thane support. | SN-000113 | Representative. |
| OBJ-002764 | Mine Ore representative activity | Representative / trophy support | Complete one player mining action for Hard Worker support and one paid ore turn-in for favor coverage. | The ore sale is useful but not required for the trophy action. | SN-000113 | Representative. |
| OBJ-002765 | Fight! Fight! representative brawl | Representative | Win one qualifying brawl and finish the post-fight dialogue. | Pick a deliberate target; nearby brawl givers can silently block one another. | SN-000113 | Representative. |
| OBJ-002766 | Quest all Beggars Have representative favor | Representative | Give one gold to one eligible beggar and receive Gift of Charity. | Repeats are excluded unless needed for local thane/favor support. | SN-000113 | Representative. |
| OBJ-002767 | Quest all Drunks Have representative favor | Representative | Share one accepted drink with one eligible drunk. | Does not advance `Hero of the People`; use only for representative/favor or thane support. | SN-000113 | Representative. |

## DLC and Branch Radiant Boundaries

| Row(s) | Radiant/system | Class | Completion boundary | Route implications | Source notes | Status |
| --- | --- | --- | --- | --- | --- | --- |
| OBJ-000365 | Ancient Technology | Finite chain | Complete six total runs to unlock the full Dawnguard crossbow and bolt crafting/vendor set. | Prefer finishing before late Dawnguard progression creates marker/dialogue risk. | SN-000114 | Required finite chain. |
| OBJ-000371 | Lost Relic | Finite chain | Complete all three relic retrievals for the Dawnguard Rune Hammer, Rune Shield, and Rune Axe. | Requires first `Ancient Technology` and semi-random Dawnguard side-radiant cycling; exact filler count is not deterministic. | SN-000114 | Required finite chain. |
| OBJ-000367-OBJ-000370; OBJ-000372; OBJ-000373 | Dawnguard repeatable side radiants | Representative / unlock filler | Complete one representative instance of each type, then repeat only as needed to unlock all three `Lost Relic` versions. | `Cleansing Light` should not accept Movarth's Lair if avoidable; `A Jarl's Justice` can only recur every twelve days at best. | SN-000114 | Representative plus filler. |
| OBJ-000374 | Amulets of Night Power | Branch-only finite reward | In the Volkihar branch, complete the quest once to retrieve both amulets. | Requires vampire-branch context and Summon Gargoyle perk access. | SN-000114 | Branch finite chain. |
| OBJ-000375 | Ancient Power | Branch-only finite upgrade | In the Volkihar branch, complete four successful body-part upgrades to reach the nine-day maximum Blood of the Ancients duration. | Duplicate body parts may be requested; count successful duration increases, not unique part names. | SN-000114 | Branch finite chain. |
| OBJ-000376; OBJ-000377; OBJ-000380; OBJ-000382 | Ordinary Volkihar repeatable radiants | Branch-only representative | Complete one branch instance each of `Culling the Beast`, `Deceiving the Herd`, `The Hunt`, and `Protecting the Bloodline`. | Extra repeats are excluded unless a branch checklist later needs a specific target/world-state. | SN-000114 | Branch representative. |
| OBJ-000378 | Destroying the Dawnguard | Branch-only finite quest | In the Volkihar branch, complete once after Volkihar-side `Kindred Judgment`. | Kills Dawnguard leaders on the branch only; never route on the Dawnguard canonical save. | SN-000114 | Branch finite quest. |
| OBJ-000381 | New Allegiances | Branch-only finite / representative | Complete at least one Volkihar conversion. Up to three distinct named targets may be pursued if the Volkihar branch checklist treats all conversions/coffins as required; duplicate-target offers should be avoided. | TB-028 should settle whether all three conversions are worth full branch routing. | SN-000114 | Branch policy handoff. |
| OBJ-000383 | Rings of Blood Magic | Branch-only finite reward | In the Volkihar branch, complete the quest once to retrieve both rings. | Preserve Ring of the Beast and Ring of the Erudite as branch rewards. | SN-000114 | Branch finite chain. |
| OBJ-000412 | Bandit Attack | Opportunistic / excluded random | Do not force the Hearthfire spouse-kidnapping event. Resolve safely if it triggers naturally. | Family-home defaults can reduce exposure; keep saves if spouse is housed at a constructable homestead. | SN-000114 | Excluded as forced content. |
| OBJ-000438 | Dragonborn Skaal Kill the Bandit Leader | Finite named objective | Complete Fanari's Skaal Village bandit-leader favor once. | Treat as a named Solstheim favor, not as generic bounty repetition. | SN-000114; SN-000113 | Required once. |

## Handoffs

| Topic | Follow-up |
| --- | --- |
| Companions Hired Muscle | TB-021 policy: accept and route it if the early seed offers it, but do not require a new-game restart solely for this representative radiant type. |
| Thieves Guild 125 side jobs | TB-031C decided this is required completionist counter coverage through `OBJ-000048`; TB-031F must choose the exact job mix, rejection policy, Raven Rock/Riften handling, and counter-tracking mechanics. |
| Dawnguard Lost Relic filler | Route phases should record actual side-radiant fillers while cycling for all three relics; the table only supplies the count boundary. |
| New Allegiances | Branch planning should decide whether the Volkihar branch completes one conversion or all three possible named conversions. |
| No-journal activities | TB-019 should choose representative targets that also support Survival Mode travel, thaneship, relationship, or economy needs. |
