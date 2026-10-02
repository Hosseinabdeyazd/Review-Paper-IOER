# Uncertainty Traceability Model

## 1. Objective

The Digital Twin must trace where uncertainty enters, how it changes, and how it affects each material-level circularity and environmental decision.

## 2. Uncertainty chain

Observation → Identity/Context → Material Inference → Dynamic Release → Circular Pathway → LCA/Decision

Every downstream output may contain:
- inherited uncertainty;
- newly introduced uncertainty;
- transformed uncertainty;
- uncertainty legitimately reduced;
- uncertainty amplified by modelling/context;
- information masked or lost;
- unassessed uncertainty.

## 3. Core uncertainty families

### U1 — Observation
Image/sensor resolution, measurement error, classification confidence, missing records.

### U2 — Identity / integration / context
Entity mismatch, incorrect spatial join, outdated temporal linkage, generic data used for a local building, scale mismatch.

### U3 — Material-state inference
Archetype assignment, hidden assemblies, material-intensity uncertainty, renovation-history uncertainty, proxy transfer.

### U4 — Dynamics
Service life, renovation/demolition timing, event probability, future stock change.

### U5 — Circularity process
Separability, contamination, recovery rate, process yield, quality retention.

### U6 — Scenario / market
Open-loop vs closed-loop choice, future demand, facility availability, transport constraint, technology uptake.

### U7 — Substitution / replacement
Functional equivalence, substitution ratio, replacement coefficient.

### U8 — LCA / environmental
Foreground inventory, background database, energy mix, system boundary, allocation, characterization and model choice.

## 4. Record required for each uncertainty source

| Field | Description |
|---|---|
| uncertainty_source_id | unique record |
| entity/material | object affected |
| origin_layer | DT-L1...DT-L5 |
| affected_streams | S1...S5 |
| source_type_original | terminology used by source |
| source_type_harmonized | project mapping |
| variability_or_uncertainty | real variability / uncertainty / mixed / unclear |
| representation | probability, interval, distribution, confidence, qualitative |
| inherited_or_new | inherited / newly introduced |
| transfer_status | transferred / partial / explicitly omitted / unclear |
| representation_change | unchanged / transformed / unclear |
| magnitude_change | reduced / amplified / unchanged / incomparable / unassessed |
| decision_consequence | effect on quantity/pathway/environmental result |
| evidence_locator | source/section/table/model |
| candidate_mitigation | additional evidence/model/action |

## 5. Hotspot analysis

Do not target a single building-level uncertainty score.

Analyze hotspots as:

Material × Output variable × Digital Twin layer × Uncertainty source

Examples:
- Brick × reusable quantity × DT-L5 × quality/separability uncertainty;
- Concrete × release year × DT-L4 × demolition timing uncertainty;
- Steel × avoided impact × DT-L5 × substitution uncertainty.

## 6. Uncertainty contribution

If evidence and model structure allow, a decision output may later be decomposed into uncertainty contributions.

Example concept only:
Uncertainty in reusable brick quantity = stock quantity + quality/condition + separability + release timing + recovery assumptions.

Do not assign percentage contributions without a defensible sensitivity, variance or decomposition method.

## 7. Feedback mechanism

Decision output → dominant uncertainty → required evidence/model refinement → target DT layer → update → rerun downstream chain.

Examples:
- quantity uncertainty high → improve DT-L1/DT-L3 evidence;
- regional representativeness high → improve DT-L2;
- release-time uncertainty high → improve DT-L4;
- quality/reuse uncertainty high → targeted inspection or deconstruction evidence;
- substitution uncertainty high → improve DT-L5 process/scenario evidence.

## 8. Uncertainty-reduction rule

A Digital Twin capability should only be called uncertainty-reducing when:
1. the uncertainty source is identified;
2. the intervention targets that source;
3. evidence supports improvement;
4. the before/after uncertainty metric is comparable.

Otherwise describe the capability as improving traceability, context, representation, updating or decision transparency.