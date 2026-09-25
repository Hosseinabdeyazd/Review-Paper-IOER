# Web of Science S2 results

Searches completed on 2026-09-25 in the S2 family:

| Variant | Exported records | Final CSV | Validation |
|---|---:|---|---|
| S2-1 Base | 182 | `results/final/WOS_S2-1.csv` | 182 unique UTs; no duplicate UTs; 1 correction record has no abstract |
| S2-2 Base + uncertainty | 32 | `results/final/WOS_S2-2.csv` | 32 unique UTs; all are contained in S2-1; all match an uncertainty term |

## Files

- `queries/S2-1_base/` and `queries/S2-2_uncertainty/` each contain the canonical Scopus source query and the corresponding WoS query.
- `results/raw/` contains byte-identical copies of the supplied raw WoS tagged exports.
- `results/final/` contains the Full Record and Cited References tagged text plus CSV files with the Scopus column schema and appended WoS fields. Each CSV has 54 columns.
- `results/metadata/` contains run records, export validation, conversion notes, and SHA-256 hashes.
- The conversion script is `../scripts/convert_wos_to_scopus_csv.py`.

All records have titles, author full names, affiliations, and cited references. The S2-1 correction record without an abstract was kept because it is part of the retrieved WoS set. Optional fields can be blank. The tagged export does not itself store the executed query string or collection selection; the query-to-export association follows the supplied S2 labels and saved query files.
