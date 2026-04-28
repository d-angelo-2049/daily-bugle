import feedparser
import json
from datetime import datetime

FEEDS = {
    "tech": [
        ("TechCrunch", "https://techcrunch.com/feed/"),
        ("The Verge", "https://www.theverge.com/rss/index.xml"),
        ("Wired", "https://www.wired.com/feed/rss"),
        ("MIT Tech Review", "https://www.technologyreview.com/feed/"),
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
        articles.append({
            "title": entry.get("title"),
            "url": entry.get("link"),
            "summary": entry.get("summary", "")[:300],
            "source": name,
        })
    return articles

def fetch():
    result = {"tech": [], "movies": []}
    for category, feeds in FEEDS.items():
        for name, url in feeds:
            result[category].extend(fetch_feed(name, url))
    return result

if __name__ == "__main__":
    import os
    os.makedirs("data", exist_ok=True)
    data = fetch()
    with open("data/rss.json", "w") as f:
        json.dump({"fetched_at": datetime.now().isoformat(), "articles": data}, f, ensure_ascii=False, indent=2)
    print(f"Fetched {len(data['tech'])} tech, {len(data['movies'])} movie articles from RSS")
