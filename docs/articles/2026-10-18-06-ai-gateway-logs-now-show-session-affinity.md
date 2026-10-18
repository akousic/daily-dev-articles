# AI Gateway logs now show session affinity

- **Source:** Vercel
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-18 17:13
- **Original:** https://vercel.com/changelog/ai-gateway-logs-now-show-session-affinity

## Summary

AI Gateway logs now have a Sessions view that groups requests into sessions and shows how session affinity routed each one. Each row shows the coding agent or app that ran the session, such as Claude Code, Codex, or Cursor, along with its cost, models, providers, and how much of its input was cached across every turn. Open a session to see its cache hit rate, duration, and path.

## Key Takeaways

- The path lists each turn with its model and timing, and names the provider serving the session along with any earlier ones.
- Session affinity sends each turn to the provider that served the one before it, so the provider already has most of the prompt in cache.
- A session that stays on one provider reads more of each prompt from cache.

---
_Auto-generated daily digest entry._
