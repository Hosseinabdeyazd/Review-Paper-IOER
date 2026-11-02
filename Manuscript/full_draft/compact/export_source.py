from pathlib import Path
from html.parser import HTMLParser
import re,json
from pypdf import PdfReader
B=Path(__file__).resolve().parent
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.root={'tag':'root','attrs':{},'children':[]};self.stack=[self.root]
 def handle_starttag(self,t,a):
  n={'tag':t,'attrs':dict(a),'children':[]};self.stack[-1]['children'].append(n)
  if t not in ['meta','img','br','link','hr','input']:self.stack.append(n)
 def handle_endtag(self,t):
  for i in range(len(self.stack)-1,0,-1):
   if self.stack[i]['tag']==t:self.stack=self.stack[:i];break
 def handle_data(self,d):self.stack[-1]['children'].append(d)
def txt(n):return n if isinstance(n,str) else ''.join(map(txt,n['children']))
def esc(t):
 return ''.join({'&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}','\\':r'\textbackslash{}'}.get(c,c) for c in t)
def tex(n):
 if isinstance(n,str):return ''
 tag=n['tag'];cl=n['attrs'].get('class','')
 if tag in ['head','style','title','meta'] or cl=='cover':return ''
 if tag=='h1':return '\n\\section'+('*' if txt(n)=='References' else '')+'{'+esc(re.sub(r'^\d+\.\s*','',txt(n)))+'}\n'
 if tag=='h2':return '\n\\'+('subsubsection' if re.match(r'\d+\.\d+\.\d+',txt(n)) else 'subsection')+'{'+esc(re.sub(r'^[\d.]+\s*','',txt(n)))+'}\n'
 if tag=='p':return esc(txt(n))+'\n\n'
 if cl=='figure':
  im=next(x for x in n['children'] if isinstance(x,dict) and x['tag']=='img')
  cap=next(x for x in n['children'] if isinstance(x,dict) and x['tag']=='p')
  source=im['attrs']['src'].replace('.svg','.pdf')
  assert (B/source).exists(),source
  return '\n\\begin{figure}[htbp]\\centering\n\\includegraphics[width=\\linewidth,height=.78\\textheight,keepaspectratio]{\\detokenize{'+source+'}}\n\\caption{'+esc(re.sub(r'^Figure \d+\.\s*','',txt(cap)))+'}\n\\end{figure}\n'
 if tag=='table':
  rows=[x for x in n['children'] if isinstance(x,dict) and x['tag']=='tr']
  if not rows:
   rows=[z for x in n['children'] if isinstance(x,dict) for z in x['children'] if isinstance(z,dict) and z['tag']=='tr']
  count=len([x for x in rows[0]['children'] if isinstance(x,dict)])
  result='\\begin{longtable}{'+'p{'+str(round(.91/count,3))+r'\linewidth}'*1
  result='\\begin{longtable}{'+('p{'+str(round(.90/count,3))+'\\linewidth}')*count+'}\n\\toprule\n'
  for i,row in enumerate(rows):result+=' & '.join(esc(txt(c)) for c in row['children'] if isinstance(c,dict))+'\\\\\n'+('\\midrule\n' if i==0 else '')
  return result+'\\bottomrule\n\\end{longtable}\n'
 return ''.join(tex(c) for c in n['children'])
p=Parser();p.feed((B/'manuscript_en.html').read_text(encoding='utf8'))
(B/'body.tex').write_text(tex(p.root),encoding='utf8')
title='From GeoAI to environmental impact assessment: A systematic review of uncertainty continuity and digital twin architecture for the circular built environment'
(B/'main.tex').write_text(r'''\documentclass[preprint,11pt,authoryear]{elsarticle}
\usepackage{fontspec}
\setmainfont{TeX Gyre Termes}
\usepackage{amsmath,graphicx,longtable,booktabs}
\usepackage[hidelinks]{hyperref}
\journal{Journal of Cleaner Production}
\begin{document}
\begin{frontmatter}
\title{'''+title+r'''}
\end{frontmatter}
\input{body.tex}
\end{document}
''',encoding='utf8')
a=json.loads((B/'layout_audit.json').read_text())
for lang in ['en','fa']:
 r=PdfReader(B/f'manuscript_{lang}.pdf');first=next(i for i,p in enumerate(r.pages) if re.search(r'^References',(p.extract_text() or ''),re.M))
 a[lang].update(main_pages=first,reference_pages=len(r.pages)-first,total_pages=len(r.pages))
 assert first<=28 and a[lang]['words_excluding_references_and_title']<=9000
a['latex_compilation_verified']=False
a['pdf_renderer']='Chromium; editable English source uses elsarticle and requires XeLaTeX. PDF page audit applies to supplied PDFs, not an uncompiled TeX build.'
a['scope']='Layout and main/supplement split. No new eligibility decisions or added references.'
(B/'layout_audit.json').write_text(json.dumps(a,indent=2),encoding='utf8')
print(json.dumps(a,indent=2))
