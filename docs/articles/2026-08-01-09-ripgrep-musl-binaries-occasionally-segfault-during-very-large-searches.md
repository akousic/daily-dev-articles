# RipGrep musl binaries occasionally segfault during very-large searches

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 114
- **Published (UTC):** 2026-08-01 12:34
- **Original:** https://github.com/BurntSushi/ripgrep/issues/3494

## Summary

- - Notifications You must be signed in to change notification settings - Fork 2.7k x86_64-unknown-linux-musl binaries occasionally segfault during very-large searches #3494 Description Please tick this box to confirm you have reviewed the above. - I have a different issue. What version of ripgrep are you using?

## Key Takeaways

- ripgrep 15.2.0 (rev e89fff8) features:+pcre2 simd(compile):+SSE2,-SSSE3,-AVX2 simd(runtime):+SSE2,+SSSE3,+AVX2 PCRE2 10.45 is available (JIT is available) How did you install ripgrep?
- I originally encountered this bug in the rg bundled with OpenAI Codex.
- That binary is byte-for-byte identical with the one in https://github.com/BurntSushi/ripgrep/releases/download/15.2.0/ripgrep-15.2.0-x86_64-unknown-linux-musl.tar.gz and I've reproduced the bug from that independently of any Codex dependency.

---
_Auto-generated daily digest entry._
