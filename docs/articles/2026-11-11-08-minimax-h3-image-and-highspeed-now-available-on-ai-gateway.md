# MiniMax H3 Image and Highspeed now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-11 21:11
- **Original:** https://vercel.com/changelog/minimax-h3-image-and-highspeed-now-available-on-ai-gateway

## Summary

MiniMax H3 Image and MiniMax H3 Image Highspeed are now available on AI Gateway. Generate images from text or edit existing images with one API key and no separate MiniMax account. Both models support custom dimensions and aspect ratios, including 2K and 4K outputs.

## Key Takeaways

- Use a text prompt to create a product visual or illustration, then pass the image back with instructions to change colors, subjects, or composition.
- The Highspeed variant offers faster generation with the same generation and editing options.
- Use minimax/minimax-h3-image or minimax/minimax-h3-image-highspeed as the model name: import { writeFile } from 'node:fs/promises';import { generateImage } from 'ai'; const { image } = await generateImage({ model: 'minimax/minimax-h3-image', prompt: 'A blue ceramic vase with wildflowers on a sunlit wooden table.', size: '2048x2048', maxRetries: 0, providerOptions: { minimax: { outputFormat: 'png' } },}); await writeFile('image.png', image.uint8Array); To edit the generated image, pass it back with an instruction: const { image: editedImage } = await generateImage({ model: 'minimax/minimax-h3-image', prompt: { text: 'Change the vase to terracotta and keep the flowers and setting.', images: [image.uint8Array], }, size: '2048x2048', maxRetries: 0, providerOptions: { minimax: { outputFormat: 'png' } },}); await writeFile('edited-image.png', editedImage.uint8Array); Both models also support the OpenAI-compatible /v1/images/generations and /v1/images/edits routes.

---
_Auto-generated daily digest entry._
