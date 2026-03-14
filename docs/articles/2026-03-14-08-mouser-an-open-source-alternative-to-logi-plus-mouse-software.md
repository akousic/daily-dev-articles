# Mouser: An open source alternative to Logi-Plus mouse software

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 358
- **Published (UTC):** 2026-03-13 18:42
- **Original:** https://github.com/TomBadash/MouseControl

## Summary

A lightweight, open-source, fully local alternative to Logitech Options+ for remapping every programmable button on the Logitech MX Master 3S mouse. No Logitech account required. - macOS support — full macOS compatibility added thanks to andrew-sz, using CGEventTap for mouse hooking, Quartz CGEvent for key simulation, and NSWorkspace for app detection.

## Key Takeaways

- See macOS Setup Guide for details.
- - Remap all 6 programmable buttons — middle click, gesture button, back, forward, horizontal scroll left/right - Per-application profiles — automatically switch button mappings when you switch apps (e.g., different bindings for Chrome vs.
- VS Code) - 22 built-in actions across navigation, browser, editing, and media categories - DPI / pointer speed control — slider from 200–8000 DPI with quick presets, synced to the device via HID++ - Scroll direction inversion — independent toggles for vertical and horizontal scroll - Gesture button support — full HID++ 2.0 divert on Bluetooth (no Logitech software needed) - Auto-reconnection — automatically detects when the mouse is turned off/on or disconnected/reconnected and restores full functionality without restarting the app - Live connection status — the UI shows a real-time "Connected" / "Not Connected" badge that updates as the mouse connects or disconnects - Modern Qt Quick UI — dark Material theme with interactive mouse diagram and per-button action picker - System tray — runs in background, hides to tray on close, toggle remapping on/off from tray menu - Auto-detect foreground app — polls the active window and switches profiles instantly - Zero external services — config is a local JSON file, all processing happens on your machine The UI shows an interactive diagram of the MX Master 3S.

---
_Auto-generated daily digest entry._
