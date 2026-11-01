# Database retrieval status — 2026-11-01

| Database | Executed search | Results shown | Records downloaded | Status |
|---|---|---:|---:|---|
| IEEE Xplore | General search: `"digital twin" AND uncertainty` | 1,228 | 1,228 | Complete metadata export; 2 exhaustive partitions |
| Scopus | Documents; Article title, Abstract, Keywords: `"digital twin" AND uncertainty` | 3,501 | 10 | Personal session active; first-page diagnostic export verified; full export unresolved |
| Web of Science | Not yet executed | Not established | 0 | SLUB access page reached; browser navigation blocked |

## Scopus

Institutional access was confirmed by the SLUB Dresden banner. No date, language, subject, document-type or open-access restriction was applied. The search ran on the Documents tab, not Preprints or Secondary documents. The result list separately says it displays up to 2,000 results; **3,501 is the search count, not an export count**.

Update: the main `www.scopus.com` domain has an active personal session and SLUB access. The same query returned 3,501 results there. Thus personal login is no longer the blocker. Native CSV export of the current first page succeeded: `Scopus/DT-U/results/pilot/SCOPUS_DTU_first_page_10.csv`, 10 rows and 10 unique EIDs, citation fields plus abstracts/keywords. This is a diagnostic sample, not a screened or representative set. Full-range and 500-record export attempts did not yield a verified local file despite a site success toast. The browser download wait expired. Full-corpus completeness is not established. No credentials were saved in project files.

Earlier proxy-domain behavior: Select all → Export requested a personal Scopus account; institutional sign-in returned to ScienceDirect. The main-domain session resolved that login issue without entering a password or creating an account.

Access source: [SLUB DBIS Scopus](https://dbis.ur.de/SLUB/resources/3636).

## Web of Science

The [SLUB DBIS entry](https://dbis.ur.de/SLUB/resources/3366) identifies its licensed Core Collection and access route. The browser security policy rejected navigation using the page's “Zur Datenbank” link, reporting an invalid URL. No alternate route was used to circumvent the rejection. User assistance opening the database is pending.

Planned comparable search: Core Collection, Topic `"digital twin" AND uncertainty` (advanced form `TS=("digital twin" AND uncertainty)`). Record the actual collection, available indexes, timespan and query when executed. This is **planned, not executed**.

Search fields and indexing differ between platforms, so the counts must not be treated as directly equivalent. Cross-database deduplication has not been performed.

