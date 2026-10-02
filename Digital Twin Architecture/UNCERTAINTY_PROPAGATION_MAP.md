# Uncertainty Propagation Map

## Purpose

This file defines where uncertainty can enter the Digital Twin, how it propagates to final material-circularity/LCA decisions, and where additional information may be most valuable.

## 1. Canonical path

```text
Observation
   ↓
Building identity / geometry / age / use
   ↓
Structural system / archetype
   ↓
Component & assembly reconstruction
   ↓
Material type & material intensity
   ↓
Material quantity
   ↓
Material quality / condition
   ↓
Service life / renovation / demolition timing
   ↓
Released material quantity
   ↓
Separation / recovery / processing
   ↓
Reuse / recycling feasibility
   ↓
Substitution or replacement factor
   ↓
LCA coefficients + future scenario
   ↓
Environmental consequence
   ↓
Decision robustness
```

## 2. Candidate hotspots by stage

| Stage | Typical uncertainty source | Downstream consequence |
|---|---|---|
| Geometry | height, footprint, GFA, volume | stock-quantity bias |
| Age/use | missing/inferred attributes | wrong archetype / MI |
| Structure | probabilistic classification | wrong material composition |
| Assembly | hidden layers | material type/quantity error |
| Density | variable density | mass uncertainty |
| MI | poor sample representativeness | stock uncertainty |
| Quality | hidden damage/contamination | reuse feasibility uncertainty |
| Lifetime | service-life distribution | timing uncertainty |
| Renovation | event probability | material-flow uncertainty |
| Demolition | survival model | future availability uncertainty |
| Disassembly | connections/accessibility | recovered quantity uncertainty |
| Processing | yield/contamination loss | secondary-output uncertainty |
| Market | demand/acceptance | usable secondary quantity uncertainty |
| Substitution | functional equivalence | avoided virgin-material uncertainty |
| LCA | database/geography/time/allocation | environmental-benefit uncertainty |

These are hypotheses to test, not final rankings.

## 3. Traceability requirement

Each final result should retain a dependency path. Example:

```text
Net GHG benefit for reused brick
  ├─ released brick mass
  │    ├─ building GFA
  │    ├─ archetype probability
  │    └─ brick MI distribution
  ├─ reuse recovery rate
  │    ├─ condition
  │    ├─ connection/access
  │    └─ breakage
  ├─ transport
  │    ├─ receiving project
  │    └─ route
  └─ avoided-product coefficient
       ├─ LCI source
       ├─ geography
       └─ substitution assumption
```

## 4. Active uncertainty-reduction loop

If the final decision is not robust:

1. identify dominant uncertainty;
2. locate its upstream parameter;
3. identify possible new evidence;
4. estimate whether that evidence can change the decision;
5. acquire/update only high-value information;
6. rerun affected links;
7. compare decision robustness before/after update.

Examples:
- uncertain structure → archive/inspection;
- uncertain insulation thickness → survey/sample;
- uncertain material quality → inspection/testing;
- uncertain release year → refine lifetime/event model;
- uncertain recovery → deconstruction audit;
- uncertain substitution → destination/product-specific analysis;
- uncertain LCA → local/prospective LCI.

## 5. Rules

- variability is not automatically uncertainty;
- finer spatial resolution is not automatically lower uncertainty;
- added complexity can reveal or amplify uncertainty;
- missing reporting ≠ zero uncertainty;
- information loss ≠ uncertainty reduction;
- deterministic assignment from a probabilistic classifier can mask uncertainty;
- a circularity score without data-completeness information is insufficient;
- environmental benefit must be pathway-, time- and scenario-specific.
