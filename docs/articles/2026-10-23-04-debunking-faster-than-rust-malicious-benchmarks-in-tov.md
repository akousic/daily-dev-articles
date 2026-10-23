# Debunking "Faster than Rust": Malicious Benchmarks in Tov

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-23 02:44
- **Original:** https://blog.fyralabs.com/debunking-faster-than-rust-malicious-benchmarks-in-tov/

## Summary

Debunking "Faster than Rust": Malicious Benchmarks in Tov Tov is a programming language that claims to perform significantly better than Rust. This blog post debunks tricks used in their unfair benchmarks. Tov is a new programming language marketed to be "[a] programming language for coding agents.

## Key Takeaways

- It reads like TypeScript and builds native binaries that beat Rust's." Benchmarks in their Git repository show that they perform better than Rust, in some cases over 10× better.
- However, they also briefly mentioned the internals of Tov: Tov is a compiler.
- It checks the TypeScript your agent wrote, writes it out as C and hands that to clang, so what you ship is one native binary with nothing to install next to it.

---
_Auto-generated daily digest entry._
