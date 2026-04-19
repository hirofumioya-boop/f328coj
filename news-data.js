/**
 * 更新情報データ
 *
 * 新しい記事を追加するときは、配列の【先頭】に追加してください。
 * そうすることで、最新記事が常に上に表示されます。
 *
 * tag の種類例: サイト / ツーリング / フォトギャラリー / ムービー / 入会 / お知らせ
 * link は不要な場合は null にしてください。
 *
 * URL は / 始まりのルート相対パスで書いてください。
 * 例: "/touring/report/2026-xxxx.html"
 */

const NEWS_ITEMS = [
  {
    date: "2026年4月",
    tag: "ツーリング",
    title: "大磯ツーリング 2026.04",
    body: "328×7台含む計12台・20名が大磯に集結。ホテル駐車場での撮影会と、海を眺めながらの中華コースランチを楽しみました。",
    link: { url: "/touring/report/2026-oiso.html", text: "レポートを読む →" }
  },
  {
    date: "2026年3月",
    tag: "ツーリング",
    title: "328DAY ツーリング 2026.03",
    body: "芦ノ湖湖畔「山のホテル」へのランチツーリングレポートを公開しました。カウンタックアニバーサリーのお披露目も話題に。",
    link: { url: "/touring/report/2026-328day.html", text: "レポートを読む →" }
  },
  {
    date: "2026年3月",
    tag: "サイト",
    title: "ホームページがリニューアルしました",
    body: "F328 Club of Japanの公式ウェブサイトをリニューアルしました。",
    link: null
  },
  {
    date: "2026年1月",
    tag: "ツーリング",
    title: "外房ツーリング 2026.01",
    body: "外房方面へのツーリングレポートを公開しました。",
    link: { url: "/touring/report/2026-sotobou.html", text: "レポートを読む →" }
  },
  {
    date: "2025年12月",
    tag: "ツーリング",
    title: "年次総会兼三浦ツーリング 2025.12",
    body: "年次総会を兼ねた三浦ツーリングのレポートを公開しました。",
    link: { url: "/touring/report/2025-miura.html", text: "レポートを読む →" }
  },
  {
    date: "2025年10月",
    tag: "ツーリング",
    title: "群馬ツーリング 2025.10",
    body: "群馬方面へのツーリングレポートを公開しました。",
    link: { url: "/touring/report/2025-gunma.html", text: "レポートを読む →" }
  },
  {
    date: "2025年9月",
    tag: "ツーリング",
    title: "舞浜ツーリング 2025.09",
    body: "舞浜方面へのツーリングレポートを公開しました。",
    link: { url: "/touring/report/2025-maihama.html", text: "レポートを読む →" }
  },
  {
    date: "2025年5月",
    tag: "ツーリング",
    title: "軽井沢ツーリング 2025.05",
    body: "軽井沢へのツーリングレポートを公開しました。",
    link: { url: "/touring/report/2025-karuizawa.html", text: "レポートを読む →" }
  },
  {
    date: "2025年4月",
    tag: "ツーリング",
    title: "御殿場ツーリング 2025.04",
    body: "御殿場方面へのツーリングレポートを公開しました。",
    link: { url: "/touring/report/2025-gotemba.html", text: "レポートを読む →" }
  },
  {
    date: "2025年3月",
    tag: "ツーリング",
    title: "328DAYツーリング 2025.03",
    body: "328DAYを記念したツーリングのレポートを公開しました。",
    link: { url: "/touring/report/2025-328day.html", text: "レポートを読む →" }
  },
  {
    date: "2025年1月",
    tag: "ツーリング",
    title: "小田原ツーリング 2025.01",
    body: "小田原方面へのツーリングレポートを公開しました。",
    link: { url: "/touring/report/2025-odawara.html", text: "レポートを読む →" }
  },
  {
    date: "2024年10月",
    tag: "ツーリング",
    title: "山中湖ツーリング 2024.10",
    body: "山中湖方面へのツーリングレポートを公開しました。",
    link: { url: "/touring/report/2024-yamanakako.html", text: "レポートを読む →" }
  },
  {
    date: "2024年4月",
    tag: "ツーリング",
    title: "横須賀ツーリング 2024.04",
    body: "横須賀方面へのツーリングレポートを公開しました。",
    link: { url: "/touring/report/2024-yokosuka.html", text: "レポートを読む →" }
  }
];

/**
 * ニュースリストを描画する関数
 * @param {string} containerId - 描画先要素のid
 * @param {number|null} max - 表示件数の上限。null または省略で全件表示
 */
function renderNews(containerId, max) {
  const container = document.getElementById(containerId);
  if (!container) return;
  const items = (max != null) ? NEWS_ITEMS.slice(0, max) : NEWS_ITEMS;
  if (items.length === 0) {
    container.innerHTML = '<p class="news-empty">現在、更新情報はありません。</p>';
    return;
  }
  container.innerHTML = items.map(item => `
    <div class="news-item">
      <p class="news-date">${item.date}</p>
      <span class="news-tag">${item.tag}</span>
      <h2 class="news-title">${item.title}</h2>
      <p class="news-body">${item.body}</p>
      ${item.link ? `<a class="news-link" href="${item.link.url}">${item.link.text}</a>` : ''}
    </div>
  `).join('');
}
