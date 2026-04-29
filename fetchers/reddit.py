import json
from datetime import datetime

import requests

HEADERS = {"User-Agent": "daily-bugle/1.0"}

SUBREDDITS = {
    "ai": [
        "MachineLearning",
        "artificial",
        "LocalLLaMA",
        "ChatGPT",
    ],
    "frontend": [
        "javascript",
        "reactjs",
        "vuejs",
        "css",
        "webdev",
    ],
    "backend": [
        "golang",
        "rust",
        "java",
        "python",
        "node",
    ],
    "cloud": [
        "devops",
        "aws",
        "kubernetes",
        "docker",
        "sre",
    ],
    "oss": [
        "linux",
        "opensource",
        "programming",
    ],
    "startups": [
        "startups",
        "technology",
    ],
    "movies": [
        "movies",
        "TrueFilm",
        "flicks",
    ],
}


def fetch_subreddit(subreddit, limit=10):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    if resp.status_code != 200:
        print(f"Failed to fetch r/{subreddit}: {resp.status_code}")
        return []
    posts = []
    for post in resp.json()["data"]["children"]:
        d = post["data"]
        if d.get("stickied"):
            continue
        posts.append(
            {
                "title": d["title"],
                "url": d.get("url"),
                "score": d.get("score", 0),
                "comments": d.get("num_comments", 0),
                "subreddit": subreddit,
                "source": f"r/{subreddit}",
                "permalink": f"https://reddit.com{d['permalink']}",
            }
        )
    return posts


def fetch():
    result = {category: [] for category in SUBREDDITS}
    for category, subreddits in SUBREDDITS.items():
        for sub in subreddits:
            result[category].extend(fetch_subreddit(sub))
    return result


if __name__ == "__main__":
    import os

    os.makedirs("data", exist_ok=True)
    data = fetch()
    with open("data/reddit.json", "w") as f:
        json.dump(
            {"fetched_at": datetime.now().isoformat(), "articles": data},
            f,
            ensure_ascii=False,
            indent=2,
        )
    for cat, posts in data.items():
        print(f"  {cat}: {len(posts)} posts")
