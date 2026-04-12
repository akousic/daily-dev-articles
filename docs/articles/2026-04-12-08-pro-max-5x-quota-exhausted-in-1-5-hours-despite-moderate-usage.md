# Pro Max 5x Quota Exhausted in 1.5 Hours Despite Moderate Usage

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 249
- **Published (UTC):** 2026-04-12 13:15
- **Original:** https://github.com/anthropics/claude-code/issues/45756

## Summary

Preflight Checklist What's Wrong? Pro Max 5x Quota Exhausted in 1.5 Hours Despite Moderate Usage Summary On a Pro Max 5x (Opus) plan, quota resets at a fixed interval. After reset, with moderate usage (mostly Q&A, light development), quota was exhausted within 1.5 hours.

## Key Takeaways

- Prior to reset, 5 hours of heavy development (multi-file implementation, graphify pipeline, multi-agent spawns) consumed the previous quota window — but that was expected given the workload.
- The post-reset exhaustion was not.
- Investigation reveals the likely root cause: cache_read tokens appear to count at full rate against the rate limit, negating the cost benefit of prompt caching for quota purposes.

---
_Auto-generated daily digest entry._
