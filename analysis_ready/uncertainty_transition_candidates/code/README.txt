# Rebuild uncertainty-transition candidate CSVs from analysis_ready/final.
# Candidate inclusion requires Broad + U membership in every stage in the transition.
# See README.md for interpretation and full-text validation requirements.
#
# Current source datasets:
# S1b, S1u, S2b, S2u, S3b, S3u
#
# Deduplication key:
# 1) normalized DOI when available
# 2) normalized title otherwise
#
# The generated transition sets are:
# S1_to_S2       = S1b & S1u & S2b & S2u
# S2_to_S3       = S2b & S2u & S3b & S3u
# S1_to_S3       = S1b & S1u & S3b & S3u
# S1_to_S2_to_S3 = S1b & S1u & S2b & S2u & S3b & S3u
#
# The current CSVs are generated from the repository snapshot dated 2026-10-06.
