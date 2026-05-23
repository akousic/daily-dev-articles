# That one time I used Go panics for flow control

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-23 04:57
- **Original:** https://noncrab.net/posts/panic-as-flow-control/

## Summary

How our protagonist discovered that a key service that powers our support was absurdly vulnerable to overload, and what we did to fix it. Part of our support infrastructure at work is an in-memory datastore, that allows us to query our outstanding support work over various dimensions, such as work type, whether it's been put on hold for some reason, etc. It's functionally equivalent to a single table in an SQL database, where you have a single dataset, boolean filters and configurable sorting.

## Key Takeaways

- At work, we have an in-memory datastore that powers part of our support infrastructure.
- Its kind of analgous to having bitmap filters with post-hoc filtering, so any use of sort/limit will sort the entire result set.
- And the key part here, is that the result sets can be large enough that sorts can take one or two seconds.

---
_Auto-generated daily digest entry._
