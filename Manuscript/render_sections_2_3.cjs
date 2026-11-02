// Local document rendering only; no access to authenticated browser profiles.
const fs = require('fs');
const path = require('path');
const {pathToFileURL} = require('url');
const {chromium} = require('C:/Users/technokade/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
 const base=__dirname;
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const page=await browser.newPage({viewport:{width:1100,height:1000},deviceScaleFactor:1});
 fs.mkdirSync(path.join(base,'pdf'),{recursive:true});
 fs.mkdirSync(path.join(base,'figures/methods/qa'),{recursive:true});
 for(const lang of ['en','fa']){
  await page.goto(pathToFileURL(path.join(base,`reading_versions/sections_2_3_${lang}.html`)).href);
  await page.evaluate(()=>document.fonts.ready);
  await page.pdf({path:path.join(base,`pdf/sections_2_3_${lang}.pdf`),format:'A4',printBackground:true,preferCSSPageSize:true});
  await page.screenshot({path:path.join(base,`figures/methods/qa/text_${lang}.png`)});
  for(const fig of ['workflow','evidence_join','prisma_broad_dtu_status','focused_selection_status']){
   const svg=fs.readFileSync(path.join(base,`figures/methods/${fig}_${lang}.svg`),'utf8');
   await page.setContent('<html><head><style>@page{size:1000px 850px;margin:0}html,body{margin:0;width:1000px;height:850px}</style></head><body>'+svg+'</body></html>');
   await page.evaluate(()=>document.fonts.ready);
   await page.pdf({path:path.join(base,`figures/methods/${fig}_${lang}.pdf`),printBackground:true,preferCSSPageSize:true});
   await page.locator('svg').screenshot({path:path.join(base,`figures/methods/${fig}_${lang}.png`)});
  }
 }
 await browser.close();
 console.log('Rendered two bilingual reading PDFs and eight vector figure PDFs/PNGs.');
})().catch(e=>{console.error(e);process.exit(1)});
