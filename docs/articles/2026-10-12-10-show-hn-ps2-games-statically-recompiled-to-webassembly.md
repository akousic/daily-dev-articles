# Show HN: PS2 games statically recompiled to WebAssembly

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 246
- **Published (UTC):** 2026-10-12 06:46
- **Original:** https://github.com/snuri00/ps2-web-recomp

## Summary

PlayStation 2 games running in the browser without an emulator. The game's Emotion Engine machine code is translated ahead of time into C++, compiled to WebAssembly, and linked against a reimplementation of the PS2's operating system and hardware that draws with WebGPU. Watch the full recording (1:24) This is the sibling of psp-web-recomp and follows the same method.

## Key Takeaways

- The first title brought up this way is Gran Turismo 4, chosen because it is one of the most demanding games on the system: it leans on both vector units, on exact floating point behaviour for its replays and license tests, and on graphics tricks that read rendered images back as palettes.
- It plays from boot through the opening movie, the menus and races, with music and sound effects, and saves to a memory card kept in the browser.
- A race runs at full speed, 50 frames per second for this PAL release, in Chrome on a laptop's integrated GPU at twice the PS2's resolution, which is how the recording above was made.

---
_Auto-generated daily digest entry._
