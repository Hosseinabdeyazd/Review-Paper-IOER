# S4/S5 — second reading of all 946 unclear records

All 946 prior unclear canonical records were reread using title, entire available abstract and prior reason. No record was silently dropped; zero rechecks remain pending. This is AI-assisted semantic screening, not an independent human review or complete full-text eligibility assessment.

## Decisions in this revision

| New decision | Records |
|---|---:|
| exclude_core_keep_methods | 146 |
| exclude_nonresearch_component | 2 |
| exclude_title_abstract | 179 |
| retain_for_fulltext | 264 |
| retain_fulltext_unclear | 327 |
| retain_secondary | 28 |

Unresolved cases now record the exact missing information: absent chapter/abstract, actual evaluation criteria, operational-versus-embodied boundary, or physical reuse/material scope. Absence of quantitative findings alone does not justify ambiguity when scope is explicit. Broad S4/S5 eligibility is not conditional on Digital Twin or uncertainty terminology.

Operational-only performance, generic project governance, and mechanical tests with no assessed material/reuse consequence were separated from core evidence. Useful transferable methods remain available in the methods/background set. An uncertainty method or historic-building setting alone does not establish material-chain relevance. Direct reuse/retention feasibility, recovery, material environmental assessment and applicable secondary evidence remain eligible for full-text review.

## Updated entire corpus

| Current decision | Records |
|---|---:|
| exclude_core_keep_methods | 1623 |
| exclude_nonresearch_component | 117 |
| exclude_retracted_source | 1 |
| exclude_title_abstract | 4236 |
| retain_for_fulltext | 2932 |
| retain_fulltext_unclear | 327 |
| retain_secondary | 351 |

All 9587 canonical records have a screening decision. 3610 reports remain for core full-text or secondary assessment; 5977 are outside that set. These are report counts, not independent-study or final-inclusion counts. Full-text eligibility and quantitative uncertainty-transfer extraction have not been completed by this revision.

## Base versus uncertainty search layers

The previous 2668 clear retain_for_fulltext records comprised 2323 Base-only records and 345 records also retrieved by S4-2 or S5-2. The number was 2668, not 2268. Including unclear and secondary candidates, the previous broader candidate total was 3937 (3408 Base-only, 529 uncertainty-query members). The updated membership table is:

| Current status | Base only | Member of S4-2 or S5-2 |
|---|---:|---:|
| exclude_core_keep_methods | 1170 | 453 |
| exclude_nonresearch_component | 102 | 15 |
| exclude_retracted_source | 1 | 0 |
| exclude_title_abstract | 3247 | 989 |
| retain_for_fulltext | 2540 | 392 |
| retain_fulltext_unclear | 294 | 33 |
| retain_secondary | 300 | 51 |

Membership is computed from original query IDs only; it is not a new keyword classifier and does not prove uncertainty quantification or propagation. The uncertainty subset is a retrieval subset, not a verified mechanistic evidence set. Full-text extraction must distinguish mention, quantification, propagation between stages, and validation/monitoring. No Base records were discarded merely to make the corpus smaller.

## PRISMA accounting

19963 query memberships - 5094 within-database overlaps = 14869 database-distinct records. Prior cross-database removals 4951 plus 331 adjudicated duplicates leave 9587 canonical records. All 330 candidate duplicate groups and 14 DOI-conflict decisions remain unchanged. This revision changes screening outcomes only, not identification or deduplication denominators. A remaining blank unverified DOI has not been invented. The 91 duplicate-alias original IDs not separately read remain documented in the prior audit; canonical coverage must not be described as all original IDs independently read.

## Publisher-verified metadata correction

Record S45-b7761f1ee86d (DOI 10.34659/eis.2022.83.4.575) has an electronic-waste title in the supplied data but a building-reuse abstract. The [publisher page](https://ekonomiaisrodowisko.pl/journal/article/view/575) identifies it as **Adaptive reuse of buildings** with the matching abstract. A legacy PDF indexed by a repository retains the anomalous title. Raw title/DOI/abstract are preserved; `verified_title` and `verified_title_source` record the correction separately. The record is retained based on the confirmed reuse subject, not silently relabelled.

## Reproducibility and limits

The 946-row full-metadata CSV records before/after decisions. `individual_decisions.json` records the new authored decisions, rationale, literal evidence and remaining gap. `current_canonical_records.zip` includes all original bibliographic fields and unchanged merged provenance. `decision_sets.zip` splits current records by outcome; excluded records are retained for audit. `search_layer_counts.csv` and `prisma_counts.csv` reconcile exactly to current records. Additional primary-source checks are documented in `primary_source_checks.json`; one targeted publisher fulltext check resolved record S45-9664a9714f51 to methods background. This does not constitute completion of fulltext eligibility for the corpus.

The script integrates authored decisions and validates coverage/evidence/preservation; it does not infer scientific eligibility. Four assistant readers divided the queue, and a further targeted consistency audit checked borderline decisions. No independent human reviewer participated. Incomplete abstracts remain incomplete; three attempted MDPI direct-page checks returned HTTP429, so no conclusions were inferred from those failed accesses. Full-text retrieval remains needed for unresolved cases. Earlier completion files remain immutable historical inputs and are superseded only for current screening counts.

To reproduce, extract `reproducibility_bundle.zip` at the workspace root with the prior `outputs/S4 S5 Core Review/screening/adjudication/canonical_screening_complete.zip` present, then run `python work/integrate_unclear946.py`.
