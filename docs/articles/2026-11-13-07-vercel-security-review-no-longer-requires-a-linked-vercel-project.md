# Vercel Security Review no longer requires a linked Vercel project

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-13 20:49
- **Original:** https://vercel.com/changelog/vercel-security-review-no-longer-requires-a-linked-vercel-project

## Summary

You can now scan code changes for vulnerabilities with Vercel Security Review in GitHub repositories that have not yet been linked to a Vercel project. By default, Security Review covers all unlinked repositories the Vercel GitHub App can access in a connected GitHub account. You can limit coverage to selected connected accounts or individual repositories in Agent settings.

## Key Takeaways

- Once enabled, each push to a covered repository automatically triggers a review of its code changes.
- Security Review checks commits directly in repositories with Security Review enabled, without requiring a Vercel project or deployment.
- When a push creates a deployment for a linked project with Security Review enabled, the review uses the additional project and deployment context.

---
_Auto-generated daily digest entry._
