from pathlib import Path
import re,html,json,csv,shutil,textwrap
B=Path(__file__).resolve().parent;M=B.parent
(B/'reading').mkdir(exist_ok=True);(B/'tex').mkdir(exist_ok=True)
bib=(M/'references.bib').read_text(encoding='utf8')+'\n'+(B/'inputs/references.bib').read_text(encoding='utf8')
(B/'references.bib').write_text(bib,encoding='utf8');refs={}
for key,block in re.findall(r'@article\{([^,]+),(.*?)(?=\n@|\Z)',bib,re.S):
 def val(k):
  m=re.search(r'\b'+k+r'\s*=\s*\{(.*?)\}\s*,?\s*(?:\n|$)',block,re.S);return m.group(1).strip('{}').replace('\\&','&') if m else ''
 names=[a.split(',')[0] for a in val('author').split(' and ')]
 refs[key]={'label':names[0]+(' and '+names[1] if len(names)==2 else ' et al.' if len(names)>2 else '')+', '+val('year'),'text':val('author').replace(' and ','; ')+'. '+val('year')+'. '+val('title')+'. '+val('journal')+'. https://doi.org/'+val('doi'),'doi':val('doi')}
def cite(t):
 return re.sub(r'(?<!\[)\[((?:I|U|M|R)\d+(?:,(?:I|U|M|R)\d+)*)\]',lambda m:'('+'; '.join(refs[k]['label'] for k in m[1].split(','))+')',t)
def read(p):return Path(p).read_text(encoding='utf8')
# Proposed architecture overlay, not an empirically measured network.
out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1020"><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0 0 L0 6 L8 3Z" fill="#326678"/></marker></defs><rect width="1200" height="1020" fill="white"/>']
def txt(x,y,t,size=19):out.append(f'<text x="{x}" y="{y}" font-family="Arial" font-size="{size}" fill="#17384b" text-anchor="middle">{html.escape(t)}</text>')
def box(x,y,w,h,title,lines,fill='#eaf3f5'):
 out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" stroke="#678a99"/>');txt(x+w/2,y+28,title,21)
 for j,line in enumerate(lines):txt(x+w/2,y+57+j*24,line,17)
def arrow(x,y,xx,yy):out.append(f'<path d="M{x} {y} L{xx} {yy}" stroke="#326678" stroke-width="2" marker-end="url(#a)"/>')
txt(600,38,'Uncertainty tracking across material-flow interfaces',29);txt(600,68,'Proposed synthesis: reported capabilities mapped to explicit interface requirements',18)
box(45,95,1110,90,'A. Intended use and evidence requirement',['Quantity of interest | spatial support | time horizon | tolerance | decision authority'])
stages=[('S1','Attributes'),('S2','Inventory'),('S3','Dated outflows'),('S4','Recovery'),('S5','Impacts')]
for i,(s,l) in enumerate(stages):
 box(45+i*230,225,190,90,s,[l]);
 if i<4:arrow(235+i*230,270,275+i*230,270)
box(45,365,1110,110,'B. Shared interface contract — proposed cross-study connection',['Entity + variable + unit | U representation + dependencies | transformation + assumptions','Spatial support + valid time | version + evidence | downstream use'],'#f4edf6')
for i in range(5):arrow(140+i*230,315,140+i*230,365)
mods=[('Observe','Quality / timing','Missing or stale data'),('Infer','State / parameter U','Supported uncertainty'),('Propagate','Samples / dependencies','Input-to-output mapping'),('Diagnose','Residuals / coverage','Mismatch, not unique cause'),('Decide','Risk / scenario context','Conditions and authority')]
for i,(a,b,c) in enumerate(mods):
 box(25+i*235,540,215,120,a,[b,c]);arrow(132+i*235,475,132+i*235,540)
box(45,720,1110,100,'C. Traceable update and explanation',['Retain previous state → record new evidence → revise the relevant model → reassess the decision','Capability concepts: R2, R3, R5, R6, R15; allocation to all S1–S5 boundaries is our synthesis.'],'#eaf4ec')
for i in range(5):arrow(132+i*235,660,132+i*235,720)
txt(600,885,'Diagnostic limits',22);txt(600,919,'A residual can flag disagreement; it does not identify every uncertainty source.',18);txt(600,949,'No universal threshold, automatic reduction or end-to-end deployment is claimed.',18)
out.append('</svg>');(B/'figures/F07_tracking_architecture.svg').write_text('\n'.join(out),encoding='utf8')
figs={
'M1':('../figures/methods/workflow_{lang}.svg','Connected review workflow. Conceptual methodological design.','روند متصل مرور؛ طراحی مفهومی روش.'),
'M2':('../figures/methods/evidence_join_{lang}.svg','Shared interface record and evidence joins.','رکورد مشترک رابط و اتصال شواهد.'),
'M3':('../figures/methods/prisma_broad_dtu_status_{lang}.svg','Broad Base+DT+U selection audit. Pending eligibility is not relabelled as exclusion.','ممیزی انتخاب گسترده؛ صلاحیت ناتمام به خروج تبدیل نشده است.'),
'M4':('../figures/methods/focused_selection_status_{lang}.svg','Focused-set adjudication; overlapping subsets, not an additional independent database flow.','تصمیم مجموعه‌های متمرکز؛ زیرمجموعه‌های هم‌پوشان و نه جست‌وجوی مستقل اضافی.'),
'F01':('figures/F01_sources.svg','Recalculated source frequencies, archived 17-paper coding. Multi-label, paper denominator.','فراوانی بازشماری‌شدهٔ منابع در کدگذاری ۱۷ مقاله؛ چندبرچسبی با مخرج مقاله.'),
'F02':('figures/F02_methods.svg','Recalculated method frequencies in the same 17 papers; broad legacy codes retain their original scope.','فراوانی بازشماری‌شدهٔ روش‌ها در همان ۱۷ مقاله؛ طبقات گستردهٔ قدیمی حفظ شده‌اند.'),
'F03':('figures/F03_outcomes.svg','Legacy outcome labels reconstructed with supporting IDs. These are not measured variance changes.','بازسازی برچسب‌های پیامد قدیمی با شناسهٔ پشتیبان؛ این‌ها تغییر واریانس اندازه‌گیری‌شده نیستند.'),
'F06':('figures/F06_outcome_vocabulary.svg','Conceptual outcome vocabulary. Synthetic normalized curves; not data from the reviewed models.','واژگان مفهومی پیامد؛ منحنی‌های مصنوعی نرمال‌شده و نه دادهٔ مدل‌های مرورشده.'),
'D01':('../relational_analysis/data_diagrams/figures/D01_boundary_continuity_alluvial.svg','Current boundary–continuity coding: 23 contexts from 20 publications.','کدگذاری فعلی مرز–پیوستگی: ۲۳ زمینه از ۲۰ مقاله.'),
'F04':('figures/F04_boundary_percentages.svg','Within-boundary percentages and counts. B34 denominator is zero, so its percentage is undefined.','درصد و تعداد درون هر مرز؛ مخرج B34 صفر و درصد آن تعریف‌نشده است.'),
'D02':('../relational_analysis/data_diagrams/figures/D02_stage_function_network.svg','Stage–function co-coding; edge width is distinct supporting publications, not uncertainty flow.','کدگذاری مرحله–کارکرد؛ پهنای یال تعداد مقالات است، نه جریان عدم قطعیت.'),
'F05':('figures/F05_dt_mechanisms.svg','Positive mechanism frequency in ten non-review general-DT records.','فراوانی سازوکار مثبت در ده رکورد غیرمروری DT عمومی.'),
'D03':('../relational_analysis/data_diagrams/figures/D03_exact_uncertainty_configurations.svg','Exact positive-code intersections. Each publication occupies one configuration.','تقاطع دقیق کدهای مثبت؛ هر مقاله در یک ترکیب قرار دارد.'),
'D04':('../relational_analysis/data_diagrams/figures/D04_uncertainty_source_method_associations.svg','Source–method co-occurrence restricted to the same paper and context.','هم‌وقوعی منبع–روش، محدود به همان مقاله و زمینه.'),
'A01':('inputs/figure_1_design_to_use.svg','Previously developed design-to-use synthesis. R keys are resolved in the accompanying foundations register; arrows are conceptual.','سنتز پیشین از طراحی تا استفاده؛ کلیدهای R در فهرست مبانی مشخص شده‌اند و پیکان‌ها مفهومی‌اند.'),
'A02':('inputs/figure_S2_configuration_choices (1).svg','Configuration vocabulary, not empirical pair frequencies. Unresolved terms remain marked in the original figure.','واژگان پیکربندی، نه فراوانی تجربی اتصال‌ها؛ اصطلاحات فاقد پشتوانه در شکل اصلی علامت دارند.'),
'A03':('inputs/figure_S3_functional_allocation.svg','Functional allocation. Activities are not equivalent to material-flow stages.','تخصیص کارکرد؛ فعالیت‌ها معادل مراحل جریان مصالح نیستند.'),
'F07':('figures/F07_tracking_architecture.svg','Proposed uncertainty-tracking overlay. Capability concepts have literature support; complete interface allocation is synthesis.','لایهٔ پیشنهادی ردیابی عدم قطعیت؛ مفاهیم قابلیت پشتوانه دارند و تخصیص کامل به رابط‌ها سنتز است.')}
title='From GeoAI to environmental impact assessment: A systematic review of uncertainty continuity and digital twin architecture for the circular built environment'
css='''@page wide{size:A4 landscape;margin:14mm 17mm}.wide{page:wide}.wide img{max-height:155mm!important} @page{size:A4;margin:17mm 19mm}body{font-family:Tahoma,Arial,sans-serif;font-size:10.5pt;line-height:1.7;color:#193142}h1{font-size:20pt;color:#164b60;break-before:page}h2{font-size:13pt;break-after:avoid;margin-top:18pt}p{orphans:3;widows:3;margin:0 0 11pt}table{width:100%;border-collapse:collapse;font-size:8.6pt;line-height:1.5;margin:15pt 0}tr{break-inside:avoid}td{border:1px solid #c3d1d8;padding:6px;vertical-align:top}tr:first-child{background:#eaf2f5;font-weight:bold}.figure{break-before:page;break-after:page;break-inside:avoid}.figure img{display:block;width:100%;max-height:230mm;object-fit:contain}.caption{font-size:9pt;line-height:1.5;margin-top:9pt}.note{padding:12pt;background:#fff4df;font-size:10pt}.refs p{font-size:8.5pt;line-height:1.45;overflow-wrap:anywhere}.cover h1{break-before:auto;font-size:23pt}.cover{break-after:page;padding-top:35mm}.query{font-family:monospace;direction:ltr;font-size:8pt;white-space:pre-wrap;overflow-wrap:anywhere}a{color:#245d75}'''
intro=read(M/'sections/01_introduction.tex');intro=re.sub(r'\\section\{Introduction\}','# 1. Introduction',intro)
intro=re.sub(r'\\citep\{([^}]+)\}',r'[\1]',intro);intro=intro.replace('\\&','&').replace('\\%','%');intro=re.sub(r'\\(?:textbf|emph)\{([^}]+)\}',r'\1',intro)
intro=re.sub(r'Section 4 presents the evidence analysis, Section 5 develops.*?priorities\.', 'Section 4 presents the evidence analysis and architectural synthesis. Section 5 discusses interpretation, limitations and validation priorities.',intro)
ifa=read(M/'Introduction_FA.txt');ifa=ifa[ifa.find('۱. مقدمه'):];ifa='# '+ifa
ifa=re.split(r'\n(?:منابع|References)',ifa)[0]
ifa=re.sub(r'بخش دوم،.*?اعتبارسنجی بعدی نیاز دارد\.', 'بخش دوم پیشینه و مبانی مفهومی، بخش سوم روش متصل مرور، بخش چهارم نتایج و سنتز معماری و بخش پنجم بحث و محدودیت‌ها را ارائه می‌کند. اثربخشی عملیاتی معماری به اعتبارسنجی بعدی نیاز دارد.', ifa, flags=re.S)
ifa=re.sub(r'بخش ۲.*?نتیجه‌گیری[^\n]*', 'بخش ۲ مبانی و کارهای مرتبط، بخش ۳ روش متصل مرور، بخش ۴ نتایج و سنتز معماری و بخش ۵ بحث، محدودیت‌ها و اولویت اعتبارسنجی را ارائه می‌کند.',ifa)
extra_en='''\n## 3.6.7. Recalculation of archived frequencies and conceptual outcome diagrams\n\nThe 17-paper legacy subset is retained separately from the 20-paper/23-context set. Source and method tokens are counted once per publication and divided by 17. Outcome labels are reconstructed from explicit legacy wording using documented aliases; multiple outcomes can occur in a publication. Supporting IDs and percentages are exported. This tests numerical reproduction, not a new semantic judgement. Eligibility is cross-linked by DOI. Probabilistic densities in the outcome vocabulary are synthetic illustrations, not extracted distributions. Mechanism percentages use ten non-review DT records and positive R codes. No pooling of uncertainty magnitudes, variance contributions or reductions is performed because compatible quantitative quantities and conditions have not been extracted.\n'''
extra_fa='''\n## ۳.۶.۷. بازشماری فراوانی‌های آرشیوی و طرح مفهومی پیامدها\n\nمجموعهٔ قدیمی ۱۷ مقاله‌ای از مجموعهٔ ۲۰ مقاله و ۲۳ زمینه جدا نگه داشته شد. هر کد منبع و روش در هر مقاله یک بار شمرده و بر ۱۷ تقسیم شد. پیامدها با نگاشت صریح عبارت‌های قدیمی بازسازی شدند و می‌توانند در یک مقاله هم‌زمان باشند. شناسه‌های پشتیبان و درصدها خروجی گرفته شدند. این کنترل بازتولید عددی است، نه قضاوت معنایی جدید. صلاحیت از طریق DOI تطبیق داده شد. منحنی‌های پیامد، مثال مصنوعی‌اند و توزیع استخراج‌شده نیستند. درصد سازوکارهای DT از ده رکورد غیرمروری و کد مثبت R محاسبه شد. به دلیل نبود استخراج هماهنگ کمیت و شرایط، اندازهٔ عدم قطعیت، سهم واریانس یا کاهش آن تجمیع نشد.\n'''
all_used=set();manif=[]
for lang in ['en','fa']:
 s2=read(M/f'sections/02_related_work_{lang}.txt');s3=read(M/f'sections/03_methods_{lang}.txt')
 # Insert immediately before reporting-status section.
 pos=s3.find('## 3.7.') if lang=='en' else s3.find('## ۳.۷.')
 if pos<0:pos=s3.find('## 3.7.')
 if pos<0:pos=len(s3)
 s3=s3[:pos]+(extra_en if lang=='en' else extra_fa)+s3[pos:]
 s3+='\n\n'+ '\n\n'.join('[[M'+str(i)+']]' for i in range(1,5))
 texts=[intro if lang=='en' else ifa,s2,s3,read(B/f'results_{lang}.txt'),read(B/f'discussion_{lang}.txt')]
 raw='\n\n'.join(texts);used=set(k for mat in re.findall(r'(?<!\[)\[((?:I|U|M|R)\d+(?:,(?:I|U|M|R)\d+)*)\]',raw) for k in mat.split(','))
 # Persian introduction uses resolved author-year citations; include its source keys too.
 used|=set(k for mat in re.findall(r'\[((?:I|U)\d+(?:,(?:I|U)\d+)*)\]',intro) for k in mat.split(','));all_used|=used
 assert used<=refs.keys(),used-refs.keys()
 num=0;body=[];table=False;tex=[]
 for line in raw.splitlines():
  marker=re.fullmatch(r'\[\[([A-Z]\d+)\]\]',line.strip())
  if marker:
   k=marker[1];num+=1;path,en,fa=figs[k];path=path.format(lang=lang);caption=en if lang=='en' else fa
   assert (B/path).exists(),path
   layout='figure wide' if k in ['F01','F02','F03','F04','F05','D02','D03','A02','F07'] else 'figure'
   body.append(f'<div class="{layout}"><img src="../{html.escape(path)}"/><p class="caption">'+('Figure ' if lang=='en' else 'شکل ')+str(num)+'. '+html.escape(caption)+'</p></div>')
   if lang=='en':
    pdf=path.replace('.svg','.pdf');tex.append('\\begin{figure}[p]\\centering\\includegraphics[width=\\linewidth,height=.82\\textheight,keepaspectratio]{../'+pdf+'}\\caption{'+caption.replace('&','\\&')+'}\\end{figure}')
   manif.append({'language':lang,'figure':num,'key':k,'file':path,'caption':caption});continue
  if line.startswith('|'):
   cells=[x.strip() for x in line.strip('|').split('|')]
   if all(re.fullmatch('[-:]+',c) for c in cells):continue
   if not table:body.append('<table>');tex.append('\\begin{longtable}{'+'p{'+str(round(15.5/len(cells),2))+'cm}'*len(cells)+'}');table=True
   body.append('<tr>'+''.join('<td>'+html.escape(cite(c))+'</td>' for c in cells)+'</tr>');tex.append(' & '.join(c.replace('%','\\%').replace('&','\\&') for c in cells)+'\\\\');continue
  if table:body.append('</table>');tex.append('\\end{longtable}');table=False
  if line.startswith('# '):body.append('<h1>'+html.escape(line[2:])+'</h1>');tex.append('\\section{'+re.sub(r'^\d+\.\s*','',line[2:])+'}')
  elif line.startswith('## '):body.append('<h2>'+html.escape(line[3:])+'</h2>');tex.append('\\'+('subsubsection' if re.match(r'^## \d+\.\d+\.\d+\.',line) else 'subsection')+'{'+re.sub(r'^[\d.]+\s*','',line[3:])+'}')
  elif line.strip():
   body.append('<p>'+html.escape(cite(line))+'</p>')
   tx=line.replace('&','\\&').replace('%','\\%').replace('_','\\_');tx=re.sub(r'(?<!\[)\[((?:I|U|M|R)\d+(?:,(?:I|U|M|R)\d+)*)\]',r'\\citep{\1}',tx);tex.append(tx+'\n')
 if table:body.append('</table>');tex.append('\\end{longtable}')
 # Keep one bibliography line per DOI even when inherited keys alias the same work.
 selected=[];seen=set()
 for k in sorted(used,key=lambda k:refs[k]['label']):
  doi=refs[k]['doi'].lower()
  if doi not in seen:selected.append(k);seen.add(doi)
 legend='<h1>'+('Appendix: architectural source keys' if lang=='en' else 'پیوست: کلید منابع شکل‌های معماری')+'</h1><p>'+('The R register is a conceptual seed bibliography, not a separately completed systematic corpus. Source-specific access limits are retained in inputs/academic-foundations.md.' if lang=='en' else 'فهرست R مجموعهٔ مبانی مفهومی است و مجموعهٔ نظام‌مند مستقل و بسته‌شده نیست. حدود دسترسی هر منبع در فایل مبانی حفظ شده است.')+'</p><table dir="ltr">'+''.join('<tr><td>R'+str(i)+'</td><td>'+html.escape(refs['R'+str(i)]['text'])+'</td></tr>' for i in range(1,17) if 'R'+str(i) in refs)+'</table>'
 refs_html=legend+'<div class="refs" dir="ltr"><h1>References</h1>'+''.join('<p>'+html.escape(refs[k]['text'])+'</p>' for k in selected)+'</div>'
 notice=('Complete-text working draft, without abstract. Numerical coding was reproduced; all-search eligibility and complete semantic recoding are not closed. Empirical frequencies and conceptual architecture diagrams are explicitly distinguished.' if lang=='en' else 'پیش‌نویس کامل متنی، بدون ابسترکت. کدگذاری عددی بازتولید شده؛ صلاحیت همهٔ جست‌وجوها و بازکدگذاری معنایی کامل هنوز بسته نشده است. فراوانی تجربی و نمودار معماری مفهومی تفکیک شده‌اند.')
 cover='<div class="cover"><h1 dir="ltr">'+title+'</h1><p>'+('Introduction · Related work · Methods · Results · Discussion' if lang=='en' else 'مقدمه · کارهای مرتبط · روش · نتایج · بحث')+'</p><div class="note">'+notice+'</div></div>'
 doc='<!doctype html><html lang="'+lang+'" dir="'+('rtl' if lang=='fa' else 'ltr')+'"><meta charset="utf-8"><title>Full manuscript</title><style>'+css+'</style><body>'+cover+'\n'.join(body)+refs_html+'</body></html>'
 (B/f'reading/manuscript_no_abstract_{lang}.html').write_text(doc,encoding='utf8');(B/f'reading/manuscript_no_abstract_{lang}.txt').write_text(cite(raw)+'\n\nREFERENCES\n'+'\n\n'.join(refs[k]['text'] for k in selected),encoding='utf8')
 if lang=='en':
  (B/'tex/body.tex').write_text('\n'.join(tex),encoding='utf8')
  (B/'tex/main.tex').write_text('\\documentclass[11pt,a4paper]{article}\n\\usepackage{fontspec}\n\\setmainfont{TeX Gyre Termes}\n\\usepackage[margin=2.2cm]{geometry}\n\\usepackage{amsmath,graphicx,longtable,booktabs}\n\\usepackage[round,authoryear]{natbib}\n\\usepackage[hidelinks]{hyperref}\n\\title{'+title+'}\n\\author{}\\date{}\n\\begin{document}\\maketitle\n\\input{body}\n\\bibliographystyle{../../elsarticle-harv}\n\\bibliography{../references}\n\\end{document}',encoding='utf8')
with (B/'figure_manifest.csv').open('w',encoding='utf8',newline='') as f:
 w=csv.DictWriter(f,list(manif[0]));w.writeheader();w.writerows(manif)
(B/'References_full_manuscript.txt').write_text('\n\n'.join(refs[k]['text'] for k in sorted(all_used,key=lambda k:refs[k]['label'])),encoding='utf8')
(B/'document_validation.json').write_text(json.dumps({'figures_per_language':num,'sections':5,'abstract_included':False,'citation_keys_resolved':len(all_used),'full_review_closed':False,'latex_compilation_verified':False},indent=2),encoding='utf8')
print('Built English/Persian manuscripts;',num,'figures each;',len(all_used),'resolved citation keys.')
