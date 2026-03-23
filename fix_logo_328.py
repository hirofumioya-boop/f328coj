import os
import glob

base = r"H:\マイドライブ\Claude Code\ferrari-redesign"
old = '>F328 CLUB OF JAPAN<'
new = '>F<span style="color:var(--red)">328</span> CLUB OF JAPAN<'

files = (
    glob.glob(os.path.join(base, "touring", "archive", "*.html")) +
    glob.glob(os.path.join(base, "touring", "report", "*.html")) +
    [os.path.join(base, "touring", "touring.html"),
     os.path.join(base, "news", "news.html")]
)

count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    if old in content:
        content = content.replace(old, new)
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        count += 1
        print(f"更新: {os.path.basename(f)}")

print(f"\n合計 {count} ファイルを更新しました")
