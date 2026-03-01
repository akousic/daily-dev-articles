# MCP server that reduces Claude Code context consumption by 98%

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 460
- **Published (UTC):** 2026-02-28 10:01
- **Original:** https://mksg.lu/blog/context-mode

## Summary

Every MCP tool call in Claude Code dumps raw data into your 200K context window. A Playwright snapshot costs 56 KB. Twenty GitHub issues cost 59 KB.

## Key Takeaways

- One access log — 45 KB.
- After 30 minutes, 40% of your context is gone.
- Context Mode is an MCP server that sits between Claude Code and these outputs.

---
_Auto-generated daily digest entry._
