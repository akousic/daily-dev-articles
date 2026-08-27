# CEO fired developers to make room for AI. Developers create open source AI CEO

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 931
- **Published (UTC):** 2026-08-27 01:46
- **Original:** https://github.com/SenteLabsAI/OpenExecutive

## Summary

An AI system that acts as your company's virtual executive team — a senior advisor with Harvard MBA-level knowledge, customized for your specific business. A walkthrough of Open Executive in action — watch on YouTube. Developed by sentelabs.ai Open Executive provides a single coherent executive voice backed by eight specialist AI agents: - Chief Strategy Officer — competitive analysis, M&A, market positioning, OKRs - Chief Financial Officer — financial modeling, fundraising, unit economics, cash flow - Chief HR/People Officer — hiring, compensation, performance, culture - General Counsel — contracts, IP, employment law basics, compliance - Chief Operating Officer — process design, vendor management, operational scaling - Chief Marketing Officer — GTM strategy, brand, communications, PR - Chief Product Officer — roadmap, prioritization, product strategy - Board Communications Director — board decks, investor relations, governance All responses come from one consistent executive voice.

## Key Takeaways

- The internal agent architecture is never exposed to the user.
- Beyond Q&A, the system maintains episodic memory of past decisions and initiatives across sessions, and a built-in scheduler can proactively surface follow-ups and time-sensitive actions.
- User message ↓ Executive Orchestrator (claude-sonnet-4-6) ↓ tool use → parallel specialist calls CSO / CFO / CHRO / GC / COO / CMO / CPO / Board ↓ each specialist retrieves relevant context from ChromaDB Built-in MBA knowledge + Your company documents ↓ Synthesized executive response Knowledge — Two retrieval layers per specialist call: (1) built-in MBA-level Markdown (knowledge/builtin/, git-tracked) seeded into ChromaDB at startup, and (2) your uploaded company documents chunked and stored in a separate company_docs collection.

---
_Auto-generated daily digest entry._
