# data/checklist-mapping

Checklist synchronization materials belong here.

Use this directory for the coverage strategy and matrix that map checklist objectives to route steps, branch routes, appendices, or explicit exclusions.

Current raw checklist snapshot:

* `raw/Skyrim Checklist.xlsx`

Generated TB-030 outputs:

* `coverage-matrix.csv` maps spreadsheet rows to current route prototypes, branch prototypes, option lists, appendices, exclusions, or review buckets.
* `checklist-coverage-summary.md` records row counts and remaining review buckets.
* `checklist-scope-review.md` records the TB-031A scope decision for broad regular-book checklist rows.

Regenerate the matrix with:

```bash
python3 tools/build_checklist_coverage.py
```

The generator requires `openpyxl` to read the raw workbook.
