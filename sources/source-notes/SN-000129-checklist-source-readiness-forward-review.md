# Source Note: Checklist Source-Readiness Forward Review

Status: researched.

Source note ID: SN-000129

## Claim

TB-031J pulls the remaining 78 checklist `source_readiness_required` rows forward from TB-036 and resolves them before warning-layer work begins.

The review does not create final route prose or exact acquisition steps. It makes source-backed checklist dispositions:

* 75 rows map to existing main-route objective or parent-route handling.
* 1 row maps to an existing branch prototype: `Reclamation Priest's Journal (AE)` belongs with the Ghosts of the Tribunal destroy-heretics / Reclamation Priest attack-state branch.
* 2 rows are explicit exclusions: `A Kiss, Sweet Mother` and `Pension of the Ancestor Moth`, because the source pages list them as ordinary `List 2` books rather than required skill, quest, AE, spell-tome, Black Book, or checklist-unique books.

## Routing Relevance

After this review, checklist coverage should have no `source_readiness_required` rows. TB-032 can place warning and hard-save text without carrying hidden source-readiness holds. TB-033/TB-034 still own final validation and route placement: this note only decides whether each checklist row is source-supported, excluded, or branch-prototype coverage.

`data/checklist-mapping/source-readiness-resolutions.csv` is the machine-readable row-level decision table consumed by `tools/build_checklist_coverage.py`.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000188 | Skyrim:Creation Club Books | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Creation_Club_Books | 2026-05-11 | AE book index used for Creation-added checklist title existence and package association. |
| SRC-000218 | Skyrim:Unique Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Unique_Items | 2026-05-11 | Existing unique-item overview. |
| SRC-000219 | Skyrim:Unique Weapons | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Unique_Weapons | 2026-05-11 | Existing unique weapon inventory. |
| SRC-000220 | Skyrim:Unique Armor | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Unique_Armor | 2026-05-11 | Existing unique armor inventory. |
| SRC-000221 | Skyrim:Unique Clothing | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Unique_Clothing | 2026-05-11 | Existing unique clothing inventory. |
| SRC-000222 | Skyrim:Unique Jewelry | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Unique_Jewelry | 2026-05-11 | Existing unique jewelry inventory. |
| SRC-000223 | Skyrim:Other Unique Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Other_Unique_Items | 2026-05-11 | Existing other unique-item inventory. |
| SRC-000378 | Skyrim:Her Word Against Theirs | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Her_Word_Against_Theirs | 2026-05-12 | Reclamation Priest attack-state and journal dependency cross-check. |
| SRC-000443 | Skyrim:Specialty Gear | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Specialty_Gear | 2026-05-12 | Blades equipment, Akaviri Sword, and Headsman's Axe source-readiness checks. |
| SRC-000444 | Skyrim:Staves | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Staves | 2026-05-12 | Staff rows including Rahgot, Eye of Melka, Gadnor's Staff of Charming, Halldir's Staff, Hevnoraak's Staff, Staff of Hag's Wrath, Staff of Jyrik Gauldurson, and Staff of Ruunvald. |
| SRC-000445 | Skyrim:Quest Items | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Quest_Items | 2026-05-12 | Asgeir's Wedding Band, Fjola's Wedding Band, and Kahvozein's Fang source-readiness checks. |
| SRC-000446 | Skyrim:Clothing | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Clothing | 2026-05-12 | Emperor's Robes, Mythic Dawn pieces, Radiant Raiment clothes, Vaermina Robes, and wedding clothing checks. |
| SRC-000447 | Skyrim:Execution Hood | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Execution_Hood | 2026-05-12 | Execution Hood acquisition check. |
| SRC-000448 | Skyrim:Falmer Equipment | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Falmer_Equipment | 2026-05-12 | Ancient Falmer armor source-readiness checks. |
| SRC-000449 | Skyrim:Vampire Equipment | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Vampire_Equipment | 2026-05-12 | Vampire Royal Armor source-readiness check. |
| SRC-000450 | Skyrim:Pension of the Ancestor Moth | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Pension_of_the_Ancestor_Moth | 2026-05-12 | Skill-book misclassification check; source lists regular `List 2` type. |
| SRC-000451 | Skyrim:Dwarven Crown Journal | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Dwarven_Crown_Journal | 2026-05-12 | `Dwarven Crown Control` checklist alias/source correction. |
| SRC-000452 | Skyrim:Guard's Dossier: Ehlhiel | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Guard%27s_Dossier:_Ehlhiel | 2026-05-12 | `Guard Dossier: Ehlhiel` checklist alias/source correction. |
| SRC-000453 | Skyrim:Reclamation Priest's Journal | 2 - UESP | https://en.uesp.net/wiki/Skyrim:Reclamation_Priest%27s_Journal | 2026-05-12 | Branch-state journal source and location check. |
| SRC-000454 | Skyrim:A Kiss, Sweet Mother | 2 - UESP | https://en.uesp.net/wiki/Skyrim:A_Kiss,_Sweet_Mother | 2026-05-12 | Base-game regular-book scope check; source lists regular `List 2` type and multiple copies. |

## Evidence Summary

The unique-gear rows were source-ready as checklist cues but not all had exact item objective rows. TB-031J maps them to the safest existing parent route surface: the related quest, dungeon/location objective, artifact objective, or faction-route objective that controls normal acquisition.

Examples:

| Checklist rows | Resolution |
| --- | --- |
| Blades Armor, Boots, Gauntlets, Helmet, Shield, Sword | Map to `Alduin's Wall` / Sky Haven Temple handling. |
| Dragon Priest Staff (Rahgot), Hevnoraak's Staff, Staff of Jyrik Gaudurson | Map to the related dragon-priest or College/Saarthal objective; preserve the checklist spelling correction for Jyrik Gauldurson. |
| Wedding Dress, Wedding Sandals, Wedding Wreath, Asgeir's Wedding Band | Map to `Bound Until Death`. |
| Ancient Falmer armor pieces and Vampire Royal Armor | Map to Dawnguard main-route parent objectives. |

The AE document rows are checklist-tracked Creation documents. They map to their parent AE quest, package, or route surface unless a source proves they are ordinary out-of-scope books.

Notable corrections:

| Checklist row | Source-backed correction |
| --- | --- |
| `Dwarven Crown Control (AE)` | Source title is `Dwarven Crown Journal`; map to `The Dwarven Crown`. |
| `Guard Dossier: Ehlhiel (AE)` | Source title includes possessive form `Guard's Dossier: Ehlhiel`; map to `Double-Edged`. |
| `Reclamation Priest's Journal (AE)` | Source page and `Her Word Against Theirs` tie it to giving propaganda to the Reclamation Priest and his later Ashfall's Tear attack state. Map to BR-007 branch coverage instead of ordinary main-route Ghosts cleanup. |
| `A Kiss, Sweet Mother` | Source lists a regular `List 2` book with multiple copies; exclude from required book coverage. |
| `Pension of the Ancestor Moth` | Source lists a regular `List 2` book, not a skill book; exclude from skill-book coverage. |

## Linked Records

`data/checklist-mapping/source-readiness-resolutions.csv`

`data/checklist-mapping/coverage-matrix.csv`

`tools/build_checklist_coverage.py`

`data/checklist-mapping/checklist-coverage-summary.md`

`docs/source-objective-readiness-audit.md`
