# In defense of lock poisoning in Rust (2025)

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-26 05:51
- **Original:** https://sunshowers.io/posts/on-poisoning/

## Summary

In defense of lock poisoning in Rust Table of contents There’s recently been some discussion about the benefits and downsides of lock (mutex) poisoning in Rust, spurred by a recent proposal to make the default mutex non-poisoned, i.e. silently unlock on panic (see also, recent discussion on Hacker News). As a passionate defender of lock poisoning, I thought I’d gather and write about my thoughts on this matter.

## Key Takeaways

- To summarize, I believe: - Unexpected cancellations in critical sections cause real harm to system correctness.
- - Lock poisoning is an important part of ensuring the correctness of critical sections in Rust.
- - Poisoning applies more generally than mutexes, and providing an easy way to track that (via e.g.

---
_Auto-generated daily digest entry._
