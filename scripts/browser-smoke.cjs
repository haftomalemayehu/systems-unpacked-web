const { chromium } = require('playwright');
const pages = ['/', '/projects/', '/knowledge/', '/references/', '/about/', '/blog/', '/resume/', '/contact/', '/privacy/', '/terms/'];
(async () => {
 const browser = await chromium.launch({headless:true});
 let failed = 0;
 for (const width of [390, 1440]) {
  const page = await browser.newPage({viewport:{width,height:850}});
  page.on('pageerror', error => { console.error('Browser error:',error.message); failed++; });
  for (const path of pages) {
   const response = await page.goto('http://127.0.0.1:8000'+path,{waitUntil:'networkidle'});
   if (!response || response.status() >= 400) {console.error('HTTP failure',path,response?.status());failed++;}
   const h1 = await page.locator('main h1').count();
   if (h1 !== 1) {console.error('Heading count',path,h1);failed++;}
   if (width === 390 && await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2)) {console.error('Horizontal overflow',path);failed++;}
   if (path === '/projects/') {
    const svg = page.locator('svg.cicd-illustration');
    if (await svg.count()) {
     const bounds = await svg.boundingBox();
     if (!bounds || bounds.width < 100 || bounds.height < 100) {console.error('CI/CD diagram invisible');failed++;}
    }
   }
  }
  if (width === 390) {
   await page.goto('http://127.0.0.1:8000/');
   const menu=page.locator('.mobile-navigation summary');
   await menu.click();
   if (!(await page.locator('.mobile-navigation').evaluate(el=>el.open))) {console.error('Mobile menu failed');failed++;}
   await menu.press('Enter');
  }
  await page.close();
 }
 await browser.close();
 if(failed)process.exit(1);
 console.log('Browser smoke tests passed on mobile and desktop.');
})().catch(err=>{console.error(err);process.exit(1)});
