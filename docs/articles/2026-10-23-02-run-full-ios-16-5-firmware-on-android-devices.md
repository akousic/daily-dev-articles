# Run full iOS 16.5 firmware on Android Devices

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 504
- **Published (UTC):** 2026-10-22 15:26
- **Original:** https://github.com/oosexgang/hackios-xnu-kernel

## Summary

HackiOS boots Apple's open-source XNU kernel (xnu-8796.121.2, the kernel of iOS 16.5) on Android phone hardware and runs the unmodified iOS 16.5 user space on top of it: launchd → backboardd → SpringBoard → apps. Our own EFI loader, our own replacements for Apple's closed drivers, a UEFI port, and a Linux Wi-Fi driver on a compatibility layer make that possible. It runs in two places: - POCO X5 Pro 5G (redwood, Snapdragon 778G) — nothing is flashed: the UEFI is started with fastboot boot, the whole system lives in RAM, and after a reboot the phone is back in Android; - QEMU (virt, aarch64) — the same thing on any Linux computer, no phone needed.

## Key Takeaways

- This repository is half of the project: | Repository | What | |---|---| | hackios-xnu-kernel (this one) | XNU patches, the EFI loader, the UEFI port, Wi-Fi, QEMU scripts, xl, prebuilt kernel/loader/UEFI, common/ scripts | | hackios-xnu-userland | our init, injected libraries, launchd jobs, the APFS image builder, the scripts that take iOS out of Apple's IPSW, Metal/Mesa work | No Apple files are in either repository.
- ios165/fetch.sh downloads the iOS 16.5 IPSW from Apple's own CDN to your machine and extracts what is needed there.
- HackiOS is an independent research project by OOSEX GANG and is not affiliated with, authorised or endorsed by Apple Inc.

---
_Auto-generated daily digest entry._
