# Scopus DT-UA: fresh complete architecture-focused search

Executed 2026-11-01 on the main Scopus domain with an active personal session and SLUB Dresden institutional access. Documents search, Article title, Abstract, Keywords:

```text
"digital twin" AND uncertainty AND (architectur* OR "probabilistic graphical model*" OR "Bayesian network*" OR "knowledge graph*" OR "data assimilation" OR "sensor fusion" OR "uncertainty propagation" OR provenance OR traceability OR "runtime verification")
```

Equivalent field wrapper: `TITLE-ABS-KEY ( <query above> )`. No year, language, subject, document-type or open-access restriction added. Preprints and secondary documents were not searched. Result count: **1,011**.

Select all → Export → CSV opened an **Export 1,011 documents to CSV** dialog. All five groups were checked: Citation information, Bibliographical information, Abstract & keywords, Funding details, Other information (including references). Every individual export field was verified selected. **Truncate to optimize for Excel was switched OFF**; Save as preference remained unchecked. One native export successfully delivered all results.

Native download `export_9715e547-0b06-4085-a60f-dbcc22f1eba3_2026-11-01T112132.029346108.csv` is retained byte-for-byte as `results/raw/SCOPUS_DTUA_1011.csv`, with SHA-256 manifest. All **45 original columns** are retained, including references, funding, affiliations, author identifiers and conference details. The merged CSV adds five provenance columns.

Validation: **1,011 rows, 1,011 unique EIDs**, 962 supplied DOI values, 49 missing DOIs, no blank abstracts but **one source placeholder `[No abstract available]`**. The source identifiers exactly equal the prior local 1,011-record match set; every native field value matches the broad baseline for those records. No new record lies outside the earlier 3,501-record Scopus corpus.

This is a newly executed database query and native export, not a relabelled local subset. It confirms the earlier local candidate set, without increasing baseline retrieval counts or making eligibility decisions. Rebuild with `python scripts/prepare_dtua_live.py`.
