# S4/S5 title-and-abstract reassessment: PRISMA reporting record

Status: requested 7,188-record reassessment complete.

This report concerns the S4/S5 core retrieval and the requested reassessment queue. It does not establish final full-text eligibility, study-level inclusion or completeness of S1–S5. The earlier digital-twin full-text corpus is separate.

## Identification and deduplication

| Quantity | Count |
|---|---:|
| Exported query memberships | 19,963 |
| Overlapping query memberships within databases, removed before identification count | 5,094 |
| Database-specific distinct records identified | 14,869 |
| Previous duplicate removals | 4,951 |
| Additional bibliographically adjudicated duplicate removals | 331 |
| Canonical records remaining | 9,587 |

The 330 candidate duplicate groups were resolved as 318 merges, 11 groups retaining distinct reports, and one partial merge. A distinct report is not necessarily a distinct study. All supplied identifiers and source metadata remain auditable; one canonical DOI is unverified and blank.

## Selection coverage

- Requested original-ID queue: 7,238 records (5,093 previously unclear plus 2,145 proposed exclusions).
- Previously read by the assistant: 50.
- Elicit decisions downloaded: 80; all 80 titles and complete available abstracts independently reread by the primary assistant, with 14 recorded decision corrections. This is AI reassessment, not independent human review.
- Additional original IDs read directly by assistants after the initial 50 and Elicit 80: 7,108.
- Requested original IDs with a recorded decision: 7,238.
- Requested original IDs still without a decision: 0.
- Elicit reported 180 saved records in its interface, but only 80 were delivered. The undelivered 100 are not counted. Elicit stopped at the monthly quota; the user declined upgrade and authorized direct multi-agent reading.
- The prior direct-scope/secondary automated routing groups are not silently counted as newly semantically read.
- Canonical records lacking a new semantic adjudication: 2,588.

| Canonical adjudication outcome | Records |
|---|---:|
| exclude_core_keep_methods | 1,301 |
| exclude_nonresearch_component | 64 |
| exclude_retracted_source | 1 |
| exclude_title_abstract | 3,668 |
| not_yet_reassessed | 2,588 |
| retain_for_fulltext | 1,037 |
| retain_fulltext_unclear | 789 |
| retain_secondary | 139 |

## Method and limitations

The original title and complete available abstract were read directly in sequential batches by the primary assistant and three delegated assistants, except for the delivered Elicit subset which was also entirely reread by the primary assistant. No mandatory uncertainty or digital-twin term was imposed. The protocol distinguishes S4 circular recovery/retention and S5 material-related environmental assessment from operational-energy-only, financial-cost-only and unrelated topics. Explicit physical retention or adaptive reuse can qualify even if economically motivated. Plausible unclear records are retained for full text. Every authored decision includes an ID, individual rationale, literal evidence excerpt, abstract-adequacy label and AI-review attribution. Scripts persist and validate authored decisions; they do not replace semantic reading with keyword rules.

Checks compare input/output IDs, completeness, duplicates, exact title/DOI preservation, nonempty rationales and literal evidence against the original input. These checks establish traceability, not scientific accuracy or sensitivity. Any assistant reassessments are recorded separately with reasons. No independent human reviewer participated. Elicit model/version is not exposed in the delivered script; its actual code and exact instructions are preserved.

Five merged records with differing semantic decisions were explicitly reread and reconciled in canonical_conflict_resolutions.json; their initial decisions remain in the original-ID log. Book-level summaries and missing abstracts are distinguished from substantive article abstracts. Background-method records remain separately traceable.

No reports have been assessed for full-text eligibility in this revision. Reports sought/retrieved and final included studies are not yet determined; they must not be inferred from the retained title/abstract count. The PRISMA record explicitly identifies AI decisions rather than presenting them as human screening.

Reporting basis: [PRISMA 2020 explanation and elaboration, items 8 and 16](https://www.bmj.com/content/372/bmj.n160). PRISMA is a reporting guideline; use of this report does not certify review quality or independent validation.

## Supplemental integrity checks

One additional original record outside the 7,238-ID queue was read and excluded for retraction. Three duplicate members were reread for QA but already belong to the main queue; they are not counted twice. These do not inflate requested-queue coverage. See supplemental_retraction_note.md and supplemental_integrity_decisions.json.
