# Bugs Rust won't catch

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 492
- **Published (UTC):** 2026-04-29 02:19
- **Original:** https://corrode.dev/blog/bugs-rust-wont-catch/

## Summary

In April 2026, Canonical disclosed 44 CVEs in uutils, the Rust reimplementation of GNU coreutils that ships by default since 25.10. Most of them came out of an external audit commissioned ahead of the 26.04 LTS. I read through the list and thought there’s a lot to learn from it.

## Key Takeaways

- What’s notable is that all of these bugs landed in a production Rust codebase, written by people who knew what they were doing, and none of them were caught by the borrow checker, clippy lints, or cargo audit.
- I’m not writing this to criticize the uutils team.
- Quite the contrary; I actually want to thank them for sharing the audit results in such detail so that we can all learn from them.

---
_Auto-generated daily digest entry._
