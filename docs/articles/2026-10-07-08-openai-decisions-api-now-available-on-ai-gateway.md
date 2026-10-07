# OpenAI Decisions API now available on AI Gateway

- **Source:** Vercel
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-07 19:51
- **Original:** https://vercel.com/changelog/openai-decisions-api-now-available-on-ai-gateway

## Summary

OpenAI's Decisions API is now available on AI Gateway through an OpenAI-compatible /v1/decisions endpoint. Use it with GPT-6 Luna Decisions or any other decision model on AI Gateway. Decision models answer typed questions about a shared input and return probabilities, choices, and scores instead of generated text, which suits routing, triage, guardrails, and rubric scoring.

## Key Takeaways

- You can ask predicate (yes/no), choice, and score questions against the same input in one request.
- openai/gpt-6-luna-decisions is a separate model ID from openai/gpt-6-luna, which stays a language model for text generation.
- Requests to the decisions ID go to the Decisions API and are billed at its rates.

---
_Auto-generated daily digest entry._
