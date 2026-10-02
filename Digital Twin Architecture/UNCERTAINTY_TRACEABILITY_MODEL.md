# Uncertainty Traceability and Propagation Model

## 1. Objective

The Digital Twin must trace **where uncertainty enters, what object/parameter it belongs to, how it is transferred or transformed, and how it affects material-level circularity and environmental decisions**.

A final building/material result is incomplete if its uncertainty has been collapsed into one undocumented score.

---

# 2. Core distinction

For every uncertainty source keep separate:

1. **source/type** — what is uncertain and why;
2. **transfer** — whether it is carried downstream;
3. **representation change** — whether the uncertainty changes form;
4. **magnitude change** — whether comparable evidence shows increase/decrease;
5. **decision consequence** — whether it changes the material/circularity/LCA result.

"Preserved", "transformed" and "amplified/reduced" are not mutually exclusive concepts across these axes.

---

# 3. Variability versus uncertainty

Store explicitly:
- real variability;
- epistemic/data uncertainty;
- model/structural uncertainty;
- choice/scenario uncertainty;
- mixed/unclear.

Do not call real spatial/material heterogeneity an error.

Conversely, if heterogeneity is hidden through aggregation or generic coefficients, record the representational consequence.

---

# 4. Uncertainty families

## U1 — Observation
- measurement error;
- sensor/image resolution;
- occlusion;
- classification probability;
- missing records;
- geolocation;
- sample/test measurement.

## U2 — Identity / context / scale
- entity matching;
- taxonomy mapping;
- regional representativeness;
- temporal mismatch;
- source-to-target scale transition;
- aggregation/disaggregation;
- generic-to-building transfer.

## U3 — Building/material reconstruction
- archetype;
- structural-system classification;
- hidden assembly;
- MCI;
- density;
- geometry-to-mass conversion;
- renovation history;
- omitted material/component.

## U4 — Quality / condition / hazards
- damage assessment;
- strength/performance;
- contamination;
- hazardous substances;
- retained quality;
- connection/separability.

## U5 — Dynamics
- component service life;
- remaining service life;
- renovation event;
- demolition timing;
- replacement cycle;
- future condition.

## U6 — Deconstruction/recovery process
- accessibility;
- removal damage;
- collection;
- separation;
- sorting;
- process yield;
- output quality.

## U7 — Circularity scenario
- direct reuse eligibility;
- open/closed-loop route;
- facility availability/capacity;
- demand;
- regulation;
- storage;
- future technology.

## U8 — Substitution
- functional equivalence;
- substitution ratio;
- replacement coefficient;
- displaced product/material.

## U9 — Environmental / LCA
- foreground quantities;
- background coefficients;
- database geography/year;
- LCI method;
- system boundary/truncation;
- allocation;
- characterization;
- future energy/process mix.

## U10 — Decision
- objective/weights;
- constraint choice;
- scenario set;
- robustness threshold.

---

# 5. Uncertainty record

| Field | Description |
|---|---|
| uncertainty_source_id | unique record |
| target_entity_id | object affected |
| target_parameter | parameter |
| material/component | context |
| origin_layer | DT-L1…DT-L5 |
| affected_streams | S1…S5 |
| source_type_original | source terminology |
| source_type_harmonized | project taxonomy |
| variability_or_uncertainty | variability/uncertainty/mixed/unclear |
| causal_description | mechanism |
| representation | probability/range/SD/distribution/confidence/qualitative |
| parameters | numerical parameters |
| inherited_or_new | inherited/new |
| dependency_ids | upstream variables |
| correlation_group | dependence |
| transfer_status | transferred/partial/omitted/unclear |
| representation_change | unchanged/transformed/unclear |
| magnitude_change | reduced/amplified/unchanged/incomparable/unassessed |
| comparison_basis | metric/before-after basis |
| decision_consequence | output affected |
| evidence_locator | source/model/table/test |
| candidate_mitigation | possible evidence/model action |
| mitigation_evidence | source supporting effect |
| validation_status | status |

---

# 6. Dependency graph

Uncertainty propagation must follow a dependency graph, not an independent list.

Example:

```text
Construction age
 ├── archetype
 ├── structural system
 ├── material composition
 ├── pollutant risk
 └── remaining service life

Geometry
 ├── component areas
 └── material quantity

Material quantity
 ├── release quantity
 ├── recoverable quantity
 └── LCA foreground

Quality
 ├── reuse eligibility
 ├── process route
 ├── substitution
 └── environmental benefit
```

A shared cause must not be sampled as independent uncertainty multiple times.

---

# 7. Representation by variable type

## Categorical inference
Store probability vector where possible.

Example:
`P(structure={RC:0.6, masonry:0.3, steel:0.1})`.

## Continuous measurement
Store measurement distribution/range/precision.

## Archetype/MCI
Store empirical distribution or uncertainty around the coefficient where available.

## Service life/event time
Store survival/lifetime distribution or scenario envelope.

## Process yield
Store process-specific distribution/range.

## Scenario choice
Treat as scenario branch unless a probability is defensibly available.

## Qualitative unknown
Use explicit unknown/low-evidence status; do not invent a numeric distribution solely to make Monte Carlo possible.

---

# 8. Propagation methods

Method selection depends on evidence.

### Monte Carlo
Appropriate when probabilistic inputs and dependencies are defensible.

### Ensemble / scenario branching
Appropriate for model/choice uncertainty and alternative archetypes/pathways.

### Global sensitivity analysis
Appropriate for attribution of output variance to inputs when model structure supports it.

### Interval / bound analysis
Appropriate when only defensible bounds are available.

### Qualitative traceability
Appropriate when numerical uncertainty cannot be justified.

The architecture allows mixed representations.

---

# 9. Evidence fusion and updating

For a parameter with multiple evidence items:

1. preserve prior;
2. evaluate object/spatial/temporal match;
3. evaluate source quality;
4. identify conflict;
5. update/fuse using explicit rule/model;
6. create new value/version;
7. record posterior/updated uncertainty;
8. retain transformation provenance.

Example:
regional archetype prior → GeoAI evidence → BIM/plan → inspection/test.

**Do not assume that a more detailed source automatically dominates if it is old, unvalidated or mismatched.**

---

# 10. Scale-transition uncertainty

For every change of grain:
- source grain;
- target grain;
- aggregation/disaggregation method;
- spatial heterogeneity;
- information loss;
- uncertainty before/after if comparable.

Examples:
- regional MCI → building;
- component materials → building totals;
- building release → neighborhood supply;
- regional LCI → local process.

Information loss and uncertainty reduction are different concepts.

---

# 11. Material-level uncertainty chain

```text
Observation
  ↓
Building/use/age/structure inference
  ↓
Component/assembly reconstruction
  ↓
Material type/intensity/quantity
  ↓
Quality/condition/hazard
  ↓
Service life / release event
  ↓
Deconstruction / separation / recovery
  ↓
Circular pathway / facility / demand
  ↓
Substitution / replacement
  ↓
LCA
  ↓
Decision robustness
```

At every arrow record:
- inherited uncertainty;
- new uncertainty;
- representation change;
- lost/masked information.

---

# 12. Hotspot architecture

Analyze at:

> Building/context × MaterialBatch × Output variable × DT layer × Uncertainty source.

Possible outputs:
- quantity hotspot;
- release-time hotspot;
- reuse hotspot;
- substitution hotspot;
- environmental hotspot;
- decision hotspot.

Do not target a single building uncertainty score as the main scientific output.

---

# 13. Impact hotspot versus uncertainty hotspot

Track independently.

Example logic supported by LCA uncertainty literature:
- material A may dominate GWP;
- material B may dominate uncertainty in GWP.

The system should display both.

---

# 14. Decision robustness

For scenario comparison record:
- central difference;
- output distributions/intervals;
- overlap;
- probability of scenario ordering if method supports it;
- sensitivity to model choice;
- scenario reversals;
- unassessed uncertainty.

Robustness is stronger than simply reporting a smaller mean impact.

---

# 15. Targeted uncertainty reduction

A capability is called **uncertainty-reducing** only when:

1. source identified;
2. intervention targets that source;
3. before/after uncertainty uses comparable metric;
4. evidence/model supports the change.

Otherwise describe benefit as:
- improved traceability;
- improved specificity;
- improved validation;
- improved context;
- reduced data gap;
- better representation.

---

# 16. Active data acquisition / value-of-information concept

When decision uncertainty is high:

```text
decision output
→ uncertainty decomposition
→ candidate dominant sources
→ possible evidence actions
→ expected uncertainty/decision benefit
→ acquisition cost/feasibility
→ select next action
→ update twin
→ rerun
```

Candidate actions:
- geometry scan;
- archive/permit lookup;
- BIM retrieval;
- wall opening;
- material sample;
- hazard test;
- structural NDT;
- connection inspection;
- facility confirmation;
- demand confirmation;
- regional LCI update.

This value-of-information prioritization is **[PROP]** until a formal method is selected.

---

# 17. Hotspot register rules

1. High variability ≠ high uncertainty.
2. High impact ≠ high uncertainty contribution.
3. Missing reporting ≠ zero uncertainty.
4. Finer scale ≠ automatically more accurate.
5. Aggregation can transform/mask information.
6. "Reduced" requires comparable evidence.
7. Material-specific and pathway-specific uncertainty should not be collapsed prematurely.
8. Unassessed uncertainty remains visible.

---

# 18. Output contract

Every Material Decision Profile must include:
- uncertainty representation for stock;
- release-time/quantity uncertainty;
- pathway uncertainty;
- environmental-result uncertainty;
- dominant source(s) if defensible;
- unassessed sources;
- evidence tier;
- recommended next-data action.
