import glob, os, re

html_files = glob.glob('**/*.html', recursive=True) + ['index.html']
seen = set()
count = 0

for f in html_files:
    norm = os.path.normpath(f)
    if norm in seen or not os.path.exists(f):
        continue
    seen.add(norm)

    fslash = norm.replace(os.sep, '/')

    # Skip links.html and news.html (already have correct nav)
    if 'links/links.html' in fslash or 'news/news.html' in fslash:
        continue

    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    original = content

    # Determine depth and root path
    depth = norm.count(os.sep)
    if depth == 0:
        root = ''
        links_path = 'links/links.html'
    elif depth == 1:
        root = '../'
        links_path = '../links/links.html'
    else:
        root = '../../'
        links_path = '../../links/links.html'

    # Insert リンク in nav-links between ムービー and 入会について
    content = re.sub(
        r'(<li><a href="[^"]*#movie">ムービー</a></li>)',
        r'\1\n      <li><a href="' + links_path + r'">リンク</a></li>',
        content
    )
    # Insert リンク in mobile menu between ムービー and 入会について
    content = re.sub(
        r'(<a href="[^"]*#movie" onclick="toggleMenu\(\)">ムービー</a>)',
        r'\1\n    <a href="' + links_path + r'" onclick="toggleMenu()">リンク</a>',
        content
    )

    if content != original:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        count += 1

print(f'Updated: {count} files')
