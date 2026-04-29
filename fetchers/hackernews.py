import json
from datetime import datetime

import requests

HN_TOP_STORIES = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM = "https://hacker-news.firebaseio.com/v0/item/{}.json"


def fetch(limit=30):
    ids = requests.get(HN_TOP_STORIES).json()[:limit]
    stories = []
    for item_id in ids:
        item = requests.get(HN_ITEM.format(item_id)).json()
        if item and item.get("type") == "story" and item.get("url"):
            stories.append(
                {
                    "title": item.get("title"),
                    "url": item.get("url"),
                    "score": item.get("score", 0),
                    "comments": item.get("descendants", 0),
                    "by": item.get("by"),
                    "source": "Hacker News",
                }
            )
    return stories


if __name__ == "__main__":
    import json
    import os

    os.makedirs("data", exist_ok=True)
    data = fetch()
    with open("data/hackernews.json", "w") as f:
        json.dump(
            {"fetched_at": datetime.now().isoformat(), "articles": data},
            f,
            ensure_ascii=False,
            indent=2,
        )
    print(f"Fetched {len(data)} stories from Hacker News")
