# OpenAI Introduces Websocket-Based Execution Mode to Reduce Latency in Agentic Workflows

- **Source:** InfoQ
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-07 16:09
- **Original:** https://www.infoq.com/news/2026/05/openai-websocket-responses-api/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

OpenAI has introduced a WebSocket-based execution mode for its responses API to improve the performance of agentic workflows used in coding agents and real-time AI systems. The change replaces the traditional HTTP request-response pattern with a persistent, bidirectional connection between client and server, targeting latency and coordination overhead in multi-step reasoning workflows. According to OpenAI, early production use shows up to 40% latency reduction and improved throughput in high-concurrency scenarios.

## Key Takeaways

- The update addresses a growing bottleneck in agentic systems where each step in a workflow, such as tool calls, intermediate reasoning, and follow-up queries, previously required separate HTTP requests.
- As inference speeds improved, these repeated network round-trip times became a dominant source of latency and operational complexity.
- Traditional HTTP Flow (Source: OpenAI Blog Post) The WebSocket-based execution mode uses a long-lived, bidirectional connection to enable continuous data exchange without repeated handshakes.

---
_Auto-generated daily digest entry._
