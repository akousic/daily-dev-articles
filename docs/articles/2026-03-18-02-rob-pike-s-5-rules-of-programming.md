# Rob Pike's 5 Rules of Programming

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 427
- **Published (UTC):** 2026-03-18 09:59
- **Original:** https://www.cs.unc.edu/~stotts/COMP590-059-f24/robsrules.html

## Summary

Rob Pike's 5 Rules of Programming - Rule 1. You can't tell where a program is going to spend its time. Bottlenecks occur in surprising places, so don't try to second guess and put in a speed hack until you've proven that's where the bottleneck is.

## Key Takeaways

- Don't tune for speed until you've measured, and even then don't unless one part of the code overwhelms the rest.
- Fancy algorithms are slow when n is small, and n is usually small.
- Fancy algorithms have big constants.

---
_Auto-generated daily digest entry._
