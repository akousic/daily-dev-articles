# Better and Cheaper Than IPTV

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 257
- **Published (UTC):** 2026-07-19 00:59
- **Original:** https://github.com/stupside/castor

## Summary

Smart TVs won't cast arbitrary web video, and screen mirroring is laggy and drops resolution. Castor casts the real stream instead, at full quality, from your terminal. Point Castor at a web page you are watching, or at a direct stream URL, and it finds the video, extracts the stream, transcodes it for your TV, and casts in real time.

## Key Takeaways

- It can also resolve an IMDB/TMDB id against sources you configure yourself, and burn in auto-generated subtitles.
- To extract, it launches headless Chrome and watches network traffic over the Chrome DevTools Protocol, then runs a short action pipeline to start playback: click the page, navigate into the largest iframe, and click again as a fallback.
- This works on pages that allow automated playback, and won't work everywhere.

---
_Auto-generated daily digest entry._
