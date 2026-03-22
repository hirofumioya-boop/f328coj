"""デザイン一貫性の修正スクリプト"""

# ============================================================
# style.css の修正
# ============================================================
with open('style.css', encoding='utf-8') as f:
    css = f.read()

# 1. page-hero-title の line-height を 1.2 に統一
css = css.replace(
    'font-weight: 700; line-height: 1.1;\n  margin-bottom: 16px;\n}',
    'font-weight: 700; line-height: 1.2;\n  margin-bottom: 16px;\n}'
)

# 2. #schedule の背景色を CSS に追加
if '#schedule {' not in css:
    css = css.replace(
        '.contact {\n  background: var(--dark);',
        '#schedule { background: var(--dark2); }\n.links-section { background: var(--dark2); }\n\n.contact {\n  background: var(--dark);'
    )

# 3. .contact に padding-top: 60px を追加
css = css.replace(
    '.contact {\n  background: var(--dark);\n  padding-bottom: 0;\n}',
    '.contact {\n  background: var(--dark);\n  padding-top: 60px;\n  padding-bottom: 0;\n}'
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('style.css updated')

# ============================================================
# index.html の修正
# ============================================================
with open('index.html', encoding='utf-8') as f:
    html = f.read()

# 1. デスクトップナビのツーリングレポートリンク修正
html = html.replace(
    '<li><a href="#events">ツーリングレポート</a></li>',
    '<li><a href="touring/touring.html">ツーリングレポート</a></li>'
)

# 2. モバイルメニューのツーリングレポートリンク修正
html = html.replace(
    '<a href="#events" onclick="toggleMenu()">ツーリングレポート</a>',
    '<a href="touring/touring.html" onclick="toggleMenu()">ツーリングレポート</a>'
)

# 3. schedule-intro のインライン text-align を削除（style.css で管理）
html = html.replace(
    '<p class="schedule-intro" style="text-align:left;">',
    '<p class="schedule-intro">'
)

# 4. schedule セクションのインライン背景色を削除（style.css に移動）
html = html.replace(
    '<section id="schedule" style="background: var(--dark2);">',
    '<section id="schedule">'
)

# 5. links セクションのインライン背景色を削除（style.css に移動）
html = html.replace(
    '<section class="links-section" id="links" style="background: var(--dark2);">',
    '<section class="links-section" id="links">'
)

# 6. contact セクションのインラインパディングを削除（style.css に移動）
html = html.replace(
    '<section class="contact" id="contact" style="padding-bottom:0; padding-top:60px;">',
    '<section class="contact" id="contact">'
)

# 7. btn-primary の重複インラインスタイルを削除
html = html.replace(
    '<button type="submit" class="btn-primary" style="border:none; cursor:pointer; font-family:\'Montserrat\',sans-serif;">',
    '<button type="submit" class="btn-primary">'
)

# 8. 「入会要件」ラベルの色を白→赤に変更
html = html.replace(
    '<p style="font-size:14px; font-weight:700; color:var(--white); letter-spacing:2px; margin-bottom:12px;">入会要件</p>',
    '<p style="font-size:14px; font-weight:700; color:var(--red); letter-spacing:2px; margin-bottom:12px;">入会要件</p>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html updated')
print('All done!')
