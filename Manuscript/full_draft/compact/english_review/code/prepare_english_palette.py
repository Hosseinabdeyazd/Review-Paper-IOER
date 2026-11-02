from pathlib import Path
import re,json,sys,csv,xml.etree.ElementTree as ET,hashlib,base64,io
from PIL import Image
sys.path.insert(0,str(Path('work/plot_dependencies').resolve()))
import numpy as np
from matplotlib import colormaps
from matplotlib.colors import to_rgb,to_hex,LinearSegmentedColormap
B=Path('outputs/Manuscript/full_draft/compact');O=B/'english_review';O.mkdir(exist_ok=True);A=O/'figures';A.mkdir(exist_ok=True)
pal=['#4c78a8','#72b7b2','#9d755d','#7f7f7f','#b8b8b8','#d9d9d9','#ececec','#2f2f2f','#ffffff']
special={'#90a0ad':'#7f7f7f','#c86c65':'#b8b8b8','#d8aa4a':'#9d755d','#7d9cc4':'#4c78a8','#53a79d':'#72b7b2','#28745e':'#72b7b2', '#9baab4':'#7f7f7f','#c7776c':'#b8b8b8','#d7b34e':'#9d755d','#7099bd':'#4c78a8','#56a59d':'#72b7b2','#276f5b':'#72b7b2', '#357fa3':'#4c78a8','#278d88':'#72b7b2','#9477b5':'#9d755d','#d2943e':'#7f7f7f','#b96765':'#b8b8b8','#17364a':'#2f2f2f','#17384b':'#2f2f2f','#16394c':'#2f2f2f','#526676':'#7f7f7f','#287f7a':'#72b7b2','#337fa8':'#4c78a8','#ffffff':'#ffffff','#000000':'#2f2f2f'}
old=colormaps['YlGnBu'];new=LinearSegmentedColormap.from_list('repository',['#ececec','#72b7b2','#4c78a8'])
grad={to_hex(old(i/255)):to_hex(new(i/255)) for i in range(256)}
audit=[]
def color(m,name):
 c=m.group().lower()
 if name.startswith('D04') and c in grad:return grad[c]
 if c=='#307f92':return '#72b7b2' if name.startswith('F01') else '#4c78a8'
 if c in special:return special[c]
 v=np.array(to_rgb(c));return min(pal,key=lambda p:np.linalg.norm(v-np.array(to_rgb(p))))
def recolor(p):
 name=p.name;raw=p.read_text(encoding='utf8');s=re.sub(r'#[0-9a-fA-F]{6}',lambda m:color(m,name),raw)
 if name.startswith('D04'):
  def recolor_bar(m):
   im=Image.open(io.BytesIO(base64.b64decode(m[1]))).convert('RGBA');a=np.array(im);rgb=a[:,:,:3].reshape(-1,3).astype(float)
   lut=np.array([old(i/255)[:3] for i in range(256)])*255
   idx=((rgb[:,None,:]-lut[None,:,:])**2).sum(axis=2).argmin(axis=1)
   a[:,:,:3]=np.array([new(int(i)/255)[:3] for i in idx]).reshape(a.shape[0],a.shape[1],3)*255
   buf=io.BytesIO();Image.fromarray(a).save(buf,format='PNG');return 'data:image/png;base64,'+base64.b64encode(buf.getvalue()).decode()
  s=re.sub(r'data:image/png;base64,\s*([A-Za-z0-9+/=]+)',recolor_bar,s)
 if name.startswith('F03'):
  data=list(csv.DictReader(Path('outputs/Manuscript/full_draft/data/F03_outcomes.csv').open(encoding='utf8')))
  colors={'Preserved':'#72b7b2','Transformed':'#4c78a8','Amplified':'#9d755d','Masked / lost':'#7f7f7f','Legitimately reduced':'#b8b8b8','Unassessed':'#ececec'}
  for i,r in enumerate(sorted(data,key=lambda r:int(r['n'])),3):
   pattern=r'(<g id="patch_'+str(i)+r'">)(.*?)(</g>)'
   s=re.sub(pattern,lambda m:m[1]+re.sub(r'fill: #[0-9a-f]{6}','fill: '+colors[r['label']],m[2])+m[3],s,flags=re.S)
 if name.startswith('F06'):
  root=ET.fromstring(s);colors=['#72b7b2','#4c78a8','#9d755d','#b8b8b8','#7f7f7f','#ececec']
  for g in root.iter():
   match=re.fullmatch(r'axes_(\d+)',g.get('id',''))
   if match:
    row=(int(match[1])-1)//2
    for e in g.iter():
     if 'style' in e.attrib:e.set('style',e.get('style').replace('#4c78a8',colors[row]))
  s=ET.tostring(root,encoding='unicode')
 if 'prisma_broad_dtu' in name:
  for a,b in [('89','91'),('219','217'),('64','66')]:
   s=re.sub(r'>([^<>]+)<',lambda m:'>'+re.sub(r'\b'+a+r'\b',b,m[1])+'<',s)
 # Preserve geometry and wording; palette operations do not recalculate scientific data.
 (A/name).write_text(s,encoding='utf8');audit.append({'source':str(p),'output':name,'source_sha256':hashlib.sha256(raw.encode()).hexdigest(),'output_sha256':hashlib.sha256(s.encode()).hexdigest()})
for langfile in ['manuscript_en','supplement_figures_en']:
 h=(B/(langfile+'.html')).read_text(encoding='utf8')
 def image(m):
  p=(B/m[1]).resolve()
  if p.name=='F07_tracking_architecture.svg':p=Path('outputs/Manuscript/completion_review/dt_uncertainty_architecture.svg').resolve()
  recolor(p);return 'src="figures/'+p.name+'"'
 h=re.sub(r'src="([^"]+\.svg)"',image,h)
 h=h.replace('</style>','p{text-align:justify;text-justify:inter-word;hyphens:auto;text-align-last:left}h1,h2,.caption,.note,td{text-align:left}.refs p{hyphens:none;text-align:left}a{color:#4C78A8}</style>')
 if langfile=='manuscript_en':
  h=h.replace('Proposed uncertainty-tracking overlay. Capability concepts have literature support; complete interface allocation is synthesis.','Digital-twin assessment architecture: supported mechanisms and proposed cross-stage integration. Module frequencies refer to ten general-DT publications; modules can serve multiple stages. Dashed integration elements are our synthesis, not demonstrated end-to-end deployment.')
 (O/(langfile+'.html')).write_text(h,encoding='utf8')
(O/'palette_audit.json').write_text(json.dumps({'palette_source':'figure/code/PALETTE.md','palette':pal,'continuous_association_scale':'very-light gray to uncertainty teal to manuscript blue','figures':audit},indent=2),encoding='utf8')
print('Prepared',len(audit),'figure instances')
