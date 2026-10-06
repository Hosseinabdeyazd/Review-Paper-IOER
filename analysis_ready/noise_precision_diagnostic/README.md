# S1-S3 noise and precision diagnostic

This folder contains the reproducible quality-control step used before descriptive and cross-stage analysis of the merged S1-S3 corpora.

## Contents

- METHODS_NOTE.md: methodological rationale and reporting rules.
- code/diagnostic_core.py: shared implementation.
- code/S1_noise_precision_diagnostic.py: S1 runner.
- code/S2_noise_precision_diagnostic.py: S2 runner.
- code/S3_noise_precision_diagnostic.py: S3 runner.
- code/cross_stage_bridge_diagnostic.py: candidate cross-stage overlap analysis.
- analysis_inputs/current_merged/: exact snapshots currently used for diagnostic and exploratory analysis.
- analysis_inputs/final_screened/: reserved for datasets that pass diagnostic review and formal screening.
- outputs/: structural diagnostics, subset violations, duplicate groups, bridge candidates, and fixed-seed precision-pilot samples.

Automated flags are diagnostic only and never constitute automatic exclusions.
Cross-stream overlap is a candidate interface only; propagation requires full-text evidence.
