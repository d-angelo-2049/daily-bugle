#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime

import preprocess

os.makedirs("data", exist_ok=True)
os.makedirs("output", exist_ok=True)

sys.path.insert(0, os.path.dirname(__file__))

from fetchers import github_trending, hackernews, reddit, rss  # noqa: E402

print("=== Daily Bugle: Fetching news ===")

print("\n[1/4] Hacker News...")
hn_data = hackernews.fetch()
with open("data/hackernews.json", "w") as f:
    json.dump(
        {"fetched_at": datetime.now().isoformat(), "articles": hn_data},
        f,
        ensure_ascii=False,
        indent=2,
    )
print(f"  -> {len(hn_data)} stories")

print("\n[2/4] Reddit...")
reddit_data = reddit.fetch()
with open("data/reddit.json", "w") as f:
    json.dump(
        {"fetched_at": datetime.now().isoformat(), "articles": reddit_data},
        f,
        ensure_ascii=False,
        indent=2,
    )
for cat, posts in reddit_data.items():
    print(f"  -> {cat}: {len(posts)} posts")

print("\n[3/4] RSS feeds...")
rss_data = rss.fetch()
with open("data/rss.json", "w") as f:
    json.dump(
        {"fetched_at": datetime.now().isoformat(), "articles": rss_data},
        f,
        ensure_ascii=False,
        indent=2,
    )
for cat, articles in rss_data.items():
    print(f"  -> {cat}: {len(articles)} articles")

print("\n[4/4] GitHub Trending...")
gh_data = github_trending.fetch()
with open("data/github_trending.json", "w") as f:
    json.dump(
        {"fetched_at": datetime.now().isoformat(), "repos": gh_data},
        f,
        ensure_ascii=False,
        indent=2,
    )
print(f"  -> {len(gh_data)} trending repos")

print("\n[5/5] Preprocessing (curating articles)...")
preprocess.main()

print("\n=== Done! Run /digest in Claude Code to generate the digest ===")
