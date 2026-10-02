# DT-L3 — Building State & Material Reconstruction

## Status
Architecture v0.3 — detailed working specification.

## Mission
Convert heterogeneous evidence into a **probabilistic component- and material-level representation** of the selected building.

---

## 1. Inference hierarchy

### 1A Building state
Infer/confirm:
- use/type;
- construction period;
- archetype;
- structural system;
- renovation state;
- geometry/morphology.

### 1B Component inventory
Reconstruct:
- foundation/substructure;
- frame/load-bearing structure;
- floors/slabs;
- exterior walls/façade;
- interior walls;
- ceilings;
- roof;
- windows;
- doors;
- stairs;
- finishes;
- insulation;
- MEP where data/scope support it.

### 1C Assembly/layer structure
Represent ordered layers:
e.g. exterior wall backing + insulation + cavity + membrane + cladding + finish.

### 1D Material batches
Create material objects by component/location/age/state rather than only building-wide totals.

### 1E Condition/quality/hazard state
Attach:
- quality/condition;
- damage;
- contamination;
- hazardous substances;
- certification/test status;
- connection/access/separability.

---

## 2. Principal predictors/evidence

- construction year/period;
- use/function;
- region;
- structural system;
- footprint;
- perimeter/area ratio;
- height;
- floors;
- volume/GFA;
- roof type;
- façade type;
- WWR;
- visible materials;
- renovation history;
- BIM/plans;
- local/regional MCI.

---

## 3. Archetype/MCI logic

When direct quantity is unavailable:

```text
Building evidence
→ archetype probability
→ component/material composition prior
→ building-specific geometry scaling
→ density/conversion
→ material quantity distribution
```

Required MCI metadata:
- source;
- region;
- building type;
- age class;
- component scope;
- unit;
- sample size/method if known;
- distribution/variance;
- transferability status.

A transferred MCI is never labelled building-specific.

---

## 4. Geometry-to-material logic

Examples:
- wall area × layer thickness × density;
- slab area × thickness × density;
- roof area × assembly intensity;
- window area × frame/glass composition;
- component count × unit mass;
- GFA/volume × MCI.

For each calculated quantity preserve:
- geometry source;
- composition source;
- conversion rule;
- density source;
- uncertainty dependencies.

---

## 5. Probability preservation

If input class is uncertain, preserve mixture.

Example:
- RC structure 0.60;
- masonry 0.30;
- steel 0.10.

Generate conditional material inventories or propagate a mixture instead of forcing RC=100% unless a later evidence item resolves the class.

---

## 6. Quality state

For each reusable/recyclable material/component capture where relevant:
- condition grade;
- remaining function;
- cracks/spalling/corrosion/rot/deformation;
- moisture/fire/chemical exposure;
- coating/treatment;
- structural strength/grade;
- test status;
- contamination;
- hazard risk;
- recertification need.

---

## 7. Connection/separability state

- connection type;
- reversibility;
- accessibility;
- tool/effort;
- expected damage;
- sequence dependencies;
- mono-material separation;
- attachments;
- purity potential.

This information belongs in DT-L3 current state, even though it is consumed heavily by S4/DT-L5.

---

## 8. Output — Probabilistic Material Inventory

For each MaterialBatch:
- material identity;
- component/location;
- quantity distribution;
- physical properties;
- installation age;
- quality/condition;
- hazards;
- connection/separability;
- service-life information;
- evidence tier;
- provenance;
- uncertainty.

---

## 9. Validation

Possible validation:
- compare inferred geometry with BIM/scan;
- compare material inventory with BoQ;
- inspect sampled components;
- pre-demolition audit;
- mass balance;
- cross-source consistency.

Store validation residuals rather than only pass/fail.

---

## 10. Main uncertainty sources

- archetype classification;
- MCI variability;
- region transfer;
- hidden layers;
- unknown renovation;
- wrong structural-system inference;
- geometry conversion;
- density;
- material-class confusion;
- omitted non-structural/MEP materials;
- quality/hazard inference.

---

## 11. Success criterion

DT-L3 must produce a material inventory detailed enough that DT-L4 can model **when each batch is released** and DT-L5 can evaluate **what can be done with that batch**.
