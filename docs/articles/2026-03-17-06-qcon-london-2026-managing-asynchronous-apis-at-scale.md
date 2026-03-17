# QCon London 2026: Managing Asynchronous APIs at Scale

- **Source:** InfoQ
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-17 15:06
- **Original:** https://www.infoq.com/news/2026/03/managing-async-apis/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

At QCon London 2026, Ian Cooper, senior principal engineer at Just Eat Takeaway, discussed managing asynchronous APIs in production, showing how endpoint definitions can drive code generation, schema registration, and the automation of messaging infrastructure. Cooper began the session by highlighting how event-driven architectures often evolve informally in their early stages, with teams typically relying on shared knowledge to understand which services publish events, which services consume them, and how messages flow through the system. As organizations scale, however, this informal approach becomes increasingly fragile.

## Key Takeaways

- "At scale, ad-hoc breaks," argued Cooper, with integration points difficult to discover, consumers unknown to producers, and undocumented schema changes breaking downstream systems: As a producer, how do I find consumers?
- Do I search all the repos looking for my message name?
- Do I ask on Slack if anyone consumes my events?

---
_Auto-generated daily digest entry._
