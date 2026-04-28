import requests
import json
from datetime import datetime

HEADERS = {"User-Agent": "daily-bugle/1.0"}

SUBREDDITS = {
    "tech": [
        "MachineLearning",
        "artificial",
        "programming",
        "startups",
        "devops",
        "aws",
        "kubernetes",
        "webdev",
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
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code != 200:
        print(f"Failed to fetch r/{subreddit}: {resp.status_code}")
        return []
    posts = []
    for post in resp.json()["data"]["children"]:
        d = post["data"]
        if d.get("stickied") or d.get("is_self") and len(d.get("selftext", "")) < 100:
            continue
        posts.append({
            "title": d["title"],
            "url": d.get("url"),
            "score": d.get("score", 0),
            "comments": d.get("num_comments", 0),
            "subreddit": subreddit,
            "source": f"r/{subreddit}",
            "permalink": f"https://reddit.com{d['permalink']}",
        })
    return posts

def fetch():
    result = {"tech": [], "movies": []}
    for category, subreddits in SUBREDDITS.items():
        for sub in subreddits:
            result[category].extend(fetch_subreddit(sub))
    return result

if __name__ == "__main__":
    import os
    os.makedirs("data", exist_ok=True)
    data = fetch()
    with open("data/reddit.json", "w") as f:
        json.dump({"fetched_at": datetime.now().isoformat(), "articles": data}, f, ensure_ascii=False, indent=2)
    tech_count = len(data["tech"])
    movie_count = len(data["movies"])
    print(f"Fetched {tech_count} tech posts, {movie_count} movie posts from Reddit")
