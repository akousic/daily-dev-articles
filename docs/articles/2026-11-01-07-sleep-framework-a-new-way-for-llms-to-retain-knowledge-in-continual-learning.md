# Sleep framework: A new way for LLMs to retain knowledge in continual learning

- **Source:** Hacker News
- **Rank (today):** #7
- **Ranking metrics:** HN score 262
- **Published (UTC):** 2026-10-28 12:24
- **Original:** https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/

## Summary

October 27, 2026 Ali Behrouz and Vahab Mirrokni, Google Research We introduce a sleep phase in continual learning, enabling large language models to continuously integrate new facts and enhance reasoning while mitigating catastrophic forgetting or static knowledge cutoffs. Modern LLMs achieve impressive performance via pre-training and in-context learning (ICL). However, once deployed, they remain largely static, operating with a fixed knowledge cutoff date that leaves them unable to acquire long-term capabilities or adapt to new information.

## Key Takeaways

- While updating models with new data seems like the obvious solution, continual parameter updates often trigger catastrophic forgetting, a fundamental issue where learning new tasks severely degrades performance on previously learned ones.
- Alternatively, relying strictly on ICL limits knowledge retention to the immediate context window: once the context session ends, the acquired short-term information is forgotten.
- Inspired by how the human brain processes and stabilizes memory during rest, we introduce a sleep framework in continual learning: a learning paradigm that equips large language models (LLMs) with a continuous periodic lifecycle, enabling them to continually learn, consolidate fragile short-term context into stable long-term parameters.

---
_Auto-generated daily digest entry._
