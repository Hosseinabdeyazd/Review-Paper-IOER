# Digital Twin + uncertainty across S1–S5

This is a new, uncertainty-gated retrieval dataset in the building/material-flow review. It is separate from the earlier Digital Twin base corpus and the 392-record S4/S5 Base + Uncertainty corpus that did not require Digital Twin.

## Search design

For each stage: **Digital Twin AND building-domain block AND stage block AND uncertainty block**. Exact executable queries are frozen in `protocol/queries.json`. Existing stage vocabulary is preserved. Scopus searches TITLE-ABS-KEY; Web of Science Core Collection searches TS (including Keywords Plus); IEEE uses the default metadata search. These field scopes are not identical. No date, language, document-type or access filters were applied.

| Stage | Analytical role | IEEE | Scopus | WoS | Conservative unique stage records |
|---|---|---:|---:|---:|---:|
| S1 | Observation and building reconstruction | 80 | 231 | 154 | 306 |
| S2 | Material inventory and stock inference | 1 | 10 | 9 | 12 |
| S3 | Timing, service life and material outflows | 14 | 33 | 13 | 47 |
| S4 | Circularity, reuse and recoverability | 40 | 115 | 67 | 161 |
| S5 | Embodied environmental impacts and decisions | 21 | 67 | 48 | 92 |

All **15 exports match their observed result counts**: 903 source rows, 534 conservatively deduplicated records, 369 repeated source rows. Stage counts overlap and must not be summed. 52 unique records have no DOI in the exports; no DOI was invented. Seven title/year groups are flagged for manual adjudication; they are not automatically merged. These are **retrieval counts, not confirmed relevant articles**. Conference-review/container records and out-of-domain false positives remain in the raw data.

Run label: 2026-11-02 Europe/Berlin. Export filenames supplied by the databases carry 2026-11-01 UTC; original bytes are preserved and fingerprints are logged.

## What is complete

- All native export fields: IEEE CSV; Scopus CSV with Select all information, including abstracts, keywords, affiliations, funding and references; WoS tab-delimited Full Record and Cited References.
- A normalized source CSV, conservative deduplicated CSV, and explicit database/stage/source membership.
- Raw-file SHA-256 manifest, observed-count completeness audit, missing-field report and metadata-conflict report.
- Reproducible Python standard-library ingestion code. Native fields, including fields outside the normalized schema, are retained in `source_records.csv` as JSON key/value pairs and in unchanged raw files.

## Interpretation and evidence limits

The uncertainty block contains `uncertaint*`, `probabil*`, `stochastic*`, Bayesian, Monte Carlo, sensitivity, variability, calibration, robustness, decision confidence, value of information and interval terms. Broad terms improve recall but do **not** establish that a paper models uncertainty. `building*` can also match model-building, and recovery can refer to networks rather than materials. S5 operational-energy-only papers need separate exclusion or explicit supporting-role classification.

S1–S5 are analytical stages, not claimed universal software layers of Digital Twins. To establish uncertainty continuity, a paper must identify the uncertain input, its representation, the mapping between stages, the output representation, dependencies/correlations, and an update/validation mechanism. A Digital Twin mention or single-stage Monte Carlo analysis alone does not prove this chain.

Evidence-review CSVs, where present, are title/abstract assessments only, distinct from the raw retrieval and deduplication outputs. Full-text verification is not complete in this dataset. Missing abstracts are not evidence of absence. No paper should be represented as a demonstrated cross-stage uncertainty architecture from these search hits alone.

## Files and reproduction

- `raw/IEEE`, `raw/Scopus`, `raw/WoS`: unchanged full exports, one per stage.
- `protocol/queries.json`: exact search statements and stage mapping.
- `protocol/expected_counts.json`: counts observed in database result pages.
- `protocol/export_completeness.csv`, `file_manifest.csv`: count and byte-integrity audits.
- `analysis/source_records.csv`: all 903 source occurrences plus native fields.
- `analysis/deduplicated_records.csv`: 534 conservative records with authors, title, year, DOI where available, journal/source, abstract, keywords, document type and links.
- `analysis/stage_source_membership.csv`: provenance and stage overlap.
- `analysis/metadata_conflicts.csv`: alternative metadata values retained for audit; a conflict is not automatically an error.
- `analysis/possible_title_duplicates.csv`: no automatic fuzzy merging.
- `analysis/missing_fields.csv`, `summary.json`: completeness statistics.

Rebuild with `python code/build_dataset.py` from this folder, or `python code/build_dataset.py --check-only` for a read-only audit. DOI normalization only removes DOI URL/prefix and normalizes case; exact DOI keys merge. Without DOI, only a matching native identifier within the same database merges. The pipeline does not silently merge titles or modify raw exports.
