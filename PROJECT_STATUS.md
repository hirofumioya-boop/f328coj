# F328 Club of Japan — サイトリデザイン プロジェクト状況

最終更新: 2026-03-20

---

## 公開URL
- **Vercel（プレビュー）**: https://f328coj.vercel.app
- **GitHub リポジトリ**: https://github.com/hirofumioya-boop/f328coj
- **本番ドメイン（旧サイト）**: https://f328coj.jp（Weeblyホスト）

---

## ファイル構成

```
ferrari-redesign/
├── index.html              # トップページ（全コンテンツ含む）
├── style.css               # 共通スタイルシート
├── hero.jpg                # トップページヒーロー画像
├── images/                 # 全画像（180枚以上）
├── news/
│   └── news.html           # 更新情報ページ（別ページ）
├── gallery/
│   └── gallery.html        # フォトギャラリーページ（別ページ）
├── touring/
│   ├── touring.html        # ツーリングレポート一覧（別ページ）
│   ├── archive/
│   │   ├── 2018.html〜2024.html  # 年別アーカイブ（7ファイル）
│   └── report/
│       └── *.html          # 個別レポート（63ファイル: 2017〜2026）
```

**ページ設計方針：**
- コンテンツが増え続けるもの（ツーリングレポート・フォトギャラリー・更新情報）→ 別ページ
- 量が少なく増減が少ないもの（リンク・ムービー・入会・お問合せ）→ トップページ内セクション

---

## ページ構成と主な内容

### index.html（トップページ）
- ヒーロー画像: `hero.jpg`（オーバーレイなし・素の写真）
- ナビ: ホーム / 当クラブについて / 更新情報 / ツーリングレポート / フォトギャラリー / ムービー / リンク / 入会について / お問合せ
- セクション:
  - **当クラブについて**: クラブ紹介・歴史
  - **ツーリングレポート**: 最新イベントカード6件（各レポートページへリンク）
  - **フォトギャラリー**: アルバムサムネイル（各ギャラリーページへリンク）
  - **ムービー**: YouTube動画7本（iframe埋め込み）
  - **リンク**: SNS・関連サイトへのリンク（準備中）
  - **入会について**: 入会条件・年会費・特典
  - **お問合せ**: コンタクトフォーム（現在はaction="#"で送信不可）
- フッター: copyright + 免責事項のみ

### touring/touring.html（ツーリングレポート一覧）
- 2017〜2026年の全イベントを年別カードで一覧表示
- 各カードから個別レポートページへリンク

### touring/archive/YYYY.html（年別アーカイブ）
- 2018〜2024の7ページ

### touring/report/YYYY-name.html（個別レポート）
- 63ページ（2017〜2026）
- 2019〜2024: 実写真グリッド表示
- 2017〜2018, 2025〜2026: 写真あり（一部）

### news/news.html（更新情報）
- クラブからのお知らせ・コンテンツ更新情報を掲載
- 記事ごとに日付・タグ・タイトル・本文・リンクを設定可能
- `<a class="news-link" href="リンク先">テキスト →</a>` でリンクを追加
- ファイル内にコピー用テンプレートコメントあり

### gallery/gallery.html（フォトギャラリー）
- ツーリング写真アルバム一覧

---

## デザイン仕様

| 項目 | 内容 |
|---|---|
| フォント | Montserrat（本文）+ Playfair Display（見出し） |
| メインカラー | Red `#cc0000` / Gold `#b8960c` / Dark `#0a0a0a` |
| CSS変数 | `--red`, `--gold`, `--dark`, `--dark2`, `--white`, `--text-muted` |
| レイアウト | 純粋なHTML/CSS（フレームワークなし） |
| レスポンシブ | あり（ハンバーガーメニュー対応） |

---

## ナビゲーション構成（全ページ共通）

**トップバー（左→右）:**
ホーム / 当クラブについて / 更新情報 / ツーリングレポート / フォトギャラリー / ムービー / リンク / 入会について / お問合せ

**左上ロゴ:**
`F328 CLUB OF JAPAN`（白・太字・letter-spacing）

**リンク先:**
- トップページ（index.html）: `#` アンカーリンクで各セクションへ
- サブページ: `../index.html`, `../index.html#movie` 等の相対パス

---

## フッター構成（全ページ共通）

```
© 2026 F328 Club of Japan. F328COJ. All Rights Reserved.
免責事項 / Disclaimer  Ferrari is a registered trademark of Ferrari N.V. ...
```

- フッターロゴ・ナビリンクは削除済み
- CSSパディング: `footer { padding: 20px 5% 20px }`

---

## お問合せフォーム

- 現状: `action="#" onsubmit="return false;"` → 送信不可
- テスト用メールアドレス: `hirofumioya@gmail.com`
- 本番用メールアドレス: `ferrari328clubofjapan@yahoo.co.jp`
- **課題**: 静的HTMLのため直接メール送信不可。Weeblyに移行後はWeebly組み込みフォームを使用予定

---

## ⚠️ CSS修正時の重要ルール

**index.htmlには独自のインラインCSS（`<style>`タグ内）があるため、style.cssを変更しただけではindex.htmlに反映されない。**

スタイルを変更する際は必ず以下の4ファイルをセットで確認・修正すること：

1. `style.css`
2. `index.html`（インラインCSS）
3. `touring/touring.html`（インラインCSS）
4. `gallery/gallery.html`（インラインCSS）

修正後は必ず全ファイルで変更が反映されているか確認してからpushする。

---

## ⚠️ モバイルメニュー（ハンバーガー）の重要ルール

モバイルメニューはPC版ナビと**完全に同じ項目・同じ順番**でなければならない。

**現在の正しい順番（index.html）:**
```html
<a href="#" onclick="toggleMenu()">ホーム</a>
<a href="#about" onclick="toggleMenu()">当クラブについて</a>
<a href="news/news.html" onclick="toggleMenu()">更新情報</a>
<a href="#events" onclick="toggleMenu()">ツーリングレポート</a>
<a href="#gallery" onclick="toggleMenu()">フォトギャラリー</a>
<a href="#movie" onclick="toggleMenu()">ムービー</a>
<a href="index.html#links" onclick="toggleMenu()">リンク</a>
<a href="#membership" onclick="toggleMenu()">入会について</a>
<a href="#contact" onclick="toggleMenu()">お問合せ</a>
```

**過去の失敗例と原因:**
- 「About」という英語表記が残っていた（コピペ元が古いバージョン）
- 「ホーム」「当クラブについて」「更新情報」が抜けていた
- 「ホーム」と「お問合せ」が画面外に切れて見えなかった
  → 原因: 9項目が縦に並ぶと画面高さを超えるのに `justify-content: center` のせいで上下がはみ出していた
  → 修正: `justify-content: flex-start` + `overflow-y: auto` + `padding: 32px 0`

ナビを変更するときは必ずPC版・モバイル版の両方を同時に修正すること。

---

## 運用・管理方針

| 役割 | 担当 |
|---|---|
| コンテンツ作成・修正（HTML編集） | あなた（ボランティア） |
| GitHub push / Vercel管理 | 検討中（管理者または継続担当者） |
| ドメイン管理（f328coj.jp） | クラブサイト管理者（Weebly） |

**将来の移行計画:**
1. Vercelプレビューでメンバーレビュー（現在進行中）
2. フィードバック反映・修正完了
3. Weeblyの `f328coj.jp` DNSをVercelに向ける
4. Weeblyのコンタクトフォームのコードをindex.htmlに組み込む
5. 本番公開

---

## 既知の課題・TODO

- [ ] コンタクトフォームの送信機能（Weebly移行後に解決）
- [ ] ムービーセクションのYouTube（localhostでは表示されないがVercel上では正常）
- [ ] フォトギャラリーのホバーエフェクト削除（ライトボックス未実装のため）
- [ ] 2025〜2026レポートページの写真追加（写真入手次第）
- [ ] リンクセクションのSNS・関連サイトURL追加（URL確定次第）

---

## 除外・削除済み項目

- `movie/movie.html`: 削除済み（トップページのムービーセクションに統合）
- `restore/`: 削除済み（コンテンツ不要のため）
- `links/links.html`: 削除済み（トップページの#linksセクションに統合）
- フッターのナビリンク: 削除済み
- フッターのロゴ・クラブ説明文: 削除済み
- 「会員専用ページ」「レストア情報」「イベントスケジュール」リンク: 削除済み
- 「すべてのアルバムは元サイトでご覧いただけます」: 削除済み
- f328coj.jpへの外部リンク: 全削除済み
- 統計バッジ（2014設立年/328/10+イベント/¥6K年会費）: 削除済み
- 赤丸Fロゴ: 削除済み（「F328 CLUB OF JAPAN」テキストに置き換え）

---

## 過去に踏んだ地雷・トラブル事例集

### 1. style.cssを直してもトップページに反映されない
- **原因**: index.htmlに独自のインラインCSS（`<style>`タグ）があり、外部CSSより優先される
- **教訓**: style.cssとindex.htmlのインラインCSSは必ず両方修正する

### 2. モバイルメニューの項目が上下で切れて見えない
- **原因**: 項目が9個に増えて画面高さを超えたが `justify-content: center` で中央揃えのため上下がはみ出す。スクロールも不可
- **修正**: `justify-content: flex-start` + `overflow-y: auto` + `padding: 32px 0`
- **教訓**: メニュー項目が増えたら画面に収まるか必ずスマホで確認する

### 3. モバイルメニューとPC版ナビの内容が不一致
- **原因**: ナビに項目を追加するとき、PC版（`<ul class="nav-links">`）だけ更新してモバイル版（`<div class="mobile-menu">`）を更新し忘れた
- **教訓**: ナビ変更は必ずPC版・モバイル版の両方を同時に修正する

### 4. 「更新情報」がナビに2回表示された
- **原因**: ナビ項目追加時のコピペミスで同じ行が重複した
- **教訓**: ナビ修正後は必ずHTML上で重複がないか確認する

### 5. サブページのpage-hero-tagの文字が細くて小さい
- **原因**: style.cssの `.page-hero-tag` が `font-size: 10px`・font-weight未設定のまま
- **修正**: `font-size: 12px; font-weight: 700;` に変更
- **教訓**: トップページの `.section-tag` とサブページの `.page-hero-tag` は同じ見た目にする

### 6. Pythonスクリプトのバックスラッシュエスケープエラー
- **原因**: コマンドライン上でPythonをインラインで実行する際のエスケープ問題
- **修正**: `.py` ファイルに書き出してから実行する

### 7. フッター上部のスペースが広い
- **原因**: index.htmlのインラインCSSに `footer { padding: 64px 5% 32px; }` が残存していた
- **修正**: `padding: 20px 5% 20px;` に変更（style.cssと同じ値）

---

## 免責事項テキスト（フッター）

```
免責事項 / Disclaimer　Ferrari is a registered trademark of Ferrari N.V.
This site is a private fan club and is not affiliated with Ferrari N.V.
（和訳：FerrariはFerrari N.V.の登録商標です。当サイトは個人のファンクラブであり、
Ferrari N.V.社とは一切関係ありません。）
```
