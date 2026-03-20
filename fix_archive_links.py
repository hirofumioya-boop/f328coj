import re, os

base = r"H:\マイドライブ\Claude Code\ferrari-redesign"
old_url1 = "https://f328coj.jp/124841254012522125311246412524125091254012488.html"
old_url2 = "https://f328coj.jp/1248412540125221253112464125241250912540124881.html"

# archive-2024.html: title -> new file
map_2024 = {
    "年次総会兼ミニツーリング": "report-2024-miura.html",
    "山中湖ツーリング": "report-2024-yamanakako.html",
    "舞浜ツーリング": "report-2024-maihama.html",
    "軽井沢ツーリング": "report-2024-karuizawa.html",
    "横須賀ツーリング": "report-2024-yokosuka.html",
    "328DAY・10周年記念ツーリング": "report-2024-328day.html",
    "九十九里ツーリング": "report-2024-kujukuri.html",
}
map_2023 = {
    "ABARTHコラボツーリング": "report-2023-abarth.html",
    "湾岸ツーリング": "report-2023-wangan.html",
    "山梨ツーリング": "report-2023-yamanashi.html",
    "軽井沢ツーリング": "report-2023-karuizawa.html",
    "三浦半島ツーリング": "report-2023-miura.html",
    "328DAYツーリング": "report-2023-328day.html",
    "千葉ツーリング": "report-2023-chiba.html",
}
map_2022 = {
    "前橋ツーリング": "report-2022-maebashi.html",
    "大乗フェラーリミーティング参加": "report-2022-daijo.html",
    "箱根ツーリング": "report-2022-hakone.html",
    "軽井沢ツーリング": "report-2022-karuizawa.html",
    "神奈川ツーリング": "report-2022-kanagawa.html",
    "328DAYツーリング": "report-2022-328day.html",
}
map_2021 = {
    "埼玉ツーリング": "report-2021-saitama.html",
    "箱根ツーリング": "report-2021-hakone.html",
    "328DAYツーリング": "report-2021-328day.html",
}
map_2020 = {
    "大磯ツーリング / 大乗フェラーリミーティング2020": "report-2020-oiso.html",
    "お台場ツーリング": "report-2020-odaiba.html",
    "山中湖ツーリング": "report-2020-yamanakako.html",
    "小田原ツーリング": "report-2020-odawara.html",
}
map_2019 = {
    "総会・クリスマスパーティー": "report-2019-party.html",
    "箱根ツーリング": "report-2019-hakone.html",
    "群馬ツーリング": "report-2019-gunma.html",
    "山梨ツーリング": "report-2019-yamanashi.html",
    "軽井沢一泊ツーリング": "report-2019-karuizawa.html",
    "サーキットの狼ミュージアムツーリング": "report-2019-scw.html",
    "328DAY御殿場ツーリング": "report-2019-328day.html",
    "横須賀ツーリング": "report-2019-yokosuka.html",
}

archives = [
    ("archive-2024.html", map_2024),
    ("archive-2023.html", map_2023),
    ("archive-2022.html", map_2022),
    ("archive-2021.html", map_2021),
    ("archive-2020.html", map_2020),
    ("archive-2019.html", map_2019),
]

for filename, mapping in archives:
    filepath = os.path.join(base, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    count = 0
    for title, new_href in mapping.items():
        # Find card containing this title and replace its old link
        pattern = (
            r'(<h3[^>]*class="card-title"[^>]*>' + re.escape(title) + r'</h3>.*?)'
            r'<a[^>]*class="card-link"[^>]*href="https://f328coj\.jp/[^"]*"[^>]*>([^<]*)</a>'
        )
        replacement = r'\1<a class="card-link" href="' + new_href + r'">\2</a>'
        new_content, n = re.subn(pattern, replacement, content, count=1, flags=re.DOTALL)
        if n > 0:
            content = new_content
            count += 1
            print(f"OK [{filename}] {title[:25]} -> {new_href}")
        else:
            print(f"NG [{filename}] {title[:25]}")

    remaining = content.count("f328coj.jp")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  -> {filename}: {count} replaced, {remaining} old URLs remain\n")

print("Done.")
