# Web of Science Core Collection searches

This directory contains local WoS Core Collection query and export files. S1-1, S1-2, S2-1, and S2-2 have results. S3-1 and S3-2 remain pending. No S4 or S5 WoS searches are included.

## Completed searches

- **S1-1 Base:** 504 records.
- **S1-2 Base + uncertainty:** 152 records.
- **S2-1 Base:** 182 records.
- **S2-2 Base + uncertainty:** 32 records.
- Each S2 variant has a separate query directory containing the canonical Scopus source query and its WoS translation.
- Uploaded WoS tagged Plain Text exports are preserved under each search family’s `results/raw/` folder. Final tagged exports and Scopus-schema CSVs are in `results/final/`.
- S2 validation summaries, run metadata, and conversion notes are under `S2/results/metadata/`; the family-wide search log is `search_log.csv`.
- The reusable converter is `scripts/convert_wos_to_scopus_csv.py`.

The tagged export files contain Full Record and Cited References fields. Optional fields can be blank when WoS does not provide them for a record.
