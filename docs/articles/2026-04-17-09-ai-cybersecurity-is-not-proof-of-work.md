# AI cybersecurity is not proof of work

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 226
- **Published (UTC):** 2026-04-16 10:48
- **Original:** https://antirez.com/news/163

## Summary

The proof of work is the wrong analogy: finding hash collisions, while exponentially harder with N, is guaranteed to find, with enough work, some S so that H(S) satisfies N, so an asymmetry of resources used will see the side with more "work ability" eventually winning. But bugs are different: 1. Different LLMs executions take different branches, but eventually the possible branches based on the code possible states are saturated.

## Key Takeaways

- If we imagine sampling the model for a bug in a given code M times, with M large, eventually the cap becomes not "M" (because of saturated state of the code AND the LLM sampler meaningful paths), but "I", the model intelligence level.
- The OpenBSD SACK bug easily shows that: you can run an inferior model for an infinite number of tokens, and it will never realize(*) that the lack of validation of the start window, if put together with the integer overflow, then put together with the fact the branch where the node should never be NULL is entered regardless, will produce the bug.
- So, cyber security of tomorrow will not be like proof of work in the sense of "more GPU wins"; instead, better models, and faster access to such models, will win.

---
_Auto-generated daily digest entry._
