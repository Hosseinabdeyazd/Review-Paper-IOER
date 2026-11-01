# Full-text architecture and uncertainty review

Review date: 2026-11-01. Scope: 13 locally verified full texts from the 18-record DT-UM corpus. Twelve are publisher PDFs; DTUM-004 is arXiv:2512.25056v2, not the journal version. The request refers to 15 papers, but the additional two have not yet been identified. This report does not claim that 15 papers were read. Five corpus records remain unavailable as local PDFs: DTUM-003, 005, 006, 007 and 017. Missing full text is not an exclusion decision.

The main texts of all 13 available papers were examined, including methodological details, results and limitations. Page references below are PDF pages of the local versions. This is a single-reviewer extraction, not an independently replicated assessment or reproduction of the studies' experiments. Relevance judgments and S1–S5 transfer suggestions are reviewer interpretations. The original source exports remain unchanged.

## Findings for the research question

No examined paper establishes end-to-end uncertainty continuity across the proposed S1 GeoAI → S2 material stocks → S3 dynamic MFA → S4 reuse/circularity → S5 LCA network. Useful building blocks exist, but their integration would be a research contribution, not an already validated conclusion from this corpus.

An architecture can make uncertainty observable when it combines (1) explicit stochastic representations, (2) measurement-to-model comparison, (3) sequential updating, (4) dependence-preserving interfaces and (5) calibrated decision rules with traceable versions. These are separate requirements: small prediction errors, narrow posterior intervals and successful fault classification do not by themselves establish all five.

For implementation examples, prioritize **DTUM-002, DTUM-018, DTUM-013 and DTUM-016**. For the mathematics of preserving dependence, prioritize **DTUM-004**. For the organizing framework and credibility assessment, prioritize **DTUM-001**, supported by DTUM-009 and DTUM-010. These priorities reflect relevance to the research question rather than an overall study-quality score.

## DTUM-001 — Physics-informed digital twins: PRISMA-ScR review

DOI: https://doi.org/10.1007/s11831-026-10754-w

**Architecture and mechanism.** The asset–model–data–update–uncertainty–decision framework links physics-informed learning, operators, calibration, assimilation and deployment (pp. 9–10). It distinguishes parameter, discrepancy, measurement and numerical/reduction uncertainty (pp. 23–27). Joint parameter/discrepancy posteriors and cross-covariances matter; the reduced-order representation also contains reconstruction error. Innovation consistency, bias, autocorrelation and observability diagnose whether updates remain credible (pp. 31–33). Coverage, interval width and scoring rules should be assessed together and by operating regime. Deployment gates require evidence beyond model accuracy (pp. 38–44).

**Evidence and limits.** Secondary synthesis of 79 reports, not 79 additional independent records in our 18-paper corpus. Single-author screening and capped ranked retrieval limit completeness. No new operational DT is experimentally validated here.

**Relevance and continuity judgment.** High conceptual relevance. Useful for defining what must cross each S1–S5 interface and for separating calibration, updating and decision evidence. It supplies assessment principles rather than an implemented continuity service.

## DTUM-002 — Hybrid methanol fuel-supply DT

DOI: https://doi.org/10.1016/j.apenergy.2026.128822

**Architecture.** Synchronized 1-Hz measurements feed parallel conservation-law and fixed TCN models. Each branch has a dynamic Bayesian network with particle-filter updates of hidden parameters. Pump-specific adaptive fusion combines posterior outputs, followed by health indicators and screening thresholds (pp. 3–13; Figs. 1, 3). The physical branch's parameters describe hydraulic/thermal behavior; the TCN branch's parameters are empirical output corrections and must not be interpreted as direct physical damage.

**Detection and monitoring.** Predicted–observed deviation triggers adaptive updates (p. 14). Particle posteriors track parameter changes. Current posterior residuals determine fusion weights; these residuals already use assimilated current measurements, so the reported tracking performance is not an independent future-prediction test. Posterior health-indicator means and ±2σ bands summarize monitoring; 0.8/0.4 thresholds are screening rules, not certified safety limits (pp. 10–13, 26–30).

**What the architecture reveals.** Under first-pump bypass leakage, the data branch also lowers the second pump's health indicator because it can confuse downstream coupling with local degradation. Physical interpretation plus fusion separates the affected pump more effectively in this experiment (pp. 28–31). This is a particularly relevant example of why source attribution needs model structure rather than uncertainty bands alone.

**Validation.** A water-based laboratory rig, changing flow and one persistent leakage scenario. The leak starts before the fault recording, so this does not validate general fault-onset detection delay. Normal-operation fused RMSEs are 0.104/0.110 Hz, 0.022/0.031 bar and 0.017/0.015 °C (Table 13, p. 24). The complete serial online calculation is 93.32 ms/step, excluding training, initialization and I/O (p. 23). EKF/EnKF are faster and sometimes more accurate than PF; PF is retained for posterior-based health propagation. Data-PF worsens some pressure errors (pp. 19, 23).

**Continuity judgment.** Explicit within-branch posterior propagation and transformation to health indicators. Cross-branch dependence and calibrated fused-interval coverage are not demonstrated. Shared measurements make independence unsafe to assume. Narrower posteriors do not independently prove that uncertainty has been legitimately reduced. Methanol, shipboard operation, sensor drift and multi-component faults remain future validation (p. 31).

**Relevance.** High: heterogeneous model fusion, source attribution and monitoring. Transfer to S1–S5 would require explicit joint dependence and interface contracts rather than copying residual weights directly.

## DTUM-004 — Sequential Bayesian parameter–state estimation

Journal DOI in corpus: https://doi.org/10.1016/j.jcp.2026.115057. Version actually examined: https://arxiv.org/abs/2512.25056v2 (39 pages).

**Architecture.** FBOVI approximates the joint posterior as q(X,θ)=ν(θ)ρ(X|θ). Stage 1 updates the parameter marginal by variational inference; Stage 2 updates the state conditional on parameters using KF, UKF or EnKF. Neural networks represent conditional means and covariance factors to keep the representation size fixed over time (pp. 6–14, Fig. 8). EnKF particles are regenerated each step; the parameter distribution and conditional functions, rather than the same particles, pass to the next step.

**Uncertainty mechanism.** Conditioning retains parameter–state dependence instead of imposing independent marginal distributions. Even with Gaussian conditionals, integration over parameters can produce non-Gaussian joint and state distributions (pp. 22–24, Fig. 16). Theorems bound cumulative approximation error under stated assumptions (pp. 7, 11; Appendices B–C). They are not a universal tight operational confidence certificate. Neural approximation, Gaussian filtering and variational-family restrictions introduce separate errors (pp. 34–35).

**Validation.** Numerical pendulum experiments, 10-state Lorenz ’96 and a 51-state convection–diffusion example with partial observations (pp. 17–30). One pendulum comparison uses 50 independent data realizations. Early posterior uncertainty is overestimated in one case (p. 18). Model mismatch tests use altered discretization and increased process noise; they do not establish automatic identification of arbitrary model-form error (pp. 22–23). Large online training budgets and network sizes are disclosed in Appendices G–H; constant per-step structure does not mean low latency.

**Relevance and continuity judgment.** High mathematical relevance for dependence-preserving transfer and sequential approximation-error accounting. This is an inference component, not a demonstrated deployed DT architecture with anomaly alarms, maintenance decisions or an S1–S5 interface system. Journal-version differences remain unchecked.

## DTUM-008 — Self-learning architecture for self-protection

DOI: https://doi.org/10.1109/acsos-c52956.2021.00075

Monitoring, Modelling, Verification, Imagining, Falsification and Reconsidering form a feedback architecture. Prediction-accuracy deterioration triggers DMDc re-identification (p. 1). A simulated boiler evaluates the approach (p. 2). The protection experiment temporarily uses a fast-forward simulation to obtain accurate future information, which limits claims about the learned predictor's operational protection ability.

There is useful residual-driven model maintenance, but no explicit posterior, coverage calibration or cross-model uncertainty representation. Relevance is supporting architectural feedback, not a core demonstration of probabilistic continuity.

## DTUM-009 — AI soft sensors

DOI: https://doi.org/10.1109/ai4im69129.2026.11558210

The review links synchronized/quality-controlled measurements, soft sensing, monitoring, drift assessment and governed model updates to DT/control applications (Fig. 1; pp. 3–5). It discusses sensor noise, model uncertainty and distribution shift, including input/latent-space drift and hybrid residual checks when ground truth is unavailable. Traceability, versioning, reference measurements and fallback behavior support interpretation of model confidence.

This is a conceptual/metrological synthesis, not a newly validated online detector. Conformal, quantile and ensemble approaches are options, not jointly implemented components. Reported literature percentages lack sufficiently clear denominators for use as prevalence estimates. Relevance is high for measurement provenance and interface specifications, with implementation and continuity evidence still unassessed.

## DTUM-010 — Water-quality DT review

DOI: https://doi.org/10.1109/i-smac65734.2025.11597612

An edge–fog–cloud reference architecture connects quality checks, state/bias estimation and probabilistic alerts. Kalman innovations, robust outlier screening and change-point methods distinguish noise, drift and sustained events (pp. 5–7). Posterior covariance informs exceedance probabilities; hysteresis and time-over-threshold reduce transient alarms. Proposed payloads explicitly include estimates, covariances, residuals, sensor/time information and communication health, with model/threshold version traceability (pp. 7–8).

This is one of the clearest interface proposals in the corpus. Multivariate dependence must be retained or handled conservatively. However, the paper is a review/reference architecture, not an end-to-end experimental validation. Its relationship with DTUM-012 should be considered when avoiding double-counting independent evidence. High conceptual relevance for uncertainty-carrying interfaces.

## DTUM-011 — Bio360

DOI: https://doi.org/10.1109/ichi69079.2026.00214

Wearable/activity, nutrition and clinical information are harmonized into personal baselines and contextual event evaluation. Standardized deviations and a reliability/persistence-weighted event confidence score support alerts (pp. 2–5). The weighted score is not shown to be a calibrated event probability. Bayesian integration is described, but its full likelihood, posterior calibration and clinical validation are not established.

Useful for heterogeneous-data harmonization and contextual interpretation. Low direct relevance to demonstrated uncertainty continuity; transfer across its data streams remains unassessed. Do not interpret a normalized score as a posterior without evidence.

## DTUM-012 — Robust field-focused water DT

DOI: https://doi.org/10.1109/icsedis68157.2026.11518496

Probe/emulation, edge, fog and cloud tiers combine QA, buffering, Kalman state/bias estimation, robust innovations, smoothing, registries and alert policies (pp. 2–4). The state includes pH, TDS and slow bias; residual/change-point checks feed probabilistic threshold exceedance with hysteresis and persistence. The paper reports nominal-95% coverage of 94.8%, 95.2% and 93.9% across synthetic, semi-synthetic and real holdout categories (p. 5), plus lower false alarms and delay.

The specific real dataset, sample counts and implementation detail are insufficiently clear for an independent replication. Adaptive calibration is future work. Architecture relevance is high, while evidence strength is qualified. A complete serialized covariance contract across tiers is not demonstrated, even though lineage/API concepts are discussed.

## DTUM-013 — DHPE

DOI: https://doi.org/10.1109/isctis70043.2026.11571854

Hierarchical Gaussian/inverse-gamma uncertainty, quasi-Monte Carlo projection and Gaussian-mixture representation feed geometric distribution evolution. Wasserstein/transport distances from an anchor define stable/warning/alarm modes and adaptation of history/physics/likelihood contributions; finer transport deformation adjusts uncertainty scale (pp. 3–5). This is explicit monitoring of distribution evolution rather than point residuals alone.

Titanium-furnace historical and enhanced scenarios include operating changes, degradation and bias. Table I reports RMSE 0.86 and PICP 95.1% (p. 6). However, Table V's no-closed-loop peak value is 4.25, whereas the full-model peak reported in Table IV is 10.2; the accompanying claim that removing the loop amplifies that peak needs clarification (pp. 7–8; table visually checked). Treat the ablation narrative cautiously.

High mechanism relevance, qualified evidence. The distribution is compressed to a Gaussian for macro monitoring, which can hide mixture structure; the amount of information lost is not audited. Temporal continuity within this learner is not yet evidence of continuity across heterogeneous DT models.

## DTUM-014 — Adaptive weighted physical prior for Bayesian learning

DOI: https://doi.org/10.1109/ispds67367.2025.11391182

Physics-based pretraining and supervised Bayesian learning are coupled by Wasserstein alignment. Adaptive weighting uses curvature, training progress and rollback; posterior sampling provides prediction bands (pp. 3–6). These diagnostics primarily govern training, not a validated runtime change detector.

The paper reports prediction-error improvements, including RMSE 1.21955, but does not establish empirical interval coverage merely by plotting a nominal band (pp. 7–8). Out-of-band or wide-band triggers are suggested; online concept-drift feedback remains future work (pp. 8–9). Moderate relevance as a UQ component. Shared authors/topic with DTUM-013 do not constitute independent end-to-end confirmation.

## DTUM-015 — Explainable conflict-aware O-RAN

DOI: https://doi.org/10.1109/ojcoms.2026.3698326

Non-real-time training/monitoring and near-real-time control exchange models/statistics. Group-attribution distribution shifts support selective retraining. Dirichlet evidence produces uncertainty that modifies action thresholds, with switching costs and conflict resolution (pp. 4–8). This is an adjacent control architecture, rather than a primary DT deployment.

Simulation and external ColORAN evaluation show shift sensitivity; increasing uncertainty under shift does not establish calibrated coverage. Selective retraining improves accuracy in one result while increasing QoS violations (p. 15). A full multi-xApp operational loop remains future work (p. 18). Monotonic individual additive functions do not establish monotonicity of the whole network when cross-group interactions are unconstrained. Action-label/direction descriptions around pp. 7–8 need replication clarification.

Supporting relevance for uncertainty-aware action and model-version feedback. Cross-component covariance continuity is unassessed; avoid treating explainability or monotonic components as a general safety proof.

## DTUM-016 — Parallel DTs for nonlinear predictive control

DOI: https://doi.org/10.1109/tcst.2024.3437163

Parallel executable twins evaluate controller parameter variations. UKF sigma points propagate parameter covariance into performance mean/covariance and cross-covariance; real-vehicle performance then updates parameters, combined with SPSA (pp. 3–10, Algorithm 1). Simulation–reality discrepancy adjusts exploration/noise settings. It compensates for uncertainty effects without necessarily identifying their physical source.

A real SimRod experiment runs the controller at 20 Hz; tuning evaluates 85-second windows. Reported path RMSE improves from 1.365 to 0.295 m (results section). Nominal-twin bounds and non-increasing-cost checks constrain candidate updates, but depend on assumptions about the underlying controller and do not guarantee the fused learning algorithm universally (pp. 10, 15).

High relevance for explicit covariance transport between executable models, measured feedback and decisions. The represented covariance describes the tuning/inference problem, not every source of physical discrepancy. Neither generic change-point detection nor full uncertainty-source attribution is demonstrated.

## DTUM-018 — CNC tool-health DT

DOI: https://doi.org/10.3390/machines14030335

Physical, connectivity, DT-core and application layers combine multirate sensing, time synchronization, Kalman state estimation, deep prediction and uncertainty-aware maintenance (pp. 6–13). Innovation covariance and normalized innovation squared monitor consistency; Q/R adaptation follows. MC dropout supplies classification entropy and RUL prediction intervals; high uncertainty supports deferral (pp. 11–13, 19).

Reported 90% interval coverage is 90.9±2.1%, with width 7.3; entropy-based deferral covers 6.1% and lowers false alarms by 18% in the stated test (p. 19). These are paper-reported, not independently reproduced. The proposed KF-to-neural interface passes posterior means, with optional tags; an explicit transfer of the KF covariance into the neural predictor is not demonstrated. Two UQ components therefore do not establish a continuous uncertainty chain.

The R-adaptation description does not clearly separate state-prediction uncertainty from innovation covariance. Some training hyperparameters in Appendix A remain symbolic, data are available on request, and general reproducibility is limited. The blanket sub-100-ms statement is qualified by an external Transformer result of 108±7 ms (p. 18). Alert-rule descriptions require reconciliation with Appendix A. Architecture figure and relevant table were visually checked.

High direct mechanism relevance. Especially useful as an example where explicit uncertainty exists at several stages but the connecting interface still needs auditing.

## Proposed S1–S5 extraction rules

These are reviewer-proposed rules, not features already validated by the papers.

| Interface requirement | What to record | Relevant evidence |
|---|---|---|
| Representation | Distribution/ensemble, units, spatial and temporal support, model version | 001, 004, 010 |
| Dependence | Joint samples or covariance; shared observations and assumptions | 004, 016; unresolved fusion issue in 002 |
| Detection | Innovation, bias, coverage, distribution distance, threshold and persistence | 012, 013, 018 |
| Transformation | Function mapping uncertain input to output, added discrepancy and approximation | 001, 002, 004 |
| Decision | Probability/quantile/score semantics, calibration, abstention and fallback | 010, 015, 018 |
| Provenance | Source IDs, versions, update time, evidence supporting each uncertainty change | 001, 009, 010 |

For S1 building observations → S2 stocks, preserve correlated geometry/classification uncertainty instead of only point estimates. For S2 → S3, distinguish inventory uncertainty from future lifetime/scenario uncertainty. For S3 → S4 and S4 → S5, preserve scenario identity and dependencies instead of mixing unrelated quantiles. Direct S2 → S5 links also require explicit contracts. These are design hypotheses to test, not results established by this domain-diverse set.

Code each interface as one or more of **preserved, legitimately reduced, amplified, transformed, masked/lost, unassessed**. Require evidence before assigning loss or legitimate reduction. An undocumented transfer is **unassessed**, not automatically lost. Keep source statements, observed implementation and reviewer interpretation in separate fields when extending the extraction table.

## Remaining scope and acquisition

The local verified set is 13, not 15. The five unavailable corpus full texts remain eligible for acquisition and later assessment. Publisher/SLUB routes were pursued; browser-visible PDFs were not treated as downloaded files when saving failed. DTUM-006 also had an SSRN route that did not yield a local PDF. DTUM-017's proceedings attachment required meeting-specific access. No abstract-only architecture description is substituted for a full-text judgment in this report.

Publisher PDFs remain in the local fulltext/local_pdfs directory. This repository report contains analytical paraphrases and identifiers, not copies of subscription PDFs.

