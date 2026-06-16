# How We Saved Big and Simplified Our Image Pipeline: Adopting bunny.net on DEV

- **Source:** Dev.to
- **Rank (today):** #4
- **Ranking metrics:** reactions 29, comments 2
- **Published (UTC):** 2026-06-16 16:41
- **Original:** https://dev.to/devteam/how-we-saved-big-and-simplified-our-image-pipeline-adopting-bunnynet-on-dev-3d53

## Summary

Hey everyone, Ben here. If you’ve been following the journey of DEV and our open source project Forem, you know we’ve always been obsessed with web performance. Way back in the day, I spoke at Codeland about how to make your website so fast it goes viral in Japan, diving into the mechanics of edge caching and how we kept our page loads nearly instant.

## Key Takeaways

- Our core philosophy has always been simple: keep the architecture as lean as possible, cache aggressively at the edge, and let the Rails monolith (Forem) focus on what it does best.
- For years, Fastly has handled our HTML edge caching brilliantly—most of your page requests never even have to touch our Puma servers, which keeps our RAM usage low and our response times in the milliseconds.
- Fastly continues to be how all the document content on DEV is served.

---
_Auto-generated daily digest entry._
