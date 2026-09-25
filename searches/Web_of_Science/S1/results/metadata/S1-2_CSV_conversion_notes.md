# S1-2 CSV conversion notes

- Source: one Web of Science Core Collection Plain Text export, configured as `Full Record and Cited References`.
- 152 records exported; 152 unique WoS UT values; all 152 UTs are present in S1-1, as expected for S1-2 (Base + uncertainty).
- Output `WOS_S1-2.csv` keeps the 45 Scopus CSV columns in their exact order and appends nine labelled WoS-specific columns.
- Scopus-specific author IDs and EID remain blank. WoS ResearcherID, ORCID, and UT are kept separately.
- WoS `DE` maps to `Author Keywords`; WoS `ID` (Keywords Plus) maps to `Index Keywords` and is also retained as `Keywords Plus`.
- WoS `TC` maps to `Cited by`; `Z9` is retained separately as Times Cited All Databases.
- No duplicate records were removed. Empty optional fields indicate missing/not-indexed source values.
- Conversion code: `searches/Web_of_Science/scripts/convert_wos_to_scopus_csv.py`.
