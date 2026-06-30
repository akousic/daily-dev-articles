# Elastic Open-Sources Atlas Agent Memory Based on Cognitive Science

- **Source:** InfoQ
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-30 16:25
- **Original:** https://www.infoq.com/news/2026/06/elastic-atlas-agent-memory/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Elastic open-sourced Atlas, a system built on Elasticsearch that maintains three categories of memory for agents. Atlas integrates with agents via MCP and maintains per-user isolation of memories. When evaluated on question-answering capability, it scored 0.89 Recall@10.

## Key Takeaways

- Atlas is a solution to the problem of identifying the proper context data to add to an agent's LLM prompt when dealing with users that have a long history of interacting with the agent.
- Loading the entire interaction history isn't a scalable solution, according to Elastic: The standard workaround is to stuff prior context into the context window.
- That breaks down on cost, on latency, and on the well-documented "lost in the middle" effect, where models ignore facts placed far from the prompt's edges.

---
_Auto-generated daily digest entry._
