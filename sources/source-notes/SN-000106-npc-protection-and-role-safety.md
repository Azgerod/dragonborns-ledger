# Source Note: NPC Protection and Role Safety

Status: researched.

Source note ID: SN-000106

## Claim

NPC dependency routing must distinguish essential NPCs, protected NPCs, ordinary killable NPCs, and role-assigned NPCs. Followers and spouses are safer than ordinary NPCs, but protected status is not full invulnerability, and Hearthfire steward assignments are mostly permanent choices.

## Routing Relevance

TB-016 needs a constraint table that prevents route-critical NPC deaths without turning spouse, child, steward, follower, pet, horse, and farmhand preferences into full branch routes. This note supports class-level NPC safety rules and keeps later default recommendations separate from hard requirements.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000389 | Skyrim:Essential NPCs | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Essential_NPCs | 2026-05-12 | Essential status mechanics and named NPC killability windows. |
| SRC-000390 | Skyrim:Protected NPCs | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Protected_NPCs | 2026-05-12 | Protected status mechanics for followers, spouses, and player-caused death risk. |
| SRC-000248 | Skyrim:Followers | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Followers | 2026-05-12 | Permanent follower behavior, protection, death risks, faction prerequisites, and follower option tables. |
| SRC-000244 | Skyrim:Marriage | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Marriage | 2026-05-12 | Marriage prerequisites, spouse benefits, protected spouse status, spouse property, and marriage bugs. |
| SRC-000033 | Skyrim:Adoption | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Adoption | 2026-05-12 | Adoption capacity, child-bedroom requirements, Constance/orphanage path, child pets, and adoption bugs. |
| SRC-000245 | Skyrim:Personal Steward | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Personal_Steward | 2026-05-12 | Steward assignment requirements, permanence, services, Goldenhills exception, and steward bugs. |
| SRC-000247 | Skyrim:Farmhand | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Farmhand | 2026-05-12 | Goldenhills farmhand candidate and service support. |

## Evidence Summary

UESP describes essential NPCs as unkillable while their essential flag is active, while protected NPCs can enter bleedout from non-player damage but can still be killed by a direct player hit. The Followers page similarly says permanent followers are protected while actively following, but can still die from player hits, stray damage during recovery, poison, or damage-over-time. The Marriage page says a spouse becomes protected after marriage, but also records spouse death and no-remarriage risks.

The Marriage, Adoption, Followers, Personal Steward, and Farmhand pages support the existing option-list structure. Marriage requires an eligible NPC with raised disposition and the marriage setup through Maramal. Adoption allows up to two children and requires a valid child bedroom or self-built-house child beds and containers. Personal steward candidates must be recruited as followers and brought to a qualifying property; Hearthfire steward assignment is permanent for that homestead, while Goldenhills Plantation stewards can be fired and rehired. Steward services also affect carriage, bard, horse, livestock, materials, furnishings, and Goldenhills farm income.

## Confidence and Open Questions

Confidence is high for class-level NPC safety rules and option-list treatment. Later tasks still need to choose default spouse, children, stewards, farmhands, followers, household pets, and home base; TB-017 still needs bug-specific mitigation for steward, adoption, spouse, and follower issues; TB-019 must account for Survival Mode travel value of homes, horses, pets, and carriage services.

## Linked Records

`data/constraints/npc-dependencies.md`, `data/npc/relationship-options.csv`, OBJ-001945 through OBJ-001954, OBJ-000408, OBJ-000410, OBJ-000411, and OBJ-000663.
