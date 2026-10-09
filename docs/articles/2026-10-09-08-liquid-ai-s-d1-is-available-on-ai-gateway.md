# Liquid AI's d1 is available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-09 19:24
- **Original:** https://vercel.com/changelog/liquid-ai-d1-is-available-on-ai-gateway

## Summary

Liquid d1 is now available on AI Gateway. d1 is a decision model that evaluates shared state against typed questions for classification, routing, and scoring. It returns structured answers with probabilities without generating text tokens.

## Key Takeaways

- d1 also has vision support: the model can answer typed questions about images for visual classification, inspection, and scoring.
- Use liquid/d1 through the AI SDK decision API, the OpenAI-compatible Decisions API, or the TypeSafe-compatible API.
- These examples ask whether a support agent issued a refund: import { experimental_decide as decide } from 'ai'; const result = await decide({ model: 'liquid/d1', state: 'The support agent issued a full refund to the customer.', questions: { refunded: { type: 'boolean', instructions: 'Was a refund issued?', }, },}); console.log(result.answers.refunded); Copy link to headingImage input This example reads a local PNG named square.png and asks which color it shows: import { readFileSync } from 'node:fs';import { experimental_decide as decide } from 'ai'; const image = readFileSync('./square.png').toString('base64'); const result = await decide({ model: 'liquid/d1', state: [ { type: 'json', value: [ 'Which color is the square?', { type: 'image_url', image_url: { url: `data:image/png;base64,${image}` }, }, ], }, ], questions: { color: { type: 'choice', instructions: 'What color is the square?', criteria: { red: null, blue: null, green: null }, }, },}); console.log(result.answers.color); AI Gateway provides a unified way to access models and track usage and cost.

---
_Auto-generated daily digest entry._
