# Scopus S1-1 result set

The complete S1-1 Scopus export contains **726 records** and preserves the full Scopus CSV field set.

The raw export is stored as four non-overlapping parts:

- `SCOPUS_S1-1_part001.csv`: records 1–181
- `SCOPUS_S1-1_part002.csv`: records 182–362
- `SCOPUS_S1-1_part003.csv`: records 363–543
- `SCOPUS_S1-1_part004.csv`: records 544–726

Each part repeats the original header row so that every file can be read independently. Concatenating the data rows in part order reconstructs the complete 726-record export.
