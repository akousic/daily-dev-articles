# The time the x86 emulator team found code so bad they fixed it during emulation

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 451
- **Published (UTC):** 2026-06-16 04:46
- **Original:** https://devblogs.microsoft.com/oldnewthing/20260615-00/?p=112419

## Summary

During an exchange of war stories, a colleague of mine told one from back in the days when Windows included a processor emulator for x86-32 on systems that natively ran some other processor. (This has happened many times. And no, I don’t know which processor this particular story applied to.) This particular emulator employed binary translation, generating native code to perform the equivalent operations of the original x86-32 code.

## Key Takeaways

- This offered a significant performance improvement over emulation via interpreter.
- You can imagine that x86-32 is just a bytecode, and the emulator is a JIT compiler.
- Anyway, my colleague found that there was one program that needed to allocate around 64KB of memory on the stack and initialize it.

---
_Auto-generated daily digest entry._
