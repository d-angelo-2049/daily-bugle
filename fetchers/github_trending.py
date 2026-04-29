from datetime import datetime

import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "daily-bugle/1.0"}

LANGUAGES = ["", "python", "javascript", "typescript", "go", "rust", "java"]


def fetch_trending(language="", since="daily", limit=10):
    url = f"https://github.com/trending/{language}?since={since}"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    if resp.status_code != 200:
        print(f"Failed to fetch GitHub trending ({language or 'all'}): {resp.status_code}")
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    repos = []
    for article in soup.select("article.Box-row")[:limit]:
        name_tag = article.select_one("h2 a")
        if not name_tag:
            continue
        full_name = name_tag.get("href", "").strip("/")
        description_tag = article.select_one("p")
        description = description_tag.get_text(strip=True) if description_tag else ""
        stars_tag = article.select_one("a[href$='/stargazers']")
        stars = stars_tag.get_text(strip=True) if stars_tag else "0"
        today_tag = article.select_one("span.d-inline-block.float-sm-right")
        stars_today = today_tag.get_text(strip=True) if today_tag else ""
        lang_tag = article.select_one("span[itemprop='programmingLanguage']")
        lang = lang_tag.get_text(strip=True) if lang_tag else language or "Unknown"

        repos.append(
            {
                "name": full_name,
                "url": f"https://github.com/{full_name}",
                "description": description,
                "stars": stars,
                "stars_today": stars_today,
                "language": lang,
                "source": "GitHub Trending",
            }
        )
    return repos


def fetch():
    all_repos = fetch_trending(language="", limit=15)
    seen = {r["name"] for r in all_repos}
    for lang in ["python", "javascript", "typescript", "go", "rust", "java"]:
        for repo in fetch_trending(language=lang, limit=5):
            if repo["name"] not in seen:
                all_repos.append(repo)
                seen.add(repo["name"])
    return all_repos


if __name__ == "__main__":
    import json
    import os

    os.makedirs("data", exist_ok=True)
    data = fetch()
    with open("data/github_trending.json", "w") as f:
        json.dump(
            {"fetched_at": datetime.now().isoformat(), "repos": data},
            f,
            ensure_ascii=False,
            indent=2,
        )
    print(f"Fetched {len(data)} trending repos from GitHub")
