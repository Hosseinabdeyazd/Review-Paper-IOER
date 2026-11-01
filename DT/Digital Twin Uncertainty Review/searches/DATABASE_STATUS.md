# Database retrieval status — 2026-11-01

| Database | Executed search | Results shown | Records downloaded | Status |
|---|---|---:|---:|---|
| IEEE Xplore | General search: `"digital twin" AND uncertainty` | 1,228 | 1,228 | Complete metadata export; 2 exhaustive partitions |
| Scopus | Documents; Article title, Abstract, Keywords: `"digital twin" AND uncertainty` | 3,501 | 3,501 unique EIDs | Complete; 18 native batches, all 45 columns, truncation OFF |
| Web of Science | Not yet executed | Not established | 0 | SLUB access page reached; browser navigation blocked |

## Scopus

Institutional access was confirmed by the SLUB Dresden banner. No date, language, subject, document-type or open-access restriction was applied. The search ran on the Documents tab, not Preprints or Secondary documents. The result list separately says it displays up to 2,000 results; **3,501 is the search count, not an export count**.

Complete retrieval is now verified on the main `www.scopus.com` domain with active personal session and SLUB access. Native current-page exports with all information selected and truncation OFF cover Date (newest) pages 1–10 and Date (oldest) pages 1–8, 200 records per page. The 3,600 raw rows contain 3,501 unique EIDs and 99 identical repeated occurrences. All 45 native fields are retained. There are 3,315 supplied DOIs and 186 blank DOI values; 9 abstracts use the source placeholder `[No abstract available]`. No source record was excluded. Full-range attempts did not yield verified files; page-wise retrieval resolved that issue. The earlier diagnostic sample is not part of this final corpus. No credentials were saved in project files. See `Scopus/DT-U/SEARCH_LOG.md` and the machine-readable audit for complete reconciliation.

Earlier proxy-domain behavior: Select all → Export requested a personal Scopus account; institutional sign-in returned to ScienceDirect. The main-domain session resolved that login issue without entering a password or creating an account.

Access source: [SLUB DBIS Scopus](https://dbis.ur.de/SLUB/resources/3636).

## Web of Science

The [SLUB DBIS entry](https://dbis.ur.de/SLUB/resources/3366) identifies its licensed Core Collection and access route. The browser security policy rejected navigation using the page's “Zur Datenbank” link, reporting an invalid URL. No alternate route was used to circumvent the rejection. User assistance opening the database is pending.

Planned comparable search: Core Collection, Topic `"digital twin" AND uncertainty` (advanced form `TS=("digital twin" AND uncertainty)`). Record the actual collection, available indexes, timespan and query when executed. This is **planned, not executed**.

Search fields and indexing differ between platforms, so the counts must not be treated as directly equivalent. Cross-database deduplication has not been performed.



## Final-data publication requirement

Only complete, verified database exports should be published as final data. Diagnostic samples are not deliverables. Reconcile expected and downloaded counts and unique source identifiers. Retain every supplied metadata field, including DOI, abstract and keywords. Report missing source fields explicitly; do not invent missing DOIs. Metadata-complete retrieval does not mean final eligibility screening or full-text architectural validation is complete.
