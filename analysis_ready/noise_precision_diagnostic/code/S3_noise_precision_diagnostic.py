from pathlib import Path
from diagnostic_core import run_stage
B=Path(__file__).resolve().parents[1]
run_stage("S3",B/"analysis_inputs/current_merged/S3b.csv",B/"analysis_inputs/current_merged/S3u.csv",B/"outputs/S3",
{"lifetime":r"\b(lifetime|life time|service life|lifespan|life span)\b","demolition":r"\b(demolition|dismantl|deconstruction|retirement)\b","survival_hazard":r"\b(survival|hazard|weibull|lognormal|mortality)\b","turnover_cohort":r"\b(turnover|replacement|renewal|vintage|cohort)\b","dynamic_mfa":r"\b(dynamic material flow|dynamic mfa|stock[- ]driven|inflow[- ]driven|material flow analysis)\b","outflow_forecast":r"\b(material outflow|outflow|demolition waste|waste flow|future material flow|scenario|forecast|projection)\b"},
{"operational_energy":r"\b(thermal comfort|hvac|operational energy|building energy simulation|building energy model)\b","generic_energy_system":r"\b(electricity market|power grid|energy system optimization|energy dispatch)\b","generic_health":r"\b(patient|clinical|medical|disease survival)\b"})
