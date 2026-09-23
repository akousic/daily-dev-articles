# Cheaper LLM labelling

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-23 08:14
- **Original:** https://entropicthoughts.com/cheaper-llm-labeling

## Summary

Cheaper LLM labelling I have a small project where I needed to label commits as either “maintenance” or “new development”. The obvious way to do it is with a cheap but relatively capable llm, like gpt 5.6 Luna. I tested it on a small set of commits and manually verified its labelling, and it emitted the same label as I would have for the entire test set.

## Key Takeaways

- That was good enough for me to roll out on a wider scale.
- If we have Simon Willison’s llm cli tool installed (and you should – it’s great!), we can call it in a pipe from Perl, and read its response.
- My script had a loop that retried the request a few times1 I have experience of models sometimes failing to heed output format instructions, which is usually solved by retrying once or twice.

---
_Auto-generated daily digest entry._
