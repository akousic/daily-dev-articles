# Google Chrome silently installs a 4 GB AI model on your device without consent

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 694
- **Published (UTC):** 2026-05-05 07:34
- **Original:** https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/

## Summary

Google Chrome silently installs a 4 GB AI model on your device Two weeks ago I wrote about Anthropic silently registering a Native Messaging bridge in seven Chromium-based browsers on every machine where Claude Desktop was installed [1]. The pattern was: install on user launch of product A, write configuration into the user's installs of products B, C, D, E, F, G, H without asking. Reach across vendor trust boundaries.

## Key Takeaways

- Re-installs itself if the user removes it manually, every time Claude Desktop is launched.
- This week I discovered the same pattern, executed by Google.
- Google Chrome is reaching into users' machines and writing a 4 GB on-device AI model file to disk without asking.

---
_Auto-generated daily digest entry._
