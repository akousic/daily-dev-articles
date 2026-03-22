# The three pillars of JavaScript bloat

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 389
- **Published (UTC):** 2026-03-22 02:04
- **Original:** https://43081j.com/2026/03/three-pillars-of-javascript-bloat

## Summary

The Three Pillars of JavaScript Bloat Over the last couple of years, we’ve seen significant growth of the e18e community and a rise in performance focused contributions because of it. A large part of this is the “cleanup” initiative, where the community has been pruning packages which are redundant, outdated, or unmaintained. One of the most common topics that comes up as part of this is “dependency bloat” - the idea that npm dependency trees are getting larger over time, often with long since redundant code which the platform now provides natively.

## Key Takeaways

- In this post, I want to briefly look at what I think are the three main types of bloat in our dependency trees, why they exist, and how we can start to address them.
- Older runtime support (with safety and realms) The graph above is a common sight in many npm dependency trees - a small utility function for something which seems like it should be natively available, followed by many similarly small deep dependencies.
- So why is this a thing?

---
_Auto-generated daily digest entry._
