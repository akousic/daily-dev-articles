# krabby: making a fast Rust compiler

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-05 17:22
- **Original:** https://bal-e.org/speed/krabby/

## Summary

Rust is my favorite programming language, but its compiler is noticeably slow. There are plenty of incredibly talented people working on improving rustc , and compilation speed is important to them too. At this point, if a change to a single function could noticeably improve performance, it’s already implemented.

## Key Takeaways

- Meaningful improvements are now coming from changes to APIs and data structures, which are significantly harder to evolve.
- In a large codebase like rustc , where many features are worked on simultaneously and there is a need for stability, making these large-scale changes is effectively impossible.
- I’m deeply appreciative of the people who find ways to slowly and incrementally pushing these changes through, but I want to take a different approach.

---
_Auto-generated daily digest entry._
