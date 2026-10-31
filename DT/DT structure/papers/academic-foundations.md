# Academic foundations of the proposed digital twin framework

Version: 2026-10-31. Status: literature-informed conceptual synthesis for manuscript development. This is not a validated universal taxonomy, an ISO-conformance assessment or a completed systematic review.

## What the framework adds

The proposal distinguishes **A, the design brief**, **B, configuration descriptors**, **C, functional allocation**, and an **implemented digital twin**. A defines intended use and evidence needs; B describes structural choices; C assigns required activities to components and people. Model calibration, prediction and operational optimization require instantiated models and data. They do not operate on a vocabulary of architecture choices alone.

The organization, arrows and mapping to B are our synthesis. Papers support individual concepts, design approaches or case implementations; they do not validate the complete drawing or every candidate pairing in Figure S2.

## Evidence notation

- **L: literature-supported concept**. The source explicitly discusses the concept; its scope still applies.
- **E: case evidence**. A paper demonstrates one implementation, without establishing a universal class.
- **S: proposed synthesis**. Our grouping, interpretation or design implication.
- **U: unresolved**. This selected source set does not yet substantiate the exact descriptor or proposed category. This is not a claim that no relevant literature exists.

Reference keys R1-R16 are shared by the figures and tables. Full-text access and abstract-only checking are distinguished below. No figure claims that sixteen complete papers were read in this update.

## Claims and interpretation boundaries

| Figure element or claim | Basis | What is supported | What remains our proposal |
|---|---|---|---|
| A: object, purpose, architecture intent, data and services | R1, R5; L/S | Cross-domain characterization and use-specific scope | The five-card design brief; R1 actually has six dimensions including modelling |
| Decision specification | R2, R5, R6, R13; S | Design choices, context and distribution of human/computer roles | Six fields: subject, alternatives, objectives, scope/horizon, evidence and authority |
| Design of the twin versus design using a twin | R2, R13; S | R2 addresses DT-system design; R13 addresses design/operation of the represented system | Their explicit separation in our diagram |
| B configuration vocabulary | R1-R6, R8, R10, R14-R16; L/E/S/U | Selected architecture terms and implementation examples | Six families; no completeness or mutual exclusivity claim |
| C functional allocation | R2, R6; L/S | Service allocation and human/computer role distribution | The five-row activity table and all B-column mappings |
| Calibration and updating | R3, R10, R11; E | Parameter updating using observations in particular systems | General placement as a reusable capability, not a mandatory stage |
| Verification and validation | R12; L | Distinct activities establishing evidence in a context of use | The criteria gate and explicit diagnose/revise route |
| Prediction, optimization and control | R3, R7-R10; L/E | Coupled analytical and operational capabilities | Optional use-dependent paths; no requirement that all DTs execute all three |
| Outputs beyond commands | R5, R9, R13; L/E/S | Planning, recovery/remanufacturing and target-system design decisions | The combined list of possible outcome types |
| All-to-all adjacent-column curves in S2 | S | A display convention only | Candidate pairings, not empirical compatibility or causal connections |

## Decisions in A and their consequences

The proposed decision specification asks: **what is being decided; which variables or alternatives may change; what objectives and constraints apply; what scope and consequence horizon matter; what evidence is required; and who analyses, selects, approves and executes?** These are cross-cutting questions, not a sixth mandatory component or a published six-item taxonomy.

Three subjects should be distinguished: designing/revising the twin; deciding whether its evidence is adequate for a use; and deciding about the represented target using the twin. The last includes target design, operation, maintenance and recovery. Subject and time horizon do not, on their own, determine automation authority.

Prediction can be an end service or an input to decision support. Optimization can return advice without execution. Calibration may itself use an optimization algorithm, but its variables are model parameters, whereas operational optimization may vary a schedule, maintenance choice or control input. Validation assesses adequacy; it does not tune an output until it looks acceptable. Verification addresses implementation and specified requirements. Fitting and evaluation evidence should be managed to avoid an unjustified claim of independent validation.

Model activities may occur before deployment and during use. Failed evaluation calls for diagnosis: data, parameters, model form, operating context or design may be responsible. Revisions require reassessment. The figure does not assert that calibration alone establishes validity or that every failure can be fixed by recalibration.

## Source register

### R1 — Cross-domain characterization

Xiong, G., Li, H., and Gao, Y. (2025). **Cross-domain comparative analysis of digital twins and universalised solutions.** *Advanced Engineering Informatics*, 68, 103726. DOI: [10.1016/j.aei.2025.103726](https://doi.org/10.1016/j.aei.2025.103726).

[Published open-access text](https://orca.cardiff.ac.uk/id/eprint/180281/1/1-s2.0-S1474034625006196-main.pdf). Relevant location: characterization framework and architecture discussion. The paper's dimensions are object, purpose, system architecture, data, modelling and services. These are not our six configuration columns. Access checked: published text and institutional record.

### R2 — Designing systems of twins and services

Human, C., Basson, A. H., and Kruger, K. (2023). **A design framework for a system of digital twins and services.** *Computers in Industry*, 144, 103796. DOI: [10.1016/j.compind.2022.103796](https://doi.org/10.1016/j.compind.2022.103796).

[Publisher record](https://www.sciencedirect.com/science/article/abs/pii/S0166361522001920). Relevant location: abstract/highlights and design framework. Supports systematic design decisions, aggregated twins, services and modularity. It does not provide our A/B/C figure. Access checked in this update: publisher abstract and highlights; detailed step-level quotation is not claimed.

### R3 — Calibration, inference and decisions

Kapteyn, M. G., Pretorius, J. V. R., and Willcox, K. E. (2021). **A probabilistic graphical model foundation for enabling predictive digital twins at scale.** *Nature Computational Science*, 1, 337-347. DOI: [10.1038/s43588-021-00069-0](https://doi.org/10.1038/s43588-021-00069-0).

[Author manuscript](https://arxiv.org/html/2012.05841). Relevant locations: mathematical abstraction; calibration phase; operational phase. The UAV model is calibrated with experimental data; the in-flight damage/decision example is synthetic. It supports coupled data/model/decision reasoning, not field validation of every route in our figure. Access checked: author manuscript.

### R4 — Engineering perspective

Ferrari, A., and Willcox, K. (2024). **Digital twins in mechanical and aerospace engineering.** *Nature Computational Science*, 4, 178-183. DOI: [10.1038/s43588-024-00613-8](https://doi.org/10.1038/s43588-024-00613-8).

[Publisher](https://www.nature.com/articles/s43588-024-00613-8). A Perspective informing modelling and use-specific engineering concerns; not a new experimentally validated universal taxonomy. Access checked: bibliographic record and indexed publisher text; the direct publisher PDF was not consistently accessible in this update. Fine-grained claims should be checked against a locally retained full text before manuscript submission.

### R5 — Scope and requirements

Shao, G., and Helu, M. (2020). **Framework for a Digital Twin in Manufacturing: Scope and Requirements.** *Manufacturing Letters*, 24. DOI: [10.1016/j.mfglet.2020.04.004](https://doi.org/10.1016/j.mfglet.2020.04.004).

[Open author manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC7431924/). Relevant locations: Section 2, perspectives; Section 3, example uses. Supports application-dependent scope, fidelity and temporal integration, including periodic offline connection. Manufacturing scope applies. Its description of ISO 23247 development is historical, not a statement of the standard's current status. Access checked: full manuscript.

### R6 — Responsibility and authority

Agrawal, A., Thiel, R., Jain, P., Singh, V., and Fischer, M. (2023). **Digital Twin: Where do humans fit in?** *Automation in Construction*, 148, 104749. DOI: [10.1016/j.autcon.2023.104749](https://doi.org/10.1016/j.autcon.2023.104749).

[Accepted manuscript](https://arxiv.org/pdf/2301.03040). Relevant locations: role-allocation framework, Table 3 and building-temperature example. Distinguishes observer, analyst, decision maker and action executor, with automation considered per role. Our six-field decision brief is not their taxonomy. Access checked: accepted manuscript; publication DOI separately verified.

### R7 — Prescriptive components and timing

Walton, R. B., Ciarallo, F. W., and Champagne, L. E. (2024). **A unified digital twin approach incorporating virtual, physical, and prescriptive analytical components to support adaptive real-time decision-making.** *Computers & Industrial Engineering*, 193, 110241. DOI: [10.1016/j.cie.2024.110241](https://doi.org/10.1016/j.cie.2024.110241).

[Institutional record](https://scholar.afit.edu/facpub/1506/). Supports prescriptive analysis and timing concerns in a transporter-system example. Access checked: institutional abstract; full subscription text not claimed as reviewed. No universal latency threshold is inferred.

### R8 — Adaptive architecture

Ogunsakin, R., Mehandjiev, N., and Marin, C. A. (2023). **Towards adaptive digital twins architecture.** *Computers in Industry*, 149, 103920. DOI: [10.1016/j.compind.2023.103920](https://doi.org/10.1016/j.compind.2023.103920).

[Institutional record](https://keele-repository.worktribe.com/output/1053432/towards-adaptive-digital-twins-architecture). Relevant locations: Section 3.3 architecture; Section 6 discussion. Supports multi-agent coordination, federated architecture, simulation and online optimization in the proposed adaptive system. Demonstration is an in-silico manufacturing system, not equivalent to full real-factory validation. Access checked: publisher text and institutional abstract.

### R9 — Recovery and remanufacturing decisions

Kerin, M., Hartono, N., and Pham, D. T. (2023). **Optimising remanufacturing decision-making using the bees algorithm in product digital twins.** *Scientific Reports*, 13, 701. DOI: [10.1038/s41598-023-27631-2](https://doi.org/10.1038/s41598-023-27631-2).

[Publisher](https://www.nature.com/articles/s41598-023-27631-2); [bibliographic record](https://pubmed.ncbi.nlm.nih.gov/36639730/). Supports remanufacturing as a decision application, not an obligation to actuate every twin. Access checked in this update: bibliographic record and abstract; full-text endpoints were intermittently blocked. Environmental/social performance and continuous synchronization are not claimed as validated here.

### R10 — Model adaptation and control

Chen, Y.-P., Suarez, D., Tsai, Y.-K., Karkaria, V., Hu, G., Chen, Z., Guo, P., Cao, J., and Chen, W. (2026). **Adaptive digital twin of sheet metal forming via proper orthogonal decomposition-based Koopman operator with model predictive control.** *Journal of Manufacturing Systems*, 86, 762-773. DOI: [10.1016/j.jmsy.2026.04.004](https://doi.org/10.1016/j.jmsy.2026.04.004).

[Author manuscript](https://arxiv.org/html/2511.10852v1). Relevant locations: model validation, online updating and experimental demonstration. Reduced modelling, recursive parameter updates and MPC have distinct roles. This is case evidence, not a mandatory DT architecture. Access checked: author manuscript and publication metadata; manuscript wording may differ from the final article.

### R11 — Online calibration and validation

Lugaresi, G., Dhore, A. S., and Matta, A. (2026). **Joint online validation and parameter calibration within a digital twin framework: an approach based on bootstrap particle filtering.** *Procedia CIRP*, 146, 786-791. DOI: [10.1016/j.procir.2026.03.284](https://doi.org/10.1016/j.procir.2026.03.284).

[Publisher](https://www.sciencedirect.com/science/article/pii/S2212827126012163). Supports monitoring discrepancies, diagnosis and parameter updating for a discrete-event simulation twin. Evidence is a lab-scale production proof of concept. Access checked: publisher abstract; not a full-text methodological audit.

### R12 — Verification and validation

Bitencourt, J., Wooley, A., and Harris, G. (2025; online 2024). **Verification and validation of digital twins: a systematic literature review for manufacturing applications.** *International Journal of Production Research*, 63(1), 342-370. DOI: [10.1080/00207543.2024.2357741](https://doi.org/10.1080/00207543.2024.2357741).

[Publisher](https://doi.org/10.1080/00207543.2024.2357741). Relevant locations: V&V definitions and systematic-review discussion. Supports their distinction and the importance of context of use; does not establish a universal pass/fail threshold. Access checked: indexed publisher sections and publication record; no page-specific quotation asserted.

### R13 — Decisions across target-system design and operation

van Beek, A., Karkaria, V. N., and Chen, W. (2023). **Digital twins for the designs of systems: a perspective.** *Structural and Multidisciplinary Optimization*, 66, 49. DOI: [10.1007/s00158-023-03488-x](https://doi.org/10.1007/s00158-023-03488-x).

[Published manuscript](https://par.nsf.gov/servlets/purl/10468762). Supports integrating design and operational decisions across the represented system's lifecycle. Do not confuse this with designing DT software. Access checked: published repository text/abstract; used as conceptual support, not broad empirical validation.

### R14 — Data-flow integration categories

Kritzinger, W., Karner, M., Traar, G., Henjes, J., and Sihn, W. (2018). **Digital Twin in manufacturing: A categorical literature review and classification.** *IFAC-PapersOnLine*, 51(11), 1016-1022. DOI: [10.1016/j.ifacol.2018.08.474](https://doi.org/10.1016/j.ifacol.2018.08.474).

[Publisher](https://www.sciencedirect.com/science/article/pii/S2405896318316021). Distinguishes digital model, shadow and twin by integration. Automated physical-to-digital-only flow is a shadow in this classification. This does not settle definitions across all disciplines or equate bidirectional exchange with autonomous control. Access checked: publisher record and classification discussion available in R8.

### R15 — Coexisting modular and semantic architecture choices

Kosse, S., Hagedorn, P., and König, M. (2025). **Semantic Digital Twins in Construction: Developing a modular System Reference Architecture based on Information Containers.** *Advanced Engineering Informatics*, 67, 103483. DOI: [10.1016/j.aei.2025.103483](https://doi.org/10.1016/j.aei.2025.103483).

[Publisher](https://www.sciencedirect.com/science/article/pii/S1474034625003763). Relevant locations: methodology, Figure 2 architecture and implementation. Combines modularity, services and semantic information/knowledge graphs. Construction case evidence supports coexistence, not exhaustive compatibility. Access checked: publisher full-text sections.

### R16 — Systems of twins terminology

**Systems of Digital Twins: A Systematic Literature Review and a formal framework.** (2026). *Digital Engineering*, 9, 100100. DOI: [10.1016/j.dte.2026.100100](https://doi.org/10.1016/j.dte.2026.100100).

[Publisher](https://www.sciencedirect.com/science/article/pii/S2950550X26000130). Supports examining aggregate, composite, network, federated and ecosystem terminology while acknowledging inconsistent definitions. Access checked: indexed publisher abstract; author metadata and exact term definitions require full-text verification before a submission bibliography is finalized. The title-led record deliberately avoids inventing unverified authors.

## Publication limits and next validation step

The selected set includes three papers in Nature-portfolio journals (two in *Nature Computational Science*, one in *Scientific Reports*), not three papers in the flagship *Nature*. Manufacturing/mechanical cases are prominent; cross-domain universality has not been established. The source list is a seed set, not a systematically screened corpus.

Before presenting B as a formal taxonomy, operationalize each term, separate overlapping subattributes, complete unresolved evidence, code a cross-domain sample and assess reproducibility of the coding. Evaluate compatibility at the level of a concrete use case, interfaces and constraints. A pair of independently cited nodes does not prove their connecting edge.

ISO reference architectures may inform a later comparison, but this package claims neither ISO endorsement nor compliance. The public standard record alone is insufficient for a clause-level mapping.

Published papers are linked rather than redistributed. Our diagrams are original drawings and are not reproductions of publisher figures.
