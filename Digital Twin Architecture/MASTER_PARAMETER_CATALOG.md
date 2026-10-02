# Master Parameter Catalog — Building-to-Material Decision Twin

## Status and notation

This is the detailed **data architecture catalog** for the Digital Twin. It is intentionally broader than the minimum implementation so that later datasets can be mapped into a stable structure rather than redesigning the model.

Tags:
- **CORE** — required for the principal material-decision workflow;
- **COND** — required when the relevant component/material/pathway exists;
- **ADV** — advanced parameter that can materially improve inference or decision quality;
- **OPT** — optional/contextual; not required for the core material-circularity result.

Evidence:
- **SRC** — directly supported by reviewed literature/practice;
- **SYN** — synthesis across sources;
- **PROP** — proposed project architecture.

A parameter may be populated by observation, registry, BIM, archetype, model inference, inspection, testing or scenario assumption. The source must never be hidden.

---

# 0. Universal metadata attached to every parameter

Every field that enters the twin should support the following metadata wrapper.

| Field | Requirement | Meaning |
|---|---|---|
| value | CORE | scalar/category/vector/geometry |
| unit | CORE where numeric | SI/predefined unit |
| value_type | CORE | observed / inferred / dynamic / scenario |
| evidence_source_id | CORE | dataset/document/model/test identifier |
| acquisition_method | CORE | GIS/BIM/registry/image/LiDAR/survey/test/archetype/model/etc. |
| source_version | CORE | version/date of source |
| observation_time | CORE where relevant | when evidence was collected |
| valid_from / valid_to | COND | temporal validity |
| spatial_grain | CORE | component/building/block/city/region/etc. |
| spatial_coverage | CORE | area/context for which value is representative |
| regionalization_status | CORE | building-specific / local / regional / national / generic |
| uncertainty_representation | CORE | none-reported / confidence / range / SD / distribution / probability / qualitative |
| uncertainty_parameters | COND | parameters of uncertainty representation |
| source_type_original | ADV | terminology used by original source |
| source_type_harmonized | ADV | our project classification |
| variability_or_uncertainty | ADV | variability / uncertainty / mixed / unclear |
| validation_status | CORE | validated / partially validated / unvalidated / unreported |
| validation_method | COND | field check / holdout / audit / test / cross-source / expert |
| dependency_ids | ADV | upstream parameters on which this field depends |
| correlation_group | ADV | dependence group for uncertainty propagation |
| model_id / model_version | COND | inference/simulation model |
| last_updated | CORE | latest twin update |
| evidence_tier | CORE | DT data maturity tier |
| data_completeness | ADV | complete / partial / missing or quantitative score |
| responsible_actor | OPT | data owner/custodian |
| access_rights | OPT | public/restricted/confidential |

---

# 1. Site, location and spatial context

## 1.1 Identity and geolocation

| Parameter | Req. | Role | Why it matters |
|---|---|---|---|
| building_id | CORE | observed/integration | persistent identity across S1–S5 |
| external_building_ids | ADV | observed | cadastral/BIM/municipal linkage |
| address | CORE | observed | entity matching |
| parcel_id | ADV | observed | legal/spatial context |
| centroid_coordinates | CORE | observed | spatialization |
| footprint_geometry | CORE | observed | geometry/material quantity |
| footprint_area | CORE | derived | volume/GFA/component estimation |
| administrative_units | CORE | derived | regional coefficients/policy |
| coordinate_reference_system | CORE | metadata | prevents spatial mismatch |
| elevation / terrain level | ADV | observed | basement/exposure/site geometry |
| urban_rural_class | ADV | derived | regional construction/context prior |
| neighborhood_id | ADV | derived | aggregation/local demand |
| climate_zone | ADV | contextual | envelope/insulation/material context |
| exposure_zone | OPT | contextual | service life/degradation |
| seismic/wind/snow design context | OPT | contextual | structural-system/material demand |
| heritage/protection status | COND | observed | deconstruction/reuse constraints |

## 1.2 Regional circularity context

- local/regional material-cadastre ID — ADV
- region-specific MCI dataset/version — ADV
- regional construction practice/type — ADV
- regional demolition rate — ADV
- regional renovation rate — ADV
- regional landfill/recovery statistics — ADV
- regional electricity/energy mix — CORE for LCA scenario
- waste-management jurisdiction — CORE for EoL scenario
- local regulations/acceptance criteria — COND
- local secondary-material demand zone — ADV

**Evidence:** IOER material cadastres, Schiller et al. transferability work, Patouillard spatial/regionalization lessons.

---

# 2. Building identity, function, age and history

## 2.1 Building classification

| Parameter | Req. | Typical state | Notes |
|---|---|---|---|
| building_use_primary | CORE | observed/inferred | residential/office/industrial/etc. |
| building_use_secondary | COND | observed/inferred | mixed-use fractions |
| occupancy/use intensity | ADV | dynamic | may affect renovation/operation |
| residential subtype | COND | inferred | SFH/MFH/apartment/etc. |
| non_residential_subtype | COND | inferred | office/factory/storage/retail/etc. |
| archetype_id | CORE | inferred | links building to material prior |
| archetype_probability | CORE if inferred | inferred | do not keep only argmax |
| typology_source | CORE | metadata | local/regional/generic |

## 2.2 Construction age and history

- construction_year exact — CORE if known
- construction_year_interval — CORE when exact unknown
- construction_period_class — CORE
- construction_year_probability_distribution — ADV
- original_completion_date — ADV
- major_extension_year(s) — COND
- vertical_extension / added floors year — COND
- change_of_use history — COND
- major_renovation_year(s) — CORE when known
- façade renovation year — COND
- roof renovation year — COND
- window replacement year — COND
- insulation retrofit year — COND
- structural intervention year — COND
- MEP renewal year — OPT/COND
- demolition/partial-demolition history — COND
- documentation completeness of history — CORE

**Evidence:** IOER age-based MCIs, German archetype literature, service-life and material-intensity studies.

---

# 3. Building geometry and morphology

## 3.1 Whole-building geometry

- building footprint polygon — CORE
- footprint area — CORE
- footprint perimeter — CORE
- perimeter-to-area ratio — ADV
- building length — ADV
- building width — ADV
- building height — CORE
- eave height — ADV
- ridge height — COND
- number of above-ground floors — CORE
- number of below-ground floors — ADV
- average floor-to-floor height — CORE/ADV
- gross floor area (GFA) — CORE
- net floor area — ADV
- gross internal area — ADV
- building volume — CORE
- heated/cooled volume — OPT
- basement area/volume — ADV
- building shape class — ADV
- roof shape — CORE/ADV
- roof slope — ADV
- roof area — CORE/ADV
- façade area by orientation — ADV
- external wall area — CORE
- party-wall/shared-wall area — ADV
- window area — CORE/ADV
- window-to-wall ratio total — CORE/ADV
- WWR by orientation — ADV
- external door area/count — ADV
- internal partition length/area — ADV
- floor/slab area by level — CORE/ADV
- ceiling area — ADV
- foundation footprint/area — ADV

## 3.2 Geometry uncertainty

- footprint measurement error
- height error
- floor-count confidence
- inferred GFA error
- inferred façade/window area error
- missing/occluded geometry flag
- geometry source resolution
- LoD / model detail level

**Evidence:** Heeren & Hellweg; non-residential LCI archetype literature; IOER 3D material cadastre; parametric archetype studies.

---

# 4. Structural system and load-bearing architecture

## 4.1 Whole-building structural classification

- primary structural system — CORE
  - reinforced concrete frame
  - concrete wall/slab
  - steel frame
  - timber frame
  - mass timber
  - load-bearing masonry
  - mixed/hybrid
  - other/unknown
- structural-system probability — CORE when inferred
- lateral-load-resisting system — ADV
- foundation system — ADV
- basement structural system — ADV
- floor/slab structural system — CORE/ADV
- roof structural system — ADV
- structural grid/span — ADV
- typical bay dimensions — ADV
- load-bearing wall layout — ADV
- column dimensions/grid — ADV
- beam dimensions — ADV
- slab thickness — ADV
- structural redundancy/adaptability — OPT
- design standard/code era — ADV
- original design load class — OPT/COND

## 4.2 Reuse-specific structural data

- member/component geometry — COND
- section/profile designation — COND
- material grade — COND
- nominal strength — COND
- measured strength — ADV/COND
- reinforcement layout — ADV for RC reuse
- prestress/post-tension status — COND
- corrosion state — COND
- deformation/damage — COND
- fire exposure history — COND
- fatigue/load history — ADV for steel
- section loss — COND
- structural test results — ADV
- residual capacity estimate — ADV
- certification/traceability — COND
- intended second-use class — COND

**Evidence:** material-intensity predictor studies; reuse/quality-assurance literature; steel/reinforced-concrete reuse studies.

---

# 5. Building-component hierarchy

Every component is a separate entity with geometry, material layers, age, connection, condition and service life.

## 5.1 Required component classes

### Substructure
- foundation
- piles
- footings
- ground beams
- basement walls
- basement slab
- retaining walls

### Structural frame
- columns
- beams
- load-bearing walls
- cores
- bracing
- slabs/decks
- structural roof

### Envelope
- external wall/facade
- cladding
- backing wall
- cavity
- air/vapor/water membranes
- exterior insulation
- windows
- curtain wall
- external doors
- shutters/shading
- roof covering
- roof insulation
- gutters/drainage

### Interior
- internal load-bearing walls
- partitions
- linings
- ceilings/suspended ceilings
- floor finishes
- wall finishes
- internal doors
- stairs/ramps
- balustrades

### Services / MEP — conditional but architecture-ready
- HVAC plant
- ductwork
- pipes
- electrical cabling
- lighting
- sanitary fixtures
- lifts/elevators
- PV/solar systems
- batteries/other equipment

### Site/external works — optional
- paving
- external walls/fences
- drainage
- ancillary structures

## 5.2 Universal component parameters

For each component:
- component_id — CORE
- parent_building_id — CORE
- component_class/subclass — CORE
- storey/location — CORE
- 3D/2D geometry — CORE/ADV
- count — COND
- length / width / height — COND
- area — CORE when area-based
- thickness — CORE/ADV
- volume — derived
- unit mass — COND
- total mass — CORE/derived
- installation year — ADV
- last replacement year — COND
- condition grade — ADV
- accessibility — ADV
- connection_to_parent — ADV
- disassembly sequence dependency — ADV
- service-life distribution — ADV
- remaining-service-life distribution — ADV
- material layer list — CORE

---

# 6. Assembly and layer composition

Each assembly must allow ordered material layers rather than one single material label.

## 6.1 Exterior wall / façade

- façade system type — CORE/ADV
- structural backing material — CORE
- cladding material — CORE/ADV
- cladding thickness — ADV
- insulation material — CORE/ADV
- insulation thickness — ADV
- cavity thickness — ADV
- membrane layers — ADV
- render/plaster type — ADV
- mortar type — ADV
- fixings/anchors — ADV
- adhesive/bonding type — ADV
- coating/paint — ADV
- wall total thickness — ADV
- façade replacement/renovation year — COND
- façade condition — ADV
- surface contamination/hazard — COND

## 6.2 Interior wall / partition

- partition system type — CORE/ADV
- studs/frame material — ADV
- board/panel material — CORE/ADV
- infill/insulation — ADV
- plaster/render/finish — ADV
- connection type to floor/ceiling — ADV
- demountability — ADV
- wall thickness — ADV
- area/length — ADV

## 6.3 Floor / slab

- structural slab material — CORE
- slab thickness — ADV
- screed material/thickness — ADV
- floor finish material/thickness — ADV
- acoustic/thermal insulation — ADV
- raised-floor system — COND
- ceiling layer below — ADV
- adhesives/bonding — ADV

## 6.4 Roof

- roof structural material — CORE/ADV
- roof covering — CORE
- waterproofing membrane — ADV
- insulation material/thickness — ADV
- vapor layer — ADV
- boarding/deck — ADV
- roof slope — ADV
- drainage components — OPT
- roof condition — ADV
- replacement year — COND

## 6.5 Windows and glazed façade

- window_id/type — ADV
- frame material — CORE/ADV
- glazing type — CORE/ADV
- glazing layers — ADV
- glass thickness/area — ADV
- spacer/sealant — OPT
- opening mechanism — OPT
- U-value / thermal performance — OPT
- installation/replacement year — ADV
- condition — ADV
- demountability — ADV

## 6.6 Doors

- external/internal — ADV
- leaf material — ADV
- frame material — ADV
- glazing fraction — OPT
- hardware metal — OPT
- dimensions/count — ADV
- fire/security classification — OPT
- installation year/condition — ADV

**Reason:** layer-level composition controls both quantity and whether materials can be separated into clean flows.

---

# 7. Material identity, physical properties and provenance

## 7.1 Material classification

- material_id — CORE
- material_group — CORE
- material_subgroup — CORE
- product/material name — CORE
- material standard/code — ADV
- manufacturer/product ID — COND
- material origin — ADV
- production region/country — ADV
- virgin/recycled/reused origin — ADV
- recycled content % — ADV
- renewable content % — ADV
- bio-based content % — ADV
- secondary-material content % — ADV
- raw-material category — ADV
- waste-code / EWC mapping — ADV
- product/component classification code — OPT
- material-passport/DPP identifier — COND

## 7.2 Minimum material groups architecture must handle

- concrete
- reinforced concrete
- lightweight concrete
- autoclaved aerated concrete
- brick/clay masonry
- sand-lime brick
- natural stone
- mortar/render/plaster
- cement/screed
- gypsum/gypsum board
- ceramic/tiles
- glass
- mineral wool
- EPS
- XPS
- PUR/PIR and other polymer insulation
- cellulose/fibre insulation
- timber solid wood
- engineered wood
- steel
- stainless steel
- aluminium
- copper
- zinc/lead/other non-ferrous metals
- plastics/PVC/PE/PP/etc.
- bitumen/asphalt
- roofing membranes
- paints/coatings
- sealants/adhesives
- flooring materials
- carpet/textiles
- composite panels
- fibre cement
- asbestos-containing materials — hazard-controlled
- other renewable materials
- unknown/mixed materials

This list is an architecture taxonomy, not a claim that every source uses identical categories.

## 7.3 Physical and functional properties

- density — CORE for conversion
- bulk density — COND
- moisture content — ADV
- porosity — OPT
- thickness — CORE/ADV
- dimensions/product format — ADV
- mass — CORE
- volume — CORE/derived
- area — COND
- count — COND
- compressive strength — COND
- tensile/yield strength — COND
- modulus/stiffness — OPT/COND
- reinforcement ratio — COND
- thermal conductivity — OPT
- thermal resistance — OPT
- fire rating/performance — COND
- acoustic performance — OPT
- durability class — ADV
- exposure class — ADV
- surface treatment/coating — ADV
- functional role — CORE/ADV

---

# 8. Material quantity and stock inference

For each material/component batch:

- observed_quantity — COND
- inferred_quantity_mean — CORE if inferred
- inferred_quantity_distribution — ADV
- quantity_unit — CORE
- material_intensity_value — CORE if MCI-based
- material_intensity_unit — CORE
- MCI_distribution — ADV
- MCI_building_type — CORE
- MCI_age_class — ADV
- MCI_region — CORE
- MCI_component_scope — CORE
- MCI_sample_size — ADV
- MCI_source_method — CORE
- MCI_transferability_status — ADV
- geometry_to_quantity_rule — CORE
- density_conversion_source — CORE
- gross/net adjustment factor — COND
- waste/over-order allowance for original construction — OPT
- stock_total_by_material — CORE
- stock_total_by_component — CORE
- stock_total_building — CORE
- quantity_validation_measurement — ADV
- mass-balance check — ADV

---

# 9. Material quality, condition, damage and hazardous content

## 9.1 Condition/quality

- condition_grade — CORE for reuse analysis
- quality_grade — CORE/ADV
- inspection_date — CORE when inspected
- inspection_method — CORE
- visual_damage_type — ADV
- damage_severity — ADV
- cracking — COND
- spalling — COND
- corrosion — COND
- rot/biological degradation — COND
- moisture damage — COND
- deformation — COND
- wear/abrasion — COND
- fire damage — COND
- chemical attack — COND
- fatigue history — COND
- remaining performance estimate — ADV
- test_required_for_reuse — ADV
- test_result — COND
- recertification_required — COND
- certification_possible — COND

## 9.2 Hazard/contamination

- hazardous_material_flag — CORE/COND
- asbestos_risk — COND
- lead/heavy-metal risk — COND
- PCB risk — COND
- PAH/bituminous contamination risk — COND
- treated timber/biocide risk — COND
- fire-retardant/additive concern — COND
- coating contamination — COND
- mixed-material contamination — COND
- chemical incompatibility — ADV
- contaminant concentration/test — ADV
- pollutant evidence source — CORE
- hazardous handling requirement — COND
- hazardous disposal requirement — COND

**Architecture rule:** hazardous/contaminated material cannot be treated as a generic recyclable mass.

---

# 10. Connection, accessibility, disassembly and separability

For every component/material interface:

- connection_id — ADV
- connected_entities — ADV
- connection_type — CORE/ADV
  - loose/gravity
  - click/interlocking
  - bolted
  - screwed
  - plugged
  - nailed/pinned
  - clipped
  - mortared
  - cement-bonded
  - glued/adhesive
  - welded
  - cast-in
  - composite/irreversible
  - unknown
- reversible_connection_flag — ADV
- fastener_material/type — ADV
- accessibility — CORE/ADV
- disassembly_tool_requirement — ADV
- disassembly_skill_requirement — OPT
- estimated disassembly effort/time — ADV
- selective_deconstruction_feasibility — ADV
- expected removal damage — CORE/ADV
- damage_probability — ADV
- sequence_dependency — ADV
- material_separability — CORE/ADV
- mono-material/purity potential — ADV
- attachment/contamination after separation — ADV
- sorting requirement — ADV
- deconstruction_space_requirement — OPT
- storage_requirement — OPT
- safety constraint — COND

**Evidence:** DGNB, DfD reviews, component-reuse systematic review.

---

# 11. Service life, maintenance, renovation and event timing

## 11.1 Lifetimes

- building_reference_study_period — CORE
- building_expected_lifetime — ADV
- component_reference_service_life — CORE/ADV
- material_service_life — ADV
- service_life_distribution_type — ADV
- distribution_parameters — ADV
- age_since_installation — ADV
- remaining_service_life — ADV
- remaining_service_life_distribution — ADV
- maintenance_interval — COND
- replacement_interval — COND
- number_of_expected_replacements — derived
- degradation_rate/state transition — ADV

## 11.2 Event model

- event_id — CORE
- event_type — CORE
  - maintenance
  - repair
  - replacement
  - renovation
  - retrofit
  - change of use
  - extension
  - partial demolition
  - full demolition
- event_time/year — CORE
- event_time_distribution — ADV
- event_probability — ADV
- trigger — ADV
  - technical failure
  - functional obsolescence
  - energy retrofit
  - policy
  - market/redevelopment
  - user decision
- affected_component_ids — CORE
- affected_material_ids — CORE
- released_quantity — CORE
- release_quantity_distribution — ADV
- retained_in_building_quantity — ADV
- newly_installed_quantity — ADV
- event scenario ID — CORE

---

# 12. Material release, collection and pre-demolition audit

- pre_demolition_audit_status — ADV/CORE near EoL
- audit_date — COND
- documentation_review_complete — COND
- site_inspection_complete — COND
- sampling/testing_complete — COND
- hazardous-material survey complete — COND
- component inventory verified — COND
- material quantities verified — COND
- reusable component candidates — COND
- recyclable material candidates — COND
- demolition_method — CORE scenario
- selective_deconstruction_flag — CORE scenario
- source_separation_level — ADV
- collection_efficiency — ADV
- deconstruction_recovery_yield — CORE/ADV
- breakage_loss — ADV
- sorting_loss — ADV
- contamination_gain during demolition — ADV
- mixed-waste fraction — CORE/ADV
- reusable component yield — CORE/ADV
- recyclable feedstock yield — CORE/ADV

---

# 13. Circularity pathway model

A pathway is a scenario object attached to a **specific released material/component batch**.

## 13.1 Pathway identity

- pathway_id — CORE
- material_batch_id — CORE
- pathway_type — CORE
  - direct reuse
  - preparation for reuse
  - remanufacture/refurbish
  - closed-loop recycling
  - open-loop recycling
  - downcycling
  - other material recovery
  - energy recovery
  - backfilling
  - landfill
  - hazardous disposal
- loop_type — CORE where recycling
- pathway_status — CORE
  - technically feasible
  - conditionally feasible
  - infeasible
  - unknown
- infeasibility_reason — COND

## 13.2 Direct reuse

- reusable_quantity_before_losses — CORE
- deconstruction_damage_loss — ADV
- quality_pass_fraction — CORE/ADV
- dimensional_match — ADV
- functional_match — ADV
- structural_capacity_match — COND
- regulatory/certification pass — COND
- cleaning/repair need — ADV
- refurbishment_process — COND
- preparation_for_reuse_yield — ADV
- final_reusable_quantity — CORE
- reuse_destination/use class — ADV

## 13.3 Closed-loop recycling

- process_chain_id — CORE
- feedstock acceptance criteria — ADV
- collection_yield — ADV
- sorting_yield — ADV
- processing_yield — CORE
- quality_after_processing — CORE/ADV
- recycled_product_output — CORE
- closed_loop_technical_flag — CORE
- substitution_ratio — CORE
- substitution_ratio_distribution — ADV
- virgin_material_displaced — CORE/derived
- quality limiting factor — ADV

## 13.4 Open-loop recycling

- output_product/material — CORE
- alternative_application — CORE
- processing_yield — CORE
- output_quality — ADV
- downcycling/upcycling classification — ADV
- replacement_coefficient — CORE
- replacement_coefficient_distribution — ADV
- displaced_product/material — CORE
- functional_equivalence_basis — ADV

## 13.5 Disposal/recovery

- energy_recovery_fraction — COND
- backfill_fraction — COND
- landfill_fraction — CORE
- hazardous_disposal_fraction — COND
- landfill_type — COND
- treatment_process — COND
- residual_fraction_after_processing — CORE

**Mass-balance requirement:** pathway fractions/flows must reconcile with released mass, allowing explicit processing losses and stored inventory.

---

# 14. Recycling/process facility and logistics

## 14.1 Facility

- facility_id — ADV
- facility_type — ADV
- coordinates — ADV
- accepted_materials — ADV
- acceptance_quality_thresholds — ADV
- contamination_limit — ADV
- process technology — ADV
- nominal capacity — ADV
- available capacity at target time — OPT/ADV
- process yield — CORE/ADV
- output product — ADV
- output quality/grade — ADV
- energy consumption — ADV
- fuel/electricity mix — ADV
- water consumption — OPT/ADV
- process emissions — ADV
- waste/residue rate — ADV
- permit/regulatory status — OPT

## 14.2 Logistics

- origin building coordinates — CORE
- destination/facility coordinates — ADV
- route distance — CORE/ADV
- straight-line distance — OPT
- transport mode — CORE for LCA
- vehicle type/capacity — ADV
- load factor — ADV
- backhaul assumption — OPT
- number of trips — derived
- transport energy/emission factor — CORE
- intermediate storage location — OPT
- storage time — OPT
- storage loss/damage — OPT
- deconstruction-site handling — ADV
- loading/unloading process — OPT

---

# 15. Secondary-material/product demand and market matching

These are **conditional decision-realism fields**, not intrinsic material properties.

- demand_location — ADV
- demand_time/window — ADV
- requested_material/product — ADV
- requested_quantity — ADV
- required_quality/grade — ADV
- required_dimensions/specification — ADV
- acceptable provenance/certification — ADV
- max_transport_distance — ADV/scenario
- demand-supply temporal match — ADV
- quantity match — ADV
- quality match — ADV
- dimensional match — ADV
- market availability — ADV
- secondary-material availability from competitors — OPT
- storage buffer allowed — OPT
- price virgin material — OPT
- price secondary material — OPT
- deconstruction/processing cost — OPT
- market confidence/uncertainty — ADV

**Architecture rule:** technical recoverability is not the same as actual circular use; demand and timing can limit realized substitution.

---

# 16. LCA and environmental-impact module

## 16.1 Study/model definition

- lca_model_id — CORE
- functional_unit — CORE
- reference_study_period — CORE
- system_boundary — CORE
- LCI_method — CORE
  - process
  - input-output
  - hybrid
- LCI_database — CORE
- database_version — CORE
- geography — CORE
- reference_year — CORE
- data_quality/completeness — ADV
- allocation_method — CORE/ADV
- recycling_allocation_method — CORE/ADV
- substitution/avoided-burden method — CORE/ADV
- biogenic_carbon_method — COND
- carbon_storage_timing — COND
- characterization_method/version — CORE
- cut_off_rules — ADV
- uncertainty method — ADV

## 16.2 Material/product environmental coefficients

For each material/process:
- embodied GHG factor — CORE
- embodied primary energy factor — ADV
- embodied water factor — ADV
- resource/depletion indicator(s) — ADV
- acidification — OPT/ADV
- eutrophication — OPT/ADV
- photochemical ozone formation — OPT/ADV
- ozone depletion — OPT
- particulate matter — OPT/ADV
- toxicity/ecotoxicity — OPT/ADV
- land use — OPT/ADV
- waste indicators — ADV
- factor uncertainty — ADV
- factor source/provenance — CORE

## 16.3 Lifecycle modules / process stages

Architecture should be able to represent:
- A1 raw material supply
- A2 transport
- A3 manufacturing
- A4 transport to site
- A5 construction/installation
- B2 maintenance
- B3 repair
- B4 replacement
- B5 refurbishment
- C1 deconstruction/demolition
- C2 transport
- C3 waste processing
- C4 disposal
- D reuse/recovery/recycling potential beyond system boundary

Not every study uses every module; absence must be explicit.

## 16.4 Scenario environmental outputs

- baseline impact — CORE
- pathway impact — CORE
- processing impact — CORE
- transport impact — CORE
- deconstruction impact — ADV
- disposal impact — CORE
- avoided virgin production — CORE when substitution applied
- Module-D/benefit credit — COND
- net scenario impact — CORE
- impact difference vs baseline — CORE
- impact uncertainty — CORE/ADV
- impact contribution by material — ADV
- uncertainty contribution by material/source — ADV

**Evidence:** Crawford EPiC/hybrid LCI; Hoxha uncertainty; Level(s); Hossain & Ng circular LCA.

---

# 17. User/scenario controls

The user must be able to alter assumptions without overwriting physical building evidence.

- scenario_id — CORE
- scenario_name — CORE
- target_year — CORE
- assessment_horizon — CORE
- intervention type — CORE
- demolition/renovation event selection — CORE
- allowed pathways — CORE
- direct reuse allowed? — CORE
- closed-loop allowed? — CORE
- open-loop allowed? — CORE
- energy recovery allowed? — CORE
- landfill allowed/limit — CORE
- max transport radius — ADV
- facility set — ADV
- future technology assumption — ADV
- future energy mix — ADV
- future market/demand assumption — ADV
- regulatory scenario — ADV
- material-quality threshold — ADV
- minimum confidence/robustness threshold — ADV
- optimization objective — ADV
  - minimize GHG
  - minimize virgin resource use
  - minimize landfill
  - maximize reuse
  - multi-objective
- scenario probability/weight — ADV
- user-defined constraints — ADV
- baseline scenario — CORE

---

# 18. Decision-ready outputs

For each **material/component batch**:

## Stock
- material identity
- location in building
- quantity distribution
- quality/condition
- provenance
- data completeness

## Release
- event
- release-time distribution
- released-quantity distribution

## Circularity
- technically recoverable mass
- directly reusable mass
- closed-loop recyclable mass
- open-loop recyclable mass
- other recovery mass
- landfill/residual mass
- hazardous disposal mass
- process losses

## Effective substitution
- substitution ratio / replacement coefficient
- effective virgin material displaced
- substituted product/material
- functional-equivalence basis

## Environmental
- baseline burden
- pathway burden
- avoided burden
- net difference
- indicators
- system boundary/method

## Uncertainty
- output distribution/range
- inherited uncertainty sources
- newly introduced uncertainty
- dominant uncertainty contributor(s)
- impact hotspot vs uncertainty hotspot
- decision robustness
- missing evidence
- recommended next data acquisition

---

# 19. Uncertainty parameters by architectural stage

## U1 Observation
- measurement error
- sensor/image resolution
- occlusion
- classification probability
- missing records
- geolocation error

## U2 Identity/context
- entity-linkage confidence
- temporal mismatch
- regional representativeness
- scale mismatch
- schema/harmonization ambiguity

## U3 Material inference
- archetype probability
- MCI variance
- material-class probability
- density uncertainty
- hidden-layer uncertainty
- renovation-history uncertainty

## U4 Dynamics
- service-life distribution
- demolition probability
- renovation-event probability
- replacement interval
- future technology/context

## U5 Quality/recovery
- condition assessment
- contamination probability
- separability
- damage during deconstruction
- recovery/sorting/processing yield

## U6 Circular scenario
- pathway choice
- facility availability
- market demand
- transport distance
- future regulation

## U7 Substitution
- functional equivalence
- substitution ratio
- replacement coefficient
- output quality

## U8 LCA
- foreground quantity
- LCI coefficient
- database geography/year
- system boundary/truncation
- allocation
- characterization
- future energy mix

---

# 20. Data maturity / evidence tiers

This is a **project synthesis**, designed so the same schema can operate with sparse or rich evidence.

### Tier 0 — Regional/archetype prior
Only building type/region or generic stock information.

### Tier 1 — Geospatial/GeoAI evidence
Footprint, height, floors, roof/façade cues, function/age predictions.

### Tier 2 — Administrative/building records
Construction year/use, permits, renovation records, cadastral attributes.

### Tier 3 — Plans/BIM/component documentation
Assemblies, dimensions, bill of quantities, product/material data.

### Tier 4 — Inspection / pre-demolition audit / testing
Verified materials, condition, contamination, connection/separability, test results.

### Tier 5 — Dynamic/operational update
Current event/state information, replacement history, sensor/maintenance/asset-management records where relevant.

**Rule:** higher tier does not automatically mean lower uncertainty; it means more direct/specific evidence. Reduction must be demonstrated.

---

# 21. Parameter inclusion logic

A new parameter enters the **core** architecture only if it can materially affect one or more of:

1. material identity;
2. quantity;
3. quality/condition;
4. release timing;
5. recovery/separation;
6. reuse/recycling feasibility;
7. substitution/replacement;
8. environmental consequence;
9. uncertainty/decision robustness.

This catalog is intentionally extensible. New literature should map into this structure before new top-level categories are invented.
