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
* `../constraints/progression-source-selection.md` and `../constraints/progression-source-selections.csv` record the TB-031E progression source-selection defaults and progression alias resolutions.
* `counter-coverage-plan.md` records the TB-031F route-planning decisions for checklist/trophy counters, activity mechanics, and counter-owned source-readiness rows.
* `../locations/location-route-validation.md` records the TB-031G location route-validation decisions for Delver/Explorer mechanics, marker exceptions, content-location treatment, and the remaining location source-readiness row.
* `../../docs/source-objective-readiness-audit.md` records the TB-031H readiness audit for source notes, objective rows, support tables, and generated owner labels.
* `../../docs/deferred-work-audit.md` records the closed TB-031I final deferred-work scan before warning placement.

Regenerate the matrix with:

```bash
python3 tools/build_checklist_coverage.py
```

The generator requires `openpyxl` to read the raw workbook.
