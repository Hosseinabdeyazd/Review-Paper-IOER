# Methodological reading of Abdelrahman et al. (2025)

Reference: *What is a Digital Twin anyway? Deriving the definition for the built environment from over 15,000 scientific publications*. Building and Environment 274, 112748. DOI: [10.1016/j.buildenv.2025.112748](https://doi.org/10.1016/j.buildenv.2025.112748).

The supplied 19-page PDF was examined for its methods and analytical sequence, with visual inspection of pages 5, 9, 11 and 13. The public [code workflow](https://github.com/ualsg/dt-definitions/blob/main/README_CODE.md) and repository listing were also inspected. The notebooks were not executed, and the statistical results were not independently reproduced. This is a methodological reference, not an automatic addition to a selected-study denominator.

## What the paper actually analyses

| Element | Paper locator | Actual analytical role | Adaptation to our review |
|---|---|---|---|
| Full-text and expert evidence | Sections 3.1.1–3.1.2, p6 | Authors report 15,353 search results and a 52-expert survey; literature and practitioner definitions are compared | Preserve the three-database provenance of our corpus. Do not claim an expert-validation exercise that we have not conducted |
| Semantic extraction and consolidation | Section 3.1.3, pp6–7; Figs3–4, p5 | Regex extracts definition candidates; LLM filtering, embeddings, k-means and fuzzy matching consolidate definitions | Extract study claims about functions, uncertain variables and actual interfaces. Synonym clustering can assist; semantic evidence requires checked locators |
| Component taxonomy | Section 3.2, pp7–9; Table3, p8 | Frequency-derived terms are harmonized with reference architectures into Data, Analysis/services, Infrastructure, Interface and Governance | Use these as an initial DT coding scaffold. Add domain-specific categories inductively; do not equate the five categories with S1–S5 |
| Frequency and relative representation | Section 3.3, p10; Fig8, p9 | Component frequencies are compared across urban, building, manufacturing and architecture domains using chi-square and residuals | Construct three separately defined matrices: S×U, S×DT functions, DT functions×U mechanisms. First show supported counts, denominators and missingness |
| Temporal development | Fig9, p11; Section4.1, p10 | Tracks particular components through time | Track components/mechanisms within eligible annual cohorts, with both counts and within-year shares. Existing aggregate query trends cannot substitute for this |
| Correlation and clustering | Section3.3, p10; Fig10, p11 | Correlates **component residual profiles across domains**, then clusters them | Distinguish profile similarity from same-paper co-occurrence and from directed technical coupling. Only the third can support an implemented architectural edge |
| Context, time and maturity | Figs12–13, p13; Section4.2, pp13–14 | Authors relate application time scales and a maturity framework to their domain-specific interpretations | Code update frequency, event resolution, prediction horizon and validation setting separately. Spatial scale and decision roles are cross-cutting attributes |
| Synthesis | Section4.1, pp10–13; Section4.2, pp13–14 | Authors infer HPRT/LTDS groupings and domain-specific definitions | Our target is an evidence-traceable material-flow DT architecture, with direct, synthesized and proposed edges explicitly separated |

## Boundaries on reuse of the method

1. A component's frequency is evidence of its representation in a corpus, not proof of its necessity, usefulness, implementation or maturity. Our architectural requirements must be justified by functions and gaps, in addition to frequency.
2. Fig10 is not a paper-level co-occurrence network. Its correlations describe similarity across domain residual profiles. Repeating that operation across five stages provides few profile positions and cannot establish robust architectural modules by itself.
3. The paper describes standardized-residual interpretation and adjustments for low/zero counts, but an identical test is not automatically appropriate for overlapping stages, multilabel components or multiple reports of the same study. We must preserve the unit of observation and dependencies.
4. Definitions, general discussion, proposed architectures and implemented mechanisms require separate coding. A definition mentioning feedback or uncertainty is not evidence that a particular implementation transports a covariance or updates a posterior.
5. The paper's long-term-decision-support interpretation is relevant to material stocks, but it does not prove that every material-flow DT has the same requirements. The review must extract timing requirements from the actual modelled processes and decision needs.
6. The number of definitions is described approximately in the text and differently in Fig4. No precise definition denominator is borrowed into our analysis. Search results, full texts, definitions and component occurrences are distinct units.

No sentence or figure from the source is reproduced as original work here. The methodological sequence is adapted, and the architecture remains our proposed synthesis until supported and validated at the stated level.
