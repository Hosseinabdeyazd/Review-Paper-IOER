const fs=require('fs'),path=require('path');
const {pathToFileURL}=require('url');
const {chromium}=require('C:/Users/technokade/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const out=path.join(__dirname,'compact');fs.mkdirSync(out,{recursive:true});
const keep=[1,3,4,5,9,11,13,14,18];
const css=`@page{size:A4;margin:19mm 19mm 20mm}body{font-family:'Times New Roman',Tahoma,serif;font-size:11pt;line-height:1.38;color:#111}body[dir=rtl]{font-family:Tahoma,Arial,sans-serif;font-size:10.5pt;line-height:1.65}h1{font-size:15pt;break-after:avoid;margin:18pt 0 10pt}h2{font-size:12pt;break-after:avoid;margin:12pt 0 6pt}p{margin:0 0 7pt;orphans:3;widows:3}table{border-collapse:collapse;width:100%;font-size:9pt;line-height:1.3;margin:10pt 0}td{border:0;border-bottom:.5pt solid #bbb;padding:4pt;vertical-align:top}tr{break-inside:avoid}tr:first-child{font-weight:bold;border-top:1pt solid #111;border-bottom:1pt solid #111}.figure{break-inside:avoid;margin:12pt 0}.figure img{display:block;width:100%;max-height:185mm;object-fit:contain}.caption{font-size:9pt;line-height:1.25;margin-top:5pt}.cover{margin-bottom:15pt}.cover h1{font-size:16pt}.note{font-size:9pt}.refs{break-before:page}.refs p{font-size:10pt;line-height:1.3;overflow-wrap:anywhere}.supplement-title{break-before:page}`;
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});const page=await browser.newPage();const audit={};
 for(const lang of ['en','fa']){
  await page.goto(pathToFileURL(path.join(__dirname,`reading/manuscript_no_abstract_${lang}.html`)).href);
  const data=await page.evaluate(({keep,css,lang})=>{
   document.querySelector('style').textContent=css;document.body.setAttribute('dir',lang==='fa'?'rtl':'ltr');
   const supplement=[];const map={};let mainN=0,supN=0;
   // Detailed reproducibility checks remain available in the supplement.
   const normalize=s=>s.replace(/[۰-۹]/g,c=>'۰۱۲۳۴۵۶۷۸۹'.indexOf(c));
   for(const h of [...document.querySelectorAll('h2')]){
    if(/^3\.6\.[1267]\./.test(normalize(h.textContent))){
     let el=h;while(el){const next=el.nextElementSibling;supplement.push(el.outerHTML);el.remove();if(!next||/^H[12]$/.test(next.tagName))break;el=next;}
    }
   }
   const qt=document.querySelector('table');if(qt){supplement.push(qt.outerHTML);const note=document.createElement('p');note.textContent=lang==='en'?'The search-block table, counting equations and reproducibility checks are provided in the supplement. Continuity distributions count assessed paper–boundary contexts, with one status per context. Stage–function edges count distinct publications carrying the exact paired code; memberships overlap and are not summed as unique papers.':'جدول بلوک‌های جست‌وجو، معادلات شمارش و کنترل بازتولیدپذیری در مکمل ارائه شده‌اند. توزیع پیوستگی بر مبنای زمینه‌های ارزیابی‌شدهٔ مقاله–مرز محاسبه می‌شود و هر زمینه فقط یک وضعیت دارد. یال مرحله–کارکرد تعداد مقالات متمایز دارای همان کد مشترک را نشان می‌دهد؛ عضویت‌ها هم‌پوشان‌اند و جمع آن‌ها تعداد مقالهٔ یکتا نیست.';qt.replaceWith(note);}
   document.querySelectorAll('.figure').forEach((f,i)=>{const n=i+1;f.className='figure';const img=f.querySelector('img');img.src='../'+img.getAttribute('src').replace(/^\.\.\//,'');
    // Both source and compact directories sit one level below full_draft.
    if(keep.includes(n)){map[n]='Figure '+(++mainN);f.querySelector('.caption').textContent=f.querySelector('.caption').textContent.replace(/^(Figure |شکل )\d+\./,(lang==='en'?'Figure ':'شکل ')+mainN+'.');}
    else{map[n]='Supplementary Figure S'+(++supN);f.querySelector('.caption').textContent=f.querySelector('.caption').textContent.replace(/^(Figure |شکل )\d+\./,(lang==='en'?'Supplementary Figure S':'شکل مکمل S')+supN+'.');supplement.push(f.outerHTML);const p=document.createElement('p');p.textContent=lang==='en'?`See Supplementary Figure S${supN}.`:`شکل مکمل S${supN} را ببینید.`;f.replaceWith(p);}
   });
   const app=[...document.querySelectorAll('h1')].find(h=>/Appendix:|پیوست:/.test(h.textContent));
   if(app){let el=app;while(el&&!el.classList.contains('refs')){const next=el.nextElementSibling;supplement.push(el.outerHTML);el.remove();el=next;}}
   // Resolve explicit numbered cross-references after the figure split.
   document.querySelectorAll('p:not(.caption),td').forEach(p=>{if(!p.closest('.refs'))p.innerHTML=p.innerHTML.replace(/Figure (\d+)/g,(s,n)=>map[n]||s);});
   document.querySelectorAll('h2').forEach(h=>{h.textContent=h.textContent.replace(/^3\.6\.([345])\./,(_,n)=>'3.6.'+(Number(n)-2)+'.').replace(/^۳\.۶\.([۳۴۵])\./,(_,n)=>'۳.۶.'+['۱','۲','۳']['۳۴۵'.indexOf(n)]+'.');});
   document.querySelectorAll('p').forEach(p=>{p.textContent=p.textContent.replace('Table 1 lists the concepts','Supplementary Table S1 lists the concepts');});
   const clone=document.body.cloneNode(true);clone.querySelectorAll('.refs,.cover').forEach(e=>e.remove());
   const count=clone.textContent.trim().split(/\s+/).length;
   const refs=document.querySelectorAll('.refs p').length;
   return {html:document.documentElement.outerHTML,supplement,words:count,refs,mainFigures:mainN,supplementFigures:supN};
  },{keep,css,lang});
  fs.writeFileSync(path.join(out,`manuscript_${lang}.html`),data.html);
  fs.writeFileSync(path.join(out,`supplement_figures_${lang}.html`),`<!doctype html><html lang="${lang}" dir="${lang==='fa'?'rtl':'ltr'}"><meta charset="utf-8"><style>${css}</style><body dir="${lang==='fa'?'rtl':'ltr'}"><h1>${lang==='en'?'Supporting figures and architectural source register':'شکل‌های پشتیبان و فهرست منابع معماری'}</h1>${data.supplement.join('\n')}</body></html>`);
  for(const name of [`manuscript_${lang}`,`supplement_figures_${lang}`]){
   await page.goto(pathToFileURL(path.join(out,name+'.html')).href);await page.evaluate(()=>document.fonts.ready);
   const bad=await page.locator('img').evaluateAll(xs=>xs.filter(x=>!x.complete||!x.naturalWidth).map(x=>x.src));if(bad.length)throw Error(JSON.stringify(bad));
   await page.pdf({path:path.join(out,name+'.pdf'),format:'A4',printBackground:true,preferCSSPageSize:true,displayHeaderFooter:true,headerTemplate:'<span></span>',footerTemplate:'<div style="font-size:8px;text-align:center;width:100%"><span class="pageNumber"></span></div>'});
  }
  audit[lang]={words_excluding_references_and_title:data.words,references:data.refs,main_figures:data.mainFigures,supplement_figures:data.supplementFigures};
 }
 fs.writeFileSync(path.join(out,'layout_audit.json'),JSON.stringify(audit,null,2));await browser.close();console.log(audit);
})();
