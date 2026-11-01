# Digital twin bridge searches: S1–S2 and S2–S3

Search date: 2026-11-01. This is a completed retrieval and deduplication release, not a full-text screening result.

| Database | S1→S2 (B12) | S2→S3 (B23) |
|---|---:|---:|
| IEEE Xplore | 4 | 0 |
| Scopus | 36 | 11 |
| Web of Science Core Collection | 23 | 9 |
| Total source occurrences | 63 | 20 |

83 source occurrences become **43 unique bibliographic records** after removing 40 duplicate occurrences. B12 contains 42 unique records, B23 contains 13, and 12 occur in both. 37 unique records have a source-provided DOI; six have no DOI in the retrieved exports. These are records, not necessarily 43 individual research articles: the corpus includes reviews, chapters and conference-volume records.

## Search logic

- B12: Digital Twin AND built-environment context AND observation/model-information terms AND material-inventory terms.
- B23: Digital Twin AND built-environment context AND material-inventory terms AND flow/lifetime/change-event terms.
- Exact strings and term blocks are preserved in `protocol/queries.json`.
- Scopus: TITLE-ABS-KEY. Web of Science: TS (including Keywords Plus). IEEE: standard search queryText, with its native search scope. These fields are not identical across databases.
- No year, language, document-type or open-access filters were applied. Displayed year ranges reflect retrieved records, not imposed restrictions.
- This version requires terms from both adjacent stages. Compared with the broad S1–S5 stream, it also changes context terms and adds BIM/GIS/IFC input vocabulary. It is a new bridge query, not a mathematically guaranteed subset of the earlier corpus.
- No mandatory uncertainty, architecture or algorithm block was added: those requirements could exclude relevant interface architectures. Co-occurrence does not establish that a paper implements the directional transfer or propagates uncertainty.

## Files and provenance

- `raw/`: unchanged native exports. Scopus has 45 fields with all information selected; IEEE has 28 native CSV fields; WoS has 71 fields with Full Record and Cited References selected.
- `converted/`: WoS exports converted losslessly to CSV using the native field names.
- `analysis/source_records.csv`: normalized metadata for every occurrence, with native file and record references.
- `analysis/deduplicated_records.csv`: the 43-record review queue. The longest available abstract supplies the representative normalized metadata; other source variants remain in the raw exports.
- `analysis/bridge_source_membership.csv`: links every unique record to every source occurrence and bridge.
- `analysis/possible_title_duplicates.csv`: exact normalized-title/year candidates not already DOI/native-ID merged; none found in this release.
- `analysis/missing_doi.csv`: six records for which the native exports contain no DOI. Blank does not establish that no DOI exists.
- `protocol/search_log.csv` and `file_manifest.csv`: count reconciliation and raw-file hashes.
- `protocol/IEEE_B23_zero_results.md`: zero-result observation. No fictitious native export was created for this query.
- `code/build_dataset.py`: Python 3 standard-library rebuild, run with `python code/build_dataset.py` from any directory.

Deduplication normalizes DOI prefixes/case and merges exact DOI matches. Without DOI it uses database plus native identifier, avoiding automatic fuzzy-title merges. Conference papers, chapters and later journal versions are not merged merely because they are similar. Raw exports remain unchanged. Missing metadata is not fabricated. The exported metadata includes abstracts, authors, affiliations, keywords, citation/reference fields and other details where the database supplies them; it is not full text.

## Next screening question

For B12, identify an explicit conversion from observations/BIM/GIS entities to material quantities or component inventories, including identifiers, units, transformation rules and validation. For B23, identify how an inventory becomes dated inflows/outflows using lifetime, demolition, renovation or replacement models. Then inspect whether uncertainty is represented at input, transformed through the operation, retained at output and updated by new observations. Search membership alone is not evidence of these capabilities.
