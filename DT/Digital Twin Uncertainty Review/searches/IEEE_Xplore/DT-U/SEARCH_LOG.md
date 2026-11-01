# IEEE DT-U search and export log

- Retrieval date: 2026-11-01, user timezone Europe/Berlin.
- Access: IEEE Xplore through SLUB Dresden / DBoD; institutional access confirmed in the interface.
- Executed query: `"digital twin" AND uncertainty` through the general search box. No manually imposed date, language, subject or publication-type restriction in the parent query. Search-field scope is the platform default for this search, not asserted equivalent to Scopus TITLE-ABS-KEY or WoS TS.
- Parent result count: **1,228**.
- Export: native Export → Results → CSV; full metadata including abstracts and keywords when supplied.
- The export dialog caps a download at 1,000 records. Combining relevance/oldest/newest top-1,000 downloads yielded only 1,218 unique links, so those exploratory batches were not used as the final corpus.
- Final method: exhaustive content-type partition, newest-first within each partition.

| Batch | UI filter | UI count | Export rows |
|---|---|---:|---:|
| IEEE_DTU_conferences_809.csv | Conferences | 809 | 809 |
| IEEE_DTU_other_types_419.csv | Journals OR Books OR Magazines OR Early Access Articles OR Standards | 419 | 419 |

The second UI partition comprises Journals 285, Books 53, Magazines 44, Early Access 36 and Standards 1. Native `Document Identifier` has more granular publisher labels, so its counts differ from these UI labels.

Original downloads: `export2026.11.01-04.53.41.csv` and `export2026.11.01-04.54.23.csv`, respectively. Their filename times are not interpreted as timezone-qualified timestamps.

Reconciliation: **809 + 419 = 1,228 rows; 1,228 unique IEEE item identifiers; zero overlap.** Identifiers are parsed from `arnumber` or ebook `fileName` in the native PDF Link. All 28 native columns are retained. Row-level provenance records the batch filename and CSV row (header is row 1). Raw file hashes are in `results/raw/manifest.json`.

Data quality: 62 blank DOIs and 2 blank abstracts. Some ebook chapter records carry volume-level descriptions instead of chapter abstracts; these must not support chapter-specific claims. Publication years span 2016–2027; the 2027 metadata entry is retained as exported, not silently removed or treated as retrieval after 2026.

No full-text PDFs were downloaded in this metadata export. No record was excluded or automatically judged eligible.
