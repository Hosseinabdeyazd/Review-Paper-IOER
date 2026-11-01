# S4/S5 completed requested reassessment

All **7,188 remaining records** have now received title-and-complete-available-abstract decisions. Together with the prior 50, the requested queue contains **7,238/7,238 reviewed original IDs**, with zero pending. One supplemental retraction review is counted separately; three duplicate-member QA rereads do not add records.

This is AI-assisted title/abstract screening, not independent human review or completed full-text eligibility. Elicit delivered 80 records; all were reread and 14 decisions corrected. No paid upgrade was used. Three delegated assistants and the primary assistant completed the direct reading. Missing abstracts remain explicitly uncertain.

## Files

- `PRISMA_REASSESSMENT.md`: coverage, canonical outcome counts, method and limitations.
- `revised_records.zip`: `revised_records.csv` with 9,587 canonical records, all available bibliographic fields including authors, DOI, abstract and provenance; also original merged metadata JSON.
- `title_abstract_review_log.zip`: full CSV of 7,239 original-ID decisions, including bibliographic fields, individual reason, literal evidence and reviewer attribution.
- `title_abstract_decisions.json`: all 7,238 requested decisions; supplemental decisions in their separate JSON.
- `duplicate_group_adjudication.csv`, `record_alias_map.csv`, `IDENTIFIER_RESOLUTION.md`: all 330 groups and 14 DOI-conflict resolutions. 331 additional duplicates removed. One canonical DOI remains unverified/blank; original supplied values preserved.
- `summary.json`, `direct_review_coverage.json`, `prisma_reassessment_counts.csv`: machine-readable actual counts.
- `reproducibility_bundle.zip`: explicitly authored decision files and processing/validation code. Extract at the original review workspace root; source input is `outputs/S4 S5 Core Review/screening/tables/all_records_screening.zip` from this repository. Run work/aggregate_direct_reviews.py --require-complete, then adjudication/build_revision.py, then work/build_prisma_adjudication_report.py and work/package_final_reassessment.py. No model API or keyword classifier runs in these rebuilding scripts.

## Decision interpretation

Retained records need full-text eligibility; secondary literature is separate. Methods/background leads are preserved outside the S4/S5 core. Five differing decisions on merged records were explicitly reconciled after rereading; original decisions and reasons remain preserved in canonical_conflict_resolutions.json and the review log. The 2,680 previously automated scope/secondary records outside the requested queue are not claimed as newly read; only one documented supplemental record was added. Report counts and original-ID counts have different denominators.

Historical `revised_records_partial.zip`, `prisma_checkpoint.csv` and the old uncompressed 50-record CSV on GitHub are superseded by the files above, and remain only as checkpoints. No final included-study count is claimed.
