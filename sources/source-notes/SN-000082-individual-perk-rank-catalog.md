# Source Note: Individual Perk-Rank Catalog

Status: needs review.

Source note ID: SN-000082

## Claim

The 18 Skyrim skill-tree pages list the individual perk nodes and perk ranks needed to complete all perks. Together, those pages support a 180-node, 251-rank perk catalog with source-listed skill requirements, prerequisite perks, descriptions, and form IDs.

## Routing Relevance

The specification requires all perks. The route cannot plan perk allocation, Legendary resets, level checkpoints, merchant investments, or crafting-system timing until the project has a rank-level catalog of every perk requirement. This note supports the TB-009B support table only; final allocation timing and grind strategy remain deferred to TB-020.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000269 | Skyrim:Alteration | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Alteration | 2026-05-12 | Alteration skill perk table. |
| SRC-000270 | Skyrim:Conjuration | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Conjuration | 2026-05-12 | Conjuration skill perk table. |
| SRC-000271 | Skyrim:Destruction | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Destruction | 2026-05-12 | Destruction skill perk table. |
| SRC-000272 | Skyrim:Enchanting | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Enchanting | 2026-05-12 | Enchanting skill perk table. |
| SRC-000273 | Skyrim:Illusion | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Illusion | 2026-05-12 | Illusion skill perk table. |
| SRC-000274 | Skyrim:Restoration | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Restoration | 2026-05-12 | Restoration skill perk table. |
| SRC-000275 | Skyrim:Archery | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Archery | 2026-05-12 | Archery skill perk table. |
| SRC-000276 | Skyrim:Block | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Block | 2026-05-12 | Block skill perk table. |
| SRC-000277 | Skyrim:Heavy Armor | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Heavy_Armor | 2026-05-12 | Heavy Armor skill perk table. |
| SRC-000278 | Skyrim:One-handed | 2 - UESP | https://en.uesp.net/wiki/Skyrim:One-handed | 2026-05-12 | One-handed skill perk table. |
| SRC-000279 | Skyrim:Smithing | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Smithing | 2026-05-12 | Smithing skill perk table. |
| SRC-000280 | Skyrim:Two-handed | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Two-handed | 2026-05-12 | Two-handed skill perk table. |
| SRC-000281 | Skyrim:Alchemy | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Alchemy | 2026-05-12 | Alchemy skill perk table. |
| SRC-000282 | Skyrim:Light Armor | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Light_Armor | 2026-05-12 | Light Armor skill perk table. |
| SRC-000283 | Skyrim:Lockpicking | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Lockpicking | 2026-05-12 | Lockpicking skill perk table. |
| SRC-000284 | Skyrim:Pickpocket | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Pickpocket | 2026-05-12 | Pickpocket skill perk table. |
| SRC-000285 | Skyrim:Sneak | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Sneak | 2026-05-12 | Sneak skill perk table. |
| SRC-000286 | Skyrim:Speech | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Speech | 2026-05-12 | Speech skill perk table. |

## Evidence Summary

Each UESP skill page has a "Skill Perks" table with one row per perk rank or one row per one-rank perk. Those tables provide the perk name, rank where applicable, description, form ID, skill requirement, and prerequisite perk requirement. `data/skills/perk-rank-catalog.csv` transcribes those tables into one row per perk rank.

The parsed rank rows reconcile to the TB-009A skill summary counts:

| Skill | Perk nodes | Perk ranks |
| --- | ---: | ---: |
| Alteration | 10 | 14 |
| Conjuration | 15 | 16 |
| Destruction | 14 | 17 |
| Enchanting | 9 | 13 |
| Illusion | 13 | 13 |
| Restoration | 12 | 13 |
| Archery | 9 | 16 |
| Block | 9 | 13 |
| Heavy Armor | 8 | 12 |
| One-handed | 10 | 21 |
| Smithing | 10 | 10 |
| Two-handed | 9 | 19 |
| Alchemy | 9 | 15 |
| Light Armor | 6 | 10 |
| Lockpicking | 11 | 11 |
| Pickpocket | 8 | 12 |
| Sneak | 9 | 13 |
| Speech | 9 | 13 |
| **Total** | **180** | **251** |

The catalog records prerequisite text as source-listed text. Requirements such as "Daedric Smithing or Glass Smithing" are preserved as text rather than converted into route logic in this pass.

## Confidence and Open Questions

Confidence is high for source-table transcription and count reconciliation. The validator checks that the perk-rank catalog has 251 rank rows, 180 perk nodes, expected per-skill counts, valid source-note references, and cross-references to the TB-009A skill-tree objective rows.

Open questions for later work:

* final perk allocation order;
* whether any prerequisite text needs normalized machine-readable `and`/`or` logic before TB-020;
* which skills should be trained naturally, bought from trainers, or made Legendary;
* how perk choices interact with gradual Legendary difficulty pacing;
* merchant-investment timing after the Speech Investor perk;
* PS4 trophy metadata and achievement behavior validation in TB-015.

## Linked Records

`data/skills/perk-rank-catalog.csv`; `data/skills/skill-perk-catalog.csv`; `data/objectives/objectives.csv` rows `OBJ-002444` through `OBJ-002462`; `docs/task-board.md`.
