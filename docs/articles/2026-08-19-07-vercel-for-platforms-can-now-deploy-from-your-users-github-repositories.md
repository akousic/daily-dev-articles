# Vercel for Platforms can now deploy from your users' GitHub repositories

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-08-19 14:40
- **Original:** https://vercel.com/changelog/vercel-for-platforms-can-now-deploy-from-your-users-github-repositories

## Summary

Teams building on Vercel for Platforms can now create deployments directly from their users' GitHub repositories, without requiring them to install the Vercel GitHub App. When creating a deployment, pass a gitAccessToken alongside gitSource. Vercel uses the token to retrieve the source and build the deployment.

## Key Takeaways

- Tokens should be read-only, scoped to the requested repository, and valid for 24 hours or less.
- Vercel temporarily stores the token in encrypted form so source retrieval can complete.
- The token is never stored on the deployment.

---
_Auto-generated daily digest entry._
