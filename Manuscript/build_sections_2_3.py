"""Build bilingual manuscript sections, vector workflow/audit figures and LaTeX.
No eligibility decisions are created or changed by this script.
Run from repository root: python Manuscript/build_sections_2_3.py
or from this workspace: python outputs/Manuscript/build_sections_2_3.py
"""
from pathlib import Path
import re,json,html,csv,hashlib,textwrap
B=Path(__file__).resolve().parent
F=B/'figures/methods'; F.mkdir(parents=True,exist_ok=True)
D=B/'reading_versions';D.mkdir(exist_ok=True)
A=B/'methods_audit/eligibility'
extra=r'''
@article{M01,
 title={The PRISMA 2020 statement: an updated guideline for reporting systematic reviews},
 author={Page, Matthew J. and McKenzie, Joanne E. and Bossuyt, Patrick M. and others},
 year={2021}, journal={BMJ}, volume={372}, pages={n71}, doi={10.1136/bmj.n71}
}
@article{M02,
 title={PRISMA-S: an extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews},
 author={Rethlefsen, Melissa L. and Kirtley, Shona and Waffenschmidt, Siw and others},
 year={2021}, journal={Systematic Reviews}, volume={10}, pages={39}, doi={10.1186/s13643-020-01542-z}
}
@article{M03,
 title={Life cycle assessment in circular design process: A systematic literature review},
 author={Falsafi, Amirmehrab and Togiani, Amir and Colley, Ashley and Varis, Juha and Horttanainen, Mika},
 year={2025}, journal={Journal of Cleaner Production}, volume={521}, pages={146188}, doi={10.1016/j.jclepro.2025.146188}
}
'''
extra=re.sub(r', (?=(?:year|journal|volume|pages|doi)=)',',\n ',extra)
bib=(B/'references.bib').read_text(encoding='utf8')
if '@article{M01,' in bib: bib=bib.split('@article{M01,')[0]
bib+='\n'+extra;(B/'references.bib').write_text(bib,encoding='utf8')
refs={}
for key,block in re.findall(r'@article\{([^,]+),(.*?)(?=\n@|\Z)',bib,re.S):
 def val(k):
  m=re.search(r'\b'+k+r'\s*=\s*\{(.*?)\}\s*,?\s*(?:\n|$)',block,re.S)
  return m.group(1).strip('{}') if m else ''
 authors=val('author').split(' and '); names=[a.split(',')[0] for a in authors]
 label=names[0]+(' and '+names[1] if len(names)==2 else ' et al.' if len(names)>2 else '')+', '+val('year')
 refs[key]={'label':label,'text':val('author').replace(' and ','; ')+'. '+val('year')+'. '+val('title')+'. '+val('journal')+'. https://doi.org/'+val('doi'),'doi':val('doi')}
def cite(s,links=False):
 def sub(m):
  keys=m[1].split(',')
  return '('+'; '.join(('<a href="https://doi.org/'+refs[k]['doi']+'">'+html.escape(refs[k]['label'])+'</a>') if links else refs[k]['label'] for k in keys)+')'
 return re.sub(r'\[((?:I|U|M)\d+(?:,(?:I|U|M)\d+)*)\]',sub,s)
def svg(name,lang,title,boxes,edges,foot):
 rtl=lang=='fa';out=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="850" viewBox="0 0 1000 850">', '<defs><marker id="a" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#526579"/></marker></defs>','<rect width="1000" height="850" fill="white"/>']
 def text(x,y,line,size=19,color='#17384c'):
  out.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Tahoma,Arial,sans-serif" font-size="{size}" fill="{color}"'+(' direction="rtl" unicode-bidi="plaintext"' if rtl else '')+'>'+html.escape(line)+'</text>')
 text(500,36,title,25)
 for x1,y1,x2,y2 in edges:out.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#526579" stroke-width="2" fill="none" marker-end="url(#a)"/>')
 for x,y,w,h,lines,color in boxes:
  lines=[part for line in lines for part in textwrap.wrap(line,width=max(18,int((w-30)/10)),break_long_words=False,break_on_hyphens=False)]
  out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{color}" stroke="#567180" stroke-width="1.3"/>')
  yy=y+h/2-(len(lines)-1)*13+6
  for line in lines:text(x+w/2,yy,line);yy+=26
 for i,line in enumerate(foot):text(500,795+i*24,line,16)
 out.append('</svg>');p=F/(name+'_'+lang+'.svg');p.write_text('\n'.join(out),encoding='utf8')
blue='#eaf3f8';green='#e8f4ec';amber='#fff2db'
counts=json.loads((A/'broad_dtu_adjudicated_counts.json').read_text(encoding='utf8'))
ft=json.loads((A/'broad_dtu_fulltext_validation.json').read_text(encoding='utf8'))
focus=json.loads((A/'verified_fulltext_counts.json').read_text(encoding='utf8'))
pending=sum(counts['unique_publication_decisions'][x] for x in ['retain_fulltext','retain_secondary','unclear'])-ft['assessed_unique_publications']
assert 903-375==528 and 528-2==526 and 526-218==308 and 89+pending==308
assert 21+4+64==89 and 52-7==45 and 45-2==43
for lang in ['en','fa']:
 fa=lang=='fa'
 labels=([
 ['Research questions','S1-S5 interfaces and uncertainty continuity'],
 ['Scopus | Web of Science | IEEE','S / S+U / S+DT / S+DT+U'],
 ['Selection and full-text eligibility','Deduplicate; document decisions and retrieval'],
 ['Shared interface extraction','Input → transformation → output + U + context'],
 ['Join DT capability evidence','Match entities, variables, time, scale and assumptions'],
 ['Relational analysis → evidence-traceable architecture','Direct evidence | cross-study synthesis | proposal']
 ] if not fa else [
 ['پرسش‌های پژوهش','رابط‌های S1–S5 و پیوستگی عدم قطعیت'],
 ['Scopus | Web of Science | IEEE','S / S+U / S+DT / S+DT+U'],
 ['انتخاب و صلاحیت متن کامل','حذف تکراری؛ ثبت تصمیم و وضعیت دریافت'],
 ['استخراج مشترک رابط','ورودی ← تبدیل ← خروجی؛ عدم قطعیت و زمینه'],
 ['اتصال شواهد قابلیت DT','تطبیق موجودیت، متغیر، زمان، مقیاس و فرض‌ها'],
 ['تحلیل رابطه‌ای و سنتز معماری مستند','شاهد مستقیم؛ تلفیق مطالعات؛ پیشنهاد']])
 boxes=[(110,75+i*112,780,84,l,green if i==5 else blue) for i,l in enumerate(labels)]
 svg('workflow',lang,'1. Connected review workflow' if not fa else '۱. روند متصل مرور',boxes,[(500,159+i*112,500,187+i*112) for i in range(5)],['General DT / DT+U supplies complementary mechanisms; no automatic domain transfer.' if not fa else 'DT و DT+U عمومی، شواهد مکمل فراهم می‌کنند؛ انتقال به حوزه باید توجیه شود.'])
 labels=([
 ['S → workflow and variables'],['S+U → uncertainty operation'],['S+DT → domain architecture'],['S+DT+U → direct joint evidence'],
 ['Shared interface record E(p,i,j)','Entity | input | transformation | output','U-in / U-out | dependencies | context | evidence'],
 ['Interface × U'],['Interface × DT'],['DT × U'],
 ['Joined evidence: interface × U × DT','Same-paper support is counted separately from cross-study synthesis']
 ] if not fa else [
 ['S: جریان کار و متغیرها'],['S+U: عملیات عدم قطعیت'],['S+DT: معماری حوزه'],['S+DT+U: شاهد مشترک مستقیم'],
 ['رکورد مشترک رابط E(p,i,j)','موجودیت؛ ورودی؛ تبدیل؛ خروجی','عدم قطعیت؛ وابستگی؛ زمینه؛ محل شاهد'],
 ['رابط × عدم قطعیت'],['رابط × قابلیت DT'],['DT × عدم قطعیت'],
 ['شاهد متصل: رابط × عدم قطعیت × DT','پشتوانهٔ درون مقاله از تلفیق میان مقاله‌ها جداست']])
 boxes=[(30+i*245,90,225,90,labels[i],blue) for i in range(4)]
 boxes += [(150,275,700,135,labels[4],green)]
 boxes += [(55+i*320,500,250,85,labels[5+i],blue) for i in range(3)]
 boxes += [(90,670,820,80,labels[8],green)]
 edges=[(142+i*245,180,500,275) for i in range(4)]+[(500,410,180+i*320,500) for i in range(3)]+[(180+i*320,585,500,670) for i in range(3)]
 svg('evidence_join',lang,'2. One extraction model, three connected analyses' if not fa else '۲. یک مدل استخراج، سه تحلیل متصل',boxes,edges,['Conceptual analysis design; boxes and arrows are not empirical frequencies.' if not fa else 'این شکل طراحی تحلیل است؛ جعبه‌ها و پیکان‌ها فراوانی تجربی نیستند.'])
 labels=([
 ['Query occurrences: 903'],['Duplicates removed: 375'],['Records screened: 528'],['Late aliases removed: 2'],['Unique publications: 526'],['Title/abstract exclusions: 218'],['Retrieval candidates: 308'],[f'Not fully assessed: {pending}','Includes 2 defective retrieved files'],['Full texts assessed: 89'],['Excluded from strict intersection: 64'],['Domain included: 21','Complementary included: 4']
 ] if not fa else [
 ['رخدادهای جست‌وجو: ۹۰۳'],['تکراری پیش از غربالگری: ۳۷۵'],['رکورد غربال‌شده: ۵۲۸'],['تکراری شناسایی‌شدهٔ بعدی: ۲'],['انتشار یکتا: ۵۲۶'],['خروج عنوان و چکیده: ۲۱۸'],['نامزد دریافت و بررسی: ۳۰۸'],['ارزیابی کامل‌نشده: ۲۱۹','شامل دو فایل دریافت‌شدهٔ معیوب'],['متن کامل ارزیابی‌شده: ۸۹'],['خروج از تقاطع سخت‌گیرانه: ۶۴'],['ورود مجموعهٔ حوزه: ۲۱','ورود مجموعهٔ مکمل: ۴']])
 boxes=[]
 for row,left in enumerate([0,2,4,6,8,10]):boxes.append((55,70+row*112,420,82,labels[left],green if row==5 else blue))
 for row,right in enumerate([1,3,5,7,9]):boxes.append((565,70+row*112,390,82,labels[right],amber))
 edges=[(265,152+i*112,265,182+i*112) for i in range(5)]+[(475,111+i*112,565,111+i*112) for i in range(5)]
 svg('prisma_broad_dtu_status',lang,'3. Base+DT+U | PRISMA-style audit status' if not fa else '۳. وضعیت ممیزی Base+DT+U به سبک PRISMA',boxes,edges,['Audit snapshot, NOT final PRISMA. Pending is not an exclusion reason.' if not fa else 'تصویر وضعیت ممیزی، نه PRISMA نهایی؛ در انتظار بررسی به معنی خروج نیست.','The 25 assessed inclusions do not close eligibility for all 308 candidates.' if not fa else 'ورود ۲۵ مورد ارزیابی‌شده، صلاحیت همهٔ ۳۰۸ نامزد را نهایی نمی‌کند.'])
 labels=([
 ['Previously selected focused sets','53 memberships / 52 unique publications'],['Not retrieved: 7'],['Full texts assessed: 45'],['Full-text exclusions: 2'],['Included unique publications: 43','S+U: 20 | domain DT bridge: 10 | focused DT+U: 14'],['One publication overlaps two included groups','20 + 10 + 14 - 1 = 43']
 ] if not fa else [
 ['مجموعه‌های متمرکز قبلاً منتخب','۵۳ عضویت / ۵۲ انتشار یکتا'],['دریافت‌نشده: ۷'],['متن کامل ارزیابی‌شده: ۴۵'],['خروج پس از بررسی متن کامل: ۲'],['انتشار یکتای واردشده: ۴۳','S+U: ۲۰ | پل DT حوزه: ۱۰ | DT+U متمرکز: ۱۴'],['یک مقاله در دو گروه ورود مشترک است','۲۰ + ۱۰ + ۱۴ − ۱ = ۴۳']])
 boxes=[(65,100,530,95,labels[0],blue),(650,100,300,95,labels[1],amber),(65,300,530,95,labels[2],blue),(650,300,300,95,labels[3],amber),(65,500,870,110,labels[4],green),(100,660,800,75,labels[5],blue)]
 svg('focused_selection_status',lang,'4. Focused-set full-text adjudication' if not fa else '۴. تصمیم متن کامل در مجموعه‌های متمرکز',boxes,[(330,195,330,300),(595,147,650,147),(330,395,330,500),(595,347,650,347)],['Subset adjudication only: not the database identification flow; overlaps broad searches.' if not fa else 'فقط تصمیم زیرمجموعه؛ این شکل جریان شناسایی پایگاه‌ها نیست و با جست‌وجوی گسترده هم‌پوشانی دارد.'])

def md_html(text):
 out=[];table=False
 for line in text.splitlines():
  if line.startswith('|'):
   cells=[c.strip() for c in line.strip('|').split('|')]
   if all(re.fullmatch(r'[-:]+',c) for c in cells):continue
   if not table:out.append('<table>');table=True
   out.append('<tr>'+''.join('<td>'+cite(html.escape(c),True)+'</td>' for c in cells)+'</tr>');continue
  if table:out.append('</table>');table=False
  if line.startswith('## '):out.append('<h2>'+html.escape(line[3:])+'</h2>')
  elif line.startswith('# '):out.append('<h1>'+html.escape(line[2:])+'</h1>')
  elif line.strip():out.append('<p>'+cite(html.escape(line),True)+'</p>')
 if table:out.append('</table>')
 return '\n'.join(out)
def tex(text):
 def esc(s):
  for a,b in [('&',r'\&'),('%',r'\%'),('_',r'\_'),('→',r'$\rightarrow$'),('×',r'$\times$'),('–','--')]:s=s.replace(a,b)
  return re.sub(r'\[((?:I|U|M)\d+(?:,(?:I|U|M)\d+)*)\]',r'\\citep{\1}',s)
 out=[];table=False
 for l in text.splitlines():
  if l.startswith('|'):
   cells=[c.strip() for c in l.strip('|').split('|')]
   if all(re.fullmatch(r'[-:]+',c) for c in cells):continue
   if not table:out.append(r'\begin{center}\small\begin{tabularx}{\linewidth}{'+'X'*len(cells)+r'}\toprule');table=True
   out.append(' & '.join(esc(c) for c in cells)+r'\\\addlinespace');continue
  if table:out.append(r'\bottomrule\end{tabularx}\end{center}');table=False
  if re.match(r'^## \d+\.\d+\.\d+\. ',l):out.append(r'\subsubsection{'+re.sub(r'^\d+\.\d+\.\d+\. ','',l[3:])+'}')
  elif l.startswith('## '):out.append(r'\subsection{'+re.sub(r'^\d+\.\d+\. ','',l[3:])+'}')
  elif l.startswith('# '):out.append(r'\section{'+re.sub(r'^\d+\. ','',l[2:])+'}')
  else:out.append(esc(l))
 return '\n'.join(out)
used=set()
css='''@page{size:A4;margin:18mm 19mm}body{font-family:Tahoma,Arial,sans-serif;font-size:10.5pt;line-height:1.75;color:#172c3b;max-width:900px;margin:auto}h1{font-size:20pt;color:#174761}h2{font-size:13pt;break-after:avoid;margin-top:22pt}p{orphans:3;widows:3;margin:0 0 10pt}table{break-inside:avoid;width:100%;border-collapse:collapse;font-size:9pt;margin:14pt 0}tr{break-inside:avoid}td{border:1px solid #bdcbd3;padding:7px;vertical-align:top}tr:first-child{background:#eaf3f8;font-weight:bold}a{color:#185675;text-decoration:none}.figure{break-before:page;break-inside:avoid}.figure img{width:100%}.note{padding:12px;background:#fff2db;font-size:9pt}pre{white-space:pre-wrap;direction:ltr;text-align:left;font-size:8pt;overflow-wrap:anywhere}.refs p{font-size:8.5pt;line-height:1.5}.page{break-before:page}'''
for lang in ['en','fa']:
 s2=(B/f'sections/02_related_work_{lang}.txt').read_text(encoding='utf8')
 s3=(B/f'sections/03_methods_{lang}.txt').read_text(encoding='utf8')
 keys=set(k for m in re.findall(r'\[((?:I|U|M)\d+(?:,(?:I|U|M)\d+)*)\]',s2+s3) for k in m.split(','));used|=keys
 if lang=='en':
  (B/'sections/02_related_work.tex').write_text(tex(s2),encoding='utf8')
  tx=tex(s3)
  for fig,caption in [('workflow','Connected review workflow.'),('evidence_join','Shared interface records connect the three relational analyses.'),('prisma_broad_dtu_status','Broad Base+DT+U audit status; not a final PRISMA flow.'),('focused_selection_status','Focused-set adjudication only; not a database-wide selection flow.')]:
   tx+=r'\begin{figure}[p]\centering\includegraphics[width=\linewidth]{figures/methods/'+fig+'_en.pdf}\\caption{'+caption+r'}\end{figure}'+'\n'
  (B/'sections/03_methods.tex').write_text(tx,encoding='utf8')
 # Human-readable citations for standalone text; source keys remain in authoring files.
 (D/f'sections_2_3_{lang}.txt').write_text(cite(s2+'\n\n'+s3)+'\n\nREFERENCES\n\n'+'\n\n'.join(refs[k]['text'] for k in sorted(keys,key=lambda k:refs[k]['label'])),encoding='utf8')
 notice=('Working manuscript: connected methods specified; selection is not closed for all search families. Figures 3–4 show verified audit status and must not be cited as final all-scenario PRISMA.' if lang=='en' else 'نسخهٔ کاری: روش متصل تدوین شده است، اما انتخاب همهٔ خانواده‌ها بسته نشده است. شکل‌های ۳ و ۴ وضعیت ممیزی تأییدشده را نشان می‌دهند و PRISMA نهایی همهٔ سناریوها نیستند.')
 body='<div class="note">'+notice+'</div>'+md_html(s2)+'<div class="page"></div>'+md_html(s3)
 for fig in ['workflow','evidence_join','prisma_broad_dtu_status','focused_selection_status']:
  body+='<div class="figure"><img src="../figures/methods/'+fig+'_'+lang+'.svg"/></div>'
 # One actual archived query, not a fabricated historical run.
 supp=(B/'supplementary_material/S1_search_strategies.txt').read_text(encoding='utf8')
 query=re.search(r'S4-2 \[archived Scopus syntax\]\s*\n(.*)',supp).group(1)
 body+='<div class="page"><h2>'+('Archived query example: S4 Base+U (Scopus)' if lang=='en' else 'نمونهٔ کوئری آرشیوشده: S4 Base+U در Scopus')+'</h2><pre>'+html.escape(query)+'</pre><p>'+('Full archived queries: Supplement S1; this example does not redefine historical searches.' if lang=='en' else 'عبارت‌های آرشیوشدهٔ کامل در مکمل S1 هستند؛ این نمونه جست‌وجوهای تاریخی را بازتعریف نمی‌کند.')+'</p></div>'
 body+='<div class="refs page" dir="ltr"><h1>References</h1>'+''.join('<p>'+html.escape(refs[k]['text'])+'</p>' for k in sorted(keys,key=lambda k:refs[k]['label']))+'</div>'
 (D/f'sections_2_3_{lang}.html').write_text('<!doctype html><html lang="'+lang+'" dir="'+('rtl' if lang=='fa' else 'ltr')+'"><meta charset="utf-8"><title>Sections 2–3 | '+lang+'</title><style>'+css+'</style><body>'+body+'</body></html>',encoding='utf8')
(B/'References_sections_2_3.txt').write_text('\n\n'.join(refs[k]['text'] for k in sorted(used,key=lambda k:refs[k]['label'])),encoding='utf8')
# Wire the new sections without deleting the archived methods or later drafts.
main=(B/'main.tex').read_text(encoding='utf8')
main=main.replace(r'\usepackage{amsmath,booktabs,tabularx}',r'\usepackage{amsmath,booktabs,tabularx,graphicx}')
main=main.replace(r'\input{sections/02_methods}',r'\input{sections/02_related_work}'+'\n'+r'\input{sections/03_methods}')
(B/'main.tex').write_text(main,encoding='utf8')
intro=B/'sections/01_introduction.tex';s=intro.read_text(encoding='utf8')
old='Section 2 presents the search, screening, extraction and synthesis methods. Section 3 compares integrated workflows and analyses their interfaces and supporting evidence. Section 4 develops the architecture with explicit evidence traceability. Sections 5 and 6 discuss implications, limitations and validation priorities and present the conclusions.'
new='Section 2 reviews the conceptual foundations and related work. Section 3 specifies the connected search, selection, interface extraction and synthesis methods. Section 4 presents the evidence analysis, Section 5 develops the evidence-traceable architecture, and Section 6 discusses implications, limitations and validation priorities.'
intro.write_text(s.replace(old,new),encoding='utf8')
rows=[['Base+DT','screened_unique',2400],['Base+DT','excluded_title_abstract',724],['Base+DT','direct_candidates',890],['Base+DT','secondary_candidates',762],['Base+DT','unclear_candidates',24],['Base+DT+U','identified_occurrences',903],['Base+DT+U','duplicates_before_screening',375],['Base+DT+U','records_screened',528],['Base+DT+U','late_aliases',2],['Base+DT+U','unique',526],['Base+DT+U','excluded_title_abstract',218],['Base+DT+U','fulltext_candidates',308],['Base+DT+U','assessed',89],['Base+DT+U','pending',pending],['Base+DT+U','domain_included',21],['Base+DT+U','complementary_included',4],['Base+DT+U','excluded_strict_intersection',64],['Focused_only','unique_selected',52],['Focused_only','not_retrieved',7],['Focused_only','assessed',45],['Focused_only','excluded',2],['Focused_only','included_unique',43]]
with (F/'figure_counts.csv').open('w',encoding='utf8',newline='') as f:
 w=csv.writer(f);w.writerow(['scope','metric','count']);w.writerows(rows)
validation={'references_resolved':len(used),'related_work_has_no_subheadings':all('## ' not in (B/f'sections/02_related_work_{l}.txt').read_text(encoding='utf8') for l in ['en','fa']),'count_balance':'passed','new_fulltext_decisions':0,'final_all_scenario_PRISMA':False,'count_sources':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [A/'broad_dtu_adjudicated_counts.json',A/'broad_dtu_fulltext_validation.json',A/'verified_fulltext_counts.json']}}
(F/'validation.json').write_text(json.dumps(validation,indent=2),encoding='utf8')
print(json.dumps(validation,indent=2))
