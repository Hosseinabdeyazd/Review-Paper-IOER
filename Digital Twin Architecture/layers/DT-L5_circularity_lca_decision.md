# DT-L5 — Circularity, LCA & Decision Intelligence

## Status
Architecture v0.3 — detailed working specification.

## Mission
Turn material release profiles into **pathway-specific feasible quantities, substitution/replacement potential, environmental consequences and uncertainty-aware decision outputs**.

See also:
- ../CIRCULARITY_PATHWAY_ENGINE.md
- ../ENVIRONMENTAL_LCA_ENGINE.md
- ../MATERIAL_DECISION_PROFILE.md

---

## 1. User/scenario inputs

- target year;
- intervention;
- allowed pathways;
- reuse/closed-loop/open-loop permissions;
- max transport radius;
- facility assumptions;
- demand assumptions;
- future technology;
- future energy mix;
- regulatory context;
- quality threshold;
- environmental objectives;
- robustness/confidence threshold.

These do not overwrite physical building evidence.

---

## 2. Recoverability cascade

For each released batch:

```text
released
→ accessible
→ removable
→ separated
→ quality/hazard accepted
→ technically recoverable
```

Track loss and uncertainty at every stage.

---

## 3. Direct reuse module

Evaluate:
- intact removal;
- damage;
- condition/quality;
- remaining service life;
- dimensions;
- functional performance;
- structural capacity if relevant;
- certification;
- repair/refurbishment;
- demand match;
- timing;
- transport/storage.

Outputs:
- technical reuse potential;
- realized/matched reuse potential;
- environmental result.

---

## 4. Recycling module

### Closed-loop
- input acceptance;
- sorting;
- processing yield;
- output grade;
- quality retention;
- substitution ratio;
- displaced virgin material.

### Open-loop
- alternative product/application;
- process yield;
- output quality;
- replacement coefficient;
- displaced product/material.

Do not equate recycling rate, processing yield and substitution rate.

---

## 5. Residual pathways

- other recovery;
- energy recovery;
- backfilling;
- landfill;
- hazardous disposal;
- storage/unmatched stock.

All released mass must be balanced.

---

## 6. Facility/process selection

Evaluate:
- accepted materials;
- quality/contamination thresholds;
- technology;
- capacity/availability;
- output product;
- yield;
- energy/water/emissions;
- distance/transport.

Nearest facility is not automatically feasible.

---

## 7. Demand matching

For reuse/secondary products:
- demand material/product;
- quantity;
- quality;
- dimensions;
- certification;
- location;
- time window.

Separate:
technical recoverability ≠ actual circular uptake.

---

## 8. Environmental/LCA comparison

For each pathway:
- deconstruction burden;
- transport;
- cleaning/testing/repair;
- recycling/processing;
- storage;
- disposal;
- avoided production/substitution;
- net impact vs baseline;
- indicators and method;
- uncertainty.

Circularity is not assumed environmentally superior.

---

## 9. Material Decision Profile

Per batch output:
- stock quantity;
- quality/state;
- release event/time;
- direct reusable mass;
- closed-loop mass;
- open-loop mass;
- other recovery;
- landfill/residual;
- effective substitution;
- environmental consequences;
- uncertainty;
- robustness;
- dominant uncertainty;
- missing evidence;
- next-data recommendation.

---

## 10. Uncertainty decomposition

Potential sources:
- upstream quantity;
- quality;
- contamination;
- separability;
- deconstruction damage;
- recovery/process yield;
- facility;
- demand;
- substitution;
- transport;
- LCI;
- future scenario.

Report impact hotspot and uncertainty hotspot separately.

---

## 11. Feedback

If result is not robust:

```text
decision uncertainty
→ dominant source
→ target evidence/model
→ DT-L1/L2/L3/L4 update
→ rerun DT-L5
```

Examples:
- quality bottleneck → inspection/test;
- timing bottleneck → service-life/event model;
- regional factor bottleneck → DT-L2 regionalization;
- substitution bottleneck → process/product evidence;
- LCI bottleneck → higher-quality environmental factor.

---

## 12. Decision discipline

DT-L5 may compare and rank scenarios only when an explicit objective/rule is supplied.

Otherwise it reports:
- feasible alternatives;
- environmental and circularity results;
- uncertainty;
- trade-offs;
without inventing a preferred pathway.

---

## 13. Success criterion

For every material in a selected building, the system can answer:

**How much is there? When does it become available? What can realistically happen to it? What does that do to environmental burden? How uncertain is each answer, and what evidence would improve the decision most?**
