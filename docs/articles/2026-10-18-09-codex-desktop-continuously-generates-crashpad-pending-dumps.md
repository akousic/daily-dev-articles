# Codex Desktop continuously generates Crashpad pending dumps

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 160
- **Published (UTC):** 2026-10-17 17:45
- **Original:** https://github.com/openai/codex/issues/25921

## Summary

Repository navigation Codex Desktop continuously generates Crashpad pending dumps, growing without any limit: +5GB per day at least #25921 Description Summary Codex Desktop is continuously adding paired .dmp and _sidecar.json files under: ~/Library/Application Support/com.openai.codex/web/Crashpad/pending On my machine this directory grew to 4.9G and 54,504 files in one day. The count continued increasing during investigation, so this appears to be active Crashpad dump generation rather than stale one-time leftovers. The Codex Desktop app is still functional while this is happening.

## Key Takeaways

- I can use the app, inspect the filesystem, and interact with GitHub from the same running session.
- So the user-visible problem is not that Codex is fully crashing or unable to launch.
- The issue is that Crashpad is continuously generating pending dump/sidecar pairs in the background while the app remains usable, causing unbounded local disk growth.

---
_Auto-generated daily digest entry._
