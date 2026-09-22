# rift - a tiling window manager for macos

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-21 13:02
- **Original:** https://github.com/acsandmann/rift/

## Summary

- Multiple layout styles - Tiling (i3/sway-like) - Binary Space Partitioning (bspwm-like) - Floating (independent window frames with optional stacks) - Master-stack (dwm-like) - Scrolling columns (niri-style) - Stack (accordion) - Menubar icon that opens a menu for switching workspaces, changing layouts, and accessing quick Rift controls - Save and restore layouts from the menu bar or CLI, with reusable layouts listed from a configurable folder - Focus follows the mouse with auto raise - Does not require disabling SIP - Performant animations (as seen in the demo) - Switch to next/previous workspace with trackpad gestures (just like native macOS) - Hot reloadable configuration - Mach port based IPC for communicating with rift from third-party programs (sketchybar, etc) - Works with “Displays have separate Spaces” enabled (unlike all other major WMs) Get up and running via the docs: Join #rift:matrix.org for discussion, support, and development. If rift is part of your daily workflow, consider sponsoring its development. Aerospace worked well for me, but I missed animations and the ability to use fullscreen on one display while working on the other.

## Key Takeaways

- I also prefer leveraging private/undocumented APIs as they tend to be more reliable (due to the OS being built on them and all the public APIs) and performant.
- for more on why rift exists and what rift strives to do, see the manifesto Rift began as a fork (and is licensed as such) of glide-wm but has since diverged significantly.
- It uses private APIs reverse engineered by yabai and other projects.

---
_Auto-generated daily digest entry._
