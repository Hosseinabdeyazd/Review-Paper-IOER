# Digital Twin Material Flow Review

This stream investigates **building/material-flow digital-twin architectures across S1–S5**, as a domain-specific complement to the general Digital Twin Uncertainty Review. It is not an additional stage S6, and S1–S5 are analytical streams, not five universally established DT software layers.

## Research question and purpose

Which entities, data interfaces, inference models, temporal updates and decision services connect observations of buildings to material inventories, material outflows, recovery and environmental decisions? Once these architectures are established from full texts, where can uncertainty enter, be inherited, change representation, propagate, or lose traceability?

The immediate deliverable is a reproducible retrieval corpus and an extraction protocol. Retrieved records are **not automatically included studies**. No claim of completed full-text assessment of this new corpus is made.

## Search design

Each stage uses `(digital twin OR digital twins) AND building-context AND stage-terms`. Five searches are run in each of IEEE Xplore, Scopus and Web of Science Core Collection. The complete executable strings and original source queries are preserved in `protocol/queries.json`; counts and completion status are in `protocol/search_log.csv`.

| Stage | Functional scope | Main search concepts |
|---|---|---|
| S1 | Observation and building reconstruction | GeoAI, remote sensing, computer vision, LiDAR, photogrammetry, point clouds, scan-to-BIM, building geometry/age/classification |
| S2 | Material inventory and stock inference | material stocks, inventories, intensity, composition, quantities, archetypes, passports, quantity takeoff |
| S3 | Time and material-flow generation | material flows, stock dynamics, service life, remaining useful life, demolition timing, replacement and renovation |
| S4 | Recovery and circular circulation | reuse, recycling, recovery, deconstruction, urban mining, passports, disassembly, reverse logistics, matching |
| S5 | Environmental assessment and decisions | embodied carbon, LCA, environmental impacts, carbon footprint, material-related decision support/ranking |

### Derivation and scope changes

These are **stage-aligned adaptations**, not a literal replay of the original S1–S5 searches with one extra word. Existing Scopus base queries were consulted. The new building context admits individual buildings and components, rather than requiring urban stock studies. Existing exclusions were not inherited, and neither uncertainty, architecture nor named algorithms are mandatory retrieval terms. This avoids excluding architectures that do not advertise uncertainty in their metadata. New DT-oriented observation terms and quantity-takeoff terms were added. Broad S5 decision terms require material/circularity context.

The original S4/S5 files were marked draft. They remain unchanged. The new DTMF-S4-v1 and DTMF-S5-v1 are distinct, frozen retrieval versions prepared for this user-authorized stream. `queries.json` retains the source wording for audit.

**Known precision limitations:** `building*` can mean the act of constructing a model; `recover*` may retrieve system recovery; service-life queries may retrieve equipment prognosis; LCA can concern operational energy. S1 deliberately retrieves enabling reconstruction methods. These must be classified at screening, not silently deleted from raw exports. A hit on Digital Twin does not prove a functioning synchronized twin.

### Database fields and exports

- Scopus: Article title, Abstract, Keywords (`TITLE-ABS-KEY`). All documents selected; **Select all information**, including DOI, abstracts, keywords, affiliations, funding and references.
- WoS: `TS` topic search (includes Keywords Plus, so it is not field-identical to Scopus). All editions available through the subscription; **Full Record and Cited References**. This format has a 500-record export limit, so S1 is split into 1–500 and 501–652.
- IEEE: Search by All with the recorded Boolean expression; native Results CSV, all results. Its search scope and exported fields are not identical to Scopus/WoS. All 28 native columns are preserved; reference *counts* do not mean cited-reference lists are available.
- No year, language, document-type or open-access restrictions were intentionally applied. Future issue years already indexed on the retrieval date are retained. Subscription coverage and indexing differences affect counts.
- Retrieval date: 2026-11-01. No credentials, cookies, signed session URLs or authentication artifacts belong in this folder.

## Files and reproducibility

```
protocol/queries.json             Frozen queries and original source wording
protocol/search_log.csv           Displayed counts versus actual exported rows
protocol/file_manifest.csv        Raw-export SHA-256, size, rows and column counts
raw/IEEE/*.csv                    Native unmodified exports
raw/Scopus/*.csv                  Native unmodified exports
raw/WoS/*.txt                     Native tab-delimited full-record exports
converted/*.csv                   Lossless column-preserving WoS CSV conversions
analysis/source_records.csv       Common metadata fields, one row per retrieved occurrence
analysis/deduplicated_records.csv Conservative unique records for screening
analysis/stage_source_membership.csv Every stage/database/raw-record link
analysis/possible_title_duplicates.csv Candidate duplicates needing human review
analysis/summary.json             Recomputed counts
code/build_dataset.py             Standard-library normalization and audit code
ARCHITECTURE_EXTRACTION_PROTOCOL.md Coding rules and evidence requirements
PRELIMINARY_ARCHITECTURE_SIGNALS.md Abstract-based signals; not full-text findings
```

Run `python code/build_dataset.py` from any directory. It preserves raw files, converts WoS to CSV, rebuilds the common tables and checks exported row counts against the observed counts. Repeated execution is deterministic.

Deduplication uses normalized exact DOI; records without DOI use database plus native identifier. Exact normalized title/year collisions across remaining groups are flagged **without automatic merging**. Consequently, the unique count is conservative and may contain unresolved duplicates. Titles, conflicting years and authors are not overwritten in the raw exports. One representative row uses the longest available abstract; all source occurrences remain recoverable through membership links. Multiple query hits on the same paper are not independent evidence of uncertainty propagation.

Missing DOI or abstract is retained as missing. Complete export means all matching records and all fields supported by the selected native export, not that every publisher supplies every field. The final verified counts are in `REPORT_FA.md` and the machine-readable logs.

## Relationship to existing repository work

Read this alongside `Digital Twin Architecture/README.md`, `S1_S5_CONNECTION_MATRIX.md`, `UNCERTAINTY_TRACEABILITY_MODEL.md`, the DT-L3/DT-L4 layer notes, and `analysis_ready/fulltext_uncertainty_results/README.md`. Earlier uncertainty transition counts and the 18-record general DT mechanism corpus are separate evidence sets; they are not merged with this retrieval or presented as findings from it.

The next analytical step is full-text architecture coding with page/figure/equation locators. A proposed uncertainty interface must remain labelled as our synthesis until a specific paper demonstrates it.
