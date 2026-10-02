# Material Decision Profile — Final Output Specification

## Purpose

This file defines the **target output** of the Digital Twin for a selected building.

The architecture should be considered incomplete unless it can eventually populate this profile with evidence-based values and uncertainty.

---

## 1. Building-level header

- Building ID
- Location / spatial unit
- Building use
- Construction period
- Geometry summary
- Current state / reference date
- Data completeness
- Overall provenance summary
- Last update
- Scenario horizon

---

## 2. Material inventory

One record per material or material-component combination.

| Field | Meaning |
|---|---|
| Material ID | persistent identifier |
| Material type | brick, concrete, steel, glass, timber, insulation, etc. |
| Component | wall, slab, roof, façade, window, etc. |
| Estimated quantity | mass / volume / area as relevant |
| Quantity uncertainty | range, distribution, confidence or other supported measure |
| Quality / condition | current condition or inferred quality |
| Quality uncertainty | uncertainty in material state |
| Source / method | observation, BIM, archetype, model, inspection |
| Evidence date | temporal validity |
| Spatial context | building / component / location |

---

## 3. Release profile

For each material:

- release event;
- expected release year / interval;
- release quantity;
- event probability;
- uncertainty in timing;
- uncertainty in released quantity.

Candidate events:
- construction waste;
- maintenance;
- component replacement;
- renovation;
- partial demolition;
- full demolition.

---

## 4. Circular pathway profile

For each material, evaluate relevant pathways independently.

### Direct reuse
- separability;
- retained quality;
- technical feasibility;
- reusable quantity;
- demand / market match;
- transport requirement;
- uncertainty.

### Closed-loop recycling
- recovery rate;
- processing loss;
- quality retention;
- substitution ratio;
- effective virgin-material substitution;
- uncertainty.

### Open-loop recycling
- alternative application;
- quality loss / transformation;
- replacement coefficient;
- market availability;
- effective substituted product/material;
- uncertainty.

### Recovery / disposal
- recovery pathway;
- residual disposal;
- treatment burden;
- uncertainty.

A building should not be assigned a single "open-loop" or "closed-loop" label. These are **material- and scenario-specific pathway choices**.

---

## 5. Environmental consequence profile

For each material × pathway × scenario:

- processing burden;
- transport burden;
- avoided virgin production;
- substitution credit where methodologically appropriate;
- disposal burden;
- GHG impact;
- energy/resource indicators where available;
- other impact categories where supported;
- uncertainty interval/distribution;
- reference/baseline scenario.

The profile should allow comparison such as:

```text
Baseline: demolition + disposal

vs.

Scenario A: direct reuse
Scenario B: closed-loop recycling
Scenario C: open-loop recycling
```

---

## 6. Decision profile

For each material:

- feasible pathways;
- infeasible / excluded pathways and reason;
- pathway-specific effective quantity;
- pathway-specific environmental consequence;
- uncertainty;
- robustness of comparison;
- critical missing information;
- recommended next observation / validation need, if decision uncertainty is high.

No pathway should be declared "best" unless an explicit decision rule and adequate evidence are available.

---

## 7. Uncertainty decomposition

The target profile should support material-specific uncertainty attribution where evidence permits.

Possible contributors:
- observation;
- building age / typology;
- component assignment;
- material intensity;
- material quantity;
- quality / condition;
- event timing;
- recovery rate;
- contamination;
- substitution / replacement;
- market assumptions;
- transport;
- LCI / LCIA;
- scenario choice.

The architecture should distinguish:
- quantified contribution;
- qualitative contribution;
- unknown / unassessed.

---

## 8. Example skeleton — no empirical numbers

```text
Building B-XXXX

Material: Brick

Stock
- quantity: [...]
- uncertainty: [...]

Release
- event: [...]
- expected time: [...]
- uncertainty: [...]

Pathway 1: Reuse
- feasible quantity: [...]
- quality constraint: [...]
- uncertainty: [...]
- environmental consequence: [...]

Pathway 2: Closed-loop recycling
- recovery rate: [...]
- substitution ratio: [...]
- effective substitution: [...]
- environmental consequence: [...]
- uncertainty: [...]

Pathway 3: Open-loop recycling
- destination: [...]
- replacement coefficient: [...]
- environmental consequence: [...]
- uncertainty: [...]

Dominant uncertainty source:
[...]

Additional data that would most improve the decision:
[...]
```

This skeleton is the central output contract for the architecture.
