import urllib.request, os, time, re

BASE = 'https://www.f328coj.jp'
IMG_DIR = 'images'

# ── 1. レストアページ写真のダウンロード ─────────────────────────────────
RESTORE_URLS = [
    '/uploads/1/0/8/6/108610815/dscf2063a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2064a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2067a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2071a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2082a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2084a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2087a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2088a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2095a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2096a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2097a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2101a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2104a.jpg',
    '/uploads/1/0/8/6/108610815/pic005a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2109a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2111a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2122a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2127a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2130a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2188a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2191a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2193a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2247a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2248a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2252a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2261a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2269a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2278a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2291a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2295a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2301a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2307a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2311a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2312a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2315a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2318a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2319a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2325aa.jpg',
    '/uploads/1/0/8/6/108610815/dscf2332a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2335a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2347a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2350a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2362a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2380a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2381a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2383a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2385a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2387a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2391a.jpg',
    '/uploads/1/0/8/6/108610815/dscf2392a.jpg',
    '/uploads/1/0/8/6/108610815/pic001a.jpg',
    '/uploads/1/0/8/6/108610815/pic002a.jpg',
    '/uploads/1/0/8/6/108610815/pic003a.jpg',
    '/uploads/1/0/8/6/108610815/pic004a.jpg',
    '/uploads/1/0/8/6/108610815/pic01.jpg',
    '/uploads/1/0/8/6/108610815/pic02.jpg',
    '/uploads/1/0/8/6/108610815/pic03.jpg',
]

print('=== Downloading restore photos ===')
ok = ng = skip = 0
for path in RESTORE_URLS:
    fname = path.split('/')[-1]
    local = os.path.join(IMG_DIR, fname)
    if os.path.exists(local):
        skip += 1
        continue
    try:
        req = urllib.request.Request(BASE + path, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as r, open(local, 'wb') as f:
            f.write(r.read())
        print(f'OK: {fname}')
        ok += 1
        time.sleep(0.2)
    except Exception as e:
        print(f'NG: {fname} -- {e}')
        ng += 1

print(f'Restore: {ok} downloaded, {skip} skipped, {ng} failed')

# ── 2. レストアページのalbu-thumbをimgに差し替え ─────────────────────────
restore_imgs = [f for f in os.listdir(IMG_DIR) if f.startswith('dscf') or f.startswith('pic0')]
restore_imgs.sort()

with open('restore/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build img tags for restore (show first 20, rest as more)
img_tags = '\n'.join(
    f'      <img class="album-thumb" src="../images/{fn}" alt="レストア記録" loading="lazy">'
    for fn in restore_imgs[:20]
)

# Replace all album-thumb divs block with img tags
content = re.sub(
    r'(<div class="album-grid">)\s*(<div class="album-thumb"[^>]*></div>\s*)+</div>',
    r'\1\n' + img_tags + '\n    </div>',
    content,
    count=1,
    flags=re.DOTALL
)

# Update CSS for img
content = content.replace(
    '.album-thumb {',
    '.album-thumb { width:100%; aspect-ratio:4/3; object-fit:cover; display:block; background:var(--gray); /* '
)
content = content.replace(
    'background: var(--gray); /* ',
    'background: var(--gray); '
)

with open('restore/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated: restore/index.html')

# ── 3. ギャラリーページの写真を実写真に差し替え ────────────────────────────
# 各イベントの写真マッピング (gallery/index.htmlの順に合わせる)
GALLERY_ALBUMS = [
    {
        'title': '2018年5月27日 群馬ラリー',
        'imgs': ['201810_2.jpg', '20181122_1.jpg'],
    },
    {
        'title': '2018年5月20日 那須高原ツーリング',
        'imgs': ['01_10.jpg','02_12.jpg','03_9.jpg','04_9.jpg','05_5.jpg','06_10.jpg','07_9.jpg','08_8.jpg'],
    },
    {
        'title': '2018年2月 銚子ツーリング',
        'imgs': ['20181120-203521_1.jpg','20181120-205157_1.jpg','2018z_1.jpg'],
    },
    {
        'title': '2018年1月 佐島ツーリング',
        'imgs': ['20181202.jpg','20181202_1.jpg'],
    },
    {
        'title': '2017年1月 伊豆ツーリング',
        'imgs': ['1_3.jpg','2_3.jpg','3_3.jpg','4_3.jpg'],
    },
    {
        'title': '2017年2月 千葉鴨川ツーリング',
        'imgs': ['01_9.jpg','02_11.jpg','03_8.jpg','04_8.jpg','05_6.jpg','06_9.jpg','07_8.jpg','07_2.gif'],
    },
    {
        'title': '2017年3月 328DAYツーリング',
        'imgs': ['01_11.jpg','02_10.jpg','02_13.jpg','03_10.jpg','04_10.jpg','04_1.gif','01_2.gif'],
    },
    {
        'title': '2017年4月 高尾山うかい鳥山ツーリング',
        'imgs': ['45_2.jpg','1_3.jpg','2_3.jpg','3_3.jpg','4_3.jpg'],
    },
]

with open('gallery/index.html', 'r', encoding='utf-8') as f:
    gcontent = f.read()

def make_album_grid(imgs):
    # Only use imgs that exist locally
    tags = []
    for fn in imgs:
        local = os.path.join(IMG_DIR, fn)
        if os.path.exists(local):
            tags.append(f'          <img class="album-thumb" src="../images/{fn}" alt="" loading="lazy">')
    if not tags:
        return None
    return '\n'.join(tags)

# Replace each album-grid's empty divs with real imgs
for album in GALLERY_ALBUMS:
    grid_html = make_album_grid(album['imgs'])
    if not grid_html:
        continue
    # Match the album section by title, then replace its album-grid content
    pattern = (
        r'((?:<h2 class="album-title">' + re.escape(album['title']) + r'</h2>).*?'
        r'<div class="album-grid">)\s*(?:<div class="album-thumb[^"]*"[^>]*></div>\s*)+</div>'
    )
    replacement = r'\1\n' + grid_html + '\n        </div>'
    gcontent, n = re.subn(pattern, replacement, gcontent, count=1, flags=re.DOTALL)
    if n:
        print(f'Gallery updated: {album["title"]}')
    else:
        print(f'Gallery SKIP: {album["title"]}')

# Update CSS so album-thumb img works
gcontent = re.sub(
    r'\.album-thumb \{[^}]*\}',
    '.album-thumb { width:100%; aspect-ratio:4/3; object-fit:cover; display:block; background:var(--gray); }',
    gcontent
)
# Remove color override rules for nth-child (they conflict with img display)
gcontent = re.sub(r'    \.album-thumb:nth-child\(8n\+\d+\)\s*\{[^}]*\}\n', '', gcontent)

with open('gallery/index.html', 'w', encoding='utf-8') as f:
    f.write(gcontent)
print('Updated: gallery/index.html')
print('Done.')
