# Microsoft Three-Layer LLM Routing Architecture for AI Agents on AKS

- **Source:** InfoQ
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-29 15:53
- **Original:** https://www.infoq.com/news/2026/07/microsoft-agents-aks-routing/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Microsoft has released a reference architecture for routing agent traffic on Azure Kubernetes Service. It breaks down the issue into three key choices: which model answers a call, how the call is managed, and which GPU replica handles it. The design combines the Kubernetes Gateway API Inference Extension for load balancing, agentgateway as an AI proxy, and RouteLLM for semantic routing.

## Key Takeaways

- All three connect into one OpenAI-compatible endpoint.
- The motivation is agentic workloads specifically, not chat.
- A single agent task can fire hundreds of LLM calls in a plan-act-observe loop, and most of those calls (a tool-argument fill, a yes/no gate, a summary) don't need a frontier model.

---
_Auto-generated daily digest entry._
