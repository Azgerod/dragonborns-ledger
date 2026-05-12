# Source Note: Hearthfire Construction and Service Detail Expansion

Status: needs review.

Source note ID: SN-000075

## Claim

The property detail table now carries source-backed Hearthfire rows for homestead land summaries, construction modules, exterior additions, wing choices, steward furnishing costs, steward material purchases, household services, livestock services, and construction bug-warning follow-up.

## Routing Relevance

The specification requires Hearthfire land acquisition, house building, full furnishing, adoption support, related trophies, Survival Mode logistics, and service/role choices. Hearthfire construction also creates major material, gold, storage, crafting, family, and travel-planning constraints. These rows support later route placement and material planning without choosing final wing layouts or writing guide instructions.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000063 | Skyrim:Houses | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Houses | 2026-05-12 | Hearthfire homestead summaries, land prices, housecarls, and unique exterior features. |
| SRC-000032 | Skyrim:Construction | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Construction | 2026-05-12 | Construction modules, material totals, room/wing options, steward furnishing costs, material-service notes, achievements, and construction/furnishing bug cautions. |
| SRC-000245 | Skyrim:Personal Steward | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Personal_Steward | 2026-05-12 | Steward improvements, carriage/bard/horse/livestock services, building material purchases, furnishing-service behavior, and steward permanence note. |

## Evidence Summary

UESP's Houses page lists Lakeview Manor, Windstad Manor, and Heljarchen Hall as Hearthfire houses with 5,000 gold land purchase cost, relevant housecarls, and unique exterior options: Lakeview apiary, Windstad fish hatchery, and Heljarchen grain mill.

UESP's Construction page gives material totals for Small House Layout, Main Hall, Cellar, Aquarium, exterior additions, and all three choices for each wing. It also states that Master Architect requires all three wings on each of the three houses, and that steward furnishing can cover most house sections over time while Cellar furnishings must be self-built.

UESP's Personal Steward page lists Hearthfire steward services: carriage driver, bard, horse, cow, chickens, lumber, stone, clay, material-store direction, and room furnishing. It also notes that steward furnishing is gradual and eventually adds all possible furnishings for the paid section.

## Confidence and Open Questions

Confidence is high for source-listed Hearthfire construction, service, and material rows. TB-031D selects the default wing layout, Hearthfire steward/service policy, and family-base direction. Later passes must still decide exact material procurement route, self-build details for checklist-sensitive furnishings, trophy timing on PS4, construction bug mitigations, and final safe-storage validation.

## Linked Records

`data/properties/property-details.csv`, `OBJ-000395` through `OBJ-000408`, `OBJ-001948` through `OBJ-001950`, and `OBJ-001954`.
