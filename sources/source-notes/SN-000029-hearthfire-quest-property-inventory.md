# Source Note: Hearthfire Quest and Property Inventory

Status: needs review.

Source note ID: SN-000029

## Claim

The Hearthfire inventory should cover land-permission objectives, the `Build Your Own Home` quest, the three homestead properties, construction stage objectives, full home furnishing, staff/service option handling, and the source-listed `Bandit Attack` radiant. The route should not treat isolated role-assignment choices as hard branches.

## Routing Relevance

Hearthfire is required by the specification for land acquisition, house building, furnishing, adoption, and related trophies. These rows give later property, NPC, trophy, Survival Mode, and bug-risk passes stable records without prematurely choosing exact wing layouts, children, stewards, bards, carriage drivers, spouse home, or final furnishing strategy.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000027 | Bethesda support: How do I gain the ability to purchase a plot of land in the Hearthfire DLC? | 1 - Bethesda official support | https://help.bethesda.net/app/answers/detail/a_id/18215/~/how-do-i-gain-the-ability-to-purchase-a-plot-of-land-in-the-hearthfire-dlc | 2026-05-11 | Official general land-purchase access rule. |
| SRC-000028 | Bethesda support: In the Hearthfire DLC, what are the specific requirements for getting land in each hold? | 1 - Bethesda official support | https://help.bethesda.net/app/answers/detail/a_id/18216/~/in-the-hearthfire-dlc%2C-what-are-the-specific-requirements-for-getting-land-in | 2026-05-11 | Official hold-specific land-purchase prerequisites. |
| SRC-000029 | Category:Skyrim-Hearthfire-Quests | 2 - UESP | https://en.uesp.net/wiki/Category:Skyrim-Hearthfire-Quests | 2026-05-11 | Lists Hearthfire quest-category pages. |
| SRC-000030 | Skyrim:Build Your Own Home | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Build_Your_Own_Home | 2026-05-11 | Describes the formal house-building quest steps and completion boundary. |
| SRC-000031 | Skyrim:Hearthfire | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Hearthfire | 2026-05-11 | Summarizes Hearthfire houses, adoption, staff, services, and property systems. |
| SRC-000032 | Skyrim:Construction | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Construction | 2026-05-11 | Details construction stages, furnishing, room options, safe storage notes, and bugs. |

## Evidence Summary

Bethesda support states that Hearthfire land purchase requires earning the relevant Jarl's trust and receiving the land-availability letter. Bethesda's hold-specific support article identifies Falkreath requirements as `Rare Gifts` and `Kill the Bandit Leader`, Hjaalmarch as `Laid to Rest`, and Dawnstar as `Waking Nightmare` plus `Kill the Giant`; it also gives `Kill the Giant` a level 22 prerequisite.

UESP's Hearthfire quest category lists 14 Hearthfire quest pages, including `Bandit Attack`, `Build Your Own Home`, three `BYOHHouse...` property trackers, four land-contact objectives, three property-visit objectives, and the drafting-table and carpenter-workbench objectives. This pass keeps user-facing rows for the same objective families instead of exposing internal quest IDs as final guide content.

UESP's `Build Your Own Home` page describes the formal flow as obtaining permission, buying land, visiting the new property, using the drafting table, and building the foundation at the carpenter's workbench. It states that the quest ends after foundation construction while broader construction and furnishing continue afterward.

UESP's Hearthfire and Construction pages describe three purchasable plots for 5000 gold each, the use of raw materials at drafting tables and carpenter's workbenches, staff/services such as stewards, bards, and carriage drivers, and the need to handle room and furnishing choices separately. Construction notes also identify safe construction chests and several building/furnishing bugs, so exact mitigation belongs in the later bug-risk and property passes.

## Confidence and Open Questions

Confidence is high for Hearthfire quest/property inventory and official land prerequisites. Later passes must validate exact PS4 trophy timing, bug mitigations, storage safety, full material requirements, wing-layout recommendations, staff eligibility, adoption home defaults, spouse/family movement, and whether `Bandit Attack` should be routed, appendix-only, or excluded as random/unbounded content.

## Linked Records

OBJ-000390 through OBJ-000408 and OBJ-000412. Existing prerequisite rows affected by this note include OBJ-000191, OBJ-000243, OBJ-000244, and OBJ-000267.
