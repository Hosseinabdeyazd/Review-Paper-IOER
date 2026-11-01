# Scopus: architecture and continuity of uncertainty

## Scope

The full 3,501-record metadata corpus is retrieved. This document is an initial, purposive reading of selected exported abstracts, not completed eligibility screening or a full-text review. The executable lexical queue covers every record and leaves all records `not_screened`.

Term matches: uncertainty representation 3,501; updating/calibration 773; propagation/coupling 302; semantics/interoperability 296; provenance/traceability 139; validation/monitoring 1,304; decision/feedback 1,292; architecture/framework/interface terms 2,121. These categories overlap. A term match does not establish an implemented mechanism or uncertainty continuity.

## Evidence that sharpens the architecture question

| Source (DOI) | What the abstract supports | Boundary of the evidence |
|---|---|---|
| [Capturing Uncertainty in the Digital Twin State](https://doi.org/10.2514/6.2025-1091) | Uncertain states and simulation history must be stored and read for decision use; compares compression/file formats with databases, considering memory, speed, storage and accuracy. | Strong relevance to persistence and data-to-decision traceability; does not establish a universal interoperable uncertainty payload. |
| [PGM-based twins: a space habitat study](https://doi.org/10.1016/j.jsse.2023.04.001) | Directed acyclic graphs connect expert knowledge and observations; historical training and online probabilistic inference estimate time to a critical temperature. Reports experiments in three office rooms as an analogue. | Analogue experiments, not an operating space habitat. A separate conference record with no DOI is retained in the corpus. |
| [Probabilistic Graphical Modeling for Machine Tool Dynamics](https://doi.org/10.1115/1.4072445) | Dynamic Bayesian network explicitly represents parameters, observations and decisions; sequential inference supports model selection and state estimation; reports a controller-connected 3D-printer experiment. | Evidence for implemented uncertainty-to-control coupling in this case; general scalability and computational cost need full-text checking. |
| [Chemical engineering DT framework](https://doi.org/10.1016/j.compchemeng.2025.109178) | Combines online/transfer learning, Bayesian inference and Monte Carlo methods; applications concern gas-lift and electric-submersible-pump systems. | Detailed coupling equations, data provenance and nature of the demonstrations must be checked in full text. |
| [The Role of Uncertainty Propagation for Digital Twins](https://doi.org/10.1007/978-3-031-60271-9_28) | Monte Carlo propagation for bridge predictions with a non-parametric distribution-convergence check. | Supports propagation and numerical convergence monitoring; does not itself prove uncertainty preservation across heterogeneous service interfaces. |
| [Dealing with Uncertainty in Software Architecture on the IoT](https://doi.org/10.1007/978-3-030-24289-3_57) | Extends SosADL with concurrent constraints and twins to address partial knowledge and changing system composition; reports a vehicle-platooning example. | Architectural/configuration uncertainty must be distinguished from numerical measurement or prediction uncertainty. |
| [Real-Time Uncertainty-Aware DT Framework for Intra-Operative Valve Surgery](https://doi.org/10.1109/RAMS50514.2026.11424435) | Proposes a data pipeline, Bayesian state/covariance assimilation, coupled multiphysics, polynomial-chaos propagation, decision control and human authority. | Abstract gives an implementation roadmap. Do not infer clinical deployment, regulatory approval or verified standards compliance from its design claims. |

## Working extraction model

Trace **measurement → state/model → interface/coupled component → propagated prediction → validation/update → decision**. For each transition, extract the transferred quantity, uncertainty representation, units, temporal/spatial support, dependence assumptions, transformation, provenance and validation evidence. Persistence and versioning are necessary to reconstruct why a decision had a given uncertainty at a given time; merely displaying a confidence interval is insufficient evidence of that reconstruction.

Distinguish four questions: (1) is uncertainty represented; (2) is it updated from observations; (3) does it survive the transition between components and models with dependencies accounted for; (4) does a monitored or validated uncertainty estimate affect a decision? Mark unexamined transitions `not_assessed`, never `lost`.

The abstracts already supply examples of probabilistic graphs, persistent uncertain state, propagation and feedback control. Therefore the research gap cannot simply be “digital twins do not handle uncertainty.” A testable question is **which architectures preserve interpretable uncertainty and its provenance across heterogeneous interfaces, and with what validation evidence**. That gap remains a hypothesis until full-text coding and the additional database searches are completed.
