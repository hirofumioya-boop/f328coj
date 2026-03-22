"""SEO meta tags 最適化スクリプト"""
import glob, re

# ============================================================
# index.html
# ============================================================
with open('index.html', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<title>F328 Club of Japan</title>',
    '<title>F328 Club of Japan | フェラーリ328（Ferrari 328）クラブ・日本</title>'
)
html = html.replace(
    '<meta name="description" content="F328 Club of Japan（F328COJ）は、フェラーリ328を愛するオーナー・愛好家のクラブです。定期ツーリング、フォトギャラリー、ムービーなど活動情報を発信しています。" />',
    '<meta name="description" content="F328 Club of Japan（F328COJ）は、フェラーリ328（Ferrari 328）を愛するオーナー・愛好家のクラブです。2014年設立。定期ツーリングイベントや会員コミュニティの情報を発信しています。" />\n  <meta name="keywords" content="フェラーリ328, Ferrari 328, F328, F328COJ, F328クラブオブジャパン, フェラーリクラブ, フェラーリオーナーズクラブ, Ferrari club Japan" />'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html updated')

# ============================================================
# news/news.html
# ============================================================
with open('news/news.html', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<title>更新情報 | F328 Club of Japan</title>',
    '<title>更新情報 | F328 Club of Japan | フェラーリ328クラブ</title>'
)
html = html.replace(
    '<meta name="description" content="F328 Club of Japanからの最新情報・お知らせ。ツーリングレポートの追加やイベント情報をお届けします。" />',
    '<meta name="description" content="F328 Club of Japan（フェラーリ328クラブ）からの最新情報・お知らせ。ツーリングレポートの追加やイベント情報をお届けします。" />\n  <meta name="keywords" content="フェラーリ328, Ferrari 328, F328COJ, フェラーリクラブ, ツーリング, イベント" />'
)

with open('news/news.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('news/news.html updated')

# ============================================================
# touring/touring.html
# ============================================================
with open('touring/touring.html', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<title>ツーリングレポート | F328 Club of Japan</title>',
    '<title>ツーリングレポート | F328 Club of Japan | フェラーリ328クラブ</title>'
)
html = html.replace(
    '<meta name="description" content="F328 Club of Japanのツーリングレポート一覧。フェラーリ328で走った全国各地のドライブ記録をご覧いただけます。" />',
    '<meta name="description" content="F328 Club of Japan（フェラーリ328クラブ）のツーリングレポート一覧。Ferrari 328で走った全国各地のドライブ記録をご覧いただけます。" />\n  <meta name="keywords" content="フェラーリ328, Ferrari 328, F328, ツーリングレポート, ドライブ, フェラーリクラブ" />'
)

with open('touring/touring.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('touring/touring.html updated')

print('\nAll SEO meta tags updated!')
