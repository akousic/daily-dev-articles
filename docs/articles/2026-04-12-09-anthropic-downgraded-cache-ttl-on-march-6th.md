# Anthropic downgraded cache TTL on March 6th

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 216
- **Published (UTC):** 2026-04-12 05:45
- **Original:** https://github.com/anthropics/claude-code/issues/46829

## Summary

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window.

## Key Takeaways

- Reload to refresh your session.Dismiss alert Cache TTL appears to have silently regressed from 1h to 5m around early March 2026, causing significant quota and cost inflation Summary Analysis of raw Claude Code session JSONL files spanning Jan 11 – Apr 11, 2026 shows that Anthropic appears to have silently changed the prompt cache TTL default from 1 hour to 5 minutes sometime in early March 2026.
- Prior to this change, Claude Code was receiving 1-hour TTL cache writes — which we believe was the intended default.
- The reversion to 5-minute TTL has caused a 20–32% increase in cache creation costs and a measurable spike in quota consumption for subscription users who have never previously hit their limits.

---
_Auto-generated daily digest entry._
