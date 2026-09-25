# S1-1 CSV conversion notes

- Source: the two Web of Science Core Collection Plain Text exports, both configured as `Full Record and Cited References`.
- Output: `../final/WOS_S1-1.csv`, with the exact 45 Scopus CSV columns in their original order, followed by nine explicitly labelled WoS-specific columns.
- All 504 WoS records are retained. Deduplication uses WoS UT first, DOI second, and normalized title only when UT and DOI are missing. This run had 504 distinct UTs and removed 0 duplicates.
- `Author(s) ID` and `EID` are Scopus-specific and remain blank. WoS ResearcherID, ORCID, and UT are preserved in separate added columns.
- WoS `DE` maps to Scopus `Author Keywords`; WoS `ID` (Keywords Plus) maps to `Index Keywords` and is also retained as `Keywords Plus`.
- WoS `TC` maps to `Cited by`; `Z9` (Times Cited, All Databases) is retained separately.
- WoS fields are not present for every record. Empty cells reflect missing/not-indexed source values, not dropped records.
- The converter uses only the Python standard library and preserves all bibliographic text in the raw WoS exports.

To reproduce from this directory's parent:

```bash
python scripts/convert_wos_to_scopus_csv.py \
  S1/results/raw/WOS_S1-1_part001.txt \
  S1/results/raw/WOS_S1-1_part002.txt \
  --output S1/results/final/WOS_S1-1.csv
```
