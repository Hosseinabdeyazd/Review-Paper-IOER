# Protocol v0.1 — Systematic Conceptual and Architectural Scoping Review

**Draft, not registered; no search run or screening completed under this protocol.**
Method orientation: **JBI-style scoping review for concept/architecture heterogeneity, reported with PRISMA-ScR**; structured qualitative content analysis and typed architecture graph coding. Do not imply PRISMA-ScR alone determines search quality. Full protocol to be frozen before formal retrieval.

## Objective and questions

**PCC framing**
- **Population / concept object:** DT definitions, architectures, implementations and digital-twin-adjacent technical systems.
- **Concept:** explicit architecture components, functions, observed coupling relations, synchronization, stakeholders, governance and evidence of implementation.
- **Context:** built environment from component/building to city/region, emphasizing MFA, circular built environment, recovery, reuse and environmental assessment.

**RQ-D1** How are digital twins in built environments defined, and which attributes are presented as minimum, optional or maturity-dependent across application domains?

**RQ-D2** Which *structural, functional and interaction topologies* are reported, and how do physical–digital and model–model links, updating strategies and users differ across scales?

**RQ-D3** Which of these architectures and functions demonstrably support building-material stocks, MFA, R-strategies, recovery, resource supply–demand and LCA?

**RQ-D4** What architecture/interface conditions are reported for information provenance, uncertainty representation, handoff, validation and feedback? What remains unreported?

## Design: two linked, separately screened evidence streams

- **A — General DT definition / reference architecture:** DT terminology, standardized concepts, conceptual models, system architecture, data models, process / communication, synchronization, governance, maturity.
- **B — Circular built-environment applications:** DT + building stock, material passports, dynamic MFA, circularity / R-strategies, deconstruction, supply/demand, urban mining, environmental assessment. Complement by cited-reference searching from foundational models.
- **Existing S1–S5 systematic-review corpus** is a separate analytic companion, **not automatically included in DT corpus A**; a study with MFA but without DT evidence can inform domain interface requirements but not DT prevalence.

## Seed search strategy (DRAFT; database syntax needs local testing)

**Scopus stream A** (draft):
```
TITLE-ABS-KEY( ("digital twin*" OR "urban digital twin*" OR "city digital twin*")
 AND ("defin*" OR "conceptual model*" OR "reference architecture*" OR "architecture*" OR "framework*" OR "ontology" OR "synchroni*" OR "interoperab*" OR "maturity") )
```

**Scopus stream B** (draft):
```
TITLE-ABS-KEY( ("digital twin*" OR "urban digital twin*" OR "city digital twin*")
 AND ("built environment" OR building* OR construction OR "urban stock*" OR cit*)
 AND ("material flow*" OR "material stock*" OR "material passport*" OR circular* OR reus* OR recycl* OR "urban mining" OR "life cycle assessment" OR LCA OR deconstruction) )
```

Replicate translations and record exact field tags for **Web of Science Core Collection**, **IEEE Xplore**, and potentially **Compendex**; Scopus should not be treated as a sole sufficient architecture repository. Supplement ISO/IEC, DTC, CDBB/Gemini and verified technical documentation as a **clearly marked grey-literature/standards stratum**. Capture search date, database, query ID, filters, export count, and file hash. No language restriction at search stage; document translation treatment at full-text stage. Check preprints vs published versions. Use backward/forward citation chaining with reproducible rules.

## Eligibility — two levels, not only "says digital twin"

**Conceptual/architectural eligible (A):** explicitly defines a DT or describes a structural/functional reference architecture, formalized digital–physical interface, maturity or governance framework; source identifiable and sufficiently detailed to extract model components.

**Applied eligible (B):** DT-labeled built-environment study with documented physical referent and at least a described digital representation / updating or coupling path, and relevance to stock, materials, reuse, resource flows or environmental impacts. Separate "claimed DT" from "verified DT functioning"; do **not** reject studies just because they lack full automation or high-frequency sensing.

**Comparison evidence (C):** non-DT GIS/MFA/LCA workflows can be tagged as **non-DT comparator** for interface functions only; not counted in DT architectural prevalence denominators.

**Exclusions:** marketing-only mentions with no definitional, architectural, or function detail; inaccessible content with insufficient evidence for requested coding (log separately); duplicate publications; irrelevant sectors without transferable definition/architecture evidence. Grey documents treated in separate strata.

## Extraction units / codebook

- **Unit 1: study** — id, citation, study type, research/technical domain, spatial scope, lifecycle stage, intervention/decision context, implemented/proposed, source access, potential bias.
- **Unit 2: definition** — exact location, concept elements, claimed necessities, optional capabilities, exclusions, definition version and contradictory source.
- **Unit 3: component** — node ID, node class, semantic meaning, physical/digital/service/user category, granularity, deployment.
- **Unit 4: directed interface** — source and target IDs; type (observes, transforms, synchronizes, simulates, validates, updates, recommends, actuates); periodic/event/streaming; data types and units; provenance; uncertainty representation; evidence location; reported implementation.
- **Unit 5: model handoff** — upstream parameter and uncertainty, downstream parameter, mapping, covariance preservation, uncertainty outcome (preserved / legitimately reduced / amplified / transformed / masked-lost / unassessed) **only if evidence supports**.
- **Unit 6: claim quality** — textual claim vs diagram only vs described implementation vs empirical validation with comparator; insufficient = Not reported / Not assessed.

## Domain-specific coding items

Context items from Georg's feedback: stakeholders (operational/strategic), planning processes, component/material/connection detail, natural vs anthropogenic resources, supply/demand matching, spatial boundaries, temporal horizons, MFA methods and typologies, indicators/R-strategies, GIS/BIM/GeoAI and AI function, programming stack. These are extraction covariates; not mandatory terms on every search query.

## Screening, adjudication, reporting

1. Pilot diverse 10–15 sources including Abdelrahman, AlBalkhy, Kosse, Geremicca, De Wolf, Malihi, urban DTs and non-DT comparators; refine labels *before* recording final tests.
2. Freeze inclusion rules and data dictionary. Two independent reviewers code a calibration sample of definitions/components/edges, report agreement and adjudication protocol; do not invent a kappa result.
3. Manage duplicate records by DOI, title/year and version; keep full-text evidence with page/figure and an immutable source ID.
4. Present PRISMA-ScR flow and descriptive distributions with denominators separated by A/B/C strata; use qualitative and network synthesis where comparable effect-size data do not exist.
5. For ambiguity, record **Unclear / Not reported** and a reviewer note; never infer an API implies bi-directionality or a dashboard implies physical feedback.
6. Quantitative aggregation of uncertainty handoffs should be conditional on comparable evidence; review diagrams cannot supply fabricated numerical edge weights.
7. Maintain search-protocol versions and deviation log. Append new studies after the freeze as a separately dated update, not silent changes.

## Critical validity threats

- **Self-label bias:** a "DT" in the title may only be a BIM/shadow.
- **Publication bias:** case studies demonstrating success may omit failure modes.
- **Source-type asymmetry:** a standards document, position paper and instrumented prototype yield different kinds of evidence.
- **False equivalence:** frequency of a term ≠ minimum requirement; architectural diagram ≠ implemented data exchange.
- **Confounding:** more complex models do not necessarily improve validation/propagation (see Geremicca 2026, BIM-to-energy interface).
- **Scope drift:** refrain from an entire new city-DT review unless justified by the architecture–MFA interface question.

## Repositories and reproducibility

Older proposed engineering materials are under [../Digital Twin Architecture](../Digital%20Twin%20Architecture/README.md). This **DT/** directory controls the independent, evidence-based conceptual/architectural assessment. Both are linked only *after* completing the literature-coded matrix.

## Method anchors

Abdelrahman et al. (2025), DOI 10.1016/j.buildenv.2025.112748 (NLP analysis + expert survey; not a substitute for our architecture-edge extraction); Davila Delgado & Oyedele (2021), DOI 10.1016/j.aei.2021.101332 (structural vs functional analysis); JBI scoping-review guidance; PRISMA-ScR reporting guidance (https://www.prisma-statement.org/scoping); other domain sources in [01_definition_evidence.md](01_definition_evidence.md).
