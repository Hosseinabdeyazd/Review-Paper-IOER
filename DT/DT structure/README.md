# Digital Twin structure — evidence-linked working model

**Status:** provisional synthesis, 2026-10-31. This is a research working model, not a published or ISO-endorsed taxonomy, and not the result of a completed systematic review.

## Why two levels?

The proposal separates two kinds of questions:

1. **Meta-level design concerns (4):** why the twin is needed, what data and rules govern it, how it exchanges information, and how its claims are checked.
2. **Configuration dimensions (6):** how the twin is composed and architected, which models and control arrangements it uses, how much agency it has, and how it behaves over time.

The four concerns guide choices across the six configuration dimensions. They are not sequential lifecycle phases, and the relation is many-to-many. *Assurance & Evidence* is especially cross-cutting. The mapping in the figure is an explicit synthesis for discussion; it must be validated against a systematic evidence corpus before being presented as a definitive taxonomy.

## Four meta-level design concerns

| Meta-level concern | Questions it organizes |
|---|---|
| Purpose, Scope & Context | What decision or service is needed? What is the represented entity, system boundary, scale, context, and intended use? |
| Data, Semantics & Governance | Which data sources and forms are used? How are meaning, quality, provenance, ownership, access, security, and retention handled? |
| Interfaces & Interoperability | Which users, physical entities, external systems, and other twins exchange information? Through what interfaces, standards, and semantic mappings? |
| Assurance & Evidence | What evidence supports model fidelity, data quality, synchronization, safety, performance, and validation against the represented system? |

## Six configuration dimensions

| Configuration dimension | Candidate alternatives to investigate |
|---|---|
| System Composition | Single Twin; Aggregate; Composite; Network; Federated; Ecosystem |
| Internal Architecture | Layered; Modular; Service-oriented; Knowledge-graph-based |
| Computational Model | Physics-based; Data-driven; Hybrid; Multiscale |
| Coupling & Control | One-way; Bidirectional; Human-mediated; Automated closed-loop |
| Agency & Intelligence | Rule-based; Agent-based; Multi-agent; Agentic AI |
| Temporal Organization | Continuous; Periodic; Event-driven; Multi-rate |

These alternatives are a candidate parameter space. They are not mutually exclusive across dimensions, and not every combination is feasible or supported by evidence.

## Proposed many-to-many mapping

| Meta-level concern | Configuration dimensions it can guide |
|---|---|
| Purpose, Scope & Context | System Composition; Internal Architecture; Computational Model; Agency & Intelligence; Temporal Organization |
| Data, Semantics & Governance | Internal Architecture; Computational Model; Coupling & Control; Temporal Organization |
| Interfaces & Interoperability | System Composition; Internal Architecture; Coupling & Control; Agency & Intelligence |
| Assurance & Evidence | Cross-cutting across all six dimensions |

This mapping is an analytical synthesis, not a claim that each cited paper uses these exact four meta-level labels.

## Evidence and interpretation boundaries

- Xiong et al.'s cross-domain framework uses six different dimensions: twinning objects, purposes, system architectures, data, modelling, and services. It is not the same six-axis configuration space shown here.
- Jones et al. characterize a twin through thirteen properties, including physical/virtual entities and environments, state, metrology, realization, twinning rate, links, and processes. These inform scope, observability, coupling, and time-related subparameters.
- van der Valk et al. derive a configuration taxonomy with data collection, data handling/distribution, and conceptual-scope meta-dimensions. Their dimensions include data acquisition/source/input, synchronization, governance, link, interface, interoperability, purpose, accuracy, conceptual elements, and time of creation.
- ISO/IEC 30188:2026 describes architecture through foundational, functional, implementation, and architecture-pattern viewpoints. These are architectural views, not a competing list of system components.
- Software-engineering and platform surveys add implementation, deployment, orchestration, security, interoperability, and quality-assurance concerns. Blockchain is treated as an optional trust/data-management design choice where justified, not a mandatory DT component.
- These sources differ in scope and abstraction level. Their terms have not been collapsed into a single taxonomy without traceability.

## Files

- [Figure: four meta-level concerns guiding six configuration dimensions](figures/dt-structure-4-plus-6.svg)
- [Selected source register and evidence mapping](papers/README.md)

## Citation and reuse

The figure is an original synthesis prepared for this review project. Cite the underlying sources listed in the paper register when discussing specific concepts. Do not cite the figure as if its complete 4+6 structure appeared in a single source.
