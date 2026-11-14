"""Run with Python and Playwright/Chromium installed in the cloud environment."""
from pathlib import Path
import os
os.chdir(Path(__file__).resolve().parents[1])
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import threading,json
from playwright.sync_api import sync_playwright
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),Quiet);threading.Thread(target=server.serve_forever,daemon=True).start();base='http://127.0.0.1:'+str(server.server_port)
source=json.load(open('docs/content-reference.json'))['prices']
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for width in [320,375,390,430,768,1440]:
  page=b.new_page(viewport={'width':width,'height':850});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto(base,wait_until='domcontentloaded');page.evaluate('document.fonts.ready')
  rows=page.locator('.ptable tbody tr');assert rows.count()==27
  for row,r in zip(rows.all(),source):
   assert row.locator('th').inner_text().replace('\n','')==r['breed']
   actual=[x.replace(',','') for x in row.locator('.course-amount').all_text_contents()];assert actual==[r['shampoo'],r['cut']],actual
  if width<=600:
   assert page.locator('.mobile-course').first.is_visible()
   assert page.locator('.mobile-course').evaluate_all('(xs)=>xs.every(x=>x.scrollWidth<=x.clientWidth)')
   for note in page.locator('.breed-note').all():assert note.evaluate('(x)=>x.offsetHeight<25')
  else:assert not page.locator('.mobile-course').first.is_visible()
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
  page.locator('.sticky a[href="#price"]' if width<=900 else '.hero a[href="#price"]').click()
  page.wait_for_function("location.hash==='#price' && scrollY>100")
  page.wait_for_timeout(600)
  page.evaluate("scrollTo({top:document.querySelector('.price-wrap').getBoundingClientRect().top+scrollY-100,behavior:'instant'})")
  page.screenshot(path=f'/tmp/biscuit-readable-prices-{width}.png')
  page.reload(wait_until='domcontentloaded');page.evaluate('document.fonts.ready');page.wait_for_function("scrollY===0 && location.hash===''")
  page.goto(base+'/?direct=1#price',wait_until='load');page.wait_for_function("location.hash==='#price' && scrollY>100")
  page.reload(wait_until='domcontentloaded');page.wait_for_function("scrollY===0 && location.hash===''")
  assert not errors,errors
  print('PASS',width,'all prices, names, weight conditions, label layout, reload reset and direct links')
  page.close()
 b.close()
server.shutdown()
