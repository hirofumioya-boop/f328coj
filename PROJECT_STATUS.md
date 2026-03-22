# F328 Club of Japan — サイトリデザイン プロジェクト状況

最終更新: 2026-03-22（本番公開・Google Search Console登録完了）

---

## 公開URL

- **本番サイト**: https://f328coj.jp ✅ 稼働中
- **Vercel（プレビュー）**: https://f328coj.vercel.app
- **GitHub リポジトリ**: https://github.com/hirofumioya-boop/f328coj

---

## インフラ構成

| 役割 | サービス | 費用 |
|---|---|---|
| ドメイン管理 | お名前ドットコム（f328coj.jp） | 更新料のみ（2028年7月31日まで） |
| コード管理 | GitHub | 無料 |
| ホスティング | Vercel | 無料 |
| コンタクトフォーム | Web3Forms | 無料 |
| SEO管理 | Google Search Console | 無料 |

**DNSの向き先**: お名前ドットコム → Vercel（AレコードとCNAMEレコード設定済み）

---

## ファイル構成

```
ferrari-redesign/
├── index.html              # トップページ（全コンテンツ含む）
├── style.css               # 共通スタイルシート（全ページ共通）
├── hero.jpg                # トップページヒーロー画像
├── news-data.js            # 更新情報データ（ここだけ編集すれば更新情報が自動反映）
├── sitemap.xml             # Google Search Console用サイトマップ
├── images/                 # 全画像（180枚以上）
├── news/
│   └── news.html           # 更新情報ページ
├── touring/
│   ├── touring.html        # ツーリングレポート一覧
│   ├── archive/
│   │   └── 2018.html〜2024.html  # 年別アーカイブ（7ファイル）
│   └── report/
│       └── *.html          # 個別レポート（60ファイル: 2017〜2026）
└── _backup_deleted_content/ # 削除済みコンテンツのバックアップ（Git管理外）
```

**ページ設計方針：**
- コンテンツが増え続けるもの（ツーリングレポート・更新情報）→ 別ページ
- 量が少ないもの（入会・お問合せ・イベントスケジュール）→ トップページ内セクション
- 将来コンテンツが増えたら別ページ化（リンク・ムービー等）

---

## ページ構成と主な内容

### index.html（トップページ）

- ヒーロー画像: `hero.jpg`（オーバーレイなし・素の写真）
- ナビ: ホーム / 当クラブについて / 更新情報 / イベントスケジュール / ツーリングレポート / 入会について / お問合せ
- セクション:
  - **当クラブについて (ABOUT US)**: クラブ紹介・歴史・特徴
  - **更新情報**: 最新5件を表示（news-data.jsから自動生成）→ 更新情報ページへリンク
  - **イベントスケジュール**: 2026年のイベント一覧・体験参加案内
  - **ツーリングレポート**: 最新イベントカード6件 → touring/touring.htmlへリンク
  - **入会について**: 入会条件・入会要件
  - **お問合せ**: コンタクトフォーム（Web3Forms連携済み）
- フッター: copyright + 免責事項のみ

### news/news.html（更新情報）

- 全更新情報を表示（news-data.jsから自動生成）
- **更新情報の追加方法**: `news-data.js` の `NEWS_ITEMS` 配列の先頭に追加 → GitHubにpush

### touring/touring.html（ツーリングレポート一覧）

- 2017〜2026年の全イベントを年別カードで一覧表示

### touring/archive/YYYY.html（年別アーカイブ）

- 2018〜2024の7ページ

### touring/report/YYYY-name.html（個別レポート）

- 60ページ（2017〜2026）

---

## ナビゲーション構成（全ページ共通）

**デスクトップナビ（左→右）:**
ホーム / 当クラブについて / 更新情報 / イベントスケジュール / ツーリングレポート / 入会について / お問合せ

**左上ロゴ:** `F328 CLUB OF JAPAN`（白・太字・letter-spacing）

**リンク先（index.html）:**
- ホーム: `index.html`
- 当クラブについて: `#about`
- 更新情報: `#news`
- イベントスケジュール: `#schedule`
- ツーリングレポート: `touring/touring.html`（別ページ）
- 入会について: `#membership`
- お問合せ: `#contact`

⚠️ ナビを変更するときは必ずPC版・モバイル版の両方を同時に修正すること。

---

## CSS管理方針

**style.cssで一元管理。** index.htmlにインラインCSSなし。

- `style.css` → 全ページ共通スタイルを管理
- `news/news.html` / `touring/touring.html` → ページ固有の小さなインラインCSSあり（nav-logo-simple等）
- 共通スタイル（nav・footer・page-hero・section等）は `style.css` のみ修正すれば全ページに反映

---

## お問合せフォーム

- **サービス**: Web3Forms（無料）
- **Access Key**: `4a527da4-05ef-44ff-9161-86f805d81879`
- **送信先メール**: `hirofumioya@gmail.com`（暫定）
- **本番用メール**: `ferrari328clubofjapan@yahoo.co.jp`（確定次第変更）
- **メール変更方法**: web3forms.comで新メールアドレスのAccess Keyを取得 → index.htmlのhidden inputを更新

---

## SEO設定

- **index.html**: title・description・keywords設定済み
- **news/news.html**: title・description・keywords設定済み
- **touring/touring.html**: title・description・keywords設定済み
- **Google Search Console**: 登録済み・所有権確認済み・サイトマップ送信済み
- **sitemap.xml**: 全ページ（70ページ超）を含む

**主なSEOキーワード:** フェラーリ328 / Ferrari 328 / F328 / F328COJ / F328クラブオブジャパン / フェラーリクラブ / Ferrari club Japan

---

## セキュリティ設定

- **GitHub**: SMS二段階認証（2FA）設定済み
- **Vercel**: Passkey二段階認証（2FA）設定済み
- **リカバリーコード**: GoogleドライブにPDF保存済み

---

## デザイン仕様

| 項目 | 内容 |
|---|---|
| フォント | Montserrat（本文）+ Playfair Display（見出し） |
| メインカラー | Red `#cc0000` / Dark `#0a0a0a` |
| CSS変数 | `--red`, `--dark`, `--dark2`, `--white`, `--text-muted` |
| レイアウト | 純粋なHTML/CSS（フレームワークなし） |
| レスポンシブ | あり（ハンバーガーメニュー対応） |
| section-tag | `font-size: 12px; font-weight: 700; color: var(--red);` |
| page-hero-tag | `font-size: 12px; font-weight: 700; color: var(--red);`（section-tagと統一） |

---

## フッター構成（全ページ共通）

```
© 2026 F328 Club of Japan. F328COJ. All Rights Reserved.
免責事項 / Disclaimer  Ferrari is a registered trademark of Ferrari N.V.
This site is a private fan club and is not affiliated with Ferrari N.V.
```

---

## 削除済みコンテンツ

- `gallery/gallery.html`: 削除済み（バックアップあり）
- ムービーセクション: 削除済み（バックアップあり）
- フォトギャラリーセクション: 削除済み（バックアップあり）
- `restore/`: 削除済み
- `links/links.html`: 削除済み（リンクセクションはトップページから一時非表示中）
- フッターのナビリンク・ロゴ: 削除済み
- 赤丸Fロゴ: 削除済み（「F328 CLUB OF JAPAN」テキストに置き換え）
- 統計バッジ（設立年/会員数等）: 削除済み

---

## TODO（残課題）

- [ ] リンクセクションのURL追加（URL確定次第）
- [ ] 2025〜2026レポートページの写真追加（写真入手次第）
- [ ] 旧ホスティング（WordPress）の解約確認（管理者確認中）
- [ ] お問合せ先メールを本番用（ferrari328clubofjapan@yahoo.co.jp）に変更

---

## 過去に踏んだ地雷・トラブル事例集

### 1. style.cssを直してもトップページに反映されない
- **原因**: index.htmlに独自のインラインCSSがあり外部CSSより優先される
- **修正**: index.htmlの`<style>`タグを完全削除し style.css に統合済み（2026-03-20）
- **教訓**: インラインCSSはできる限り外部CSSに統合して一元管理する

### 2. モバイルメニューの項目が上下で切れて見えない
- **原因**: 項目が増えて画面高さを超えたが `justify-content: center` で上下がはみ出す
- **修正**: `justify-content: flex-start` + `overflow-y: auto` + `padding: 32px 0`
- **教訓**: メニュー項目が増えたら必ずスマホで確認する

### 3. ナビにフォトギャラリー・ムービーリンクが残存
- **原因**: スクリプトが `href="#gallery"` パターンを見落とし
- **教訓**: 削除後は全ページをgrepで確認する

### 4. 空の`<li></li>`がナビに残りスペースが生じる
- **原因**: ナビ項目削除スクリプトがli要素だけ削除してもli自体が空で残存
- **修正**: `re.sub(r'\s*<li></li>', '', c)` で全ページ一括削除

### 5. サブページのpage-hero-titleが左寄り
- **原因**: レポートページに`page-hero-inner`ラッパーがなく、`.page-hero`に`text-align:center`が未設定
- **修正**: `.page-hero { text-align: center; }` を追加

### 6. Pythonスクリプトのバックスラッシュエスケープエラー
- **原因**: コマンドライン上でPythonをインラインで実行する際のエスケープ問題
- **修正**: `.py` ファイルに書き出してから実行する

---

## 免責事項テキスト（フッター）

```
Ferrari is a registered trademark of Ferrari N.V.
This site is a private fan club and is not affiliated with Ferrari N.V.
（FerrariはFerrari N.V.の登録商標です。当サイトは個人のファンクラブであり、Ferrari N.V.社とは一切関係ありません。）
```
