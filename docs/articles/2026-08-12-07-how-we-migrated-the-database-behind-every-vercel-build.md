# How we migrated the database behind every Vercel build

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-08-12 15:04
- **Original:** https://vercel.com/blog/how-we-migrated-the-database-behind-every-vercel-build

## Summary

Every build on Vercel starts in the build warm pool, which is a set of standby containers that let builds begin without waiting for new compute. The pool runs on state that tracks which containers are ready, the tokens each one uses to authenticate, and the mapping that ties every running build back to the deployment that gets billed for it. When we built the pool, we put all of that in Redis, which was fast and made sense at the time.

## Key Takeaways

- Over the years, though, that state turned into a liability.
- Tokens and container statuses can be rebuilt if they get lost, but the billing mappings can't, and all of it was sitting in a store that we ran as an ephemeral cache.
- That state needed to live somewhere durable, which is why we decided to migrate it to DynamoDB.

---
_Auto-generated daily digest entry._
