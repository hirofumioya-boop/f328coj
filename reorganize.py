import os, re, shutil

BASE = r'H:\マイドライブ\Claude Code\ferrari-redesign'
os.chdir(BASE)

# ── File mapping: old_name → new_relative_path ──────────────────────────
FILE_MAP = {
    'index.html':      'index.html',
    'style.css':       'style.css',
    'hero.jpg':        'hero.jpg',
    'touring.html':    'touring/index.html',
    'gallery.html':    'gallery/index.html',
    'movie.html':      'movie/index.html',
    'restore.html':    'restore/index.html',
    'membership.html': 'membership/index.html',
    'contact.html':    'contact/index.html',
    'archive-2018.html': 'touring/archive/2018.html',
    'archive-2019.html': 'touring/archive/2019.html',
    'archive-2020.html': 'touring/archive/2020.html',
    'archive-2021.html': 'touring/archive/2021.html',
    'archive-2022.html': 'touring/archive/2022.html',
    'archive-2023.html': 'touring/archive/2023.html',
    'archive-2024.html': 'touring/archive/2024.html',
}

# Add all report-*.html files
for fn in sorted(os.listdir('.')):
    if fn.startswith('report-') and fn.endswith('.html'):
        new_name = fn[len('report-'):]  # strip 'report-' prefix
        FILE_MAP[fn] = f'touring/report/{new_name}'

print(f'Total files to process: {len(FILE_MAP)}')

# ── Helper: compute relative path ────────────────────────────────────────
def compute_rel(old_ref, current_new_path):
    """Given an old filename and the current file's new path, return new relative href."""
    if old_ref not in FILE_MAP:
        return None
    target = FILE_MAP[old_ref]
    current_dir = os.path.dirname(current_new_path).replace('\\', '/')
    if not current_dir:
        current_dir = '.'
    rel = os.path.relpath(target, current_dir).replace('\\', '/')
    return rel

# ── Fix all paths in content ──────────────────────────────────────────────
def fix_content(content, current_new_path):
    depth = len([p for p in current_new_path.split('/') if p]) - 1
    root = '../' * depth if depth > 0 else ''

    # style.css link
    content = re.sub(r'href="(?:\.\./)*style\.css"', f'href="{root}style.css"', content)

    # images/ in src=
    content = re.sub(r'src="(?:\.\./)*images/', f'src="{root}images/', content)

    # images/ in CSS url()
    content = re.sub(r"url\('(?:\.\./)*images/", f"url('{root}images/", content)

    # hero.jpg in CSS url()
    content = re.sub(r"url\('(?:\.\./)*hero\.jpg'\)", f"url('{root}hero.jpg')", content)

    # href links to known HTML files (skip http/https/mailto/#)
    def replace_href(m):
        old_ref = m.group(1)
        if old_ref.startswith(('http', 'mailto', '#', '/')):
            return m.group(0)
        new_rel = compute_rel(old_ref, current_new_path)
        if new_rel:
            return f'href="{new_rel}"'
        return m.group(0)

    content = re.sub(r'href="([^"]*)"', replace_href, content)

    return content

# ── Create directories ────────────────────────────────────────────────────
for new_path in FILE_MAP.values():
    d = os.path.dirname(new_path)
    if d:
        os.makedirs(d, exist_ok=True)

# ── Process each file ─────────────────────────────────────────────────────
moved = skipped = 0
for old_name, new_path in FILE_MAP.items():
    if not os.path.exists(old_name):
        print(f'  MISSING: {old_name}')
        skipped += 1
        continue
    if old_name in ('style.css', 'hero.jpg'):
        # Non-HTML assets that don't move: skip content processing
        if old_name != new_path:
            shutil.copy2(old_name, new_path)
        continue

    with open(old_name, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = fix_content(content, new_path)

    with open(new_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    # Delete old file if it moved
    if old_name != new_path:
        os.remove(old_name)
        moved += 1

print(f'Moved & updated: {moved}, Skipped: {skipped}')
print('Done.')
