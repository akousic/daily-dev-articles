# Training a 3.8B LLM to 0.384 CORE for $998

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 107
- **Published (UTC):** 2026-09-10 02:04
- **Original:** https://hugovergnes.github.io/little-lm-3-8b/

## Summary

Training a 3.8B LLM to 0.384 CORE for $998 Somewhere between “nanoGPT toy” and “you need a research lab” there’s a large, under-described region where one person with a few thousand dollars can train a meaningful model. I wanted to see language and understanding emerge from random weights for myself, and to learn the parts you can only learn by starting from scratch. This project was written in the evenings, debugged on a 5090 and finished on rented B200s.

## Key Takeaways

- It was heavily inspired by Andrej Karpathy’s nanochat.
- The result is a 3.8B-parameter model scoring 0.384 on CORE, trained on 65B tokens in 43 hours for $998.
- What follows is what worked, what didn’t, and what I still don’t know.

---
_Auto-generated daily digest entry._
