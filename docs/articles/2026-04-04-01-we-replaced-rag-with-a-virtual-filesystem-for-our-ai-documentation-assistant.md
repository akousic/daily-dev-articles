# We replaced RAG with a virtual filesystem for our AI documentation assistant

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 350
- **Published (UTC):** 2026-04-02 18:24
- **Original:** https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant

## Summary

How we built a virtual filesystem for our Assistant March 24, 2026 Dens Sumesh Engineering Share this article RAG is great, until it isn't. Our assistant could only retrieve chunks of text that matched a query. If the answer lived across multiple pages, or the user needed exact syntax that didn't land in a top-K result, it was stuck.

## Key Takeaways

- We wanted it to explore docs the way you'd explore a codebase.
- Agents are converging on filesystems as their primary interface because grep , cat , ls , and find are all an agent needs.
- If each doc page is a file and each section is a directory, the agent can search for exact strings, read full pages, and traverse the structure on its own.

---
_Auto-generated daily digest entry._
