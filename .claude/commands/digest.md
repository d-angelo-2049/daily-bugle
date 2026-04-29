以下の手順で今日のDaily Bugleダイジェストを生成してください。

## 手順

1. `data/` ディレクトリ内のJSONファイルをすべて読み込む
2. 各記事・リポジトリをキュレーション・要約する
3. `output/index.html` を生成する

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

## HTMLの要件

- モダンでリーダブルなデザイン（ダークモード）
- **タブ形式**でセクションを切り替え（AI / Frontend / Backend / Cloud / OSS / Startups / Movies）
- 各セクションの冒頭にフィーチャーカード（最重要記事1〜2件を大きく表示）
- 残りはグリッドカード（2カラム）
- 各カードに：タイトル、日本語要約（2〜3文）、ソース、元リンク、スコア
- 生成日時を表示

## キュレーション基準

- スコア・コメント数・話題性を重視
- セクションをまたいで重複する記事は最も関連するセクションに1回だけ掲載
- AIセクションは現状の分量を維持しつつ、他セクションも充実させる
- 要約は**日本語**で、技術的内容はわかりやすく噛み砕く
