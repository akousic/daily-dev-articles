# Claude Code regularly sends each background agent’s transcript to its model

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 549
- **Published (UTC):** 2026-10-29 03:33
- **Original:** https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce

## Summary

by Flamerix AI · MIT License Tested on Linux, Claude Code 2.1.257–2.1.312; macOS reported working by others (see Tested versions). The binary is not modified (BUN_OPTIONS=--preload). An update can silently undo it, so see Verify.

## Key Takeaways

- Every ~30 seconds, Claude Code re-sends each background agent's full transcript to the model just to fill that agent's status line in the agents panel.
- no-agent-summary.js is a Bun --preload that stops that timer without modifying the Claude Code binary.
- curl -fsSL https://gist.githubusercontent.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce/raw/no-agent-summary.js -o ~/.local/share/no-agent-summary.js claude daemon stop --any BUN_OPTIONS="${BUN_OPTIONS:+$BUN_OPTIONS }--preload=$HOME/.local/share/no-agent-summary.js" claude To make it permanent for every Claude Code process, see Install.

---
_Auto-generated daily digest entry._
