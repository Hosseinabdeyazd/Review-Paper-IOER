# Environmental / LCA Engine

## Purpose

This module converts material stocks and pathway-specific material flows into environmental consequences.

Circularity performance and environmental performance are intentionally kept separate.

---

# 1. Required LCA definition

Every result must specify:

- functional unit;
- reference study period;
- building/material/product scope;
- geographic context;
- reference year;
- LCI method: process / input-output / hybrid;
- LCI database and version;
- system boundary;
- allocation method;
- recycling/substitution method;
- characterization method/version;
- cut-off rules;
- treatment of biogenic carbon where relevant;
- treatment of Module D / avoided burden where relevant;
- uncertainty method.

A result lacking this context should not be treated as directly comparable with another result.

---

# 2. Lifecycle-module structure

Architecture supports EN 15978-style stages where applicable:

## A1–A3 — product stage
- raw material supply;
- transport to manufacturing;
- manufacturing.

## A4–A5 — construction stage
- transport to site;
- construction/installation/waste.

## B2–B5 — maintenance, repair, replacement, refurbishment
Important for component-service-life and recurring material flows.

## C1–C4 — end of life
- deconstruction/demolition;
- transport;
- waste processing;
- disposal.

## D — beyond-boundary benefits/loads
- reuse;
- recovery;
- recycling;
according to declared methodological rules.

The engine must allow studies/scenarios with different boundaries while marking omitted modules explicitly.

---

# 3. Environmental-factor object

Every factor should store:

- factor_id;
- material/process/product;
- indicator;
- numeric value/distribution;
- unit;
- functional reference;
- lifecycle module;
- production/process technology;
- geography;
- reference year;
- database;
- database version;
- LCI method;
- system boundary;
- allocation;
- completeness/truncation note;
- data quality;
- uncertainty;
- source/provenance.

**Reason:** Crawford et al.'s EPiC work highlights that inventory method and system-boundary completeness materially affect embodied environmental coefficients.

---

# 4. Indicator families

## Core
- global warming potential / GHG;
- virgin-material use / effective substitution;
- waste to disposal.

## Advanced where supported
- primary energy;
- water;
- abiotic/resource use;
- acidification;
- eutrophication;
- photochemical ozone formation;
- ozone depletion;
- particulate matter;
- toxicity/ecotoxicity;
- land use;
- radioactive waste/other method-specific indicators.

No single indicator is assumed sufficient for all decisions.

---

# 5. Pathway foreground processes

## Direct reuse
Potential foreground burdens:
- selective deconstruction;
- inspection/testing;
- cleaning;
- repair/refurbishment;
- storage;
- transport;
- recertification/preparation.

Potential avoided burden:
- production of functionally equivalent new component/material.

## Closed-loop recycling
- deconstruction;
- collection;
- sorting;
- transport;
- recycling process;
- residues/disposal;
- production of recycled product;
- avoided virgin equivalent according to substitution rule.

## Open-loop recycling
- same chain, but output replaces a different product/material;
- replacement coefficient/functionality must be explicit.

## Disposal
- demolition;
- transport;
- pretreatment;
- landfill/incineration/other disposal.

---

# 6. Baseline architecture

Every circular scenario requires a baseline.

Possible baselines:
- conventional demolition + current waste treatment;
- landfill-heavy baseline;
- current regional recycling practice;
- virgin-production reference;
- project-specific existing plan.

Required fields:
- baseline_id;
- reference year;
- geography;
- treatment fractions;
- facilities;
- transport;
- LCI;
- uncertainty.

Do not compare a future circular scenario against an undefined baseline.

---

# 7. Effective substitution

Environmental credit must be based on effective displacement, not gross recovered mass.

Conceptually:

```text
effective displaced quantity
= circular output quantity
× substitution/replacement coefficient
```

But the coefficient may depend on:
- material quality;
- product performance;
- closed/open loop;
- market/demand;
- technical standards;
- process technology;
- time/location.

The basis must be recorded.

---

# 8. Transport

Required:
- origin;
- destination;
- route distance;
- transport mode;
- vehicle/load factor where material;
- number of trips or tonne-km;
- transport emission/energy factor;
- backhaul assumption if used;
- uncertainty.

Facility proximity is not enough: the accepted material/quality and available capacity must also match.

---

# 9. Future-scenario environmental context

For prospective scenarios, allow:
- future electricity mix;
- future fuel mix;
- process-efficiency change;
- recycling technology;
- virgin-production decarbonization;
- landfill technology;
- transport decarbonization;
- future characterization/context if methodologically justified.

All future assumptions are scenario variables, not observed building properties.

---

# 10. Environmental output per material batch

For each material × pathway × scenario:

- gross released mass;
- useful circular output;
- effective substituted mass;
- A/B/C/D modules included;
- deconstruction impact;
- transport impact;
- processing impact;
- storage/repair impact;
- disposal impact;
- avoided virgin-production credit;
- other benefits/loads;
- net indicator results;
- difference from baseline;
- uncertainty;
- provenance/method.

---

# 11. Uncertainty sources

## Foreground
- material quantity;
- release quantity;
- process yield;
- distance;
- energy use;
- substitution.

## Background
- database coefficient;
- geography;
- year;
- technology;
- electricity mix.

## Methodological
- system boundary;
- allocation;
- LCI method;
- characterization;
- cut-off;
- Module D/recycling method.

## Temporal
- service life;
- release year;
- future background system.

## Scenario
- route/facility;
- treatment fraction;
- demand.

---

# 12. Hotspot distinction

For every scenario, separately report:

### Impact hotspot
Which material/process contributes most to environmental impact?

### Uncertainty hotspot
Which input/source contributes most to uncertainty in the environmental result?

Hoxha et al. demonstrate why these need not be the same.

---

# 13. Comparability gate

Before comparing two scenario/study results, verify:

- same/compatible functional unit;
- system boundary;
- reference period;
- indicator/method;
- geographic/temporal basis;
- treatment of replacements;
- treatment of recycling/substitution;
- material scope;
- lifecycle stages.

If not, mark comparison as limited/incomparable rather than harmonizing silently.

---

# 14. Decision output

The environmental engine supplies DT-L5 with:

- scenario impact distribution;
- difference from baseline;
- material/process contributions;
- uncertainty contributions where supported;
- methodological comparability status;
- missing/weak data;
- next-data recommendation.

It does not independently select a circular pathway unless the user has supplied an explicit decision objective/rule.
