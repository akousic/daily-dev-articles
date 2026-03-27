# We rewrote JSONata with AI in a day, saved $500k/year

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 223
- **Published (UTC):** 2026-03-26 22:36
- **Original:** https://www.reco.ai/blog/we-rewrote-jsonata-with-ai

## Summary

We Rewrote JSONata with AI in a Day, Saved $500K/Year A few weeks ago, Cloudflare published “How we rebuilt Next.js with AI in one week.” One engineer and an AI model reimplemented the Next.js API surface on Vite. Cost about $1,100 in tokens. The implementation details didn’t interest me that much (I don’t work on frontend frameworks), but the methodology did.

## Key Takeaways

- They took the existing Next.js spec and test suite, then pointed AI at it and had it implement code until every test passed.
- Midway through reading, I realized we had the exact same problem - only in our case, it was with our JSON transformation pipeline.
- Long story short, we took the same approach and ran with it.

---
_Auto-generated daily digest entry._
