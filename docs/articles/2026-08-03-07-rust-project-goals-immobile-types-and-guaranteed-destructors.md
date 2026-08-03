# Rust project goals: Immobile types and guaranteed destructors

- **Source:** Hacker News
- **Rank (today):** #7
- **Ranking metrics:** HN score 180
- **Published (UTC):** 2026-08-03 06:42
- **Original:** https://github.com/rust-lang/rust-project-goals/blob/main/src/2026/move-trait.md

## Summary

| Metadata | | |---|---| | Point of contact | @lcnr | | Status | Accepted | | What and why | Let types opt out of being moved or forgotten, enabling scoped spawn, async drop, and pin-by-default | | Timespan | 2026-2027 | | Roadmap | Just add async | | Roadmap | Rust for Linux | | Tracking issue | [#635] | | Other tracking issues | [rust-lang/rust#149607] | | Zulip channel | #t-lang/move-trait | | [types] champion | @lcnr | | [lang] champion | @jackh726 | We propose to introduce new traits that describe what operations are possible on a type. Today Rust assumes all types can be moved (relocated in memory) and forgotten (via mem::forget). We will introduce traits like Move and Forget that make these capabilities explicit, allowing types to opt out.

## Key Takeaways

- This follows the precedent set by the Sized hierarchy work, which relaxes the assumption that all types have a compile-time-known size.
- We will implement MVPs in the compiler, write RFCs, and validate viability through real-world testing in the Linux Kernel.
- Rust has historically assumed that all values can be moved (relocated in memory) and forgotten (via mem::forget, without running destructors).

---
_Auto-generated daily digest entry._
