from pathlib import Path
import json,re,shutil
from pypdf import PdfReader
import pypdfium2 as pdf
from PIL import Image,ImageDraw
O=Path('outputs/Manuscript/full_draft/compact/english_review')
src=Path('outputs/Manuscript/full_draft/compact/export_source.py').read_text(encoding='utf8')
ns={'__file__':str((O/'export_source.py').resolve())}
exec(src.split('p=Parser();')[0],ns)
p=ns['Parser']();p.feed((O/'manuscript_en.html').read_text(encoding='utf8'))
(O/'body.tex').write_text(ns['tex'](p.root),encoding='utf8')
shutil.copyfile(O.parent/'main.tex',O/'main.tex')
a=json.loads((O/'layout_audit.json').read_text())
r=PdfReader(O/'manuscript_en.pdf');first=next(i for i,p in enumerate(r.pages) if re.match(r'References\b',p.extract_text() or ''))
a['manuscript_en'].update(main_pages=first,reference_pages=len(r.pages)-first,total_pages=len(r.pages))
assert first<=28 and a['manuscript_en']['words']<=9000
assert a['manuscript_en']['paragraphAlignment']=='justify'
assert all(p.mediabox.width>0 for p in r.pages)
a['scientific_status']='Working review copy; broad eligibility incomplete. Updated DT+U selection 91 assessed, 217 pending; not a final closed PRISMA.'
a['latex_compilation_verified']=False
(O/'layout_audit.json').write_text(json.dumps(a,indent=2),encoding='utf8')
q=O/'qa';q.mkdir(exist_ok=True)
for file in ['manuscript_en','supplement_figures_en']:
 d=pdf.PdfDocument(O/(file+'.pdf'));canvas=Image.new('RGB',(1200,((len(d)+3)//4)*440),'#dddddd');draw=ImageDraw.Draw(canvas)
 for i in range(len(d)):
  im=d[i].render(scale=1.2).to_pil();im.save(q/f'{file}_{i+1}.png');im.thumbnail((290,410));canvas.paste(im,((i%4)*300,(i//4)*440+20));draw.text(((i%4)*300+5,(i//4)*440+4),str(i+1),fill='black')
 canvas.save(q/(file+'_contact.png'))
print(json.dumps(a,indent=2))
