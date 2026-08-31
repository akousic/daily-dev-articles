# MiniMax H3 and H3 Max are 50% off on AI Gateway

- **Source:** Vercel
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-08-31 19:55
- **Original:** https://vercel.com/changelog/minimax-h3-and-h3-max-are-50-off-on-ai-gateway

## Summary

MiniMax H3 and H3 Max are 50% off on AI Gateway from August 30 through September 13, in partnership with MiniMax. The discount covers requests billed through AI Gateway, at every duration and in every aspect ratio the model supports. H3 generates 2K video from a text prompt, a starting image, a pair of first and last frames, or reference images, video, and audio.

## Key Takeaways

- H3 Max trades resolution for speed: it renders faster at 480p and 768p, and it takes a text prompt or a starting image.
- The model IDs (minimax/minimax-h3 and minimax/minimax-h3-max) are unchanged, so requests you already send pick up the discounted rate with no code change: import{ experimental_generateVideo as generateVideo }from'ai'; const{ videos }=awaitgenerateVideo({ model:'minimax/minimax-h3-max', prompt:'San Francisco sunrise on a weekend morning.', duration:5, poll:{ timeoutMs:600000}, }); Renders take minutes, so poll runs the generation as a background job and makes short status requests until it lands, rather than holding one long request open.
- See asynchronous generation for the webhook and start-and-status routes.

---
_Auto-generated daily digest entry._
