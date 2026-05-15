# linux 0-day, access root-owned files as an unprivileged user

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-14 20:14
- **Original:** https://github.com/0xdeadbeefnetwork/ssh-keysign-pwn/

## Summary

"It is a fearful thing to fall into the hands of the living God." — Hebrews 10:31 Read root-owned files as an unprivileged user. Pre-31e62c2ebbfd kernels (everything in stable as of 2026-05-14). __ptrace_may_access() skips the dumpable check when task->mm == NULL .

## Key Takeaways

- do_exit() runs exit_mm() before exit_files() — no mm, fds still there.
- pidfd_getfd(2) succeeds in that window when the caller's uid matches the target's.
- Reported by Qualys, fixed by Linus 2026-05-14.

---
_Auto-generated daily digest entry._
