# 11 year old unsoundness bugs found in Rust borrow checker

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 606
- **Published (UTC):** 2026-10-13 10:27
- **Original:** https://github.com/rust-lang/rust/issues/164250

## Summary

Repository navigation struct's lifetime requirements can be bypassed via covariant field assignment #164250 Description Note Given that this issue has been shared online and is currently getting quite a few visitors, here's some additional context. Rust's type system is intended to prevent memory unsafety. Upholding this promise is something we take very seriously, which is why we've been working on things like the next-generation trait solver, the region constraint rework, and more generally Project Zero.

## Key Takeaways

- It is a large priority of the Types Team to fix all type system unsoundnesses and to work towards there being a solid foundation to minimize the risk of unknown ones.
- This bug is a P-high issue and would have been P-critical regardless of whether people encountered it in the wild.
- The reason that it is "only P-high" is that it's 11 years old.

---
_Auto-generated daily digest entry._
