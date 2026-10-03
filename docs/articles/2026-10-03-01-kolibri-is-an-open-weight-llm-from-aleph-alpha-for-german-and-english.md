# Kolibri is an open-weight LLM from Aleph Alpha for German and English

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 395
- **Published (UTC):** 2026-10-03 10:43
- **Original:** https://tej.as/blog/aleph-alpha-kolibri

## Summary

Aleph Alpha Kolibri: How the Sovereign German LLM Works Kolibri is an open-weight large language model (LLM) from Aleph Alpha for German and English: a mixture of experts with 78 billion parameters that only uses about 3.5 billion of them for each token it reads or writes. It came out on 3 October 2026 under the Apache 2.0 license, the weights are on Hugging Face, and it was trained from scratch on infrastructure in Germany and Finland. (Kolibri is German for hummingbird, which is cute for a model whose whole trick is being light.) I live in Germany, and at SmashingConf New York in 2024 I told the room what I’d heard in the US when I said where I’m based: “you regulate, you don’t innovate.” It hurt to hear, and what I wished for on that stage was the middle, “the right balance between innovation and regulation around data privacy, data stewardship, environmental constraints and energy requirements.” Kolibri is a pretty direct answer to that: a German team built it with the EU AI Act in mind “from the ground up”, and in Aleph Alpha’s own evaluation it scores above every compared model of its size in both languages.

## Key Takeaways

- Huge congrats to everyone at Aleph Alpha who built it, my good friend Michael Hofmann among them!
- This post is about how Kolibri works, where it’s strong, where it isn’t, how to run it, and when it’s the right pick.
- Everything here comes from Aleph Alpha’s 189 page technical report, the model card and their launch post, plus one experiment I ran on its tokenizer.

---
_Auto-generated daily digest entry._
