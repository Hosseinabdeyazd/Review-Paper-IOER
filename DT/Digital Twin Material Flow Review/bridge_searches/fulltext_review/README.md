# S1–S2 and S2–S3 full-text screening

Screened all 43 unique records from the completed three-database bridge search. See [Persian synthesis](REPORT_FA.md), [all screening decisions](screening_43.csv), [mechanism extraction](extraction_14.csv), and [access manifest](fulltext_manifest.csv).

Scope: building observations/geometry/typology → material inventory (B12); material inventory → time-indexed release/replacement flows (B23). Construction logistics and scheduling are retained as explicitly labelled methodological complements, not conflated with building-stock turnover.

Counts: 8 core candidates, 6 complements, 18 background records, 11 exclusions. Fourteen full-text targets; 12 retrieved (5 PDFs, 7 saved web article bodies), two pending. Core retention is not a claim of implemented uncertainty propagation. Single AI-assisted screener; not independently double-screened.

The strongest direct bridge is Ettl et al. (10.1007/978-981-96-6657-7_7): CityGML → synthetic component masses → layer service lives → annual outflow CSV. Alternative compositions are averaged, and reference service lives/scenarios determine timing. Explicit end-to-end probabilistic uncertainty continuity is not demonstrated in the examined methods. The uncertainty ledger and joint-realization propagation described in the report are review proposals, not reported implementations.

## Evidence rules

- `full_text` / `full_article_body` refer to accessible complete articles, with targeted methods/results/limitations examination. Sources and section/page locators are in each row.
- `abstract_only_pending_fulltext` rows must not support mechanistic or negative full-text claims.
- Error metrics, material traceability, deterministic sensitivity and uncertainty propagation are separate fields.
- Empty DOI values remain empty when no DOI was established. No guessed identifiers.
- `stages` in the original data indicate query membership; `assessed_bridge` is the review assessment. These are different.
- Possible proceedings/journal versions are not silently merged. The 43-record input is preserved.

Full texts are local-only. Public outputs contain bibliographic identifiers, analytical paraphrases, source links and access statuses; no credentials, browser tokens or publisher PDFs.

Run `python code/rebuild_tables.py` from any directory to validate and rebuild screening, selection, extraction and summary from the versioned review inputs. Manual scientific decisions are explicit inputs; the script does not classify papers by keywords.

Access update: Taylor & Francis institutional sign-in succeeded, but the chapter page explicitly states that the institution has not purchased DOI 10.1201/9781003677895-269. Springer DOI 10.1007/978-3-032-18712-3_19 remains a subscription preview. These two records remain abstract-only pending full text.

