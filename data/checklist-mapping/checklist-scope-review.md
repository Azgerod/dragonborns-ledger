# Checklist Scope Review

Status: TB-031A complete.

Input: `data/checklist-mapping/coverage-matrix.csv`

Raw checklist snapshot: `data/checklist-mapping/raw/Skyrim Checklist.xlsx`

No new gameplay research was performed for this pass. This review applies the existing project scope in `docs/guide-specification.md` and `docs/decisions-log.md` to rows that TB-030 marked `scope_review_required`.

## Scope Decision

| Bucket | Rows | Decision | Matrix treatment |
| --- | ---: | --- | --- |
| Broad regular-book library rows | 312 | Exclude from required route and required appendix coverage. | `mapping_type=Explicit exclusion`; `status=excluded_with_justification`; `match_status=support_table_only`; `match_source=book_scope_review`. |

The 312 resolved rows all come from the Books tab, category `general_book`, raw group `Regular books, journals and spell tomes`, and raw status `N/N/N`.

## Rationale

The required book/document scope remains:

* skill books;
* spell tomes needed to learn all spells;
* Black Books;
* quest books, notes, and journals required for quests or AE starts;
* unique books/notes tracked by the checklist.

The project explicitly excludes every-copy/every-readable-book library completion from required completion. The raw spreadsheet's broad regular-book section is therefore treated as an external checklist extension, not as a route or appendix requirement for this guide.

Optional broader library-completion discussion may be added only if the project scope changes. Do not use TB-036 appendices or final guide prose to quietly reintroduce these 312 titles as required objectives.

## Boundary

This decision does not exclude or downgrade in-scope book/document rows. Skill books, spell tomes, Black Books, quest/AE documents, unique checklist-tracked documents, and unmatched book/document rows remain governed by their own rows and later tasks.

TB-031B has resolved the remaining book-related manual-review rows:

| Category | Rows | Owner |
| --- | ---: | --- |
| `book_document` | 49 | TB-031B mapped 6 to existing source-backed rows and converted 43 checklist-only rows into `source_readiness_required` holds; TB-031H assigned ownership, and TB-031J resolved the remaining holds before TB-032. |
| `skill_book` | 2 | TB-031B mapped 1 title-spelling variant to an existing skill-book row and converted 1 checklist-only row into a `source_readiness_required` hold; TB-031H assigned ownership, and TB-031J excluded the remaining hold as a regular-book/scope mismatch. |

## Audit Query

Use this matrix filter to inspect every row resolved by TB-031A:

```text
match_source == book_scope_review
```

Expected count after TB-031A: 312 rows.

Expected remaining `scope_review_required` count after TB-031A: 0 rows.
