# S4/S5 uncertainty mechanism screening

392 unique clear fulltext candidates retrieved by the uncertainty-layer queries were individually assessed from titles and complete available abstracts. This is AI-assisted title/abstract mechanism screening, not fulltext verification or independent human review.

S4+Uncertainty:143; S5+Uncertainty:331; intersection:82; unique union:392. S4-only:61; S5-only:249. These are query memberships, not confirmed scientific stage assignments. The 33 unclear and 51 secondary uncertainty-query records are outside this requested 392-record cohort.

| Evidence category | Unique | S4 query | S5 query | Both queries |
|---|---:|---:|---:|---:|
| explicit_propagation | 52 | 17 | 43 | 8 |
| mention_or_no_demonstrated_uq | 144 | 63 | 112 | 31 |
| quantified_uncertainty_only | 40 | 20 | 30 | 10 |
| sensitivity_scenarios_only | 156 | 43 | 146 | 33 |

Explicit propagation requires an uncertain input, a stated mapping/model and an uncertain output in the available abstract. Quantification alone, deterministic scenarios and sensitivity alone are separate. An explicit S4-to-S5 claim requires a described recovery/reuse uncertainty carried into environmental/LCA or decision outputs; appearing in both searches is insufficient. Missing information is not evidence of absence. No final included-study count is asserted.

Each row preserves source metadata and original decisions; mechanism_* fields record this new assessment, input, transformation, output, evidence and reason. The earlier broad S4/S5 screening counts and duplicate adjudications are unchanged. This is an additional thematic selection, not new PRISMA identification or a fulltext exclusion round.

Three assistant readers reviewed disjoint record batches. Fulltext checks are required before treating these candidates as confirmed mechanisms, especially to establish equations, distributions, dependence assumptions, calibration and actual stage interfaces. No mandatory Digital Twin criterion was used in the original S4/S5 queries.

## Targeted primary-source checks

The separate targeted_source_checks.csv documents four followups without overwriting abstract-only decisions. Mutale et al. use a Bayesian network for stock-property inference; reuse quantities and embodied carbon remain proposed extensions (sections2.3,3.5.3,4). Di Bari et al., DOI10.3390/buildings10030048, map stochastic earthquakes through repair/rebuild choices to GWP/cost outcomes (sections3-4); this is a qualified building-retention bridge, not a recovered-material quality/yield model. Galimshina et al. author slides show PCE-based LCA/LCC distributions, but slides are not the article fulltext. Almeida et al., DOI10.1016/j.jclepro.2026.148705, directly connect multicycle recovery/circularity with environmental allocation and probabilistic parameters at abstract level; fulltext access failed. Source URLs and limitations accompany each check.

Generic propagation counts include peripheral hazard, cost and stock-property models. They must not be presented as counts of demonstrated material recovery-to-LCA propagation. Likewise, a repair-to-carbon pathway is a building-retention bridge, distinct from modelling uncertain recovered-material quality or recovery yields. `cross_stage_candidates.csv` is the narrower abstract-level candidate set, still requiring fulltext confirmation.

## Closest pathways identified

- Almeida et al., [10.1016/j.jclepro.2026.148705](https://doi.org/10.1016/j.jclepro.2026.148705): strongest direct material circularity-to-environment candidate. Recovery/reuse and lifetimes feed multicycle MCIRENO/CFF outcomes with probabilistic parameter analysis. Exact uncertainty distributions and dependence across loops remain unverified.
- [10.1016/j.jobe.2023.108149](https://doi.org/10.1016/j.jobe.2023.108149): seismic component damage is converted through repair-material consequence models to embodied-carbon distributions. Explicit repair-to-environment pathway, not recovered-component quality transfer.
- [10.1038/s41467-025-68120-6](https://doi.org/10.1038/s41467-025-68120-6): probabilistic earthquake scenarios combine with repair/reconstruction material quantities and carbon factors to embodied-carbon risk at continental scale. A repair/reconstruction pathway.
- [10.3390/buildings10030048](https://doi.org/10.3390/buildings10030048): targeted methods check confirms event sampling, retention/rebuild decisions and GWP/LCC accumulation. Treat as a qualified retention bridge, not an uncertain recovery-yield model.

These mechanisms support complementary parts of a future architecture; none of these checks establishes a complete Digital Twin uncertainty-tracking implementation. The architecture mapping is the reviewer's interpretation, not terminology necessarily used by the authors.
