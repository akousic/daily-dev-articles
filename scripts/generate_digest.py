#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import json
import re
import textwrap
from pathlib import Path
from typing import Dict, List

import requests
import trafilatura

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ARTICLES_DIR = DOCS / "articles"

HN_TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{id}.json"
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

    md = f"""# {story['title']}

- **Source:** {story['source']}
- **Rank (today):** #{rank}
- **Ranking metrics:** {story['source_meta']}
- **Published (UTC):** {story['published'].strftime('%Y-%m-%d %H:%M')}
- **Original:** {story['url']}
- **HN discussion:** {story.get('comments_url', '')}

## Summary

{summary_data['summary']}

## Key Takeaways

"""
    for item in summary_data["takeaways"]:
        md += f"- {item}\n"

    md += "\n---\n_Auto-generated daily digest entry._\n"
    path.write_text(md, encoding="utf-8")
    return path


def update_daily_digest(day: str, articles: List[Dict]) -> None:
    digest_path = DOCS / f"{day}.md"
    md = f"# Daily Dev Articles — {day}\n\n"
    md += f"Top {len(articles)} software-development articles sourced from **Hacker News**.\n\n"

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
    lines += ["", "## About", "", "- Source: Hacker News", "- Count: 5 articles/day", "- Format: one digest + individual markdown pages", ""]
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
                "score_text": story["source_meta"],
                "summary": summary_data["summary"],
                "article_path": f"./articles/{path.name}",
            }
        )

    update_daily_digest(today, article_meta)
    update_index()
    print(json.dumps({"date": today, "count": len(article_meta), "source": "Hacker News"}, indent=2))


if __name__ == "__main__":
    main()
