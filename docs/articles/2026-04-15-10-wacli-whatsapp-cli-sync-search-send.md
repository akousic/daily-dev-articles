# Wacli – WhatsApp CLI: sync, search, send

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 165
- **Published (UTC):** 2026-04-15 07:04
- **Original:** https://github.com/steipete/wacli

## Summary

WhatsApp CLI built on top of whatsmeow , focused on: - Best-effort local sync of message history + continuous capture - Fast offline search - Sending messages - Contact + group management This is a third-party tool that uses the WhatsApp Web protocol via whatsmeow and is not affiliated with WhatsApp. Core implementation is in place. See docs/spec.md for the full design notes.

## Key Takeaways

- - Messages: search/list includes display text for reactions, replies, and media types.
- - Send: wacli send file --filename to override the display name.
- - Auth: optional WACLI_DEVICE_LABEL /WACLI_DEVICE_PLATFORM env overrides.

---
_Auto-generated daily digest entry._
