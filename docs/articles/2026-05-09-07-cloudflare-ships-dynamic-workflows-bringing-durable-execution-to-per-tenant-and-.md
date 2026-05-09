# Cloudflare Ships Dynamic Workflows, Bringing Durable Execution to Per-Tenant and Per-Agent Code

- **Source:** InfoQ
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-09 15:00
- **Original:** https://www.infoq.com/news/2026/05/cloudflare-dynamic-workflows/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Cloudflare has released Dynamic Workflows, an MIT-licensed library that extends the company's durable execution engine so that workflow code can be different for every tenant, agent, or request at runtime. Previously, Cloudflare Workflows required workflow code to be part of the deployment, one binding, one class, per deploy. Dynamic Workflows removes that constraint, letting a platform route every create() call to a different tenant's code and have the engine dispatch run(event, step) back to that same code when the workflow executes seconds, hours, or days later.

## Key Takeaways

- Dan Lapid and Luís Duarte from the Cloudflare engineering team write: Say you're building an app platform where the AI writes TypeScript for every tenant.
- Say you're running a CI/CD product where each repository has its own pipeline.
- Say you're using an agents SDK where each agent writes its own durable plan.

---
_Auto-generated daily digest entry._
