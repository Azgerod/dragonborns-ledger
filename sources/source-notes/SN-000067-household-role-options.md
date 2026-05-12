# Source Note: Household Role Options

Status: researched; TB-031D defaults added.

Source note ID: SN-000067

## Claim

Spouse, adopted-child, personal-steward, homestead-bard, carriage-service, and Goldenhills farmhand choices should be tracked as option lists rather than hard-save branch routes. TB-031D records the main-route defaults while preserving the remaining candidates for TB-035 option-list presentation.

## Routing Relevance

The specification says isolated role-assignment choices should be listed with a later default recommendation instead of fully branched. The objective rows and `data/npc/relationship-options.csv` preserve the full candidate surface for later recommendation, NPC-dependency, property, family-home, and checklist passes without prematurely deciding final household defaults.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000244 | Skyrim:Marriage | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Marriage | 2026-05-12 | Lists marriage process, benefits, spouse property, and 67 marriage candidates with conditions. |
| SRC-000033 | Skyrim:Adoption | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Adoption | 2026-05-12 | Lists adoptable children, adoption requirements, child pet options, and adoption notes/bugs. |
| SRC-000245 | Skyrim:Personal Steward | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Personal_Steward | 2026-05-12 | Lists steward services and 35 steward candidates across base game, DLC, and AE Creation content. |
| SRC-000246 | Skyrim:Bardic Performances | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Bard | 2026-05-12 | Cross-checks Hearthfire homestead bard performer names. |
| SRC-000031 | Skyrim:Hearthfire | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Hearthfire | 2026-05-11 | Existing Hearthfire overview for steward, carriage driver, bard, family, and pet systems. |
| SRC-000075 | Skyrim:A Farmer's Life For Me | 2 - UESP | https://en.uesp.net/wiki/Skyrim:A_Farmer%27s_Life_For_Me | 2026-05-11 | Existing Goldenhills farm setup source, including steward and farmhand steps. |
| SRC-000247 | Skyrim:Farmhand | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Farmhand | 2026-05-12 | Lists generic Goldenhills farmhands and named farmhand alternatives. |

## Evidence Summary

The Marriage page lists 67 marriage candidates split into female and male NPC tables. The Adoption page lists adoptable children from Honorhall Orphanage and elsewhere, plus child pet options. The Personal Steward page lists steward commands/services, Goldenhills farm services, and 35 candidates who can become stewards. The Bardic Performances page identifies the Hearthfire homestead bards, while Hearthfire and Goldenhills sources establish carriage-driver, bard, steward, and farmhand service categories.

`data/npc/relationship-options.csv` now records these role candidates and services as option-list data rather than individual routed branches. TB-031D marks the selected route defaults in that table and in `data/route-planning/route-default-decisions.md`: Ysolda as spouse, Lucia and Sofie as adopted children, Rayya/Valdimar/Gregor as Hearthfire stewards, Faendal as Goldenhills steward, all Hearthfire bard and carriage services after prerequisites, and generic Goldenhills farmhands.

## Confidence and Open Questions

Confidence is high for source-list candidate membership and TB-031D default selection. Exact route timing, NPC safety, spouse/family movement checks, child-bedroom availability, steward assignment bug mitigation, service-hiring warnings, and non-default option presentation remain downstream work.

## Linked Records

OBJ-000408, OBJ-000410, OBJ-000411, OBJ-001945 through OBJ-001951, and `data/npc/relationship-options.csv`.
