# DeepSeek V4 Flash Vision Experimental now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-08-22 14:28
- **Original:** https://vercel.com/changelog/deepseek-v4-flash-with-vision-now-available-on-ai-gateway

## Summary

DeepSeek V4 Flash with vision is now available on AI Gateway. This model is an experimental version that accepts images alongside text. You can ask it to describe a picture, read text out of a screenshot, or work through a chart in the same request as your prompt.

## Key Takeaways

- DeepSeek V4 Flash Vision Experimental now available on AI Gateway.
- Tool use, reasoning, and caching all work the same as before.
- Use deepseek/deepseek-v4-flash-vision-exp to get started: import { generateText } from 'ai';import fs from 'node:fs'; const { text } = await generateText({ model: 'deepseek/deepseek-v4-flash-vision-exp', messages: [ { role: 'user', content: [ { type: 'text', text: 'What is in this screenshot?' }, { type: 'file', mediaType: 'image/png', data: fs.readFileSync('./example.png'), }, ], }, ],}); Images can be JPEG, PNG, GIF, or WebP.

---
_Auto-generated daily digest entry._
