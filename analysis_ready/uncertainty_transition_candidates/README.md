# Uncertainty transition candidate papers

This folder contains the papers currently identified as candidate uncertainty-transition studies across S1-S3.

## Candidate rule

A paper is included in a transition CSV only when it is present in both the Broad and uncertainty-focused corpora for every stage in that candidate transition.

Examples:

- S1→S2 candidate = S1b ∩ S1u ∩ S2b ∩ S2u
- S2→S3 candidate = S2b ∩ S2u ∩ S3b ∩ S3u
- S1→S2→S3 candidate = S1b ∩ S1u ∩ S2b ∩ S2u ∩ S3b ∩ S3u

This is stricter than simple U-layer overlap and prevents the current S3 subset inconsistency from being treated as transition evidence.

## Interpretation

These are candidate transition papers, not yet verified uncertainty-propagation studies.

Cross-stage corpus membership shows that a paper is retrieved by multiple stage-specific searches and contains uncertainty-oriented terminology. It does not by itself demonstrate that uncertainty is transferred downstream.

Full-text validation is still required to code:
- Preserved
- Legitimately reduced
- Amplified
- Transformed
- Masked / lost
- Unassessed

## Files

- S1_to_S2/: adjacent S1→S2 candidates
- S2_to_S3/: adjacent S2→S3 candidates
- S1_to_S3/: non-adjacent bridge candidates
- S1_to_S2_to_S3/: three-stage chain candidates
- all_transition_candidates_master.csv: unique candidate papers with transition membership
- transition_candidate_summary.csv: counts by transition
- structural_exclusions.csv: apparent U-overlap records excluded because Broad/U subset consistency fails

## Current counts

- S1→S2: 9
- S2→S3: 10
- S1→S3: 2
- S1→S2→S3: 1

All rows have Full-text validation status = Pending.
