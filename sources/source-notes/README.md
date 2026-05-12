# sources/source-notes

Source notes for gameplay facts belong here.

Each routing-relevant factual claim should be traceable to a source note before it is used in objective data, constraints, skeletons, or final guide prose.

Use `source-note.template.md` for new notes.

Naming convention:

`SN-000001-short-slug.md`

Rules:

* Assign source-note IDs sequentially.
* Keep each note focused on one claim or a small set of tightly related claims.
* Reference bibliography `source_id` values inside the note.
* Link source-note filenames from data rows and route prototypes through their citation fields.

## Status Semantics

Source-note `Status:` values describe the note's local review state, not automatic permission to write final guide prose.

| Status pattern | Meaning for route work |
| --- | --- |
| `researched` or `researched; ... added` | The note supports the current planning claim named in the file; later route prose must still inspect linked constraints and validation owners. |
| `complete` | The note is a coordination/source-intake artifact whose limited claim is complete. |
| `needs review` | Historical or source-list note retained as input. It is usable only through the current objective, constraint, support-table, checklist, or route-planning rows that cite it; do not treat the status itself as a hidden blocker or as validation. |

TB-031H audited source-note, objective-row, support-table, and generated-index readiness in `docs/source-objective-readiness-audit.md`. Do not mass-update older `needs review` notes without source-checking the concrete row being changed under `docs/source-standards.md`.
