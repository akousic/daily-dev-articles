# Hardware backdoors in some x86 CPUs

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 221
- **Published (UTC):** 2026-08-08 07:04
- **Original:** https://github.com/xoreaxeaxeax/rosenbridge

## Summary

: hardware backdoors in x86 CPUs github.com/xoreaxeaxeax/rosenbridge // domas // @xoreaxeaxeax project:rosenbridge reveals a hardware backdoor in some desktop, laptop, and embedded x86 processors. The backdoor allows ring 3 (userland) code to circumvent processor protections to freely read and write ring 0 (kernel) data. While the backdoor is typically disabled (requiring ring 0 execution to enable it), we have found that it is enabled by default on some systems.

## Key Takeaways

- This repository contains utilities to check if your processor is affected, close the backdoor if it is present, and the research and tools used to discover and analyze the backdoor.
- The rosenbridge backdoor is a small, non-x86 core embedded alongside the main x86 core in the CPU.
- It is enabled by a model-specific-register control bit, and then toggled with a launch-instruction.

---
_Auto-generated daily digest entry._
