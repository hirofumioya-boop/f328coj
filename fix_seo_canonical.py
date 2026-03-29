"""
SEO修正スクリプト
- 全ページにcanonicalタグ追加
- レポート・アーカイブページにmeta description追加
- robots.txt作成
"""

import os
import re

BASE_URL = "https://f328coj.jp"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ページごとのURL・description定義
PAGES = [
    {
        "path": "index.html",
        "url": f"{BASE_URL}/",
        "description": None,  # 既に存在するのでスキップ
    },
    {
        "path": "news/news.html",
        "url": f"{BASE_URL}/news/news.html",
        "description": None,  # 既に存在するのでスキップ
    },
    {
        "path": "touring/touring.html",
        "url": f"{BASE_URL}/touring/touring.html",
        "description": "F328 Club of Japanのツーリングレポート一覧。フェラーリ328オーナーによる各地へのドライブ記録をご覧いただけます。",
    },
]

# アーカイブページ
for year in range(2018, 2025):
    PAGES.append({
        "path": f"touring/archive/{year}.html",
        "url": f"{BASE_URL}/touring/archive/{year}.html",
        "description": f"{year}年のF328 Club of Japanツーリング記録一覧。フェラーリ328による{year}年の各ツーリングレポートをまとめています。",
    })

# レポートページ（reportフォルダを走査）
report_dir = os.path.join(BASE_DIR, "touring", "report")
for fname in sorted(os.listdir(report_dir)):
    if not fname.endswith(".html"):
        continue
    PAGES.append({
        "path": f"touring/report/{fname}",
        "url": f"{BASE_URL}/touring/report/{fname}",
        "description": None,  # タイトルから動的生成
    })


def get_title(html):
    m = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
    return m.group(1).strip() if m else ""


def has_tag(html, tag_pattern):
    return bool(re.search(tag_pattern, html, re.IGNORECASE))


def insert_after_viewport(html, tags_to_insert):
    """viewportメタタグの直後に挿入"""
    pattern = r'(<meta\s+name=["\']viewport["\'][^>]*>)'
    replacement = r'\1\n' + tags_to_insert
    return re.sub(pattern, replacement, html, count=1, flags=re.IGNORECASE)


def process_file(page):
    filepath = os.path.join(BASE_DIR, page["path"])
    if not os.path.exists(filepath):
        print(f"  SKIP (not found): {page['path']}")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    tags_to_insert = ""

    # canonicalタグ（なければ追加）
    if not has_tag(html, r'<link\s+rel=["\']canonical["\']'):
        tags_to_insert += f'  <link rel="canonical" href="{page["url"]}">\n'

    # meta description（なければ追加）
    if not has_tag(html, r'<meta\s+name=["\']description["\']'):
        description = page.get("description")
        if description is None:
            # タイトルから自動生成
            title = get_title(html)
            # "タイトル | F328 Club of Japan" → "タイトル" だけ取り出す
            title_short = title.split("|")[0].strip()
            description = f"{title_short} — F328 Club of Japanのツーリングレポート。フェラーリ328オーナーによるドライブ記録です。"
        tags_to_insert += f'  <meta name="description" content="{description}">\n'

    if not tags_to_insert:
        print(f"  OK (already has tags): {page['path']}")
        return

    new_html = insert_after_viewport(html, tags_to_insert)

    if new_html == html:
        print(f"  WARN (viewport not found, skipping): {page['path']}")
        return

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_html)

    print(f"  FIXED: {page['path']}")


def create_robots_txt():
    robots_path = os.path.join(BASE_DIR, "robots.txt")
    content = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  CREATED: robots.txt")


print("=== SEO修正開始 ===")
for page in PAGES:
    process_file(page)

print("\n=== robots.txt作成 ===")
create_robots_txt()

print("\n=== 完了 ===")
print(f"処理ページ数: {len(PAGES)}")
