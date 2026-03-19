# Cook: A simple CLI for orchestrating Claude Code

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 254
- **Published (UTC):** 2026-03-19 02:20
- **Original:** https://rjcorwin.github.io/cook/

## Summary

A simple CLI for orchestrating Claude Code, Codex, and OpenCode. # review loop cook "Implement dark mode" review # 3 passes cook "Implement dark mode" x3 # race 3, pick best cook "Implement dark mode" v3 "least code" # two approaches, pick one cook "Auth with JWT" vs "Auth with sessions" pick "best security" # task list cook "Work on next task in plan.md" review \ ralph 5 "DONE if all tasks complete, else NEXT" # compose freely cook "Implement dark mode" review v3 "cleanest result" Two ways to get it: Add the /cook skill to Claude Code: Cook parses three categories of tokens: A prompt. Wrap work with iteration: xN , review , ralph .

## Key Takeaways

- Run parallel branches and resolve: vN , vs , pick .
- Operators compose left to right.
- Each wraps everything to its left.

---
_Auto-generated daily digest entry._
