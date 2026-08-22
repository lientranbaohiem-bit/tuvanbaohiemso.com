# -*- coding: utf-8 -*-
"""Dung file xem truoc gop tat ca trang vao 1 file HTML"""
import re, os, urllib.parse

css = open('assets/css/style.css', encoding='utf-8').read()
js = open('assets/js/main.js', encoding='utf-8').read()

imgs = {}
for f in os.listdir('assets/img'):
    raw = open('assets/img/' + f, encoding='utf-8').read()
    imgs[f] = 'data:image/svg+xml;utf8,' + urllib.parse.quote(raw)

PAGES = [('index.html', 'index'), ('san-pham.html', 'san-pham'), ('thai-san.html', 'thai-san'),
         ('suc-khoe.html', 'suc-khoe'), ('bao-ve-thu-nhap.html', 'bao-ve-thu-nhap'),
         ('cong-cu.html', 'cong-cu'), ('ve-chung-toi.html', 've-chung-toi'), ('lien-he.html', 'lien-he'),
         ('kien-thuc/index.html', 'kien-thuc-index'),
         ('kien-thuc/chi-phi-sinh-con.html', 'kien-thuc-chi-phi-sinh-con'),
         ('kien-thuc/thoi-gian-cho-thai-san.html', 'kien-thuc-thoi-gian-cho-thai-san'),
         ('kien-thuc/ke-khai-suc-khoe.html', 'kien-thuc-ke-khai-suc-khoe')]


def slug_for(href, base):
    href = href.split('?')[0].split('#')[0]
    if not href.endswith('.html'):
        return None
    if href.startswith('../'):
        href = href[3:]
    elif base.startswith('kien-thuc/') and '/' not in href:
        href = 'kien-thuc/' + href
    return href.replace('/', '-').replace('.html', '')


def cut(html, start, end_tag='</div>'):
    """Xoa mot khoi bat dau bang chuoi start cho toi the dong ngoai cung."""
    i = html.find(start)
    if i < 0:
        return html
    depth = 0
    j = i
    while j < len(html):
        if html.startswith('<div', j):
            depth += 1
        elif html.startswith('</div>', j):
            depth -= 1
            if depth == 0:
                return html[:i] + html[j + 6:]
        j += 1
    return html


parts = []
for path, sid in PAGES:
    html = open(path, encoding='utf-8').read()
    body = re.search(r'<body[^>]*>(.*)</body>', html, re.S).group(1)
    body = re.sub(r'<script src="[^"]*"></script>', '', body)
    if sid != 'index':
        body = cut(body, '<div class="gate" id="needGate"')
        body = cut(body, '<div class="track-band" id="trackBand">')
        body = body.replace('id="burger"', 'id="b-' + sid + '"').replace('id="mobileNav"', 'id="m-' + sid + '"')

    def fiximg(m):
        f = m.group(1).split('/')[-1]
        return 'src="%s"' % imgs.get(f, m.group(1))
    body = re.sub(r'src="([^"]*assets/img/[^"]+)"', fiximg, body)

    def fixhref(m):
        h = m.group(1)
        s2 = slug_for(h, path)
        return 'href="#pv-%s"' % s2 if s2 else m.group(0)
    body = re.sub(r'href="([^"]+\.html(?:\?[^"#]*)?(?:#[^"]*)?)"', fixhref, body)

    def fixgo(m):
        s3 = slug_for(m.group(1), path)
        return 'data-go="#pv-%s"' % s3 if s3 else m.group(0)
    body = re.sub(r'data-go="([^"]+)"', fixgo, body)
    body = re.sub(r'data-open-gate="[^"]*"', 'data-open-gate="#pv-index"', body)
    parts.append('<div class="pv-page" id="pv-%s" style="display:none">%s</div>' % (sid, body))

router = """
(function(){
  function show(){
    var id = location.hash.replace('#','') || 'pv-index';
    if(id.indexOf('pv-')!==0) return;
    var pages=document.querySelectorAll('.pv-page');
    var found=document.getElementById(id)||document.getElementById('pv-index');
    for(var i=0;i<pages.length;i++) pages[i].style.display='none';
    found.style.display='block';
    window.scrollTo(0,0);
    if(window.__pvInit) window.__pvInit();
  }
  window.addEventListener('hashchange', show);
  show();
})();
"""

banner = """<div style="position:fixed;left:0;right:0;bottom:0;z-index:1200;background:#16181D;color:#fff;
padding:9px 16px;font:500 12.5px/1.5 system-ui,sans-serif;text-align:center">
Ban xem truoc gop 12 trang trong 1 file &middot; bam menu de chuyen trang &middot; popup chon nhu cau chi hoat dong o trang chu
</div><div style="height:38px"></div>"""

out = ('<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8">'
       '<meta name="viewport" content="width=device-width,initial-scale=1">'
       '<title>Xem truoc - tuvanbaohiemso.com</title>'
       '<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
       '<style>' + css + '\n.pv-page .fab{bottom:56px}</style></head><body data-gate-auto>'
       + ''.join(parts) + banner
       + '<script>window.__pvInit=function(){' + js + '};</script>'
       + '<script>' + router + '</script></body></html>')

open('/home/claude/xem-truoc-tuvanbaohiemso.html', 'w', encoding='utf-8').write(out)
print('preview:', len(out) // 1024, 'KB')
