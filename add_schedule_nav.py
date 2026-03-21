import os
import re

BASE = r"H:\マイドライブ\Claude Code\ferrari-redesign"

# ナビに追加するパターン（サブページ用）
# 更新情報の次にイベントスケジュールを挿入

def process_file(filepath, schedule_href):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # すでにイベントスケジュールがある場合はスキップ
    if 'イベントスケジュール' in content:
        print(f"SKIP (already exists): {filepath}")
        return

    # PC nav: 更新情報の次の行にイベントスケジュールを挿入
    # パターン: 更新情報のli要素の後
    old_touring = f'<li><a href="{schedule_href.replace("schedule", "").replace("#", "").replace("index.html", "../index.html")}更新情報'

    # 更新情報リンクを探す（news.html or ../news/news.html）
    # PCナビ用
    pc_pattern = re.compile(
        r'(<li><a href="[^"]*"[^>]*>更新情報</a></li>)\s*\n(\s*<li><a href="[^"]*"[^>]*>ツーリングレポート</a></li>)'
    )

    def pc_replace(m):
        indent = re.match(r'\s*', m.group(2)).group()
        return f'{m.group(1)}\n{indent}<li><a href="{schedule_href}">イベントスケジュール</a></li>\n{m.group(2)}'

    new_content = pc_pattern.sub(pc_replace, content)

    # モバイルメニュー用
    mobile_pattern = re.compile(
        r'(<a href="[^"]*"[^>]*onclick="toggleMenu\(\)"[^>]*>更新情報</a>)\s*\n(\s*<a href="[^"]*"[^>]*onclick="toggleMenu\(\)"[^>]*>ツーリングレポート</a>)'
    )

    def mobile_replace(m):
        indent = re.match(r'\s*', m.group(2)).group()
        return f'{m.group(1)}\n{indent}<a href="{schedule_href}" onclick="toggleMenu()">イベントスケジュール</a>\n{m.group(2)}'

    new_content = mobile_pattern.sub(mobile_replace, new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"UPDATED: {filepath}")
    else:
        print(f"NO MATCH: {filepath}")

# news/news.html (same level as touring/ gallery/)
process_file(os.path.join(BASE, 'news', 'news.html'), '../index.html#schedule')

# gallery/gallery.html
process_file(os.path.join(BASE, 'gallery', 'gallery.html'), '../index.html#schedule')

# touring/touring.html
process_file(os.path.join(BASE, 'touring', 'touring.html'), '../index.html#schedule')

# touring/archive/*.html
archive_dir = os.path.join(BASE, 'touring', 'archive')
for fname in os.listdir(archive_dir):
    if fname.endswith('.html'):
        process_file(os.path.join(archive_dir, fname), '../../index.html#schedule')

# touring/report/*.html
report_dir = os.path.join(BASE, 'touring', 'report')
for fname in os.listdir(report_dir):
    if fname.endswith('.html'):
        process_file(os.path.join(report_dir, fname), '../../index.html#schedule')

print("\nDone!")
