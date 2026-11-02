# Temporal trends: three-database query audit

## Summed view requested on 2 November 2026

The complete eight-figure arithmetic-sum package is in [summed_three_databases](summed_three_databases/README.md). It combines IEEE + Scopus + Web of Science counts, retaining cross-database duplicates as explicitly requested. The previous source-separated diagnostics remain below for provenance.


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

## Live three-database update, 2 November 2026

General DT source-specific search totals are IEEE 25,085, Scopus 61,675 and WoS 37,609. Do not sum them. Annual Scopus facets were downloaded as native CSV; WoS year facets were captured from the visible page; IEEE years 2016–2027 were individually queried and sum to 25,080, leaving five pre-2016 results not disaggregated. This is a complete 2016–2025 annual trend window, not a complete record-level DT export.

`general_dt_dtu_source_profiles.pdf/svg/png` presents three source-specific panels for 2016–2025. Orange curves use the full previously exported legacy DT+U searches. Their literal U block is `uncertainty`, not the broad stage U vocabulary; DT-only uses singular/plural OR whereas legacy U uses the singular phrase. These are documented historical profiles, not a final harmonized prevalence comparison. Missing IEEE years before 2016 are not plotted or filled with zero.

WoS default Publication Years facets sum exactly to 37,609; Final Publication Year facets sum to 36,563. The difference of 1,046 equals the Early Access count. Thus no numerical double counting was found in the default facet total; changing to final-year-only instead omits Early Access records. Both snapshots are retained and final-year sensitivity counts are in the CSV.

All record-level general DT exports, cross-database union deduplication, and query harmonization remain outstanding. Annual source counts alone cannot produce a deduplicated union. The earlier query-audit chart is unchanged and remains diagnostic.
