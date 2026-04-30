# Orchestrating AI Code Review at scale

- **Source:** Cloudflare
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-30 15:50
- **Original:** https://blog.cloudflare.com/ai-code-review/

## Summary

Code review is a fantastic mechanism for catching bugs and sharing knowledge, but it is also one of the most reliable ways to bottleneck an engineering team. A merge request sits in a queue, a reviewer eventually context-switches to read the diff, they leave a handful of nitpicks about variable naming, the author responds, and the cycle repeats. Across our internal projects, the median wait time for a first review was often measured in hours.

## Key Takeaways

- When we first started experimenting with AI code review, we took the path that most other people probably take: we tried out a few different AI code review tools and found that a lot of these tools worked pretty well, and a lot of them even offered a good amount of customisation and configurability!
- Unfortunately, though, the one recurring theme that kept coming up was that they just didn’t offer enough flexibility and customisation for an organisation the size of Cloudflare.
- So, we jumped to the next most obvious path, which was to grab a git diff, shove it into a half-baked prompt, and ask a large language model to find bugs.

---
_Auto-generated daily digest entry._
