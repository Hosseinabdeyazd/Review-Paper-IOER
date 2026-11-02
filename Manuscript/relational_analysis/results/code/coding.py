"""Explicit semantic coding of archived extractions; no keyword classification.

R = operational method/function described in the extraction, not independent
validation. C = conceptual/review/proposed. Unlisted features are NR (not
positively recorded), never claims of absence in the full literature.
"""

SDT_FEATURES = [
 ('obs','Observation / attribute inference'),
 ('sem','Semantic objects / material information'),
 ('qty','Quantity / inventory model'),
 ('time','Time / event / service-life model'),
 ('reuse','Recovery / reuse information'),
 ('impact','Environmental consequence model'),
 ('link','Cross-model / data exchange'),
 ('trace','Identity / version / provenance'),
 ('view','Visualization / decision interface'),
]
STAGES=['S1','S2','S3','S4','S5','X']

# Aliases follow the source table order. B02 and B07 remain pending and excluded.
# Each tag is stage:feature. X denotes adjacent construction/cost/schedule functions.
SDT=[
 ('B01','DTMFB-2394c459ec04','Parametric assemblies','domain/enabling',
  'S1:obs S1:sem S2:sem S2:qty S2:link S2:trace','S3:time',
  'GIS attributes infer assemblies; mass is computed and hierarchically located. Temporal MFA/LCA is enabled but not demonstrated as dated outflows.'),
 ('B03','DTMFB-7b8729bf813b','District urban mining','domain/enabling',
  'S1:obs S1:sem S2:sem S2:qty S2:link S2:trace S3:time S3:link S3:trace','S4:reuse',
  'CityGML/component alternatives yield masses; service lives yield annual CSV flows. Recovery is a scenario context, not a verified recovery-state mechanism.'),
 ('B04','DTMFB-786eef4ce139','Residential BIM / reuse','domain/enabling',
  'S1:obs S2:sem S2:qty S2:trace S4:reuse S4:sem','S3:time',
  'Survey and BIM yield quantities and reusable-component information. Residual life is discussed; no dated probabilistic outflow model is established.'),
 ('B05','DTMFB-2c878ddf4181','BIM–GIS stock model','domain/enabling',
  'S1:obs S2:sem S2:qty S2:link S2:trace S3:time','',
  'Scan/BIM material intensities map to GIS quantities. S3 time coding refers to retrospective demolition change detection, not a lifetime forecast.'),
 ('B06','DTMFB-ba08181cf4ef','Audio material sensing','complement',
  'S1:obs','',
  'Audio processing/CNN infers material class; no downstream mass calculation or material-stock DT is established.'),
 ('B08','DTMFB-856d2825c306','BIM–AI cost model','complement',
  'X:obs X:sem X:link','',
  'Document/BIM extraction feeds cost models. These cost-related functions are kept adjacent and not relabelled as material-stock stages.'),
 ('B09','DTMFB-f82bf5f38bf3','Construction logistics twin','complement',
  'X:obs X:sem X:qty X:time X:link X:trace X:view','',
  'Product/package identity, quantities and planning dates connect through databases, WebAPI and mobile capture. Timing concerns construction logistics, not stock retirement.'),
 ('B10','DTMFB-0e906b271b76','BIM stochastic scheduling','complement',
  'X:qty X:time X:link X:trace X:view','',
  'Illustrative BIM/productivity-to-schedule chain with IDs, units and versions. Quantity is deterministic; scheduling is not S3 turnover.'),
 ('B11','DTMFB-f1a803053705','BIM / VR material bank','domain/enabling',
  'S2:sem S2:qty S2:trace S4:reuse S4:view','',
  'BIM/BoQ connects quantities to material-bank/disassembly visualization. This is reuse information, not measured recovery yield or calibrated reuse probability.'),
 ('B12','DTMFB-8ac6d6a19330','BIM / carbon substitution','domain/enabling',
  'S2:sem S2:qty S2:link S5:impact S5:link S5:time','',
  'Material substitutions couple quantities/structure/energy/carbon. S5 timing means fixed replacement events in a 60-year assessment, not stochastic S3 retirement.'),
 ('B13','DTMFB-14cd06b4ebfd','Point-cloud pipe inventory','complement',
  'S1:obs S1:sem S1:trace S2:qty','',
  'Scans yield pipe count/location/orientation and timestamps. S2 denotes count inventory only; no mass UQ or lifetime model is inferred.'),
 ('B14','DTMFB-e67012835c1e','Semantic city reconstruction','complement',
  'S1:obs S1:sem S1:trace','',
  'Image inference and human QA yield semantic city objects. Material mass/flow modelling is not executed.'),
]

DTU_FEATURES=[
 ('prob','Probabilistic U\nrepresentation'),
 ('bayes','Bayesian state /\nparameter inference'),
 ('joint','Explicit joint /\ndependence transport'),
 ('detect','Residual / shift\ndiagnostics'),
 ('adapt','Online model /\nparameter adaptation'),
 ('cover','Empirical interval\ncoverage assessment'),
 ('decision','Confidence / U\nlinked alerts or actions'),
]
# Per-feature reasons are stored next to every positive coding decision.
DTU=[
 ('DTUM-001','Physics-informed review','Review / reference architecture',{
  'prob':('C','Distinguishes U sources and joint posterior representations; secondary review, pp23–27.'),
  'bayes':('C','Calibration/assimilation framework; no new operational implementation.'),
  'joint':('C','Joint parameter/discrepancy posteriors and cross-covariances discussed, pp23–27.'),
  'detect':('C','Innovation, bias and autocorrelation diagnostics, pp31–33.'),
  'adapt':('C','Asset/model/update framework, pp9–10; secondary synthesis.'),
  'cover':('C','Coverage/width/scoring recommended; not a new empirical coverage test.'),
  'decision':('C','Evidence-based deployment gates, pp38–44.')}),
 ('DTUM-009','Soft-sensor review','Review / reference architecture',{
  'prob':('C','Conformal/quantile/ensemble U options discussed, not jointly implemented.'),
  'detect':('C','Input/latent drift and hybrid residual checks, pp3–5.'),
  'adapt':('C','Governed model updating discussed in synthesis.'),
  'decision':('C','Fallback and governed interpretation of confidence discussed.')}),
 ('DTUM-010','Water-quality review','Review / reference architecture',{
  'prob':('C','Posterior covariance and exceedance probabilities proposed.'),
  'bayes':('C','Kalman state/bias estimation reference architecture, pp5–7.'),
  'joint':('C','Payload proposals include covariance; multivariate dependence is a requirement, pp7–8.'),
  'detect':('C','Innovation/outlier/change-point mechanisms described in review.'),
  'decision':('C','Probabilistic alerts with hysteresis and persistence proposed.')}),
 ('DTUM-002','Hybrid fuel-system twin','Hybrid model fusion',{
  'prob':('R','Particle posteriors and health-indicator uncertainty bands, pp10–13.'),
  'bayes':('R','Parallel DBN/particle-filter hidden-parameter updates, pp3–13.'),
  'detect':('R','Prediction–observation residuals trigger adaptation, p14.'),
  'adapt':('R','Adaptive hidden parameters and posterior-residual fusion weights, p14.'),
  'decision':('R','Health bands and screening thresholds, pp26–30; not certified risk limits.')}),
 ('DTUM-004','Conditional state–parameter inference','Inference component',{
  'prob':('R','Joint posterior q(X,theta)=nu(theta)rho(X|theta), examined preprint pp6–14.'),
  'bayes':('R','Variational parameter marginal plus conditional KF/UKF/EnKF state update.'),
  'joint':('R','Parameter–state dependence retained by conditional factorization, pp22–24.'),
  'adapt':('R','Sequential parameter/state updating; numerical inference component, not deployed DT.')}),
 ('DTUM-008','Self-protection architecture','Feedback / control',{
  'detect':('R','Prediction-accuracy deterioration is monitored, p1.'),
  'adapt':('R','Deterioration triggers DMDc re-identification, pp1–2.')}),
 ('DTUM-015','Conflict-aware O-RAN control','Feedback / control',{
  'prob':('R','Dirichlet evidence produces uncertainty, pp4–8; calibration not established.'),
  'detect':('R','Group-attribution distribution shift diagnostics.'),
  'adapt':('R','Selective retraining based on distribution shift.'),
  'decision':('R','Uncertainty modifies action thresholds; adjacent control architecture, not primary DT deployment.')}),
 ('DTUM-016','Parallel twins for NMPC','Feedback / control',{
  'prob':('R','Parameter/performance covariance represented, pp3–10.'),
  'bayes':('R','UKF update combines twin evaluations with real-vehicle performance.'),
  'joint':('R','Sigma points propagate covariance and cross-covariance into performance statistics.'),
  'detect':('R','Simulation–reality discrepancy adjusts exploration/noise; not generic source attribution.'),
  'adapt':('R','Measured performance updates tuning parameters with UKF/SPSA.'),
  'decision':('R','Tuning/candidate acceptance uses uncertain inferred performance and constraints; no universal safety proof.')}),
 ('DTUM-011','Bio360 event framework','Layered monitoring',{
  'prob':('C','Bayesian integration is described but likelihood/posterior specification is not established; confidence score is not a calibrated probability.'),
  'bayes':('C','Bayesian integration description lacks full operational likelihood/posterior details.'),
  'detect':('R','Standardized deviations and persistence-based event assessment, pp2–5.'),
  'decision':('R','Reliability/persistence-weighted confidence feeds alerts; clinical calibration unestablished.')}),
 ('DTUM-012','Field water-quality twin','Layered monitoring',{
  'prob':('R','State/bias covariance informs threshold exceedance, pp2–4.'),
  'bayes':('R','Kalman state/bias estimation.'),
  'detect':('R','Robust innovations and residual/change-point checks.'),
  'adapt':('C','Adaptive calibration is future work; not counted as executed online model adaptation.'),
  'cover':('R','Nominal-95% coverage reported for three holdout categories, p5; dataset detail limited.'),
  'decision':('R','Probabilistic alerts with hysteresis/persistence, pp2–4.')}),
 ('DTUM-018','CNC tool-health twin','Layered monitoring',{
  'prob':('R','KF state covariance plus dropout entropy/RUL intervals, pp11–13.'),
  'bayes':('R','Kalman state estimation in the DT core.'),
  'detect':('R','Innovation covariance and normalized innovation squared consistency checks.'),
  'adapt':('R','Q/R adaptation follows consistency checks; interpretation limitations retained.'),
  'cover':('R','90% interval coverage reported as 90.9±2.1%, p19; not independently reproduced.'),
  'decision':('R','Entropy-based maintenance deferral, p19.')}),
 ('DTUM-013','Hierarchical posterior evolution','Bayesian learner',{
  'prob':('R','Hierarchical Gaussian/inverse-gamma and mixture representation, pp3–5.'),
  'bayes':('R','Bayesian neural posterior learner under nonstationarity.'),
  'detect':('R','Transport distance from an anchor defines stable/warning/alarm regimes.'),
  'adapt':('R','Regime-dependent weighting and distribution-scale adjustment.'),
  'cover':('R','PICP reported, p6; other ablation inconsistencies remain in the appraisal.'),
  'decision':('R','Warning/alarm regime changes model response; not a validated safety guarantee.')}),
 ('DTUM-014','Adaptive physical-prior BNN','Bayesian learner',{
  'prob':('R','Posterior sampling yields prediction bands, pp3–6.'),
  'bayes':('R','Physics-based pretraining and supervised Bayesian learning.'),
  'detect':('C','Out-of-band/wide-band diagnostics suggested; runtime drift detection unvalidated.'),
  'adapt':('C','Online drift feedback is future work; training-weight adaptation not counted as online adaptation.'),
  'decision':('C','Uncertainty-band triggers proposed, pp8–9.')}),
]

NEGATIVE_NOTES={
 ('DTUM-002','joint'):'Cross-branch dependence is not demonstrated; shared measurements prevent an independence assumption.',
 ('DTUM-008','decision'):'Protection uses predicted behaviour/fast-forward simulation; no explicit confidence/U-conditioned decision rule established.',
 ('DTUM-012','joint'):'A complete serialized covariance/dependence contract across tiers is not demonstrated.',
 ('DTUM-013','joint'):'Mixture compression and within-learner evolution do not demonstrate joint dependence transfer across heterogeneous modules.',
 ('DTUM-014','cover'):'Plotted nominal bands do not establish measured coverage.',
 ('DTUM-018','joint'):'KF-to-neural interface passes means; explicit KF covariance transfer is not demonstrated.'
}
