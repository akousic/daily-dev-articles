# How close can pure functional programming get to C?

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 209
- **Published (UTC):** 2026-10-24 03:43
- **Original:** https://rtfeldman.com/fp-vs-c

## Summary

How close can pure FP get to C? October 22, 2026 In Why Lean is Faster Than Rust, the author shares an impressive result: a DEFLATE compression library written in Lean 4, a functional programming language and proof assistant, outperforming an equivalent Rust package that crates.io says has been downloaded over a billion times. From the article: lean-zip beats every single compression level miniz_oxide provides, i.e.

## Key Takeaways

- we're capable of providing the same compression at higher throughput.
- At its fastest setting we're 15% quicker and the output is 8.8% smaller.
- However, the article also notes that while they managed to surpass Rust's miniz_oxide, they were no match for the end boss of DEFLATE performance: libdeflate, written in C.

---
_Auto-generated daily digest entry._
