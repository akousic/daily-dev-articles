# Malicious Rust crate Arrayref runs a build-time payload

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 532
- **Published (UTC):** 2026-08-20 13:23
- **Original:** https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/

## Summary

On this page Summary On August 20, 2026, a compromised release of the popular Rust crate arrayref appeared on crates.io. Version 0.3.10 added a dependency on a typosquatted crate called proc-macro1, whose build script downloads and runs a remote binary while a project compiles. The code runs at build time, so simply compiling a project that pulled the bad versions is enough to trigger it.

## Key Takeaways

- The crates.io team has since removed the malicious versions.
- Packages involved The genuine arrayref and append-only-vec crates are maintained by droundy, whose account appears to have been compromised.
- The corresponding GitHub repositories are no longer available.

---
_Auto-generated daily digest entry._
