
# LCA / Environmental Consequence Engine

## Purpose

Translate material stocks and circular pathways into environmental consequences without losing material identity, quantity, location, time, pathway, substitution assumptions, system boundary, and uncertainty.

The LCA engine is downstream of material-stock and circularity modelling but can send feedback upstream when missing data dominate the environmental decision.

---

# 1. Material-to-LCA dataset mapping

Every material/product/component record should map to an environmental dataset through:

- material/product identity;
- dataset ID;
- dataset version;
- dataset owner/source;
- geographic scope;
- reference year;
- validity period;
- technology/process represented;
- declared unit;
- conversion factor to Digital Twin quantity;
- product-specific vs representative vs generic status;
- background database;
- EPD operator where relevant;
- data-quality metadata.

If no direct match exists, store the proxy hierarchy explicitly:
1. product-specific;
2. regional representative;
3. national representative;
4. generic;
5. cross-region proxy.

Every proxy step creates a traceable representativeness uncertainty.

---

# 2. Life-cycle module representation

Preserve life-cycle stages separately.

## Product / construction
- A1 raw material supply / extraction and upstream production
- A2 transport to manufacturing
- A3 manufacturing
- A4 transport to site
- A5 construction / installation

## Use
- B1 use
- B2 maintenance
- B3 repair
- B4 replacement
- B5 refurbishment
- B6 operational energy
- B7 operational water

## End of life
- C1 deconstruction / demolition
- C2 transport to processing or disposal
- C3 waste processing for reuse / recycling / recovery
- C4 disposal

## Beyond system boundary
- D1 reuse / recycling / recovery potential
- D2 exported utility effects where applicable

Benefits/credits beyond the system boundary should not be silently merged into A-C. They remain separate until an explicit accounting method/scenario combines them.

---

# 3. Environmental data per material/product

Minimum preferred indicators:
- GWP-total
- GWP-fossil
- GWP-biogenic
- GWP-land-use

Where available:
- embodied energy
- non-renewable primary energy
- renewable primary energy
- embodied water / water use
- acidification
- eutrophication
- ozone depletion
- photochemical ozone formation
- particulate matter
- mineral/metal resource use
- fossil resource use
- hazardous waste
- non-hazardous waste
- radioactive waste

The architecture should support multiple indicators even if the initial implementation focuses on GWP.

---

# 4. Scenario-specific circularity burdens

## Direct reuse
Possible burdens:
- selective deconstruction;
- inspection/testing;
- cleaning;
- repair;
- recertification;
- storage;
- transport;
- reinstallation.

Possible benefits:
- avoided production of the receiving new product;
- avoided disposal;
- life extension.

## Refurbishment / remanufacturing
- deconstruction;
- transport;
- repair/replacement materials;
- process energy;
- testing/certification;
- reinstallation;
- avoided new production.

## Closed-loop recycling
- collection;
- sorting;
- transport;
- processing;
- losses;
- secondary-material production;
- residual disposal;
- avoided primary production based on substitution ratio.

## Open-loop recycling
- collection;
- sorting;
- transport;
- processing;
- transformed downstream product;
- residual disposal;
- avoided alternative product based on replacement coefficient.

## Energy recovery
- preparation;
- transport;
- combustion/recovery;
- residue treatment;
- substituted energy if methodologically included.

## Landfill
- demolition;
- transport;
- treatment;
- landfill process;
- long-term emissions where the LCA method includes them.

---

# 5. Conceptual accounting relation

For scenario s:

Scenario impact =
deconstruction burden
+ transport burden
+ sorting burden
+ processing burden
+ storage burden
+ repair/refurbishment burden
+ residual disposal burden
+ other included life-cycle burdens
- methodologically valid avoided burdens

The exact treatment of credits depends on LCA method. Therefore store:

- attributional vs consequential approach;
- allocation rule;
- recycled-content method;
- end-of-life method;
- substitution method;
- Module D convention;
- cut-off rule;
- biogenic-carbon method.

---

# 6. Quantity and unit conversion

Store:
- Digital Twin quantity unit;
- declared unit of LCA dataset;
- density;
- bulk density;
- thickness;
- surface weight;
- linear weight;
- weight per piece;
- conversion factor;
- conversion uncertainty.

Never silently convert component count/area/volume to mass without recording the conversion basis.

---

# 7. Regionalization

Store independently:
- building location;
- material manufacturing location;
- reuse receiver location;
- processing/recycling location;
- landfill location;
- electricity-grid region;
- transport network;
- LCI dataset geography;
- characterization-factor geography where relevant.

Spatialization and regional representativeness are separate.

---

# 8. Time and dynamic environmental coefficients

Potential time-varying inputs:
- electricity mix;
- fuel mix;
- transport technology;
- manufacturing efficiency;
- recycling technology;
- facility yield;
- future characterization factors where methodologically supported.

Store:
- coefficient reference year;
- scenario year;
- future scenario source;
- dynamic/static flag;
- interpolation/extrapolation rule;
- temporal uncertainty.

Future material release in 2050 should not automatically use a 2020 process coefficient without an explicit assumption.

---

# 9. Service life and replacement

For each relevant component/material:
- reference study period;
- reference service life;
- expected service life distribution;
- residual service life;
- maintenance cycle;
- repair cycle;
- replacement cycle;
- replacement count distribution;
- replacement material;
- replacement process.

Arbitrary deterministic replacement counts should be avoidable when service life is uncertain.

---

# 10. LCA data-quality and uncertainty dimensions

Potential uncertainty sources:
- material quantity;
- density/unit conversion;
- dataset selection;
- geographic representativeness;
- temporal representativeness;
- technology representativeness;
- system boundary;
- allocation;
- characterization factor;
- service life;
- transport;
- processing yield;
- energy mix;
- substitution ratio;
- replacement coefficient;
- future demand/technology scenario.

Each material should expose two distinct concepts:
- contribution to environmental impact;
- contribution to uncertainty of environmental impact.

They are not assumed to be the same.

---

# 11. Baselines

Possible baselines:
- current conventional demolition + disposal;
- conventional demolition + current recycling practice;
- virgin-material production;
- business-as-usual building replacement;
- region-specific waste-management baseline.

Every scenario comparison must store its baseline explicitly.

---

# 12. Environmental output per building × material × pathway × scenario

- gross impact by life-cycle module;
- deconstruction burden;
- transport burden;
- processing burden;
- repair/reuse burden;
- disposal burden;
- avoided production;
- avoided disposal;
- benefits/credits separately;
- net impact if method allows;
- uncertainty distribution;
- percentile range;
- probability of outperforming baseline;
- data-quality/provenance flag;
- dominant LCA uncertainty sources.

The preferred decision output is a distribution/robustness statement, not only one deterministic kg CO2e result.
