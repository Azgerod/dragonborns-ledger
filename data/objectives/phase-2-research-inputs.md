# Phase 2 Research Input Index

Status: TB-010B complete.

This index maps Phase 2 constraint-table tasks to the objective rows and support tables they should start from.

It is a handoff artifact, not gameplay research. It does not resolve triggers, thresholds, conflicts, trophy behavior, bug behavior, route placement, or recommendations. Each Phase 2 task must still verify current source facts and cite new source notes before updating constraint tables.

## Queue Syntax

Objective ID ranges are inclusive. For example, `OBJ-000001-OBJ-000003` means `OBJ-000001`, `OBJ-000002`, and `OBJ-000003`.

Large queues are intentionally broad when the constraint could affect many route steps. The Phase 2 task should reduce its queue into researched constraint rows, explicit non-issues, or deferred checklist/route notes.

## Source Datasets

| Dataset | Role in Phase 2 |
| --- | --- |
| `data/objectives/objectives.csv` | Primary candidate objective queue. |
| `data/objectives/ae-creation-manifest.md` | AE package parent/child manifest. |
| `data/objectives/unique-item-reconciliation.md` | Unique item, artifact, and leveled-reward boundary decisions. |
| `data/objectives/aggregate-reconciliation.md` | Parent/set rows and downstream ownership notes. |
| `data/objectives/activity-favor-reconciliation.md` | No-journal activity/favor boundary and representative rows. |
| `data/items/ae-item-members.csv` | AE item member table and parent-objective links. |
| `data/books/skill-books-locations.csv` | Skill-book location candidates. |
| `data/books/spell-tomes-locations.csv` | Spell-tome acquisition candidates. |
| `data/books/book-document-locations.csv` | Quest, AE, Black Book, and unique book/document locations. |
| `data/locations/location-catalog.csv` | Clearable, discoverable, secondary, duplicate, and AE location rows. |
| `data/npc/relationship-options.csv` | Spouse, steward, follower, housecarl, adoption, pet, and role-option candidates. |
| `data/properties/property-details.csv` | Property, home, homestead, furnishing, farm, and service details. |
| `data/skills/skill-perk-catalog.csv` | Skill and perk-tree foundation rows. |
| `data/skills/perk-rank-catalog.csv` | Individual perk-rank requirements and prerequisites. |
| `data/skills/enchantment-learning-catalog.csv` | Learnable enchantment effects and preservation exclusions. |
| `data/skills/alchemy-effect-catalog.csv` | Ingredient effect discovery candidates. |
| `data/skills/merchant-investment-catalog.csv` | Merchant investment availability and audit rows. |
| `data/skills/practical-crafting-system-catalog.csv` | Practical crafting-system coverage. |
| `sources/source-notes/` | Prior source-list citations. Phase 2 must add tighter constraint-specific notes. |

## Phase 2 Summary

| Task | Constraint table | Candidate objectives | Main support inputs |
| --- | --- | ---: | --- |
| TB-011 | `data/constraints/ae-creation-start-triggers.md` | 684 | AE manifest, AE item members, AE books, AE properties, AE locations, AE skill/crafting rows. |
| TB-012 | `data/constraints/leveled-unique-items.md` | 24 | Unique item reconciliation, leveled reward rows, associated quest rows. |
| TB-013 | `data/constraints/cell-entry-locks.md` | 745 | Location catalog, unique items, leveled rewards, AE item members. |
| TB-014 | `data/constraints/quest-conflicts-hard-saves.md` | 744 | Quest/branch rows, option-list rows, artifact rows, relationship/property rows. |
| TB-015 | `data/constraints/trophy-dependencies.md` | 1,260 | Trophy rows, trophy relevance fields, objective rows with trophy/checklist notes. |
| TB-016 | `data/constraints/npc-dependencies.md` | 436 | NPC dependencies, relationship options, properties, pets/mounts, investments, favors. |
| TB-017 | `data/constraints/bug-prone-quests.md` | 932 | Bug-risk fields, bug notes, first-visit caveats, location catalog, quest rows. |
| TB-018 | `data/constraints/radiant-boundaries.md` | 110 | Radiant rows, favor rows, bounty rows, activity/favor reconciliation. |
| TB-019 | `data/constraints/survival-mode-constraints.md` | 2,552 | Location catalog, property details, pets/mounts, regional objective rows. |
| TB-020 | `data/constraints/skill-perk-leveling-plan.md` | 516 | Skill/perk, enchantment, alchemy, crafting, investment, trophy, and leveling rows. |

## TB-011 - AE Creation Start Triggers and Level Gates

Research question: for every official AE Creation row, what starts it, what gates it, what region it belongs to, and what must be delayed for difficulty, level, reward, conflict, or trophy reasons?

Candidate objective selectors:

* `source_content=ae_creation`
* `category=ae_creation`
* `subcategory` begins with `ae_`

Candidate objective IDs:

```text
OBJ-000479-OBJ-000759, OBJ-000813, OBJ-000814, OBJ-000912, OBJ-000913, OBJ-000919, OBJ-000920, OBJ-000922,
OBJ-000935-OBJ-000937, OBJ-000942-OBJ-000944, OBJ-000947, OBJ-000949, OBJ-000951, OBJ-000953, OBJ-000955,
OBJ-000956, OBJ-000958, OBJ-000959, OBJ-000961, OBJ-000963-OBJ-000965, OBJ-000969, OBJ-000970, OBJ-000972,
OBJ-000973, OBJ-000978-OBJ-000981, OBJ-000986, OBJ-000987, OBJ-000991, OBJ-000998, OBJ-001000, OBJ-001004,
OBJ-001008, OBJ-001011, OBJ-001013-OBJ-001016, OBJ-001031, OBJ-001033, OBJ-001336-OBJ-001554,
OBJ-001893-OBJ-001918, OBJ-001951, OBJ-002206, OBJ-002210, OBJ-002211, OBJ-002218, OBJ-002254, OBJ-002258,
OBJ-002262, OBJ-002269, OBJ-002308, OBJ-002332, OBJ-002336, OBJ-002340, OBJ-002346, OBJ-002352, OBJ-002385,
OBJ-002389, OBJ-002409-OBJ-002424, OBJ-002495, OBJ-002496, OBJ-002637-OBJ-002710, OBJ-002712, OBJ-002716
```

Support inputs:

* `data/objectives/ae-creation-manifest.md`
* `data/items/ae-item-members.csv`
* `data/books/book-document-locations.csv`
* `data/books/spell-tomes-locations.csv`
* `data/locations/location-catalog.csv`
* `data/properties/property-details.csv`
* `data/skills/alchemy-effect-catalog.csv`
* `data/skills/enchantment-learning-catalog.csv`
* `data/skills/practical-crafting-system-catalog.csv`

Output expectations:

* Record start trigger, level gate, recommended level, region, hard delay, core rewards, known conflicts, and checklist category.
* Mark unknowns explicitly rather than filling from memory.
* Do not route AE content yet.

## TB-012 - Leveled Unique Item Thresholds and Lock Timing

Research question: which unique rewards are leveled, what level gives the maximum useful version, and whether the level locks on pickup, quest completion, or cell entry?

Candidate objective selectors:

* Objective name, subcategory, threshold field, or notes mention `leveled`.
* Associated quest rows that mention leveled reward handling.

Candidate objective IDs:

```text
OBJ-000198, OBJ-001750-OBJ-001772
```

Support inputs:

* `data/objectives/unique-item-reconciliation.md`
* `data/objectives/objectives.csv`
* `data/items/ae-item-members.csv`

Output expectations:

* Record maximum threshold, acquisition/locking event, associated quest/location, warning text needed later, and confidence.
* Link each researched threshold back to objective IDs.
* Feed confirmed cell-entry cases to TB-013.

## TB-013 - Cell-Entry Locks

Research question: which items, quests, or locations can be permanently affected by entering a cell too early, and what exact entry warning must later appear in the route?

Candidate objective selectors:

* `category=location`
* `category=unique_item`
* TB-012 leveled reward queue
* rows whose notes mention first-visit or cell-entry caveats

Candidate objective IDs:

```text
OBJ-000180, OBJ-000198, OBJ-000221, OBJ-000223, OBJ-000226, OBJ-000234, OBJ-000237, OBJ-000242, OBJ-000247,
OBJ-000252, OBJ-000256, OBJ-000265, OBJ-000320, OBJ-000713-OBJ-000759, OBJ-001555-OBJ-001772,
OBJ-001958-OBJ-002424
```

Support inputs:

* `data/locations/location-catalog.csv`
* `data/objectives/unique-item-reconciliation.md`
* `data/items/ae-item-members.csv`
* `data/objectives/activity-favor-reconciliation.md`

Output expectations:

* Separate confirmed cell-entry locks from pickup locks, quest-stage locks, and no-lock cases.
* Preserve enough location detail for later warning placement.
* Do not decide route order beyond the minimum safe-entry rule.

## TB-014 - Quest Conflicts, Missables, and Hard Saves

Research question: where can choices, quest states, branch paths, NPC outcomes, or irreversible actions block completion, branch coverage, trophies, or preserved rewards?

Candidate objective selectors:

* `route_placement=branch_route`, `option_list`, or `excluded`
* `routing_rigidity=branch_only`, `option_list`, or `excluded_unbounded`
* `quest_conflicts` is populated
* `missability=possible` or `confirmed`
* rows mentioning branch, choice, outcome, artifact-safe handling, hard saves, or mutual exclusivity

Candidate objective IDs:

```text
OBJ-000019, OBJ-000053-OBJ-000068, OBJ-000072-OBJ-000074, OBJ-000076, OBJ-000080, OBJ-000084,
OBJ-000087-OBJ-000101, OBJ-000109-OBJ-000111, OBJ-000165, OBJ-000167-OBJ-000169, OBJ-000171, OBJ-000172,
OBJ-000174, OBJ-000175, OBJ-000179-OBJ-000186, OBJ-000189, OBJ-000193, OBJ-000196, OBJ-000199, OBJ-000201,
OBJ-000207, OBJ-000209, OBJ-000213, OBJ-000216, OBJ-000219-OBJ-000223, OBJ-000225-OBJ-000227, OBJ-000229,
OBJ-000230, OBJ-000232-OBJ-000247, OBJ-000249, OBJ-000250, OBJ-000252-OBJ-000256, OBJ-000261-OBJ-000267,
OBJ-000273, OBJ-000274, OBJ-000276-OBJ-000280, OBJ-000282-OBJ-000284, OBJ-000286, OBJ-000296-OBJ-000300,
OBJ-000302-OBJ-000304, OBJ-000306, OBJ-000307, OBJ-000309, OBJ-000310, OBJ-000312, OBJ-000316-OBJ-000321,
OBJ-000325-OBJ-000335, OBJ-000353, OBJ-000356, OBJ-000357, OBJ-000360, OBJ-000364, OBJ-000374-OBJ-000383,
OBJ-000385, OBJ-000390, OBJ-000391, OBJ-000395-OBJ-000412, OBJ-000420, OBJ-000423, OBJ-000424, OBJ-000434,
OBJ-000436, OBJ-000437, OBJ-000439, OBJ-000441, OBJ-000443, OBJ-000447, OBJ-000449, OBJ-000452,
OBJ-000454-OBJ-000459, OBJ-000461, OBJ-000462, OBJ-000465, OBJ-000469, OBJ-000472, OBJ-000476, OBJ-000535,
OBJ-000553-OBJ-000658, OBJ-000663, OBJ-000713-OBJ-000759, OBJ-000764, OBJ-000776, OBJ-000783,
OBJ-000788-OBJ-000801, OBJ-000805-OBJ-000807, OBJ-000811, OBJ-000815-OBJ-000818, OBJ-001065-OBJ-001070,
OBJ-001079-OBJ-001082, OBJ-001275, OBJ-001555-OBJ-001749, OBJ-001797, OBJ-001837, OBJ-001892,
OBJ-001919-OBJ-001957, OBJ-002216, OBJ-002217, OBJ-002238, OBJ-002263, OBJ-002272, OBJ-002322, OBJ-002329,
OBJ-002334, OBJ-002397, OBJ-002405, OBJ-002425-OBJ-002464, OBJ-002498, OBJ-002521-OBJ-002523, OBJ-002525,
OBJ-002526, OBJ-002626, OBJ-002711-OBJ-002751, OBJ-002753-OBJ-002757, OBJ-002765, OBJ-002768-OBJ-002772
```

Support inputs:

* `docs/guide-specification.md`
* `data/objectives/unique-item-reconciliation.md`
* `data/objectives/activity-favor-reconciliation.md`
* `data/npc/relationship-options.csv`
* `data/properties/property-details.csv`
* `data/items/ae-item-members.csv`

Output expectations:

* Produce a conflict/hard-save table with branch policy, canonical choice, alternate branch treatment, and reload point.
* Distinguish full branch routes from option-list choices.
* Do not create branch route prose yet.

## TB-015 - PS4 Trophy Dependencies and Risks

Research question: what does each PS4 trophy require in the PS4 AE setup, and which objectives are trophy dependencies, trophy risks, or trophy counters?

Candidate objective selectors:

* `category=trophy`
* `trophy_relevance` is populated
* checklist/notes mention trophy relevance

Candidate objective IDs:

```text
OBJ-000001, OBJ-000003, OBJ-000005, OBJ-000008, OBJ-000010, OBJ-000012, OBJ-000014, OBJ-000017, OBJ-000018,
OBJ-000020, OBJ-000022, OBJ-000025, OBJ-000028, OBJ-000032, OBJ-000035, OBJ-000037, OBJ-000046, OBJ-000047,
OBJ-000053, OBJ-000055, OBJ-000060, OBJ-000066, OBJ-000067, OBJ-000070, OBJ-000080, OBJ-000084, OBJ-000086,
OBJ-000087, OBJ-000094, OBJ-000099, OBJ-000101, OBJ-000165-OBJ-000414, OBJ-000417, OBJ-000419-OBJ-000422,
OBJ-000424, OBJ-000436, OBJ-000441, OBJ-000447, OBJ-000460-OBJ-000463, OBJ-000466, OBJ-000473-OBJ-000478,
OBJ-000760-OBJ-000909, OBJ-001064-OBJ-001070, OBJ-001773, OBJ-001892, OBJ-001919-OBJ-001925, OBJ-001945,
OBJ-001947, OBJ-001956-OBJ-002443, OBJ-002465-OBJ-002755, OBJ-002758, OBJ-002761, OBJ-002762,
OBJ-002764-OBJ-002772
```

Support inputs:

* `sources/source-notes/SN-000002-main-quest-trophies.md`
* `sources/source-notes/SN-000010-civil-war-trophies-season-unending.md`
* `sources/source-notes/SN-000016-daedric-trophy-and-artifact-risks.md`
* `sources/source-notes/SN-000020-sideways-trophy-caveats.md`
* `sources/source-notes/SN-000022-hero-of-the-people-misc-objective-caveats.md`
* `sources/source-notes/SN-000028-dawnguard-trophy-caveats.md`
* `sources/source-notes/SN-000030-hearthfire-trophy-adoption.md`
* `sources/source-notes/SN-000033-dragonborn-trophy-system-objectives.md`
* `sources/source-notes/SN-000081-skill-perk-foundation.md`
* `sources/source-notes/SN-000086-practical-crafting-system-reconciliation.md`
* `sources/source-notes/SN-000089-activity-favor-boundary-reconciliation.md`

Output expectations:

* Verify PS4 AE trophy behavior from current sources.
* Capture trophy counters, branch-risk interactions, trophy-disabling setup warnings, and hard-save needs.
* Do not infer PS4 behavior from PC, modded, or memory-only sources.

## TB-016 - NPC Dependencies

Research question: which NPCs must stay alive, accessible, non-hostile, unblocked by quest state, or assigned to a role for quests, property, training, marriage, adoption, investment, titles, rewards, or route convenience?

Candidate objective selectors:

* `npc_dependencies` is populated
* `category=npc_relationship`, `property`, or `pet_mount`
* merchant investment rows
* no-journal favor/brawl rows
* rows mentioning NPC, follower, spouse, steward, housecarl, marriage, adoption, investment, trainer, thane, relationship, or disposition

Candidate objective IDs:

```text
OBJ-000167-OBJ-000172, OBJ-000174-OBJ-000179, OBJ-000182-OBJ-000187, OBJ-000191, OBJ-000202, OBJ-000210,
OBJ-000212, OBJ-000213, OBJ-000221-OBJ-000335, OBJ-000348-OBJ-000351, OBJ-000355, OBJ-000373,
OBJ-000390-OBJ-000397, OBJ-000403-OBJ-000412, OBJ-000423-OBJ-000425, OBJ-000427-OBJ-000440,
OBJ-000442-OBJ-000459, OBJ-000464, OBJ-000465, OBJ-000468-OBJ-000470, OBJ-000476, OBJ-000494, OBJ-000537,
OBJ-000659-OBJ-000691, OBJ-000802, OBJ-000805, OBJ-000806, OBJ-000815-OBJ-000908, OBJ-001075-OBJ-001078,
OBJ-001081-OBJ-001083, OBJ-001431, OBJ-001510, OBJ-001553, OBJ-001554, OBJ-001919-OBJ-001957,
OBJ-002717-OBJ-002750, OBJ-002753, OBJ-002754, OBJ-002756, OBJ-002757, OBJ-002759, OBJ-002760,
OBJ-002762-OBJ-002772
```

Support inputs:

* `data/npc/relationship-options.csv`
* `data/properties/property-details.csv`
* `data/skills/merchant-investment-catalog.csv`
* `data/objectives/activity-favor-reconciliation.md`
* `data/objectives/unique-item-reconciliation.md`

Output expectations:

* Produce NPC dependency rows with objective links, required state, risk, and mitigation.
* Keep recommendation choices separate from hard requirements.
* Feed spouse, child, steward, base, Black Book, and transformation recommendation questions to later writer-recommendation work, not route prose.

## TB-017 - Bug-Prone Quests and Mitigations

Research question: which objectives have known bugs that require order constraints, hard saves, avoid-early-collection warnings, or alternate completion methods on PS4 AE?

Candidate objective selectors:

* `bug_risk=possible` or `confirmed`
* notes mention bug, glitch, stuck state, unavailable state, avoid-early-collection, or first-visit availability

Candidate objective IDs:

```text
OBJ-000067, OBJ-000109-OBJ-000111, OBJ-000182-OBJ-000187, OBJ-000202, OBJ-000220-OBJ-000223,
OBJ-000225-OBJ-000227, OBJ-000229, OBJ-000230, OBJ-000232, OBJ-000234, OBJ-000236-OBJ-000239,
OBJ-000241-OBJ-000245, OBJ-000247, OBJ-000249, OBJ-000252-OBJ-000254, OBJ-000256, OBJ-000261-OBJ-000267,
OBJ-000274, OBJ-000276, OBJ-000278-OBJ-000280, OBJ-000282-OBJ-000284, OBJ-000298, OBJ-000299, OBJ-000304,
OBJ-000306, OBJ-000316, OBJ-000320, OBJ-000321, OBJ-000326, OBJ-000327, OBJ-000329-OBJ-000335, OBJ-000407,
OBJ-000409-OBJ-000412, OBJ-000424, OBJ-000436, OBJ-000448, OBJ-000449, OBJ-000454, OBJ-000455, OBJ-000464,
OBJ-000465, OBJ-000476, OBJ-000477, OBJ-000553-OBJ-000658, OBJ-000662, OBJ-000677, OBJ-000678, OBJ-000774,
OBJ-000780, OBJ-000804, OBJ-000809, OBJ-000819-OBJ-001063, OBJ-001079, OBJ-001827-OBJ-001835,
OBJ-001837-OBJ-001841, OBJ-001848, OBJ-001879, OBJ-001881, OBJ-001919-OBJ-001925, OBJ-001947-OBJ-001949,
OBJ-001951-OBJ-001953, OBJ-001956, OBJ-001958-OBJ-002407, OBJ-002627, OBJ-002644, OBJ-002717, OBJ-002753,
OBJ-002754, OBJ-002769-OBJ-002772
```

Support inputs:

* `data/locations/location-catalog.csv`
* `data/books/*-locations.csv`
* `data/items/ae-item-members.csv`
* `data/properties/property-details.csv`
* `data/skills/*-catalog.csv`

Output expectations:

* Distinguish confirmed PS4 AE risks from PC-only, USSEP-only, or source-uncertain bugs.
* Convert only confirmed/likely relevant bugs into later hard-save or ordering constraints.

## TB-018 - Radiant Quest Boundaries

Research question: which radiant/repeatable objectives are required, finite, representative-only, unlock-gated, trophy-relevant, or excluded after all meaningful rewards/unlocks are exhausted?

Candidate objective selectors:

* `category=radiant`
* subcategory, notes, or start trigger mention radiant
* TB-010A representative no-journal activity/favor rows

Candidate objective IDs:

```text
OBJ-000026, OBJ-000048, OBJ-000102-OBJ-000116, OBJ-000121-OBJ-000128, OBJ-000134-OBJ-000140, OBJ-000161,
OBJ-000162, OBJ-000221-OBJ-000223, OBJ-000225-OBJ-000227, OBJ-000229, OBJ-000230, OBJ-000232, OBJ-000234,
OBJ-000236-OBJ-000239, OBJ-000241-OBJ-000245, OBJ-000247, OBJ-000249, OBJ-000252-OBJ-000254, OBJ-000256,
OBJ-000261-OBJ-000267, OBJ-000274, OBJ-000278-OBJ-000280, OBJ-000282-OBJ-000284, OBJ-000317, OBJ-000320,
OBJ-000321, OBJ-000327, OBJ-000329-OBJ-000335, OBJ-000365, OBJ-000367-OBJ-000378, OBJ-000380-OBJ-000383,
OBJ-000412, OBJ-000438, OBJ-000816, OBJ-002762-OBJ-002767
```

Support inputs:

* `data/objectives/activity-favor-reconciliation.md`
* `data/npc/relationship-options.csv`
* `data/properties/property-details.csv`
* `data/skills/merchant-investment-catalog.csv`

Output expectations:

* Mark each row as required, finite chain, representative type, unlock gate, branch-only, or excluded repetition.
* Record exact minimum count where needed, such as faction restoration or trophy counters.
* Do not route exact targets unless source evidence makes target selection part of the constraint.

## TB-019 - Survival Mode Constraints

Research question: what travel, cold, food, rest, storage, carry-weight, carriage/ferry, camping, home, pet/mount, and regional sequencing constraints must shape the route before route anchors are built?

Candidate objective selectors:

* `survival_mode_relevance` is populated
* `category=location`, `property`, or `pet_mount`
* official DLC rows that likely affect geography or survival logistics

Candidate objective IDs:

```text
OBJ-000182-OBJ-000186, OBJ-000221-OBJ-002767
```

Support inputs:

* `data/locations/location-catalog.csv`
* `data/properties/property-details.csv`
* `data/npc/relationship-options.csv`
* `data/items/ae-item-members.csv`
* `data/books/*-locations.csv`

Output expectations:

* Produce route-shaping regions, cold-risk areas, early safe-storage options, travel networks, food/rest/carry implications, and no-fast-travel assumptions.
* Keep exact route order for later route-skeleton phases.

## TB-020 - Skill, Perk, Leveling, and Crafting Constraint Plan

Research question: what skill, perk, perk-point, crafting, enchantment, alchemy, investment, material, and leveling constraints must exist before progression planning can be integrated into the route?

Candidate objective selectors:

* `category=skill_perk` or `crafting_unlock`
* crafting trophy rows
* rows mentioning skills, perks, alchemy, enchanting, smithing, crafting, investment, training, leveling, or Legendary resets

Candidate objective IDs:

```text
OBJ-000122, OBJ-000129-OBJ-000133, OBJ-000184-OBJ-000186, OBJ-000282, OBJ-000285, OBJ-000295, OBJ-000296,
OBJ-000322, OBJ-000348-OBJ-000350, OBJ-000407, OBJ-000425, OBJ-000428, OBJ-000431, OBJ-000436, OBJ-000441,
OBJ-000442, OBJ-000446, OBJ-000453, OBJ-000458, OBJ-000464, OBJ-000469, OBJ-000476, OBJ-000490, OBJ-000491,
OBJ-000515, OBJ-000532, OBJ-000539, OBJ-000542, OBJ-000563, OBJ-000635, OBJ-000637, OBJ-000659,
OBJ-000661-OBJ-000668, OBJ-000692, OBJ-000696-OBJ-000699, OBJ-000704-OBJ-000712, OBJ-000788, OBJ-000795,
OBJ-000814-OBJ-000817, OBJ-000819-OBJ-000909, OBJ-001064, OBJ-001070, OBJ-001079, OBJ-001189, OBJ-001379,
OBJ-001392, OBJ-001413, OBJ-001418, OBJ-001423, OBJ-001471, OBJ-001485, OBJ-001549, OBJ-001730, OBJ-001780,
OBJ-001788, OBJ-001789, OBJ-001794, OBJ-001919-OBJ-001925, OBJ-002425-OBJ-002755, OBJ-002760, OBJ-002765
```

Support inputs:

* `data/skills/skill-perk-catalog.csv`
* `data/skills/perk-rank-catalog.csv`
* `data/skills/enchantment-learning-catalog.csv`
* `data/skills/alchemy-effect-catalog.csv`
* `data/skills/merchant-investment-catalog.csv`
* `data/skills/practical-crafting-system-catalog.csv`
* `data/objectives/activity-favor-reconciliation.md`
* `data/objectives/unique-item-reconciliation.md`

Output expectations:

* Wait for TB-012 and TB-019 before finalizing level/crafting timing.
* Separate hard requirements from writer recommendations and efficiency choices.
* Keep exploit decisions explicit, bounded, trophy-safe, and deferred until researched.

## Phase 2 Gate

TB-010B closes Phase 1 source-list objective database setup. Phase 2 can begin after this index exists, but route construction remains blocked until TB-021 completes the constraint-table consistency review.
