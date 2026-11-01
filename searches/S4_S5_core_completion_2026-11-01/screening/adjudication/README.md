# S4/S5 — all canonical title/abstract records screened

**9,587/9,587 canonical records screened; 0 pending.** The final 2,588 are completed in this revision. This is AI-assisted title/abstract screening; full-text eligibility remains a separate next step.

| Outcome | Count |
|---|---:|
| Retain for full text | 2,668 |
| Unclear: retain for full-text verification | 946 |
| Secondary literature | 323 |
| Methods/background, outside core | 1,477 |
| Out-of-scope title/abstract exclusions | 4,057 |
| Nonresearch components | 115 |
| Retracted source | 1 |

## Current deliverables

- `canonical_screening_complete.zip`: complete CSV with all original bibliographic fields, DOI/authors/abstract, provenance, previous status and final screening reasons/evidence; original merged metadata JSON preserved.
- `screening_decision_sets.zip`: seven full-metadata CSVs split by decision.
- `remaining_2588_review_log.zip` and `remaining_2588_decisions.json`: all newly authored decisions with individual reasons, literal evidence, stage and abstract adequacy.
- `PRISMA_REASSESSMENT.md`, `prisma_complete_counts.csv`, `completion_summary.json`: actual coverage/counts and methodological qualifications.
- `completion_validation.json`: preservation and coverage checks.
- `related_report_versions.csv`: two publisher/university-verified translation/correction families; distinct reports must not be double-counted as independent studies.
- `completion_reproducibility_bundle.zip`: authored decisions, immutable queue and processing code.
- `duplicate_group_adjudication.csv`, `record_alias_map.csv`, `IDENTIFIER_RESOLUTION.md`: unchanged evidence for all 330 duplicate groups and 14 DOI-conflict resolutions. 331 additional removals; one unverified DOI blank rather than invented.

## Historical inputs

`revised_records.zip`, `summary.json`, `title_abstract_review_log.zip`, `title_abstract_decisions.json`, `direct_review_coverage.json`, `final_validation.json`, `final_manifest.json`, `prisma_reassessment_counts.csv` and `reproducibility_bundle.zip` describe the previous completed queue of 7,238 original IDs plus one supplemental integrity review. They remain auditable inputs and are superseded for current totals by the completion files above. Earlier partial/checkpoint files are historical only. Do not rerun the older build scripts over the new report.

There was no independent human review; Elicit was not upgraded. Retained reports are not final included studies. Full-text assessment count for this revision is zero. See the PRISMA report for exact original-ID versus canonical denominators and limits.

## CSV field interpretation

Use `adjudication_status`, `adjudication_reason`, `adjudication_evidence` and `adjudication_reviewer` for the current semantic decision. `screening_status`, `decision_reason`, `decision_basis`, `matched_rule` and `reviewer` are preserved original automated-routing fields, not the current decision. `previous_adjudication_status` records the prior revision. The `completion_*` stage/adequacy fields are populated for the new 2,588 only; older detailed adequacy/stage evidence remains in the previous original-ID review log. All original author, DOI, abstract, journal, year, source and identifier fields remain available. Empty DOI means missing/unverified, not a fabricated identifier. `related_report_family` links known versions without asserting that every possible study family has been resolved.
