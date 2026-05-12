# data/checklist-mapping

Checklist synchronization materials belong here.

Use this directory for the coverage strategy and matrix that map checklist objectives to route steps, branch routes, appendices, or explicit exclusions.

Current raw checklist snapshot:

* `raw/Skyrim Checklist.xlsx`

Generated TB-030 outputs:

* `coverage-matrix.csv` maps spreadsheet rows to current route prototypes, branch prototypes, option lists, appendices, exclusions, or review buckets.
* `checklist-coverage-summary.md` records row counts and remaining review buckets.
* `checklist-scope-review.md` records the TB-031A scope decision for broad regular-book checklist rows.
* `checklist-manual-review.md` records the TB-031B resolution of generic manual-review rows into source-backed mappings or typed source-readiness holds.
* `checklist-escalation-decisions.md` records the TB-031C decisions for branch/default/radiant/counter escalation.
* `../route-planning/route-default-decisions.md` records the TB-031D route defaults used by option-list and logistics follow-up rows.

Regenerate the matrix with:

```bash
python3 tools/build_checklist_coverage.py
```

The generator requires `openpyxl` to read the raw workbook.
