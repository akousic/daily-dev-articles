# Mistral Large 4 updated weights and lower pricing on AI Gateway

- **Source:** Vercel
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-29 19:29
- **Original:** https://vercel.com/changelog/mistral-large-4-updated-weights-and-lower-pricing-on-ai-gateway

## Summary

Mistral Large 4 from Mistral now uses updated weights on AI Gateway, with lower pricing for input, cached input, and output tokens. According to Mistral’s release announcement, the updated weights improve agentic coding and defensive cybersecurity, with greater token efficiency on coding tasks. The release also improves spreadsheet creation and editing, web research, and resistance to prompt injection.

## Key Takeaways

- If you were already using mistral/mistral-large-4 via AI Gateway, there is no need to change your model to start using the updated version.
- The existing model ID string uses the new model with updated weights and pricing.
- import { streamText } from 'ai'; const result = streamText({ model: 'mistral/mistral-large-4', prompt: 'Suggest three fixes for a flaky API retry loop.',}); for await (const text of result.textStream) { process.stdout.write(text);} To use Mistral Large 4 in fx, Pi, Claude Code, Codex, Cursor, or other harnesses, install the latest Vercel CLI and run setup: npx vercel ai-gateway setup Then select mistral/mistral-large-4 in the agent.

---
_Auto-generated daily digest entry._
