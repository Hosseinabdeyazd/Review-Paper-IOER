const fs=require('fs'),path=require('path');const {pathToFileURL}=require('url');
const {chromium}=require('C:/Users/technokade/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const out=path.resolve('outputs/Manuscript/full_draft/compact/technical_review');
(async()=>{const b=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});const page=await b.newPage();let audit={};
for(const name of ['manuscript_en','supplement_figures_en']){
 await page.goto(pathToFileURL(path.join(out,name+'.html')).href);await page.evaluate(()=>document.fonts.ready);
 const report=await page.evaluate(()=>{
  const changes=[];for(const p of document.querySelectorAll('p,td')){if(p.closest('.refs'))continue;let t=p.textContent;if(/\b(89|219)\b/.test(t)){changes.push(t);p.textContent=t.replace(/\b89\b/g,'91').replace(/\b219\b/g,'217').replace(/\b64\b/g,'66');}}
  const c=document.body.cloneNode(true);c.querySelectorAll('.cover,.refs').forEach(e=>e.remove());return {words:c.textContent.trim().split(/\s+/).length,references:document.querySelectorAll('.refs p').length,figures:document.querySelectorAll('.figure').length,changes,brokenImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),paragraphAlignment:getComputedStyle(document.querySelector('p')).textAlign};
 });if(report.brokenImages.length)throw Error(JSON.stringify(report));
 fs.writeFileSync(path.join(out,name+'.html'),await page.content());
 await page.pdf({path:path.join(out,name+'.pdf'),printBackground:true,preferCSSPageSize:true,displayHeaderFooter:true,headerTemplate:'<span></span>',footerTemplate:'<div style="font-size:8px;text-align:center;width:100%"><span class="pageNumber"></span></div>'});audit[name]=report;
}
fs.writeFileSync(path.join(out,'layout_audit.json'),JSON.stringify(audit,null,2));
for(const file of fs.readdirSync(path.join(out,'figures')).filter(x=>x.endsWith('.svg'))){
 await page.goto(pathToFileURL(path.join(out,'figures',file)).href);await page.evaluate(()=>document.fonts.ready);
 const box=await page.locator('svg').evaluate(e=>({w:e.getBoundingClientRect().width,h:e.getBoundingClientRect().height}));
 await page.pdf({path:path.join(out,'figures',file.replace('.svg','.pdf')),width:box.w+'px',height:box.h+'px',printBackground:true,margin:{top:0,bottom:0,left:0,right:0}});
}
await b.close();console.log(audit);})();

