from pathlib import Path
import re,json,xml.etree.ElementTree as ET
O=Path('outputs/Manuscript/full_draft/compact/technical_review')
p=O/'manuscript_en.html';s=p.read_text(encoding='utf8')
a=s.index('<h1>2.');b=s.index('<h1>3.',a);before=len(re.sub('<[^>]+>',' ',s[a:b]).split())
section='''<h1>2. Related work and conceptual foundations</h1>
<p>Circular material assessment connects information produced for different purposes: observations describe buildings, stock models estimate material content, dynamic models predict releases, and recovery and environmental assessments evaluate subsequent use. Integrated studies establish this connection. Mastrucci et al. (2017) link geospatial stock characterization with life-cycle assessment of end-of-life scenarios; Ajayebi et al. (2020) connect building information with spatial and temporal product-stock estimates; and Pei et al. (2024) review stock–LCA integration. Their boundaries differ, but together they motivate comparison of the transformations linking observations to circular decisions.</p>
<p>This comparison organizes the review around five activities: observing and inferring building characteristics (S1), estimating material stocks (S2), modelling stock change and outflows (S3), evaluating recovery and subsequent use (S4), and assessing environmental consequences and supporting decisions (S5). These labels identify comparable activities, not a universal architecture implemented by every study. Workflows may combine, omit or revisit them. GeoAI extends the observational activity through spatial inference, while image-based demolition-waste modelling illustrates its connection to material accounting (Wang et al., 2024; Bogoviku and Waldmann, 2021).</p>
<p>The interfaces introduce substantive assumptions. S1→S2 associates building attributes with material composition or intensity. Schiller et al. (2019) show that transferring composition indicators between German and Japanese residential buildings requires harmonization and attention to building type and context; coefficients are not universally interchangeable. Building-size–intensity relationships and lifespan assumptions also influence stock and release estimates (Miatto et al., 2023; Miatto et al., 2017). At S2→S3, a stock becomes a dated flow. Shared attributes and parameters can therefore create dependencies between upstream and downstream estimates that should not be discarded during model coupling.</p>
<p>At S3→S4, an estimated outflow must be distinguished from an available secondary resource. Material passports address information needed for end-of-life management, while probabilistic reusability assessment evaluates technical suitability (Honic et al., 2021; Rakhshan et al., 2021). Condition, separation and quality influence the recoverable quantity and its destination. S4→S5 then connects those outcomes to environmental accounting, including the treatment of subsequent use and substitution (De Wolf et al., 2020). These boundaries remain analytically relevant even when one model performs several activities.</p>
<p>Uncertainty and variability have different meanings in this chain (Michiels and Geeraerd, 2020). Incomplete knowledge about an attribute, variation among buildings and alternative future scenarios cannot automatically be interpreted as equivalent probability distributions. We use <em>uncertainty continuity</em> to mean the traceable retention or explicit revision of uncertainty information, dependencies and validity conditions across transformations. Continuity does not require a distribution to remain unchanged: propagation, new observations or aggregation may legitimately alter it. The question is whether that alteration is documented and usable downstream. Missing reporting alone does not establish that uncertainty was lost in the implementation.</p>
<p>Digital-twin research supplies a complementary perspective on connected representations and updating. Systematic reviews characterize DT concepts and construction applications, while semantic construction twins emphasize information integration (Jones et al., 2020; Boje et al., 2020; Opoku et al., 2021; Tuhaise et al., 2023). These functions require separate assessment: a geometric model need not maintain a data connection, and an updated representation need not propagate uncertainty. Abdelrahman et al. (2025) distinguish real-time operational twins from longer-term decision-support applications. For material assessment, a survey, renovation or recovery inspection may be the relevant update trigger; a continuous sensor stream is not itself evidence of a valid connected assessment.</p>
<p>Uncertainty-aware DT research offers more specific mechanisms. Kapteyn et al. (2021) demonstrate probabilistic modelling, calibration and updating in an aircraft-related application, while Lin et al. (2021) review uncertainty quantification and software risks. Their mechanisms motivate examination of state representation, dependencies and revision procedures, but do not demonstrate continuity throughout the circular-material chain. Transfer requires matching entities, quantities, time horizons and validation conditions. Likewise, a scalable software architecture does not establish that material assumptions remain valid across buildings, districts and regions.</p>
<p>The review connects these literatures through their interfaces: material-flow research identifies what is transformed; uncertainty research identifies what information must be retained or revised; DT research identifies capabilities for linking evidence and calculations. Spatial support, temporal validity and stakeholder information requirements qualify these connections. Building on stock–LCA, uncertainty and DT reviews, the analysis distinguishes directly documented connections, cross-study synthesis and proposals addressing gaps. Its contribution is an evidence-traceable architectural synthesis, rather than a newly implemented or validated end-to-end twin.</p>
'''
s=s[:a]+section+s[b:]
ref='<p>Schiller, Georg; Miatto, Alessio; Gruhler, Karin; Ortlepp, Regine; Deilmann, Clemens; Tanikawa, Hiroki. 2019. Transferability of Material Composition Indicators for Residential Buildings: A Conceptual Approach Based on a German-Japanese Comparison. Journal of Industrial Ecology 23(4), 796–807. https://doi.org/10.1111/jiec.12817</p>\n'
idx=s.index('<p>Shao',s.index('class="refs"'));s=s[:idx]+ref+s[idx:];p.write_text(s,encoding='utf8')
ET.register_namespace('','http://www.w3.org/2000/svg')
changes={
 'focused_selection_status_en.svg':[(195,300,28),(395,500,28),(610,660,28)],
 'evidence_join_en.svg':[(180,275,32),(410,500,32),(585,670,32)],
 'prisma_broad_dtu_status_en.svg':[(280,330,28),(485,530,28),(900,945,28)]}
for name,gaps in changes.items():
 f=O/'figures'/name;root=ET.fromstring(f.read_text(encoding='utf8'))
 def y(v):
  v=float(v);return v-sum(max(0,min(v-end+end-start,end-start))*(1-new/(end-start)) for start,end,new in gaps)
 # Coordinate remapping removes only empty horizontal bands; text and box heights are retained.
 def yy(v):
  v=float(v);return v-sum(max(0,min(v-lo,hi-lo))*(1-new/(hi-lo)) for lo,hi,new in gaps)
 for e in root.iter():
  tag=e.tag.split('}')[-1]
  if tag=='rect':
   old=float(e.get('y',0));h=float(e.get('height',0));e.set('y',str(yy(old)));e.set('height',str(yy(old+h)-yy(old)))
  elif tag=='text':
   if 'y' in e.attrib:e.set('y',str(yy(e.get('y'))))
   if 'transform' in e.attrib:e.set('transform',re.sub(r'translate\(([^,]+),([^\)]+)\)',lambda m:'translate('+m[1]+','+str(yy(m[2]))+')',e.get('transform')))
  elif tag=='path' and 'marker-end' in e.attrib:
   e.set('d',re.sub(r'([ML])([\d.]+),([\d.]+)',lambda m:m[1]+m[2]+','+str(yy(m[3])),e.get('d')))
 h=yy(root.get('height'));root.set('height',str(h));root.set('viewBox','0 0 1000 '+str(h));f.write_text(ET.tostring(root,encoding='unicode'),encoding='utf8')
audit={'section_2_words_before':before,'section_2_words_after':len(re.sub('<[^>]+>',' ',section).split()),'figure_gaps':changes,'added_reference':'Schiller et al. (2019), 10.1111/jiec.12817','reference_verification':'Publisher abstract and citation metadata; https://onlinelibrary.wiley.com/doi/10.1111/jiec.12817','eligibility_counts_changed':False}
(O/'spacing_related_work_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf8');print(audit)
