# DT-UM: uncertainty recognition and inference mechanisms

Executed on 2026-11-01 in all three databases. **25 complete source records reduce to 18 unique DOI-identified publications after removing 7 duplicate occurrences. All 18 have a supplied DOI and an abstract.** These are candidates for detailed review, not 18 confirmed eligible studies.

| Database | Fresh results / exported records | Native fields | Missing DOI | Missing abstract |
|---|---:|---:|---:|---:|
| IEEE Xplore | 9 / 9 | 28 | 0 | 0 |
| Scopus | 13 / 13 | 45 | 0 | 0 |
| Web of Science Core Collection | 3 / 3 | 71 | 0 | 0 |

Every record belongs to its previous DT-UA architecture corpus. Do not add these counts to the broad review identification total. No date, language, document-type, subject or open-access restrictions were added. Source-supplied publication years, including 2027, are retained unchanged.

## Stronger distinction from DT-UA

DT-UA required a digital-twin phrase, uncertainty, and an architectural mechanism. DT-UM additionally requires **both** (1) terminology for recognizing model–measurement disagreement, distribution change or adaptive noise, **and** (2) terminology for inference or model/state updating. A match is lexical co-occurrence; it does not prove a causal connection between components.

The complete executable expression and term lists are in [query.json](query.json). Exact per-database queries and export settings are recorded in the three `searches/<database>/DT-UM/SEARCH_LOG.md` files. Scope is IEEE main Search by All, Scopus TITLE-ABS-KEY and WoS Topic (TS), respectively; these scopes and platform indexing are not identical.

The initial wildcard-heavy IEEE expression was rejected before execution because the interface permits at most 10 wildcards. Detection and inference stems were therefore replaced with explicit word forms; this same successful expression was used in all three databases. Finite forms operationalize the earlier exploratory local regex but do not cover every possible suffix. No rejected-query result count is reported as a completed search.

Prior exploratory local matches were IEEE 6, Scopus 13 and WoS 3. Fresh IEEE retrieval returned 9 and is authoritative for the new export. Additional database matches are retained, without inventing a reason for the discrepancy or excluding them on the basis of local matching alone.

## Complete data and traceability

- Raw: native IEEE and Scopus CSVs and WoS tab-delimited Full Record and Cited References export under each DT-UM search directory.
- Standardized source exports: `data/merged/IEEE_DTUM_9.csv`, `SCOPUS_DTUM_13.csv`, `WOS_DTUM_3.csv`, preserving every native field and adding provenance.
- [All 25 source records](all_25_source_records.csv): harmonized fields, explicit term/field matches, and complete native metadata in a JSON cell.
- [18 unique publications](deduplicated_publications.csv): DOI links, title, authors, abstract, year, source, database membership, source IDs, and all source metadata variants in a JSON cell.
- [Deduplication map](deduplication_map.csv): each original source record linked to its unique publication ID and merge basis.
- [Audit](audit.json): record counts, native column counts, raw SHA-256 hashes, completeness checks and deduplication results.

Scopus included all five field groups and cited references, with truncation OFF. WoS exported records 1–3 with Full Record and Cited References. IEEE supplied all native CSV fields, including reference counts but not full cited-reference lists. “Complete” means the entire result set and all metadata supplied by these native exports, not full-text PDFs or every optional field being populated.

## Deduplication decisions

Normalize DOI case, surrounding whitespace and a DOI URL/`doi:` prefix, then group on exact normalized DOI. The 25 records contain 18 distinct DOIs. Seven DOI groups each occur in two databases: four IEEE–Scopus and three Scopus–WoS. Five publications occur only in IEEE and six only in Scopus; no publication occurs only in WoS or in all three fresh result sets.

Matching DOI groups have no normalized-title or publication-year conflicts. Distinct DOI groups were checked for normalized-title similarity >=0.85; no pairs were flagged. Similar titles with different DOI would not be automatically merged. Missing-DOI records would remain separate for manual review; none occur in this retrieval. The deduplication unit is a publication, not a research project: conference/journal versions with different DOI would remain distinct.

Canonical display metadata use Scopus, then WoS, then IEEE when present. All source variants and identifiers remain available, so canonical selection cannot erase metadata. The raw exports are never deleted or modified. Conversion checks confirm every native cell survives in its merged source CSV. Every one of the 25 source IDs maps to exactly one of the 18 publication IDs.

## Detailed-review question and extraction fields

For each candidate, determine: **which component uses which observation and test to recognize uncertainty or model inadequacy, how it represents that uncertainty, and what it changes next?**

Extract: implemented DT boundary; measured and predicted variables; residual/innovation/drift statistic and threshold; distinction between physical change and model/data uncertainty; uncertainty source and type; representation (distribution, covariance, interval, etc.); inference/update algorithm; data/component interfaces and dependency assumptions; calibration/coverage or other validation evidence; decision/action triggered; online versus offline operation; and evidence location in full text.

Residuals, drift detection, Bayesian terminology or anomaly detection alone are insufficient evidence of uncertainty recognition. Reviews and broad adjacent methods remain in the candidate set until screening. Do not claim a universal architecture, research-gap prevalence, or end-to-end uncertainty continuity from keyword matches. This high-specificity subset can miss relevant work using other vocabulary; retain DT-U and DT-UA as the broader evidence base.

Rebuild with `python scripts/prepare_dtum.py`. All screening statuses are `not_screened`; full-text status is `not_assessed`.
