# Claude Code managed to get Adobe Lightroom working on Linux

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-17 07:58
- **Original:** https://github.com/sander110419/lightroom-cc-on-linux

## Summary

Status: ✅ Working as of 2026-05-16, Wine 11.8 staging, Lightroom CC 9.3.1. This repo documents how to install and run Adobe Lightroom CC (the cloud-syncing photo app, sometimes called "Lightroom Desktop" — NOT Lightroom Classic) on Linux with Wine. - The full Creative Cloud desktop app working under Wine (sign in, apps panel, install other Adobe apps from the catalog) - Lightroom CC launching, showing the cloud-synced photo library, and the Edit module rendering with all the panels (Light, Color, Effects, Detail, Optics, Geometry, …) - The Remove / Heal tool working — brush, mask, apply (as of 2026-05-16; this needed an extra Media Foundation patch over the earlier drafts of this guide — see GUIDE.md section 6.5) See KNOWN_ISSUES.md .

## Key Takeaways

- Short version: a couple of specific dialogs (like "What's New") can crash, and some advanced GPU-accelerated features may not be 100% — but the core editing workflow works.
- - 64-bit Linux distro, kernel 6.x or newer - Wine 11.8 staging or newer ( wine --version should saywine-11.8 (Staging) or similar) winetricks 20240105 or newer- An NVIDIA, AMD or Intel GPU with Vulkan drivers (we tested NVIDIA, but DXVK works on all three) - A valid Adobe Creative Cloud subscription that includes Lightroom CC - About 10 GB of free disk for the prefix + Adobe install mingw-w64 for building the stub DLLs (sudo apt install mingw-w64 )build-essential ,git , and wine build deps if you want to rebuild the patchedd2d1.dll from source instead of using our prebuilt one git clone https://github.com/sander110419/lightroom-cc-on-linux.git cd lightroom-cc-on-linux ./scripts/setup.sh # ~30 min, mostly downloads Then download ACCCx*.zip from https://creativecloud.adobe.com/apps/download/creative-cloud (signed in to your Adobe account), drop it in installers/ , and run: ./scripts/install-cc.sh ./scripts/install-lightroom.sh ./scripts/run-lightroom.sh See GUIDE.md for the full walkthrough — every fix explained, what wine gap it works around, and how to roll it back.
- The six non-obvious pieces are: - DXVK dummy composition swapchain so WebView2 (Adobe's Electron UI shell) can render at all.

---
_Auto-generated daily digest entry._
