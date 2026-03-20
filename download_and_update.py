import urllib.request, os, time, re

BASE = 'https://www.f328coj.jp'
IMG_DIR = 'images'
os.makedirs(IMG_DIR, exist_ok=True)

REPORT_IMAGES = {
  'report-2024-miura.html': [
    '/uploads/1/0/8/6/108610815/published/sketch-1734393779011.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1734400372031.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1734393448141.png',
    '/uploads/1/0/8/6/108610815/sketch-1734399634488_orig.png',
  ],
  'report-2024-yamanakako.html': [
    '/uploads/1/0/8/6/108610815/published/sketch-1730179995061.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1730179684188-2.png',
    '/uploads/1/0/8/6/108610815/editor/sketch-1730179535433.png',
    '/uploads/1/0/8/6/108610815/editor/sketch-1730179644671.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1730179824796.png',
  ],
  'report-2024-maihama.html': [
    '/uploads/1/0/8/6/108610815/editor/img-4575-2.jpg',
    '/uploads/1/0/8/6/108610815/sketch-1725920579899_orig.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1725921080690.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1725920922643.png',
  ],
  'report-2024-karuizawa.html': [
    '/uploads/1/0/8/6/108610815/sketch-1716252068308_orig.png',
    '/uploads/1/0/8/6/108610815/sketch-1716252287511_orig.png',
    '/uploads/1/0/8/6/108610815/sketch-1716252370009_orig.png',
    '/uploads/1/0/8/6/108610815/sketch-1716296531494_orig.png',
  ],
  'report-2024-yokosuka.html': [
    '/uploads/1/0/8/6/108610815/editor/sketch-1713827964962.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1713827764423.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1713827662656.png',
    '/uploads/1/0/8/6/108610815/editor/sketch-1713828202987.png',
  ],
  'report-2024-328day.html': [
    '/uploads/1/0/8/6/108610815/published/sketch-1711369995461.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1711423115585.png',
    '/uploads/1/0/8/6/108610815/editor/sketch-1711369847054.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1711369582850.png',
    '/uploads/1/0/8/6/108610815/editor/sketch-1711369689588.png',
    '/uploads/1/0/8/6/108610815/published/img-3388.jpg',
  ],
  'report-2024-kujukuri.html': [
    '/uploads/1/0/8/6/108610815/published/sketch-1706570909513.png',
    '/uploads/1/0/8/6/108610815/editor/sketch-1706570702915.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1706579015897.png',
    '/uploads/1/0/8/6/108610815/editor/sketch-1706571366624.png',
  ],
  'report-2023-abarth.html': [
    '/uploads/1/0/8/6/108610815/sketch-1700562694911_orig.png',
    '/uploads/1/0/8/6/108610815/published/img-2791.jpg',
  ],
  'report-2023-wangan.html': [
    '/uploads/1/0/8/6/108610815/published/sketch-1698138429706.png',
    '/uploads/1/0/8/6/108610815/editor/sketch-1698138543640.png',
  ],
  'report-2023-yamanashi.html': [
    '/uploads/1/0/8/6/108610815/img-2581_orig.jpg',
    '/uploads/1/0/8/6/108610815/published/img-2583.jpg',
  ],
  'report-2023-karuizawa.html': [
    '/uploads/1/0/8/6/108610815/published/img-2172-2.jpg',
    '/uploads/1/0/8/6/108610815/ab81ffba6c85360f1b5c3f312c8ec57a4187a39b-3_orig.jpeg',
    '/uploads/1/0/8/6/108610815/published/e706432748949b7ef98ead838db07c193d0ade30.jpeg',
  ],
  'report-2023-miura.html': [
    '/uploads/1/0/8/6/108610815/editor/sketch-1682333324228.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1682333545784.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1682333444206.png',
  ],
  'report-2023-328day.html': [
    '/uploads/1/0/8/6/108610815/editor/sketch-1679904539534.png',
    '/uploads/1/0/8/6/108610815/editor/sketch-1679877969788.png',
    '/uploads/1/0/8/6/108610815/editor/sketch-1679879014291.png',
    '/uploads/1/0/8/6/108610815/editor/17868648203279.jpg',
    '/uploads/1/0/8/6/108610815/editor/sketch-1679878530181.png',
    '/uploads/1/0/8/6/108610815/editor/sketch-1679904446016.png',
  ],
  'report-2023-chiba.html': [
    '/uploads/1/0/8/6/108610815/published/sketch-1674522098291.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1674522864452.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1674522597501.png',
    '/uploads/1/0/8/6/108610815/sketch-1674520121834_orig.png',
    '/uploads/1/0/8/6/108610815/published/cache-messagep2806.jpg',
  ],
  'report-2022-maebashi.html': [
    '/uploads/1/0/8/6/108610815/sketch-1667862468577_orig.png',
    '/uploads/1/0/8/6/108610815/sketch-1667862381344_orig.png',
    '/uploads/1/0/8/6/108610815/editor/sketch-1667862267967.png',
  ],
  'report-2022-daijo.html': [
    '/uploads/1/0/8/6/108610815/editor/sketch-1665661289386.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1665661365323.png',
  ],
  'report-2022-hakone.html': [
    '/uploads/1/0/8/6/108610815/published/sketch-1662951395214.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1663020762231.png',
    '/uploads/1/0/8/6/108610815/sketch-1662950979697_orig.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1662950909175.png',
  ],
  'report-2022-karuizawa.html': [
    '/uploads/1/0/8/6/108610815/published/sketch-1653348178504.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1653348068382.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1653353883221.png',
    '/uploads/1/0/8/6/108610815/published/img-0984.jpg',
  ],
  'report-2022-kanagawa.html': [
    '/uploads/1/0/8/6/108610815/sketch-1650278358145_orig.png',
    '/uploads/1/0/8/6/108610815/sketch-1650277293886_orig.png',
    '/uploads/1/0/8/6/108610815/sketch-1650276997357_orig.png',
  ],
  'report-2022-328day.html': [
    '/uploads/1/0/8/6/108610815/sketch-1648382931890_orig.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1648380325929.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1648383119603.png',
  ],
  'report-2021-saitama.html': [
    '/uploads/1/0/8/6/108610815/published/sketch-1638159774804.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1638162091333-2.png',
    '/uploads/1/0/8/6/108610815/sketch-1638159671920_orig.png',
  ],
  'report-2021-hakone.html': [
    '/uploads/1/0/8/6/108610815/published/sketch-1635118708332.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1635114143048.png',
  ],
  'report-2021-328day.html': [
    '/uploads/1/0/8/6/108610815/20210329-080939_orig.jpg',
    '/uploads/1/0/8/6/108610815/published/20210329-080636.jpg',
  ],
  'report-2020-oiso.html': [
    '/uploads/1/0/8/6/108610815/editor/20201108-165140.jpg',
    '/uploads/1/0/8/6/108610815/20201108-203453_orig.jpg',
    '/uploads/1/0/8/6/108610815/published/20201108-165453.jpg',
    '/uploads/1/0/8/6/108610815/published/dsc02562-li.jpg',
  ],
  'report-2020-odaiba.html': [
    '/uploads/1/0/8/6/108610815/published/20201025-125816.jpg',
    '/uploads/1/0/8/6/108610815/20201025-125243_orig.jpg',
  ],
  'report-2020-yamanakako.html': [
    '/uploads/1/0/8/6/108610815/editor/20200927-210651.jpg',
    '/uploads/1/0/8/6/108610815/editor/20200928-055459.jpg',
  ],
  'report-2020-odawara.html': [
    '/uploads/1/0/8/6/108610815/published/20200121-082110.jpg',
    '/uploads/1/0/8/6/108610815/published/20200120-215929.jpg',
    '/uploads/1/0/8/6/108610815/published/20200121-083821.jpg',
  ],
  'report-2019-party.html': [
    '/uploads/1/0/8/6/108610815/published/37302.jpg',
    '/uploads/1/0/8/6/108610815/editor/20191202-084600.jpg',
  ],
  'report-2019-hakone.html': [
    '/uploads/1/0/8/6/108610815/editor/20191119-083312.jpg',
    '/uploads/1/0/8/6/108610815/published/20191119-075403.jpg',
    '/uploads/1/0/8/6/108610815/published/20191119-075014.jpg',
    '/uploads/1/0/8/6/108610815/editor/20191119-083014.jpg',
  ],
  'report-2019-gunma.html': [
    '/uploads/1/0/8/6/108610815/editor/20191028-162808.jpg',
    '/uploads/1/0/8/6/108610815/published/sketch-1572349159095.png',
    '/uploads/1/0/8/6/108610815/published/dsc-1280.jpg',
    '/uploads/1/0/8/6/108610815/editor/20191029-205434.jpg',
    '/uploads/1/0/8/6/108610815/editor/20191028-162300.jpg',
  ],
  'report-2019-yamanashi.html': [
    '/uploads/1/0/8/6/108610815/2019929_orig.png',
    '/uploads/1/0/8/6/108610815/editor/498017130.png',
    '/uploads/1/0/8/6/108610815/editor/20190929.png',
  ],
  'report-2019-karuizawa.html': [
    '/uploads/1/0/8/6/108610815/published/20190521-2.jpg',
    '/uploads/1/0/8/6/108610815/editor/20190521.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1558999740564.png',
  ],
  'report-2019-scw.html': [
    '/uploads/1/0/8/6/108610815/published/dsc-1053.jpg',
    '/uploads/1/0/8/6/108610815/editor/sketch-1555891865277.png',
    '/uploads/1/0/8/6/108610815/editor/dsc-1060.jpg',
    '/uploads/1/0/8/6/108610815/published/sketch-1555923571524.png',
    '/uploads/1/0/8/6/108610815/published/sketch-1555924850302.png',
  ],
  'report-2019-328day.html': [
    '/uploads/1/0/8/6/108610815/published/2019328day-2.jpg',
    '/uploads/1/0/8/6/108610815/published/2019328day.jpg',
    '/uploads/1/0/8/6/108610815/published/2019328day-3.jpg',
  ],
  'report-2019-yokosuka.html': [
    '/uploads/1/0/8/6/108610815/published/201901-3.jpg',
    '/uploads/1/0/8/6/108610815/published/201901.jpg',
    '/uploads/1/0/8/6/108610815/editor/201901-2.jpg',
  ],
  'report-2018-party.html': [
    '/uploads/1/0/8/6/108610815/published/20181202.jpg',
    '/uploads/1/0/8/6/108610815/published/20181202_1.jpg',
  ],
}

# Step 1: Download missing images
print('=== Downloading missing images ===')
ok = ng = skip = 0
for page, paths in REPORT_IMAGES.items():
    for path in paths:
        fname = path.split('/')[-1]
        local = os.path.join(IMG_DIR, fname)
        if os.path.exists(local):
            skip += 1
            continue
        url = BASE + path
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=15) as r, open(local, 'wb') as f:
                f.write(r.read())
            print(f'OK: {fname}')
            ok += 1
            time.sleep(0.2)
        except Exception as e:
            print(f'NG: {fname} -- {e}')
            ng += 1

print(f'Downloaded: {ok}, Skipped: {skip}, Failed: {ng}')

# Step 2: Update each report HTML to replace coming-soon with actual photos
PHOTO_STYLE = '''  <style>
  .report-content{max-width:900px;margin:0 auto}
  .report-meta{display:flex;gap:24px;flex-wrap:wrap;margin-bottom:40px;padding-bottom:32px;border-bottom:1px solid rgba(255,255,255,0.08)}
  .report-meta-item{display:flex;flex-direction:column;gap:4px}
  .report-meta-label{font-size:9px;letter-spacing:3px;text-transform:uppercase;color:var(--gold)}
  .report-meta-value{font-size:14px;font-weight:600}
  .report-photos{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:8px;margin-bottom:48px}
  .report-photo{width:100%;aspect-ratio:4/3;object-fit:cover;display:block;background:var(--gray)}
  .report-nav{display:flex;justify-content:space-between;padding-top:40px;border-top:1px solid rgba(255,255,255,0.08)}
  </style>'''

print()
print('=== Updating HTML files ===')
for page, paths in REPORT_IMAGES.items():
    if not os.path.exists(page):
        print(f'SKIP (no file): {page}')
        continue

    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()

    # Build photo grid HTML
    imgs = []
    for path in paths:
        fname = path.split('/')[-1]
        local = os.path.join(IMG_DIR, fname)
        if os.path.exists(local):
            imgs.append(f'      <img class="report-photo" src="images/{fname}" alt="">')

    if not imgs:
        print(f'SKIP (no local images): {page}')
        continue

    photo_grid = '    <div class="report-photos">\n' + '\n'.join(imgs) + '\n    </div>'

    # Replace <style> block
    content = re.sub(r'<style>.*?</style>', PHOTO_STYLE, content, count=1, flags=re.DOTALL)

    # Replace coming-soon block with photo grid
    content = re.sub(
        r'<div class="coming-soon">.*?</div>\s*',
        photo_grid + '\n    ',
        content, count=1, flags=re.DOTALL
    )

    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated: {page} ({len(imgs)} photos)')

print()
print('Done.')
