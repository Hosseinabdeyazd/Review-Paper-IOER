const fs=require('fs'),path=require('path');
const {pathToFileURL}=require('url');
const {chromium}=require('C:/Users/technokade/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const page=await browser.newPage();fs.mkdirSync(path.join(__dirname,'pdf'),{recursive:true});
 for(const lang of ['en','fa']){
  await page.goto(pathToFileURL(path.join(__dirname,`reading/manuscript_no_abstract_${lang}.html`)).href);
  await page.evaluate(()=>document.fonts.ready);
  const bad=await page.locator('img').evaluateAll(xs=>xs.filter(x=>!x.complete||!x.naturalWidth).map(x=>x.src));if(bad.length)throw Error(JSON.stringify(bad));
  await page.pdf({path:path.join(__dirname,`pdf/manuscript_no_abstract_${lang}.pdf`),format:'A4',printBackground:true,displayHeaderFooter:true,headerTemplate:'<span></span>',footerTemplate:'<div style="font-size:8px;text-align:center;width:100%;color:#74838c">Working manuscript · <span class="pageNumber"></span></div>',preferCSSPageSize:true});
 }
 // Vector copies for the LaTeX source. Original uploaded SVGs are preserved.
 for(const rel of ['inputs/figure_1_design_to_use.svg','inputs/figure_S2_configuration_choices (1).svg','inputs/figure_S3_functional_allocation.svg','figures/F07_tracking_architecture.svg']){
  const p=path.join(__dirname,rel);const s=fs.readFileSync(p,'utf8');const v=s.match(/viewBox="([^"]+)"/)[1].split(/\s+/).map(Number);
  await page.setContent('<html><head><style>@page{margin:0}body{margin:0}svg{width:100%;height:100%}</style></head><body>'+s+'</body></html>');
  await page.pdf({path:p.replace('.svg','.pdf'),width:v[2]+'px',height:v[3]+'px',printBackground:true});
 }
 await browser.close();console.log('Rendered bilingual full manuscript and architecture vector PDFs.');
})();
