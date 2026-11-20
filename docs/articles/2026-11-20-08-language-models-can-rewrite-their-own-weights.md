# Language Models Can Rewrite Their Own Weights

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 285
- **Published (UTC):** 2026-11-20 16:29
- **Original:** https://arxiv.org/abs/2611.21885

## Summary

Computer Science > Artificial Intelligence [Submitted on 16 Nov 2026 (v1), last revised 18 Nov 2026 (this version, v2)] Title:Language Models Can Rewrite Their Own Weights View PDF HTML (experimental) Abstract:A language model is trained once and frozen. Making it better takes another training run, or a prompt, a harness or extra computation at inference that is gone once the task ends. We show a third way: to our knowledge for the first time, a language model rewrites its own weights by its own reasoning and becomes better, with no gradients and no training.

## Key Takeaways

- We call this self-rewriting: the model is its own optimizer.
- In earlier work, a frontier model edited a much smaller one; here an open 27B model, given its weights, its graded answers and the ability to run itself, diagnoses its own failure and rewrites the weights behind it.
- It surpasses itself: its own edit makes it 6.6 points more accurate on problems it never saw.

---
_Auto-generated daily digest entry._
