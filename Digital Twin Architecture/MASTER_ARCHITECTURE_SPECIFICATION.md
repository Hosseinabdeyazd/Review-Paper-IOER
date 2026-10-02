# Master Architecture Specification — Building-to-Material Circularity Digital Twin

## Version
Working architecture v0.3 — literature-informed, output-driven, uncertainty-aware.

## 1. Mission

The system is not designed primarily to reproduce a building as a geometric digital object.

Its mission is:

> For any selected building, reconstruct the material inventory with explicit evidence and uncertainty, simulate when and how those materials leave the building, evaluate technically and contextually feasible circular pathways, propagate uncertainty into environmental consequences, and return a decision-ready material profile.

The final analytical unit is:

> **Material / component batch × building context × time × circularity pathway × environmental scenario.**

---

# 2. Architectural principles

## P1 — Output-driven
Architecture is designed backward from the final Material Decision Profile.

## P2 — Material-centric but building-context-aware
The building is the container/context; decisions are made at material/component-batch level.

## P3 — Nonlinear Digital Twin fabric
DT-L1–DT-L5 are capabilities, not a mandatory one-way software pipeline. Any layer may serve multiple S1–S5 streams and downstream decision needs can trigger upstream data acquisition.

## P4 — Evidence hierarchy
Archetype assumptions, GeoAI predictions, administrative records, BIM/plans and physical inspections are different evidence classes and must remain distinguishable.

## P5 — Uncertainty is first-class
A value without provenance, temporal/spatial validity and uncertainty status is incomplete.

## P6 — Circularity is pathway-specific
"Reusable", "recyclable", "open-loop" and "closed-loop" are not permanent building labels. They are conditional properties of a material/component under a scenario.

## P7 — Mass balance
All released material must be accounted for across reuse, recycling, recovery, processing losses, storage and disposal.

## P8 — Environmental benefit is not assumed
Circularity does not automatically imply lower impact. Each pathway requires an explicit environmental comparison against a defined baseline.

## P9 — Impact hotspot ≠ uncertainty hotspot
High environmental contribution and high uncertainty contribution are tracked separately.

## P10 — Context matters
Regionalization, spatialization, scale, facility availability, energy mix and market demand may change the decision.

---

# 3. System planes

The architecture is divided into four interacting planes.

```text
┌──────────────────────────────────────────────────────────────────────┐
│ A. EVIDENCE / KNOWLEDGE PLANE                                      │
│ Building ↔ Component ↔ Material ↔ Event ↔ Flow ↔ Facility ↔ Scenario│
└──────────────────────────────────────────────────────────────────────┘
          ↑             ↑                ↑                 ↑
          │             │                │                 │
┌──────────────────────────────────────────────────────────────────────┐
│ B. CAPABILITY PLANE — DT-L1 … DT-L5                                │
│ acquisition → integration → inference → dynamics → circular/LCA     │
└──────────────────────────────────────────────────────────────────────┘
          ↑             ↑                ↑                 ↑
┌──────────────────────────────────────────────────────────────────────┐
│ C. CONTROL PLANE                                                   │
│ ID | provenance | version | time | scale | uncertainty | validation │
└──────────────────────────────────────────────────────────────────────┘
          ↑                                                      ↓
┌──────────────────────────────────────────────────────────────────────┐
│ D. DECISION / INTERACTION PLANE                                    │
│ building selection | scenario constraints | output | feedback       │
└──────────────────────────────────────────────────────────────────────┘
```

---

# 4. Evidence / knowledge plane — canonical entity graph

## 4.1 SiteContext
Represents geographic and regulatory context.

Relationships:
- SiteContext CONTAINS Building
- SiteContext HAS regional material cadastre
- SiteContext HAS waste regulations
- SiteContext HAS energy mix
- SiteContext HAS facilities
- SiteContext HAS secondary-material demand

## 4.2 Building
Persistent object selected by the user.

Relationships:
- Building HAS Component
- Building HAS BuildingHistory
- Building HAS Observation
- Building HAS Event
- Building BELONGS_TO SiteContext
- Building HAS material-inventory version

## 4.3 Component
Physical construction entity: foundation, wall, slab, window, roof, etc.

Relationships:
- Component PART_OF Building
- Component HAS MaterialLayer / MaterialBatch
- Component CONNECTED_TO Component
- Component HAS installation/replacement history
- Component HAS condition
- Component HAS service-life model

## 4.4 Assembly
Ordered system of layers/components.

Example:
external wall =
structural backing → insulation → cavity → membrane → cladding → coating.

Relationships:
- Assembly HAS ordered MaterialLayer
- Assembly HAS Connection
- Assembly HAS geometry
- Assembly HAS separability state

## 4.5 MaterialBatch
Decision-relevant material object.

A batch should be split if:
- material type differs;
- component differs;
- installation age differs materially;
- condition/quality differs;
- contamination differs;
- removal pathway differs;
- location changes reuse feasibility.

Relationships:
- MaterialBatch LOCATED_IN Component
- MaterialBatch HAS quantity distribution
- MaterialBatch HAS quality state
- MaterialBatch HAS provenance
- MaterialBatch RELEASED_BY Event
- MaterialBatch ENTERS MaterialFlow

## 4.6 Connection
Interface between components/material layers.

Properties:
connection type, reversibility, access, tool, effort, damage, sequence dependency, purity after separation.

## 4.7 Event
Time-dependent building intervention.

Types:
maintenance, repair, replacement, renovation, retrofit, extension, change of use, partial demolition, full demolition.

Relationships:
- Event AFFECTS Component
- Event RELEASES MaterialBatch
- Event INSTALLS MaterialBatch
- Event HAS probability/time distribution

## 4.8 MaterialFlow
A mass/quantity flow from source to destination through a process.

Relationships:
Building/Event → Collection → Sorting → Facility/Process → OutputMaterial → Demand/Use → Disposal.

## 4.9 Process
Demolition, deconstruction, sorting, crushing, cleaning, testing, refurbishment, remanufacturing, recycling, disposal.

Properties:
input acceptance, yield, losses, energy, emissions, output quality.

## 4.10 Facility
Spatially explicit process location.

Properties:
technology, capacity, accepted materials, contamination thresholds, distance, availability.

## 4.11 Demand / ReceivingProject
Optional but critical for realized reuse.

Properties:
required material/product, quantity, quality, dimensions, location, time, certification.

## 4.12 CircularityScenario
User/model-defined possible future.

Properties:
target year, allowed pathways, technology assumptions, energy mix, transport limit, market assumptions, policy conditions.

## 4.13 LCAProfile
Defines environmental method and coefficients.

Relationships:
Material/Process/Transport/Disposal HAS EnvironmentalFactor
Scenario HAS LCA model
Pathway PRODUCES ImpactResult

## 4.14 ImpactResult
Material × pathway × scenario environmental result.

## 4.15 DecisionResult
Feasible pathways, tradeoffs, robustness, dominant uncertainty, next-data recommendation.

## 4.16 EvidenceItem
Raw/derived evidence object.

Examples:
image, LiDAR scan, BIM object, registry record, plan, inspection, lab test, archetype record.

## 4.17 UncertaintyRecord
Attached to any value/model/output.

---

# 5. Capability plane

## DT-L1 — Observation & Data Acquisition

### Mission
Acquire evidence needed to reduce ambiguity in material identity, quantity, state and timing.

### Input channels
- satellite/aerial imagery;
- street-view/façade imagery;
- LiDAR/point cloud;
- cadastral/building footprint;
- 3D city model;
- administrative registry;
- permits;
- construction/renovation records;
- BIM/IFC;
- drawings/specifications/BoQ;
- asset-management/maintenance records;
- pre-demolition audit;
- visual inspection;
- NDT / destructive tests;
- material samples;
- facility/market/context datasets.

### Processing
- detection;
- segmentation;
- geometry extraction;
- classification;
- document parsing;
- entity matching;
- quality control;
- observation confidence.

### Output contract
EvidenceItems, not unqualified "facts".

Each output has:
value + source + date + coverage + confidence/uncertainty + validation.

### Typical uncertainty
resolution, occlusion, measurement error, classification error, missing documents, outdated records, sampling error.

---

## DT-L2 — Identity, Integration & Context

### Mission
Keep all evidence and model outputs attached to the correct object, scale, place and time.

### Services
- Building ID management;
- component/material ID;
- entity resolution;
- spatial joins;
- temporal alignment;
- regionalization;
- spatialization;
- unit conversion;
- taxonomy mapping;
- raw-material / building-material / waste-code mapping;
- component taxonomy;
- MCI/context selection;
- provenance/version graph;
- scale-transition rules.

### Critical checks
- Is this MCI from the correct country/region?
- Is a generic LCI coefficient being used for a local process?
- Is the source dataset older than the renovation?
- Are building geometries from different dates?
- Did aggregation erase material/component distinctions?
- Are units and functional references consistent?

### Output contract
Context-qualified, identity-resolved values.

### Typical uncertainty
false entity match, regional representativeness, temporal mismatch, taxonomy ambiguity, scale mismatch.

---

## DT-L3 — Building State & Material Reconstruction

### Mission
Open the physical "black box" of the building.

### Stage 3A — Building/archetype inference
Uses:
age + use + region + geometry + structural clues + façade/roof/window clues + records.

Outputs:
probability distribution over archetypes/structural systems.

### Stage 3B — Component reconstruction
Outputs:
component inventory, geometry, assembly/layer hypotheses.

### Stage 3C — Material reconstruction
Outputs:
material types, product forms, densities, quantities and distributions.

### Stage 3D — State/quality reconstruction
Outputs:
condition, hazards, contamination, access, connections, separability and test status.

### Key implementation rule
Do not collapse a probability distribution to a single class prematurely.

Example:
P(structure=RC)=0.65,
P(masonry)=0.25,
P(steel)=0.10
should propagate into alternative material inventories if it materially affects results.

### Output contract
Probabilistic Material Inventory:
Building → Components → MaterialBatches → quantity × quality × evidence × uncertainty.

### Typical uncertainty
archetype transfer, hidden layers, unknown renovation, MCI variance, density, geometry conversion, material-class confusion, missing services/finishes.

---

## DT-L4 — Dynamics & Material-Flow Simulation

### Mission
Convert current stock into time-dependent material availability.

### Stage 4A — Component ageing
service-life and condition models.

### Stage 4B — Building events
maintenance, repair, replacement, renovation, change-of-use, demolition.

### Stage 4C — Release
for each event:
which batch, what quantity, at what time, in what state.

### Stage 4D — Stock-flow balance
existing stock + inflow − outflow = future stock.

### Stage 4E — scenario ensemble
multiple plausible futures rather than one deterministic demolition date.

### Output contract
Material Release Profile:
batch + event + time distribution + release quantity distribution + retained state.

### Typical uncertainty
lifetime distribution, functional obsolescence, redevelopment, policy, renovation choice, future technology.

---

## DT-L5 — Circularity, LCA & Decision Intelligence

### Mission
Convert release profiles into pathway-specific feasible quantities and environmental consequences.

### Stage 5A — Recoverability filter
released mass
→ accessible mass
→ separable mass
→ uncontaminated/acceptable mass
→ technically recoverable mass.

### Stage 5B — direct reuse
technical/quality/dimensional/structural/certification/demand matching.

### Stage 5C — recycling
collection → sorting → processing → output quality.

Separate:
- closed-loop;
- open-loop;
- downcycling/upcycling;
- other recovery.

### Stage 5D — substitution
output quantity × functional substitution/replacement factor.

### Stage 5E — logistics/demand
facility availability, distance, capacity, receiving demand and temporal match.

### Stage 5F — environmental accounting
demolition/deconstruction + transport + processing + disposal − avoided virgin production (according to stated LCA method).

### Stage 5G — robustness
compare scenario distributions, not only central estimates.

### Stage 5H — feedback
if decision is not robust:
identify uncertainty hotspot → request targeted evidence → update/re-run.

### Output contract
Material Decision Profile.

---

# 6. Cross-cutting control plane

## 6.1 Identity
Persistent IDs:
- building
- component
- assembly
- material batch
- event
- flow
- process/facility
- scenario
- evidence
- uncertainty record.

## 6.2 Provenance
Every derived value records:
raw inputs → transformations → model/version → output.

## 6.3 Versioning
The twin must preserve:
- state at t0;
- new evidence at t1;
- changed model at v2;
- scenario rerun;
- reason for value change.

## 6.4 Temporal validity
Distinguish:
- observation date;
- installation date;
- model reference year;
- scenario target year;
- service-life horizon;
- LCI reference year.

## 6.5 Spatial validity
Distinguish:
- object location;
- data spatial grain;
- data geographic validity;
- facility/demand location;
- regional factor.

## 6.6 Uncertainty
Every uncertain variable can store:
distribution/range/confidence/qualitative state.

## 6.7 Validation
Different validation targets:
- geometry;
- classification;
- material quantity;
- condition;
- service life;
- process yield;
- LCA coefficient.

## 6.8 Interoperability
Map external schemas to the canonical graph:
GIS / CityGML / BIM-IFC / material passport / DPP / LCI database / waste classification.

---

# 7. Data-evidence maturity ladder

## E0 — Prior only
Regional/national archetype or generic material factor.

## E1 — Geospatial building evidence
Footprint/height/roof/use/morphology/GeoAI prediction.

## E2 — Administrative evidence
construction age, use, permits, renovation history.

## E3 — Design/BIM/document evidence
component geometry, assembly, material/product specification.

## E4 — Inspection/audit/test evidence
verified material, quality, contamination, connection, mechanical properties.

## E5 — Dynamic asset evidence
maintenance/event history, state update, current operation/asset management.

For each output, report the evidence mix. Example:
brick quantity = 60% component geometry from BIM + 40% archetype material intensity is not the same evidential status as direct BoQ.

---

# 8. Inference hierarchy and evidence fusion

When multiple evidence sources exist:

1. retain each EvidenceItem;
2. evaluate temporal validity;
3. evaluate spatial/object specificity;
4. evaluate method/validation quality;
5. detect contradictions;
6. fuse evidence probabilistically or by explicit rule;
7. record posterior/updated uncertainty;
8. preserve the prior and update history.

Never silently overwrite an old value.

### Example
Regional prior:
wall = masonry probability 0.70

Street-image model:
brick façade probability 0.82

Plan:
structural wall = concrete

Result:
façade material and structural backing are represented separately; façade evidence must not overwrite structural material.

---

# 9. Material-batch creation rules

Create distinct MaterialBatch objects when any of the following differ:
- material type;
- product/form;
- component;
- location/storey;
- installation age;
- quality;
- contamination;
- connection/separation route;
- release event/time;
- circular destination.

This prevents a building-wide "steel" or "brick" total from hiding material that has different circular potential.

---

# 10. Stock-to-flow-to-decision equations — conceptual

## 10.1 Material stock
For component c and material m:

Q_stock(m,c) = geometry(c) × material share/intensity(m,c) × density/conversion

Inputs may be distributions.

## 10.2 Released mass
Q_release(m,c,t,s) = Q_stock × event fraction × event occurrence

## 10.3 Recoverable mass
Q_recoverable = Q_release × accessibility × separation yield × quality acceptance × contamination acceptance

The factors may be discrete rules or probabilistic quantities; do not assume multiplication if a source/model defines another dependency structure.

## 10.4 Pathway output
Q_output(pathway) = Q_recoverable × collection/sorting/process yield

## 10.5 Effective substitution
Q_substituted = Q_output × substitution or replacement coefficient

## 10.6 Net environmental consequence
Impact_net =
deconstruction + transport + processing + disposal
− avoided virgin production/other credit

The exact allocation and Module-D treatment depend on the LCA method and must be explicit.

---

# 11. Mass-balance engine

For each event and material:

Q_released =
Q_reuse
+ Q_closed_loop_input
+ Q_open_loop_input
+ Q_other_recovery
+ Q_landfill
+ Q_hazardous_disposal
+ Q_storage
+ Q_unaccounted

Processing chains then split input into product + residue/loss.

### Mandatory diagnostic
If unaccounted mass exceeds a defined tolerance, flag scenario invalid/incomplete.

Do not silently renormalize unless the rule is documented.

---

# 12. Circularity pathway decision tree

For each material batch:

### Step 1 — Is the batch physically accessible?
No → conventional demolition/mixed stream or unknown.

### Step 2 — Can it be separated without unacceptable damage?
No → recycling/downcycling/disposal routes.

### Step 3 — Is quality known and sufficient?
Unknown → request inspection/testing or retain uncertainty.

### Step 4 — Are hazardous/contaminating substances acceptable?
No → special treatment/disposal; possibly exclude reuse.

### Step 5 — Is component/product reuse technically feasible?
Check dimensions, remaining capacity, function, certification.

### Step 6 — Is there matching demand at the relevant time/place?
If yes → direct reuse scenario.
If no/unknown → storage/remanufacture/recycling scenarios.

### Step 7 — For recycling, which loop?
Closed-loop if output meets same/product-equivalent function under defined criteria.
Open-loop if output replaces a different product/material.
Downcycling if performance/value/function is materially lower.

### Step 8 — What is the actual substitution?
Do not equate recycling rate with virgin displacement.

### Step 9 — What is the environmental result?
Compare with baseline under identical functional basis.

---

# 13. User interaction model

## User selects
- building;
- reference date;
- target year/time horizon;
- intervention: renovate / partial demolition / demolition;
- allowed circular pathways;
- maximum transport radius;
- environmental objective(s);
- optional market/facility constraints;
- uncertainty/robustness threshold.

## System returns
### Building overview
evidence completeness and current state.

### Material inventory
material/component batches and quantities.

### Material timeline
when each batch is expected to become available.

### Circularity pathways
reuse, closed/open-loop, recovery, landfill.

### Environmental result
baseline vs scenarios.

### Uncertainty
confidence/distribution by output, dominant sources.

### Data action
which next evidence acquisition would most improve the decision.

---

# 14. S1–S5 interoperability

## S1 — GeoAI / observation
Feeds evidence and classifications into DT-L1/L3.

## S2 — material stock
Uses DT-L2 context and DT-L3 inference; produces stock.

## S3 — dynamics
Uses component/service-life/event model through DT-L4.

## S4 — circularity
Uses quality/connection/process/facility/demand data through DT-L5.

## S5 — LCA/decision
Uses full upstream flow and uncertainty through DT-L5.

Cross-links are allowed:
- S5 can request better S1 evidence;
- S4 can request DT-L3 quality inspection;
- S3 can update S2 through replacements;
- regional material cadastre can update priors for S2.

---

# 15. Uncertainty propagation architecture

## 15.1 Preserve upstream uncertainty
Classification outputs should remain probability vectors when feasible.

## 15.2 Transform explicitly
Example:
construction-period uncertainty
→ archetype mixture
→ material quantity distribution.

This is both transferred and representation-transformed.

## 15.3 Add downstream uncertainty
Example:
material quantity distribution
+ service-life distribution
+ deconstruction yield distribution.

## 15.4 Track dependencies
Do not assume independent factors when they share a cause:
age affects archetype, material, service life and pollutant risk.

## 15.5 Quantify only when valid
Possible methods:
- Monte Carlo;
- probabilistic graphical model;
- ensemble;
- global sensitivity/Sobol;
- interval analysis;
- scenario envelope.

Method choice depends on evidence structure.

## 15.6 Hotspot output
For each final output:
rank/identify uncertainty contributors only where analysis supports it.

---

# 16. Active information acquisition

When decision uncertainty exceeds threshold:

```text
Final decision uncertainty
        ↓
uncertainty decomposition
        ↓
dominant source
        ↓
candidate evidence actions
        ↓
expected information gain / feasibility
        ↓
targeted acquisition
        ↓
update twin
        ↓
rerun
```

Candidate actions:
- higher-resolution geometry;
- registry lookup;
- plan/BIM retrieval;
- façade/roof image;
- interior survey;
- opening-up inspection;
- material sampling;
- hazardous-material test;
- structural NDT;
- connection inspection;
- facility/process confirmation;
- market-demand confirmation.

**[PROP]** Later, value-of-information logic can prioritize which acquisition is worth doing.

---

# 17. Environmental architecture

Separate three concepts:

## 17.1 Circularity performance
How much mass/value/function stays in circulation?

## 17.2 Environmental performance
What are lifecycle environmental impacts?

## 17.3 Decision robustness
How stable is the scenario comparison under uncertainty?

A high recycling rate can still have poor environmental performance if processing/transport is intensive or substitution is weak. Therefore outputs stay separate.

---

# 18. Implementation-ready minimum viable core

The full schema is large. A minimum pilot needs:

### Building
ID, location, use, construction period, footprint, height, floors, GFA, structural system.

### Component
foundation, exterior wall, interior wall, slab/floor, roof, window/door at minimum.

### Material
type, component, quantity distribution, source, density/intensity, quality status.

### Dynamics
component age, service-life distribution, release event/time.

### Circularity
connection/separability, contamination, recovery yield, pathway, substitution/replacement.

### LCA
material/process factors, transport, disposal, avoided production, system boundary.

### Uncertainty
distribution/confidence/source for every non-certain input.

The full catalog remains available for expansion.

---

# 19. Architecture validation tests

A software/model implementation should not be accepted until it can pass:

1. **Identity test:** all material outputs trace to one building/component.
2. **Provenance test:** every quantity can be traced to evidence/model.
3. **Temporal test:** old and new evidence are distinguishable.
4. **Spatial test:** generic/regional/building-specific values are labelled.
5. **Mass balance test:** released material is fully accounted for.
6. **Uncertainty test:** uncertain inputs do not become false deterministic outputs.
7. **Scenario test:** physical evidence remains unchanged when user switches scenario.
8. **Circularity test:** reuse/open/closed-loop are batch/pathway specific.
9. **LCA test:** benefit is based on explicit baseline, functional equivalence and allocation.
10. **Feedback test:** a high-uncertainty decision can generate a targeted data request.
11. **Version test:** reruns are reproducible from model/data versions.
12. **No-hidden-default test:** every default coefficient is identifiable.

---

# 20. Architecture status

### Source-supported foundations
Material cadastres, MCI/age/use/region, component geometry, probabilistic stock-flow dynamics, material passports, quality/separability, service life, process chains, LCA and uncertainty are individually well supported.

### Our synthesis
Their integration into one material-centric Digital Twin fabric spanning S1–S5 is the project architecture.

### Not yet established
- universal material-specific reuse thresholds;
- universal substitution ratios;
- universal landfill/recycling rates;
- universal uncertainty-reduction effect of a Digital Twin.

These must remain material-, region-, technology-, time- and scenario-specific.
