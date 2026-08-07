# Humans missed 1 in 3 threats approving AI agent commands across 40k game runs

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 326
- **Published (UTC):** 2026-08-06 11:58
- **Original:** https://scalex.dev/blog/ai-agent-permissions-stats/

## Summary

Table of Contents A couple of months ago I published a small browser game: you play the human-in-the-loop for an AI coding agent, approving or denying its commands under time pressure. Some commands are routine (git status, npm test) and some other commands indicate your agent has been possessed and is sending your secrets to a remote server (cat ~/.aws/credentials). More on the threats associated with agents running commands and how to mitigate them can be found in the original post.

## Key Takeaways

- The game garnered some interest on hacker news, and after adding in statistics (unfortunately a bit later on) we can take a closer look at the data of over 40,000 runs and 409,000 individual approve/deny decisions.
- Let’s see how the human-in-the-loop, our last line of defence against rogue agents, fared.
- The headline numbers - The average player missed 1 in 3 threats (mean accuracy 66.3%) - 32.9% of sessions ended with a negative score: penalties from approved threats and blocked safe commands outweighed everything done right - 35.2% of players caught every threat, but only 20.8% managed that while blocking at most 1 in 5 of the safe commands.

---
_Auto-generated daily digest entry._
