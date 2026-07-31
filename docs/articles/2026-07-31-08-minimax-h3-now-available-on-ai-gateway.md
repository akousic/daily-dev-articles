# MiniMax H3 now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-31 16:04
- **Original:** https://vercel.com/changelog/minimax-h3-now-available-on-vercel-ai-gateway

## Summary

MiniMax H3 is now available on AI Gateway. H3 generates 2K video from a text prompt, a starting image, a pair of first and last frames, or reference material. Alongside text-to-video and first-frame image-to-video, the model supports first-to-last keyframe transitions and multimodal reference-to-video, conditioning a generation on reference images, video, or audio in a single request.

## Key Takeaways

- Reference and keyframe modes are mutually exclusive.
- Output is mp4 at 2K resolution, from 5 to 15 seconds, in aspect ratios including 21:9, 16:9, 4:3, 1:1, 3:4, and 9:16, or adaptive to a supplied image.
- To use MiniMax H3, set model to minimax/minimax-h3 in the AI SDK: import { experimental_generateVideo as generateVideo } from 'ai'; const { videos } = await generateVideo({ model: 'minimax/minimax-h3', prompt: 'A white kitten chases a butterfly across a sunlit garden.', aspectRatio: '16:9', duration: 5, providerOptions: { minimax: { pollTimeoutMs: 600000, }, },});Text to video with MiniMax H3 Pass a starting image with the prompt, and the model animates it following the image's aspect ratio.

---
_Auto-generated daily digest entry._
