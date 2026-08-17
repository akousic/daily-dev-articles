# Writing a Fast Compiler

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-08-17 06:13
- **Original:** https://tibleiz.net/blog/2024-02-04-writing-a-fast-compiler.html

## Summary

Writing a Fast Compiler 2024-02-04 I'm going to describe the various tricks I used to write fast compilers for my programming languages. By fast compilation, I mean compiling at least 500.000 lines of code per second (excluding blank lines and comments) on a single CPU core. You may argue that compilation time is not important.

## Key Takeaways

- After all, once released, who cares that a program took hours to build; as users, we only want it to work and to work fast.
- It's like complaining that the last Pixar movie took days for the final rendering.
- However it can severely affect the development cycle and make developers angry.

---
_Auto-generated daily digest entry._
