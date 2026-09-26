# Push images to Vercel Container Registry from GitHub Actions

- **Source:** Vercel
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-26 17:42
- **Original:** https://vercel.com/changelog/vcr-login-github-action

## Summary

You can now push container images from GitHub Actions to Vercel Container Registry (VCR) without storing long-lived registry credentials. The new vercel/vcr-action/login action authenticates your workflow using GitHub OIDC. It exchanges the workflow’s OIDC token for a short-lived Vercel access token, then uses that token to log in to vcr.vercel.com.

## Key Takeaways

- When the job ends, the action logs out and revokes the Vercel token.
- To start: - Create an OIDC policy on your Vercel team that matches the GitHub repository and workflow, and grants read-write access to VCR.
- - Store your Vercel team ID as a GitHub repo variable, for example VERCEL_TEAM_ID , along with the team slug, project slug, and repo name used in the image tag.

---
_Auto-generated daily digest entry._
