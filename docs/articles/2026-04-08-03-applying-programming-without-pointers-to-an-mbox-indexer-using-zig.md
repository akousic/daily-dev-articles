# Applying "Programming Without Pointers" to an mbox indexer using Zig

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-08 02:40
- **Original:** https://simonhartcher.com/posts/2026-04-08-applying-programming-without-pointers-to-an-mbox-indexer-using-zig

## Summary

Programming without pointers I must have watched Programming without pointers (or PWP) roughly 10 times by now. In garbage collected languages where memory allocations are mostly invisible, it can be so easy to forget that memory allocations are often poison for high performance software. In the video, Zig’s creator Andrew Kelley shows us how to structure our programs so that they only need to do minimal memory allocations, reducing the number of total pointers that we need to manage.

## Key Takeaways

- Memory allocations are expensive, so reducing them can improve the overall complexity of our programs.
- I think that the pattern of PWP can make the code a little bit more complex if you’re not used to writing code that way.
- But once you’re used to it, I think that complexity can go away as you’ll recognise the pattern when you see it.

---
_Auto-generated daily digest entry._
