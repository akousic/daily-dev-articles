# Linux 7.3 improves performance when running out of vRAM

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 349
- **Published (UTC):** 2026-08-18 07:51
- **Original:** https://pixelcluster.dev/VRAM-Overcommit/

## Summary

Earlier this year, I blogged about work I did to improve VRAM management for games. Now, after many months of floating around in mailing lists, the kernel patches are finally merged upstream and queued for Linux 7.3! To celebrate, let’s look a bit deeper at one sentence I wrote in my previous post: [Games] should perform much more stable - as long as the game itself doesn’t use more VRAM than you actually have.

## Key Takeaways

- So, one may ask: What if they do, in fact, use more VRAM than you actually have?
- Typical expectations for this seem to be that once this happens you’re pretty much screwed.
- Games will start crashing left and right, performance plummets to unplayable levels, a good gaming experience becomes impossible.

---
_Auto-generated daily digest entry._
