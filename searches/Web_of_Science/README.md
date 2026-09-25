# Web of Science searches

This directory contains only the Web of Science Core Collection work completed to date. Search families S1-1, S1-2, S2-1, S2-2, S3-1, and S3-2 are part of the project plan; only S1-1 is represented here as a completed search/export. No S4 or S5 WoS searches are included.

## Current completed search

- **S1-1 Base** — executed 2026-09-25 in Web of Science Core Collection Advanced Search.
- Exact Scopus source and executed WoS query are under `S1/queries/`.
- Two raw WoS tagged Plain Text exports are preserved under `S1/results/raw/`.
- `S1/results/final/WOS_S1-1.csv` has 504 rows and is shaped to match the Scopus CSV schema, with WoS-only identifiers/metadata appended.
- `S1/results/final/WOS_S1-1_full_record_cited_references.txt` preserves the merged tagged export.
- Export counts, conversion notes, validation details, and search log are in `S1/results/metadata/`.
- Reusable conversion code is in `scripts/convert_wos_to_scopus_csv.py`.

The search strategies and conversion script are project-authored; the bibliographic records were exported from Web of Science Core Collection under the researcher’s authorized access.
