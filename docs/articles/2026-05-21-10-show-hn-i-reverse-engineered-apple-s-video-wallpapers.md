# Show HN: I reverse engineered Apple's video wallpapers

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 372
- **Published (UTC):** 2026-05-20 23:54
- **Original:** https://github.com/kageroumado/phosphene

## Summary

A video wallpaper engine for macOS Tahoe. Phosphene is a menu bar app + wallpaper extension that plays your own video files as the macOS desktop and lock-screen wallpaper. It plugs into the system's native wallpaper picker, so videos appear alongside Apple's built-in Aerials in System Settings → Wallpaper.

## Key Takeaways

- It is built on top of Apple's private WallpaperExtensionKit framework — the same one Apple's own Aerials use — which means playback runs out-of-process, survives app quits, and integrates with the OS-level lock-screen / idle / sleep lifecycle.
- ⚠️ Private framework.
- Phosphene loadsWallpaperExtensionKit viadlopen and uses Mirror-based runtime introspection to talk to its XPC types.

---
_Auto-generated daily digest entry._
