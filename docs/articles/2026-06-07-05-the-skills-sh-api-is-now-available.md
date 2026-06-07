# The skills.sh API is now available

- **Source:** Vercel
- **Rank (today):** #5
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-07 15:26
- **Original:** https://vercel.com/changelog/the-skills-sh-api-is-now-available

## Summary

1 min read The skills.sh API is now available. Authenticate with your project's Vercel OIDC token and start querying more than 600,000 skills from across the open-source ecosystem. Search for skills, pull detailed info on any one, check its security audit, and more.

## Key Takeaways

- Vercel issues a short-lived token scoped to your team and project, rotated automatically, so there's no long-lived secret to leak or rotate.
- On each request, skills.sh verifies the token and applies a rate limit of 600 requests per minute per team and project.
- import { getVercelOidcToken } from '@vercel/oidc'; const token = await getVercelOidcToken();const res = await fetch('https://skills.sh/api/v1/skills?per_page=10', { headers: { Authorization: `Bearer ${token}` },}); Fetch skills with your project's Vercel OIDC token Read the skills.sh API documentation to get started.

---
_Auto-generated daily digest entry._
