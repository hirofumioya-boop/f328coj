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
    if 'links/links.html' in fslash:
        continue

    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    original = content

    depth = norm.count(os.sep)
    if depth == 0:
        index_path = 'index.html#links'
    elif depth == 1:
        index_path = '../index.html#links'
    else:
        index_path = '../../index.html#links'

    # Replace links/links.html with index.html#links in nav
    content = re.sub(r'[./]*links/links\.html', index_path, content)

    if content != original:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        count += 1

print(f'Updated: {count} files')
