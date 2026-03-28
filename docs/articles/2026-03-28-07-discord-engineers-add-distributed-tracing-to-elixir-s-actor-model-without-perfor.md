# Discord Engineers Add Distributed Tracing to Elixir's Actor Model Without Performance Penalty

- **Source:** InfoQ
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-28 14:40
- **Original:** https://www.infoq.com/news/2026/03/discord-elixir-actor-tracing/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Discord engineering published details on how they added distributed tracing to their Elixir infrastructure while handling millions of concurrent users. The team built a custom "Transport" library that wraps Elixir's message-passing system with trace context, solving a fundamental challenge in instrumenting actor-based architectures. Unlike HTTP-based microservices, where trace context travels in headers, Elixir's actor model passes arbitrary messages between processes with no built-in metadata layer.

## Key Takeaways

- Discord needed end-to-end visibility across its chat infrastructure, yet it faced a gap: OpenTelemetry's standard tracing worked within individual services but couldn't propagate context between Elixir processes.
- The team identified three requirements for any solution: it had to be ergonomic enough for developers to adopt, support both raw messages and GenServer abstractions, and enable zero-downtime deployment across their production fleet.
- Discord's solution introduces an "Envelope" primitive that wraps messages with trace context.

---
_Auto-generated daily digest entry._
