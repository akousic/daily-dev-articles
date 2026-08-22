# Rust Glancer: Rust LSP using 100x less RAM

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 323
- **Published (UTC):** 2026-08-21 19:51
- **Original:** https://rust-glancer.github.io/blog/hello-world/

## Summary

I want to present a project that I've been working on for the past 4 months: an alternative Rust LSP implementation that is built with a focus on low memory usage. It has two main features: - It can use very little memory (target <100mb for reasonable projects). There are caveats, these are described below.

## Key Takeaways

- - It allows immediate indexing after restart: if your project was indexed, restarting the editor will not require re-indexing.
- Note: throughout this video, the used RAM remained under 100mb These features make Rust Glancer suitable for the older computers: I have tested it on my old MacBook Pro M1 2020 with 8GB RAM, and it was pretty good.
- | Machine | LSP | Base indexing (engine usable) | Full indexing | |---|---|---|---| | MacBook Pro M4 Max, 36GB (2025) | Rust Glancer | 5 seconds | 8 seconds | | MacBook Pro M4 Max, 36GB (2025) | rust-analyzer | 6 seconds | 13 seconds | | MacBook Pro M1, 8GB (2020) | Rust Glancer | 6 seconds | 9 seconds | | MacBook Pro M1, 8GB (2020) | rust-analyzer | 7 seconds | 14 seconds | As you can imagine, 4 months is not a lot of time for a project as big as a Rust LSP.

---
_Auto-generated daily digest entry._
