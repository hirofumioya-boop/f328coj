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
 * 例: "/touring/touring.html" "/gallery/gallery.html"
 */

const NEWS_ITEMS = [
  {
    date: "2026年3月",
    tag: "サイト",
    title: "ウェブサイトをリニューアルしました",
    body: "F328 Club of Japanの公式ウェブサイトをリニューアルしました。ツーリングレポート、フォトギャラリー、ムービーなどのコンテンツを一新しています。",
    link: { url: "/touring/touring.html", text: "ツーリングレポートを見る →" }
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
