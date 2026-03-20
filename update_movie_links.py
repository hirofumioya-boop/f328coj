import os, glob, re

html_files = glob.glob('**/*.html', recursive=True) + ['index.html']
seen = set()
files = []
for f in html_files:
    norm = os.path.normpath(f)
    if norm not in seen and os.path.exists(f):
        seen.add(norm)
        files.append(f)

count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    original = content

    depth = f.replace('\\', '/').count('/')

    # Replace movie/movie.html links with index.html#movie at correct depth
    if depth == 1:
        content = content.replace('../movie/movie.html', '../index.html#movie')
    elif depth >= 2:
        content = content.replace('../../movie/movie.html', '../../index.html#movie')

    # Remove standalone footer div containing only the movie link
    content = re.sub(
        r'<div>\s*\n?\s*\n?\s*<ul class="footer-nav-links">\s*\n?\s*<li><a href="[^"]*index\.html#movie">ムービー</a></li>\s*\n?\s*</ul>\s*\n?\s*</div>',
        '',
        content
    )

    if content != original:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        count += 1
        print(f'Updated: {f}')

print(f'Total: {count} files updated')
