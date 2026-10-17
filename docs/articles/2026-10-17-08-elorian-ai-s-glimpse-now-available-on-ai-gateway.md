# Elorian AI's Glimpse now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-17 16:57
- **Original:** https://vercel.com/changelog/elorian-ai-glimpse-now-available-on-ai-gateway

## Summary

Glimpse from Elorian is now available on AI Gateway. The visual reasoning model accepts images and video to follow objects through motion, interpret spatial relationships, and connect an action to its physical consequences. Glimpse can return to visual evidence as it works: zooming into a detail, revisiting a short interval of video, or tracking the same feature across frames.

## Key Takeaways

- This allows the model to support use cases like scientific chart analysis, video captioning, visual counting, and robotics data annotation.
- Some examples include checking a train's motion to determine whether it is slowing down, keeping objects distinct through camera movement, and labeling completed actions in robot footage.
- Use elorian/glimpse as the model name: import { streamText } from 'ai'; const result = streamText({ model: 'elorian/glimpse', messages: [{ role: 'user', content: [ { type: 'text', text: 'Describe this image in one sentence.' }, { type: 'file', mediaType: 'image/jpeg', data: new URL('https://elorian.ai/assets/blog/glimpse/open-pliers.jpg'), }, ], }], maxOutputTokens: 4096, reasoning: 'low'}); for await (const text of result.textStream) { process.stdout.write(text);} With AI SDK 7, you can send a video as a file part.

---
_Auto-generated daily digest entry._
