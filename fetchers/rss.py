import json
from datetime import datetime

import feedparser

FEEDS = {
    "ai": [
        ("MIT Tech Review AI", "https://www.technologyreview.com/feed/"),
        ("The Batch (DeepLearning.AI)", "https://www.deeplearning.ai/the-batch/feed/"),
    ],
    "frontend": [
        ("CSS-Tricks", "https://css-tricks.com/feed/"),
        ("Smashing Magazine", "https://www.smashingmagazine.com/feed/"),
    ],
    "backend": [
        ("The Pragmatic Engineer", "https://newsletter.pragmaticengineer.com/feed"),
        ("InfoQ", "https://feed.infoq.com/"),
    ],
    "cloud": [
        ("The New Stack", "https://thenewstack.io/feed/"),
        ("CNCF Blog", "https://www.cncf.io/feed/"),
    ],
    "oss": [
        ("The Verge", "https://www.theverge.com/rss/index.xml"),
        ("Wired", "https://www.wired.com/feed/rss"),
    ],
    "startups": [
        ("TechCrunch", "https://techcrunch.com/feed/"),
    ],
    "movies": [
        ("Roger Ebert", "https://www.rogerebert.com/feed"),
        ("IndieWire", "https://www.indiewire.com/feed/"),
    ],
}


def fetch_feed(name, url, limit=5):
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries[:limit]:
        articles.append(
            {
                "title": entry.get("title"),
                "url": entry.get("link"),
                "summary": entry.get("summary", "")[:300],
                "source": name,
            }
        )
    return articles


def fetch():
    result = {category: [] for category in FEEDS}
    for category, feeds in FEEDS.items():
        for name, url in feeds:
            result[category].extend(fetch_feed(name, url))
    return result


if __name__ == "__main__":
    import os

    os.makedirs("data", exist_ok=True)
    data = fetch()
    with open("data/rss.json", "w") as f:
        json.dump(
            {"fetched_at": datetime.now().isoformat(), "articles": data},
            f,
            ensure_ascii=False,
            indent=2,
        )
    for cat, articles in data.items():
        print(f"  {cat}: {len(articles)} articles")
