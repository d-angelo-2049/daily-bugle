# Daily Bugle

自分専用の朝刊。テック・AI・映画など興味トピックのニュースを収集し、読みやすいHTMLにまとめる。

## プロジェクト概要

- **収集ソース**: Hacker News API、Reddit API、RSSフィード
- **要約・キュレーション**: Claude Code 内で実行（外部APIコールなし）
- **出力**: `output/YYYY-MM-DD.html`（当時の日付のついたファイル名で出力し、ブラウザで開くだけで読める）

## セクション構成

1. **AI & ML** — HN・r/MachineLearning・r/artificial・r/LocalLLaMA
2. **Frontend** — r/javascript・r/reactjs・r/css・CSS-Tricks
3. **Backend** — r/golang・r/rust・r/java・r/python・InfoQ
4. **Cloud & CNCF** — r/kubernetes・r/aws・r/docker・CNCF Blog・The New Stack
5. **OSS & Linux** — r/linux・r/opensource・GitHub Trending
6. **Startups** — r/startups・r/technology・TechCrunch
7. **Movies** — Reddit（r/movies・r/TrueFilm）、Roger Ebert・IndieWire

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
