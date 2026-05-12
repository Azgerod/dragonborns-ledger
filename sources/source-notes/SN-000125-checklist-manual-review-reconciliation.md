# Checklist Manual Review Reconciliation

Status: complete.

Source note ID: SN-000125

## Claim

The raw checklist snapshot contains checklist-only rows that cannot yet be treated as source-backed objective, support-table, route, appendix, or exclusion records without follow-up validation.

## Routing Relevance

TB-031B uses these rows only to preserve checklist synchronization pressure. A row marked `source_readiness_required` is not a gameplay fact, route instruction, appendix commitment, or final-scope decision. The owner named in `guide_location` must validate source scope, promote the row into the appropriate source-backed table, or explicitly exclude it before final guide coverage is claimed.

## Sources

| source_id | Source | Priority | URL/reference | Accessed | Notes |
| --- | --- | --- | --- | --- | --- |
| SRC-000425 | User-provided checklist snapshot | 4 - Working input | `data/checklist-mapping/raw/Skyrim Checklist.xlsx` | 2026-05-12 | Local export from the user's Google Sheets checklist, used as checklist synchronization input rather than independent gameplay authority. |

## Evidence Summary

The TB-031B generator pass mapped naming, spelling, abbreviation, parent-objective, quest-detail, and location-detail gaps to existing source-backed rows where the repository already had source support. Remaining checklist-only rows were carried as typed source-readiness holds. They are grouped by category and owner in `data/checklist-mapping/checklist-manual-review.md`; TB-031J later resolved the final source-readiness queue in `data/checklist-mapping/source-readiness-resolutions.csv`.

## Confidence and Open Questions

Confidence is high that the listed checklist rows exist in the workbook snapshot. Confidence is not asserted here for gameplay availability, PS4 AE scope, route safety, or final completion value of any historical `source_readiness_required` row. TB-031H audited ownership for the remaining rows; TB-031J then source-checked and resolved the book/document, skill-book, and unique-gear source-readiness holds before TB-032.

## Linked Records

* `data/checklist-mapping/checklist-manual-review.md`
* `data/checklist-mapping/coverage-matrix.csv`
* `tools/build_checklist_coverage.py`
* `tools/validate_coverage.py`
