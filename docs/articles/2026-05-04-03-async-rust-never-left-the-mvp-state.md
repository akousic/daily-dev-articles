# Async Rust never left the MVP state

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-04 09:26
- **Original:** https://tweedegolf.nl/en/blog/237/async-rust-never-left-the-mvp-state

## Summary

Async Rust never left the MVP state I love me some async Rust! It's amazing how we can write executor agnostic code that can run concurrently on huge servers and tiny microcontrollers. But especially on those tiny microcontrollers we notice that async Rust is far from the zero cost abstractions we were promised.

## Key Takeaways

- That's because every byte of binary size counts and async introduces a lot of bloat.
- This bloat exists on desktops and servers as well, but it's much less noticable when you have substantially more memory and compute available.
- I've previously explained some work-arounds for this issue, but would much prefer to get to the root of the problem, and work on improving async bloat in the compiler.

---
_Auto-generated daily digest entry._
