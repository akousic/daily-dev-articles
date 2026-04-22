# wsl9x: Windows 9x subsystem for Linux

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-22 01:33
- **Original:** https://codeberg.org/hails/wsl9x

## Summary

- C 64% - Assembly 35.5% - Makefile 0.5% | bin | || | ddk | || | inc | || | vxd | || | wsl | || | .envrc.example | || | .gitignore | || | bochs.bxrc | || | config.sys | || | fixlink.c | || | Makefile | || | mtoolsrc | || | README.md | || | screenshot.png | || | system.ini | WSL9x Windows 9x Subsystem for Linux. WSL9x runs a modern Linux kernel (6.19 at time of writing) cooperatively inside the Windows 9x kernel, enabling users to take advantage of the full suite of capabilities of both operating systems at the same time, including paging, memory protection, and pre-emptive scheduling. Run all your favourite applications side by side - no rebooting required!

## Key Takeaways

- Proudly written without AI.
- Technical details WSL9x is made up of three components: a patched Linux kernel (see the win9x-um-6.19 branch), a VxD driver, and a wsl.com client program.
- The driver is responsible for the initialisation of WSL9x (see vxd/wsl9x.asm for the driver entry point).

---
_Auto-generated daily digest entry._
