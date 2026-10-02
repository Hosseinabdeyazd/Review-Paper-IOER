# Parameter Registry — Governance and Registration Rules

## Purpose

This file governs how parameters are added to the architecture.

The detailed field inventory is maintained in:
- `MASTER_PARAMETER_CATALOG.md`
- `schemas/BUILDING_MATERIAL_TWIN_TEMPLATE.yaml`

The architecture is intentionally extensive, but it must not become an uncontrolled collection of variables.

---

## 1. Registration rule

Every proposed parameter must be assigned:

1. **entity** — SiteContext / Building / Component / Assembly / MaterialBatch / Connection / Event / Flow / Process / Facility / Demand / Scenario / LCA / Decision;
2. **modelling role** — Observed / Inferred / Dynamic / Scenario;
3. **Digital Twin capability layer(s)** — DT-L1…DT-L5;
4. **analytical stream(s)** — S1…S5;
5. **downstream decision function** — identity / quantity / quality / timing / recoverability / pathway / substitution / LCA / robustness;
6. **evidence status** — source-supported / synthesis / proposed;
7. **requirement class** — CORE / COND / ADV / OPT;
8. **uncertainty representation**;
9. **provenance**;
10. **validation status**.

---

## 2. Requirement classes

### CORE
Required for the main Building-to-Material Decision workflow or required whenever the relevant entity exists.

### COND
Required only for particular material/component/pathway conditions.

### ADV
Can materially improve building-specific accuracy, uncertainty reduction, realism or decision usefulness.

### OPT
Useful context but not required for the core circular-material/environmental result.

Requirement level may change after further evidence review.

---

## 3. Evidence classes

### SRC — source-supported
Explicitly supported by reviewed literature, standards/guidelines or documented operational systems.

### SYN — synthesis
Derived by integrating evidence from multiple sources.

### PROP — proposed
Project architecture choice not directly established by one source.

No PROP parameter should later be presented as if it were a literature finding.

---

## 4. Mandatory metadata wrapper

Every populated parameter should support:

| Field | Meaning |
|---|---|
| parameter_id | stable parameter definition |
| value | value/category/geometry |
| unit | where applicable |
| value_type | observed / inferred / dynamic / scenario |
| entity_id | object to which value belongs |
| evidence_source_id | source |
| acquisition_method | GIS/BIM/record/image/test/model/etc. |
| source_version | dataset/model version |
| observation_time | collection/reference time |
| valid_from / valid_to | temporal validity where relevant |
| spatial_grain | component/building/region/etc. |
| spatial_coverage | geographic validity |
| regionalization_status | building/local/regional/national/generic |
| uncertainty_representation | confidence/range/SD/distribution/probability/qualitative |
| uncertainty_parameters | parameters if available |
| validation_status | validated/partial/unvalidated/unreported |
| validation_method | how checked |
| dependency_ids | upstream inputs |
| correlation_group | dependence group |
| model_id/version | when derived |
| evidence_tier | E0–E5 |
| data_completeness | completeness status |
| last_updated | versioning |

---

## 5. Entity classes

- SiteContext
- Building
- BuildingHistory
- Component
- Assembly
- MaterialLayer
- MaterialBatch
- Connection
- EvidenceItem
- Event
- MaterialFlow
- Process
- Facility
- Demand/ReceivingProject
- CircularityScenario
- LCAProfile
- EnvironmentalFactor
- ImpactResult
- DecisionResult
- UncertaintyRecord

---

## 6. Variable-role classes

### Observed
Directly measured/retrieved evidence.

### Inferred
Estimated via model/archetype/proxy.

### Dynamic
State variable that evolves in time.

### Scenario / decision
User/model assumption describing a possible future, not current physical truth.

A parameter can change role across contexts, but each stored value must have one explicit role.

---

## 7. Core functional filter

A parameter belongs in the **core** only when it contributes to at least one of:

- material identity;
- material quantity;
- material quality/condition;
- release timing;
- accessibility/separability/recovery;
- reuse/recycling feasibility;
- effective substitution/replacement;
- environmental consequence;
- uncertainty/decision robustness.

---

## 8. No-hidden-default rule

Any default must store:
- value;
- source;
- geography;
- time;
- material/component applicability;
- uncertainty;
- reason used;
- whether it is archetype/generic/scenario.

Examples that must never be hidden:
- density;
- MCI;
- service life;
- demolition rate;
- recycling rate;
- landfill fraction;
- processing yield;
- substitution ratio;
- transport distance;
- LCI factor.

---

## 9. Parameter-review workflow

```text
new literature / dataset
        ↓
candidate parameter
        ↓
map to existing entity/category
        ↓
is an existing parameter sufficient?
  yes → add evidence/allowed value/source
  no  → propose new parameter
        ↓
assign requirement + evidence status
        ↓
define uncertainty/provenance
        ↓
add to master catalog + YAML schema if accepted
```

---

## 10. Current master groups

1. universal metadata/provenance;
2. site/location/regional context;
3. building use/age/history;
4. geometry/morphology;
5. structural system;
6. component hierarchy;
7. assemblies/layers;
8. material identity/properties;
9. material quantity/stock;
10. quality/condition/hazards;
11. connections/disassembly/separability;
12. service life/events;
13. release/audit;
14. circular pathways;
15. processes/facilities/logistics;
16. demand/market matching;
17. LCA/environmental data;
18. user/scenario controls;
19. decision outputs;
20. uncertainty.

See `MASTER_PARAMETER_CATALOG.md` for detailed fields.
