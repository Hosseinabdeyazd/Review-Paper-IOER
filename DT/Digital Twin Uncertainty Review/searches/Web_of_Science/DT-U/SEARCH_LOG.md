# Web of Science DT-U — complete retrieval

- Date: 2026-11-01. User completed institutional access through SLUB; the proxy-hosted Core Collection advanced-search page was accessible with an active personal session. The earlier navigation blocker is resolved.
- Executed query: `TS=("digital twin" AND uncertainty)`; **2,016 results**. The interface identifies `TS` as Topic. This is not the same search field definition as Scopus Title/Abstract/Keywords or IEEE general search.
- Database: **Web of Science Core Collection**; Editions: **All**. No date, language, document-type, subject or access filter added. No date clause in the query.
- Selected editions and coverage displayed: SCI-EXPANDED 1900–present; SSCI 1956–present; AHCI 1975–present; CPCI-S and CPCI-SSH 1990–present; BKCI-S, BKCI-SSH and ESCI 2005–present; CCR-EXPANDED 1990–present; IC 1993–present. These are available edition coverage limits, not publication-year exclusions applied by this review.
- Sort: Relevance. Native format: Tab delimited file. Content: **Full Record and Cited References**. This option limits each export to 500 records.

## Export reconciliation

| Native download | Published raw filename | Result positions | Rows |
|---|---|---|---:|
| savedrecs.txt | WOS_DTU_0001_0500.tsv | 1–500 | 500 |
| savedrecs (1).txt | WOS_DTU_0501_1000.tsv | 501–1000 | 500 |
| savedrecs (2).txt | WOS_DTU_1001_1500.tsv | 1001–1500 | 500 |
| savedrecs (3).txt | WOS_DTU_1501_2000.tsv | 1501–2000 | 500 |
| savedrecs (4).txt | WOS_DTU_2001_2016.tsv | 2001–2016 | 16 |

**2,016 raw rows = 2,016 unique UT accession identifiers**, with zero duplicate UTs. All five files have the same 71 native columns. Source bytes are preserved; only filenames/extensions change. SHA-256 hashes are recorded in `results/raw/manifest.json`.

The merged CSV retains all 71 original fields, plus five provenance columns. Native tags remain unchanged: `UT` accession identifier, `DI` DOI, `TI` title, `AB` abstract, `DE` author keywords, `ID` Keywords Plus, `CR` cited references, `WE` source indexes. All other tags and values are retained as supplied, including author names/identifiers, affiliations, correspondence, funding, publication details, subject categories and citation metrics.

**1,944 records have DOI values; 72 are blank. Three abstracts and three cited-reference fields are blank.** Future publication years, including 35 records labelled 2027, are retained as supplied. No source record was excluded or edited to fabricate missing information.

Run `python scripts/prepare_wos.py` to rebuild the merged CSV, manifest, audit and lexical queue. Eligibility screening and full-text architecture verification are not complete. The three database record counts must not be interpreted as unique studies without cross-database reconciliation.
