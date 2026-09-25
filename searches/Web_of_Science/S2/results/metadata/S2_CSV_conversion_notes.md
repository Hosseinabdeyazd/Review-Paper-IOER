# S2 WoS export conversion notes

- The uploaded files were WoS tagged Plain Text exports with Full Record and Cited References fields.
- Original upload bytes are preserved in `results/raw/`; the same records are copied to `results/final/` as the merged tagged-text deliverables because each search arrived as one file.
- CSV files were produced with `../../scripts/convert_wos_to_scopus_csv.py`, retaining Scopus column names/order and appending WoS-only fields.
- S2-1: 182 records, 182 unique WoS accession numbers (UT), 0 duplicate UTs, 54 columns. One WoS correction record has no abstract; it is retained because WoS returned it.
- S2-2: 32 records, 32 unique UTs, 0 duplicate UTs, 54 columns. All 32 UTs are in S2-1, and all 32 have an uncertainty term in title, abstract, author keywords, or Keywords Plus.
- All records in both exports have a title, full author names, affiliations, and cited references. Optional metadata such as abstracts, keywords, DOI, ISSN/ISBN, and funding may be absent on some records.
- The TXT export itself does not store the executed query string or the selected database collection. The query file associated with each export is identified by the user-provided search label and saved alongside the Scopus source query.
