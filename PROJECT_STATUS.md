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
├── gallery/
│   └── gallery.html        # フォトギャラリーページ
├── restore/
│   └── restore.html        # レストアページ
├── touring/
│   ├── touring.html        # ツーリングレポート一覧
│   ├── archive/
│   │   ├── 2018.html〜2024.html  # 年別アーカイブ（7ファイル）
│   └── report/
│       └── *.html          # 個別レポート（63ファイル: 2017〜2026）
```

---

## ページ構成と主な内容

### index.html（トップページ）
- ヒーロー画像: `hero.jpg`（オーバーレイなし・素の写真）
- ナビ: ホーム / Our Story / ツーリングレポート / フォトギャラリー / ムービー / 入会について / お問合せ
- セクション:
  - **Our Story**: クラブ紹介・歴史
  - **ツーリングレポート**: 最新イベントカード6件（各レポートページへリンク）
  - **フォトギャラリー**: アルバムサムネイル（各ギャラリーページへリンク）
  - **ムービー**: YouTube動画7本（iframe埋め込み）
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

### gallery/gallery.html（フォトギャラリー）
- ツーリング写真アルバム一覧

### restore/restore.html（レストア）
- エンジン・ボディ・インテリアの写真グリッド

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
ホーム / Our Story / ツーリングレポート / フォトギャラリー / ムービー / 入会について / お問合せ

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

---

## 除外・削除済み項目

- `movie/movie.html`: 削除済み（トップページのムービーセクションに統合）
- フッターのナビリンク: 削除済み
- フッターのロゴ・クラブ説明文: 削除済み
- 「会員専用ページ」「レストア情報」「イベントスケジュール」リンク: 削除済み
- 「すべてのアルバムは元サイトでご覧いただけます」: 削除済み
- f328coj.jpへの外部リンク: 全削除済み
- 統計バッジ（2014設立年/328/10+イベント/¥6K年会費）: 削除済み

---

## 免責事項テキスト（フッター）

```
免責事項 / Disclaimer　Ferrari is a registered trademark of Ferrari N.V.
This site is a private fan club and is not affiliated with Ferrari N.V.
（和訳：FerrariはFerrari N.V.の登録商標です。当サイトは個人のファンクラブであり、
Ferrari N.V.社とは一切関係ありません。）
```
