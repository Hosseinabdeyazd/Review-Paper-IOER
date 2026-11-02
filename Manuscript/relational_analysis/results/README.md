# Stages, Digital Twin and uncertainty: visual results

Date: 2026-11-02. **Four descriptive result figures, underlying coding tables and reproducible code.** Conceptual Figures 05–06 have been moved to `../conceptual_synthesis/` and removed from this atlas.

**New data-derived diagrams:** [alluvial distribution, stage–function network, exact mechanism configurations and source–method associations](../data_diagrams/README.md). Every plotted edge/configuration is computed from recorded article-level codes.

These are descriptive results from the current selected evidence sets. They are not prevalence estimates for the entire literature or a validated integrated Digital Twin.

[Open the four-page results atlas](Results_Atlas.pdf) · [Browse all figures](gallery.html) · [Read the interpretation in Persian](REPORT_FA.md) · [LaTeX figure blocks](figures.tex)

## Figures

| Figure | What was computed or synthesized | Evidence unit |
|---|---|---|
| [01 Stages × uncertainty](figures/01_stages_uncertainty.pdf) | Source coverage plus separate continuity assessments | 20 papers; 23 paper–context assessments |
| [02 Stages × DT functions](figures/02_stages_dt_functions.pdf) | Nine domain/enabling functions across S1–S5 and a separate adjacent category | 12 assessed papers; overlapping stage memberships |
| [03 DT architectures × uncertainty](figures/03_dt_uncertainty_mechanisms.pdf) | Seven uncertainty mechanisms, distinguishing described methods from conceptual support | 13 assessed records, including three reviews |
| [04 Mechanism co-occurrence](figures/04_method_cooccurrence.pdf) | Shared-paper counts, Jaccard similarity and average-linkage clustering | 10 non-review method-level records; only R codes |

Every figure is also available as editable SVG and high-resolution PNG. Blue/amber/grey coding in Figures 02–03 distinguishes described functions, conceptual support and unrecorded positive evidence. The conceptual diagrams are retained separately under [conceptual synthesis](../conceptual_synthesis/README.md).

## Findings within this working set

1. **Domain function coverage concentrates at S1 and S2.** Seven of twelve S–DT papers describe a function assigned to S1, seven to S2, two to S3, two to S4 and one to S5. Three papers have adjacent construction/cost/scheduling functions; memberships overlap. S3 includes retrospective event detection; S4 includes reuse information. These counts do not imply seven complete twins, stochastic retirement forecasting, or validated recovery yields.
2. **Uncertainty estimation and monitoring have more recorded method support than explicit dependence transport.** Across the thirteen DT–U appraisals, R-coded methods include probabilistic representation in 8, Bayesian inference in 7, diagnostics in 8, online adaptation in 7, confidence/U-linked decisions in 7, empirical interval-coverage assessment in 3 and explicit joint/dependence transport in 2. Three records are reviews and contribute C, not R. The two dependence codes refer to represented variables, not whole-chain continuity.
3. **Two mechanism pairs co-occur strongly in the ten method-level records.** Probabilistic representation + Bayesian inference and diagnostics + confidence/U-linked decisions each have 7 shared records and Jaccard 7/8 = 0.875. This is descriptive co-occurrence, not a statistical significance result or proof of technical coupling. Related study families have not been reconciled into independent experiments.
4. **The design problem lies at interfaces.** The separate conceptual Figures 05–06 connect the S–U requirements to domain functions and generic uncertainty mechanisms without treating this combination as an already implemented system. S3→S4 remains an evidence gap in the selected S–U set. The proposed response specifies recoverable quantity/quality/routing as a new uncertain state, not merely another label on outflow.

## Scope and coding

Inputs: 21 S–U records (20 assessed), 14 S–DT records (12 assessed), and 18 DT–U records (13 assessed). The assessed memberships total 45 but represent **44 unique publications**, because DOI `10.1016/j.jobe.2025.113391` occurs in two streams. Do not add the panels as independent populations. The source registry contains 52 unique publications across all access statuses.

This update **semantically coded archived extraction/appraisal tables; it did not re-read the PDFs**. S–U codes reuse the documented harmonization in `../content_profiles/`; S–DT and DT–U codes were added in this update. DOI, source ID, title, evidence locator, decision reason and access/version status are retained. Some legacy S–U locators identify the earlier coding table rather than a PDF page. No independent human adjudication was performed. Pending/abstract-only cases are excluded from the content counts and remain in the registers.

R = an operational method/function is described in the archived extraction, including illustrative or numerical work. R does not establish field deployment or independent validation. C = review-level, conceptual, proposed or future functionality. NR = not positively coded from the available extraction; it is **not proof of absence**. The S–U continuity codes have their own definitions in `inputs/su_codebook.csv`; its R code means propagation-ready, not the R definition used in Figures 02–03.

S1 = attribute observation/inference; S2 = inventory; S3 = temporal stock/flow change; S4 = recovery/reuse/routing; S5 = environmental consequences. X is an adjacent construction/cost/scheduling category. DT/enabling functions are assigned to the material-flow task actually described, not to the search label.

The architecture-family labels in Figure 03 are reviewer groupings. The clustering in Figure 04 is computed, but remains exploratory. No chi-square test, residual significance map, causal relationship or stable architectural taxonomy is claimed. Multi-label memberships and small, heterogeneous samples do not support copying the reference article's inferential workflow without additional design work.

## How numbers can be checked

- `S_DT_complete_coding.csv`: all 648 paper × stage × function cells, including NR.
- `DT_U_complete_coding.csv`: all 91 paper × mechanism cells, including NR.
- `S_DT_counts.csv` and `DT_U_counts.csv`: cell counts and supporting IDs.
- `new_coding_record_register.csv`: all 32 S–DT/DT–U records, including seven pending assessments.
- `cooccurrence_and_sensitivity.csv`: all 49 mechanism-pair cells, shared IDs and leave-one-record-out Jaccard ranges.
- `cluster_merges.csv`: deterministic average-linkage merge history using distance `1 − Jaccard`.
- `../conceptual_synthesis/architecture_elements.csv`: sixteen stage, interface, module and cross-cutting elements with support origins, anchors and qualifications.
- `inputs/`: exact source snapshots, including the S–U per-paper assignments and synthesis paths.
- `validation.json` and `verification.json`: input hashes, scope counts and independently recalculated output checks.
- `code/coding.py`: explicit semantic decisions. `code/build_results.py`: aggregation and plotting. `code/verify_results.py`: consistency checks.

Jaccard is the intersection divided by the union of positively R-coded publication sets. NR cells are treated as no recorded positive code, not as verified biological/technical absence. Leave-one-out ranges assess sensitivity to removing one record; they are not confidence intervals or a full cluster-stability analysis. The code deliberately makes no significance test.

## Reproduce

Requires Python, NumPy, Matplotlib and pypdf. From any directory:

```text
python path/to/results/code/build_results.py
python path/to/results/code/verify_results.py
```

The included input snapshots are sufficient; no network connection or database credentials are needed. The build uses existing snapshots unchanged. Delete/replace a snapshot deliberately if updating the underlying evidence, then review the semantic decisions before rebuilding. Figure labels and figures.tex provide insertion-ready material; journal inclusion still requires substantive review of the evidence and claims.
