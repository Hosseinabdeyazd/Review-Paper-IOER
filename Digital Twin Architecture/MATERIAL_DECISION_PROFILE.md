# Material Decision Profile — Canonical Final Output

## Purpose

For a selected building, the Digital Twin must return **material/component-batch decision profiles**, not only a building-level score.

Each profile answers:

> What is this material, how much is there, where is it, what state is it in, when will it become available, what circular pathways are feasible, how much material is effectively retained/substituted, what environmental consequence follows, how uncertain is the result, and what evidence would improve it?

---

# 1. Building header

- Building ID and external IDs
- Location / parcel / administrative context
- Reference date
- Building use
- Construction year/period distribution
- Archetype/structural-system probabilities
- Geometry summary
- Evidence-tier summary
- Data completeness
- Latest update
- Selected scenario(s)
- Target year/horizon

---

# 2. Material inventory summary

Display building-wide totals, but preserve component/material batches underneath.

| Field | Output |
|---|---|
| material group/subgroup | material identity |
| components containing material | locations/functions |
| estimated stock | mass/volume/area/count |
| quantity uncertainty | distribution/range/confidence |
| evidence tier | E0–E5 |
| quality-state coverage | verified/inferred/missing |
| hazard status | known/risk/unknown |
| expected release windows | event/time |
| circularity data completeness | status |

---

# 3. Canonical MaterialBatch profile

## 3.1 Identity
- material_batch_id;
- material group;
- material subgroup/product;
- component/assembly/layer;
- storey/zone/location;
- product/standard/grade if known;
- manufacturer/passport ID if known;
- original/recycled/reused origin if known.

## 3.2 Quantity
- mass;
- volume;
- area/count where relevant;
- material intensity and source if inferred;
- density/conversion rule;
- quantity distribution;
- validation status.

## 3.3 Quality and condition
- condition grade;
- damage;
- retained function/performance;
- mechanical/physical properties where relevant;
- inspection/test status;
- certification/recertification state.

## 3.4 Hazards / contamination
- hazard flag;
- pollutant/contamination risks;
- evidence/test;
- handling restrictions;
- pathway exclusions.

## 3.5 Connection / separability
- connection type;
- reversibility;
- access;
- tools/effort;
- expected deconstruction damage;
- separability;
- purity/single-origin recovery potential.

## 3.6 Provenance and uncertainty
- primary evidence;
- secondary evidence;
- model/archetype;
- evidence tier;
- unresolved conflicts;
- uncertainty records;
- last update.

---

# 4. Release profile

For each MaterialBatch:

- event type;
- event ID;
- expected release time/year;
- release-time distribution;
- event probability;
- released mass distribution;
- retained mass;
- state/quality at release;
- event trigger;
- scenario;
- uncertainty.

Release events may include:
- repair;
- maintenance;
- replacement;
- renovation/refurbishment;
- change of use;
- partial demolition;
- full demolition.

This prevents the system from treating demolition as the only source of future material.

---

# 5. Recoverability cascade

Report separately:

1. released mass;
2. accessible mass;
3. removable/intact mass;
4. source-separated mass;
5. quality-accepted mass;
6. uncontaminated/eligible mass;
7. technically recoverable mass.

For each stage:
- fraction;
- mass;
- uncertainty;
- limiting factor.

---

# 6. Direct reuse profile

- technically reusable candidate mass;
- deconstruction damage loss;
- quality/test rejection;
- repair/refurbishment requirement;
- preparation-for-reuse yield;
- remaining service life;
- dimensional/functional match;
- structural-capacity match where relevant;
- certification status;
- demand match;
- temporal match;
- spatial/transport match;
- final reusable mass;
- environmental result;
- uncertainty;
- dominant constraint.

Distinguish:
**technical reuse potential** vs **realized/matched reuse potential**.

---

# 7. Closed-loop recycling profile

- feedstock mass;
- acceptance criteria;
- collection yield;
- sorting yield;
- processing technology;
- processing yield;
- output material/product;
- output quality;
- residue/loss;
- substitution ratio;
- effective virgin-material displacement;
- facility;
- route/distance;
- environmental burden;
- avoided burden/credit method;
- net result;
- uncertainty.

---

# 8. Open-loop recycling profile

- feedstock mass;
- alternative output/application;
- process;
- process yield;
- quality transformation;
- output grade;
- downcycling/upcycling classification where defined;
- replacement coefficient;
- displaced alternative product/material;
- functional-equivalence basis;
- facility/logistics;
- demand/market match;
- environmental result;
- uncertainty.

---

# 9. Other recovery/disposal profile

- energy recovery mass;
- backfill mass;
- other recovery;
- non-hazardous landfill mass;
- hazardous disposal mass;
- process residue;
- temporary storage/unmatched stock;
- treatment/disposal distance;
- environmental result;
- uncertainty.

---

# 10. Mass-balance panel

For every release event:

```text
Released mass
= reuse
+ preparation/remanufacture
+ closed-loop input
+ open-loop input
+ other material recovery
+ energy recovery
+ backfill
+ landfill
+ hazardous disposal
+ storage
+ unaccounted
```

Flag:
- double-counted mass;
- negative mass;
- excessive unaccounted mass;
- inconsistent process yields.

---

# 11. Environmental consequence panel

For each pathway × scenario:

## Method context
- functional unit;
- LCI method/database/version;
- geography/year;
- system boundary;
- allocation/recycling method;
- characterization method;
- modules included.

## Foreground burdens
- deconstruction;
- transport;
- cleaning/testing/repair;
- processing;
- storage;
- disposal.

## Benefits/credits
- avoided virgin production;
- effective substitution;
- Module D/other method-specific benefit.

## Indicators
At minimum where available:
- GWP/GHG;
- virgin-material/resource displacement;
- waste/disposal.

Advanced:
- energy;
- water;
- acidification;
- eutrophication;
- particulate matter;
- toxicity;
- land use;
- other LCIA indicators.

## Comparison
- baseline result;
- circular scenario result;
- difference;
- uncertainty;
- comparability status.

---

# 12. Uncertainty dashboard

## 12.1 Upstream sources
- geometry;
- construction age/use;
- archetype/structure;
- MCI/material quantity;
- density;
- renovation history.

## 12.2 State sources
- condition;
- quality;
- contamination;
- connection/separability.

## 12.3 Dynamic sources
- service life;
- replacement;
- renovation;
- demolition timing.

## 12.4 Circularity sources
- deconstruction damage;
- recovery;
- sorting/process yield;
- facility;
- demand;
- substitution.

## 12.5 Environmental sources
- LCI factor;
- transport;
- energy mix;
- system boundary;
- allocation/method.

For each source record:
- representation;
- inherited/new;
- transfer status;
- representation change;
- magnitude change if comparable;
- decision consequence.

---

# 13. Hotspot panel

Report separately:

### Impact hotspot
Material/process with greatest environmental contribution.

### Uncertainty hotspot
Parameter/source with greatest uncertainty contribution where quantifiable, or strongest qualitative uncertainty concern where not.

Never infer one from the other.

---

# 14. Decision robustness panel

For each pair/set of pathways:
- difference in central result;
- overlap in uncertainty;
- sensitivity to assumptions;
- scenario reversals;
- constraints causing infeasibility;
- confidence/robustness status.

No pathway is declared preferred without an explicit user decision objective and sufficient evidence.

---

# 15. Next-data recommendation

The final profile must identify:

- critical missing field;
- affected decision;
- relevant DT layer;
- candidate evidence action;
- expected benefit qualitatively or quantitatively where defensible.

Examples:
- retrieve BIM/plan;
- verify construction year;
- inspect wall build-up;
- sample material;
- test strength;
- hazardous-material test;
- inspect connections;
- confirm facility acceptance;
- confirm demand;
- replace generic LCI factor with regional data.

---

# 16. Building-level summary derived from material profiles

Only after material-level outputs exist may the system aggregate to building-level summaries:

- total stock by material;
- total expected releases by time;
- reuse potential;
- closed-loop potential;
- open-loop potential;
- total residual/landfill;
- effective virgin displacement;
- environmental scenarios;
- uncertainty;
- evidence completeness.

Aggregation must preserve the ability to drill down to the contributing material batches.

---

# 17. Example output skeleton — no empirical defaults

```text
BUILDING B-XXXX
Scenario: Renovation/Demolition in YYYY

MATERIAL BATCH: Brick / external wall / zone X

STOCK
Quantity: [distribution]
Evidence: [sources]
Quality: [state]
Hazards: [state]
Uncertainty: [...]

RELEASE
Event: [...]
Time: [distribution]
Released mass: [distribution]

RECOVERABILITY
Accessible: [...]
Intact removal: [...]
Separated/pure: [...]
Quality accepted: [...]
Technical recoverable: [...]

DIRECT REUSE
Technical mass: [...]
Matched mass: [...]
Constraints: [...]
Environmental result: [...]
Uncertainty: [...]

CLOSED LOOP
Process: [...]
Output: [...]
Yield: [...]
Substitution ratio: [...]
Effective substitution: [...]
Environmental result: [...]
Uncertainty: [...]

OPEN LOOP
Output/application: [...]
Replacement coefficient: [...]
Effective replacement: [...]
Environmental result: [...]
Uncertainty: [...]

RESIDUAL
Landfill: [...]
Hazardous: [...]
Other recovery: [...]

HOTSPOTS
Impact hotspot: [...]
Uncertainty hotspot: [...]

DECISION ROBUSTNESS
[...]

NEXT DATA ACTION
[...]
```

This is the canonical output contract for future code, database and UI development.
