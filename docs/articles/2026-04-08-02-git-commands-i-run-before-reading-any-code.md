# Git commands I run before reading any code

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 879
- **Published (UTC):** 2026-04-08 08:53
- **Original:** https://piechowski.io/post/git-commands-before-reading-code/

## Summary

The Git Commands I Run Before Reading Any Code Five git commands that tell you where a codebase hurts before you open a single file. Churn hotspots, bus factor, bug clusters, and crisis patterns. Ally Piechowski · · 4 min readThe first thing I usually do when I pick up a new codebase isn’t opening the code.

## Key Takeaways

- It’s opening a terminal and running a handful of git commands.
- Before I look at a single file, the commit history gives me a diagnostic picture of the project: who built it, where the problems cluster, whether the team is shipping with confidence or tiptoeing around land mines.
- What Changes the Most git log --format=format: --name-only --since="1 year ago" | sort | uniq -c | sort -nr | head -20 The 20 most-changed files in the last year.

---
_Auto-generated daily digest entry._
