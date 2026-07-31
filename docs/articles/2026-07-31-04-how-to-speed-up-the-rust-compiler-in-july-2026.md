# How to speed up the Rust compiler in July 2026

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-31 00:46
- **Original:** https://nnethercote.github.io/2026/07/31/how-to-speed-up-the-rust-compiler-in-july-2026.html

## Summary

How to speed up the Rust compiler in July 2026 My last post on the Rust compiler’s performance was in December 2025. Let’s see what has happened since then. Overall progress The measurements for the period 2025-12-03 to 2026-07-29 can be seen here.

## Key Takeaways

- The mean wall-time reduction was a healthy 5.59%.
- Around half of this was due to some huge recent improvements in rustdoc, which saw a mean wall-time reduction of 37.92%!
- With the rustdoc changes excluded, the mean wall-time change was 2.90%, which is still a good result.

---
_Auto-generated daily digest entry._
