# Web of Science searches

This directory contains only the Web of Science Core Collection work completed to date. Search families S1-1 and S1-2 are completed here. S2-1, S2-2, S3-1, and S3-2 remain pending. No S4 or S5 WoS searches are included.

## Current completed search

- **S1-1 Base** — 504 records; executed 2026-09-25 in Web of Science Core Collection Advanced Search.
- **S1-2 Base + uncertainty** — 152 records; executed 2026-09-25 in Web of Science Core Collection Advanced Search.
- Each variant has its own query folder under `S1/queries/S1-1_base/` or `S1/queries/S1-2_uncertainty/`, containing the Scopus source and executed WoS query.
- Raw WoS tagged Plain Text exports are preserved under `S1/results/raw/`.
- `S1/results/final/WOS_S1-1.csv` (504 rows) and `WOS_S1-2.csv` (152 rows) match the Scopus CSV schema, with WoS-only identifiers/metadata appended.
- Merged tagged exports are preserved in `S1/results/final/` as `WOS_S1-1_full_record_cited_references.txt` and `WOS_S1-2_full_record_cited_references.txt`.
- Export counts, conversion notes, validation details, and search log are in `S1/results/metadata/`.
- Reusable conversion code is in `scripts/convert_wos_to_scopus_csv.py`.

The search strategies and conversion script are project-authored; the bibliographic records were exported from Web of Science Core Collection under the researcher’s authorized access.
