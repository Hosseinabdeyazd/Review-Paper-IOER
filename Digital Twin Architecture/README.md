# Digital Twin Architecture

## Purpose

This workspace develops a **multi-layer Digital Twin architecture** that can connect flexibly to the analytical streams S1–S5 of the review:

- S1 — Observation / GeoAI
- S2 — Building characterization / Material stock
- S3 — Stock dynamics / Event timing
- S4 — Circularity / Recoverability
- S5 — LCA / Decision

The Digital Twin is **not treated as S6** and is not assumed to map one-to-one onto S1–S5. It is a cross-cutting architecture whose capability layers may connect to multiple analytical streams at the same time.

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

## Folder structure

```text
Digital Twin Architecture/
├── README.md
├── UNCERTAINTY_HOTSPOT_REGISTER.md
└── layers/
    ├── DT-L1_observation_data_acquisition.md
    ├── DT-L2_identity_integration_context.md
    ├── DT-L3_state_reconstruction_inference.md
    ├── DT-L4_dynamics_material_flow.md
    └── DT-L5_circularity_lca_decision.md
```

The layer files are working documents. They will be expanded one by one as the review progresses.

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

## Immediate next step

Start with **DT-L1 — Observation & Data Acquisition** and define:
1. exact input families;
2. minimum metadata;
3. uncertainty sources;
4. validation requirements;
5. outputs required by S1–S5;
6. conditions under which DT-L1 should request additional observations.
