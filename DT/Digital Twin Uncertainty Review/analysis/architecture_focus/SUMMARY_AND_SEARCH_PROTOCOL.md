# Architecture-focused uncertainty review: evidence-derived keywords

## What the current evidence permits

The exported abstracts support a working architecture chain: **measurement with uncertainty → probabilistic state/model → explicit dependencies and interfaces → propagation → checking/updating → decision**. Examples already exist for Bayesian models, uncertain-state persistence, sensor fusion, graph-based dependencies, coupled twins and uncertainty-aware control. We can formulate and code these architectural mechanisms; we cannot yet claim a validated universal architecture or establish an exhaustive research gap without full-text assessment.

Distinguish uncertainty detection/recognition, quantification, propagation and monitoring. Sensor noise, residuals or drift may reveal a problem; distributions/intervals represent it; propagation tracks its effect; validation and feedback determine whether it is trustworthy and useful. A confidence interval, API connection or knowledge graph alone does not establish end-to-end continuity.

## Keyword block and evidence anchors

| Search term | Why it helps | Seed DOI from retrieved evidence |
|---|---|---|
| `architectur*` | Explicit system/component organization and interfaces | 10.1007/978-3-030-24289-3_57 |
| `probabilistic graphical model*` | Dependencies represented as probabilistic variables and inference | 10.1016/j.jsse.2023.04.001 |
| `Bayesian network*` | State, parameters, observations and decisions linked by inference | 10.1115/1.4072445 |
| `knowledge graph*` | Explicit semantic/dependency structure; probability handling still needs verification | 10.1109/SWC62898.2024.00327 |
| `data assimilation` | Measurements update uncertain system state | 10.1109/RAMS50514.2026.11424435 |
| `sensor fusion` | Measurement uncertainty enters multi-source state estimation | 10.1109/I2MTC48687.2022.9806580 |
| `uncertainty propagation` | Quantities and dependencies transmitted through models or coupled twins | 10.1109/CASE69030.2026.11704391; 10.1007/978-3-031-60271-9_28 |
| `provenance` | Proposed retrieval synonym for reconstructing data/model-to-decision history | 10.2514/6.2025-1091 supports the concept; not asserted as an exact author keyword |
| `traceability` | Retained measurement and state lineage across transformations | 10.2514/6.2025-1091; 10.1109/I2MTC48687.2022.9806580 |
| `runtime verification` | Monitoring assumptions/constraints and controlling subsequent action | 10.1109/DS-RT62209.2024.00012 |

Terms are an evidence-informed search vocabulary, not all verbatim author keywords. Generic `framework`, `model`, `structure`, and `uncertainty detection` alone were not required: framework/model are very broad, while literal detection may miss quantification, inference and propagation studies. These choices improve focus but can miss relevant studies and do not replace the broad baseline. This protocol was derived after examining the baseline, not preregistered.

## Executed supplementary database search

Stream **DT-UA**, Web of Science Core Collection, 2026-11-01, all available editions and no added restrictions:

```text
TS=("digital twin" AND uncertainty AND (architectur* OR "probabilistic graphical model*" OR "Bayesian network*" OR "knowledge graph*" OR "data assimilation" OR "sensor fusion" OR "uncertainty propagation" OR provenance OR traceability OR "runtime verification"))
```

**494 results**, all downloaded using Tab delimited file, Full Record and Cited References, range 1–494. Validation: 494 unique UTs, 71 native columns, 482 supplied DOIs, 12 missing DOI values, zero missing abstracts. All 494 UTs occur in the previous 2,016-record WoS corpus. This is a focused subset and must not increase the baseline count. It does not discover studies that omit the baseline uncertainty term or digital-twin phrase.

Raw file: `searches/Web_of_Science/DT-UA/results/raw/WOS_DTUA_0494.tsv`; merged CSV: `data/merged/WOS_DTUA_494.csv`. Raw SHA-256 and identifier reconciliation are in `analysis/architecture_focus/audit.json`. Only Web of Science was freshly queried in this round. IEEE and Scopus results below come from local processing of their complete previously exported corpora, not fresh database searches.

## Added analytical fields and local results

The same keyword family was applied to title, abstract and available keyword fields in each source. Matching handles capitalization, singular/plural forms where specified, spaces and hyphens. It does not search reference lists or author affiliations. Each matching field and term is recorded explicitly.

| Source | Complete baseline records | Keyword matches | Retrieval mode this round |
|---|---:|---:|---|
| IEEE Xplore | 1,228 | 278 | Local tagging of complete baseline |
| Scopus | 3,501 | 1,011 | Local tagging of complete baseline |
| Web of Science | 2,016 | 494 | Local tagging plus fresh database search/export |

The WoS local matching and fresh search agree on **every UT**, not just the total. The initial local match missed three hyphenated expressions; handling hyphens resolved the difference. No baseline record is deleted. Source-specific focused CSVs retain every original metadata/provenance field and add `architecture_focus_terms` and `architecture_focus_fields`. The all-record tag table covers **6,745 source records**, including nonmatches. Cross-database duplicates are not removed; 6,745 is not a unique-study count.

All added flags are **lexical_only**, and all records remain **not_screened**. A broad AI review may match `knowledge graph` without implementing a twin; a digital shadow may need separate eligibility treatment. Do not equate matches with proof of uncertainty-aware architecture.

## Proposed next coding fields

For full-text review, extract uncertainty source/type/representation; data-to-state update method; component/dependency structure; interface input/output and units; covariance/dependence assumptions; propagation method; provenance/versioning; runtime checks and validation; decision use; and implementation/evaluation status. Use `not_assessed` until there is evidence. These are proposed coding fields, not automatically inferred facts.

Rebuild with `python scripts/prepare_architecture_focus.py`. Complete baseline files and all earlier counts remain authoritative for retrieval reporting. A subsequent expansion search could relax the uncertainty term to probabilistic/Bayesian/evidential terminology, but that has not been executed here.
