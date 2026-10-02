# MASTER ARCHITECTURE v1 — Building-to-Material Circularity Digital Twin

## 0. Purpose

This architecture is designed around one user action:

> **Select a building.**

The system should return a **decision-ready material profile** for that building, including:
- what materials/components exist;
- how much of each exists;
- their condition and quality;
- when they may be released;
- whether they can be reused, remanufactured, recycled in closed loop, recycled in open loop, recovered, or landfilled;
- the effective amount that can substitute virgin production;
- the environmental consequences of each pathway;
- the uncertainty attached to every important step;
- the dominant uncertainty hotspot and the next most valuable data acquisition action.

This is not primarily a 3D visualization architecture. It is a **material-decision architecture** with a Digital Twin as the integration, updating and uncertainty-management fabric.

---

# 1. Architectural principles

## P1 — Material-in-context is the final analytical unit
The final unit is:

```text
Material
+ Building
+ Component
+ Location
+ Time
+ Condition
+ Circular pathway
+ Environmental context
+ Uncertainty
```

## P2 — Building is the selected container, not the final output
A building selection opens a hierarchy:

```text
Building
  └── Systems
       └── Components
            └── Materials
                 └── Future flows
                      └── Circular pathways
                           └── Environmental consequences
```

## P3 — DT-L1…DT-L5 are capabilities, not a rigid pipeline
Any DT layer can interact with several S1–S5 streams. Feedback can move upstream.

## P4 — Every critical value must carry context
A value without provenance, time, spatial validity and uncertainty is incomplete for this architecture.

## P5 — Uncertainty reduction must be targeted
The system should ask for new data only when it is expected to reduce decision-relevant uncertainty.

---

# 2. Core entity model

## E1 Building
Identity and physical/spatial container.

## E2 Building System
Examples:
- substructure/foundation;
- primary structure;
- floors;
- external walls;
- internal walls/partitions;
- façade;
- roof;
- windows;
- external doors;
- internal doors;
- stairs;
- ceilings;
- finishes;
- insulation;
- building services / MEP;
- external works where relevant.

## E3 Component
Examples:
- beam;
- column;
- slab;
- brick wall;
- window unit;
- door;
- façade panel;
- insulation panel;
- roof tile;
- plasterboard sheet;
- pipe;
- duct;
- cable;
- sanitary fixture.

## E4 Material
Examples:
- concrete;
- cement/mortar;
- clay brick;
- ceramic;
- stone;
- sand/gravel;
- structural steel;
- reinforcement steel;
- aluminium;
- copper;
- glass;
- timber;
- engineered timber;
- gypsum/plasterboard;
- mineral wool;
- glass wool;
- EPS/XPS;
- polyurethane;
- PVC;
- other plastics;
- bitumen;
- paints/coatings;
- adhesives/sealants;
- composite materials.

## E5 Event
- construction;
- maintenance;
- repair;
- replacement;
- refurbishment;
- extension;
- partial demolition;
- complete demolition;
- change of use.

## E6 Material Flow
Links a material/component to an event, quantity, time, origin and destination.

## E7 Process / Facility
- on-site separation;
- deconstruction;
- sorting;
- cleaning;
- crushing;
- shredding;
- remanufacturing;
- recycling;
- disposal;
- reuse depot;
- secondary-material marketplace;
- landfill;
- incineration/energy recovery where applicable.

## E8 Scenario
A user- or model-defined future state.

## E9 Environmental Dataset
LCI/LCIA/EPD/material-flow coefficient records.

## E10 Decision
A material-specific or building-wide comparison under explicit objectives and constraints.

---

# 3. Five Digital Twin capability layers

# DT-L1 — Observation & Data Acquisition

## L1.1 Geospatial identity and geometry
### Building geometry
- building footprint;
- polygon geometry;
- centroid;
- address;
- coordinates;
- elevation;
- ground level;
- building height;
- eaves height;
- ridge height;
- gross volume;
- gross floor area;
- net floor area where available;
- number of storeys;
- basement presence/count;
- roof geometry;
- roof slope;
- façade orientation;
- perimeter;
- compactness/form factor;
- attached/detached condition;
- adjacency/shared walls;
- setbacks;
- footprint complexity;
- building orientation.

### Geometry source
- cadastral;
- LoD1/LoD2/LoD3 city model;
- LiDAR;
- photogrammetry;
- satellite imagery;
- aerial imagery;
- street imagery;
- BIM/CAD;
- permit drawings;
- manual survey.

### Geometry quality metadata
- positional accuracy;
- vertical accuracy;
- acquisition date;
- point density/resolution;
- LoD;
- occlusion;
- completeness;
- reconstruction method;
- confidence.

## L1.2 Building function and typology evidence
- current use;
- original use if known;
- mixed-use share;
- residential subtype;
- non-residential subtype;
- occupancy category;
- floor-use distribution;
- vacancy;
- ownership class where relevant;
- heritage/protection status;
- building typology;
- morphology class.

## L1.3 Age and construction-period evidence
- construction year;
- construction period band;
- permit year;
- completion year;
- major refurbishment year(s);
- extension year(s);
- façade replacement year;
- roof replacement year;
- window replacement year;
- MEP replacement year;
- structural intervention year;
- age confidence;
- evidence source.

## L1.4 Visual envelope observations
### External wall/facade
- visible façade material;
- cladding material;
- render/plaster;
- brick type;
- stone type;
- panel type;
- curtain wall;
- façade thickness if known;
- façade condition;
- visible deterioration;
- façade fastening clues.

### Windows
- number;
- dimensions;
- window-to-wall ratio;
- frame material;
- glazing type;
- glazing layers;
- visible age;
- opening type;
- replacement evidence;
- condition.

### Doors
- external door count;
- dimensions;
- material;
- frame;
- glazing share;
- condition;
- installation period.

### Roof
- roof form;
- covering material;
- insulation clues;
- drainage components;
- skylights;
- roof age;
- roof condition.

## L1.5 Documentary and administrative evidence
- BIM;
- IFC;
- CAD;
- BoQ;
- material schedule;
- construction drawings;
- specification;
- building permit;
- renovation permit;
- demolition permit;
- maintenance log;
- facility-management record;
- energy certificate;
- fire-safety documents;
- structural drawings;
- geotechnical/foundation records;
- asbestos/hazardous-material survey;
- EPDs;
- manufacturer records;
- material passports;
- product IDs/serial numbers.

## L1.6 Direct inspection / sensing
- visual inspection;
- laser scanning;
- thermal imaging;
- GPR where relevant;
- material sampling;
- hardness/strength test;
- moisture test;
- corrosion assessment;
- contamination test;
- asbestos/lead/PCB screening;
- timber moisture/decay;
- connection inspection;
- selective opening-up;
- demolition audit / pre-demolition audit.

---

# DT-L2 — Identity, Integration, Semantics & Context

## L2.1 Persistent identity
- Building ID;
- system ID;
- component ID;
- material-batch ID where feasible;
- event ID;
- scenario ID;
- dataset ID;
- facility ID.

## L2.2 Spatial context
- parcel;
- block;
- neighbourhood;
- municipality;
- region/state;
- country;
- climate zone;
- urban morphology;
- accessibility;
- transport network;
- distance to recycling/reuse facilities;
- distance to secondary-material demand;
- distance to landfill;
- distance to virgin-material supplier.

## L2.3 Regionalization
- regional construction practice;
- regional material palette;
- local structural traditions;
- historical building code;
- regional archetype library;
- local material intensity;
- local LCI/EPD;
- regional electricity mix;
- regional transport mix;
- regional waste treatment shares;
- regional recovery/recycling rates;
- local landfill rate;
- local market demand;
- local reuse/recycling infrastructure.

## L2.4 Temporal alignment
- observation date;
- dataset vintage;
- valid-from;
- valid-to;
- scenario year;
- target demolition/renovation horizon;
- technology vintage;
- LCI vintage;
- electricity-grid year;
- policy/regulation year.

## L2.5 Scale/grain management
- source spatial grain;
- target spatial grain;
- coverage;
- native resolution;
- aggregation rule;
- disaggregation rule;
- interpolation rule;
- archetype assignment rule;
- overlap/matching rule;
- information-loss flag.

## L2.6 Semantic harmonization
- material naming ontology;
- component naming ontology;
- unit harmonization;
- density conversion;
- mass-volume-area conversions;
- classification-system mapping;
- IFC class mapping;
- EPD/LCI material mapping;
- duplicate/conflict resolution.

## L2.7 Provenance/versioning
- source;
- author/owner;
- method;
- version;
- timestamp;
- transformation history;
- responsible model;
- validation record;
- confidence;
- superseded value history.

---

# DT-L3 — Building State, Component & Material Reconstruction

## L3.1 Building structural system
- load-bearing masonry;
- reinforced-concrete frame;
- reinforced-concrete wall/slab;
- steel frame;
- timber frame;
- CLT/mass timber;
- hybrid;
- prefabricated panel;
- modular;
- mixed/unknown.

## L3.2 Foundation/substructure
- foundation type;
- material;
- dimensions;
- concrete grade if known;
- reinforcement ratio;
- waterproofing;
- basement wall material;
- slab-on-ground;
- piles;
- retained soil structures.

## L3.3 Primary structure
### Columns
- material;
- section;
- dimensions;
- count;
- spacing;
- connection type;
- fire protection.

### Beams
- material;
- section;
- span;
- count;
- connection type;
- composite action;
- fire protection.

### Load-bearing walls
- material;
- thickness;
- reinforcement;
- finish layers;
- openings.

### Floors/slabs
- structural type;
- thickness;
- material;
- reinforcement;
- topping/screed;
- floor finish;
- ceiling build-up.

## L3.4 External wall assembly
Layer-by-layer:
- structural substrate;
- masonry/block;
- insulation;
- cavity;
- membrane;
- render;
- cladding;
- internal lining;
- coatings;
- fixings;
- adhesives/mortar;
- thickness per layer;
- density per layer;
- area;
- mass;
- service life;
- condition;
- separability.

## L3.5 Internal wall / partition assembly
- partition type;
- studs/frame;
- boards;
- blocks;
- insulation;
- finishes;
- coatings;
- adhesives;
- services embedded;
- thickness;
- area;
- mass;
- separability.

## L3.6 Roof assembly
- structural frame;
- deck;
- insulation;
- waterproofing;
- membrane;
- covering;
- finish;
- gutters;
- fixings;
- area;
- mass;
- condition;
- remaining life.

## L3.7 Windows and glazing
- frame material;
- glazing material;
- number of panes;
- gas fill if known;
- spacer;
- hardware;
- dimensions;
- count;
- mass;
- installation year;
- condition;
- demountability;
- reusability.

## L3.8 Doors
- leaf material;
- frame;
- glazing;
- hardware;
- dimensions;
- mass;
- fire/acoustic rating;
- condition;
- demountability.

## L3.9 Finishes
- flooring;
- wall finish;
- ceiling finish;
- paint;
- tiles;
- carpet;
- resilient flooring;
- plaster;
- suspended ceiling;
- adhesives;
- coatings;
- service life.

## L3.10 MEP / services where included
- pipes;
- ducts;
- cabling;
- radiators;
- HVAC units;
- sanitary fixtures;
- electrical equipment;
- metals/plastics;
- installation year;
- expected replacement;
- hazardous substances.

## L3.11 Material quantity model
For every material/component:
- source measurement;
- area;
- volume;
- count;
- density;
- mass;
- material intensity factor;
- wastage factor;
- uncertainty distribution;
- correlation with other quantities.

## L3.12 Material identity/properties
- material family;
- subtype/grade;
- composition;
- virgin/recycled content;
- density;
- mechanical properties where relevant;
- thermal properties where relevant;
- fire properties where relevant;
- manufacturer/product;
- certification;
- EPD availability;
- batch/production year if known.

## L3.13 Material condition and quality
- visual condition;
- damage;
- cracking;
- corrosion;
- decay;
- moisture;
- deformation;
- contamination;
- coating;
- hazardous content;
- strength/residual capacity;
- dimensional tolerance;
- surface quality;
- aesthetic quality;
- certification status;
- testing status;
- unknown-condition flag.

## L3.14 Connectivity / disassembly
- connection type;
- bolt/screw/nail/weld/adhesive/mortar/cast-in-place;
- reversible vs irreversible;
- number of connection steps;
- accessibility;
- tool requirements;
- destructive removal requirement;
- interdependency with adjacent components;
- sequence constraint;
- separability;
- expected damage during removal;
- deconstruction time;
- labour intensity;
- safety constraint.

## L3.15 Material-stock outputs
- material mass by building;
- material mass by system;
- material mass by component;
- component count;
- material intensity per m² / m³;
- reusable component inventory;
- unknown/unresolved mass;
- confidence/uncertainty per record.

---

# DT-L4 — Dynamics, Service Life & Material Flow

## L4.1 Service-life parameters
- building design life;
- observed age;
- component technical life;
- material technical life;
- reference service life;
- actual service-life evidence;
- remaining service life;
- maintenance interval;
- replacement interval;
- survival distribution;
- hazard rate;
- obsolescence rate.

## L4.2 Event drivers
- physical deterioration;
- functional obsolescence;
- energy retrofit;
- change of use;
- code/regulation;
- owner decision;
- market redevelopment pressure;
- damage/disaster;
- planned demolition;
- urban redevelopment scenario.

## L4.3 Event probabilities
- maintenance probability;
- replacement probability;
- renovation probability;
- demolition probability;
- event year distribution;
- scenario-dependent event probability.

## L4.4 Stock-to-flow transformation
For each material/component:
- stock at t;
- inflow;
- retained stock;
- outflow;
- replacement outflow;
- renovation outflow;
- demolition outflow;
- loss during removal;
- captured/recovered fraction;
- residual waste.

## L4.5 Release profile
- expected release date;
- earliest/latest release;
- release distribution;
- quantity released;
- location;
- component state at release;
- expected condition;
- uncertainty.

## L4.6 Future-context variables
- future energy mix;
- future recycling technology;
- future processing efficiency;
- future transport technology;
- future market demand;
- future secondary-material standards;
- future landfill/recycling policy;
- future carbon factors;
- future material prices where used.

---

# DT-L5 — Circularity, Recovery, LCA & Decision Intelligence

## L5.1 Pathway taxonomy
For every material/component:
1. continued use;
2. repair;
3. refurbishment;
4. direct reuse;
5. component remanufacture;
6. closed-loop recycling;
7. open-loop recycling;
8. downcycling;
9. energy recovery where applicable;
10. landfill/disposal.

## L5.2 Reuse feasibility
- component integrity;
- residual capacity;
- condition;
- remaining service life;
- dimensional compatibility;
- standardization/modularity;
- disassembly feasibility;
- connection reversibility;
- removal damage;
- contamination/hazard;
- cleaning requirement;
- repair requirement;
- recertification need;
- traceability;
- documentation;
- storage requirement;
- transport;
- market demand;
- buyer match;
- timing match between supply and demand;
- regulatory acceptance.

## L5.3 Recycling feasibility
- material purity;
- mixed-material content;
- separability;
- contamination;
- sorting requirement;
- compatible recycling route;
- facility availability;
- process yield;
- recycling efficiency;
- quality retention;
- number of recycling loops;
- secondary-product specification;
- residue fraction;
- landfill fraction.

## L5.4 Open-loop vs closed-loop
### Closed-loop
- recovered quantity;
- processing yield;
- quality retention;
- substitution ratio;
- virgin material displaced;
- loop-specific losses.

### Open-loop
- destination product;
- quality transformation;
- replacement coefficient;
- alternative material displaced;
- market acceptance;
- cascading level;
- downcycling/upcycling flag.

## L5.5 Recovery and landfill
- collection rate;
- recovery rate;
- recycling rate;
- reuse rate;
- sorting loss;
- processing loss;
- contamination rejection rate;
- energy recovery share;
- landfill share;
- hazardous disposal share;
- residual inert fraction.

## L5.6 Logistics
- deconstruction site;
- sorting site;
- processing facility;
- reuse warehouse;
- destination project;
- distance;
- transport mode;
- load factor;
- backhaul;
- storage time;
- storage losses;
- facility capacity;
- facility acceptance criteria.

## L5.7 Environmental inventory per material
At minimum where data support it:
- functional unit;
- density;
- embodied energy;
- embodied water;
- embodied GHG;
- EPD/LCI source;
- process/location;
- technology;
- production year/vintage;
- recycled content;
- A1-A3 production impacts;
- A4 transport;
- A5 construction;
- B4 replacement where relevant;
- C1 deconstruction;
- C2 transport;
- C3 waste processing;
- C4 disposal;
- D benefits/loads beyond system boundary where method allows.

## L5.8 Environmental impact categories
Candidate set:
- climate change / GWP;
- primary energy;
- water use;
- resource use/depletion;
- acidification;
- eutrophication;
- photochemical ozone formation;
- ozone depletion;
- particulate matter;
- human toxicity/ecotoxicity where method/data support them;
- land use where relevant.

Do not force every study/data source to cover every category.

## L5.9 Circular scenario parameters
- target year;
- pathway enabled/disabled;
- reuse-first rule;
- closed-loop-only rule;
- open-loop allowed;
- maximum transport distance;
- minimum quality threshold;
- minimum substitution ratio;
- processing-capacity constraint;
- market-demand constraint;
- landfill restriction;
- carbon objective;
- resource-conservation objective;
- cost objective if later included;
- multi-objective weighting.

## L5.10 Environmental comparison
For each Material × Pathway × Scenario:
- gross processing burden;
- transport burden;
- deconstruction burden;
- avoided virgin production;
- avoided disposal;
- substitution credit;
- net GWP;
- net energy;
- net water;
- other LCIA indicators;
- uncertainty interval/distribution;
- sensitivity drivers.

## L5.11 Decision outputs
- technically feasible pathways;
- environmentally evaluated pathways;
- effective reusable mass;
- effective recyclable mass;
- effective substituted virgin mass;
- residual landfill mass;
- scenario-specific environmental burden;
- confidence/uncertainty;
- robustness;
- dominant uncertainty;
- value of additional information / next data request.

---

# 4. Cross-cutting uncertainty and data-quality plane

Every important parameter should, where possible, carry:

## U1 Measurement uncertainty
Sensor/survey/geometry error.

## U2 Classification uncertainty
Use/typology/material classification probabilities.

## U3 Archetype/proxy uncertainty
Error introduced by assigning generic assemblies/material intensities.

## U4 Parameter uncertainty
Density, intensity, rate, life, yield, coefficient.

## U5 Model-structure uncertainty
Choice of stock-flow, lifetime, recovery or LCA formulation.

## U6 Choice/scenario uncertainty
Open/closed loop, EoL route, system boundary, allocation, future technology.

## U7 Spatial uncertainty
Location, regional representativeness, resolution mismatch, aggregation.

## U8 Temporal uncertainty
Construction date, renovation date, service life, release year, future context.

## U9 Data-quality uncertainty
Reliability, completeness, temporal representativeness, geographical representativeness, technological representativeness.

## U10 Dependency/correlation
Dependencies among age, typology, materials, service life, quality, pathway and LCA coefficients.

## U11 Missingness
Observed missing, structurally unavailable, censored, or unreported.

For each uncertainty source track:
- original terminology;
- harmonized type;
- evidence;
- distribution/interval/confidence;
- transfer status;
- representation change;
- magnitude change if comparable;
- fate: preserved / legitimately reduced / amplified / transformed / masked-lost / unassessed;
- decision consequence.

---

# 5. Parameter-to-output filter

Every parameter must justify at least one output dependency:

```text
Material identity
Material quantity
Material quality
Release timing
Reuse feasibility
Recycling feasibility
Substitution potential
Landfill/residual fraction
Environmental consequence
Decision robustness
```

If a parameter cannot influence any of these, it is not a core parameter.

---

# 6. Target material output record

For every material/component in a selected building:

```text
Identity
→ Material / component / building ID

Stock
→ quantity + uncertainty

State
→ quality / condition / contamination + uncertainty

Release
→ event + time + quantity + uncertainty

Circular pathways
→ reuse / remanufacture / closed-loop / open-loop / recovery / landfill

Effective outcome
→ reusable mass
→ recyclable mass
→ substituted virgin mass
→ residual landfill mass

Environmental consequence
→ baseline
→ pathway-specific impacts
→ avoided burdens / added burdens
→ uncertainty

Decision
→ feasible options
→ robustness
→ dominant uncertainty
→ next most valuable data acquisition
```

---

# 7. Architecture status

This is a **research synthesis architecture v1**, not a finalized ontology or empirically validated Digital Twin standard.

Each parameter will be tagged in later iterations as:
- directly supported by reviewed literature;
- supported by multiple literature families;
- synthesis/integration proposed by us;
- optional/context dependent;
- unresolved.

The architecture will be refined as the systematic review progresses.
