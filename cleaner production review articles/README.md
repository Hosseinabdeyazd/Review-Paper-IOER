# Cleaner Production Review Articles

## Lessons-learned repository for improving our manuscript

This folder records the structure, argument logic, strengths, limitations, and transferable lessons from review articles published in the **Journal of Cleaner Production**. The goal is to ensure that the outcome of each article review is retained and that selected lessons can later be translated into specific, traceable changes in our own review.

**Related project:** End-to-End Uncertainty Propagation in GeoAI-Informed Urban Material-Stock and Circularity Decisions.

**Created:** 2026-10-01.

> Recording a proposal in this folder does not mean that it has been approved or implemented in the manuscript, protocol, or coding framework. At the time this folder was created, none of the new proposals had been applied to the main project files.

## File guide

| File | Purpose |
|---|---|
| [Patouillard et al. (2018) note](articles/02_Patouillard_et_al_2018.md) | Review of spatial LCA; distinction between variability and uncertainty, regionalization and spatialization, scale transitions, and transferable lessons |
| [Baustert & Benetto (2017) note](articles/03_Baustert_Benetto_2017.md) | Review of uncertainty in coupled models; article structure, evidence, interpretation, and practical adaptations |
| [LESSONS_AND_ACTIONS.md](LESSONS_AND_ACTIONS.md) | Consolidated lessons-and-actions register showing what has been proposed, where it should be applied, and when it has actually been implemented |
| [PROPOSED_MANUSCRIPT_STRUCTURE.md](PROPOSED_MANUSCRIPT_STRUCTURE.md) | Working proposed structure for our manuscript; to be revised as additional articles are reviewed |
| [ARTICLE_REVIEW_TEMPLATE.md](ARTICLE_REVIEW_TEMPLATE.md) | Standard template for reviewing each subsequent article |

## Separation of three layers

**Source evidence:** What is actually supported by the reviewed article, with DOI and section/page references.

**Our interpretation:** Our interpretation of the role of that content in the article's structure or argument; this is not presented as a direct claim by the original authors.

**Proposed adaptation:** An idea for our own manuscript that must be assessed, approved, implemented, and verified separately.

An illustrative example is not empirical validation. Likewise, a gap reported in a 2017 paper should not be treated as a confirmed gap in the current literature without an updated check.

## Current status

- A full-text structural note has been recorded for **one article: JCP-03**. Its number follows the original ten-paper list rather than the order in which the papers were reviewed.
- **Nine additional articles** remain queued for full-text review. No structural conclusions have yet been recorded for them.
- The list below is a reading and benchmarking list; it is **not the set of studies included in the systematic review** and must not be used directly in PRISMA counts or effect analyses.
- For the eight articles not yet reviewed, titles, publication years, and DOIs were transferred from the earlier candidate list and were not independently re-verified when this folder was created. Before preparing a note, the DOI, title, journal, and article type should be checked against the publisher page or PDF.

## List of ten articles

| ID | Title recorded in the original list | Year | DOI | Note status |
|---|---|---|---|---|
| JCP-01 | Spatializing environmental footprint by integrating geographic information system into life cycle assessment: A review and practice recommendations | 2021 | [10.1016/j.jclepro.2021.129113](https://doi.org/10.1016/j.jclepro.2021.129113) | Pending bibliographic verification and full-text review |
| JCP-02 | Critical review and practical recommendations to integrate the spatial dimension into life cycle assessment | 2018 | [10.1016/j.jclepro.2017.12.192](https://doi.org/10.1016/j.jclepro.2017.12.192) | [Note recorded; bibliographic details checked against PDF](articles/02_Patouillard_et_al_2018.md) |
| JCP-03 | Uncertainty analysis in agent-based modelling and consequential life cycle assessment coupled models: A critical review | 2017 | [10.1016/j.jclepro.2017.03.193](https://doi.org/10.1016/j.jclepro.2017.03.193) | [Note recorded; bibliographic details checked against PDF](articles/03_Baustert_Benetto_2017.md) |
| JCP-04 | Application of machine learning initiatives and intelligent perspectives for CO₂ emissions reduction in construction | 2023 | [10.1016/j.jclepro.2022.135504](https://doi.org/10.1016/j.jclepro.2022.135504) | Pending bibliographic verification and full-text review |
| JCP-05 | Circular economy in the construction industry: A review of decision support tools based on Information & Communication Technologies | 2022 | [10.1016/j.jclepro.2022.131335](https://doi.org/10.1016/j.jclepro.2022.131335) | Pending bibliographic verification and full-text review |
| JCP-06 | Critical consideration of buildings’ environmental impact assessment towards adoption of circular economy: An analytical review | 2018 | [10.1016/j.jclepro.2018.09.120](https://doi.org/10.1016/j.jclepro.2018.09.120) | Pending bibliographic verification and full-text review |
| JCP-07 | Circular economy in the construction industry: A systematic literature review | 2020 | [10.1016/j.jclepro.2020.121046](https://doi.org/10.1016/j.jclepro.2020.121046) | Pending bibliographic verification and full-text review |
| JCP-08 | Combining Life Cycle Assessment and System Dynamics to improve impact assessment: A systematic review | 2021 | [10.1016/j.jclepro.2021.128060](https://doi.org/10.1016/j.jclepro.2021.128060) | Pending bibliographic verification and full-text review |
| JCP-09 | To what extent can agent-based modelling enhance a life cycle assessment? Answers based on a literature review | 2019 | [10.1016/j.jclepro.2019.118123](https://doi.org/10.1016/j.jclepro.2019.118123) | Pending bibliographic verification and full-text review |
| JCP-10 | Systematic review of scale-up methods for prospective life cycle assessment of emerging technologies | 2024 | [10.1016/j.jclepro.2024.142161](https://doi.org/10.1016/j.jclepro.2024.142161) | Pending bibliographic verification and full-text review |

## Workflow

1. Verify the full text and bibliographic details, then create the article note from the standard template.
2. First record the article's actual structure, terminology, and claim boundaries; then document our interpretation and proposed adaptations separately.
3. Enter trackable proposals into the lessons-and-actions register using stable IDs.
4. Before changing the protocol, coding framework, or manuscript structure, review the proposal and record the decision.
5. Change an action status to `Implemented` or `Verified` only after the target file has actually been changed and checked, and record the relevant commit link.

Action states: `Proposed → Accepted → Implemented → Verified`; `Deferred` and `Rejected` are also available with a documented reason. The status of an article review is independent from the implementation status of its proposed lessons.

## Relationship to the main project files

The current design reference for the project is the [main README](../README.md). When this folder was created, that file was reviewed; its blob SHA was `ea5eea63a31bf930ed5c46d2deff28fe3ab5d67d`. This is a file-content identifier, not a commit SHA.

According to that version, the Scopus searches for S1–S3 are approved, while S4–S5 remain drafts. Creating this lessons repository does not change their status. Future paths such as `docs/coding_framework.md`, when mentioned in the notes, remain proposed destinations until those files actually exist.

## Source management

This folder stores notes and references; publisher PDFs or full article texts have not been uploaded here. For citation outside this conversation, use DOI and section/page references rather than temporary conversation identifiers.

## Revision history

| Date | Change |
|---|---|
| 2026-10-01 | Created the folder; recorded the ten-paper list, the JCP-03 note, the review template, the action register, and the provisional manuscript structure. Main project files remained unchanged. |
| 2026-10-02 | Reviewed the full text of JCP-02 and recorded lessons on spatial LCA, scale transitions, and uncertainty/variability. |
