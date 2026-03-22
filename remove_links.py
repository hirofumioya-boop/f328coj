import glob, re

# ============================================================
# 1. index.html からリンクセクションとナビリンクを削除
# ============================================================
with open('index.html', encoding='utf-8') as f:
    content = f.read()

# リンクセクション全体を削除
content = re.sub(
    r'\n\n  <!-- LINKS -->\n  <section class="links-section" id="links">.*?</section>\n',
    '\n', content, flags=re.DOTALL
)

# デスクトップナビからリンク削除
content = content.replace(
    '\n      <li><a href="index.html#links">リンク</a></li>',
    ''
)

# モバイルメニューからリンク削除
content = content.replace(
    '\n    <a href="index.html#links" onclick="toggleMenu()">リンク</a>',
    ''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('index.html updated')

# ============================================================
# 2. 全サブページのナビからリンクを削除
# ============================================================
files = (
    glob.glob('news/*.html') +
    glob.glob('touring/*.html') +
    glob.glob('touring/archive/*.html') +
    glob.glob('touring/report/*.html')
)

for filepath in files:
    with open(filepath, encoding='utf-8') as f:
        c = f.read()
    original = c
    c = re.sub(r'\s*<li><a href="[^"]*#links"[^>]*>リンク</a></li>', '', c)
    c = re.sub(r'\s*<a href="[^"]*#links" onclick="toggleMenu\(\)">リンク</a>', '', c)
    if c != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'Updated: {filepath}')

print('All done!')
