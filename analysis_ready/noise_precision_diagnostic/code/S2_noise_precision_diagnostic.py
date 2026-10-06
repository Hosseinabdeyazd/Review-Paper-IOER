from pathlib import Path
from diagnostic_core import run_stage
B=Path(__file__).resolve().parents[1]
run_stage("S2",B/"analysis_inputs/current_merged/S2b.csv",B/"analysis_inputs/current_merged/S2u.csv",B/"outputs/S2",
{"material_stock":r"\b(material stock|material stocks|urban stock)\b","material_intensity":r"\b(material intensit|material coefficient|kg/m2|kg m-?2)\b","inventory_quantity":r"\b(material inventory|material quantity|material quantities|material composition|component inventory|bottom[- ]up)\b","mfa":r"\b(material flow analysis|dynamic material flow|mfa)\b","archetype_typology":r"\b(archetype|typolog|building type)\b","spatial_bim":r"\b(gis|geographic information|geospatial|building information model|bim)\b"},
{"operational_energy":r"\b(thermal comfort|hvac|operational energy|building energy simulation|building energy model)\b","materials_engineering":r"\b(compressive strength|shear strength|concrete mix|cement paste|microstructure)\b","price_market":r"\b(price prediction|market price|real estate price|housing price)\b","water_waste":r"\b(wastewater|greywater|rainwater|municipal solid waste|food waste)\b"})
