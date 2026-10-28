# Concept development and terminology audit — provisional ideas only

**Status:** pre-novelty ideas ledger, v0.1. Nothing on this page should be presented as a coined term or established scientific contribution.

## The safe sequence

1. Extract an existing term's precise source definition and range of use.
2. Test whether the claimed distinction is already described elsewhere under another label.
3. Find an actual **classification failure** in reviewed architectures.
4. Give the candidate construct a falsifiable operational definition and observable indicators.
5. Pilot the construct across heterogeneous implementations; check coder agreement.
6. Retain a new term **only if** it improves explanatory and classification power over existing terms.

## Existing terms — **not** ours to invent

- **Open-loop / closed-loop / feedback control**: control and cyber-physical systems vocabulary; a workflow's loop status must be tested as an actual directed path.
- **Human-in-the-loop / human-mediated feedback**: pre-existing practice; distinguish a visual dashboard, a recommendation, an authorized action and observed physical consequences.
- **Federated / hierarchical / modular digital twin**: existing architectural strategies; the nesting of assets and data ownership differs from control-loop closure.
- **Digital shadow, digital model, digital twin**: established but contested differentiation; use context-specific documented criteria, not simplistic real-time-only classification.
- **Digital thread / provenance / semantic interoperability**: existing concepts for tracing identity, versions, data relationships and model interactions.
- **Closed-loop material recycling**: different meaning from feedback-control closure; never conflate the two.

## Candidate concepts for testing (working labels, NOT novelty claims)

| Working label | Proposed precise distinction | How to observe it | Falsifier / collision check |
|---|---|---|---|
| **Two-loop coupling profile** | Separately represents (P) physical–digital state/update/decision loops and (C) inter-model computational handoff/recalculation loops. | Typed edges for observations, decision/physical action, model-result dependencies and reruns. | Existing multi-loop DT taxonomies may already define it; find before naming. |
| **Uncertainty-carrying digital thread** | Traced object/parameter identity alone is insufficient; representation, assumptions, dependencies and distributional metadata survive each semantic/model transformation. | Evidence of upstream distribution/interval, transfer, downstream use, and lineage, including correlation if relevant. | Existing uncertainty-aware semantic DT / probabilistic provenance research may cover the same construct. |
| **Event-calibrated material twin** | For stocks and long-lived materials, discrete physical events (inspection, renovation, demolition) may be the essential update clock, separate from BAS streaming. | Event IDs, observed quantity/quality, before/after stock state, recalibration and confidence change. | Search event-sourced and state-based DT architecture literature; do not claim novelty on "event-driven". |
| **Decision-conditioned fidelity** | The sufficient data/temporal/granularity fidelity depends on the target decision and error tolerance, rather than maximizing LoD indiscriminately. | Purpose and decision threshold mapped to required precision and validation. | Existing fit-for-purpose fidelity and decision-centred calibration may fully cover this. |

All rows above are **hypotheses to test**, not accepted classes or original terms. Do not encode them as inclusion criteria for the evidence corpus.

## Architecture-level tests we could run (dependent on sufficient papers)

**T1.** Do architecture studies that report an actual physical–digital feedback path also report executable inter-model dependencies? Not necessarily; investigate.

**T2.** Is LTDS/HPRT family membership associated with update cadence or feedback topology? Neither equality nor causal connection should be assumed.

**T3.** Can component–building–city material information be reconciled across independent owners without losing temporal/source identity?

**T4.** Are explicit uncertainty-handling links more prevalent at sensing/calibration interfaces than across material-stock → dynamic MFA → recovery → LCA? Count only assessable handoffs and separately report *unassessed*.

**T5.** Are design-for-disassembly / connection-level attributes the limiting source of recovery estimates, compared with material mass, in studied DT and non-DT material models?

## Potential network indices (only after study-level data extraction)

- **Edge support**: number of independent studies explicitly reporting a typed relation, with strata for conceptual / implemented / validated.
- **Loop completeness**: proportion of required typed edges documented for a declared use-case loop; not a universal "DT maturity score".
- **Uncertainty handoff observability**: assessable links / all links with evidence for an upstream uncertainty representation.
- **Confirmed uncertainty loss**: downstream discard / masking documented with upstream uncertainty; distinguish from lack of reporting.
- **Cross-scale semantic continuity**: observed persistent identity/quantity conservation and version alignment across building–district–city aggregation.

Any "percentage of uncertainty loss" across studies requires a well-defined denominator and evidence for a loss; missing reports are not failures. Non-equivalent units and representations cannot be compared by the numerical size of ± intervals alone.

## Priority novelty audit

- Abdelrahman et al. (2025), DOI 10.1016/j.buildenv.2025.112748 — HPRT/LTDS, component families, city/building definitions.
- Davila Delgado & Oyedele (2021), DOI 10.1016/j.aei.2021.101332 — conceptual, process and communication models.
- Kosse et al. (2025), DOI 10.1016/j.aei.2025.103483 — modular semantic/federation-relevant patterns.
- Geremicca et al. (2026), DOI 10.1016/j.enbuild.2026.117332 — purpose-led BIM/MFA/LCA and event updating.
- Malihi (2026), DOI 10.1016/j.dte.2026.100140 — uncertainty-aware calibration and tolerances.
- DTC Glossary — digital twin, digital thread, synchronisation, systems and services: https://www.digitaltwinconsortium.org/glossary/glossary/

## What would count as a contribution?

**Not:** assigning a catchy name to an intuitive workflow.
**Potentially:** an evidence-coded architecture typology that captures a repeatable, measurable distinction missed by previous taxonomies, with explicit boundary rules, source-traceable examples, counterexamples and demonstrable relevance to uncertainty handoffs in circular material decisions.
