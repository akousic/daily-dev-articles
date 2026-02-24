# Daily Dev Articles

Auto-generated daily digest of top software-development articles.

## What it does

Uses only free sources:
- Hacker News
- Lobsters
- Dev.to
- Reddit (`r/programming`, `r/webdev`, `r/MachineLearning`)
- Curated engineering RSS feeds (Cloudflare, Stripe, Vercel, InfoQ, Changelog)

Then it:
- Aggregates candidates
- De-duplicates links
- Ranks by source score + recency
- Publishes **Top 10** each day

Output files:
- `docs/YYYY-MM-DD.md` (daily digest)
- `docs/articles/YYYY-MM-DD-*.md` (one markdown page per article)

## Automation

Workflow: `.github/workflows/daily-digest.yml`

- Scheduled daily at `13:05 UTC`
- Can run manually via **Run workflow**

## Static site hosting (GitHub Pages)

1. Repo **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main`, folder: `/docs`

Site URL:

`https://akousic.github.io/daily-dev-articles/`
