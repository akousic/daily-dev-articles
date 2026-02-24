# Daily Dev Articles

Auto-generated daily digest of top software-development articles.

## What it does

- Uses **X API** (preferred) to fetch recent tech posts with links
- Ranks by engagement score:
  - `score = likes + 2*reposts + 1.5*replies + 2*quotes`
- Keeps top 10 linked articles and summarizes them
- Falls back to Hacker News if X token is missing or X request fails
- Writes:
  - `docs/YYYY-MM-DD.md` (daily digest)
  - `docs/articles/YYYY-MM-DD-*.md` (one markdown page per article)

## Automation

Workflow: `.github/workflows/daily-digest.yml`

- Scheduled daily at `13:05 UTC`
- Can also run manually with **Run workflow** in GitHub Actions

## Configure X API securely

1. Go to GitHub repo → **Settings → Secrets and variables → Actions**
2. Add secret:
   - `X_BEARER_TOKEN` = your X API bearer token
3. (Optional) Add repository variable:
   - `X_TECH_QUERY` = custom query string

**Important security rules**
- Never hardcode keys in code
- Never commit `.env` or token files
- Keep token only in GitHub Secrets
- Rotate token if accidentally exposed

## Static site hosting (GitHub Pages)

1. Open repo **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main`, folder: `/docs`
4. Save

Site URL:

`https://akousic.github.io/daily-dev-articles/`
