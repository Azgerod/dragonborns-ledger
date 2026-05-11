# Objective Database Schema

This schema defines fields for objective records. It contains no gameplay data.

## CSV Conventions

* Use UTF-8 CSV with the header from `objectives.template.csv`.
* Keep one row per objective or checklist-mapped objective unit.
* Leave unknown values blank until researched; use `not_applicable` only when the field cannot apply.
* For multi-value cells, separate values with ` | `.
* Put routing-relevant factual support in source notes and reference those notes in `citations`.
* Do not place final guide prose in this database.

## Objective IDs

Use stable local IDs in this format:

`OBJ-000001`

Rules:

* Assign IDs sequentially.
* Never reuse an ID after deleting or merging a row.
* Do not encode category, route placement, source content, or research status in the ID; those values can change during research.
* Use `objective_name`, `category`, `subcategory`, and `checklist_mapping` for human meaning.

## Fields

| Field | Required | Purpose |
| --- | --- | --- |
| `objective_id` | Yes | Stable local identifier used for cross-references. |
| `objective_name` | Yes | Objective, quest, item, location, trophy, system, or checklist entry name. |
| `category` | Yes | Broad objective type. See controlled values below. |
| `subcategory` | No | More specific type within the category, such as faction, collectible set, reward type, or system type. |
| `source_content` | Yes | Content source: base game, official DLC, or official AE Creation content. |
| `worldspace` | No | Worldspace or major map context used for routing. |
| `region` | No | Region, island, broad travel area, or route-planning area. |
| `hold` | No | Hold or local political area when applicable. |
| `location` | No | Specific start, completion, or acquisition location when known. |
| `start_trigger` | No | How the objective becomes available. |
| `prerequisites` | No | Required level, quest state, faction state, item, NPC, system unlock, or other prerequisite. |
| `completion_boundary` | No | What counts as complete for the route and checklist. |
| `recommended_level` | No | Recommended level when relevant for difficulty, pacing, or survival. |
| `hard_level_gate` | No | Required level gate that must not be violated. |
| `leveled_reward_threshold` | No | Level needed for the desired or maximum reward tier. |
| `cell_entry_lock_risk` | No | Whether entering a cell early can lock reward tier, state, or availability. Use controlled risk values. |
| `quest_conflicts` | No | Quest, faction, branch, or outcome conflicts affecting routing. |
| `npc_dependencies` | No | NPCs required for access, rewards, training, property, investment, marriage, faction progress, or other objectives. |
| `trophy_relevance` | No | Trophy dependency, trophy progress, or trophy-risk note. |
| `checklist_mapping` | No | Spreadsheet tab, row, category, or other checklist reference. |
| `unique_rewards` | No | Unique rewards or unique items tied to the objective. |
| `missability` | No | Missable or permanence risk. Use controlled risk values. |
| `bug_risk` | No | Bug risk and mitigation requirement. Use controlled risk values. |
| `survival_mode_relevance` | No | Hunger, fatigue, cold, carry, sleep, travel, restock, food, warmth, camping, home, carriage, ferry, or safe-storage relevance. |
| `routing_rigidity` | Yes | How rigidly the objective must be placed. Use controlled routing-rigidity values. |
| `route_placement` | Yes | Whether the objective belongs to the main route, branch route, option list, appendix, excluded scope, or remains unclassified. |
| `citations` | No | Source-note references supporting routing-relevant factual claims. |
| `research_status` | Yes | Research state for the row. Use controlled status values. |
| `validation_status` | Yes | Validation state for the row. Use controlled status values. |
| `notes` | No | Short reviewer-facing notes, assumptions, or open questions. |

## Controlled Values

### `category`

Use the closest broad category. Add a new category only when an objective cannot be represented by these values.

| Value | Meaning |
| --- | --- |
| `quest` | Named quest or finite quest objective. |
| `misc_objective` | Trackable miscellaneous quest, favor, or local objective. |
| `trophy` | PS4 trophy or trophy dependency. |
| `ae_creation` | AE Creation quest, system, reward group, or content package. |
| `location` | Map-marked location discovery or clear state. |
| `collectible` | Collectible set member or collectible-set completion objective. |
| `unique_item` | Unique item, artifact, or preserved named reward. |
| `property` | Home, land, furnishing, farm, or upgrade objective. |
| `pet_mount` | Pet, mount, or related unlock. |
| `npc_relationship` | Thaneship, housecarl, follower, spouse, steward, bard, carriage driver, farmhand, title, or relationship unlock. |
| `spell_power` | Spell, spell tome, power, ability, transformation, or Black Book power. |
| `skill_perk` | Skill level, perk, perk-point, or Legendary-reset objective. |
| `crafting_unlock` | Enchantment, alchemy effect, recipe, crafting system, or merchant investment objective. |
| `radiant` | Required, finite, or representative radiant objective. |
| `book_document` | Skill book, spell tome, Black Book, quest document, AE document, or checklist-tracked unique book/note. |
| `system` | Setup, save hygiene, checklist synchronization, or other non-gameplay system objective needed by the guide. |

### `source_content`

| Value | Meaning |
| --- | --- |
| `base_game` | Base Skyrim content. |
| `dawnguard` | Official Dawnguard content. |
| `hearthfire` | Official Hearthfire content. |
| `dragonborn` | Official Dragonborn content. |
| `ae_creation` | Official Anniversary Edition / Anniversary Upgrade Creation Club bundle content. |
| `multiple` | Objective spans multiple allowed content sources. |
| `not_applicable` | Non-gameplay planning or system row. |

### Risk Fields

Use these for `cell_entry_lock_risk`, `missability`, and `bug_risk`.

| Value | Meaning |
| --- | --- |
| `none_known` | No relevant risk found in researched sources. |
| `possible` | Risk is plausible or source evidence is incomplete. |
| `confirmed` | Risk is confirmed and must affect routing. |
| `unknown` | Not yet researched. |
| `not_applicable` | Field does not apply. |

### `routing_rigidity`

| Value | Meaning |
| --- | --- |
| `fixed_early` | Must be done early for safety, access, or pacing. |
| `fixed_late` | Must be delayed for reward tier, difficulty, lore gravity, or safety. |
| `windowed` | Must occur within a level, quest, faction, or state window. |
| `region_flexible` | Can be done whenever the route is nearby. |
| `dependency_flexible` | Can be done once prerequisites are satisfied. |
| `branch_only` | Belongs only to an alternate branch route. |
| `option_list` | Isolated player choice, not a routed branch. |
| `cleanup_safe` | Can be safely deferred to cleanup. |
| `excluded_unbounded` | Explicitly excluded, impossible, unbounded, or outside scope. |
| `unclassified` | Not yet classified. |

### `route_placement`

| Value | Meaning |
| --- | --- |
| `main_route` | Belongs in the canonical main route. |
| `branch_route` | Belongs in a hard-save branch. |
| `option_list` | Presented as an option/recommendation, not a branch. |
| `appendix` | Tracked or verified in an appendix/table rather than routed as a standalone step. |
| `excluded` | Explicitly excluded with justification. |
| `unclassified` | Not yet placed. |

### Status Fields

Use these for `research_status` and `validation_status`.

| Value | Meaning |
| --- | --- |
| `not_started` | No research or validation work has been done. |
| `in_progress` | Work is underway but incomplete. |
| `needs_sources` | Gameplay claim needs citations before use. |
| `needs_review` | Ready for human or later QA review. |
| `validated` | Checked against the relevant source notes or downstream validation pass. |
| `blocked` | Waiting on another artifact, checklist input, or unresolved decision. |
| `not_applicable` | Field does not apply to this row. |
