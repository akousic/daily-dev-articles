# Postman silently auto-installs AI plugins and attempts to share all API data

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 708
- **Published (UTC):** 2026-11-03 17:22
- **Original:** https://github.com/postmanlabs/postman-app-support/issues/14370

## Summary

Repository navigation Description Is there an existing issue for this? - I have searched the tracker for existing similar issues and I know that duplicates will be closed Describe the Issue Opening Postman on my Mac was followed by unexpected changes to my coding agents: recurring MCP authentication warnings and Codex repeatedly routing API work through Postman skills. Investigation found a user-wide Postman plugin, a startup instruction hook, a remote MCP connection, a Claude Code plugin, and a separately installed Postman CLI.

## Key Takeaways

- I consider automatically changing unrelated coding agents and attempting to approve your own instruction hook a severe consent and trust-boundary problem.
- An API client should not make itself the default workflow in other tools simply because I opened it.
- Evidence from this Mac Postman desktop: 12.33.4.

---
_Auto-generated daily digest entry._
