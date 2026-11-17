"""Check unbroken step labels and a circular portrait placeholder across viewport sizes."""
from pathlib import Path
import os
os.chdir(Path(__file__).resolve().parents[1])
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright
import threading
class Q(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
s=ThreadingHTTPServer(('127.0.0.1',0),Q);threading.Thread(target=s.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for width in [320,375,390,430,600,768,900,1440]:
  page=b.new_page(viewport={'width':width,'height':950});errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto('http://127.0.0.1:'+str(s.server_port),wait_until='domcontentloaded');page.evaluate('document.fonts.ready')
  circle=page.locator('.hero-photo .sub').bounding_box();assert abs(circle['width']-circle['height'])<1,circle
  for word in page.locator('.step-word').all():
   assert word.evaluate('(e)=>e.getBoundingClientRect().height<=parseFloat(getComputedStyle(e).lineHeight)+1')
   assert word.evaluate('(e)=>e.getBoundingClientRect().right<=e.closest("li").getBoundingClientRect().right-8')
  assert page.locator('.portrait-content').evaluate('(e)=>e.scrollHeight<=e.clientHeight')
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth');assert not errors
  if width in [320,390,1440]:
   page.locator('.hero-photo').screenshot(path=f'/tmp/biscuit-circle-fixed-{width}.png');page.locator('.steps').screenshot(path=f'/tmp/biscuit-steps-fixed-{width}.png')
  print('PASS',width,'circle',round(circle['width'],2),round(circle['height'],2),'intact words and no clipping')
  page.close()
 b.close()
s.shutdown()
