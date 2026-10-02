# Master Parameter Architecture — Evidence-grounded working version v0.1

## Core objective

The Digital Twin is designed to answer one operational question:

> **For a selected building, what materials and components are present, in what quantity and condition, when will they become available, which circular pathways are feasible, with what uncertainty, and what environmental consequence follows from each pathway?**

The final analytical unit is therefore:

```text
BUILDING × COMPONENT × MATERIAL × TIME × CIRCULAR PATHWAY × SCENARIO
```

The architecture is intentionally **output-driven**. Building reconstruction, GeoAI, GIS, BIM, material-intensity modelling, dynamic MFA, material passports and LCA are means to produce a decision-ready material profile.

This is a working architecture. Parameters are tagged conceptually as:
- **E** = directly supported by reviewed literature;
- **S** = synthesis across sources;
- **P** = proposed architecture field that requires further evidence/validation.

---

# 1. Overall architecture

```text
SELECTED BUILDING
      │
      ▼
DT-L1  OBSERVATION & DATA ACQUISITION
      │  physical + semantic + spatial observations
      ▼
DT-L2  IDENTITY, INTEGRATION & CONTEXT
      │  persistent IDs + provenance + scale + regional context
      ▼
DT-L3  BUILDING / COMPONENT / MATERIAL STATE RECONSTRUCTION
      │  black-box opening + probabilistic material inventory
      ▼
MATERIAL STOCK STATE
      │
      ▼
DT-L4  LIFECYCLE DYNAMICS & MATERIAL-FLOW SIMULATION
      │  maintenance + renovation + replacement + demolition
      ▼
TIME-DEPENDENT MATERIAL RELEASE
      │
      ▼
DT-L5  CIRCULARITY + LCA + DECISION INTELLIGENCE
      │  reuse / closed-loop / open-loop / recovery / disposal
      ▼
MATERIAL DECISION PROFILE
      │
      ├─ circular quantities
      ├─ effective substitution
      ├─ environmental consequences
      ├─ uncertainty distribution
      └─ uncertainty hotspot / missing data request
```

The flow is not strictly linear. DT-L5 may request new data from DT-L1–L4 when decision uncertainty is too high.

---

# 2. Cross-cutting metadata contract

Every important parameter should carry, where applicable:

| Field | Meaning |
|---|---|
| `entity_id` | persistent Building / Component / Material / Event / Flow / Scenario ID |
| `parameter_id` | stable parameter identifier |
| `value` | value, class, interval, probability or distribution |
| `unit` | explicit measurement unit |
| `source` | registry, BIM, image, LiDAR, survey, archetype, database, assumption etc. |
| `provenance` | dataset / paper / model / algorithm / version |
| `observation_date` | when the evidence was acquired |
| `valid_from` / `valid_to` | temporal validity |
| `spatial_grain` | component / building / parcel / block / district / region / country |
| `spatial_coverage` | geographic domain in which the parameter is valid |
| `regionalization_status` | generic / regional / local / building-specific |
| `value_role` | observed / inferred / dynamic / scenario |
| `uncertainty_type_original` | source terminology |
| `uncertainty_type_harmonized` | our harmonized class |
| `uncertainty_representation` | confidence / probability / SD / range / distribution / qualitative |
| `validation_status` | direct validation / cross-validation / expert checked / unvalidated / unreported |
| `completeness_status` | observed / missing / unknown / not applicable / explicitly zero |
| `version` | state/version of record |

**Rule:** unknown, not-observed and zero are different states and must not be collapsed.

---

# 3. DT-L1 — Observation & Data Acquisition

## 3.1 Building identity and geolocation

| Parameter | Role | Why it matters |
|---|---|---|
| Building ID | E/S | Persistent linkage across S1–S5 |
| Parcel / property ID | E | Registry and archive linkage |
| Address | E | Retrieval and validation |
| Latitude / longitude | E | Spatialization |
| Building polygon | E | Geometry, area, linkage |
| Parcel polygon | S | Site/context constraints |
| Administrative unit | E | Regional data linkage |
| Country / region / city | E | MI and LCA representativeness |
| Urban / rural context | E | Archetype/material context |
| Elevation | P | Context / exposure / possible construction effects |
| Heritage/protection status | S | Demolition probability and intervention constraints |

## 3.2 Core geometry

These are **observed or derived geometric descriptors**, not material quantities.

- footprint area [m²] — E
- footprint perimeter [m] — E/S
- gross floor area (GFA) [m²] — E
- net floor area [m²] — S
- gross building volume [m³] — E
- above-ground volume [m³] — E
- building height [m] — E
- eaves height [m] — E
- number of floors above ground — E
- number of basement levels — S
- floor-to-floor height — S
- roof area — S
- roof slope — P
- roof form/type — S
- external façade area — S
- exposed wall area — S
- party/shared wall area — P
- window area — S
- door area — S
- window-to-wall ratio — S
- orientation / façade azimuths — P
- surface-to-volume ratio — P
- compactness — E
- perimeter-area ratio — E
- points-perimeter / footprint-complexity metric — E
- site coverage / GSI — E
- floor space index / FSI — E
- surrounding network density — E
- adjacency / attached-detached state — P
- number / shape / distribution of building wings — P

## 3.3 Visible envelope descriptors

Candidate observations from street/aerial/oblique imagery, LiDAR, survey or documents:

- external wall visual material
- façade/cladding material
- façade finish/coating
- façade panel/module pattern
- masonry pattern
- roof covering material
- roof insulation clue if externally inferable
- glazing type clue
- window frame material
- window count
- window dimensions / area
- door count
- external door material
- balcony type/material
- external stairs
- visible structural frame
- foundation/plinth clues
- rainwater goods / external metalwork
- visible PV / solar systems
- visible retrofit/overcladding
- façade deterioration indicators
- cracking/spalling/corrosion visible from imagery

These should be stored as **observations with confidence**, not converted directly into material truth.

## 3.4 Semantic / typological descriptors

- construction year — E
- construction-period start/end — E
- age cohort — E
- last major renovation year — S
- renovation history — S
- building use/function — E
- detailed use subtype — E
- occupancy category — E
- single-/multi-family distinction — E
- residential/non-residential — E
- office/commercial/industrial/public/etc. — E
- building typology/archetype — E
- density type / urban morphology class — E
- energy-efficiency class — E
- code/regulation era — S
- construction method — E
- structural construction type — E
- structural system — E
- prefabricated / cast-in-situ / masonry / frame / modular etc. — E
- primary load-bearing material — E
- mixed/hybrid structure — S

## 3.5 Source-data quality

For every L1 source:

- source type
- original resolution
- spatial accuracy
- temporal currency
- positional uncertainty
- measurement uncertainty
- classification confidence
- image quality / occlusion
- data completeness
- missing attributes
- source ownership/licence
- retrieval date
- validation sample
- cross-validation performance
- domain-shift / transferability note

---

# 4. DT-L2 — Identity, Integration, Semantics & Context

DT-L2 prevents apparently precise values from being linked to the wrong object, time, scale or geographic context.

## 4.1 Entity model

Required persistent entity classes:

1. Building
2. Building layer
3. Component
4. Assembly
5. Material
6. Product
7. Event
8. Material flow
9. Processing facility
10. Storage location
11. Receiving project / demand point
12. Circularity scenario
13. LCA scenario
14. Decision

## 4.2 Building decomposition / shearing layers

The architecture should allow both **elemental classification** and **shearing-layer classification**.

### Site
- site works
- external paving
- retaining elements
- underground site elements

### Structure
- foundations
- footings
- piles
- basement structure
- columns
- beams
- load-bearing walls
- slabs
- structural roof
- stairs
- cores
- bracing

### Skin / envelope
- external walls
- façade/cladding
- cavity
- insulation
- membranes
- windows
- external doors
- roof covering
- waterproofing
- roof insulation

### Space / interior
- internal non-load-bearing walls
- partitions
- ceilings
- floor finishes
- wall finishes
- internal doors
- raised floors

### Services
- HVAC
- electrical systems
- plumbing
- ducts
- pipes
- cables
- plant/equipment
- lifts

### Stuff / fit-out
- fixed furnishings
- demountable fit-out
- selected equipment where in scope

**Important:** structure, skin and space can have different lifetimes and renovation cycles; the model must not impose one building-wide service life on every component.

## 4.3 Context and scale

- source spatial grain
- target spatial grain
- aggregation rule
- disaggregation rule
- spatial matching method
- geometry overlap rule
- regionalization source
- regional validity
- climate zone
- geological/soil context where relevant to foundation
- local construction tradition
- local material availability
- local code era
- local energy mix
- local waste-management system
- local reuse/recycling facilities
- road-network distance
- market/catchment region

## 4.4 Provenance graph

Each derived value should retain links to:
- original observation(s);
- preprocessing step;
- model version;
- training data;
- archetype/database;
- assumptions;
- validation record;
- downstream values generated from it.

This is essential for tracing uncertainty backward from a final circularity decision.

---

# 5. DT-L3 — Building State Reconstruction & Material Black-Box Opening

## 5.1 Structural-system inference

Candidate predictors:
- age/construction period — E
- height — E
- footprint geometry — E
- perimeter-area ratio — E
- compactness — E
- ground space index — E
- network density — E
- use/function — E
- geographic context — E/S
- floor count — S
- GFA / footprint area — E/S
- historical construction rules — S
- archival plans / permits — E
- visible structure clues — S

Outputs:
- structural-system probability vector
- selected structural system
- alternative structural hypotheses
- classification confidence
- validation status

**Do not collapse probabilistic structure inference into a deterministic class when downstream uncertainty propagation is required.**

## 5.2 Component / assembly reconstruction

For every component/assembly:

- component ID
- component class
- shearing layer
- building element
- location within building
- structural/non-structural role
- load-bearing status
- dimensions
- area
- length
- thickness
- volume
- layer sequence
- material layers
- product type
- number of repeated units
- installation method
- connection type
- accessibility
- interfacing components
- crossings/entanglement
- form containment
- coating/finish
- repair/renovation history
- installation/replacement date
- documentation availability
- inference confidence

### High-priority assemblies

#### Foundations
- type: strip / pad / raft / pile / slab / other
- concrete volume
- reinforcement ratio
- depth
- thickness
- below-ground accessibility
- soil contact
- contamination exposure

#### Structural walls / frames
- structural material
- system type
- dimensions
- reinforcement
- composite nature
- connection type
- fire protection / coatings

#### External walls
- structural backing
- cavity
- insulation type and thickness
- membrane
- cladding / facing
- mortar/adhesive
- coating
- total thickness
- separability between layers

#### Internal walls
- load-bearing/non-load-bearing
- masonry/stud/panel type
- board material
- insulation infill
- finish
- connection
- removability

#### Floors/slabs
- structural slab/deck
- reinforcement
- screed
- insulation
- floor covering
- adhesives
- raised-floor system

#### Roof
- structural system
- deck
- insulation
- waterproofing
- covering
- ballast
- drainage
- attachment method

#### Windows
- frame material
- glazing layers
- pane thickness
- spacer/frame details if known
- dimensions / count
- installation year
- replacement history
- connection/sealant
- condition
- dismantling feasibility

#### Doors
- frame
- leaf material
- glazing
- hardware
- fire rating
- dimensions/count
- connection
- condition

#### Services
- equipment/material class
- metal/plastic content
- installation date
- service life
- accessibility
- hazardous/regulated substances
- recovery route

## 5.3 Material identity and composition

The material taxonomy should be extensible. Initial families include:

### Metals
- steel
- reinforcement steel
- stainless steel
- cast iron
- copper
- aluminium
- zinc
- lead
- other metals

### Mineral / masonry
- concrete
- cement
- aggregates
- sand/gravel
- brick
- clay block
- mortar
- plaster
- gypsum/plasterboard
- natural stone
- ceramics/tiles
- mineral fill
- adobe/earth
- asphalt
- bitumen

### Bio-based
- structural timber
- sawn wood
- engineered timber
- wood products
- straw
- cork
- cellulose

### Glass
- flat glass
- laminated glass
- tempered glass
- insulated glazing units

### Polymers
- generic plastics
- PVC
- PE
- PP
- EPS
- XPS
- polyurethane
- membranes/sealants

### Insulation
- mineral wool
- glass wool
- EPS/XPS
- PUR/PIR
- cellulose
- wood fibre
- cork
- other insulation

### Finishes / composites / other
- carpet
- linoleum
- coatings/paint
- composite panels
- fibre cement
- asbestos-containing cement
- adhesives
- sealants
- unspecified/other

## 5.4 Material physical and technical properties

For each material/product:
- material name
- subtype / grade
- product name
- manufacturer if known
- density [kg/m³]
- areal density [kg/m²]
- thickness
- volume
- mass
- moisture content where relevant
- strength class
- stiffness class where relevant
- fire class
- durability class
- corrosion state
- damage state
- weathering state
- dimensional tolerance
- hazardous-substance status
- asbestos/lead/PCB/other regulated contamination status
- coating/finish
- composite / mono-material status
- embedded fasteners/inserts
- recycled content
- reused content
- renewable content
- certified origin where relevant

## 5.5 Material intensity model

For each MI record:
- material
- mass
- reference unit
- reference-unit definition
- kg/m² GFA
- kg/m³ building volume
- kg/component where appropriate
- elemental MI
- layer-specific MI
- building use
- building type
- construction period
- structural type
- floor count
- region
- urban/rural
- climate class
- energy-efficiency class
- quantification method
- sample size
- measurement type: case study / average / weighted average
- source scope
- aggregation method
- conversion method
- density source
- density distribution
- MI mean
- MI SD/CV/range/distribution
- representativeness score/status

## 5.6 Material state / quality

Material quantity is not equivalent to circular supply.

For each material/component:
- current condition
- damage type
- damage severity
- contamination
- purity
- homogeneity
- degradation
- remaining mechanical capacity where assessable
- remaining service life
- residual performance
- dimensional compatibility
- aesthetic condition
- cleaning requirement
- repair requirement
- refurbishment requirement
- recertification requirement
- test requirement
- documentation completeness
- traceability
- safety status

---

# 6. DT-L4 — Lifecycle Dynamics & Material Flows

## 6.1 Time variables

- construction year
- installation year per component
- previous renovation dates
- previous replacement dates
- current age
- component age
- building service life
- component service life
- material service life
- structural lifetime distribution
- skin lifetime distribution
- space-layer lifetime distribution
- services lifetime distribution
- maintenance interval
- replacement interval
- demolition probability
- survival probability
- renovation probability
- renovation cycle
- target year
- scenario horizon

## 6.2 Lifetime model

Store:
- distribution family (Weibull / Normal / other)
- mean
- median
- shape
- scale
- SD
- source
- geographic validity
- cohort validity
- calibration data
- dependence on building survival

**Rule:** renovation probabilities for non-structural layers should be conditional on the building/structure still surviving.

## 6.3 Event ontology

Events can include:
- new construction
- routine maintenance
- repair
- partial replacement
- full component replacement
- energy retrofit
- façade renovation
- roof renewal
- internal layout renovation
- services replacement
- extension
- adaptive reuse
- partial demolition
- full demolition
- accidental damage
- deconstruction

For every event:
- event ID
- event type
- probability
- expected date
- date distribution
- trigger
- affected component(s)
- affected material(s)
- released quantity
- retained quantity
- new inflow quantity
- quality change
- uncertainty

## 6.4 Material flow record

For every flow:
- origin building/component/material
- event
- timestamp/year
- gross released mass
- gross released volume
- collection rate
- selective-deconstruction rate
- sorting rate
- breakage/damage loss
- contamination loss
- processing loss
- net recovered mass
- destination
- transport mode
- route distance
- storage duration
- storage loss
- facility
- facility capacity
- process yield
- output quality class

---

# 7. DT-L5 — Circularity, End-of-Life & Decision Intelligence

## 7.1 Circular pathway ontology

Each material can have multiple candidate pathways:

1. **Retain in situ**
2. **Repair**
3. **Refurbish**
4. **Direct component reuse**
5. **Material reuse**
6. **Remanufacture**
7. **Closed-loop recycling**
8. **Open-loop recycling**
9. **Downcycling**
10. **Energy recovery**
11. **Incineration**
12. **Landfill**
13. **Other treatment**

The building itself must never be labelled globally as "open-loop" or "closed-loop"; pathway classification is material/component/scenario-specific.

## 7.2 Reuse / recovery feasibility variables

### Technical
- component integrity
- residual structural capacity
- material condition
- contamination
- hazardous substances
- dimensional suitability
- standardization
- modularity
- interchangeability
- connection reversibility
- connection type
- connection accessibility
- connection independence
- number of connection points
- joint visibility
- use of adhesives
- use of wet joints
- form containment
- crossings / entanglement
- access for tools
- required tool
- disassembly sequence
- disassembly time
- lifting/handling requirement
- risk of damage during removal
- expected recovery yield
- reassembly feasibility
- availability of spare parts
- certification / recertification requirement

### Quality
- retained quality fraction
- quality grade after recovery
- purity
- contamination risk
- cleaning need
- repair need
- reconditioning need
- testing need
- expected degradation during processing

### Spatial/logistical
- distance to processing facility
- distance to reuse market
- transport mode
- temporary storage need
- storage availability
- storage duration
- distance to receiving project
- geographic market radius

### Market/economic
- secondary demand
- market availability
- expected resale value
- deconstruction cost
- sorting cost
- processing cost
- transport cost
- storage cost
- testing/certification cost
- landfill cost/tax
- avoided virgin-material cost

### Regulatory
- reuse allowed?
- waste/end-of-waste status
- hazardous-material restrictions
- structural certification requirement
- fire/safety requirement
- local circularity rules

## 7.3 Circularity quantities

For every pathway:
- gross released quantity
- technically recoverable fraction
- selectively recoverable fraction
- reusable fraction
- recyclable fraction
- remanufacturable fraction
- recovery fraction
- process yield
- residual waste fraction
- landfill fraction
- incineration fraction
- quality-adjusted output
- market-usable output

Mass-balance checks should ensure fractions are logically consistent.

## 7.4 Closed-loop variables

- target same-material application
- recovered quantity
- quality retention
- recycling efficiency
- processing yield
- substitution ratio
- virgin material displaced
- recycled-content constraint
- repeated-cycle degradation
- loop-count assumption
- closed-loop feasibility probability

## 7.5 Open-loop variables

- receiving product/application
- recovered quantity
- transformation process
- quality change
- replacement coefficient
- displaced product/material
- functional equivalence basis
- market availability
- downcycling/upcycling class
- open-loop feasibility probability

## 7.6 Landfill / disposal variables

- disposal fraction
- landfill fraction
- incineration fraction
- hazardous disposal fraction
- residual processing waste
- landfill distance
- landfill process
- landfill emissions
- avoided diversion benefit where methodologically appropriate

---

# 8. Environmental impact / LCA module

## 8.1 Material environmental coefficients

For each material/product:
- EPD/database ID
- database version
- geography
- technology
- reference year
- density/reference flow
- embodied energy coefficient
- embodied GHG coefficient
- embodied water coefficient
- resource-use indicators
- other LCIA indicators
- process/hybrid/IO origin
- system-boundary completeness
- data-quality metadata
- uncertainty

Robert Crawford's EPiC work is especially relevant because it provides hybrid embodied energy, water and GHG coefficients and highlights process-data system-boundary truncation.

## 8.2 Scenario-specific LCA

For every material × pathway:
- functional unit
- reference flow
- baseline scenario
- system boundary
- A1–A3 burden
- A4 transport
- A5 construction/installation
- B-stage maintenance/replacement where relevant
- C1 deconstruction/demolition
- C2 transport
- C3 processing
- C4 disposal
- Module D / substitution treatment where used
- processing energy
- processing yield
- transport distance/mode
- future electricity mix
- future fuel mix
- avoided virgin production
- substitution credit
- replacement coefficient
- allocation rule
- recycling allocation method
- biogenic carbon assumption where applicable
- carbonation/other material-specific effects where applicable
- temporal scenario
- geographic scenario

## 8.3 Environmental outputs

At minimum:
- GHG / climate change
- embodied energy
- water where data support it

Expandable to:
- resource depletion
- acidification
- eutrophication
- photochemical ozone
- particulate matter
- toxicity
- land use
- waste generation
- hazardous waste

**Rule:** impact categories should not be added simply because a database provides them; relevance and data quality must be explicit.

---

# 9. Final Material Decision Profile

For every `Building × Component × Material`:

## Identity
- Building ID
- Component ID
- Material ID

## Stock
- material
- quantity
- quantity distribution
- component location
- quality
- condition
- provenance

## Release
- release event
- release time distribution
- released quantity distribution

## Circular pathways
For each pathway:
- technical feasibility
- recoverable quantity
- quality-adjusted quantity
- process yield
- market-usable quantity
- substitution/replacement factor
- effective virgin displacement

## Environmental consequences
For each scenario:
- baseline burden
- circular-scenario burden
- avoided burden
- net burden
- uncertainty

## Decision robustness
- dominant uncertainty source
- uncertainty contribution if quantified
- sensitivity
- decision stability
- missing critical data
- recommended additional observation/inspection

---

# 10. Uncertainty model

## 10.1 Source families

### Observation uncertainty
- geometric measurement
- imagery resolution
- LiDAR accuracy
- classification error
- missing registry data

### Entity/linkage uncertainty
- wrong Building ID match
- temporal mismatch
- spatial mismatch
- duplicated/missing entities

### Archetype/inference uncertainty
- building age
- use
- structure
- assembly
- material assignment
- MI assignment

### Parameter uncertainty
- density
- dimensions
- material intensity
- lifespan
- recovery rate
- process yield
- substitution factor
- LCA factor

### Structural/model uncertainty
- archetype model choice
- lifetime model choice
- circular pathway model
- LCA allocation
- system boundary

### Scenario uncertainty
- demolition year
- renovation
- technology
- energy mix
- policy
- market demand
- future facility availability

### Variability
Real differences among buildings/materials must be distinguished from uncertainty about those differences.

## 10.2 Per-source uncertainty fields

- uncertainty source ID
- original terminology
- harmonized type
- distribution/representation
- parameter affected
- correlation/dependence
- source evidence
- transfer status
- representation change
- magnitude change
- downstream effect
- decision consequence
- evidence locator

## 10.3 Uncertainty fate

Do not use one mutually exclusive label for an entire study. For each source and link separately record:
- Preserved
- Legitimately reduced
- Amplified
- Transformed
- Masked/lost
- Unassessed

Transfer, representation change and magnitude change remain separate variables.

---

# 11. Uncertainty-reduction actions by layer

## DT-L1
Potential actions:
- higher-quality imagery
- additional viewpoints
- LiDAR
- cadastral/permit retrieval
- on-site inspection
- material sampling
- visual validation

## DT-L2
- entity-resolution validation
- consistent Building IDs
- spatial matching
- temporal alignment
- local/regional data selection
- explicit scale-transition rules

## DT-L3
- probabilistic archetypes
- multiple material hypotheses
- building-specific plans/BIM
- local MI data
- component-level MI
- quality inspection
- uncertainty-preserving inference

## DT-L4
- calibrated survival models
- component/layer-specific lifetimes
- renovation records
- cohort-specific lifetimes
- dependence between renovation and demolition

## DT-L5
- material testing
- contamination testing
- disassembly audit
- facility-specific yields
- local market data
- pathway-specific substitution factors
- prospective LCA scenarios

**Important:** every claimed reduction must be demonstrated; additional detail can also reveal or amplify uncertainty.

---

# 12. High-priority uncertainty hotspots suggested by current literature

These are hypotheses for testing, not final rankings:

- material intensity representativeness;
- structural-system classification;
- hidden assembly composition;
- insulation thickness/density;
- foundation geometry;
- component service life;
- renovation timing;
- material quality/condition;
- connection and detachability information;
- contamination;
- recovery/process yield;
- substitution/replacement factor;
- future market/technology;
- LCI geographic/temporal representativeness;
- LCA system-boundary and allocation choices.

The hotspot register must be populated only when evidence supports the importance of each factor.

---

# 13. Architecture acceptance test

The architecture succeeds only if, after filling its inputs for a selected building, it can produce:

```text
Material X
├─ Where is it?
├─ How much is there?
├─ In what component/assembly?
├─ In what condition?
├─ How sure are we?
├─ When will it be released?
├─ Can it be separated without destructive loss?
├─ Can it be reused?
├─ Can it be closed-loop recycled?
├─ Can it be open-loop recycled?
├─ What quantity survives each pathway?
├─ What virgin material/product can it substitute?
├─ What is the environmental consequence?
├─ How uncertain is that consequence?
└─ What additional data would most improve the decision?
```
