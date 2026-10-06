# Analysis-ready merged datasets

This folder is intended for database-agnostic analysis of S1-S3 after cross-database deduplication.

Expected outputs:
- `S1/S1b.csv` — S1 base layer
- `S1/S1u.csv` — S1 uncertainty-focused layer
- `S2/S2b.csv` — S2 base layer
- `S2/S2u.csv` — S2 uncertainty-focused layer
- `S3/S3b.csv` — S3 base layer
- `S3/S3u.csv` — S3 uncertainty-focused layer

Deduplication rule:
1. normalized DOI is the primary key;
2. normalized title is the fallback key when DOI is missing;
3. database provenance and platform identifiers are retained;
4. descriptive fields keep the most complete non-empty value; keyword/provenance fields are combined.

The analysis-ready files use a harmonized schema containing title, authors, year, source title, abstract, keywords, DOI, affiliations, document type, citations, references, provenance, platform IDs, source files, deduplication key, and database count.

## S1 uncertainty note

The archived Scopus S1 base export contains 726 records. A separately confirmed Scopus S1 uncertainty export is not currently archived. Therefore, the Scopus contribution to S1u is reconstructed by applying the frozen uncertainty vocabulary to Title, Abstract, Author Keywords, and Index Keywords of the 726-record S1 base export. This reconstruction should be checked against a re-executed Scopus S1 uncertainty query before the final review dataset is frozen.

## Current merged counts

- S1b: 878 unique records from 1,400 database records; 522 duplicates removed.
- S1u: 256 unique records from 410 database records; 154 duplicates removed.
- S2b: 246 unique records from 419 database records; 173 duplicates removed.
- S2u: 44 unique records from 75 database records; 31 duplicates removed.
- S3b: 165 unique records from 272 database records; 107 duplicates removed.
- S3u: 49 unique records from 80 database records; 31 duplicates removed.
