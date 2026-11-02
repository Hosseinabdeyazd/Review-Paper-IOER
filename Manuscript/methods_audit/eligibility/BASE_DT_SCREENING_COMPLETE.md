# Broad S1–S5 + DT: completed title/abstract screening

This is closure of title/abstract screening, not full-text eligibility or the review as a whole.

All 2,410 canonical retrieval records have a recorded title/abstract decision. Of these, 1,882 were read in the new batches; 528 same-publication matches reuse domain-level screening decisions from the DT+U corpus, with source IDs and matching basis retained. No full-text inclusion was inherited from a title/abstract decision.

Ten late bibliographic aliases were adjudicated, leaving **2,400 unique publication records**:

| Decision | Unique records |
|---|---:|
| Direct-domain full-text candidates | 890 |
| Separately labelled secondary/transferable candidates | 762 |
| Unclear, carried forward for adequate text/metadata | 24 |
| Screening exclusions | 724 |
| Total | 2,400 |

The exclusion category includes non-research containers and retracted items as explicitly recorded; it is not exclusively topical irrelevance. All retained and unclear records are candidates, not Included studies. The 24 unclear cases must not be converted into exclusions merely to close the flowchart.

## Identity control

The ten late aliases include proceedings-year versus publication-year variants and one article indexed with a journal-issue DOI. Original source years, DOI variants, record IDs and stage/database memberships remain available. Crossref metadata validates the article-versus-issue distinction and the relevant ASCE proceedings author/title matches. The source files are not deleted.

The conference-container audit verifies distinct CGI, CAADRIA, IN4PL and ICAE volumes using raw Scopus EIDs, volumes and ISBNs. Their identical event titles do not justify merging distinct volumes. Three generic Introduction records belong to different books. The 16 conference containers remain screening exclusions rather than duplicates.

## Files

- `broad_dt_unique_title_abstract_decisions.csv`: unique decisions with original bibliographic metadata and abstracts, per-record reasons, source quotations and provenance.
- `broad_dt_title_abstract_decisions.csv`: all 2,410 screened records before late alias suppression.
- `broad_dt_*.csv` numbered batches: original individual reading decisions.
- `broad_dt_transferred_ta.csv`: same-publication domain-screening transfers only.
- `broad_dt_residual_alias_decisions.csv`: ten identity decisions and reasons.
- `broad_dt_container_identity_audit.csv`: raw-record identity evidence for containers and generic titles.
- `broad_dt_screening_validation.json`: exact source-ID/index coverage and quote validation.
- `broad_dt_unique_screening_counts.json`: unique counting totals.

The broad Base+DT+U full-text ledger is separate. Its decisions cannot simply be copied into Base+DT because failure of the uncertainty criterion does not imply failure of the DT-only criterion. Similarly, a method retained as complementary evidence is not direct building-material-chain evidence.
