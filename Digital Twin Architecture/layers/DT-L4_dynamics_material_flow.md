# DT-L4 — Dynamics & Material-Flow Simulation

## Status
Architecture v0.3 — detailed working specification.

## Mission
Transform the current probabilistic material stock into **time-dependent stock and release flows**.

Circular material availability is an event problem, not simply a demolition total.

---

## 1. Time state

For every component/material:
- installation/construction year;
- current age;
- reference service life;
- service-life distribution;
- remaining service life;
- condition/degradation;
- replacement/maintenance history.

---

## 2. Event types

- maintenance;
- repair;
- replacement;
- refurbishment;
- energy retrofit;
- façade renewal;
- roof renewal;
- window replacement;
- internal fit-out replacement;
- structural intervention;
- change of use;
- building extension;
- partial demolition;
- full demolition.

Each event has:
- time/probability;
- trigger;
- affected components;
- material outflows;
- new material inflows;
- retained material.

---

## 3. Event timing models

Possible representations:
- known date;
- deterministic service life;
- interval;
- probability distribution;
- survival/hazard function;
- scenario-specific event.

Architecture does not force one distribution family.

---

## 4. Layer-specific lifetimes

Do not assign only one building lifetime.

Different components may have different cycles:
- structure;
- façade/skin;
- roof;
- windows;
- partitions/fit-out;
- finishes;
- services.

This creates material flows before whole-building demolition.

---

## 5. Stock-flow balance

For time t:

```text
Stock(t+1)
= Stock(t)
+ installed inflows
- released outflows
```

Maintain material identity/state so replaced materials do not disappear into anonymous totals.

---

## 6. Release profile

For each released batch:
- event ID/type;
- expected time;
- time distribution;
- released quantity distribution;
- component source;
- material state at release;
- quality degradation;
- contamination changes;
- location.

---

## 7. Renovation and replacement

A renovation can:
- release old material;
- retain some material;
- add new material;
- change future service life;
- change energy/environmental context;
- change component separability.

The twin should version the building state before/after event.

---

## 8. Demolition/deconstruction scenario

Inputs:
- intervention date;
- demolition vs selective deconstruction;
- sequence;
- recovery plan;
- pre-demolition audit;
- contamination constraints.

Outputs:
- release batches and state;
- not yet circularity allocation—that occurs in DT-L5.

---

## 9. Prospective scenarios

Future assumptions may include:
- stock turnover;
- renovation policy;
- demolition probability;
- technology;
- reuse/recycling practices;
- energy mix;
- material demand.

Scenario variables remain separate from observed current-state evidence.

---

## 10. Uncertainty

Main sources:
- service-life distribution;
- functional obsolescence;
- renovation/demolition decision;
- timing;
- component replacement;
- future policy/technology;
- quality degradation;
- inherited stock quantity.

Correlations matter:
construction age may affect material type, hazard risk and remaining life simultaneously.

---

## 11. Output to DT-L5

Canonical release object:
- material_batch_id;
- event_id;
- scenario_id;
- time distribution;
- release quantity distribution;
- condition/quality at release;
- evidence/provenance;
- uncertainty.

---

## 12. Success criterion

DT-L4 must tell DT-L5:
**what becomes available, where, when, how much, in what state, and how uncertain that forecast is.**
