import glob, os, re

html_files = glob.glob('**/*.html', recursive=True) + ['index.html']
seen = set()
count = 0

for f in html_files:
    norm = os.path.normpath(f)
    if norm in seen or not os.path.exists(f):
        continue
    seen.add(norm)

    # Skip news.html and index.html (handled separately)
    fslash = norm.replace(os.sep, '/')
    if 'news/news.html' in fslash or fslash == 'index.html':
        continue

    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    original = content

    # Determine depth
    depth = norm.count(os.sep)
    if depth == 1:
        # touring/touring.html, gallery/gallery.html, restore/restore.html
        root = '../'
    else:
        # touring/archive/*.html, touring/report/*.html
        root = '../../'

    # Build standard nav links
    # Determine active page
    if 'touring' in fslash and 'archive' not in fslash and 'report' not in fslash:
        touring_active = ' class="active"'
    else:
        touring_active = ''

    if 'gallery' in fslash:
        gallery_active = ' class="active"'
    else:
        gallery_active = ''

    new_nav_links = f'''<ul class="nav-links">
      <li><a href="{root}index.html">ホーム</a></li>
      <li><a href="{root}index.html#about">当クラブについて</a></li>
      <li><a href="{root}news/news.html">更新情報</a></li>
      <li><a href="{root}touring/touring.html"{touring_active}>ツーリングレポート</a></li>
      <li><a href="{root}gallery/gallery.html"{gallery_active}>フォトギャラリー</a></li>
      <li><a href="{root}index.html#movie">ムービー</a></li>
      <li><a href="{root}index.html#membership">入会について</a></li>
      <li><a href="{root}index.html#contact">お問合せ</a></li>
    </ul>'''

    new_mobile_menu = f'''<div class="mobile-menu" id="mobileMenu">
    <a href="{root}index.html" onclick="toggleMenu()">ホーム</a>
    <a href="{root}index.html#about" onclick="toggleMenu()">当クラブについて</a>
    <a href="{root}news/news.html" onclick="toggleMenu()">更新情報</a>
    <a href="{root}touring/touring.html" onclick="toggleMenu()">ツーリングレポート</a>
    <a href="{root}gallery/gallery.html" onclick="toggleMenu()">フォトギャラリー</a>
    <a href="{root}index.html#movie" onclick="toggleMenu()">ムービー</a>
    <a href="{root}index.html#membership" onclick="toggleMenu()">入会について</a>
    <a href="{root}index.html#contact" onclick="toggleMenu()">お問合せ</a>
  </div>'''

    # Replace nav-links block
    content = re.sub(
        r'<ul class="nav-links">.*?</ul>',
        new_nav_links,
        content,
        flags=re.DOTALL
    )
    # Replace mobile-menu block
    content = re.sub(
        r'<div class="mobile-menu" id="mobileMenu">.*?</div>',
        new_mobile_menu,
        content,
        flags=re.DOTALL
    )

    if content != original:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        count += 1
        print(f'Updated: {f}')

print(f'\nTotal: {count} files updated')
