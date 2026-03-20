import glob, os, re

html_files = glob.glob('**/*.html', recursive=True) + ['index.html']
seen = set()
count = 0

for f in html_files:
    norm = os.path.normpath(f)
    if norm in seen or not os.path.exists(f):
        continue
    seen.add(norm)

    # Skip news.html itself
    if 'news' in norm.replace(os.sep, '/'):
        continue

    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    original = content

    # Determine relative path to news/news.html
    depth = norm.count(os.sep)
    if depth == 0:
        news_path = 'news/news.html'
    elif depth == 1:
        news_path = '../news/news.html'
    else:
        news_path = '../../news/news.html'

    # Insert in nav-links after 当クラブについて
    content = re.sub(
        r'(<li><a href="[^"]*#about">当クラブについて</a></li>)',
        r'\1\n      <li><a href="' + news_path + r'">更新情報</a></li>',
        content
    )
    # Insert in mobile menu after 当クラブについて
    content = re.sub(
        r'(<a href="[^"]*#about" onclick="toggleMenu\(\)">当クラブについて</a>)',
        r'\1\n    <a href="' + news_path + r'" onclick="toggleMenu()">更新情報</a>',
        content
    )

    if content != original:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        count += 1

print(f'Updated: {count} files')
