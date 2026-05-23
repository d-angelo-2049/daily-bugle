# 📰 Daily Bugle
Evaluated environment url: https://d-angelo-2049.github.io/daily-bugle/
> Your personal morning paper — curated tech, AI, and movie news delivered as a beautiful HTML digest.

![Static Badge](https://img.shields.io/badge/built_with-Claude_Code_%2F_Codex-blue) 

---

## What is this?

Daily Bugle is a self-hosted news digest generator. It collects articles from **Hacker News**, **Reddit**, **RSS feeds**, and **GitHub Trending**, then uses **Claude Code or Codex** to curate and summarize them into a clean, readable HTML page — your own daily newspaper.

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
uv sync
```

### 2. Fetch today's news

```bash
uv run run.py
```

This pulls articles from all sources and saves raw JSON to `data/`.

### 3. Generate the digest

Open this project in **Claude Code or Codex** and run:

```
/digest
```

The agent reads the collected data, summarizes articles in Japanese, curates the best ones, and generates `output/YYYY-MM-DD.html`. The header records which agent generated the digest, using `{{GENERATOR}}` in `template.html`.

### 4. Open and read

```bash
open output/YYYY-MM-DD.html
```

---

## Project Structure

```
daily-bugle/
├── fetchers/
│   ├── hackernews.py     # Hacker News API
│   ├── reddit.py         # Reddit API (no auth required)
│   └── rss.py            # RSS feeds via feedparser
├── .agents/
│   └── skills/
│       └── digest/
│           └── SKILL.md  # Digest generation instructions for Claude Code/Codex
├── data/                 # Raw fetched JSON (gitignored)
├── output/               # Generated HTML (gitignored)
├── run.py                # Fetch entrypoint
├── pyproject.toml
├── uv.lock
└── CLAUDE.md
```

---

## Design principles

- **No paid APIs** — HN and Reddit have free public APIs; RSS is open
- **No API billing** — summarization runs inside your Claude Code or Codex session
- **No server needed** — just open the dated HTML file in your browser
- **Privacy-first** — nothing is sent anywhere; everything stays local

---

## Roadmap

- [ ] Morning notification via LINE / Slack
- [ ] Bluesky feed integration
- [ ] Custom topic filters
- [ ] Scheduled auto-fetch via cron
