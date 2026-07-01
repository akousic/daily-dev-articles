# Asahi Linux 7.1 Progress Report

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 429
- **Published (UTC):** 2026-07-01 10:07
- **Original:** https://asahilinux.org/2026/06/progress-report-7-1/

## Summary

Progress Report: Linux 7.1 Linux 7.1 is now here, and of course with it comes another progress report. We’ve got M3 progress, Apple bugs, and more! Welcome back Master Boot Record When you long-press the power button on your Mac to bring up the boot picker (or use the Startup Disk application), what you see listed as Asahi is not actually the partition with the operating system on it.

## Key Takeaways

- Apple’s boot tooling will only work with what it considers to be a “valid” macOS installation inside an APFS container.
- So that we can use Apple’s bootloader and avoid needing users to run commands from Recovery every time they want to use Asahi, the Asahi Installer creates a small APFS container (2.5 GB) with just enough of macOS on it to convince Apple’s tools that it is a bootable installation of macOS with m1n1 as its kernel.
- This arrangement worked completely unchanged from macOS 12 to macOS 26, and Apple even fixed a couple of bugs in their tools that are only encountered when attempting to boot raw binaries that are not a real XNU kernel.

---
_Auto-generated daily digest entry._
