# The Goose Programming Language

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 522
- **Published (UTC):** 2026-10-24 19:06
- **Original:** https://aardappel.github.io/goose/

## Summary

The Goose Programming Language A memory-safe systems language with no heap allocator, garbage collector, or lifetime annotations. In this repository's benchmarks, Goose runs faster than C++ and Rust while using less memory. Tutorial · Reference · Specification · Packages · Samples · Benchmarks · Standard library Goose has syntax familiar to C and Rust programmers, but there is no heap.

## Key Takeaways

- Every dynamic value lives inline on data stacks managed by the compiler.
- Growth advances a pointer, and memory is freed when its scope ends.
- The language's type and lifetime rules make this memory model safe to use.

---
_Auto-generated daily digest entry._
