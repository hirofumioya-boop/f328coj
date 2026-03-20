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

    # Remove entire footer-grid div (contains brand + nav links)
    content = re.sub(r'\s*<div class="footer-grid">.*?</div>\s*(?=<div class="footer-bottom">)', '', content, flags=re.DOTALL)

    if content != original:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        count += 1
        print(f'Updated: {f}')

print(f'Total: {count} files updated')
