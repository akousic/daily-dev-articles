#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import json
import os
import re
import textwrap
from pathlib import Path
from typing import List, Dict
from urllib.parse import urlparse

import requests
import trafilatura

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ARTICLES_DIR = DOCS / "articles"

HN_TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{id}.json"
X_SEARCH_URLS = [
    "https://api.x.com/2/tweets/search/recent",
    "https://api.twitter.com/2/tweets/search/recent",
]

HEADERS = {"User-Agent": "daily-dev-articles-bot/1.0"}


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:80] or "article"


def split_sentences(text: str) -> List[str]:
    sents = re.split(r"(?<=[.!?])\s+", text.strip())
    return [s.strip() for s in sents if len(s.strip()) > 20]


def is_dev_story(title: str, url: str) -> bool:
    text = f"{title} {url}".lower()
    tokens = set(re.findall(r"[a-z0-9+#.-]+", text))

    include_words = {
        "ai", "llm", "developer", "dev", "code", "coding", "python", "javascript",
        "rust", "go", "java", "typescript", "framework", "software", "api", "database",
        "cloud", "kubernetes", "linux", "github", "security", "infra", "compiler",
        "engineering", "programming", "startup", "open-source", "machine", "learning",
    }
    exclude_words = {
        "disney", "dog", "irs", "tax", "airport", "luggage", "celebrity", "sports",
        "fashion", "movie", "music",
    }

    if tokens & exclude_words:
        return False

    trusted_dev_domains = (
        "github.com", "gitlab.com", "stackoverflow.com", "dev.to", "arxiv.org",
        "openai.com", "anthropic.com", "cloudflare.com", "stripe.com", "vercel.com",
    )
    if any(d in url.lower() for d in trusted_dev_domains):
        return True

    return bool(tokens & include_words)


def canonicalize_url(url: str) -> str:
    try:
        p = urlparse(url)
        host = (p.netloc or "").lower().replace("www.", "")
        return f"{p.scheme}://{host}{p.path}".rstrip("/")
    except Exception:
        return url


def is_article_url(url: str) -> bool:
    if not url:
        return False
    low = url.lower()
    blocked_hosts = [
        "x.com", "twitter.com", "youtube.com", "youtu.be", "news.ycombinator.com",
        "reddit.com", "tiktok.com", "instagram.com",
    ]
    if any(h in low for h in blocked_hosts):
        return False
    return low.startswith("http")


def fetch_hn_top(limit: int = 5) -> List[Dict]:
    ids = requests.get(HN_TOP_URL, headers=HEADERS, timeout=20).json()
    stories = []
    for sid in ids[: limit * 12]:
        item = requests.get(HN_ITEM_URL.format(id=sid), headers=HEADERS, timeout=20).json()
        if not item or item.get("type") != "story" or not item.get("url"):
            continue
        url = item["url"]
        if not is_dev_story(item.get("title", ""), url):
            continue
        stories.append(
            {
                "id": item["id"],
                "title": item.get("title", "Untitled"),
                "url": url,
                "score": item.get("score", 0),
                "author": item.get("by", "unknown"),
                "published": dt.datetime.fromtimestamp(item.get("time", 0), dt.timezone.utc),
                "source": "Hacker News",
                "source_meta": f"HN score {item.get('score', 0)}",
                "comments_url": f"https://news.ycombinator.com/item?id={item['id']}",
            }
        )
        if len(stories) >= limit:
            break
    return stories[:limit]


def fetch_x_top(limit: int = 10) -> List[Dict]:
    debug = os.environ.get("X_DEBUG", "").lower() in {"1", "true", "yes"}
    token = (Path(ROOT / ".x_token").read_text().strip() if (ROOT / ".x_token").exists() else "")
    token = token or os.environ.get("X_BEARER_TOKEN", "")
    if not token:
        if debug:
            print("[x] missing X_BEARER_TOKEN")
        return []

    query = os.environ.get(
        "X_TECH_QUERY",
        '(AI OR LLM OR "software engineering" OR programming OR devtools OR "open source") has:links -is:retweet lang:en',
    )

    params = {
        "query": query,
        "max_results": 100,
        "tweet.fields": "created_at,public_metrics,author_id,entities",
        "expansions": "author_id",
        "user.fields": "username,name",
    }
    headers = {"Authorization": f"Bearer {token}", **HEADERS}
    r = None
    for endpoint in X_SEARCH_URLS:
        resp = requests.get(endpoint, params=params, headers=headers, timeout=25)
        if resp.status_code == 200:
            r = resp
            if debug:
                print(f"[x] success endpoint={endpoint}")
            break
        if debug:
            body = (resp.text or "")[:300].replace("\n", " ")
            print(f"[x] request failed endpoint={endpoint} status={resp.status_code} body={body}")

    if r is None:
        return []

    payload = r.json()
    data = payload.get("data", [])
    includes = payload.get("includes", {})
    users = {u["id"]: u for u in includes.get("users", [])}

    ranked: Dict[str, Dict] = {}

    for t in data:
        urls = ((t.get("entities") or {}).get("urls") or [])
        expanded_links = [u.get("expanded_url") or u.get("url") for u in urls]
        article_links = [u for u in expanded_links if is_article_url(u)]
        if not article_links:
            continue

        target_url = article_links[0]
        key = canonicalize_url(target_url)
        metrics = t.get("public_metrics", {})
        like = int(metrics.get("like_count", 0))
        repost = int(metrics.get("retweet_count", 0))
        reply = int(metrics.get("reply_count", 0))
        quote = int(metrics.get("quote_count", 0))
        score = like + 2 * repost + int(1.5 * reply) + 2 * quote

        user = users.get(t.get("author_id"), {})
        username = user.get("username", "unknown")
        title = (t.get("text") or "").replace("\n", " ").strip()
        if len(title) > 120:
            title = title[:117] + "..."

        candidate = {
            "id": t.get("id"),
            "title": title or f"Post by @{username}",
            "url": target_url,
            "score": score,
            "published": dt.datetime.fromisoformat((t.get("created_at") or "").replace("Z", "+00:00")) if t.get("created_at") else dt.datetime.now(dt.timezone.utc),
            "source": "X",
            "source_meta": f"likes {like}, reposts {repost}, replies {reply}, quotes {quote}, score {score}",
            "x_post_url": f"https://x.com/{username}/status/{t.get('id')}",
            "author": f"@{username}",
        }

        if key not in ranked or candidate["score"] > ranked[key]["score"]:
            ranked[key] = candidate

    results = sorted(ranked.values(), key=lambda x: x["score"], reverse=True)
    return results[:limit]


def extract_summary(url: str) -> Dict[str, List[str] | str]:
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        return {
            "summary": "Could not extract article text automatically.",
            "takeaways": ["Open the original article for full details."],
        }

    text = trafilatura.extract(downloaded, output_format="txt") or ""
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) < 150:
        return {
            "summary": "Article text was too short for reliable extraction.",
            "takeaways": ["Open the original article for full details."],
        }

    sents = split_sentences(text)
    summary = " ".join(sents[:3]) if sents else text[:350]
    takeaways = sents[3:6] if len(sents) > 3 else ["Read the full article for deeper context and examples."]
    return {"summary": summary, "takeaways": takeaways}


def write_article(day: str, rank: int, story: Dict, summary_data: Dict) -> Path:
    slug = slugify(story["title"])
    path = ARTICLES_DIR / f"{day}-{rank:02d}-{slug}.md"

    extra = ""
    if story.get("source") == "Hacker News":
        extra = f"- **HN discussion:** {story.get('comments_url', '')}\n"
    if story.get("source") == "X":
        extra += f"- **X post:** {story.get('x_post_url', '')}\n- **Posted by:** {story.get('author', '')}\n"

    md = f"""# {story['title']}

- **Source:** {story['source']}
- **Rank (today):** #{rank}
- **Ranking metrics:** {story['source_meta']}
- **Published (UTC):** {story['published'].strftime('%Y-%m-%d %H:%M')}
- **Original:** {story['url']}
{extra}
## Summary

{summary_data['summary']}

## Key Takeaways

"""
    for item in summary_data["takeaways"]:
        md += f"- {item}\n"

    md += "\n---\n_Auto-generated daily digest entry._\n"
    path.write_text(md, encoding="utf-8")
    return path


def update_daily_digest(day: str, articles: List[Dict], source_name: str) -> None:
    digest_path = DOCS / f"{day}.md"
    md = f"# Daily Dev Articles — {day}\n\n"
    md += f"Top {len(articles)} software-development articles sourced from **{source_name}**.\n\n"

    for a in articles:
        md += textwrap.dedent(
            f"""
            ## {a['rank']}. [{a['title']}]({a['article_path']})

            - **Original link:** {a['url']}
            - **Ranking metrics:** {a['score_text']}
            - **Quick summary:** {a['summary']}

            """
        )

    md += "\n---\nGenerated automatically by GitHub Actions.\n"
    digest_path.write_text(md, encoding="utf-8")


def update_index() -> None:
    index_path = DOCS / "index.md"
    daily_files = sorted([p for p in DOCS.glob("20*.md") if p.name != "index.md"], reverse=True)
    lines = ["# Daily Dev Articles", "", "Latest digests:", ""]
    for f in daily_files[:30]:
        lines.append(f"- [{f.stem}](./{f.name})")
    lines += ["", "## About", "", "- Sources: X (preferred), fallback to Hacker News", "- Count: 10 articles/day from X, fallback 5 from HN", "- Format: one digest + individual markdown pages", ""]
    index_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    today = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    DOCS.mkdir(parents=True, exist_ok=True)
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)

    for stale in ARTICLES_DIR.glob(f"{today}-*.md"):
        stale.unlink(missing_ok=True)

    stories = fetch_x_top(limit=10)
    source_name = "X"
    if not stories:
        stories = fetch_hn_top(limit=5)
        source_name = "Hacker News (fallback)"

    article_meta = []
    for i, story in enumerate(stories, start=1):
        summary_data = extract_summary(story["url"])
        path = write_article(today, i, story, summary_data)
        article_meta.append(
            {
                "rank": i,
                "title": story["title"],
                "url": story["url"],
                "score_text": story["source_meta"],
                "summary": summary_data["summary"],
                "article_path": f"./articles/{path.name}",
            }
        )

    update_daily_digest(today, article_meta, source_name)
    update_index()
    print(json.dumps({"date": today, "count": len(article_meta), "source": source_name}, indent=2))


if __name__ == "__main__":
    main()
