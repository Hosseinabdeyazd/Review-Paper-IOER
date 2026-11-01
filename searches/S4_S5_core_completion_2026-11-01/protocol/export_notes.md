# Export log and limitations

Scopus S5-1 (6621): four disjoint export partitions, unchanged parent query:
- AND PUBYEAR > 2023: 2208
- AND PUBYEAR > 2018 AND PUBYEAR < 2024: 2358
- AND PUBYEAR > 2013 AND PUBYEAR < 2019: 1150
- AND PUBYEAR < 2014: 905
Sum 6621, 6621 distinct EIDs. This is a download partition, not a date restriction on the corpus.

Scopus S5 exports with all information including references repeatedly failed to deliver a file within the download wait. Native CSV exports excluding only Include references succeeded. S5-2: all 1359 records in one file; S5-1: partitions above. Full references are therefore NOT available for these two Scopus sets. S4 exports include references. Unsuccessful full-set and pre-2019 export attempts are not counted as files or as additional results. No samples are used.

WoS: full record and cited references, batches of at most 500; ranges are encoded in filenames. Literal unescaped quotation marks in WoS TSV require csv.QUOTE_NONE. Initial conventional CSV quoting undercounted the first S4 batch by 14; direct row and unique-UT validation resolved this. Re-export returned the same content; no records were missing. A human-verification challenge during S5 export was completed by the user. All native identifiers match the displayed counts.

IEEE: unselected full-results CSV exports (242,54,433,81) include abstracts, DOI where supplied, keywords, affiliations and reference counts; the exporter does not provide full reference lists. All queries accepted without splitting. No full-text corpus is claimed here.

DOI blanks remain blanks. DOI presence means a value supplied by a database, not independent DOI-resolution validation. Abstract text may contain database placeholders; nonempty counts do not guarantee a substantive abstract. No missing metadata is invented.
