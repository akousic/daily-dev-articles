# Gemini 3.5 Flash on AI Gateway

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-20 17:17
- **Original:** https://vercel.com/changelog/gemini-3-5-flash-on-ai-gateway

## Summary

1 min read Gemini 3.5 Flash is now available on Vercel AI Gateway. This model has improved coding proficiency and parallel agentic execution loops versus previous Flash versions. It also brings improvements to core reasoning, instruction following, and multi-turn coherence, with stronger performance on complex tasks and higher-quality reasoning traces in thinking mode.

## Key Takeaways

- 3.5 Flash defaults to the medium thinking level, balancing response quality with faster, more cost-efficient generation.
- To use Gemini 3.5 Flash, set model to google/gemini-3.5-flash in the AI SDK.
- import { streamText } from 'ai'; const result = streamText({ model: 'google/gemini-3.5-flash', prompt: 'Refactor this service to run API calls in parallel.', providerOptions: { google: { // use vertex or google thinkingConfig: { thinkingLevel: 'high', includeThoughts: true, }, },}); Note that temperature , topP , topK , and thinking_budget are not supported by this model.

---
_Auto-generated daily digest entry._
