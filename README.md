# Daily Dev Articles

Auto-generated daily digest of the top 5 software-development articles.

## What it does

- Pulls top external stories from Hacker News each day
- Extracts article text and creates a short summary for each
- Writes:
  - `docs/YYYY-MM-DD.md` (daily digest)
  - `docs/articles/YYYY-MM-DD-*.md` (one markdown page per article)
- Commits updates via GitHub Actions

## Automation

Workflow: `.github/workflows/daily-digest.yml`

- Scheduled daily at `13:05 UTC`
- Can also run manually with **Run workflow** in GitHub Actions

## Static site hosting (GitHub Pages)

1. Open repo **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main`, folder: `/docs`
4. Save

Then your site will be available at:

`https://akousic.github.io/daily-dev-articles/`
