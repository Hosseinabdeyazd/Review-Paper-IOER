
# Material-Specific Circularity Templates

## Purpose

The master schema is generic, but circularity is material-specific. This file defines the first working parameter templates for major construction material families.

These are not final decision rules. They identify the information the Digital Twin should be able to store and the material-specific gates that literature indicates are relevant.

---

# 0. Common minimum record for every material

Mandatory target fields:
- material_id
- component_id
- material family/subtype
- quantity + unit + uncertainty
- location in building
- installation/construction period
- current condition
- contamination/hazard status
- connection/separability
- expected release event/time
- release uncertainty
- salvage/recovery yield
- possible circular pathways
- pathway-specific quality requirement
- substitution/replacement parameter
- transport/facility/demand context
- LCA dataset + geographic/time validity
- environmental consequence distribution
- evidence/provenance

---

# 1. Concrete / reinforced concrete / precast concrete

## Identity / stock
- concrete type
- strength class if known
- density
- component type: slab/beam/column/wall/foundation/precast panel
- component dimensions
- volume/mass
- reinforcement amount/ratio
- reinforcement grade
- prestressing status
- casting/prefabrication method
- age

## Condition / quality
- cracks
- spalling
- corrosion
- carbonation/chloride exposure where relevant
- fire exposure
- deformation
- previous repair
- compressive-strength evidence
- residual durability
- reinforcement condition
- damage class
- recertification/testing

## Disassembly
- monolithic vs precast
- connection type
- welded/bolted/grouted/cast connection
- accessibility
- lifting points
- component mass
- saw-cutting requirement
- expected damage
- salvage yield
- storage/transport geometry

## Pathways
### Direct component reuse
Needs:
- intact component
- acceptable geometry
- adequate residual strength/durability
- connection/deconstruction feasibility
- design/load compatibility
- certification/engineering verification
- demand match

### Closed-loop / high-quality recycling
Possible outputs:
- recycled concrete aggregate
- recycled cementitious fraction where technology permits

Track:
- contamination
- aggregate quality
- processing yield
- substitution ratio
- permitted replacement rate

### Open-loop/downcycling
Possible:
- road base/fill/other aggregate applications

Track replacement coefficient rather than assuming 1:1 displacement.

---

# 2. Clay brick / masonry

## Identity
- brick type
- solid/hollow/perforated
- dimensions
- manufacturing period
- fired-clay type
- density
- masonry system
- mortar type
- mortar age

## Condition / quality
- visible damage
- cracks/chipping
- freeze-thaw/weathering
- efflorescence
- contamination
- compressive strength
- water absorption where relevant
- aesthetic condition

## Critical reuse gate
Mortar bond/removability is a major barrier.

Track:
- mortar type
- bond strength proxy
- removable mortar fraction
- separation method
- brick damage during separation
- reclamation yield
- cleaning effort

## Pathways
- direct brick reuse;
- reclaimed brick after cleaning;
- crushed brick aggregate;
- open-loop use in other mineral products;
- disposal.

Outputs:
- intact reusable brick count/mass;
- cleaned reusable yield;
- crushed fraction;
- substitution/replacement coefficient;
- environmental burdens of separation/cleaning.

---

# 3. Structural steel

## Identity
- section/profile type
- section dimensions
- length
- steel grade
- manufacturer if known
- production year
- mass
- member function
- connection details
- coating/fire protection

## Documentation
- original certificates
- drawings
- inspection certificates
- traceability marks
- weld history
- modification history

Documentation is a critical reuse factor.

## Condition / testing
- corrosion/loss of section
- deformation
- fatigue exposure
- fire exposure
- holes/cuts
- weld condition
- yield strength
- tensile strength
- ductility
- chemical composition
- weldability
- coating/hazard status

## Disassembly
- bolted/welded/cast connection
- accessibility
- cutting required
- damage probability
- retained length
- handling/lifting
- salvage yield

## Pathways
### Direct structural reuse
Needs:
- geometry/section compatibility
- adequate mechanical properties
- documentation/recertification
- condition acceptance
- connection/removal feasibility
- receiver demand

### Remanufacture
- trimming
- new holes
- cleaning
- recoating
- recertification

### Recycling
- scrap collection
- alloy/contamination
- remelting route
- recycling yield
- substitution of primary steel

---

# 4. Timber / engineered wood

## Identity
- species
- product type: solid timber/CLT/glulam/LVL/board
- dimensions
- density
- structural grade if known
- manufacturing date
- treatment/coating
- adhesive system for engineered products

## Condition / quality
- moisture content
- rot
- fungal/biological attack
- insect damage
- cracks/checks
- warping
- connector damage
- fire/charring
- chemical/preservative treatment
- density
- visual grade
- dynamic modulus / non-destructive test
- residual strength
- residual service life

## Disassembly
- connection type
- screws/bolts/nails/adhesive
- accessibility
- damage during removal
- retained dimensions
- salvage yield

## Pathways
- direct structural reuse;
- non-structural reuse;
- remanufacture into smaller/engineered products;
- panel/fibre applications;
- energy recovery;
- disposal.

Track cascading value loss and avoid calling lower-value wood use "closed loop" without a functional definition.

---

# 5. Window systems / flat glass / insulating glass units

## Component identity
- window_id
- glazing configuration
- pane count
- pane thickness
- glass type
- heat treatment
- coatings
- low-e coating
- spacer type
- gas fill if known
- sealant
- frame material
- frame dimensions
- hardware
- installation year
- U-value
- dimensions

## Condition / quality
- scratches
- edge damage
- seal failure
- condensation
- discoloration
- coating condition
- surface damage
- bending strength if tested
- optical quality
- gas/seal performance
- residual service life

## Disassembly
- glazing bead / putty / adhesive
- reversible frame connection
- ability to remove IGU intact
- labor/time
- breakage risk
- deglazing yield

## Pathways
- whole-window reuse;
- IGU reuse;
- glass-pane reuse;
- remanufacture;
- cullet recycling;
- open-loop glass applications;
- frame recycling.

Reuse/remanufacture and recycling are distinct because recycling melts the glass while reuse retains component/product identity.

---

# 6. Aluminum

## Identity
- component/application
- alloy if known
- profile type
- mass
- coating/anodizing
- thermal-break material
- connection
- manufacturing source

## Quality / circularity
- alloy purity
- mixed-alloy contamination
- attached plastics/thermal breaks
- paint/coating
- corrosion
- deformation
- separability

## Pathways
- component/profile reuse;
- remanufacturing;
- alloy-preserving closed-loop recycling;
- mixed-scrap/open-loop recycling.

Track alloy quality and sorting because mass recovery alone does not equal functional substitution.

---

# 7. Gypsum / plasterboard

## Identity
- gypsum product type
- plasterboard type
- thickness
- mass
- paper fraction
- additives
- finishing/plaster
- installation system

## Quality / contamination
- gypsum purity
- moisture
- mixed waste
- screws/metal
- insulation residues
- paint/finish
- hazardous contamination

## Critical circularity conditions
- source separation/on-site segregation
- waste acceptance criteria
- recycled-gypsum quality criteria
- dedicated recycling technology

## Pathways
- board/component reuse where practical;
- gypsum recycling;
- other mineral application;
- landfill.

Gypsum separated poorly from other mineral waste can contaminate concrete recycling streams.

---

# 8. Insulation materials

## Identity
- type: mineral wool/EPS/XPS/PUR/PIR/cellulose/wood fibre/other
- manufacturer/product
- density
- thickness
- area/volume/mass
- binder/additives
- flame retardants
- blowing agents where relevant
- installation method

## Quality
- moisture
- compression/deformation
- contamination
- biological damage
- thermal performance
- dimensional stability
- adhesive contamination

## Disassembly
- loose/mechanical/adhesive fixation
- accessibility
- intact-removal potential
- contamination from adjacent layers

## Pathways
- direct reuse where quality permits;
- same-material recycling where process exists;
- open-loop material use;
- energy recovery for suitable polymers;
- landfill.

Material-specific facility acceptance criteria are essential.

---

# 9. Plastics / PVC / membranes

## Identity
- polymer type
- product/application
- mass
- additives/plasticizers
- flame retardants
- reinforcement
- composite layers
- colour
- production age

## Quality
- UV/thermal ageing
- brittleness
- contamination
- hazardous additives
- mixed-polymer status

## Pathways
- component reuse;
- mechanical recycling;
- feedstock/chemical recycling where applicable;
- open-loop recycling;
- energy recovery;
- disposal.

Polymer identity and additive history are central to quality and safety.

---

# 10. Copper, cables, pipes, and MEP metals

## Identity
- metal/alloy
- cable/pipe/equipment function
- diameter/cross-section
- mass
- insulation/sheathing
- fittings
- connection
- installation date

## Condition
- corrosion
- deformation
- contamination
- remaining function
- certification

## Pathways
- equipment/component reuse;
- pipe/cable reuse where technically acceptable;
- metal recycling;
- separation of mixed materials.

Track high-value metal recovery separately from total MEP mass.

---

# 11. Finishes, tiles, sanitary products, doors, and fixtures

These should be modeled as components when reuse is plausible.

Fields:
- component type
- dimensions/count
- manufacturer/product
- connection
- accessibility
- condition
- aesthetic quality
- contamination
- service history
- remaining life
- matching demand
- packaging/handling

Potential pathways:
- direct reuse;
- repair/refurbish;
- material recycling;
- disposal.

---

# 12. Material-specific uncertainty rule

For every material family, the system must identify:

1. quantity uncertainty;
2. identity/composition uncertainty;
3. quality/condition uncertainty;
4. disassembly/salvage uncertainty;
5. timing uncertainty;
6. process/recovery uncertainty;
7. substitution uncertainty;
8. LCA uncertainty.

Different materials are expected to have different bottlenecks.

Example:
- steel may be quantity-known but certification/condition-uncertain;
- brick may be stock-known but mortar-removability/salvage-uncertain;
- glass may be quantity-known but surface/strength/seal/removal-uncertain;
- insulation may be identity/contamination/recycling-route uncertain.

The architecture therefore does not use one universal circularity probability model for all materials.
