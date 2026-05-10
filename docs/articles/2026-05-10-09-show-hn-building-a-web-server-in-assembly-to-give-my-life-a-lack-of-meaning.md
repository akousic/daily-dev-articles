# Show HN: Building a web server in assembly to give my life (a lack of) meaning

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 339
- **Published (UTC):** 2026-05-10 03:01
- **Original:** https://github.com/imtomt/ymawky

## Summary

This is ymawky (yuh maw kee), a web server written entirely in ARM64 assembly. ymawky is a syscall-only, no libc, fork-per-connection web server written by hand. While it is developed for MacOS, I've tried to make it as portable as possible -- however, it's likely you will still need to make some (hopefully minor) Significant tweaks to get this to run on Linux/other Unix systems.

## Key Takeaways

- See Implementation Notes for more details.
- Requires Xcode Command Line Tools.
- Install with xcode-select --install .

---
_Auto-generated daily digest entry._
