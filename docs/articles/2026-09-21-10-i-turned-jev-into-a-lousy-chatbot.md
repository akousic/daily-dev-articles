# I turned Jev into a (lousy) chatbot

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 169
- **Published (UTC):** 2026-09-20 17:51
- **Original:** https://github.com/kyle-pena-nlp/jevchat/

## Summary

jevchat turns that into a chat model. At every step it asks Jev one question: Given the user's question and the reply written so far, which symbol comes next? The options are an alphabet plus an option to stop emitting.

## Key Takeaways

- Jev returns a probability for each one, and the sampler draws the next symbol from that normalised distribution.
- Append, repeat, and stop when STOP is drawn.
- There are several alphabets (including truncated token lists) and sampling strategies available.

---
_Auto-generated daily digest entry._
