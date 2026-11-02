# Temporal trends: three-database query audit

Status: NOT a final harmonized bibliometric figure. Counts use actual existing corpus records, not simulations or samples. Sources are IEEE Xplore, Scopus and Web of Science.

The requested final design is five S1–S5 panels with Base, Base+U, Base+DT and Base+U+DT, plus a general DT/DT+U panel. It is not yet defensible to overlay all four as nested cohorts: the original Base queries and DT-adapted stage queries differ. S1 Base contains 878 records while its differently scoped DT retrieval contains 1408. The audit figure therefore separates query families into columns.

## Rules
- Annual counts, not cumulative; do not sum overlapping stages or cohorts.
- Existing source-corpus deduplication is retained for stage counts; unresolved title candidates remain unresolved. Counts are retrieved publications, not verified relevant studies.
- Full year range remains in CSV; audit figure displays 2000–2025. 2026 is incomplete, 2027 is future-indexed.
- Input hashes, original file paths, source-database membership and missing-year checks appear in input_audit.json. S1–S3 inputs come from the repository's analysis_ready/final tables. Their prior filtering status must be reconciled with raw search exports before publication.
- General DT+U merges identical normalized DOI only; records without DOI remain separate. Conflicting or missing years are excluded from annual counts and explicitly listed, not silently assigned. This conservative count is not a final adjudicated union.

## Outstanding requirements for final publication
1. Fix one base stage/context query per S and derive U, DT and U+DT by adding identical blocks in every database. Re-run mismatched searches and reconcile exports.
2. Complete domain-independent DT-only retrieval in all three databases; use the same DT and U blocks as its companion DT+U search. Existing general DT+U used a narrower uncertainty term than the stage-wide U block, so it must not be treated as an equivalent subset.
3. Resolve cross-source DOI/year disagreements and missing-DOI duplicates; verify raw-versus-screened status across inputs.
4. Render the final six-panel figure only after these gates pass. No placeholder DT counts or inferred zeroes have been created.

The live IEEE DT-only search on 2026-11-02 returned 25085 records for `"digital twin" OR "digital twins"`, all results, no date filter. This is a source-specific result count only; its 1000-record export limit means it is not a completed export or a deduplicated three-database total.
