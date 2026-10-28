# DT — Systematic Conceptual and Architectural Review

**Status:** research protocol and seed evidence, v0.1 (2026-10-28). **Not a completed systematic review.**
**Purpose:** establish an evidence-derived account of what a digital twin (DT) is, how DT architectures and functions are related, and only then test how circular built-environment and material-flow workflows can be coupled to these architectures.

This directory is deliberately **separate from** [Digital Twin Architecture](../Digital%20Twin%20Architecture/README.md), which contains earlier *proposed / working* technical systems, parameters and computational engines. The existing directory must not be interpreted as a systematically validated architecture.

## Sequence and epistemic rules

1. **Definition evidence** — collect verbatim bibliographic metadata and carefully paraphrased definitions; do not select one preferred definition in advance. [01_definition_evidence.md](01_definition_evidence.md).
2. **Provisional operational definition** — explicitly mark our *working hypothesis*, eligibility thresholds, and disagreements in the literature. [02_working_definition.md](02_working_definition.md).
3. **Architectural decomposition** — separate entities, functions, services, interfaces, coupling topology, scale, temporal behavior and governance. Include the **HPRT / LTDS** distinction, and differentiate it from network topology. [03_architecture_typology.md](03_architecture_typology.md).
4. **Reproducible review protocol** — run two linked evidence streams (concept / architecture and circular-domain implementations) before revising the taxonomy; preregister changes and keep an audit trail. [04_review_protocol.md](04_review_protocol.md).
5. **Architecture–Function–Evidence matrix** — one record per source–component–function claim; confidence depends on accessible evidence and implementation status. [05_architecture_function_evidence.csv](05_architecture_function_evidence.csv).
6. **Concept-development ledger** — new terms may be proposed only after collision checking against existing literature; distinguish *open-loop*, *closed-loop*, *federated* etc. (existing vocabulary) from proposed constructs. [06_concept_development.md](06_concept_development.md).
7. **Research bridge** — test relations to GeoAI, building stock, stock dynamics, circular recovery, impact assessment and uncertainty continuity without declaring these five streams DT layers. [07_research_bridge.md](07_research_bridge.md).

## Evidence boundaries

- **Source-derived:** traceable to the article's exact section / page, or to an accessible publisher / institutional abstract. The evidence register records access status.
- **Inference:** a defensible synthesis of several sources, clearly tagged as such.
- **Proposed:** a hypothesis, taxonomy or schema that has not been tested. Do not label "novel" before an explicit terminology/novelty audit.
- **Not reported ≠ absent.** A missing implementation detail must not be automatically coded as technical failure.
- **Integration ≠ validation ≠ uncertainty propagation.** A data connection is not proof that distributions/correlations survive an analytical handoff.
- **A systematic review does not prove a new DT performs better.** That would require a subsequent prototype / controlled test.
- **HPRT** and **LTDS** are component-pattern families reported by Abdelrahman et al. (2025), not a pair of mutually exclusive ontology classes nor the sole valid DT architectures.

## Primary anchors (verified)

- Abdelrahman et al. (2025), *Building and Environment*, DOI: [10.1016/j.buildenv.2025.112748](https://doi.org/10.1016/j.buildenv.2025.112748). Full text available in the research conversation (19 pages), sections 3–5.
- AlBalkhy et al. (2024), *Automation in Construction* **162**, 105368, DOI: [10.1016/j.autcon.2024.105368](https://doi.org/10.1016/j.autcon.2024.105368). Publisher abstract/metadata verified.
- Davila Delgado & Oyedele (2021), *Advanced Engineering Informatics* **49**, 101332, DOI: [10.1016/j.aei.2021.101332](https://doi.org/10.1016/j.aei.2021.101332).
- Kosse, Hagedorn & König (2025), *Advanced Engineering Informatics* **67**, 103483, DOI: [10.1016/j.aei.2025.103483](https://doi.org/10.1016/j.aei.2025.103483).
- Geremicca & Bilec (2024), *Sustainable Cities and Society* **107**, 105445, DOI: [10.1016/j.scs.2024.105445](https://doi.org/10.1016/j.scs.2024.105445). Full text available in the conversation.
- Geremicca et al. (2026), *Energy and Buildings* **359**, 117332, DOI: [10.1016/j.enbuild.2026.117332](https://doi.org/10.1016/j.enbuild.2026.117332). Full text available in the conversation.
- De Wolf et al. (2024), *npj Materials Sustainability* **2**, 36, DOI: [10.1038/s44296-024-00034-8](https://doi.org/10.1038/s44296-024-00034-8).
- Malihi (2026), *Digital Engineering*, 100140, DOI: [10.1016/j.dte.2026.100140](https://doi.org/10.1016/j.dte.2026.100140). Full pre-proof available in the conversation.
- [Digital Twin Consortium — definition and glossary](https://www.digitaltwinconsortium.org/initiatives/the-definition-of-a-digital-twin/); [Gemini Principles](https://www.cdbb.cam.ac.uk/DFTG/GeminiPrinciples); [ISO/IEC 30173:2023](https://www.iso.org/standard/81442.html) (full ISO text **not** audited).

**Warning:** An earlier local source register cites a different AlBalkhy author list / article number. The publisher-confirmed record is AlBalkhy, Karmaoui, Ducoulombier, Lafhaj & Linner, 2024, *Automation in Construction* 162, 105368; **do not silently propagate the earlier metadata**.

## Next evidence gates

- Freeze the exact search queries, scope and eligibility rules.
- Pilot 10–15 deliberately diverse texts; conduct double independent coding for core fields and adjudicate disagreements.
- Extract *edges* (source entity, destination entity, semantics, direction, update trigger, validation evidence), not only counts of architectural components.
- Distinguish building, neighbourhood, city, regional and federated multi-asset settings.
- Only after the pilot produce figures, architecture classes and terminology candidates.

No searches, screening decisions, quality assessments or numerical meta-analyses are claimed complete by creating this folder.
