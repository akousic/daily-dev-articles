# I built a garbage collector for Rust (2023)

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-22 09:49
- **Original:** https://claytonwramsey.com/blog/dumpster/

## Summary

If carcinization happens when languages evolve to be more like Rust, then what do you call it when Rust evolves to be more like Java? Over this summer, I’ve had a decent amount of time to kill. What better way to spend a beautiful hot summer than sitting inside, staring at core dumps in a supposedly memory-safe language?

## Key Takeaways

- I built a garbage collector - in short, a piece of software that manages allocations for another, more exciting piece of software.
- The cool part: I made it in Rust, for Rust - a language designed to eliminate garbage collection and which provides few facilities for making it work properly.
- Not only that, I managed to make my garbage collector work with relatively few compromises, which I’ll describe in further detail lower down.

---
_Auto-generated daily digest entry._
