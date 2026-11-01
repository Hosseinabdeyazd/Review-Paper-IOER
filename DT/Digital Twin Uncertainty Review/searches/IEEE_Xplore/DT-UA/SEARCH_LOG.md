# IEEE DT-UA: fresh complete architecture-focused search

Executed 2026-11-01 through SLUB institutional access, using the main IEEE Xplore Search by All field:

```text
"digital twin" AND uncertainty AND (architectur* OR "probabilistic graphical model*" OR "Bayesian network*" OR "knowledge graph*" OR "data assimilation" OR "sensor fusion" OR "uncertainty propagation" OR provenance OR traceability OR "runtime verification")
```

A new main search removed the earlier baseline export content-type filters. The result page showed **349 results**, with only the query applied. No year, document-type or access restriction was added. This preserves the earlier IEEE general-search scope; it is not identical to WoS Topic or Scopus TITLE-ABS-KEY.

Export → Results → Download, with no result selection, explicitly included all 349 results. Native download `export2026.11.01-06.20.26.csv` is retained byte-for-byte as `results/raw/IEEE_DTUA_349.csv`; hash is in the adjacent manifest. All **28 native metadata columns** are retained. The merged CSV adds five provenance columns. This is the full native metadata export, not full-text article extraction; IEEE's native CSV includes reference counts rather than the full cited-reference lists supplied by Scopus/WoS.

Validation: **349 rows and 349 unique IEEE source identifiers**, 332 supplied DOI values, 17 missing DOIs, no blank abstracts. All records occur in the broad 1,228-record IEEE baseline, and all native metadata values match that baseline.

The prior local title/abstract/keyword procedure found 278 records; all 278 are present in the fresh search, alongside **71 additional records**. The fresh search is the authoritative retrieval result. The precise cause of each additional match has not been established; database search scope/indexing and term processing need not equal a regex on exported fields. Do not label these 71 records false positives or invent lexical evidence. They remain unscreened and are listed in `analysis/architecture_focus/fresh_search_vs_local_IEEE_SCOPUS.csv` and the audit.

Rebuild: `python scripts/prepare_dtua_live.py`. No baseline counts change and no cross-database deduplication is implied.
