# Claude Code reads AGENTS.md only when telemetry is on [fixed]

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 382
- **Published (UTC):** 2026-09-23 12:15
- **Original:** https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/

## Summary

Claude Code reads AGENTS.md only when telemetry is on Claude Code 2.1.277 added AGENTS.md support, but the loader sits behind a remote feature flag. With telemetry or nonessential traffic turned off, a local AGENTS.md is skipped without a warning. This is what I measured and the one-line CLAUDE.md I use instead.

## Key Takeaways

- Claude Code 2.1.277 announced support for AGENTS.md.
- In a project with no CLAUDE.md, it is supposed to read AGENTS.md instead.
- I keep telemetry off in my shell, and in my repos the file never loaded.

---
_Auto-generated daily digest entry._
