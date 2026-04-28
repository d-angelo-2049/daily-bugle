# Daily Bugle

自分専用の朝刊。テック・AI・映画など興味トピックのニュースを収集し、読みやすいHTMLにまとめる。

## プロジェクト概要

- **収集ソース**: Hacker News API、Reddit API、RSSフィード
- **要約・キュレーション**: Claude Code 内で実行（外部APIコールなし）
- **出力**: `output/index.html`（ブラウザで開くだけで読める）

## セクション構成

1. **Tech & AI** — HN トップ、Reddit（r/MachineLearning、r/programming、r/startups、r/devops など）
2. **Movies** — Reddit（r/movies、r/TrueFilm）、映画系RSS

## 使い方

### 記事を収集する

```bash
python3 run.py
```

これで各ソースから記事を取得し、`data/` に生データを保存する。

### Claude Code でダイジェストを生成する

```
/digest
```

`data/` の生データを読んで要約・キュレーションし、`output/index.html` を生成する。

## ファイル構成

```
daily-bugle/
├── CLAUDE.md
├── run.py                  # データ収集エントリーポイント
├── fetchers/
│   ├── hackernews.py       # Hacker News API
│   ├── reddit.py           # Reddit API
│   └── rss.py              # RSSフィード
├── data/                   # 収集した生データ（JSON）
├── output/
│   └── index.html          # 生成されたダイジェスト
└── requirements.txt
```

## 開発メモ

- Twitter/X APIは高額のため対象外。Bluesky や RSS で補完する方針。
- 要約はClaude Codeが担うため、Anthropic APIキー不要。
- `output/index.html` は毎回上書き生成される。
