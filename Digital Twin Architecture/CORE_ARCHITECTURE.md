# Core Architecture — Building-to-Material Decision Twin

## 1. Design principle

The Digital Twin is designed **backward from the final decision output**.

The primary user action is:

> Select a building.

The primary system output is:

> A material-by-material decision profile describing quantities, release timing, feasible circular pathways, effective substitution potential, environmental consequences and associated uncertainty.

The Digital Twin therefore acts as a **Building-to-Material Decision Engine**, rather than only as a geometric or visual representation of a building.

---

## 2. Target workflow

```text
Selected Building
      ↓
DT-L1  Observation & Data Acquisition
      ↓
DT-L2  Identity, Integration & Context
      ↓
DT-L3  Building State & Material Reconstruction
      ↓
      Material inventory + uncertainty
      ↓
DT-L4  Dynamics & Material-Flow Simulation
      ↓
      Time-dependent release flows
      ↓
DT-L5  Circularity, LCA & Decision Intelligence
      ↓
      Material pathway scenarios + environmental consequences
      ↓
Decision-ready Material Profile
```

This diagram is intentionally simplified. In operation, feedback may move in both directions.

---

## 3. Five capability layers

### DT-L1 — Observation & Data Acquisition
Purpose: acquire evidence relevant to material inference and downstream decisions.

Candidate data:
- geometry;
- footprint;
- height / floors;
- construction period;
- use;
- façade / roof / openings;
- visible material clues;
- cadastral records;
- BIM / plans;
- LiDAR / imagery;
- renovation records;
- inspections / samples;
- contextual datasets.

Key question:
**What evidence do we have about the building and its context?**

### DT-L2 — Identity, Integration & Context
Purpose: connect heterogeneous data to persistent entities while preserving context.

Core capabilities:
- Building ID;
- Component / Material IDs where feasible;
- provenance;
- versioning;
- temporal validity;
- spatialization;
- regionalization;
- spatial grain / coverage;
- schema mapping;
- scale transition;
- source-target alignment.

Key question:
**Do all downstream models know which object, place, time, scale and source each value belongs to?**

### DT-L3 — Building State & Material Reconstruction
Purpose: open the building "black box".

Candidate outputs:
- building archetype;
- structural system;
- component assemblies;
- material types;
- material intensities;
- material quantities;
- material quality / condition;
- renovation state;
- component age;
- remaining service life;
- recoverable stock.

Key question:
**What materials are inside this building, in what quantities and condition, with what uncertainty?**

### DT-L4 — Dynamics & Material-Flow Simulation
Purpose: convert stocks into future release flows.

Processes:
- maintenance;
- replacement;
- refurbishment;
- partial demolition;
- demolition;
- lifetime / survival;
- release timing;
- future material flow;
- recovery timing;
- changing technologies / context.

Key question:
**When and through which event will each material become available?**

### DT-L5 — Circularity, LCA & Decision Intelligence
Purpose: evaluate material-specific pathways and environmental outcomes.

Pathways:
- direct reuse;
- closed-loop recycling;
- open-loop recycling;
- recovery;
- disposal.

Decision parameters:
- technical recoverability;
- separability;
- quality retention;
- contamination;
- recycling rate;
- reuse rate;
- substitution ratio;
- replacement coefficient;
- processing losses;
- market availability;
- transport;
- future demand;
- environmental impact.

Key question:
**What can be done with each released material, and what are the environmental consequences under uncertainty?**

---

## 4. Core entity graph

```text
BUILDING
  │
  ├── COMPONENT
  │      └── MATERIAL
  │             ├── quantity
  │             ├── quality
  │             ├── condition
  │             └── uncertainty
  │
  ├── EVENT
  │      ├── maintenance
  │      ├── replacement
  │      ├── renovation
  │      └── demolition
  │
  ├── MATERIAL FLOW
  │      ├── released quantity
  │      ├── timing
  │      └── destination
  │
  ├── PROCESS / FACILITY
  │
  ├── CIRCULARITY SCENARIO
  │      ├── reuse
  │      ├── closed-loop
  │      ├── open-loop
  │      └── disposal
  │
  ├── ENVIRONMENTAL IMPACT
  │
  └── DECISION
```

The final analytical unit is the **material in context**, not the building alone.

---

## 5. Four variable classes

### Observed
Directly measured or retrieved:
- footprint;
- height;
- coordinates;
- visible façade;
- number of floors;
- registry attributes.

### Inferred
Estimated from models, archetypes or proxies:
- construction period;
- archetype;
- structural system;
- material type;
- material intensity;
- hidden component composition.

### Dynamic
Changes through time:
- condition;
- remaining service life;
- renovation state;
- event probability;
- material release.

### Scenario / decision
Not fixed building properties:
- reuse / recycling pathway;
- open-loop vs closed-loop;
- recycling rate assumption;
- substitution ratio;
- market demand;
- transport limit;
- target year;
- optimization objective.

---

## 6. Uncertainty architecture

For every material and relevant parameter, distinguish:

1. uncertainty source;
2. inherited uncertainty;
3. transfer status;
4. representation change;
5. magnitude change where comparable;
6. downstream decision consequence.

Uncertainty fate labels remain:
- Preserved
- Legitimately reduced
- Amplified
- Transformed
- Masked / lost
- Unassessed

A material-level uncertainty path might be:

```text
Geometry uncertainty
   ↓
Archetype uncertainty
   ↓
Material-intensity uncertainty
   ↓
Material-quantity uncertainty
   ↓
Release-time uncertainty
   ↓
Quality / recovery uncertainty
   ↓
Substitution uncertainty
   ↓
LCA uncertainty
   ↓
Decision uncertainty
```

---

## 7. Feedback logic

The architecture is not purely forward.

Example:

```text
DT-L5 result:
Reuse vs recycling decision is not robust
        ↓
Dominant uncertainty:
Material quality
        ↓
Information request:
Inspection / material sample / renovation record
        ↓
DT-L1 / DT-L3 update
        ↓
DT-L4 / DT-L5 re-run
```

The Digital Twin should therefore support **targeted uncertainty reduction**, not indiscriminate data collection.

---

## 8. Scope filter for new parameters

A new parameter belongs in the core architecture only if it materially helps determine at least one of:

- material identity;
- material quantity;
- material quality / condition;
- material release timing;
- circular pathway feasibility;
- effective substitution / replacement;
- environmental consequence;
- uncertainty / decision robustness.

Parameters outside these functions may still be useful context, but should not automatically enter the core model.
