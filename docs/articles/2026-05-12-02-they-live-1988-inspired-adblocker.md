# They Live (1988) inspired Adblocker

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 468
- **Published (UTC):** 2026-05-12 00:37
- **Original:** https://github.com/davmlaw/they_live_adblocker

## Summary

A fork of uBlock Origin Lite that, instead of hiding cosmetically-blocked ads, replaces them with white tiles bearing slogans from John Carpenter's 1988 film They Live: OBEY, CONSUME, WATCH TV, SLEEP, SUBMIT, CONFORM, STAY ASLEEP, BUY, WORK, NO INDEPENDENT THOUGHT, DO NOT QUESTION AUTHORITY. Each blocked ad gets a single phrase, picked at random from the list. The idea is from a blog post I wrote in 2015 (and never got around to building): They Live adblock mode.

## Key Takeaways

- Download the latest uBOLite_theylive.chromium.zip from the Releases page, extract it, then in Chromium / Chrome / Brave / Edge: - Open chrome://extensions - Toggle Developer mode on (top-right) - Click Load unpacked and select the extracted folder Keep the folder around — the extension is loaded from that path.
- By default uBO Lite uses Basic filtering mode, which blocks ads at the network layer.
- Network-blocked ads never produce a DOM element, so there's nothing to "they-live-ify" — you just get empty space, as with normal uBO Lite.

---
_Auto-generated daily digest entry._
