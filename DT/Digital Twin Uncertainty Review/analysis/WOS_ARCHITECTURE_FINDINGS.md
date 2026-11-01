# Web of Science: uncertainty architecture evidence

## Scope and limits

The complete 2,016-record export is available. Lexical flags use titles, abstracts, author keywords and Keywords Plus. Counts are overlapping term matches, not demonstrated architectures, quality assessments or eligibility decisions: uncertainty representation 2,016; state updating/calibration 487; propagation/coupling 176; semantics/interoperability 148; provenance/traceability 70; validation/monitoring 834; decision/feedback 718; architecture-related terms 1,287.

The following observations are based on selected native exported abstracts. No full-text review or comprehensive novelty assessment has been completed.

## Selected evidence

| Record and DOI | Abstract-level contribution | Required caution / full-text extraction |
|---|---|---|
| WOS:001874346600001 — [Navigating uncertainty in digital twin ecosystems](https://doi.org/10.1016/j.jii.2026.101189) | Proposes ontological uncertainty associated with a changing frame of discernment, a random-set representation and update mechanism, and drivers of propagation/amplification. Presents a six-layer framework and a battery-system case using real data. | The proposed uncertainty category is the authors' framing, not an accepted universal taxonomy. Verify formal definitions, interface behavior and how much of the layered architecture is actually implemented. Quantum and human-in-the-loop layers being named is not proof they are deployed. |
| WOS:001323733800030 — [The Role of Uncertainty Propagation for Digital Twins](https://doi.org/10.1007/978-3-031-60271-9_28) | Uses Monte Carlo prediction uncertainty for a bridge example and a distribution-convergence procedure to monitor numerical estimation. | Convergence of a simulation estimate is distinct from validation against reality and from inter-service uncertainty continuity. Same DOI already appears in Scopus: independent indexing is not independent evidence. |
| WOS:001116078600001 — [PGM-based digital twins: space habitat study](https://doi.org/10.1016/j.jsse.2023.04.001) | DAG-based uncertain variables, historical training and online conditional inference connect observations to estimates of time before a temperature limit. Reports three-room analogue experiments. | Extract graph dependencies, sensor selection, distributions and decision thresholds. This is an analogue, not a deployed space habitat. Also indexed by Scopus. |
| WOS:001153596700001 — [Continuous crystallization digital design](https://doi.org/10.1016/j.ces.2023.119688) | Population-balance parameter estimation compares experimental and model-prediction uncertainty; an experimentally validated process model and parameter uncertainty space support optimization. | Check whether live synchronization and subsequent updating satisfy the review's DT definition; an uncertain validated model alone does not establish a continuously updated twin. |

## Implications for the review question

The extraction scheme should examine not only the numerical uncertainty passed through an interface but changes in the set of variables, hypotheses or system components that the interface represents. A stable schema may become inadequate when a twin ecosystem reconfigures. Distinguish this proposed structural/ontological issue from aleatoric variability, epistemic parameter/model uncertainty and numerical approximation error.

Retain the chain **measurement → state/model → component/interface → prediction → validation/update → decision**, adding explicit checks for schema changes, model/version provenance, dependency assumptions and retained uncertainty representations at each transition. These are proposed review coding fields, not claims that every retrieved system implements them.

There are existing propagation, graph-based and integrated-framework studies. The defensible open question is which mechanisms preserve and validate interpretable uncertainty across heterogeneous components and changing system configurations. Do not claim a research gap solely from lexical counts or abstracts.
