# Windows Loudness Equalization, reverse-engineered and ported to PipeWire

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 301
- **Published (UTC):** 2026-11-25 11:34
- **Original:** https://github.com/xoxorwr/pw-loudness-eq

## Summary

Windows' Loudness Equalization for PipeWire, reverse engineered from WMALFXGFXDSP.dll. It evens out the volume of each application, so quiet and loud parts play at a similar level. - modules/loudness/: the PipeWire module and the DSP plugin.

## Key Takeaways

- It processes every app's playback stream.
- - modules/limiter/: the output limiter of Windows' audio engine (AudioEng.dll), on every playback device.
- It keeps the boost from clipping.

---
_Auto-generated daily digest entry._
