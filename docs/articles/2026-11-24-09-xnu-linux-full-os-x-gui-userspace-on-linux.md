# XNU Linux: Full OS X GUI Userspace on Linux

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 601
- **Published (UTC):** 2026-11-23 03:49
- **Original:** https://github.com/AFK-surf/xnulinux

## Summary

Run macOS userspace on Linux by loading the macOS kernel into it. xnulinux builds XNU, the open-source kernel of macOS, from Apple's published sources and runs it as a loadable kernel module (xnu.ko) inside an unmodified arm64 Linux kernel. The hosted XNU drives the CPU and MMU directly, so macOS processes run natively next to Linux processes on the same CPUs, with no hypervisor between them.

## Key Takeaways

- Linux lends XNU its memory, timers, files, network and GPU through a small interface module (fki.ko).
- With a stock Ubuntu kernel, insmod xnu.ko boots a macOS 27 system disk made by Apple's own installer to the desktop: loginwindow, WindowServer, Dock, Finder, Safari and Chrome.
- One system, two userspaces.

---
_Auto-generated daily digest entry._
