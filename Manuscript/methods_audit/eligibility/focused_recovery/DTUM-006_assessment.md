# DTUM-006 — publisher full-text HTML assessment

Title: On the synthesis of the measurements and structural models using statistical finite element method.
Author: Ahmet Oguzhan Yuksel. Mechanics Research Communications 152 (2026), 104638.
DOI: https://doi.org/10.1016/j.mechrescom.2026.104638
Source actually read: https://www.sciencedirect.com/science/article/pii/S0093641326000285

The publisher's complete HTML body, sections 1–6 and the appendix formulation, was read. The PDF viewer displayed an 11-page article, but local PDF download did not succeed. This file contains assessment notes, not a replacement publisher PDF. Any hash attached to this file identifies these notes only.

## Decision and role

Include in the focused general DT–U methodological stream as a numerical, transferable model–measurement assimilation mechanism. It is not direct building-material-chain evidence, not an implemented operational digital twin and not a demonstration of uncertainty continuity across S1–S5.

## Mechanism and locators

- Sections 2–3, equations 5–12: uncertain Young's moduli are represented by a Gaussian random field over lattice connectivity. An SPDE-derived Matérn precision matrix preserves spatial/connectivity correlation. The adjoint graph places random variables on members rather than joints.
- Section 4.1, equations 13–20: uncertain stiffness is mapped into displacement covariance through a first-order Taylor Jacobian, C_u = J C_r J^T. Figure 3 compares this approximation against Monte Carlo and shows increasing discrepancy as input coefficient of variation rises.
- Section 4.2, equations 21–26: y = H u + d + e distinguishes the projected model response, model discrepancy and measurement noise. Gaussian likelihood and prior yield posterior displacement mean and covariance. Thus uncertainty is transformed by the forward model and reduced/redistributed by observations; it is not discarded at the measurement/model interface.
- Section 5: all observations are synthetic. Timoshenko beam simulations generate measurements and an Euler–Bernoulli model is updated, deliberately introducing model mismatch. The examples are a 100-element beam, a 5,892-member BCC cantilever with nine sensor sites, and a 20,354-member octet bench. The text says fifteen sensors for the bench while the figure caption says twelve; no sensor-count-dependent quantitative claim is extracted from that example.
- Section 5, figures 5, 7 and 10: posterior fields and 95% intervals are compared with prior and synthetic truth. These are numerical demonstrations, not experimental validation or quantified material recovery benefits.
- Section 6: applicability is limited by Gaussian assumptions and first-order linearisation at moderate uncertainty. Higher-order/nonlinear extensions and experimental validation are future work. Maximum-likelihood covariance estimation can be unrepresentative from a single realisation (section 4.2).

## Transfer to the review's architecture

The transferable interface contract is a correlated input distribution plus an observation operator, model-discrepancy term and measurement-noise model. The output must retain both posterior mean and covariance. Applying that contract to inventory, outflow, recovery or LCA interfaces is a synthesis proposal; the article itself does not implement these stages.

## Retrieval status

Full-text HTML accessible and assessed. Publisher PDF visible in browser, but not archived locally. Direct DOI, publisher PDF-link download and a fresh signed asset retrieval did not produce a saved local PDF. Do not label this as a downloaded PDF or as a full-text non-retrieval in eligibility counts.
