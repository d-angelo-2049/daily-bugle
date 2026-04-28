#!/usr/bin/env python3
import os
import sys

os.makedirs("data", exist_ok=True)
os.makedirs("output", exist_ok=True)

sys.path.insert(0, os.path.dirname(__file__))

from fetchers import hackernews, reddit, rss

print("=== Daily Bugle: Fetching news ===")

print("\n[1/3] Hacker News...")
hn_data = hackernews.fetch()
import json
with open("data/hackernews.json", "w") as f:
    from datetime import datetime
    json.dump({"fetched_at": datetime.now().isoformat(), "articles": hn_data}, f, ensure_ascii=False, indent=2)
print(f"  -> {len(hn_data)} stories")

print("\n[2/3] Reddit...")
reddit_data = reddit.fetch()
with open("data/reddit.json", "w") as f:
    json.dump({"fetched_at": datetime.now().isoformat(), "articles": reddit_data}, f, ensure_ascii=False, indent=2)
print(f"  -> tech: {len(reddit_data['tech'])}, movies: {len(reddit_data['movies'])} posts")

print("\n[3/3] RSS feeds...")
rss_data = rss.fetch()
with open("data/rss.json", "w") as f:
    json.dump({"fetched_at": datetime.now().isoformat(), "articles": rss_data}, f, ensure_ascii=False, indent=2)
print(f"  -> tech: {len(rss_data['tech'])}, movies: {len(rss_data['movies'])} articles")

print("\n=== Done! Run /digest in Claude Code to generate output/index.html ===")
