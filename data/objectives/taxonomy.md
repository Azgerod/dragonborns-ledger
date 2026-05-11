# Objective Taxonomy

This taxonomy translates the requirements into planned objective-database row types. It contains no gameplay facts and should not be treated as objective data.

`objectives.csv` should stay header-only until researched rows can include source-note citations.

## Row Granularity

Use one row for each objective unit that needs independent routing, checklist mapping, validation, or warning behavior.

| Objective unit | Row rule |
| --- | --- |
| Questline | Use one row for the questline only when it is useful as a parent/planning row; use separate rows for routed quests or materially distinct objectives. |
| Quest | Use one row per named quest when the quest has a distinct completion boundary, reward, conflict, trophy relevance, or route placement. |
| Quest stage/objective | Use a separate row only when the stage has its own stop point, hard save, missable, level gate, checklist cue, or branch consequence. |
| Collectible set | Use one parent row for set-level completion when needed, plus member rows when each member needs placement or checklist mapping. |
| Unique reward | Use one row when the reward needs preservation, level-gate, branch, or checklist handling independent of its quest. |
| Location | Use one row for discovery and/or clear state when the guide must route it explicitly. |
| System completion | Use one row for bounded systems such as all perks, all alchemy effects, all enchantments, or merchant investments when they need global validation. |
| Option choice | Use one row for the option set, not one row per option, unless an option has material route consequences. |
| Branch-only content | Use rows only for branch-exclusive objectives; common objectives stay in main-route rows. |
| Exclusion | Use rows only when an exclusion needs later audit, checklist reconciliation, or explicit justification. |

## Category Map

| Category | Planned subcategories | Requirement coverage | Default row granularity | Research entry point |
| --- | --- | --- | --- | --- |
| `quest` | main quest, faction quest, DLC quest, Daedric quest, side quest, AE quest, branch quest | Main quest, guild/faction questlines, Daedric quests, DLC quests, AE quests, named side quests | Named quest or material quest stage | Quest objective research |
| `misc_objective` | favor, local objective, finite miscellaneous quest, bounded task | Finite miscellaneous quests and favors that are reasonably trackable | One row per trackable objective | Quest objective research |
| `trophy` | trophy, trophy dependency, trophy risk | All PS4 trophies and trophy preservation | One row per trophy or dependency when useful | Trophy dependency research |
| `ae_creation` | creation package, creation quest, creation system, creation reward group | Official AE Creation Club bundle quests, systems, locations, homes, pets, items, spells, ingredients, rewards | Creation package parent row plus child rows as needed | AE Creation research |
| `location` | discovered location, clearable location, non-clearable location, worldspace cleanup | All map-marked locations discovered and clearable locations cleared where possible | One row per routed location state | Location research |
| `collectible` | Stones, masks, claws, maps, insects, paragons, plants, fishing, other finite sets | All finite collectible sets and checklist-tracked collectibles | Parent set row plus member rows when routed individually | Collectible research |
| `unique_item` | artifact, leveled reward, named reward, branch reward, preserved item | All unique items obtainable on the main route and best-tier leveled rewards | One row per item when preservation, level gate, or branch matters | Unique item and leveled reward research |
| `property` | city home, Hearthfire land/home, AE home, farm, furnishing, upgrade | All player homes, land, farm, upgrades, and furnishings | One row per property/unlock/upgrade group as routing requires | Property research |
| `pet_mount` | pet, horse, mount, creature unlock | All pets and mounts obtainable on the main route | One row per unlock when route-relevant | Pet and mount research |
| `npc_relationship` | thane, housecarl, follower, spouse, steward, bard, carriage driver, farmhand, title | Thaneships, housecarls, follower/pet/mount/steward/spouse lists, faction ranks, titles, major relationship unlocks | One row per unlock or option set | NPC and role-assignment research |
| `spell_power` | spell, spell tome, power, ability, transformation, Black Book power | Permanent spells, powers, abilities, transformations, Black Book powers, spell tomes | One row per learnable/unlock or option set | Spell/power research |
| `skill_perk` | skill 100, perk set, perk point, Legendary reset, grind block | All skills to 100 and all perks acquired | One row per skill/system milestone or validation objective | Skill/perk planning |
| `crafting_unlock` | enchantment, alchemy effect, recipe/system knowledge, merchant investment | Enchantments, alchemy effects, practical crafting unlocks, merchant investments | One row per unlock type/member when checklist-routed; parent rows for global validation | Crafting research |
| `radiant` | required radiant, finite chain, representative type, excluded repetition | Required radiants, faction restoration, finite endpoints, representative completion | One row per required chain/type and representative category | Radiant boundary research |
| `book_document` | skill book, spell tome, Black Book, quest document, AE document, unique checklist book/note | Required book/document policy | One row per routed document or set parent | Book/document research |
| `system` | setup, save hygiene, checklist sync, hard-save policy, validation objective | Setup rule, save policy, checklist synchronization, QA requirements | Use sparingly for guide-system requirements that need route/checklist handling | Process and guide-structure work |

## Source Content Map

| `source_content` value | Use for |
| --- | --- |
| `base_game` | Base-game objectives. |
| `dawnguard` | Dawnguard objectives. |
| `hearthfire` | Hearthfire objectives. |
| `dragonborn` | Dragonborn objectives. |
| `ae_creation` | Official AE Creation Club bundle objectives. |
| `multiple` | Objectives spanning multiple allowed content sources. |
| `not_applicable` | Process/system rows that are not gameplay objectives. |

## Initial Research Batches

These batches describe how to populate the database later. They are not objective rows.

| Batch | Purpose | Primary categories | Must cite before row entry |
| --- | --- | --- | --- |
| Setup/system rows | Capture guide setup, save hygiene, and checklist synchronization only if needed in the database. | `system` | No gameplay citations needed unless a setup claim affects trophy behavior. |
| Trophy framework | Identify trophies and trophy dependencies that affect routing. | `trophy`, `quest`, `radiant`, `property`, `skill_perk` | PS4 trophy behavior and dependencies. |
| Base/DLC quest framework | Identify named quests, finite miscellaneous objectives, faction arcs, and branch candidates. | `quest`, `misc_objective`, `radiant` | Quest starts, prerequisites, conflicts, missables, and rewards. |
| AE framework | Identify official AE bundle content and its quest/system/reward structure. | `ae_creation`, plus child objective categories | AE bundle membership, start triggers, level gates, rewards, and conflicts. |
| Location framework | Identify map-marked and clearable location objectives. | `location` | Discovery/clearability and route-relevant access constraints. |
| Collectible/framework items | Identify collectible sets, unique items, books, spells, powers, crafting unlocks, pets, mounts, homes, and relationships. | `collectible`, `unique_item`, `book_document`, `spell_power`, `crafting_unlock`, `property`, `pet_mount`, `npc_relationship` | Member lists, acquisition rules, conflicts, and checklist mapping. |
| Progression framework | Identify all-skills/all-perks and crafting/leveling objectives. | `skill_perk`, `crafting_unlock` | Perk accounting, skill leveling assumptions, exploit safety if any. |

## Route Placement Defaults

| Requirement type | Default `route_placement` before research | Notes |
| --- | --- | --- |
| Canonical required content | `main_route` | Use only when the requirement is already user-decided and not mutually exclusive. |
| Mutually exclusive substantial content | `branch_route` | Branch routes should contain only branch-exclusive content. |
| Isolated preference choices | `option_list` | Applies to spouse, adopted children, stewards, decoration, and similar non-propagating choices unless research finds material consequences. |
| Exhaustive reference data | `appendix` | Appendices verify data; main route still tells the player when to act. |
| Infinite, arbitrary, non-trophy-safe, or out-of-scope content | `excluded` | Exclusions need justification when they touch checklist coverage or completion expectations. |
| Unknown or unresearched content | `unclassified` | Use until source-backed placement is possible. |

## Open Questions For First Research Pass

* Which checklist spreadsheet fields are available for `checklist_mapping`?
* Should parent rows and member rows both appear in coverage validation, or should parent rows be marked `appendix`/`not_applicable` for checklist mapping?
* Which objective categories should be researched first once gameplay research begins: trophies, AE bundle membership, or broad quest inventory?
