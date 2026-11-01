# Independent synthesis audit: three full-text extractions

Reviewed the three current extraction JSONs and companion notes. This is a cross-paper consistency audit of authored full-text extractions, not a fourth independent human review or computational reproduction. Paper-specific PDF checks and unresolved transcription issues retain their recorded status.

## Ranking depends on the question

| Question | Ranking | Reason |
|---|---|---|
| Actual circular recoverability/reuse feeding embodied LCA | **1 > 2 > 3**, with a substantial scope gap after 1 | Paper 1 explicitly connects functional reuse potential with CFF allocation, recovery shares, quality and avoided virgin production. Papers 2–3 concern damage repair/reconstruction; neither models uncertain circular recovery. |
| Most explicit auditable probabilistic physical-intervention-to-carbon chain | **2 > 1 > 3** | Paper 2 provides geometry ranges, sampled repair quantities, consequence distributions, conditioning and building-risk aggregation. Paper 1 demonstrates propagation in two branches but not joint draw identity. Paper 3 largely scales economic risk through a carbon proxy. |

**No paper establishes the complete target chain of independently estimated recoverability/quality uncertainty → conditional recovery and substitution → joint embodied-LCA output, with fully documented dependence and sample lineage.** This does not negate the useful mechanisms each demonstrates.

## What each paper actually contributes

**1. Almeida et al., DOI 10.1016/j.jclepro.2026.148705 — closest topical match.** Functional reuse share U2 informs plausible CFF R2 under compatible boundaries; the circularity score itself is not an LCA input. Monte Carlo produces circularity and GWP distributions. This is direct material-circularity relevance, including reuse quality and avoided-production terms. However, the publication does not document a joint conditional U2→R2 sampler, common draw identities or covariance. Figure 12 even shows different S2 display ranges for U2 and R2. That observation prevents asserting identical samples, but does not prove independence. Distribution families, sampling parameters and reproducibility details are missing; scenario/figure/prose inconsistencies further limit numerical reuse. Anchors: §§3.3–3.4, pp9–10; §4.2.4, pp16–18; Fig12.

**2. Aljawhari et al., DOI 10.1016/j.jobe.2023.108149 — strongest transformation template, adjacent S4 scope.** Sampled geometry/carbon factors yield damage-state-specific repair-carbon distributions; sampled seismic response/damage and repairability then produce building-carbon and annual-risk distributions. Damage-conditioned Beta surrogates compress the detailed results. This is explicit physical repair/replacement→S5 propagation, but repair/retention is adjacent to circular recoverability, not interchangeable with it. Recycling is fixed at90%; quality, salvage yield, contamination and substitution-credit uncertainty are absent. Surrogate damage-state distributions exclude collapse/excessive residual-drift cases, requiring a separate replacement branch. Some dependence assumptions are explicitly simplifying. Anchors: §4 pp5–10; §6.2 pp12–13; §7 pp14–16. The recorded Eq4 visual-transcription issue must be resolved or omitted from definitive formulas.

**3. Caruso et al., DOI 10.1038/s41467-025-68120-6 — scalable portfolio proxy, not direct recoverability.** Probabilistic economic annual-loss ratios are assumed equal to carbon-loss ratios, then multiplied by replacement carbon separately for structural/nonstructural components. This yields expected annual damage carbon, not a documented joint final uncertainty distribution. ECF variability is reported propagated to replacement-carbon CoV; component quantities and90% recovery are fixed. Supplemental component examples support approximate cost/carbon alignment, with acknowledged low-damage mismatch. This paper is stronger for scalable exposure integration than for recovery uncertainty. Anchors: pp6,9,12–14; Fig8; Supplement pp1–4.

## Evidence versus additions proposed by our review

Demonstrated: paper1's reuse-feasibility input bridge and separate Monte Carlo branches; paper2's conditional damage/repair-material/carbon chain and probabilistic surrogate; paper3's risk-ratio/stock-carbon aggregation.

**Our proposed extensions, not findings attributed to these papers:** shared sample IDs across S4/S5; explicit conditional yield/quality/lifetime distributions; retained dependence/covariance; mass-balance constraints across reuse/recycling/disposal; component-level provenance from observation through recovered inventory to avoided-production credits; uncertainty-preserving surrogate interfaces; and sensor/BIM/passport-based evidence updating. These require specification, implementation and validation. None of the three demonstrates an operational digital twin or live uncertainty updating.

Recommended synthesis wording: **Paper1 is the direct circularity–LCA anchor; paper2 supplies an adjacent but stronger probabilistic intervention-to-carbon mechanism; paper3 supplies a scalable, assumption-sensitive portfolio transfer. Together they motivate, rather than already establish, an end-to-end uncertainty-preserving circular-material pipeline.**
