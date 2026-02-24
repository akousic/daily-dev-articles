#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import json
import os
import re
import textwrap
from pathlib import Path
from typing import List, Dict

import requests
import trafilatura

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ARTICLES_DIR = DOCS / "articles"

HN_TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
Hn_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{id}.json"

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
        "github.com",
        "gitlab.com",
        "stackoverflow.com",
        "dev.to",
        "xda-developers.com",
        "arxiv.org",
        "openai.com",
        "anthropic.com",
    )

    if any(d in url.lower() for d in trusted_dev_domains):
        return True

    return bool(tokens & include_words)


def fetch_hn_top(limit: int = 20) -> List[Dict]:
    ids = requests.get(HN_TOP_URL, headers=HEADERS, timeout=20).json()
    stories = []
    for sid in ids[:limit * 10]:
        item = requests.get(Hn_ITEM_URL.format(id=sid), headers=HEADERS, timeout=20).json()
        if not item:
            continue
        if item.get("type") != "story" or not item.get("url"):
            continue
        url = item["url"]
        if "news.ycombinator.com" in url:
            continue
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
                "comments_url": f"https://news.ycombinator.com/item?id={item['id']}",
            }
        )
        if len(stories) >= limit:
            break
    stories.sort(key=lambda s: s["score"], reverse=True)
    return stories[:limit]


def extract_summary(url: str) -> Dict[str, str]:
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
    takeaways = sents[3:6]
    if not takeaways:
        takeaways = ["Read the full article for deeper context and examples."]

    return {
        "summary": summary,
        "takeaways": takeaways,
    }


def write_article(day: str, rank: int, story: Dict, summary_data: Dict) -> Path:
    slug = slugify(story["title"])
    filename = f"{day}-{rank:02d}-{slug}.md"
    path = ARTICLES_DIR / filename

    md = f"""# {story['title']}

- **Source:** Hacker News top stories
- **Rank (today):** #{rank}
- **HN score:** {story['score']}
- **Author on HN:** {story['author']}
- **Published (UTC):** {story['published'].strftime('%Y-%m-%d %H:%M')}
- **Original:** {story['url']}
- **HN discussion:** {story['comments_url']}

## Summary

{summary_data['summary']}

## Key Takeaways

"""
    for item in summary_data["takeaways"]:
        md += f"- {item}\n"

    md += "\n---\n_Auto-generated daily digest entry._\n"
    path.write_text(md, encoding="utf-8")
    return path


def update_daily_digest(day: str, articles: List[Dict]) -> Path:
    digest_path = DOCS / f"{day}.md"
    md = f"# Daily Dev Articles — {day}\n\n"
    md += "Top 5 software-development articles sourced from Hacker News top stories.\n\n"

    for a in articles:
        md += textwrap.dedent(
            f"""
            ## {a['rank']}. [{a['title']}]({a['article_path']})

            - **Original link:** {a['url']}
            - **HN score:** {a['score']}
            - **Quick summary:** {a['summary']}

            """
        )

    md += "\n---\nGenerated automatically by GitHub Actions.\n"
    digest_path.write_text(md, encoding="utf-8")
    return digest_path


def update_index(day: str) -> None:
    index_path = DOCS / "index.md"
    daily_files = sorted(
        [p for p in DOCS.glob("20*.md") if p.name != "index.md"], reverse=True
    )

    lines = ["# Daily Dev Articles", "", "Latest digests:", ""]
    for f in daily_files[:30]:
        lines.append(f"- [{f.stem}](./{f.name})")

    lines += ["", "## About", "", "- Sources: Hacker News top stories", "- Count: 5 articles/day", "- Format: one digest + individual markdown pages", ""]
    index_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    today = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    DOCS.mkdir(parents=True, exist_ok=True)
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)

    for stale in ARTICLES_DIR.glob(f"{today}-*.md"):
        stale.unlink(missing_ok=True)

    stories = fetch_hn_top(limit=5)
    article_meta = []

    for i, story in enumerate(stories, start=1):
        summary_data = extract_summary(story["url"])
        path = write_article(today, i, story, summary_data)
        article_meta.append(
            {
                "rank": i,
                "title": story["title"],
                "url": story["url"],
                "score": story["score"],
                "summary": summary_data["summary"],
                "article_path": f"./articles/{path.name}",
            }
        )

    update_daily_digest(today, article_meta)
    update_index(today)

    print(json.dumps({"date": today, "count": len(article_meta)}, indent=2))


if __name__ == "__main__":
    main()
