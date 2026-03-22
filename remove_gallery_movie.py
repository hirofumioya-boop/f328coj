import re, os, glob

# ============================================================
# 1. index.html からギャラリー・ムービーセクションを削除
# ============================================================
with open('index.html', encoding='utf-8') as f:
    content = f.read()

# ギャラリーセクションを削除（250-277行）
content = re.sub(
    r'\n  <section class="gallery" id="gallery">.*?</section>\n',
    '\n', content, flags=re.DOTALL
)

# ムービーセクションを削除（<!-- MOVIE --> コメントごと）
content = re.sub(
    r'\n  <!-- MOVIE -->\n  <section class="events" id="movie".*?</section>\n',
    '\n', content, flags=re.DOTALL
)

# デスクトップナビからムービー・フォトギャラリーリンクを削除
content = re.sub(r'\s*<a href="#movie"[^>]*>ムービー</a>', '', content)
content = re.sub(r'\s*<a href="gallery/gallery\.html"[^>]*>フォトギャラリー</a>', '', content)

# モバイルメニューからも削除
content = re.sub(r'\s*<a href="#movie" onclick="toggleMenu\(\)">ムービー</a>', '', content)
content = re.sub(r'\s*<a href="gallery/gallery\.html" onclick="toggleMenu\(\)">フォトギャラリー</a>', '', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('index.html updated')

# ============================================================
# 2. 全サブページのナビからムービー・フォトギャラリーを削除
# ============================================================
html_files = (
    glob.glob('news/*.html') +
    glob.glob('touring/*.html') +
    glob.glob('touring/archive/*.html') +
    glob.glob('touring/report/*.html')
)

for filepath in html_files:
    with open(filepath, encoding='utf-8') as f:
        c = f.read()
    original = c

    # デスクトップナビ・モバイルメニューから削除
    c = re.sub(r'\s*<a href="[^"]*#movie"[^>]*>ムービー</a>', '', c)
    c = re.sub(r'\s*<a href="[^"]*movie/movie\.html"[^>]*>ムービー</a>', '', c)
    c = re.sub(r'\s*<a href="[^"]*gallery/gallery\.html"[^>]*>フォトギャラリー</a>', '', c)
    # モバイルメニュー版（onclick付き）
    c = re.sub(r'\s*<a href="[^"]*#movie" onclick="toggleMenu\(\)">ムービー</a>', '', c)
    c = re.sub(r'\s*<a href="[^"]*gallery/gallery\.html" onclick="toggleMenu\(\)">フォトギャラリー</a>', '', c)

    if c != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'Updated: {filepath}')

print(f'Total files processed: {len(html_files)}')

# ============================================================
# 3. gallery/gallery.html を削除
# ============================================================
gallery_path = 'gallery/gallery.html'
if os.path.exists(gallery_path):
    os.remove(gallery_path)
    print(f'Deleted: {gallery_path}')
