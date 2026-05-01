以下の手順で今日のDaily Bugleダイジェストを生成してください。

## 手順

1. `data/curated.json` を読み込む（記事は事前にキュレーション済み）
2. 各記事・リポジトリを要約する
3. `template.html` を読み込む
4. テンプレートのプレースホルダーを記事HTMLで置き換えて `output/YYYY-MM-DD.html`（今日の日付）として保存する

## セクション構成（タブ）

| セクション | 内容 |
|---|---|
| AI & ML | HN・r/MachineLearning・r/artificial・r/LocalLLaMA、MIT Tech Review AI |
| Frontend | r/javascript・r/reactjs・r/css・CSS-Tricks・Smashing Magazine |
| Backend | r/golang・r/rust・r/java・r/python、InfoQ・Pragmatic Engineer |
| Cloud & CNCF | r/kubernetes・r/aws・r/docker・r/devops、The New Stack・CNCF Blog |
| OSS & Linux | r/linux・r/opensource・r/programming、GitHub Trending |
| Startups | r/startups・r/technology・TechCrunch |
| Movies | r/movies・r/TrueFilm・r/flicks、Roger Ebert・IndieWire |

## GitHub Trending の表示

`data/github_trending.json` のリポジトリは **OSS & Linux** セクションに「今日のGitHub急上昇」として独立したカードグループで表示する。各カードにはリポジトリ名・説明（日本語訳）・言語・本日のスター数を含める。

## テンプレートの使い方

`template.html` には以下のプレースホルダーがある。これらを**HTMLスニペットのみ**で置き換えること（`<html>` タグや `<style>` タグは不要）。

| プレースホルダー | 置き換え内容 |
|---|---|
| `{{DATE_ISO}}` | `YYYY-MM-DD` 形式の今日の日付（例: `2026-04-30`） |
| `{{DATE_JP}}` | 日本語形式の日付（例: `2026年4月30日（木）`） |
| `{{SECTION_AI}}` | AI & ML タブの中身HTML |
| `{{SECTION_FRONTEND}}` | Frontend タブの中身HTML |
| `{{SECTION_BACKEND}}` | Backend タブの中身HTML |
| `{{SECTION_CLOUD}}` | Cloud & CNCF タブの中身HTML |
| `{{SECTION_OSS}}` | OSS & Linux タブの中身HTML |
| `{{SECTION_STARTUPS}}` | Startups タブの中身HTML |
| `{{SECTION_MOVIES}}` | Movies タブの中身HTML |

## 各セクションのHTML構造

各 `{{SECTION_*}}` プレースホルダーは以下の構造で置き換える：

```html
<p class="section-desc">ソース一覧（例: Hacker News · r/MachineLearning · ...）</p>

<div class="features">
  <!-- フィーチャーカード 1〜2枚 -->
  <div class="card-feature">
    <span class="badge">ソース · 一言タグ</span>
    <h3><a href="URL" target="_blank">タイトル</a></h3>
    <p class="summary">日本語要約（2〜3文）</p>
    <div class="card-meta">
      <span class="source">ソース名</span>
      <span class="score">↑ スコア</span>
      <span class="comments">💬 コメント数</span>
    </div>
  </div>
</div>

<p class="grid-label">その他のトピック</p>
<div class="cards-grid">
  <!-- グリッドカード -->
  <div class="card">
    <h3><a href="URL" target="_blank">タイトル</a></h3>
    <p class="summary">日本語要約（1〜2文）</p>
    <div class="card-meta">
      <span class="source">ソース名</span>
      <span class="score">↑ スコア</span>
      <span class="comments">💬 コメント数</span>
    </div>
  </div>
</div>
```

OSS & Linux セクションのみ、グリッドカードの後に以下を追加：

```html
<div class="trending-section">
  <div class="trending-header"><h2>⭐ 今日のGitHub急上昇</h2></div>
  <div class="trending-grid">
    <div class="trending-card">
      <div class="repo-name"><a href="URL" target="_blank">owner/repo</a></div>
      <div class="repo-desc">日本語説明</div>
      <div class="repo-meta">
        <span class="lang">言語</span>
        <span class="stars-today">★ 本日のスター数</span>
      </div>
    </div>
  </div>
</div>
```

## 出力

- ファイル名: `output/YYYY-MM-DD.html`（今日の日付、例: `output/2026-04-30.html`）
- `output/index.html` は**更新しない**

## キュレーション基準

- スコア・コメント数・話題性を重視
- セクションをまたいで重複する記事は最も関連するセクションに1回だけ掲載
- AIセクションは現状の分量を維持しつつ、他セクションも充実させる
- 要約は**日本語**で、技術的内容はわかりやすく噛み砕く
