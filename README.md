# Daily Dev Articles

Auto-generated daily digest of top software-development articles.

## What it does

- Uses **Hacker News top stories** as source
- Filters for software/developer-relevant links
- Summarizes the top 5 articles daily
- Writes:
  - `docs/YYYY-MM-DD.md` (daily digest)
  - `docs/articles/YYYY-MM-DD-*.md` (one markdown page per article)

## Automation

Workflow: `.github/workflows/daily-digest.yml`

- Scheduled daily at `13:05 UTC`
- Can also run manually with **Run workflow** in GitHub Actions

## Static site hosting (GitHub Pages)

1. Open repo **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main`, folder: `/docs`
4. Save

Site URL:

`https://akousic.github.io/daily-dev-articles/`
