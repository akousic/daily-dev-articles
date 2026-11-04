# How to speed up the Rust compiler in November 2026

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-04 08:05
- **Original:** https://nnethercote.github.io/2026/11/04/how-to-speed-up-the-rust-compiler-in-november-2026.html

## Summary

How to speed up the Rust compiler in November 2026 My first month working on Rust compiler performance for Hexcat is over and it’s time to see some of what’s happened since my last post. Spans Spans are a critical data structure in the Rust compiler. Every AST, HIR, and MIR node carries a span.

## Key Takeaways

- Each span has four fields recording the following.
- - A source location (lo and hi).
- A crate’s source files are concatenated into a single buffer, and these are indices into that buffer.

---
_Auto-generated daily digest entry._
