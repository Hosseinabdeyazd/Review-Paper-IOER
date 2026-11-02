from pathlib import Path
import re,shutil
O=Path('outputs/Manuscript/full_draft/compact/technical_review')
mapping={'#355C7D':'#4C78A8','#326D73':'#72B7B2','#99632E':'#9D755D','#76516B':'#7F7F7F','#F0F4F8':'#ECECEC','#F0F6F5':'#ECECEC','#FAF5EE':'#ECECEC','#F6F0F5':'#ECECEC'}
for name in ['figure_1_design_to_use.svg','figure_S1_design_brief.svg']:
 p=O/'figures'/name;s=p.read_text(encoding='utf8')
 if name=='figure_S1_design_brief.svg':
  # Preserve documented categorical accents; neutral background fills use the common light grey.
  for a,b in mapping.items():s=s.replace(a,b)
  def shape(m):
   t=m[0]
   t=re.sub(r'fill="#[0-9A-Fa-f]{6}"',lambda a:a[0] if a[0].upper()=='FILL="#FFFFFF"' else 'fill="#ECECEC"',t)
   t=re.sub(r'stroke="#[0-9A-Fa-f]{6}"',lambda a:a[0] if a[0][8:-1].upper() in ['#4C78A8','#72B7B2','#9D755D','#7F7F7F'] else 'stroke="#7F7F7F"',t)
   return t
  s=re.sub(r'<rect\b[^>]*>',shape,s)
 s=re.sub(r'<(?:text|tspan)\b[^>]*>',lambda m:re.sub(r'fill="[^"]*"','fill="#000000"',m[0]),s)
 s=s.replace('</svg>','<style>text,tspan{fill:#000000 !important;font-family:"Times New Roman",serif !important}</style></svg>')
 p.write_text(s,encoding='utf8')
p=O/'manuscript_en.html';s=p.read_text(encoding='utf8')
start=s.index('<p>Source and method labels are joined');end=s.index('<p>Because labels',start)
new='''<p>Source and method labels are joined by publication and assessed context. Let A(q) denote contexts recording uncertainty source q and A(m) those recording method m. The number recording both is:</p><p class="equation" data-latex="n(q,m)=|A(q)\\cap A(m)|">n(q,m)=|A(q) intersection A(m)|</p><p>The denominator counts all contexts recording source q:</p><p class="equation" data-latex="N(q)=|A(q)|">N(q)=|A(q)|</p><p>In Figure 8, bubble colour represents the percentage of those contexts that also record method m:</p><p class="equation" data-latex="P(m\\mid q)=100\\,n(q,m)/N(q)">P(m|q)=100 n(q,m)/N(q)</p><p>Bubble area represents the count n(q,m), scaled by 150 points squared per assessment. Colour therefore shows a within-source percentage, not uncertainty magnitude. Empty source rows have undefined percentages. Rows and columns follow assessment frequency, with codebook order resolving ties.</p>
'''
s=s[:start]+new+s[end:];p.write_text(s,encoding='utf8');shutil.copyfile(__file__,O/'code/fix_figure_text_palette.py')


