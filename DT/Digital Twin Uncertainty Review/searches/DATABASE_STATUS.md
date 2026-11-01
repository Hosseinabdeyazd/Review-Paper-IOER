# Database retrieval status — 2026-11-01

| Database | Executed search | Results shown | Records downloaded | Status |
|---|---|---:|---:|---|
| IEEE Xplore | General search: `"digital twin" AND uncertainty` | 1,228 | 1,228 | Complete metadata export; 2 exhaustive partitions |
| Scopus | Documents; Article title, Abstract, Keywords: `"digital twin" AND uncertainty` | 3,501 | 3,501 unique EIDs | Complete; 18 native batches, all 45 columns, truncation OFF |
| Web of Science Core Collection | Topic: `TS=("digital twin" AND uncertainty)` | 2,016 | 2,016 unique UTs | Complete; 5 native batches, all 71 columns, Full Record and Cited References |

## Scopus

Institutional access was confirmed by the SLUB Dresden banner. No date, language, subject, document-type or open-access restriction was applied. The search ran on the Documents tab, not Preprints or Secondary documents. The result list separately says it displays up to 2,000 results; **3,501 is the search count, not an export count**.

Complete retrieval is now verified on the main `www.scopus.com` domain with active personal session and SLUB access. Native current-page exports with all information selected and truncation OFF cover Date (newest) pages 1–10 and Date (oldest) pages 1–8, 200 records per page. The 3,600 raw rows contain 3,501 unique EIDs and 99 identical repeated occurrences. All 45 native fields are retained. There are 3,315 supplied DOIs and 186 blank DOI values; 9 abstracts use the source placeholder `[No abstract available]`. No source record was excluded. Full-range attempts did not yield verified files; page-wise retrieval resolved that issue. The earlier diagnostic sample is not part of this final corpus. No credentials were saved in project files. See `Scopus/DT-U/SEARCH_LOG.md` and the machine-readable audit for complete reconciliation.

Earlier proxy-domain behavior: Select all → Export requested a personal Scopus account; institutional sign-in returned to ScienceDirect. The main-domain session resolved that login issue without entering a password or creating an account.

Access source: [SLUB DBIS Scopus](https://dbis.ur.de/SLUB/resources/3636).

## Web of Science

The user completed access through the [SLUB DBIS route](https://dbis.ur.de/SLUB/resources/3366), resolving the earlier browser navigation block. Core Collection and the personal session were verified on the institutional proxy. No credentials were stored in project files.

Executed search: Core Collection, Topic `TS=("digital twin" AND uncertainty)`, All available editions, no added date/filter restrictions. All 2,016 results were exported as Full Record and Cited References in five contiguous ranges (1–500, 501–1000, 1001–1500, 1501–2000, 2001–2016). Validation confirms 2,016 unique UTs, no duplicate UTs and identical 71-column schemas. There are 1,944 DOI values, 72 blank DOIs, three blank abstracts and three blank reference fields. All source rows and fields are retained. Edition coverage, hashes and reproducible processing are documented in `Web_of_Science/DT-U/SEARCH_LOG.md` and the audit.

Search fields and indexing differ between platforms, so the counts must not be treated as directly equivalent. Cross-database deduplication has not been performed.



## Final-data publication requirement

Only complete, verified database exports should be published as final data. Diagnostic samples are not deliverables. Reconcile expected and downloaded counts and unique source identifiers. Retain every supplied metadata field, including DOI, abstract and keywords. Report missing source fields explicitly; do not invent missing DOIs. Metadata-complete retrieval does not mean final eligibility screening or full-text architectural validation is complete.
