#!/usr/bin/env python3
"""
Reads raw fetched data and outputs data/curated.json with
top-ranked articles per section. Run between run.py and /digest
to reduce the volume Claude needs to process.
"""

import json
import os
import re
from datetime import datetime

# Max articles Claude will receive per section
LIMITS = {
    "ai": 14,
    "frontend": 14,
    "backend": 14,
    "cloud": 14,
    "oss": 14,
    "startups": 14,
    "movies": 14,
    "github_trending": 14,
}

# Reddit posts below this score are dropped before ranking
MIN_REDDIT_SCORE = 5


def is_image_post(article: dict) -> bool:
    url = article.get("url", "")
    return url.startswith("https://i.redd.it/") or url.startswith("http://i.redd.it/")


def is_rss(article: dict) -> bool:
    return "score" not in article or article.get("score") is None


def score_article(article: dict) -> float:
    return article.get("score", 0) + article.get("comments", 0) * 0.5


def score_repo(repo: dict) -> float:
    raw = repo.get("stars_today", "0 stars today")
    try:
        return float(raw.split()[0].replace(",", ""))
    except (ValueError, IndexError):
        return 0.0


def load_json(path: str) -> dict:
    if not os.path.exists(path):
        print(f"  [skip] {path} not found")
        return {}
    with open(path) as f:
        return json.load(f)


def filter_reddit(articles: list) -> list:
    """Drop image-only posts and below-threshold scores."""
    return [a for a in articles if not is_image_post(a) and a.get("score", 0) >= MIN_REDDIT_SCORE]


def curate_pool(pool: list) -> list:
    """Sort by score, deduplicate by URL."""
    seen: set[str] = set()
    deduped = []
    for a in sorted(pool, key=score_article, reverse=True):
        key = a.get("url") or a.get("title", "")
        if key not in seen:
            seen.add(key)
            deduped.append(a)
    return deduped


def main() -> None:
    os.makedirs("data", exist_ok=True)

    hn = load_json("data/hackernews.json")
    reddit = load_json("data/reddit.json")
    rss = load_json("data/rss.json")
    gh = load_json("data/github_trending.json")

    hn_articles = hn.get("articles", [])
    reddit_articles = reddit.get("articles", {})
    rss_articles = rss.get("articles", {})
    gh_repos = gh.get("repos", [])

    sections: dict[str, list] = {}

    # ── AI & ML ──────────────────────────────────────────────
    # Word-boundary patterns prevent "ai" matching "fail", "model" matching "models", etc.
    _ai_kw_exact = ("llm", "gpt", "claude", "openai", "deepseek", "mistral", "gemini", "anthropic")
    _ai_kw_word = ("ai", "ml", "model", "neural", "agent")
    _ai_exact_re = re.compile(
        r"\b(?:" + "|".join(re.escape(k) for k in _ai_kw_exact) + r")\b", re.IGNORECASE
    )
    _ai_word_re = re.compile(
        r"\b(?:" + "|".join(re.escape(k) for k in _ai_kw_word) + r")\b", re.IGNORECASE
    )

    def _is_ai_title(title: str) -> bool:
        return bool(_ai_exact_re.search(title) or _ai_word_re.search(title))

    ai_hn = [a for a in hn_articles if _is_ai_title(a.get("title", ""))]
    ai_reddit = filter_reddit(reddit_articles.get("ai", []))
    ai_rss = rss_articles.get("ai", [])  # RSS always included as-is
    sections["ai"] = curate_pool(ai_hn + ai_reddit + ai_rss)[: LIMITS["ai"]]

    # ── Per-section Reddit + RSS merge ───────────────────────
    for section in ("frontend", "backend", "cloud", "oss", "startups", "movies"):
        reddit_pool = filter_reddit(reddit_articles.get(section, []))
        rss_pool = rss_articles.get(section, [])  # RSS always included
        pool = reddit_pool + rss_pool

        # Supplement OSS with high-scoring HN items not already in AI
        if section == "oss":
            ai_urls = {a.get("url") for a in sections["ai"]}
            hn_oss = [a for a in hn_articles if a.get("url") not in ai_urls]
            pool += sorted(hn_oss, key=score_article, reverse=True)[:5]

        sections[section] = curate_pool(pool)[: LIMITS[section]]

    # ── GitHub Trending ───────────────────────────────────────
    sections["github_trending"] = sorted(gh_repos, key=score_repo, reverse=True)[
        : LIMITS["github_trending"]
    ]

    curated = {
        "generated_at": datetime.now().isoformat(),
        "sections": sections,
    }

    out_path = "data/curated.json"
    with open(out_path, "w") as f:
        json.dump(curated, f, ensure_ascii=False, indent=2)

    total = sum(len(v) for v in sections.values())
    print(f"Curated {total} articles → {out_path}")
    for sec, articles in sections.items():
        print(f"  {sec}: {len(articles)}")


if __name__ == "__main__":
    main()
