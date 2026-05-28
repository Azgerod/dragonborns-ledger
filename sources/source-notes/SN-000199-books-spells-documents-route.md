# SN-000199 - Books, Spells, and Documents Route

Status: researched for TB-035-MR-065 guide expansion.

This note supports the `Books, Spells, and Documents` section in `drafts/final-guide/main-guide-v1.md`.

## Sources

| Source ID | Tier | Page or project input | Reference | Date used | Use |
| --- | --- | --- | --- | --- | --- |
| SN-000051 | Project source note | Skill Books and Reader Trophy | `sources/source-notes/SN-000051-skill-books-and-reader.md` | 2026-05-28 | Skill-book title inventory, duplicate-copy policy, and Reader trophy target. |
| SN-000052 | Project source note | Spell Tomes and Learned Spells | `sources/source-notes/SN-000052-spell-tomes-and-learned-spells.md` | 2026-05-28 | Spell-tome title inventory, vendor-stock constraints, fixed sources, and master-tome gates. |
| SN-000126 | Project source note | Progression Source Selection and Grind Policy | `sources/source-notes/SN-000126-progression-source-selection-and-grind-policy.md` | 2026-05-28 | Selected skill-book copies, selected spell-tome sources, Oghma timing, and late progression policy. |
| SN-000168 | Project source note | College Arniel, Septimus, and Aetherium Route | `sources/source-notes/SN-000168-college-arniel-septimus-aetherium-route.md` | 2026-05-28 | Master ritual quest skill gates, linked ritual documents, and why the rituals remain fixed-late. |
| SN-000174 | Project source note | Blades, Blackreach, and The Fallen Route | `sources/source-notes/SN-000174-blades-blackreach-fallen-route.md` | 2026-05-28 | Oghma Infinium acquired through Septimus but left unread for later progression math. |
| SN-000196 | Project source note | Black Book Defaults and Progression Switches | `sources/source-notes/SN-000196-black-book-defaults-progression-switches.md` | 2026-05-28 | Scholar's Insight retention until the selected skill-book route is complete and later Winds of Change switching. |
| SN-000198 | Project source note | Collectible Reconciliation Route | `sources/source-notes/SN-000198-collectible-reconciliation-route.md` | 2026-05-28 | Fishing species route-resolution hold and inherited `Note from Mogrul` random-encounter policy. |
| DATA-031E | Project data | Progression source selections | `data/constraints/progression-source-selections.csv` | 2026-05-28 | Canonical selected sources for all 90 skill-book titles and all 154 spell-tome titles. |

## Route Decisions

The section closes the active `Scholar's Insight` policy before any final Black Book default switch. It first checks the 27 unique skill-book titles already read after `Scholar's Insight` became active, then routes the remaining 63 selected skill-book copies. This reaches the Reader threshold during the pass and closes all 90 title-level skill-book objectives under the route's selected-copy policy.

After the final skill-book read, `Black Book: The Winds of Change` is safe to change from `Scholar's Insight` to `Companion's Insight`. The section confirms all seven Black Book titles by name, stores them together, and leaves `Companion's Insight` as the standing Winds of Change default.

Spell tomes are split into three player-facing states instead of being hidden under a broad book cleanup line:

- 35 non-vendor or quest-tied tomes are checked against already-routed fixed, pet, reward, Atronach Forge, Apocrypha, or quest sources.
- 102 non-master vendor tomes are bought and read from the named spell vendors when offered, with unavailable skill-gated stock written to `All-Perks Vendor Return`.
- 17 master ritual outcomes remain staged for the all-perks loop because the guide has not yet established the final Alteration 90, Conjuration 90, Destruction 100, Illusion 100, and Restoration 90 states.

The Oghma Infinium remains acquired but unread. Its use still belongs to the all-perks loop after final skill gaps are known, and the guide repeats the boundary not to spend it on a skill already at 100.

Fishing documents remain tied to the unresolved per-species Fishing route. They are not closed here because the exact fish routes still need spot, biome, weather, time, rod, active quest state, and ingredient-preservation inputs. `Note from Mogrul` also remains unresolved under the existing Raven Rock debt-state policy; this section does not force Mogrul's thugs by waiting or wandering.

## Coverage Summary

Internal coverage adds MR-065 rows for all 90 skill-book title objectives, Reader, all 154 spell-tome objectives, the seven Black Book title rows, the Black Book set row, the final Winds of Change default, Oghma, the five master ritual quests, the four Master Illusion Text rows, `Power of the Elements`, the Fishing document hold rows, and the inherited `Note from Mogrul` route-resolution row.

## Linked Records

OBJ-000129 through OBJ-000133; OBJ-000801; OBJ-000819 through OBJ-001079; OBJ-001216 through OBJ-001219; OBJ-001241; OBJ-001325; OBJ-001398 through OBJ-001402; OBJ-001444 through OBJ-001448; OBJ-001487; OBJ-001545; OBJ-001546; OBJ-001892; PROGSEL-000001 through PROGSEL-000244; PROGSEL-000593; PROGSEL-000594.
