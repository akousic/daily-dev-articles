# Benchmarking Opus 5 on SlopCodeBench

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 373
- **Published (UTC):** 2026-07-27 22:37
- **Original:** https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-opus-5-on-slop-code-bench.md

## Summary

I've written before something along the lines of: That wasn't entirely true. I love nothing more than burying a good lede. Last Friday I dug into SlopCodeBench, a new-ish (March 2026) long-horizon coding benchmark from @GOrlanski's lab at UW Madison.

## Key Takeaways

- It addresses the thing that bothers me most about coding benchmarks - that even "larger" more complex benchmarks still divulge the whole problem up front: In contrast, each challenge in SlopCodeBench has multiple "checkpoints" - the model doesn't know the whole problem up front, it has to evolve the codebase over time as new requirements are divulged.
- What's cool about this benchmark is that it is unsaturated - at the time of running, the best models available, GPT-5.4 and Opus 4.6, got 11% and 17% strict pass rates, respectively.
- On Friday I ran three claude models (Opus 4.8, Sonnet 5, and Opus 5) through a subset of SlopCodeBench and watched it live for six hours.

---
_Auto-generated daily digest entry._
