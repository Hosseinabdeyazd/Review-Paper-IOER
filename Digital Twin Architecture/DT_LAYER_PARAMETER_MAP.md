
# DT Layer × Parameter × S1–S5 Architecture Map

## Purpose

This file turns the parameter schema into an operating architecture.

The Digital Twin layers are capability layers. S1–S5 are analytical streams. A variable may enter in one Digital Twin layer, be transformed in another, and support several S streams.

---

# Cross-cutting control plane

The following fields travel with relevant data through every layer:

- persistent entity ID;
- provenance;
- source/version;
- time/reference period;
- spatial grain;
- geographic validity;
- unit;
- uncertainty representation;
- validation status;
- evidence status;
- model version.

The control plane prevents data from becoming detached from context as it moves between models.

---

# DT-L1 — Observation & Data Acquisition

## Primary question

What can be observed, measured, retrieved, inspected, or tested about this building/material/context?

## Main parameter domains

### Building/site
- Building ID/address/parcel/location
- footprint
- perimeter
- height
- floors
- GFA/volume
- orientation
- roof form
- openings

### Visible envelope
- facade/cladding
- visible wall material
- windows
- doors
- roof cover
- visible condition

### Documentary
- age/construction year
- use
- structural drawings
- BIM
- renovation history
- permits
- maintenance

### On-site/material
- internal components
- material identity
- dimensions
- connections
- condition
- contamination
- mechanical/material tests

### Context
- facility locations
- transport network
- landfills
- regional energy mix
- market/demand

## Processing
- acquisition;
- segmentation;
- object detection;
- image classification;
- point-cloud processing;
- record extraction;
- survey;
- sampling/testing.

## Outputs to other layers
- observed geometry;
- observed building descriptors;
- observed component/material clues;
- verified document attributes;
- test results;
- observation coverage;
- validation/confidence.

## S-stream connections
- S1: core
- S2: material/geometry evidence
- S3: event/history evidence
- S4: condition/facility/market evidence
- S5: regional/LCA input evidence

## Main uncertainty sources
- measurement error;
- occlusion;
- missing surfaces;
- resolution;
- outdated records;
- missing documents;
- classification error;
- sampling error;
- temporal mismatch.

## Candidate refinement mechanisms
- combine sensors;
- combine drive-by/fly-by/indoor;
- retrieve documents;
- targeted inspection;
- targeted sampling;
- validate classifications.

---

# DT-L2 — Identity, Integration & Context

## Primary question

Do all observations and model values refer to the correct object, place, time, scale, and semantic meaning?

## Main parameter domains

### Identity
- Building ID
- component ID
- material ID
- product ID
- event ID
- facility ID
- scenario ID
- LCA dataset ID

### Spatial context
- coordinates
- polygon
- spatial grain
- regionalization
- spatialization
- source/target scale
- geographic validity

### Temporal context
- observation date
- installation date
- event date
- dataset year
- validity period
- target year

### Semantic integration
- units
- material taxonomy
- component taxonomy
- use taxonomy
- construction typology
- LCA category mapping
- schema mapping

### Provenance/versioning
- source
- source version
- model version
- last update
- evidence status

## Processing
- entity resolution;
- geospatial joining;
- schema matching;
- unit conversion;
- regionalization;
- spatialization;
- temporal alignment;
- aggregation/disaggregation;
- dataset version management.

## Outputs
- integrated object graph;
- contextualized parameters;
- validated unit mappings;
- traceable data lineage;
- scale-transition metadata.

## S-stream connections
- S1–S5: all strong

## Main uncertainty sources
- entity mismatch;
- semantic mismatch;
- unit conversion;
- regional mismatch;
- temporal mismatch;
- scale mismatch;
- aggregation information loss;
- version conflict.

## Candidate refinement mechanisms
- persistent IDs;
- controlled vocabularies;
- explicit mappings;
- building/component/material ontology;
- regional validity checks;
- time/version checks;
- uncertainty-preserving aggregation.

---

# DT-L3 — Building State & Material Reconstruction

## Primary question

What is inside the building, in what quantity and condition, given observed evidence and uncertainty?

## Main parameter domains

### Typology/archetype
- construction period
- use
- built form
- structural system
- regional typology

### Geometry-to-component model
- walls
- floors
- slabs
- beams
- columns
- roof
- windows
- doors
- partitions
- MEP

### Component-to-material model
- layer assemblies
- material types
- thicknesses
- densities
- reinforcement
- finishes
- insulation
- connectors

### Material stock
- material quantity
- component quantity
- MI
- quantity distributions
- mass/volume/area/count

### Quality/state
- condition
- damage
- contamination
- residual service life
- certification
- separability clues

## Processing
- archetype classification;
- probabilistic structural-system inference;
- component reconstruction;
- material-intensity assignment;
- geometric quantity take-off;
- density/unit conversion;
- Bayesian/data fusion where applicable;
- condition inference;
- material-passport assembly.

## Outputs
- building-specific bill of materials;
- component inventory;
- material quantity distributions;
- quality/condition state;
- hidden-state uncertainty.

## S-stream connections
- S1: consumes observation
- S2: core
- S3: provides initial stock/state
- S4: provides quality/recoverability state
- S5: provides material quantities

## Main uncertainty sources
- archetype;
- structure classification;
- hidden layers;
- MI transferability;
- reference buildings;
- component geometry;
- density;
- material identity;
- condition;
- contamination;
- renovation history.

## Candidate refinement mechanisms
- building-specific documentation;
- component geometry;
- local/regional MI;
- probabilistic MI rather than point values;
- targeted inspection;
- material testing;
- model calibration;
- uncertainty-aware fusion.

---

# DT-L4 — Dynamics & Material-Flow Simulation

## Primary question

When, where, and in what condition will each material/component leave its current in-use state?

## Main parameter domains

### Lifetimes
- building lifetime
- structural life
- facade life
- window life
- interior life
- MEP life

### Events
- maintenance
- repair
- replacement
- renovation
- adaptive reuse
- use change
- demolition

### Flow
- affected fraction
- release quantity
- release timing
- replacement input
- stock survival
- cohort state

### Dynamic context
- future energy mix
- technology
- regulation
- construction/demolition activity
- demand

## Processing
- survival models;
- cohort models;
- dynamic MFA;
- event simulation;
- conditional renovation;
- replacement-cycle modelling;
- scenario ensembles.

## Outputs
- time-dependent stock;
- material release distributions;
- renovation/replacement flows;
- demolition flows;
- future availability windows.

## S-stream connections
- S2: starts from stock
- S3: core
- S4: supplies release flows
- S5: supplies time-specific quantities/scenarios

## Main uncertainty sources
- lifetime distribution;
- renovation timing;
- demolition timing;
- event probability;
- future scenario;
- dependence between survival and renovation;
- future material quality.

## Candidate refinement mechanisms
- local demolition/renovation records;
- component-specific lifetimes;
- conditional models;
- dynamic calibration to observed stock;
- scenario ensembles;
- time-varying MI and process data.

---

# DT-L5 — Circularity, LCA & Decision Intelligence

## Primary question

For each released material/component, what pathways are feasible, how much primary resource can actually be displaced, what are the environmental consequences, and how robust is the decision?

## Circularity inputs
- released quantity/time;
- quality;
- contamination;
- separability;
- salvage yield;
- facility;
- process yield;
- demand;
- transport;
- storage;
- regulation.

## Pathways
- direct reuse;
- repair/refurbishment;
- remanufacturing;
- closed-loop recycling;
- open-loop recycling;
- energy recovery;
- landfill.

## Substitution
- substitution ratio;
- replacement coefficient;
- receiving product/material;
- demand matching;
- quality matching.

## LCA
- material coefficients;
- C1-C4 burdens;
- D1 potential;
- transport;
- processing;
- avoided primary production;
- avoided disposal;
- time/region-specific energy mix.

## Decision
- objectives;
- risk tolerance;
- pathway constraints;
- transport threshold;
- quality threshold;
- target year;
- robustness.

## Processing
- mass balance;
- pathway allocation;
- supply-demand matching;
- network-distance calculation;
- substitution calculation;
- LCA;
- uncertainty propagation;
- sensitivity/hotspot analysis;
- multi-scenario comparison.

## Outputs
- material decision profile;
- pathway quantities;
- landfill fraction;
- effective substitution;
- environmental impact distributions;
- uncertainty contributions;
- decision robustness;
- recommended next observation.

## S-stream connections
- S3: uses timing
- S4: core
- S5: core
- S1/S2: feedback when more evidence needed

## Main uncertainty sources
- salvage/recovery;
- quality;
- contamination;
- process yield;
- demand;
- facility capacity;
- substitution;
- LCA data;
- future energy/process;
- user scenario.

## Candidate refinement mechanisms
- pre-demolition audit;
- quality testing;
- facility-specific data;
- real market demand;
- regional LCA;
- product-specific EPD;
- value-of-information feedback.

---

# Layer-to-output dependency matrix

| Final output | DT-L1 | DT-L2 | DT-L3 | DT-L4 | DT-L5 |
|---|---|---|---|---|---|
| Material identity | evidence | linkage | core inference | preserve | use |
| Material quantity | geometry/data | units/context | core | evolve/release | use |
| Material quality | inspect | provenance | reconstruct | evolve | gate |
| Release time | history | temporal link | initial state | core | use |
| Reusable quantity | inspect | object link | condition | release | core |
| Closed-loop quantity | facility data | spatial link | material state | release | core |
| Open-loop quantity | facility/market | spatial link | material state | release | core |
| Landfill fraction | waste data | context | — | release | core |
| Environmental impact | LCI input | regional/time match | quantity | timing | core |
| Uncertainty hotspot | source metrics | context uncertainty | inference uncertainty | dynamic uncertainty | integrated |
| Next best data request | acquire | route request | identify need | identify need | trigger |

---

# Parameter-to-S1–S5 examples

## Construction year
Observed/inferred in DT-L1/L3.
Supports:
- S1 classification;
- S2 archetype/MI;
- S3 lifetime;
- S4 condition/reuse;
- S5 replacement/LCA.

## Structural system
Observed/inferred in DT-L3.
Supports:
- S2 material quantities;
- S3 structural lifetime;
- S4 disassembly/reuse;
- S5 material/environmental inventory.

## External wall system
Observed/inferred in DT-L1/L3.
Supports:
- S2 material stock;
- S3 replacement/renovation;
- S4 separability/recycling;
- S5 impacts.

## Window type
Observed in imagery/documents; reconstructed in DT-L3.
Supports:
- S2 component stock;
- S3 replacement cycles;
- S4 component reuse;
- S5 environmental burdens.

## Open-loop / closed-loop
Not a building property.
Defined in DT-L5 per material and scenario.
Supports:
- S4 pathway modelling;
- S5 substitution/LCA.

## Landfill fraction
Not a fixed material property.
Derived in DT-L5 from scenario, recovery chain, quality, facility, policy, and residual flow.
Supports:
- S4 circularity accounting;
- S5 C4 burden.

---

# Architectural rule

The architecture is a network, not a staircase.

A DT-L5 decision can generate a request back to DT-L1 or DT-L3. A regional LCA mismatch discovered in DT-L5 can be resolved through DT-L2. A new renovation record can update DT-L4 and change S4/S5 outputs without changing S1.

All interfaces must therefore preserve identity, provenance, time, scale, and uncertainty.
