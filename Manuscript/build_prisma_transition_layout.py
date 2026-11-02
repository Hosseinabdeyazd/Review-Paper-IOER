"""PRISMA-style geometry with explicit unresolved branches; never infer missing decisions."""
from pathlib import Path
import json,csv,html,re,textwrap
B=Path(__file__).resolve().parent;F=B/'figures/methods';A=B/'methods_audit/eligibility'
c=json.loads((A/'broad_dtu_adjudicated_counts.json').read_text(encoding='utf8'))
t=json.loads((A/'broad_dtu_fulltext_validation.json').read_text(encoding='utf8'))
assert c['records_screened']==528 and t['assessed_unique_publications']==89
for lang in ['en','fa']:
 fa=lang=='fa';out=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1250" viewBox="0 0 1000 1250"><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z"/></marker></defs><rect width="1000" height="1250" fill="white"/>']
 def txt(x,y,s,size=18):
  out.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Tahoma,Arial" font-size="{size}" fill="#102d40"'+(' direction="rtl" unicode-bidi="plaintext"' if fa else '')+'>'+html.escape(s)+'</text>')
 def box(x,y,w,h,lines,fill='white',size=18):
  out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="{fill}" stroke="#263d4d" stroke-width="1.7"/>')
  lines=[z for s in lines for z in textwrap.wrap(s,int((w-25)/(size*.52)),break_long_words=False)]
  for i,s in enumerate(lines):txt(x+w/2,y+h/2+(i-(len(lines)-1)/2)*24+6,s,size)
 def arrow(x,y,xx,yy):out.append(f'<path d="M{x},{y} L{xx},{yy}" fill="none" stroke="#263d4d" stroke-width="1.8" marker-end="url(#a)"/>')
 box(120,25,840,55,['Identification via database searches | Base+DT+U' if not fa else 'شناسایی از جست‌وجوی پایگاه‌ها | Base+DT+U'],'#ffd126',20)
 for y,h,label in [(105,175,'Identification' if not fa else 'شناسایی'),(330,155,'Screening' if not fa else 'غربالگری'),(530,370,'Retrieval / eligibility' if not fa else 'دریافت و صلاحیت'),(945,120,'Included' if not fa else 'ورود')]:
  box(22,y,65,h,[], '#a9cde2')
  out.append(f'<text transform="translate(62,{y+h/2}) rotate(-90)" text-anchor="middle" font-family="Tahoma,Arial" font-size="17">{html.escape(label)}</text>')
 en=[['Records identified','Database-query occurrences: 903','Not deduplicated publications'],['Records removed before screening','Duplicate occurrences: 375','Duplicate occurrences across query exports'],['Records screened: 528'],['Records removed at screening: 220','Outside domain: 218','Additional duplicate aliases: 2'],['Reports selected for retrieval','and assessment: 308'],['Unresolved retrieval / assessment: 219','Includes 2 defective retrieved files','Not classified as full-text exclusions'],['Reports assessed for eligibility: 89'],['Reports excluded from strict','domain-DT-U intersection: 64','Individual reasons remain in decision ledger'],['Assessed reports included','Domain synthesis: 21','Complementary synthesis: 4']]
 per=[['رکوردهای شناسایی‌شده','رخداد جست‌وجو در پایگاه‌ها: ۹۰۳','پیش از یکپارچه‌سازی انتشارها'],['حذف پیش از غربالگری','رخداد تکراری: ۳۷۵','تکرار میان خروجی‌های جست‌وجو'],['رکوردهای غربال‌شده: ۵۲۸'],['حذف در مرحلهٔ غربالگری: ۲۲۰','خارج از حوزه: ۲۱۸','شناسهٔ تکراری اضافی: ۲'],['گزارش منتخب برای دریافت','و بررسی: ۳۰۸'],['دریافت یا ارزیابی ناتمام: ۲۱۹','شامل دو فایل دریافت‌شدهٔ معیوب','این موارد خروج متن کامل نیستند'],['گزارش ارزیابی‌شده برای صلاحیت: ۸۹'],['خروج از تقاطع سخت‌گیرانهٔ','حوزه، DT و U: تعداد ۶۴','دلایل فردی در دفتر تصمیم حفظ شده‌اند'],['گزارش ارزیابی‌شدهٔ واردشده','سنتز حوزه: ۲۱','سنتز مکمل: ۴']]
 l=per if fa else en
 for x,y,w,h,k in [(120,105,390,175,0),(570,105,390,175,1),(120,330,390,115,2),(570,330,390,155,3),(120,530,390,125,4),(570,530,390,155,5),(120,750,390,125,6),(570,750,390,150,7),(120,945,390,120,8)]:box(x,y,w,h,l[k], '#fff8e7' if k==5 else 'white')
 for ya,yb in [(280,330),(445,530),(655,750),(875,945)]:arrow(315,ya,315,yb)
 for y in [190,387,592,812]:arrow(510,y,570,y)
 txt(530,1115,'AUDIT SNAPSHOT — not a final PRISMA 2020 flow' if not fa else 'وضعیت ممیزی؛ نه نمودار نهایی PRISMA 2020',20)
 txt(530,1150,'Reports sought/not retrieved and independent-study counts are not yet closed.' if not fa else 'شمار درخواست دریافت، دریافت‌نشده و مطالعات مستقل هنوز بسته نشده است.',17)
 txt(530,1180,'Source: archived screening and eligibility decision ledgers.' if not fa else 'منبع: دفتر ثبت تصمیم‌های غربالگری و ارزیابی صلاحیت.',16)
 out.append('</svg>');(F/f'prisma_broad_dtu_status_{lang}.svg').write_text('\n'.join(out),encoding='utf8')

# A separate allocation table makes all transitions visible without inventing database-level PRISMA counts.
with (B/'relational_analysis/results/inputs/su_context_assessments.csv').open(encoding='utf-8-sig') as f:rows=[r for r in csv.DictReader(f) if r['included_in_counts']=='1']
summary=[]
for k,label in [('B12','S1 -> S2'),('B23','S2 -> S3'),('B34','S3 -> S4'),('B45','S4 -> S5'),('O5','Other inputs -> S5')]:
 rr=[r for r in rows if r['context']==k]
 summary.append({'boundary':k,'transition':label,'contexts':len(rr),'unique_publications':len({r['paper_id'] for r in rr}),'paper_ids':';'.join(sorted({r['paper_id'] for r in rr}))})
with (F/'transition_analysis_denominators.csv').open('w',encoding='utf8',newline='') as f:
 w=csv.DictWriter(f,list(summary[0]));w.writeheader();w.writerows(summary)
for lang in ['en','fa']:
 p=B/f'reading_versions/sections_2_3_{lang}.html';s=p.read_text(encoding='utf8')
 title='Transition allocation for D01/D04 (not a PRISMA count)' if lang=='en' else 'تخصیص انتقال‌ها در D01 و D04؛ مستقل از شمارش PRISMA'
 desc='23 contexts from 20 publications. Publication memberships overlap across boundaries. B34=0 is a selected-corpus coverage limit. O5 is not S4→S5.' if lang=='en' else '۲۳ زمینه از ۲۰ مقاله؛ عضویت مقاله‌ها میان مرزها هم‌پوشانی دارد. صفر B34 محدودیت پوشش مجموعهٔ منتخب است. O5 به معنای S4→S5 نیست.'
 tab='<h2>'+title+'</h2><p>'+desc+'</p><table><tr><td>Boundary</td><td>Contexts</td><td>Unique publications</td><td>Supporting IDs</td></tr>'+''.join('<tr>'+''.join('<td>'+html.escape(str(r[k]))+'</td>' for k in ['transition','contexts','unique_publications','paper_ids'])+'</tr>' for r in summary)+'</table>'
 s=s.replace('<div class="refs page"',tab+'<div class="refs page"');p.write_text(s,encoding='utf8')
print(json.dumps(summary,indent=2))
