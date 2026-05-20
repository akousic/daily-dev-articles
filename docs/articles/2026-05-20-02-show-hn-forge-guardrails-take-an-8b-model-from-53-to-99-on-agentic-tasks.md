# Show HN: Forge – Guardrails take an 8B model from 53% to 99% on agentic tasks

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 613
- **Published (UTC):** 2026-05-19 12:23
- **Original:** https://github.com/antoinezambelli/forge

## Summary

A reliability layer for self-hosted LLM tool-calling. Forge lifts an 8B local model to the top of its class on multi-step agentic workflows through guardrails (rescue parsing, retry nudges, step enforcement) and context management (VRAM-aware budgets, tiered compaction). The current top self-hosted config (Ministral-3 8B Instruct Q8 on llama-server) scores 86.5% across forge's 26-scenario eval suite — and 76% on the hardest tier.

## Key Takeaways

- Three ways to use it: - WorkflowRunner — Define tools, pick a backend, run structured agent loops.
- Forge manages the full lifecycle: system prompts, tool execution, context compaction, and guardrails.
- SlotWorker adds priority-queued access to a shared inference slot with auto-preemption — for multi-agent architectures where specialist workflows share a GPU slot.

---
_Auto-generated daily digest entry._
