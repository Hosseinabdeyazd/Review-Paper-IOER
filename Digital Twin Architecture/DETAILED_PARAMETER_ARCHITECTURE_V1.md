# Detailed Digital Twin Parameter Architecture — v1.0

## Status

Literature-driven working architecture. This version is intentionally broad and detailed. It is **not a claim that every parameter must always be populated**. The architecture distinguishes mandatory, preferred, conditional and scenario-specific information so that it can work with incomplete real-world data.

The Digital Twin is designed backward from one final output:

> **For a selected building, produce a material-by-material decision profile containing stock, component context, quality, release timing, circular pathway feasibility, effective substitution, environmental consequences and propagated uncertainty.**

---

# 1. Architectural principle

The architecture has five capability layers, but parameters are not owned by only one layer. A parameter may be observed in DT-L1, contextualized in DT-L2, used for inference in DT-L3, propagated through time in DT-L4, and finally influence circularity or LCA in DT-L5.

```text
SELECT BUILDING
      ↓
DT-L1  OBSERVE / ACQUIRE
      ↓
DT-L2  IDENTIFY / LINK / CONTEXTUALIZE
      ↓
DT-L3  RECONSTRUCT BUILDING → COMPONENT → MATERIAL
      ↓
DT-L4  EVOLVE STOCK → EVENTS → MATERIAL RELEASE FLOWS
      ↓
DT-L5  TEST REUSE / CLOSED LOOP / OPEN LOOP / RECOVERY / DISPOSAL
      ↓
      CALCULATE EFFECTIVE SUBSTITUTION + LCA
      ↓
MATERIAL DECISION PROFILE
      ↓
UNCERTAINTY HOTSPOTS + NEXT DATA REQUEST
```

---

# 2. Priority classes

Each field receives one of four practical priorities:

- **P0 Core** — required to produce a minimally useful material decision profile.
- **P1 High-value** — strongly improves material inference, timing or circularity decisions.
- **P2 Conditional** — required for particular materials, building systems, pathways or LCA scopes.
- **P3 Enrichment** — useful for advanced modelling, validation or stakeholder decisions.

No missing P1–P3 field should automatically block the model; it should increase explicit uncertainty instead.

---

# 3. Entity hierarchy

```text
Site / Location
  └── Building
       ├── Building layer
       │    ├── Structure
       │    ├── Skin / Envelope
       │    ├── Space / Interior
       │    └── Services
       ├── Component
       │    └── Material / Product
       ├── Event
       ├── Material Flow
       ├── Process / Facility
       ├── Scenario
       ├── Environmental Impact
       └── Decision
```

The component level is essential because reuse decisions concern assemblies such as windows, doors, beams, façade panels and fixtures, not only tonnes of glass, steel or timber.

---

# 4. DT-L1 — Observation & Data Acquisition

## 4.1 Building identity and geospatial context

| Parameter | Priority | Role |
|---|---|---|
| building_id | P0 | persistent identity |
| parcel_id / cadastral_id | P1 | data linkage |
| centroid coordinates | P0 | spatialization |
| footprint polygon | P0 | geometry/material inference |
| address | P1 | registry linkage |
| municipality / district / region | P1 | regionalization |
| country | P0 | codes, LCI, construction practice |
| urban / suburban / rural class | P2 | archetype/context |
| climate zone | P1 | envelope typology, LCA context |
| seismic zone | P2 | structural/material intensity context |
| topographic context | P2 | construction/material differences |
| elevation | P3 | contextual |
| surrounding density | P2 | morphology/access |
| street/access conditions | P2 | deconstruction logistics |
| heritage/protection status | P2 | renovation/demolition constraints |

### Uncertainty to store
- geolocation accuracy;
- footprint positional error;
- registry matching confidence;
- geographic validity of contextual datasets.

---

## 4.2 Building geometry and morphology

| Parameter | Priority | Role |
|---|---|---|
| footprint area | P0 | stock scaling |
| footprint perimeter | P1 | façade/wall quantity |
| gross floor area (GFA) | P0 | material intensity scaling |
| net floor area | P2 | functional comparisons |
| building height | P0 | volume/floor inference |
| number of storeys | P0 | structural/material archetype |
| average floor-to-floor height | P1 | wall/column quantities |
| building volume | P1 | archetyping |
| basement presence | P1 | foundations/below-grade stock |
| number of basement levels | P2 | structural stock |
| roof form | P1 | roof materials |
| roof pitch | P2 | roof quantity/type |
| roof area | P1 | material quantity |
| façade area by orientation | P1 | envelope stock |
| plan shape / compactness | P2 | envelope-to-floor ratios |
| perimeter/area ratio | P2 | archetyping/material demand |
| built form | P1 | detached/terraced/block/tower etc. |
| adjacency/shared walls | P1 | external wall stock |
| orientation | P2 | façade/window context |
| extensions/additions | P1 | mixed-age material stock |

Evidence basis: building age, use, structure, built form, region, height, footprint, volume, GFA and P/A ratio recur in archetype/material-intensity research; recent sensitivity work also shows floor count and floor height can materially change estimated stock.

---

## 4.3 Openings and externally visible components

| Parameter | Priority | Role |
|---|---|---|
| number of windows | P1 | component stock |
| window area | P1 | glass/frame quantity |
| window-to-wall ratio | P2 | stock inference |
| glazing type | P2 | material/environmental profile |
| glazing layers | P2 | quality/reuse |
| frame material | P1 | material identification |
| window installation period | P2 | residual life |
| number of external doors | P1 | component reuse |
| door material/type | P2 | material/reuse |
| façade material | P1 | material stock |
| façade finish/coating | P2 | separability/contamination |
| balcony count/type | P2 | component/material stock |
| visible external services | P3 | supplementary stock |

Computer-vision studies show that component-level information such as façade material, windows and doors can be collected at scale and represented probabilistically rather than as deterministic counts.

---

## 4.4 Building use and occupancy-related attributes

| Parameter | Priority | Role |
|---|---|---|
| primary use | P0 | archetype/material intensity |
| secondary/mixed use | P1 | heterogeneity |
| residential subtype | P2 | archetype |
| non-residential subtype | P2 | archetype |
| occupancy status | P2 | renovation/demolition scenario |
| vacancy status/duration | P2 | event probability |
| number of dwelling/functional units | P2 | component demand |
| occupancy intensity | P3 | service/component replacement |

---

## 4.5 Age, cohort and construction history

| Parameter | Priority | Role |
|---|---|---|
| construction year | P0 | archetype/material system |
| construction period/cohort | P0 | uncertainty-tolerant age class |
| code/standard era | P1 | structural/material inference |
| last major renovation year | P1 | component age |
| renovation type/history | P1 | current hidden stock |
| façade retrofit year | P2 | envelope stock |
| roof replacement year | P2 | roof stock |
| window replacement year | P2 | component stock |
| internal refurbishment year | P2 | interior material stock |
| structural alteration history | P2 | structure/material changes |
| extension construction year | P2 | mixed-cohort stock |
| source of age information | P0 | provenance |
| age confidence/distribution | P0 | uncertainty propagation |

Age should not be used alone as the archetype key; literature shows construction type, function, geography and morphology can explain additional material-intensity variability.

---

## 4.6 Data-source metadata

For every observation:
- source type;
- source owner/provider;
- acquisition date;
- spatial resolution;
- temporal validity;
- coordinate system;
- sensor/platform;
- image/view geometry where relevant;
- completeness;
- quality flag;
- extraction method;
- manual/automatic;
- model name/version;
- confidence/probability;
- validation sample;
- legal/access restrictions.

Candidate data sources:
- cadastre;
- building registry;
- permits;
- EPC/energy certificate;
- BIM/IFC;
- architectural/structural drawings;
- bill of quantities;
- EPD/product records;
- aerial/satellite imagery;
- LiDAR/point cloud;
- street imagery;
- UAV/photogrammetry;
- field survey;
- material sample;
- demolition audit;
- maintenance logs.

---

# 5. DT-L2 — Identity, Integration, Semantics & Context

## 5.1 Persistent identity

Core identifiers:
- building_id;
- component_id;
- material_instance_id;
- product_id;
- event_id;
- flow_id;
- facility_id;
- scenario_id;
- LCA_dataset_id.

Relationships must be versioned. A window replaced in 2028 should become a new component instance, not silently overwrite the old one.

---

## 5.2 Spatial semantics

Parameters:
- geometry source;
- geometry version;
- source spatial grain;
- target spatial grain;
- spatial coverage;
- regional validity;
- coordinate uncertainty;
- spatial join/matching method;
- aggregation/disaggregation rule;
- regionalization status;
- spatialization status;
- nearest/eligible facility;
- catchment area;
- transport network linkage.

Regionalization and spatialization are kept separate:
- **regionalization** asks whether a value/process represents the geographic context;
- **spatialization** asks where the object/flow is located.

---

## 5.3 Temporal semantics

Parameters:
- observation_date;
- valid_from;
- valid_to;
- installation_date;
- expected_EoL;
- scenario_year;
- dataset_reference_year;
- electricity_mix_year;
- process_technology_year;
- price/market_year where economic extension is used.

---

## 5.4 Semantic harmonization

Required mappings:
- building-use taxonomy;
- building-type taxonomy;
- component taxonomy;
- material taxonomy;
- waste classification;
- EPD/product category;
- circularity pathway vocabulary;
- LCA impact categories;
- units and reference quantities.

Each mapping stores:
- original term;
- harmonized term;
- mapping confidence;
- rule/version;
- unresolved ambiguity.

---

# 6. DT-L3 — Building State & Material Reconstruction

## 6.1 Building archetype state

Candidate variables:
- function/use;
- age/cohort;
- structural type;
- built form;
- height class;
- floor count;
- footprint/GFA;
- region;
- climate zone;
- seismic zone;
- topographic type;
- construction technology;
- roof type;
- façade type;
- socioeconomic/context class where evidence supports it.

Store:
- assigned archetype;
- archetype probability;
- alternative archetypes;
- training/reference sample;
- sample size;
- transferability domain;
- validation error.

Material-intensity research shows that archetypes based only on use/age may miss variation. Construction type and geography can be especially important, and material-specific optimal predictors can differ.

---

## 6.2 Structural system

| Parameter | Priority |
|---|---|
| primary structural system | P0 |
| dominant structural material | P0 |
| foundation type | P1 |
| foundation material | P1 |
| slab system | P1 |
| slab material/thickness | P1 |
| beam system/material | P1 |
| column system/material | P1 |
| load-bearing wall material | P1 |
| structural core material | P2 |
| stair structure/material | P2 |
| span/grid dimensions | P2 |
| structural member sizes | P2 |
| reinforcement ratio | P2 |
| prefabricated/cast-in-situ | P2 |
| connection type | P2 |
| structural condition | P1 |
| residual structural capacity | P2 |

---

## 6.3 External envelope

### External wall
- assembly ID;
- wall type;
- layer sequence;
- material of each layer;
- layer thickness;
- density;
- area;
- mass;
- insulation material;
- insulation thickness;
- cladding material;
- render/mortar;
- membranes;
- cavity;
- fixings;
- coatings/paint;
- hazardous additives;
- adhesively bonded vs mechanically fixed;
- accessibility;
- separability;
- installation/replacement year;
- condition.

### Roof
- roof structure;
- covering;
- waterproofing;
- insulation;
- membranes;
- substrate/deck;
- drainage elements;
- fixings;
- area/thickness/mass;
- condition;
- separability;
- replacement history.

### Windows
- count;
- dimensions/area;
- frame material;
- glazing type;
- pane count;
- spacer/sealant;
- hardware;
- connection/fixing;
- installation year;
- condition;
- reuse suitability.

### External doors
- count;
- dimensions;
- material;
- glazing;
- frame;
- hardware;
- installation year;
- condition;
- reuse suitability.

---

## 6.4 Internal building layers

### Internal walls/partitions
- load-bearing/non-load-bearing;
- system type;
- studs/frame;
- boards;
- insulation;
- plaster/render;
- tiles/finish;
- dimensions;
- connection type;
- separability;
- condition.

### Floors
- structural slab;
- screed;
- insulation;
- raised floor;
- floor finish;
- adhesives;
- coatings;
- area/thickness/mass;
- contamination;
- separability.

### Ceilings
- suspended/non-suspended;
- grid;
- panels;
- insulation;
- services integration;
- accessibility;
- reuse potential.

### Fixed furniture/fit-out
- kitchens;
- sanitary fixtures;
- built-in cabinets;
- counters;
- partitions;
- lighting fixtures;
- radiators.

Component-level studies demonstrate that doors, windows, fixtures and other non-structural elements can be meaningful reuse flows and should not disappear into bulk material mass.

---

## 6.5 Building services

Conditional but important for complete circular inventories:
- HVAC equipment type;
- ducts;
- pipes by material;
- cable mass/type;
- radiators;
- pumps;
- boilers/heat pumps;
- PV modules;
- inverters;
- batteries;
- elevators;
- fire systems;
- sanitary equipment;
- controls/sensors.

For each:
- manufacturer/product;
- installation year;
- quantity;
- mass;
- material composition;
- expected service life;
- replaceability;
- hazardous substances;
- reuse/recycling route.

---

## 6.6 Material/product record — core schema

Every material/product instance should support:

### Identity
- material_id;
- material family;
- material subtype/grade;
- product name;
- manufacturer;
- product code;
- EPD/DPP/passport link.

### Physical quantity
- count;
- length;
- area;
- volume;
- density;
- mass;
- material intensity;
- reference denominator (kg/m2 GFA, kg/m3 building, kg/component etc.);
- uncertainty/distribution.

### Composition
- constituents;
- recycled content;
- renewable content;
- additives;
- binders;
- coatings;
- finishes;
- adhesives;
- reinforcement;
- embedded fasteners;
- composite/mono-material status.

### Origin
- primary/secondary;
- manufacturing location;
- extraction/source region;
- recycled feedstock origin;
- transport history where available.

### Condition/quality
- visual condition;
- damage;
- corrosion;
- cracking;
- moisture;
- biological degradation;
- dimensional damage;
- residual mechanical performance;
- contamination;
- hazardous substances;
- purity;
- certification/quality evidence;
- uncertainty.

### Environmental properties
- EPD availability;
- dataset source;
- embodied GHG;
- embodied energy;
- embodied water;
- resource use;
- other LCIA indicators;
- data year;
- geographic representativeness;
- system boundary;
- data quality.

Digital building logbook research explicitly includes material type/subtype, location, volume, weight, lifespan, reuse/recycling potential, EPD/DPP and update date; other logbook proposals also include layer thickness, conductivity, density, GWP, energy indicators, fire class and waste category.

---

# 7. DT-L4 — Dynamics, Service Life & Material Flows

## 7.1 Building-layer decomposition

At minimum distinguish:
- **Structure** — long-life structural frame/foundation;
- **Skin** — façade, roof, windows, external doors;
- **Space** — partitions, finishes, fit-out;
- **Services** — MEP systems.

Recent layered dMFA work shows that treating the building as one homogeneous object can misrepresent renovation flows because different layers have different lifetimes and renovation cycles.

---

## 7.2 Service-life parameters

For building:
- reference service life;
- demolition lifetime distribution;
- survival function;
- demolition hazard/probability;
- vacancy/obsolescence scenario.

For each component/material:
- technical service life;
- design life;
- expected service life;
- remaining service life;
- lifetime distribution family;
- distribution parameters;
- maintenance interval;
- replacement cycle;
- renovation cycle;
- dependency on building survival;
- dependency on condition;
- code/technology obsolescence.

---

## 7.3 Event model

Event types:
- construction;
- maintenance;
- repair;
- replacement;
- retrofit;
- refurbishment;
- adaptive reuse;
- extension;
- partial demolition;
- full demolition;
- disaster/damage event;
- deconstruction.

For every event:
- event probability;
- expected time;
- time distribution;
- affected components;
- removal fraction;
- retained fraction;
- incoming materials;
- outgoing materials;
- temporary storage;
- event-specific damage/loss;
- uncertainty.

---

## 7.4 Material release flow

Per material/component:
- gross stock before event;
- quantity affected;
- released quantity;
- salvageable quantity;
- mixed-waste quantity;
- sorted quantity;
- damaged quantity;
- contamination fraction;
- recovery yield;
- residual waste;
- destination class;
- timing;
- uncertainty.

---

# 8. DT-L5 — Circularity Pathways & Decision Intelligence

## 8.1 Pathway hierarchy

Each material/component may have multiple scenario-specific routes:

1. continued use / life extension;
2. repair;
3. direct reuse;
4. refurbishment;
5. remanufacture;
6. closed-loop recycling;
7. open-loop recycling;
8. downcycling;
9. material/energy recovery;
10. landfill/disposal.

Do not collapse these into one circularity percentage without retaining pathway detail.

---

## 8.2 Reuse feasibility

### Technical
- component integrity;
- residual strength/performance;
- dimensional compatibility;
- tolerance;
- standard size;
- modularity;
- code compliance;
- fire performance;
- thermal/acoustic performance;
- certification potential;
- repair requirement.

### Disassembly
- connection type;
- reversible connection?;
- mechanical vs chemical fixation;
- accessibility;
- sequence;
- dependency on adjacent layers;
- destructive removal risk;
- tools/equipment;
- worker safety;
- expected damage during removal;
- time/labour;
- disassembly yield.

### Information
- manufacturer known?;
- drawings available?;
- installation history?;
- maintenance history?;
- prior load/use history?;
- material passport?;
- test certificate?;
- inspection/test required?

### Market/logistics
- demand exists?;
- required dimensions/specification?;
- distance to demand;
- timing match between supply/demand;
- storage need;
- storage duration;
- storage loss;
- transport mode;
- handling.

---

## 8.3 Recycling and processing parameters

Per material and route:
- selective demolition yes/no;
- source separation;
- sorting technology;
- pre-processing;
- crushing/cutting/shredding;
- cleaning;
- decontamination;
- separation efficiency;
- recovery efficiency;
- process yield;
- reject rate;
- process energy;
- process water;
- auxiliary materials;
- emissions;
- output particle/size class;
- output grade;
- output purity;
- technical quality;
- residual waste;
- facility capacity;
- facility technology year.

The CDW LCA literature shows input composition and selective vs mixed demolition strongly affect recycling energy and product quality.

---

## 8.4 Recycled-material quality and replacement coefficient

Recommended decomposition:

- **Q1 purity coefficient** — composition/purity of recycled output;
- **Q2 technical quality coefficient** — technical fitness compared with substituted material/application;
- **M market coefficient** — fraction of produced secondary material actually absorbed by market;
- replacement/substitution coefficient;
- substituted product/material identity;
- substitution ratio;
- application class;
- quality-loss/downcycling flag.

This follows the quality-sensitive replacement-coefficient logic reported in CDW LCA literature. Quality should not be inferred from recovery rate alone.

---

## 8.5 Open-loop vs closed-loop

### Closed-loop
Store:
- source material;
- secondary output;
- same/similar function?;
- recycled content in next product;
- substitution ratio;
- processing losses;
- number of potential cycles where evidence exists;
- quality retention.

### Open-loop
Store:
- source material;
- destination application;
- destination product;
- quality transformation;
- replacement coefficient;
- market demand;
- potential cascading/downcycling;
- avoided virgin product;
- uncertainty.

A building itself is never simply labelled open-loop or closed-loop; the pathway is material- and scenario-specific.

---

## 8.6 Landfill/disposal

Do **not** hard-code a generic landfill percentage.

Store:
- jurisdiction;
- reference year;
- material type;
- waste classification;
- baseline landfill share;
- recycling/recovery share;
- incineration/energy recovery share where applicable;
- illegal/untracked fraction if evidenced;
- landfill type;
- landfill distance;
- landfill burden;
- scenario-specific diversion rate;
- policy constraint;
- uncertainty/source.

Rates are temporal, regional and material-specific.

---

# 9. Logistics and spatial circularity network

For each facility/destination:
- facility_id;
- type;
- accepted materials;
- accepted quality/contamination thresholds;
- capacity;
- utilization;
- processing technology;
- recovery efficiency;
- output grade;
- gate fee/cost if economic layer used;
- coordinates;
- road distance;
- travel time;
- transport mode;
- fuel/energy;
- loading factor;
- backhaul assumption;
- storage capacity;
- operating horizon.

For reuse demand:
- receiving project;
- material specification;
- required quantity;
- required quality;
- demand year/window;
- maximum distance;
- certification requirement.

This enables the Digital Twin to treat circularity as a spatial-temporal matching problem, not only as an intrinsic property of the material.

---

# 10. LCA and embodied environmental impact architecture

## 10.1 Mandatory methodological metadata

- goal;
- decision context;
- functional unit;
- reference flow;
- system boundary;
- attributional/consequential approach;
- allocation method;
- database;
- dataset version;
- geography;
- reference year;
- LCIA method;
- impact categories;
- cut-off/completeness;
- uncertainty method;
- sensitivity analysis.

---

## 10.2 Building/product life-cycle modules

Where applicable retain:
- A1 raw material supply;
- A2 transport;
- A3 manufacturing;
- A4 transport to site;
- A5 construction/installation;
- B1 use;
- B2 maintenance;
- B3 repair;
- B4 replacement;
- B5 refurbishment;
- B6 operational energy where in scope;
- B7 operational water where in scope;
- C1 deconstruction/demolition;
- C2 transport;
- C3 waste processing;
- C4 disposal;
- D benefits/loads beyond system boundary.

---

## 10.3 Environmental coefficients by material/product

At minimum where data exist:
- GWP/embodied GHG;
- embodied energy;
- embodied water;
- renewable/non-renewable primary energy;
- resource depletion;
- acidification;
- eutrophication;
- photochemical ozone;
- ozone depletion;
- particulate matter;
- human toxicity;
- ecotoxicity;
- land use;
- water scarcity;
- waste generation.

Material-specific conditional parameters:
- biogenic carbon;
- carbonation;
- recycled-content allocation;
- co-product allocation;
- reuse allocation;
- recycling allocation.

Crawford and collaborators' EPiC work is particularly relevant for hybrid embodied energy, water and GHG coefficients and for avoiding process-data truncation.

---

## 10.4 Circular scenario LCA

For every material × pathway:
- deconstruction burden;
- sorting burden;
- processing burden;
- transport burden;
- storage burden;
- testing/certification burden if known;
- avoided disposal;
- avoided virgin production;
- substitution coefficient;
- replaced product dataset;
- residual disposal;
- Module D handling;
- net scenario impact;
- uncertainty.

The literature warns that avoided-impact results are unreliable when the avoided material, quality and substitution coefficient are not transparently defined.

---

# 11. User/scenario control layer

User-configurable:
- selected building(s);
- reference date;
- target year/horizon;
- allowed pathways;
- closed-loop only?;
- open-loop allowed?;
- reuse prioritized?;
- recycling prioritized?;
- landfill cap;
- minimum recovered quality;
- maximum transport distance;
- maximum processing energy;
- local-only requirement;
- demand scenario;
- technology scenario;
- energy-mix scenario;
- demolition/renovation scenario;
- environmental objective;
- economic objective if enabled;
- robustness threshold;
- acceptable uncertainty threshold.

The system should not hide user choices inside the model. Every decision assumption is a scenario parameter with provenance.

---

# 12. Uncertainty control plane

Every important parameter should carry:

## 12.1 Source
- measurement;
- classification;
- proxy;
- archetype;
- database;
- expert assumption;
- scenario;
- model structure;
- temporal forecast;
- market forecast.

## 12.2 Nature
- variability;
- epistemic/data uncertainty;
- model/structural uncertainty;
- choice/scenario uncertainty;
- mixed.

## 12.3 Representation
- point estimate;
- range;
- confidence interval;
- probability;
- categorical confidence;
- distribution;
- ensemble;
- unknown/unassessed.

## 12.4 Propagation fields
- source_type_original;
- source_type_harmonized;
- transfer_status;
- representation_change;
- magnitude_change;
- change_basis;
- dependence_handling;
- correlation;
- evidence_locator;
- downstream_consequence.

## 12.5 Validation
- validation dataset;
- sample size;
- metric;
- bias;
- error;
- calibration;
- out-of-domain flag.

## 12.6 Decision contribution
- sensitivity rank;
- variance contribution where available;
- decision-switch contribution;
- impact on pathway feasibility;
- impact on LCA interval;
- priority for new information.

---

# 13. Target material-output record

For every selected building, final output should be iterable material-by-material:

```text
Material / Component
├── identity & location
├── quantity + uncertainty
├── condition / quality + uncertainty
├── remaining life
├── expected release event/time + uncertainty
├── direct reuse potential
├── closed-loop recycling potential
├── open-loop recycling potential
├── recovery/disposal fractions
├── substitution / replacement coefficient
├── demand / facility match
├── scenario-specific environmental impact
├── uncertainty decomposition
└── next-best information request
```

---

# 14. Uncertainty-reduction logic

The Digital Twin should not collect every possible data field by default.

For a given material decision:

1. run with currently available data;
2. propagate uncertainty;
3. identify dominant uncertainty source;
4. identify the cheapest/most feasible additional information that could reduce it;
5. acquire/update only that information;
6. rerun affected layers;
7. test whether the decision becomes more robust.

Examples:
- uncertain façade material → request street imagery/site inspection;
- uncertain hidden wall assembly → request plans/BIM/targeted inspection;
- uncertain material quantity → refine geometry or material intensity;
- uncertain component quality → inspection/testing;
- uncertain release date → refine lifetime/renovation model;
- uncertain recycling benefit → identify actual processor/output grade/substitution;
- uncertain LCA → use local/updated EPD/LCI data.

---

# 15. Evidence-derived design rules

1. **Age and use are important but insufficient archetype descriptors.**
2. **Construction/structural type should be captured where possible.**
3. **Building components must be preserved in the data model for reuse.**
4. **Material intensity needs explicit reference denominator, source and transferability domain.**
5. **Regionalization and spatialization are separate.**
6. **Structure, skin, space and services require different dynamic lifetimes.**
7. **Renovation flows cannot be represented adequately by demolition-only models.**
8. **Material quality must enter circularity and LCA, not only recovery rate.**
9. **Selective demolition/mixed waste composition changes recovery quality and processing burden.**
10. **Open-loop and closed-loop must be distinguished per material/pathway.**
11. **Substitution must name the actually replaced material/product and quality basis.**
12. **Circularity is spatial and temporal: demand, facility, distance and timing matter.**
13. **Environmental impact per tonne is not proportional to material mass; low-mass materials can dominate impacts.**
14. **Uncertainty should remain attached to material records through every link.**
15. **Missing information should increase explicit uncertainty rather than be silently filled with deterministic defaults.**

---

# 16. Literature anchors for v1.0

This architecture is synthesized from the review papers already studied in the project plus an expanded literature sweep. Key anchors include:

- Schiller et al. — material composition indicators and their transferability; building-stock quantification in Germany.
- Kleemann et al. / Schiller et al. — randomly sampled Vienna buildings; age, use, volume and plan-based material intensities.
- Dong et al. (2026) — material-intensity variability and archetype variables.
- Arbabi et al. (2022) — scalable building/component characterization using footprints, height, street imagery, façade material, windows and doors.
- Arora et al. (2020) — component-level urban mining, recovery and reuse.
- Reis Santos et al. (2019) — dynamic building-material-stock review; spatial, temporal and cohort dynamics.
- Liu et al. (2026) — layered dMFA separating structure, skin and space renovation dynamics.
- Sprecher et al. (2022) — empirical MI database with building structure and components.
- Pei, Biljecki & Stouffs (2024) — integration of building material stock analysis and LCA at urban scale.
- Bayram & Greiff (2023) — CDW recycling LCA; quality, avoided impacts, substitution and uncertainty.
- BAMB materials passports — material/product/component information and lifecycle tracking.
- Mao & Cao (2025) — material passport content/circularity relationships.
- Heisel & Rau-Oberhuber (2020) — material availability in quantities and qualities, location and time.
- ISO 20887:2020 — design for disassembly/adaptability.
- Crawford, Stephan & Prideaux — EPiC hybrid embodied environmental coefficients.
- Crawford et al. / Prideaux et al. — LCA integration and embodied-impact data in building design.
- Hossain & Ng (2018) — building LCA + circular economy, quantity/quality, substitution and full lifecycle.
- Patouillard et al. (2018) — spatialization, regionalization and resolution.
- Baustert & Benetto (2017) — uncertainty source/propagation architecture.

This is a working synthesis, not a claim that the listed literature agrees on a single Digital Twin architecture.
