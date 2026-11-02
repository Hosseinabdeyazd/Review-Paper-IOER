const fs=require('fs'),path=require('path');
const {pathToFileURL}=require('url');
const {chromium}=require('C:/Users/technokade/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const page=await browser.newPage();
 const base=path.resolve('outputs/Manuscript/full_draft/compact/technical_review/base_u_comparison');
 await page.goto(pathToFileURL(path.join(base,'report_en.html')).href);await page.evaluate(()=>document.fonts.ready);
 await page.pdf({path:path.join(base,'report_en.pdf'),printBackground:true,preferCSSPageSize:true});
 await browser.close();
})();
