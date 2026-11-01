# S4/S5 PRISMA reporting record — complete title/abstract screening

All **9,587 canonical records** now have semantic title-and-complete-available-abstract decisions; **0 remain unscreened**. This revision completes the remaining **2,588**. This is AI-assisted screening, not completed full-text eligibility or independent human review.

## Identification and duplicates

19,963 exported query memberships − 5,094 within-database query overlaps = 14,869 database-distinct records. After 4,951 earlier cross-database duplicate removals and 331 additional bibliographically adjudicated removals, 9,587 canonical records remain. The 330 candidate groups were resolved as 318 merges, 11 distinct-report groups and one partial merge. All 14 DOI-conflict groups retain their documented resolution; one canonical DOI remains unverified and blank, with supplied identifiers preserved. No new bibliographic merges were performed in this revision.

## Screening outcomes

| Decision | All canonical records | New 2,588 |
|---|---:|---:|
| exclude_core_keep_methods | 1,477 | 176 |
| exclude_nonresearch_component | 115 | 51 |
| exclude_retracted_source | 1 | 0 |
| exclude_title_abstract | 4,057 | 389 |
| retain_for_fulltext | 2,668 | 1,631 |
| retain_fulltext_unclear | 946 | 157 |
| retain_secondary | 323 | 184 |

3,937 records remain for full-text or secondary-source assessment; 5,650 are removed from the S4/S5 core at title/abstract stage. The methods/background category is retained in a separate evidence library, although excluded from the core. `retain_fulltext_unclear` means eligibility is unresolved and requires source/full-text examination, not final inclusion. `retain_secondary` is secondary literature kept separately from primary reports.

## Reading coverage and method

The earlier requested queue contained 7,238 original IDs (50 previously read plus 7,188 completed). One supplemental retraction review brought directly read original IDs to 7,239, corresponding to 6,999 canonical decisions after bibliographic merges. The present 2,588 canonical IDs were read directly by the primary assistant and three delegated assistants. Combined: 9,827 original IDs were directly read; 91 duplicate-alias IDs were not separately read. All 9,587 canonical records are covered. These denominators must not be interchanged.

Each new decision contains the record ID, queue position, individual reason, literal title/abstract evidence, stage relevance, abstract adequacy and AI attribution. Complete available abstracts were read; missing or mismatched metadata is explicitly flagged. S4 includes recoverability, reuse, repair and physical building retention; S5 includes material-related embodied and life-cycle environmental assessment. Digital Twin and uncertainty terms were not mandatory. Operational-energy-only, financial-cost-only and unrelated topics are excluded; transferable technical methods remain separate. Retention is deliberately inclusive at title/abstract stage and does not prove an uncertainty-transfer mechanism.

Elicit delivered 80 records in the prior phase, all reread by the primary assistant, with 14 corrections. No Elicit upgrade was purchased and no additional Elicit output is claimed in this revision. All new decisions are direct assistant readings. No independent human reviewer participated. Scripts persist authored decisions, check coverage and build tables; they do not classify eligibility by keyword rules.

## Validation and limits

Exact queue coverage, absence of overlapping new IDs, nonempty reasons, literal evidence, all original bibliographic/source fields, prior 6,999 decisions and merged provenance were checked. DOI, authors, titles, abstracts and all other supplied fields are preserved. Missing metadata is not fabricated. Source inconsistencies may remain for full-text verification; for example, `S45-b7761f1ee86d` has an electronic-waste title but an adaptive-building-reuse abstract and is retained as unclear.

Two additional related-report families were flagged during reading and verified against publisher/university metadata: the [Madrid Spanish/English reports](https://www.sciencedirect.com/science/article/abs/pii/S043956891830024X) and the [recovered-wood original/corrected report](https://portal.fis.tum.de/en/publications/erratum-potentials-for-cascading-of-recovered-wood-from-building-/). They retain distinct report records and source identifiers, with explicit family/version fields and `related_report_versions.csv`; do not count these versions as independent studies. Prefer the corrected wood version for quantitative extraction. This does not alter the prior 330 duplicate-group decisions or report-level denominator.

These checks establish completeness and traceability, not independent validation of scientific accuracy. Reports sought/retrieved, full-text exclusion reasons and final included-study counts are not yet determined. Full texts assessed in this screening revision: **0**. The earlier Digital Twin full-text corpus is separate. A PRISMA flow must stop at title/abstract screening until full-text eligibility is actually performed.

Reporting basis: [PRISMA 2020 explanation and elaboration](https://www.bmj.com/content/372/bmj.n160), particularly selection process and flow reporting. PRISMA is a reporting guideline, not a certification of screening quality.

## Current files and reproducibility

Use `canonical_screening_complete.zip`, `screening_decision_sets.zip`, `remaining_2588_review_log.zip`, `remaining_2588_decisions.json`, `completion_summary.json`, `completion_validation.json` and `prisma_complete_counts.csv`. The previous `revised_records.zip` and `summary.json` remain immutable historical inputs, not the current result.

`completion_reproducibility_bundle.zip` contains the immutable queue, four authored decision files and read/save/integration scripts. Extract at the workspace root with the prior `revised_records.zip`, `title_abstract_decisions.json` and `supplemental_integrity_decisions.json` in `outputs/S4 S5 Core Review/screening/adjudication/`, then run `python work/complete_canonical_screening.py`. All three prerequisites are preserved in this repository folder. The integration aborts unless every new ID has an authored decision and all preservation checks pass. No API, paid service or automatic semantic classifier is needed to reproduce the outputs.
