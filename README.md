# 📰 Daily Bugle

> Your personal morning paper — curated tech, AI, and movie news delivered as a beautiful HTML digest.

![Static Badge](https://img.shields.io/badge/built_with-Claude_Code-blue) 

---

## What is this?

Daily Bugle is a self-hosted news digest generator. It collects articles from **Hacker News**, **Reddit**, and **RSS feeds**, then uses **Claude Code** to curate and summarize them into a clean, readable HTML page — your own daily newspaper.

No subscriptions. No algorithms. Just the stories you actually want to read.

---

## How it looks

| Tech & AI | Movies |
|---|---|
| Top HN stories, Reddit hot threads, startup news | r/movies discussions, film reviews, new releases |

Cards with Japanese summaries, source badges, and scores — readable in under 5 minutes.

---

## Sources

| Category | Sources |
|---|---|
| Tech & AI | Hacker News, r/MachineLearning, r/artificial, r/programming, r/startups, r/devops, r/aws, r/kubernetes, r/webdev, r/technology |
| Tech RSS | TechCrunch, The Verge, Wired, MIT Tech Review |
| Movies | r/movies, r/TrueFilm, r/flicks, Roger Ebert, IndieWire |

---

## Usage

### 1. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 2. Fetch today's news

```bash
python3 run.py
```

This pulls articles from all sources and saves raw JSON to `data/`.

### 3. Generate the digest

Open this project in **Claude Code** and run:

```
/digest
```

Claude reads the collected data, summarizes articles in Japanese, curates the best ones, and generates `output/index.html`.

### 4. Open and read

```bash
open output/index.html
```

---

## Project Structure

```
daily-bugle/
├── fetchers/
│   ├── hackernews.py     # Hacker News API
│   ├── reddit.py         # Reddit API (no auth required)
│   └── rss.py            # RSS feeds via feedparser
├── .claude/
│   └── commands/
│       └── digest.md     # /digest slash command for Claude Code
├── data/                 # Raw fetched JSON (gitignored)
├── output/               # Generated HTML (gitignored)
├── run.py                # Fetch entrypoint
├── requirements.txt
└── CLAUDE.md
```

---

## Design principles

- **No paid APIs** — HN and Reddit have free public APIs; RSS is open
- **No Claude API billing** — summarization runs inside a Claude Code session
- **No server needed** — just open `index.html` in your browser
- **Privacy-first** — nothing is sent anywhere; everything stays local

---

## Roadmap

- [ ] Morning notification via LINE / Slack
- [ ] Bluesky feed integration
- [ ] Custom topic filters
- [ ] Scheduled auto-fetch via cron
