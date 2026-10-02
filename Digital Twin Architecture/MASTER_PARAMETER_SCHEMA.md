
# Master Parameter Schema — Decision-Ready Building Material Twin

## Purpose

This is the master data architecture for the project.

The user selects a building. The Digital Twin must ultimately return a material-by-material profile containing:

- identity and location of each material/component;
- current quantity and quality;
- future release timing and quantity;
- feasible reuse/recycling/recovery/disposal pathways;
- open-loop and closed-loop scenarios;
- effective substitution of primary materials/products;
- environmental consequences;
- uncertainty and decision robustness;
- the dominant uncertainty sources and the most useful next data-acquisition step.

Every populated parameter should carry, where applicable:

- parameter ID;
- entity ID;
- value/category/distribution;
- unit;
- source;
- acquisition/inference method;
- reference date;
- spatial grain and geographic validity;
- uncertainty representation;
- validation status;
- evidence status;
- data/model version.

The schema is intentionally broad. Individual studies or implementations may populate only a subset.

---

# Domain 01 — Building identity and administrative metadata

## Identity
- building_id
- external_building_ids
- parcel_id
- address
- latitude
- longitude
- building_polygon_id
- coordinate_reference_system
- city
- municipality
- district
- region
- country

## Legal / administrative status
- building_status
- ownership_type
- property_management_entity
- heritage_status
- protected_building_status
- building_permit_id
- demolition_permit_status
- renovation_permit_status
- occupancy_permit_status

## Temporal identity
- reference_date
- twin_creation_date
- last_twin_update
- data_valid_from
- data_valid_to
- construction_year
- construction_year_distribution
- construction_period_class
- permit_year
- first_occupancy_year
- major_renovation_years
- extension_years
- use_change_years
- partial_demolition_years

---

# Domain 02 — Spatial, environmental, and regional context

## Urban context
- urban_rural_class
- urbanization_level
- land_use_class
- zoning_class
- population_density
- building_density
- floor_area_density
- construction_activity_density
- demolition_activity_density
- neighborhood_typology
- block_typology

## Physical geography
- elevation
- terrain_class
- slope
- aspect
- climate_zone
- heating_degree_days
- cooling_degree_days
- seismic_zone
- flood_risk
- coastal_exposure
- soil/geotechnical_context

## Regional construction context
- regional_construction_practice
- regional_typology
- regional_code_generation
- common_structural_systems
- common_wall_systems
- common_roof_systems
- local_primary_material_supply
- local_secondary_material_supply
- regional_material_scarcity
- regional_material_price_context

## Circular infrastructure
- distance_to_reuse_hub
- distance_to_recycling_facility
- distance_to_processing_facility
- distance_to_landfill
- distance_to_secondary_market
- distance_to_primary_supplier
- road_network_access
- rail_access
- port_access
- on_site_sorting_space
- on_site_storage_space
- nearby_storage_capacity
- recycling_facility_capacity
- reuse_hub_capacity
- landfill_capacity
- landfill_gate_fee

## Policy / utility context
- regional_energy_mix
- projected_energy_mix
- regional_waste_policy
- regional_reuse_regulation
- regional_recycling_regulation
- landfill_restrictions
- selective_demolition_requirement
- pre_demolition_audit_requirement
- product_reuse_certification_rules

---

# Domain 03 — Building use, function, occupancy, and adaptability

- primary_use
- secondary_use
- mixed_use_fraction
- use_classification_system
- current_occupancy_status
- occupancy_density
- number_of_dwellings
- number_of_commercial_units
- number_of_total_units
- special_function
- public_private_use
- operating_schedule
- historic_use
- use_change_history
- planned_future_use
- functional_obsolescence_status
- convertibility_potential
- adaptability_constraints

Use is retained because it can affect typology, loading, internal layout, services, material intensity, component durability, and future reuse.

---

# Domain 04 — Building geometry and morphology

## Footprint and site
- footprint_area
- footprint_perimeter
- footprint_shape
- footprint_shape_complexity
- compactness
- perimeter_area_ratio
- orientation
- site_area
- building_coverage_ratio
- setback
- adjacency_type
- party_wall_length
- party_wall_fraction
- courtyard_presence
- courtyard_area

## Vertical geometry
- total_building_height
- eave_height
- ridge_height
- floor_count_above_ground
- floor_count_below_ground
- typical_floor_to_floor_height
- floor_heights_by_level
- gross_floor_area
- net_floor_area
- gross_external_floor_area
- gross_volume
- heated_volume
- unheated_volume
- basement_area
- basement_volume

## Envelope geometry
- external_wall_area_total
- external_wall_area_by_orientation
- roof_area
- ground_contact_area
- window_area_total
- window_area_by_orientation
- window_count
- window_to_wall_ratio
- external_door_area
- external_door_count

## Interior geometry
- internal_wall_length
- internal_wall_area
- internal_door_count
- ceiling_area
- floor_finish_area
- stair_count
- stair_area
- corridor_area
- circulation_area

## Morphological descriptors
- built_form
- detached_semi_row_block_slab_tower_class
- corridor_type
- core_type
- unit_layout_type
- unit_count_per_floor
- average_unit_area
- roof_form
- roof_pitch
- facade_repetition_pattern

## Geometry metadata and uncertainty
- geometry_source
- geometry_level_of_detail
- geometry_resolution
- geometry_completeness
- occluded_surface_fraction
- missing_facade_fraction
- geometry_validation_source
- geometry_accuracy_metric
- geometry_uncertainty_distribution

---

# Domain 05 — Construction age, typology, archetype, and classification

- exact_construction_year_if_known
- construction_period_probability
- age_class
- archetype_id
- archetype_definition
- archetype_method
- archetype_features_used
- archetype_probability
- archetype_reference_buildings
- archetype_sample_size
- construction_type
- construction_type_probability
- construction_technology
- regional_construction_generation
- building_code_generation
- prefabrication_status
- modular_construction_status
- industrialized_construction_status
- structural_system
- structural_system_probability
- structural_material_family
- energy_efficiency_class
- retrofit_state
- retrofit_depth
- retrofit_history
- archetype_transferability_flag
- archetype_region_mismatch
- archetype_uncertainty

Potential archetype predictors:
- age
- use
- height
- floors
- volume
- footprint shape
- built form
- structural clues
- region
- topography
- seismic zone
- facade style
- roof form

---

# Domain 06 — Structural system and load-bearing components

## Foundations
- foundation_type
- foundation_material
- foundation_dimensions
- foundation_volume
- foundation_mass
- foundation_depth
- foundation_reinforcement
- foundation_condition
- foundation_accessibility
- foundation_reuse_potential

## Vertical load-bearing system
- column_system
- column_material
- column_cross_section
- column_spacing
- column_count
- column_volume
- load_bearing_wall_system
- load_bearing_wall_material
- load_bearing_wall_thickness
- load_bearing_wall_area
- shear_wall_system
- shear_wall_material
- core_system
- core_material

## Horizontal system
- beam_system
- beam_material
- beam_cross_section
- beam_span
- beam_count
- floor_system
- floor_primary_material
- slab_type
- slab_thickness
- slab_area
- slab_volume
- joist_type
- deck_type

## Roof structure
- roof_structure_type
- roof_structure_material
- roof_member_dimensions
- roof_structure_volume
- roof_structure_condition

## Reinforcement and connectors
- reinforcement_type
- reinforcement_grade
- reinforcement_ratio
- prestressing_status
- connector_type
- welded_connection_fraction
- bolted_connection_fraction
- cast_in_connection_fraction
- adhesive_connection_fraction
- dry_connection_fraction

## Structural condition
- structural_damage_class
- cracking
- corrosion
- deformation
- spalling
- fire_damage
- moisture_damage
- fatigue_damage
- structural_repair_history
- structural_intervention_class
- remaining_structural_service_life
- structural_recertification_requirement

---

# Domain 07 — External envelope

## External walls
- external_wall_system
- external_wall_layer_count
- external_wall_layer_sequence
- external_wall_primary_material
- external_wall_secondary_materials
- external_wall_finish
- external_wall_cladding
- external_wall_insulation_type
- external_wall_insulation_thickness
- external_wall_cavity
- external_wall_total_thickness
- external_wall_area
- external_wall_U_value
- external_wall_connection_type
- external_wall_accessibility
- external_wall_condition
- external_wall_replacement_history

## Roof envelope
- roof_cover_material
- roof_membrane_material
- roof_insulation_material
- roof_insulation_thickness
- roof_deck_material
- roof_finish
- roof_U_value
- roof_condition
- roof_replacement_history
- roof_separability

## Windows
- window_id
- window_count
- window_area
- window_dimensions
- window_frame_material
- glazing_type
- glazing_layer_count
- glazing_material
- spacer_material
- window_U_value
- window_installation_system
- window_connection_type
- window_manufacture_year
- window_installation_year
- window_condition
- window_remaining_service_life
- window_reuse_potential
- window_recycling_potential

## External doors
- external_door_id
- external_door_count
- external_door_area
- external_door_material
- external_door_frame_material
- external_door_glazing
- external_door_connection
- external_door_condition
- external_door_reuse_potential

## Basement / ground interface
- basement_wall_material
- basement_wall_thickness
- basement_insulation
- waterproofing_material
- ground_slab_material
- ground_slab_thickness
- ground_slab_reinforcement
- ground_floor_finish

---

# Domain 08 — Interior and non-structural components

## Internal walls / partitions
- internal_wall_system
- internal_wall_material
- internal_wall_layer_sequence
- internal_wall_thickness
- internal_partition_area
- drywall_board_type
- stud_material
- insulation_in_partition
- plaster_type
- internal_wall_finish
- connection_to_floor_ceiling
- partition_reusability

## Floors / ceilings
- floor_finish_material
- floor_finish_thickness
- screed_type
- screed_thickness
- raised_floor_system
- ceiling_system
- suspended_ceiling_material
- ceiling_grid_material
- acoustic_panel_material

## Internal openings
- internal_door_id
- internal_door_count
- internal_door_material
- internal_door_frame_material
- internal_door_condition
- internal_door_reuse_potential

## Other interior components
- stairs_material
- balustrade_material
- built_in_furniture
- kitchen_fittings
- sanitary_fittings
- lighting_fixtures
- movable_partition_system
- acoustic_elements
- fixed_equipment

For every component, preserve:
component ID; location; geometry; material composition; installation date; connection; condition; service life; recoverability; reuse potential.

---

# Domain 09 — Building services / MEP material stock

- heating_system_type
- heating_equipment_count
- cooling_system_type
- cooling_equipment_count
- ventilation_system_type
- ventilation_equipment_count
- electrical_system_type
- plumbing_system_type
- sprinkler_system
- lift_system
- photovoltaic_system
- battery_system
- duct_material
- duct_mass
- pipe_material
- pipe_mass
- cable_material
- cable_mass
- radiator_material
- equipment_material_composition
- equipment_mass
- equipment_manufacturer
- equipment_model
- refrigerant_type
- refrigerant_charge
- installation_date
- expected_replacement_year
- service_history
- remaining_service_life
- MEP_reuse_potential
- MEP_recycling_potential

MEP may be optional in early implementations but remains architecturally available because replacement cycles can create significant non-structural flows.

---

# Domain 10 — Material / product / component identity

## Identity
- material_id
- product_id
- component_id
- assembly_id
- material_name
- material_family
- material_subtype
- trade_name
- manufacturer
- supplier
- product_standard
- certification_id
- EPD_id
- material_passport_id
- digital_product_passport_id
- batch_id
- manufacturing_date
- manufacturing_location
- installation_date
- original_project_id

## Composition
- chemical_composition
- constituent_materials
- constituent_mass_fractions
- composite_structure
- recycled_content
- post_consumer_recycled_content
- pre_consumer_recycled_content
- renewable_content
- bio_based_content
- critical_material_content
- hazardous_substance_content
- additives
- coatings
- adhesives
- treatments
- preservatives

## Physical properties
- density
- bulk_density
- surface_weight
- layer_thickness
- linear_weight
- weight_per_piece
- dimensions
- volume
- mass
- moisture_content
- porosity

## Mechanical / functional properties
- compressive_strength
- tensile_strength
- elastic_modulus
- yield_strength
- ductility
- weldability
- delamination_resistance
- fire_resistance
- thermal_conductivity
- thermal_resistance
- acoustic_property
- optical_property
- durability_class

Only properties relevant to identification, reuse, recycling, performance verification, or environmental assessment need to be populated.

---

# Domain 11 — Bill of materials and material stock

For each building-component-material record:

- stock_record_id
- component_id
- material_id
- component_location_in_building
- component_count
- component_area
- component_volume
- component_mass
- stock_quantity
- stock_quantity_unit
- stock_quantity_distribution
- quantity_measurement_method
- quantity_inference_method
- material_intensity
- material_intensity_unit
- material_intensity_distribution
- MI_source
- MI_source_version
- MI_geographic_scope
- MI_structure_class
- MI_function_class
- MI_age_class
- MI_reference_dimension
- MI_sample_size
- MI_transferability_flag
- quantity_validation_source
- quantity_validation_metric
- quantity_uncertainty

Mass-based and component-based representations should coexist where feasible.

---

# Domain 12 — Condition, quality, durability, and safety

## Condition / degradation
- condition_grade
- condition_inspection_date
- condition_method
- visual_damage
- crack_presence
- crack_width
- corrosion
- spalling
- rot
- warping
- delamination
- surface_wear
- moisture_damage
- frost_damage
- UV_degradation
- fire_exposure
- fatigue
- biological_damage
- previous_repairs

## Quality
- quality_grade
- purity
- quality_retention_fraction
- mechanical_property_retention
- performance_test_result
- certification_status
- recertification_required
- recertification_feasibility
- residual_functionality

## Hazard / contamination
- contamination_status
- contaminant_type
- hazard_class
- asbestos_presence
- lead_presence
- PCB_presence
- PAH_presence
- biological_contamination
- mixed_material_contamination
- decontamination_required
- decontamination_method
- decontamination_yield
- decontamination_cost
- decontamination_environmental_burden

## Durability
- reference_service_life
- expected_service_life
- service_life_distribution
- age_in_service
- remaining_service_life
- remaining_service_life_distribution

Quality must be pathway-specific. A material can be unfit for direct reuse while still suitable for high-quality recycling.

---

# Domain 13 — Connections, accessibility, separability, and disassembly

- connection_id
- connected_component_ids
- connection_type
- connection_material
- mechanical_connection
- chemical_connection
- reversible_connection
- reversibility_score
- connection_accessibility
- connection_visibility
- connection_independence
- edge_geometry
- number_of_connection_points
- connector_condition
- tool_requirement
- specialist_skill_requirement
- lifting_requirement
- component_weight
- handling_constraint
- disassembly_sequence
- disassembly_method
- disassembly_time
- disassembly_labor
- disassembly_energy
- disassembly_cost
- damage_risk_during_disassembly
- expected_salvage_yield
- layer_independence
- modularity
- standard_dimension
- dimensional_compatibility
- documentation_available
- assembly_manual_available
- disassembly_manual_available
- spare_parts_available

---

# Domain 14 — Lifecycle events, service life, and dynamics

## Event types
- construction
- maintenance
- repair
- replacement
- refurbishment
- extension
- adaptive_reuse
- use_change
- partial_demolition
- full_demolition
- component_removal

## Event record
- event_id
- event_type
- event_date
- event_time_distribution
- event_probability
- event_trigger
- affected_component_ids
- affected_material_ids
- affected_fraction
- released_quantity
- release_quantity_uncertainty
- replacement_input_quantity
- event_scenario_id

## Lifetime / survival model
- building_lifetime_distribution
- structural_lifetime_distribution
- facade_lifetime_distribution
- roof_lifetime_distribution
- window_lifetime_distribution
- interior_lifetime_distribution
- MEP_lifetime_distribution
- renovation_cycle_distribution
- repair_cycle_distribution
- demolition_probability
- survival_probability
- conditional_renovation_probability
- conditional_replacement_probability

Dependencies between component lifetime, renovation, and building survival must be represented.

---

# Domain 15 — Material release, deconstruction, and recovery chain

For each released material/component:

- release_record_id
- released_quantity
- release_quantity_distribution
- release_time
- release_time_distribution
- release_location
- release_event
- pre_demolition_audit_status
- selective_demolition_feasible
- selective_demolition_used
- source_separation
- collection_rate
- collection_loss
- sorting_method
- sorting_efficiency
- sorting_loss
- salvage_rate
- salvage_damage_rate
- recovery_rate
- processing_route
- processing_yield
- processing_loss
- post_process_quality
- post_process_contamination
- secondary_output_quantity
- residual_waste_quantity
- residual_waste_destination

Mass balance must be checked.

---

# Domain 16 — Circular pathway engine inputs

Pathways are material- and scenario-specific.

## Direct reuse
- reuse_candidate
- reuse_suitability
- reuse_quality_threshold
- reuse_structural_verification
- reuse_functional_verification
- reuse_dimension_match
- reuse_standard_compliance
- reuse_demand
- reuse_market_match
- reuse_time_match
- reuse_location_match
- reuse_storage_need
- reuse_storage_duration
- reuse_transport_distance
- reuse_preparation_process
- reuse_repair_requirement
- reuse_recertification_requirement
- reuse_effective_quantity

## Refurbishment / remanufacturing
- refurbishment_feasibility
- remanufacturing_feasibility
- repair_requirement
- refurbishment_input
- refurbishment_yield
- remanufacturing_yield
- post_process_quality
- post_process_service_life

## Closed-loop recycling
- closed_loop_feasible
- closed_loop_process
- closed_loop_facility
- closed_loop_collection_rate
- closed_loop_sorting_efficiency
- closed_loop_recovery_rate
- closed_loop_processing_yield
- closed_loop_quality_retention
- substitution_ratio
- substituted_primary_material
- closed_loop_effective_substitution

## Open-loop recycling
- open_loop_feasible
- downstream_application
- open_loop_facility
- open_loop_processing_yield
- quality_change
- replacement_coefficient
- substituted_product
- open_loop_effective_substitution

## Energy recovery / disposal
- energy_recovery_feasible
- energy_recovery_efficiency
- substituted_energy_carrier
- landfill_fraction
- landfill_type
- landfill_distance
- backfilling_fraction
- hazardous_disposal_requirement

---

# Domain 17 — Market, supply-demand, storage, and logistics

- secondary_market_exists
- market_region
- demand_material
- demand_quantity
- demand_time
- demand_quality_specification
- demand_dimension_specification
- demand_certification_requirement
- supply_demand_time_match
- supply_demand_location_match
- supply_demand_quality_match
- buyer_distance
- storage_required
- storage_duration
- storage_capacity
- temporary_storage_distance
- transport_mode
- transport_distance
- vehicle_capacity
- transport_load_factor
- empty_return_assumption
- fuel_or_energy_type
- handling_events
- facility_capacity
- facility_utilization
- facility_acceptance_criteria
- facility_technology
- facility_process_yield
- facility_energy_mix
- local_primary_material_price
- secondary_material_price
- landfill_fee
- recycling_fee
- deconstruction_cost
- processing_cost
- storage_cost
- recertification_cost

Economic fields can remain optional when the target decision is environmental only.

---

# Domain 18 — LCA / environmental-impact data

## Dataset identity
- LCA_dataset_id
- dataset_name
- dataset_version
- dataset_owner
- dataset_geographic_scope
- dataset_reference_year
- dataset_valid_until
- background_database
- EPD_program_operator
- specific_representative_generic_class
- data_quality_score
- technology_representativeness
- geographic_representativeness
- temporal_representativeness

## Units / methods
- declared_unit
- functional_unit
- conversion_factor_to_twin_quantity
- reference_study_period
- system_boundary
- allocation_method
- cut_off_rules
- recycled_content_method
- end_of_life_allocation_method
- substitution_method
- biogenic_carbon_method
- LCA_type_attributional_consequential

## Life-cycle modules
- A1_raw_material
- A2_transport
- A3_manufacturing
- A4_transport_to_site
- A5_construction
- B1_use
- B2_maintenance
- B3_repair
- B4_replacement
- B5_refurbishment
- B6_operational_energy
- B7_operational_water
- C1_deconstruction
- C2_transport_to_processing_or_disposal
- C3_waste_processing
- C4_disposal
- D1_reuse_recycling_recovery_potential
- D2_exported_utility_effects_if_applicable

## Environmental indicators
- GWP_total
- GWP_fossil
- GWP_biogenic
- GWP_land_use
- primary_energy_nonrenewable
- primary_energy_renewable
- embodied_energy
- embodied_water
- water_use
- acidification
- eutrophication
- ozone_depletion
- photochemical_ozone
- particulate_matter
- abiotic_resource_depletion
- mineral_metal_resource_use
- fossil_resource_use
- hazardous_waste
- non_hazardous_waste
- radioactive_waste

## Circular-scenario burdens / credits
- deconstruction_burden
- inspection_testing_burden
- cleaning_repair_burden
- sorting_burden
- storage_burden
- transport_burden
- processing_burden
- reuse_preparation_burden
- recycling_burden
- landfill_burden
- avoided_primary_production
- avoided_disposal
- substitution_credit
- scenario_gross_impact
- scenario_net_impact

---

# Domain 19 — User and scenario controls

- scenario_id
- scenario_name
- target_year
- decision_objective
- allowed_pathways
- reuse_enabled
- refurbishment_enabled
- remanufacturing_enabled
- closed_loop_enabled
- open_loop_enabled
- energy_recovery_enabled
- landfill_enabled
- maximum_transport_distance
- minimum_quality_threshold
- minimum_remaining_service_life
- minimum_reuse_quantity
- minimum_substitution_ratio
- maximum_landfill_fraction
- market_scenario
- energy_mix_scenario
- technology_scenario
- demolition_scenario
- renovation_scenario
- policy_scenario
- demand_scenario
- facility_scenario
- risk_tolerance
- uncertainty_threshold_for_decision
- optimization_objective
- multiobjective_weights_if_used

A building itself is never labelled open-loop or closed-loop. These are pathway choices for particular material flows under a scenario.

---

# Domain 20 — Uncertainty, variability, provenance, and validation

## Source definition
- uncertainty_source_id
- affected_entity_id
- affected_parameter_id
- DT_layer
- S_stream
- source_type_original
- source_type_harmonized
- variability_or_uncertainty
- epistemic_aleatory_mixed_if_supported

## Numerical representation
- distribution_type
- distribution_parameters
- minimum
- maximum
- mean
- median
- standard_deviation
- percentiles
- confidence_interval
- classification_probability
- sample_size

## Dependence
- correlation_group
- spatial_correlation
- temporal_correlation
- conditional_dependency
- joint_distribution_reference

## Provenance
- data_source
- source_date
- source_version
- acquisition_method
- operator
- model_id
- model_version

## Validation
- ground_truth_source
- validation_sample_size
- accuracy
- precision
- recall
- F1
- RMSE
- MAE
- bias
- calibration_metric
- validation_geographic_scope

## Uncertainty fate
- transfer_status
- representation_change
- magnitude_change
- change_basis
- reporting_status
- masked_or_lost_evidence
- decision_consequence
- evidence_locator

---

# Domain 21 — Final material decision-profile outputs

For every selected building × material/component × scenario:

## Current stock
- material identity
- component location
- current quantity
- current quantity distribution
- current quality
- current condition
- remaining service life
- uncertainty

## Release
- release event
- release quantity
- release-time distribution
- event probability
- uncertainty

## Circular pathways
- technically reusable quantity
- practically reusable quantity
- refurbishment/remanufacturing quantity
- closed-loop recyclable input
- closed-loop secondary output
- open-loop recyclable input
- open-loop secondary output
- energy-recovery quantity
- landfill quantity
- process losses
- effective primary-material substitution
- effective alternative-product substitution
- pathway feasibility probability
- pathway uncertainty

## Environmental consequence
- baseline impact
- reuse scenario impact
- closed-loop scenario impact
- open-loop scenario impact
- disposal scenario impact
- avoided impact
- net scenario impact
- impact uncertainty distribution
- probability_of_outperforming_baseline

## Decision diagnostics
- decision robustness
- dominant uncertainty source
- uncertainty contribution by parameter
- uncertainty contribution by material
- uncertainty contribution by DT layer
- critical missing data
- most valuable next observation
- confidence in scenario comparison

---

# Architecture admission rule

No new parameter enters the core merely because it is available.

A parameter should materially support at least one of:

1. material identity;
2. material quantity;
3. material quality or condition;
4. release timing;
5. circular-pathway feasibility;
6. effective substitution;
7. environmental consequence;
8. uncertainty or decision robustness.

If not, it belongs in optional context rather than the core architecture.
