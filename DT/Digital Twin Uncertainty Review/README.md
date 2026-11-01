# Digital Twin Uncertainty Review

## Status, 1 November 2026

IEEE DT-U retrieval is complete: **1,228 unique records**, with no exclusions. The corpus is the result of the executed query `"digital twin" AND uncertainty`, not a final set of eligible studies. Architecture findings are an initial analysis of exported titles, abstracts and keywords. Full texts have not yet been assessed.

Scopus DT-U retrieval is complete: **3,501 unique EIDs**, retaining all 45 native metadata columns without Excel truncation. Eighteen 200-record native exports contain 3,600 rows and 99 identical repeated occurrences. There are 3,315 supplied DOIs, 186 missing DOI values and 9 source placeholders for unavailable abstracts. All records are retained. Web of Science retrieval is also complete: **2,016 unique UTs**, all 71 native fields, including cited references; 1,944 DOI values, 72 blank DOIs and three blank abstracts. The user resolved the earlier access block. See `searches/DATABASE_STATUS.md`.

This separate review stream follows the existing IOER repository workflow (queries, raw exports, merged data, screening/coding, analysis and reproducible scripts). It does not replace the S1–S5 evidence or their search counts.

## Files

- `searches/IEEE_Xplore/DT-U/results/raw/`: two untouched native CSV exports and their SHA-256 manifest.
- `searches/IEEE_Xplore/DT-U/SEARCH_LOG.md`: query, access route, filters and export reconciliation.
- `data/merged/IEEE_DTU_1228.csv`: all original columns plus stable ID and row-level provenance.
- `analysis/IEEE_mechanism_triage_1228.csv`: transparent lexical flags for every record; no inclusion/exclusion decisions.
- `analysis/IEEE_corpus_audit.json`: counts and data-quality checks.
- `analysis/ARCHITECTURE_FINDINGS.md`: mechanism synthesis, evidence and limits.
- `analysis/architecture_evidence.csv`: manually interpreted abstract-level evidence.
- `scripts/prepare_ieee.py`: standard-library Python pipeline, runnable from any working directory.
- `searches/Scopus/DT-U/results/raw/`: all 18 native CSV batches and hash/provenance manifest.
- `searches/Scopus/DT-U/SEARCH_LOG.md`: complete search and export reconciliation.
- `data/merged/SCOPUS_DTU_3501_parts/`: seven complete CSV partitions (six × 500 and one × 501), retaining 45 source columns plus four provenance columns. Together they contain all 3,501 records; a manifest records counts and hashes. The single 49 MB CSV exceeded the GitHub connector request limit; `prepare_scopus.py` also rebuilds that unified file locally.
- `analysis/SCOPUS_corpus_audit.json`: completeness, field missingness and maximum field lengths.
- `analysis/SCOPUS_mechanism_triage_3501.csv`: lexical reading queue; all records remain not screened.
- `analysis/SCOPUS_ARCHITECTURE_FINDINGS.md`: selected abstract-level architecture evidence and limits.
- `scripts/prepare_scopus.py`: reproducible validation, merge and triage pipeline.

The earlier 25-record pilot files are historical and superseded for corpus counts. They are not appended to the native export.

## Web of Science outputs

- `searches/Web_of_Science/DT-U/results/raw/`: five native tab-delimited exports and hash manifest.
- `searches/Web_of_Science/DT-U/SEARCH_LOG.md`: query, editions, coverage and export reconciliation.
- `data/merged/WOS_DTU_2016.csv`: all 71 source fields plus five provenance columns.
- `analysis/WOS_corpus_audit.json` and `analysis/WOS_mechanism_triage_2016.csv`: complete quality audit and lexical reading queue.
- `analysis/WOS_ARCHITECTURE_FINDINGS.md`: selected abstract-level evidence and interpretation limits.
- `scripts/prepare_wos.py`: reproducible validation and processing.

## Review design and connection to S1–S5

DT-A (architecture baseline), DT-U (uncertainty) and DT-P (propagation/interfaces) are distinct review streams. Only the initial DT-U query has been executed here. DT-A and DT-P require their own documented searches; this one query is not an exhaustive search of architecture literature.

Keep the broad DT review domain-independent first. Later map eligible systems/interfaces to the existing chain: S1 GeoAI/building-stock inference, S2 stock representation, S3 temporal dynamics, S4 circularity, and S5 environmental impacts. Treat those labels as an initial crosswalk to the user's handoff and confirm against the main review codebook before final coding. S4–S5 remain draft in the existing repository.

The extraction unit should be **study → DT system → component → interface → decision/outcome**. Record uncertainty source/type/representation, input and output variables, units, temporal/spatial support, dependencies, propagation method, updates, provenance, validation evidence, and decision use. Separate conceptual/proposed/implemented status from simulation/experiment/deployment validation. Use `not_assessed` when evidence has not been checked; never interpret it as uncertainty being lost.

IEEE, Scopus and Web of Science are retrieved as separate source corpora. Do not interpret their summed counts as unique studies before cross-database deduplication. Preserve source-specific records, then use normalized DOI plus manual title/year verification for matching. A missing DOI does not justify dropping a record or automatically merging versions.



## Final-data publication requirement

Only complete, verified database exports should be published as final data. Diagnostic samples are not deliverables. Reconcile expected and downloaded counts and unique source identifiers. Retain every supplied metadata field, including DOI, abstract and keywords. Report missing source fields explicitly; do not invent missing DOIs. Metadata-complete retrieval does not mean final eligibility screening or full-text architectural validation is complete.
