# Digital Twin Architecture — Evidence-Driven Working Architecture v0.2 — Building-to-Material Decision Twin

## Current architecture status

**Working version: v0.3 — literature-informed master architecture.**

The architecture has now been expanded using literature across:
- IOER / Georg Schiller material cadastres, MCIs and continuous MFA;
- Robert H. Crawford's embodied environmental inventory and CE-assessment work;
- geo-referenced material-stock and prospective MFA;
- building archetypes and material-intensity modelling;
- material passports / DPP ontologies;
- pre-demolition audit, component reuse and design-for-disassembly;
- service-life / replacement uncertainty;
- LCA / environmental uncertainty and Level(s).

The detailed specification is distributed across:
- `MASTER_ARCHITECTURE_SPECIFICATION.md`
- `MASTER_PARAMETER_CATALOG.md`
- `LITERATURE_EVIDENCE_BASE.md`
- `MATERIAL_DECISION_PROFILE.md`
- `UNCERTAINTY_TRACEABILITY_MODEL.md`
- `schemas/BUILDING_MATERIAL_TWIN_TEMPLATE.yaml`

The master parameter catalog is intentionally extensive. Not all fields are mandatory for every building; parameters are marked conceptually as core, conditional, advanced or optional and should be populated according to available evidence and decision need.

---

## Status

**Version:** v0.2 — detailed evidence-driven architecture, 2026-10-02.

This is a working research architecture, not a finished standard. It has been expanded using literature on building material stocks, material intensities, GeoAI/data acquisition, material passports, design for disassembly, dynamic material-flow analysis, circularity logistics, building LCA, and uncertainty. Every field should continue to receive an evidence status as the systematic review progresses.

## Purpose

This workspace develops a **multi-layer Digital Twin architecture** that can connect flexibly to the analytical streams S1–S5 of the review.

### Final project objective

The Digital Twin is **not primarily a building-reconstruction product**. Its final purpose is to generate a **decision-ready material profile for any selected building**.

For a selected building, the system should ultimately be able to answer:

1. **What materials are present?**
2. **How much of each material is present?**
3. **When are these materials expected to be released?**
4. **What fraction may be reusable, recyclable, recoverable or disposable?**
5. **Which circular pathways are technically plausible: reuse, closed-loop recycling, open-loop recycling, recovery, disposal?**
6. **What are the effective substitution / replacement potentials?**
7. **What uncertainty accompanies each material quantity, quality, timing and pathway?**
8. **How do alternative circularity scenarios change environmental burdens?**
9. **Which uncertainty sources dominate the final decision?**

The final analytical unit is therefore **the material within a building, linked to its building, spatial, temporal, circularity and environmental context**.

The architecture should be designed backward from this output.

The workspace connects to the analytical streams:

- S1 — Observation / GeoAI
- S2 — Building characterization / Material stock
- S3 — Stock dynamics / Event timing
- S4 — Circularity / Recoverability
- S5 — LCA / Decision

The Digital Twin is **not treated as S6** and is not assumed to map one-to-one onto S1–S5. It is a cross-cutting architecture whose capability layers may connect to multiple analytical streams at the same time.

A key distinction is maintained between:

- **Analytical streams S1–S5**: the scientific evidence chain from observation to decision;
- **Digital Twin capability layers DT-L1–DT-L5**: the information, inference, simulation and decision infrastructure that can serve several streams simultaneously;
- **Material Decision Profile**: the final material-by-material output delivered for a selected building.

The Digital Twin layers are therefore not expected to correspond one-to-one with S1–S5.

The goal of this folder is to determine, layer by layer:

1. what data must enter each Digital Twin capability layer;
2. what processing, inference, transformation, aggregation or simulation occurs there;
3. what outputs are passed to downstream analytical streams;
4. what uncertainty sources arise at that layer;
5. what uncertainty is inherited from upstream layers;
6. what information may be transformed, aggregated, masked or lost;
7. what additional data, validation or modelling capability could reduce uncertainty;
8. where uncertainty remains highest and why;
9. how uncertainty affects circularity and LCA decisions.

> Important: "uncertainty reduction" is not assumed. Each proposed mechanism must later be supported by evidence showing whether it reduces, preserves, transforms, amplifies, masks or leaves uncertainty unassessed.

---

## Output-driven architecture

The architecture is organized around the following target flow:

```text
SELECTED BUILDING
      ↓
OBSERVE & IDENTIFY
      ↓
RECONSTRUCT HIDDEN BUILDING / MATERIAL STATE
      ↓
MATERIAL INVENTORY WITH UNCERTAINTY
      ↓
TIME-DEPENDENT MATERIAL RELEASE
      ↓
CIRCULAR PATHWAY OPTIONS
      ↓
EFFECTIVE REUSE / RECYCLING / SUBSTITUTION
      ↓
SCENARIO-SPECIFIC LCA CONSEQUENCES
      ↓
DECISION-READY MATERIAL PROFILE
      ↓
UNCERTAINTY HOTSPOTS & DATA-IMPROVEMENT NEEDS
```

---

## Working architecture

The current working hypothesis contains at least five Digital Twin capability layers:

| Layer | Working name | Main role |
|---|---|---|
| DT-L1 | Observation & Data Acquisition | Capture observable building, spatial and contextual data |
| DT-L2 | Identity, Integration & Context | Link heterogeneous data through persistent identity, spatial context, scale, time and provenance |
| DT-L3 | Building State Reconstruction & Inference | Infer hidden building properties and reconstruct the material/state "black box" |
| DT-L4 | Dynamics & Material-Flow Simulation | Represent changes, events, release flows and temporal evolution |
| DT-L5 | Circularity, LCA & Decision Intelligence | Generate and compare circularity, end-of-life, substitution and environmental decision scenarios |

These layers are **not a rigid pipeline**. Each layer may interact with several S1–S5 streams and may receive feedback from downstream decision needs.

---

## Cross-cutting control plane

The following dimensions apply across all Digital Twin layers:

- Persistent identity / Building ID
- Provenance
- Versioning
- Time / update history
- Spatial grain and coverage
- Regionalization and spatialization
- Uncertainty representation
- Uncertainty propagation
- Validation and calibration
- Interoperability / schema mapping
- Decision feedback

These dimensions should be treated as persistent metadata, not as isolated outputs of one layer.

---

## Relation to S1–S5

A one-to-one mapping is explicitly avoided.

| Digital Twin layer | S1 GeoAI | S2 Material Stock | S3 Dynamics | S4 Circularity | S5 LCA / Decision |
|---|---|---|---|---|---|
| DT-L1 Observation & Data Acquisition | strong | direct support | direct support | possible support | contextual support |
| DT-L2 Identity, Integration & Context | strong | strong | strong | strong | strong |
| DT-L3 State Reconstruction & Inference | support | strong | strong | strong | support |
| DT-L4 Dynamics & Material-Flow Simulation | support | support | strong | strong | strong |
| DT-L5 Circularity, LCA & Decision Intelligence | feedback | feedback | strong | strong | strong |

This matrix is conceptual and will be revised only when supported by reviewed literature.

---

## Layer-analysis template

For each Digital Twin layer we will document:

### A. Role
What problem does the layer solve?

### B. Inputs
What data enter the layer?
- value
- unit
- source
- spatial grain
- spatial coverage
- time
- provenance
- uncertainty representation

### C. Processing
What happens to the data?
- detection/classification
- linkage
- harmonization
- regionalization
- spatialization
- aggregation/disaggregation
- inference
- simulation
- scenario generation
- optimization

### D. Outputs
What is passed to other Digital Twin layers and to S1–S5?

### E. Uncertainty sources
What uncertainty originates here?

### F. Inherited uncertainty
What uncertainty enters from previous layers?

### G. Uncertainty fate
For each source:
- Preserved
- Legitimately reduced
- Amplified
- Transformed
- Masked / lost
- Unassessed

Transfer, representation change and magnitude change must be coded separately.

### H. Uncertainty-reduction opportunities
What additional evidence could reduce uncertainty?
- better observations
- local/regional data
- validation
- calibration
- finer or more appropriate scale
- additional inspection
- dynamic updating
- probabilistic inference
- scenario analysis

### I. Decision consequence
Does the uncertainty materially alter circularity or LCA decisions?

### J. Evidence status
Each proposed capability must be tagged as:
- source-supported;
- synthesis from multiple sources;
- proposed by us;
- not yet supported.

---

## Core information model

The core architecture is centered on linked entities rather than isolated variables:

```text
Building
 ├── Component
 │    └── Material
 ├── Event
 ├── Material Flow
 ├── Process / Facility
 ├── Circularity Scenario
 ├── Environmental Impact
 └── Decision
```

Every relevant parameter should be attached to an entity and should, where possible, carry:

- value or probability/distribution;
- unit;
- source/provenance;
- spatial context;
- temporal validity;
- uncertainty representation;
- version/update history.

Variables are also classified by their modelling role:

- **Observed** — directly measured or retrieved;
- **Inferred** — estimated from models, archetypes or proxies;
- **Dynamic** — state variables that evolve through time;
- **Scenario / decision** — assumptions or user-controlled choices.

This separation prevents properties such as building age, material type, demolition timing and open-/closed-loop choice from being mixed into one undifferentiated input list.

---

## Detailed architecture documents

- [Master Parameter Architecture](MASTER_PARAMETER_ARCHITECTURE.md) — detailed parameter-by-parameter architecture from observation to circularity/LCA decision.
- [Evidence Base](EVIDENCE_BASE.md) — literature supporting parameter families and the boundary between source evidence and our synthesis.
- [Uncertainty Propagation Map](UNCERTAINTY_PROPAGATION_MAP.md) — source-to-decision uncertainty paths and feedback logic.
- [Material Decision Profile](MATERIAL_DECISION_PROFILE.md) — final output contract.
- [Parameter Registry](PARAMETER_REGISTRY.md) — parameter metadata and taxonomy.
- [S1–S5 Connection Matrix](S1_S5_CONNECTION_MATRIX.md) — non-one-to-one mapping between Digital Twin capabilities and review streams.

---

## Folder structure

```text
Digital Twin Architecture/
├── README.md
├── UNCERTAINTY_HOTSPOT_REGISTER.md
├── UNCERTAINTY_TRACEABILITY_MODEL.md
├── DETAILED_PARAMETER_ARCHITECTURE_V1.md
├── LITERATURE_EVIDENCE_MAP.md
├── RESEARCH_SOURCE_REGISTER.md
├── CORE_ARCHITECTURE.md
├── MATERIAL_DECISION_PROFILE.md
├── MASTER_ARCHITECTURE_v1.md
├── PARAMETER_REGISTRY.md
├── LITERATURE_EVIDENCE_BASE.md
├── S1_S5_CONNECTION_MATRIX.md
└── layers/
    ├── DT-L1_observation_data_acquisition.md
    ├── DT-L2_identity_integration_context.md
    ├── DT-L3_state_reconstruction_inference.md
    ├── DT-L4_dynamics_material_flow.md
    └── DT-L5_circularity_lca_decision.md
```

The layer files are working documents. They will be expanded one by one as the review progresses.

### Key architecture documents

- **MASTER_PARAMETER_SCHEMA.md** — comprehensive parameter architecture across 21 domains, from geometry and structural systems to material quality, disassembly, circular pathways, LCA and uncertainty.
- **DT_LAYER_PARAMETER_MAP.md** — maps those parameter families to DT-L1–DT-L5 and S1–S5, including inputs, processing, outputs and uncertainty mechanisms.
- **DATA_ACQUISITION_AND_INFERENCE.md** — defines how values enter the twin, evidence hierarchies, and progressive refinement.
- **CIRCULARITY_ENGINE.md** — stock → release → salvage → quality gate → reuse/closed-loop/open-loop/recovery/disposal → substitution.
- **LCA_ENGINE.md** — material-to-LCA mapping, A–D modules, regional/time context, pathway burdens and uncertainty.
- **UNCERTAINTY_ENGINE.md** — end-to-end uncertainty records, propagation, dependence, hotspot analysis and value-of-information feedback.
- **EVIDENCE_BASE.md** — literature ledger supporting architecture decisions.

---

## Evidence inherited from review papers so far

### From JCP-02 — Patouillard et al. (2018)
Working lessons already accepted elsewhere in the repository:
- spatial variability and uncertainty should not be treated as synonyms;
- regionalization and spatialization are distinct operations;
- source and target spatial resolution may differ;
- aggregation and scale transition can affect uncertainty and information loss;
- spatial context and scale management are candidates for a Digital Twin capability layer.

### From JCP-03 — Baustert & Benetto (2017)
- uncertainty source and uncertainty fate are different dimensions;
- uncertainty transfer, representation change and magnitude change should be recorded separately;
- feedback/coupling architecture matters for uncertainty propagation.

### From Hossain & Ng (2018)
- circularity should be considered across building life-cycle stages, not only at demolition;
- quantity, quality, contamination and recoverability influence secondary-material decisions;
- open-loop and closed-loop pathways should be distinguished;
- substitution ratio / replacement coefficient can mediate the transition from recovered material to LCA benefit;
- LCA, material-flow analysis and design/digital tools can be integrated;
- dynamic material flows and temporal changes are relevant to building environmental assessment.

These lessons support the architecture, but the Digital Twin synthesis itself is our proposed integration and must be labelled as such.

---

## Current detailed architecture baseline

A literature-driven parameter architecture has now been created in:

- `DETAILED_PARAMETER_ARCHITECTURE_V1.md` — detailed parameter schema across DT-L1–DT-L5;
- `LITERATURE_EVIDENCE_MAP.md` — maps literature themes to architectural requirements;
- `RESEARCH_SOURCE_REGISTER.md` — seed literature register for continued expansion.

The architecture now explicitly includes, among others:

- building identity, location, geometry and morphology;
- age/cohort, use, construction history and renovation history;
- structural system and member-level material information;
- external wall assemblies, internal walls, roofs, floors, ceilings, windows and doors;
- building services and replaceable components;
- material type/subtype, quantity, density, intensity, composition, additives, coatings, origin and environmental coefficients;
- quality, condition, damage, contamination, purity, residual performance and certification;
- service lives, renovation/replacement cycles, demolition/survival modelling and event uncertainty;
- reuse, repair, closed-loop, open-loop, downcycling, recovery and landfill pathways;
- disassembly, connections, accessibility, separability, damage risk and selective demolition;
- processing, sorting, recovery yields, quality coefficients, substitution/replacement and market absorption;
- facilities, transport, storage, spatial demand-supply matching and timing;
- LCA methodology, modules, databases, allocation, avoided impacts and material-specific impact coefficients;
- uncertainty source, representation, propagation, contribution and targeted data-improvement logic.

This is a broad v1 architecture, not a closed final ontology. Every new paper can add, modify or challenge parameters, with evidence status recorded.

---

## Current research status

A first high-detail research synthesis has now been added in `MASTER_ARCHITECTURE_v1.md`. It expands the architecture from coarse layer descriptions to detailed building, component, material, lifecycle, circularity, logistics, environmental-impact and uncertainty variables.

The current parameter registry contains controlled families for geometry, typology/age, structure, envelope, internal components, services, material identity/quantity, condition/quality, connections/disassembly, service life/events, material flows, circular pathways, facilities/logistics, market context, LCA, scenarios, uncertainty and decision outputs.

`LITERATURE_EVIDENCE_BASE.md` records the evidence chain behind these choices and separates source-supported variables from synthesis and project-specific proposals.

This is **v1, not an exhaustive final ontology**. It is intentionally a living architecture that will be revised as the systematic review and full-text coding progress.

---

## Core output contract

For a selected building, the system should produce one or more **Material Decision Profiles**, each at material/component-batch level:

```text
material identity
→ component/location
→ quantity distribution
→ quality/condition/hazards
→ expected release event/time
→ technically recoverable quantity
→ direct reuse quantity
→ closed-loop recyclable quantity
→ open-loop recyclable quantity
→ substitution/replacement potential
→ process/logistics
→ scenario environmental consequences
→ uncertainty decomposition
→ decision robustness
→ next-data recommendation
```

The architecture must support both sparse-data and high-evidence cases. A type-based material estimate and a physically audited material inventory can occupy the same schema but must never be presented as equally certain evidence.

---

## Immediate next step

Before expanding DT-L1 in isolation, the architecture should now be developed **from the final material output backward**.

Priority sequence:

1. continue mapping new literature into `LITERATURE_EVIDENCE_BASE.md`;
2. validate/refine the fields in `MASTER_PARAMETER_CATALOG.md`;
3. expand each DT layer against the master catalog;
4. identify material-specific quality/reuse/recycling thresholds rather than assuming universal rates;
5. connect evidence tiers to uncertainty propagation and hotspot analysis;
6. use the YAML template as the canonical input/output structure for future data ingestion.

This avoids building an oversized Digital Twin containing parameters that do not contribute to material-level circularity and environmental decisions.
