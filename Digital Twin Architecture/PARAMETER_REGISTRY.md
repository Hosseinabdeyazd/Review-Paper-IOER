# Parameter Registry

## Purpose

This registry prevents the architecture from becoming an uncontrolled list of inputs.

Every parameter should be assigned to:
1. an entity;
2. a modelling role;
3. one or more Digital Twin layers;
4. one or more S1–S5 streams;
5. a downstream material-decision function.

---

## 1. Entity classes

- Building
- Component
- Material
- Event
- Material Flow
- Process / Facility
- Scenario
- Environmental Impact
- Decision

---

## 2. Modelling-role classes

- Observed
- Inferred
- Dynamic
- Scenario / decision

---

## 3. Mandatory parameter metadata

Where applicable, every parameter record should include:

| Field | Description |
|---|---|
| parameter_id | stable identifier |
| entity_type | Building / Material / Event / etc. |
| parameter_name | clear name |
| modelling_role | Observed / Inferred / Dynamic / Scenario |
| value_type | scalar / category / interval / distribution / probability |
| unit | unit if applicable |
| source | data/model source |
| provenance | method / dataset / version |
| spatial_grain | building / component / district / region etc. |
| spatial_coverage | geographic validity |
| temporal_reference | date / period / target year |
| uncertainty_type | as reported / harmonized |
| uncertainty_representation | confidence / SD / range / distribution / unknown |
| validation_status | validated / partially validated / unvalidated / unreported |
| DT_layer | one or more DT-L1–DT-L5 |
| S_stream | one or more S1–S5 |
| downstream_use | quantity / quality / timing / pathway / substitution / LCA |
| evidence_status | source-supported / synthesis / proposed |

---

## 4. Initial parameter families

### Building
- footprint
- height
- floor count
- use
- construction period
- building age
- typology
- structural system
- renovation history
- current condition

### Component
- component type
- geometry
- assembly
- installation date
- replacement history
- separability
- accessibility

### Material
- material type
- quantity
- density
- intensity
- quality
- condition
- contamination
- embodied impact factor
- recyclability
- reusability

### Event
- event type
- event timing
- probability
- affected component/material
- released quantity

### Material Flow
- source
- destination
- quantity
- time
- transport distance
- processing route
- loss rate

### Process / Facility
- process type
- capacity
- distance
- recovery efficiency
- energy input
- output quality

### Scenario
- target year
- pathway
- open-loop / closed-loop
- reuse enabled?
- recycling enabled?
- recovery enabled?
- transport constraint
- demand assumption
- market assumption
- substitution ratio
- replacement coefficient
- optimization objective

### Environmental Impact
- functional unit
- system boundary
- LCI source
- LCIA method
- impact category
- baseline burden
- avoided burden
- scenario burden

### Decision
- decision objective
- feasible pathways
- robustness
- dominant uncertainty
- additional information need

---

## 5. Scope test

Before adding any parameter, ask:

**Does this parameter improve our ability to estimate material quantity, quality, release timing, circular pathway feasibility, effective substitution, environmental consequence or uncertainty?**

If not, it should not automatically enter the core architecture.
