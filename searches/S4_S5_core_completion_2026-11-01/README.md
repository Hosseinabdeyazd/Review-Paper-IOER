# S4–S5 core review completion — 2026-11-01

**Screening update:** [Full-corpus automated first pass, PRISMA accounting and enriched metadata](screening/README.md) is now available. Proposed exclusions are provisional; independent eligibility screening remains pending. The retrieval counts below remain the original audited snapshot.

This completes retrieval for the original review's **S4 circularity/recoverability** and **S5 embodied LCA/decision** streams, using the existing draft vocabulary frozen for this execution. **Digital Twin is not a required search term.** The separate 12-fulltext Digital Twin bridge collection remains in `DT/Digital Twin Material Flow Review/bridge_searches/fulltext_review/`.

| Database | S4 base | S4 + uncertainty | S5 base | S5 + uncertainty |
|---|---:|---:|---:|---:|
| Scopus |2538|415|6621|1359|
| Web of Science |1883|361|4834|1142|
| IEEE Xplore |242|54|433|81|

All 12 displayed counts match exported counts and unique native IDs. Every uncertainty set is a native-ID subset of its base set. The streams overlap and their counts must not be summed as independent studies.

19,963 source/query occurrences yield **9,952 conservatively deduplicated records**, 7,927 with a DOI. 10,011 repeated occurrences were collapsed using normalized exact DOI, or database-native ID when DOI is absent. **352 title/year candidate groups remain for manual duplicate review**; 9,952 is not a final count of eligible studies. No eligibility screening or full-text synthesis of this S4/S5 corpus has been performed.

## Files and reproducibility

- `protocol/`: source drafts, frozen protocol, exact queries, counts and export limitations.
- `raw/<database>/<query>.zip`: unchanged native CSV/TSV exports, compressed losslessly. Extract each archive into its containing folder to rebuild; filenames match `final/raw_manifest.csv` SHA-256 checksums.
- `final/screening_index.csv`: compact deduplicated bibliography, DOI and source/query membership.
- `final/full_tables.zip`: full deduplicated CSV (including abstracts), source-record CSV, and record-level membership CSV. All additional native source fields remain in the raw archives.
- `final/title_year_candidates.csv`: candidates requiring human duplicate adjudication; not silently merged.
- `final/search_counts.csv`, `subset_audit.csv`, `summary.json`: completeness and overlap audits.
- `code/build_dataset.py`: Python standard-library rebuild; run after extracting raw archives. Native columns are preserved in raw files, while harmonized fields support cross-database analysis.

## Field coverage and scope

Scopus S5 includes all selected bibliographic/abstract/keyword/funding fields **except cited-reference lists**, whose exports failed. S4 includes references. WoS includes full records and cited references. IEEE supplies its native CSV fields, including reference counts, not full reference lists. DOI blanks are retained; no DOI was guessed. See `protocol/export_notes.md`.

Scopus TITLE-ABS-KEY, WoS TS (including Keywords Plus), and IEEE metadata searches have different coverage and are not field-identical. Broad S5 decision terms may include operational-energy studies. Later screening must distinguish these from material flow, circularity and embodied-impact evidence. Retrieval membership does not establish an uncertainty-transfer mechanism or validate an architecture.

For the later synthesis, link S3 material outflow to S4 recovery/reuse yields, then S4 secondary-material quantities/quality to S5 environmental impacts and decisions. Extract input/output variables, units, dependency assumptions, transformations, uncertainty representations and page-level evidence. These are planned extraction dimensions, not findings established by this retrieval.
