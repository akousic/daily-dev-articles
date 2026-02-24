#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import html
import json
import re
import textwrap
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List
from urllib.parse import urlparse

import requests
import trafilatura

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ARTICLES_DIR = DOCS / "articles"

HEADERS = {"User-Agent": "daily-dev-articles-bot/1.0"}

HN_TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{id}.json"
DEVTO_URL = "https://dev.to/api/articles?top=7"
REDDIT_URLS = [
    "https://www.reddit.com/r/programming/top.json?t=day&limit=15",
    "https://www.reddit.com/r/webdev/top.json?t=day&limit=15",
    "https://www.reddit.com/r/MachineLearning/top.json?t=day&limit=15",
]
RSS_SOURCES = [
    ("Lobsters", "https://lobste.rs/rss"),
    ("Cloudflare", "https://blog.cloudflare.com/rss/"),
    ("Stripe", "https://stripe.com/blog/feed.rss"),
    ("Vercel", "https://vercel.com/blog/rss.xml"),
    ("InfoQ", "https://feed.infoq.com/"),
    ("Changelog", "https://changelog.com/feed"),
]


def safe_get_json(url: str):
    try:
        return requests.get(url, headers=HEADERS, timeout=20).json()
    except Exception:
        return None


def safe_get_text(url: str) -> str:
    try:
        return requests.get(url, headers=HEADERS, timeout=20).text
    except Exception:
        return ""


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:80] or "article"


def canonicalize_url(url: str) -> str:
    try:
        p = urlparse(url)
        host = (p.netloc or "").lower().replace("www.", "")
        return f"{p.scheme}://{host}{p.path}".rstrip("/")
    except Exception:
        return url


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
        "celebrity", "sports", "fashion", "movie", "music", "politics",
    }
    if tokens & exclude_words:
        return False
    return bool(tokens & include_words) or any(
        d in url.lower() for d in ("github.com", "arxiv.org", "dev.to", "infoq.com")
    )


def parse_pub_date(raw: str | None) -> dt.datetime:
    if not raw:
        return dt.datetime.now(dt.timezone.utc)
    for fmt in (
        "%a, %d %b %Y %H:%M:%S %z",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
    ):
        try:
            d = dt.datetime.strptime(raw, fmt)
            return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)
        except Exception:
            pass
    return dt.datetime.now(dt.timezone.utc)


def fetch_hn(limit: int = 20) -> List[Dict]:
    out = []
    ids = safe_get_json(HN_TOP_URL) or []
    for sid in ids[: limit * 8]:
        item = safe_get_json(HN_ITEM_URL.format(id=sid))
        if not item or item.get("type") != "story" or not item.get("url"):
            continue
        if not is_dev_story(item.get("title", ""), item["url"]):
            continue
        out.append(
            {
                "title": item.get("title", "Untitled"),
                "url": item["url"],
                "score": float(item.get("score", 0)),
                "source": "Hacker News",
                "source_group": "Hacker News",
                "source_meta": f"HN score {item.get('score', 0)}",
                "published": dt.datetime.fromtimestamp(item.get("time", 0), dt.timezone.utc),
            }
        )
        if len(out) >= limit:
            break
    return out


def fetch_devto(limit: int = 12) -> List[Dict]:
    out = []
    arr = safe_get_json(DEVTO_URL)
    if not isinstance(arr, list):
        return out
    for a in arr[:limit]:
        title = a.get("title", "")
        url = a.get("url", "")
        if not url or not is_dev_story(title, url):
            continue
        reactions = a.get("positive_reactions_count", 0)
        comments = a.get("comments_count", 0)
        out.append(
            {
                "title": title,
                "url": url,
                "score": float(reactions + comments * 2),
                "source": "Dev.to",
                "source_group": "Dev.to",
                "source_meta": f"reactions {reactions}, comments {comments}",
                "published": parse_pub_date(a.get("published_at", "")),
            }
        )
    return out


def fetch_reddit(limit_each: int = 12) -> List[Dict]:
    out = []
    for u in REDDIT_URLS:
        data = safe_get_json(u)
        if not data:
            continue
        for ch in (data.get("data", {}).get("children", [])[:limit_each]):
            d = ch.get("data", {})
            title = d.get("title", "")
            url = d.get("url_overridden_by_dest") or d.get("url") or ""
            if not url or not is_dev_story(title, url):
                continue
            score = int(d.get("score", 0))
            comments = int(d.get("num_comments", 0))
            out.append(
                {
                    "title": title,
                    "url": url,
                    "score": float(score + comments * 1.5),
                    "source": f"Reddit ({d.get('subreddit','')})",
                    "source_group": "Reddit",
                    "source_meta": f"score {score}, comments {comments}",
                    "published": dt.datetime.fromtimestamp(d.get("created_utc", 0), dt.timezone.utc),
                }
            )
    return out


def fetch_rss(source_name: str, rss_url: str, limit: int = 10) -> List[Dict]:
    out = []
    xml_text = safe_get_text(rss_url)
    if not xml_text:
        return out
    try:
        root = ET.fromstring(xml_text)
    except Exception:
        return out

    items = root.findall(".//item")[:limit] or root.findall(".//{http://www.w3.org/2005/Atom}entry")[:limit]
    for item in items:
        title = (item.findtext("title") or item.findtext("{http://www.w3.org/2005/Atom}title") or "").strip()
        link = (item.findtext("link") or "").strip()
        if not link:
            atom_link = item.find("{http://www.w3.org/2005/Atom}link")
            if atom_link is not None:
                link = atom_link.attrib.get("href", "")
        if not link or not is_dev_story(title, link):
            continue
        pub = item.findtext("pubDate") or item.findtext("{http://www.w3.org/2005/Atom}updated")
        out.append(
            {
                "title": title,
                "url": link,
                "score": 20.0,
                "source": source_name,
                "source_group": "Lobsters" if source_name == "Lobsters" else "RSS",
                "source_meta": "RSS curated source",
                "published": parse_pub_date(pub),
            }
        )
    return out


def normalize_and_rank(candidates: List[Dict], top_n: int = 10) -> List[Dict]:
    if not candidates:
        return []
    now = dt.datetime.now(dt.timezone.utc)
    max_score = max((c["score"] for c in candidates), default=1.0) or 1.0

    dedup: Dict[str, Dict] = {}
    for c in candidates:
        key = canonicalize_url(c["url"])
        age_hours = max((now - c["published"]).total_seconds() / 3600.0, 0.1)
        recency = max(0.0, 1.0 - min(age_hours / 48.0, 1.0))
        c["final_score"] = 0.75 * (c["score"] / max_score) + 0.25 * recency
        if key not in dedup or c["final_score"] > dedup[key]["final_score"]:
            dedup[key] = c

    ranked = sorted(dedup.values(), key=lambda x: x["final_score"], reverse=True)
    return ranked[:top_n]


def select_with_source_quotas(ranked: List[Dict], per_source: int = 2) -> List[Dict]:
    buckets = ["Hacker News", "Lobsters", "Dev.to", "Reddit", "RSS"]
    picked: List[Dict] = []

    for bucket in buckets:
        candidates = [r for r in ranked if r.get("source_group") == bucket]
        picked.extend(candidates[:per_source])

    # Backfill if some bucket had fewer than quota
    if len(picked) < per_source * len(buckets):
        seen = {canonicalize_url(p["url"]) for p in picked}
        for r in ranked:
            k = canonicalize_url(r["url"])
            if k in seen:
                continue
            picked.append(r)
            seen.add(k)
            if len(picked) >= per_source * len(buckets):
                break

    return picked[: per_source * len(buckets)]


def extract_summary(url: str) -> Dict[str, List[str] | str]:
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        return {"summary": "Could not extract article text automatically.", "takeaways": ["Open original link."]}
    text = trafilatura.extract(downloaded, output_format="txt") or ""
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) < 150:
        return {"summary": "Article text was too short for reliable extraction.", "takeaways": ["Open original link."]}
    sents = split_sentences(text)
    return {
        "summary": " ".join(sents[:3]) if sents else text[:350],
        "takeaways": sents[3:6] if len(sents) > 3 else ["Read full article for details."],
    }


def site_shell(title: str, body: str) -> str:
    css = """
:root { --bg:#f5f7fb; --panel:#ffffff; --text:#0f172a; --muted:#64748b; --line:#e2e8f0; --brand:#3b82f6; --brand2:#8b5cf6; }
@media (prefers-color-scheme: dark){ :root { --bg:#0b1020; --panel:#11172a; --text:#e2e8f0; --muted:#94a3b8; --line:#24324a; --brand:#60a5fa; --brand2:#a78bfa; } }
*{ box-sizing:border-box; }
body { margin:0; background:linear-gradient(180deg,var(--bg),var(--bg)); color:var(--text); font-family: Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial; line-height:1.6; }
.wrap{ max-width:1100px; margin:0 auto; padding:24px 16px 48px; }
.topbar{ display:flex; justify-content:space-between; align-items:center; padding:10px 0 16px; border-bottom:1px solid var(--line); }
.brand{ font-weight:800; letter-spacing:.2px; color:var(--text); text-decoration:none; }
.sub{ color:var(--muted); font-size:14px; }
.hero{ margin:20px 0; padding:20px; border:1px solid var(--line); border-radius:16px; background:linear-gradient(120deg, color-mix(in srgb, var(--brand) 12%, var(--panel)), color-mix(in srgb, var(--brand2) 12%, var(--panel))); }
.hero h1{ margin:0 0 8px; font-size:34px; line-height:1.2; }
.grid{ display:grid; grid-template-columns:1fr; gap:14px; }
.card{ border:1px solid var(--line); border-radius:14px; padding:16px; background:var(--panel); box-shadow: 0 2px 10px rgba(0,0,0,.04); }
.card h2{ margin:0 0 6px; font-size:21px; line-height:1.3; }
.meta{ color:var(--muted); font-size:13px; }
.excerpt{ margin:10px 0 12px; color:var(--text); }
a{ color:var(--brand); text-decoration:none; }
a:hover{ text-decoration:underline; }
.badge{ display:inline-block; font-size:11px; border:1px solid var(--line); border-radius:999px; padding:2px 8px; margin-right:8px; background:color-mix(in srgb, var(--panel) 80%, var(--brand) 20%); }
.actions{ display:flex; gap:14px; font-size:14px; }
footer{ margin-top:28px; color:var(--muted); font-size:13px; border-top:1px solid var(--line); padding-top:14px; }
.back{ font-size:14px; color:var(--muted); }
"""
    return f"<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{html.escape(title)}</title><style>{css}</style></head><body><div class='wrap'>{body}</div></body></html>"


def write_article(day: str, rank: int, story: Dict, summary_data: Dict) -> Path:
    slug = slugify(story['title'])
    path = ARTICLES_DIR / f"{day}-{rank:02d}-{slug}.md"
    md = f"""# {story['title']}

- **Source:** {story['source']}
- **Rank (today):** #{rank}
- **Ranking metrics:** {story['source_meta']}
- **Published (UTC):** {story['published'].strftime('%Y-%m-%d %H:%M')}
- **Original:** {story['url']}

## Summary

{summary_data['summary']}

## Key Takeaways

"""
    for item in summary_data["takeaways"]:
        md += f"- {item}\n"
    md += "\n---\n_Auto-generated daily digest entry._\n"
    path.write_text(md, encoding="utf-8")

    takeaways_html = "".join(f"<li>{html.escape(t)}</li>" for t in summary_data["takeaways"])
    body = f"""
    <div class='topbar'><a class='brand' href='../index.html'>Daily Dev Articles</a><span class='sub'>Curated daily software reading</span></div>
    <div class='hero'>
      <a class='back' href='../index.html'>← Back to all digests</a>
      <h1>{html.escape(story['title'])}</h1>
      <p class='meta'><span class='badge'>{html.escape(story['source'])}</span>Rank #{rank} · {html.escape(story['source_meta'])} · {story['published'].strftime('%Y-%m-%d %H:%M UTC')}</p>
      <div class='actions'><a href='{html.escape(story['url'])}' target='_blank' rel='noopener'>Open original article ↗</a></div>
    </div>
    <div class='card'>
      <h2>Summary</h2>
      <p class='excerpt'>{html.escape(summary_data['summary'])}</p>
      <h2>Key Takeaways</h2>
      <ul>{takeaways_html}</ul>
    </div>
    <footer>Auto-generated daily digest entry.</footer>
    """
    html_path = ARTICLES_DIR / f"{day}-{rank:02d}-{slug}.html"
    html_path.write_text(site_shell(story['title'], body), encoding="utf-8")

    return path


def update_daily_digest(day: str, articles: List[Dict]) -> None:
    digest_path = DOCS / f"{day}.md"
    md = f"# Daily Dev Articles — {day}\n\n"
    md += f"Top {len(articles)} software-development articles sourced from free channels (HN, Lobsters, Dev.to, Reddit, RSS), targeting 2 from each source.\n\n"
    cards = []
    for a in articles:
        md += textwrap.dedent(
            f"""
            ## {a['rank']}. [{a['title']}]({a['article_path']})

            - **Original link:** {a['url']}
            - **Source:** {a['source']}
            - **Ranking metrics:** {a['score_text']}
            - **Quick summary:** {a['summary']}

            """
        )
        article_html_path = a['article_path'].replace('.md', '.html').replace('./', './')
        cards.append(f"<article class='card'><h2>{a['rank']}. <a href='{article_html_path}'>{html.escape(a['title'])}</a></h2><p class='meta'><span class='badge'>{html.escape(a['source'])}</span>{html.escape(a['score_text'])}</p><p class='excerpt'>{html.escape(a['summary'])}</p><div class='actions'><a href='{article_html_path}'>Read summary</a><a href='{html.escape(a['url'])}' target='_blank' rel='noopener'>Original ↗</a></div></article>")
    md += "\n---\nGenerated automatically by GitHub Actions.\n"
    digest_path.write_text(md, encoding="utf-8")

    body = f"<div class='topbar'><a class='brand' href='./index.html'>Daily Dev Articles</a><span class='sub'>Curated daily software reading</span></div><div class='hero'><a class='back' href='./index.html'>← All digests</a><h1>Daily Dev Articles — {day}</h1><p class='meta'>Top {len(articles)} software-development articles from free sources.</p></div><div class='grid'>{''.join(cards)}</div><footer>Generated automatically by GitHub Actions.</footer>"
    (DOCS / f"{day}.html").write_text(site_shell(f"Daily Dev Articles — {day}", body), encoding='utf-8')


def update_index() -> None:
    index_path = DOCS / "index.md"
    daily_files = sorted([p for p in DOCS.glob("20*.md") if p.name != "index.md"], reverse=True)
    lines = ["# Daily Dev Articles", "", "Latest digests:", ""]
    for f in daily_files[:30]:
        lines.append(f"- [{f.stem}](./{f.name})")
    lines += [
        "",
        "## About",
        "",
        "- Sources: HN, Lobsters, Dev.to, Reddit, curated RSS",
        "- Count: 10 articles/day",
        "- Format: one digest + individual markdown pages",
        "",
    ]
    index_path.write_text("\n".join(lines), encoding="utf-8")

    cards = "".join([f"<article class='card'><h2><a href='./{f.stem}.html'>{f.stem}</a></h2><p class='meta'>Daily top 10 software-dev stories.</p><div class='actions'><a href='./{f.stem}.html'>Open digest</a><a href='./{f.stem}.md'>Raw markdown</a></div></article>" for f in daily_files[:30]])
    body = "<div class='topbar'><a class='brand' href='./index.html'>Daily Dev Articles</a><span class='sub'>Curated daily software reading</span></div><div class='hero'><h1>Top Software Articles, Every Day</h1><p class='meta'>A clean dev.to-inspired reading experience built from free high-signal sources.</p></div><div class='grid'>" + cards + "</div><footer>Sources: HN, Lobsters, Dev.to, Reddit, curated RSS.</footer>"
    (DOCS / "index.html").write_text(site_shell("Daily Dev Articles", body), encoding='utf-8')


def main() -> None:
    today = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    DOCS.mkdir(parents=True, exist_ok=True)
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    for stale in ARTICLES_DIR.glob(f"{today}-*.md"):
        stale.unlink(missing_ok=True)

    candidates: List[Dict] = []
    candidates.extend(fetch_hn(limit=20))
    candidates.extend(fetch_devto(limit=12))
    candidates.extend(fetch_reddit(limit_each=10))
    for name, url in RSS_SOURCES:
        candidates.extend(fetch_rss(name, url, limit=8))

    ranked = normalize_and_rank(candidates, top_n=200)
    stories = select_with_source_quotas(ranked, per_source=2)

    article_meta = []
    for i, story in enumerate(stories, start=1):
        summary = extract_summary(story["url"])
        path = write_article(today, i, story, summary)
        article_meta.append(
            {
                "rank": i,
                "title": story["title"],
                "url": story["url"],
                "source": story["source"],
                "score_text": story["source_meta"],
                "summary": summary["summary"],
                "article_path": f"./articles/{path.name}",
            }
        )

    update_daily_digest(today, article_meta)
    update_index()
    print(json.dumps({"date": today, "count": len(article_meta), "source": "free-multi-source"}, indent=2))


if __name__ == "__main__":
    main()
