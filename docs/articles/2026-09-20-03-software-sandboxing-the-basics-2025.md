# Software sandboxing: The basics (2025)

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-20 09:13
- **Original:** https://blog.emilua.org/2025/01/12/software-sandboxing-basics/

## Summary

Diving into the territory of software sandboxing is diving into mostly uncharted territory. The necessary pieces to implement good sandboxing in your software are scattered all-around and the pioneers haven’t yet gathered enough knowledge into an unified mappa mundi that can guide new sailors through some well understood safe routes. In this blog post I’ll offer my own share of experiences that I have acquired while working on sandboxing support for Emilua.

## Key Takeaways

- Writing style will suffer a little because I’ll err on the side of repeating myself too much to avoid any misunderstandings.
- | | Do keep in mind that some Lua code samples here require the unreleased Emilua 0.11 (just grab a recent commit from the repo’s development branch).
- | First, let’s get some informal (but useful) definition for sandboxing just to make sure we’re on the same page.

---
_Auto-generated daily digest entry._
