# Vercel Introduces Eve, an Open-Source Framework for Building AI Agents

- **Source:** InfoQ
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-27 15:20
- **Original:** https://www.infoq.com/news/2026/06/vercel-eve-agents/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Vercel has released Eve, an open-source framework for building, deploying, and operating AI agents in production. The framework provides a filesystem-based project structure that organizes an agent into directories for instructions, tools, skills, subagents, communication channels, and scheduled tasks, allowing developers to define an agent's behavior without manually implementing much of the supporting infrastructure. Eve is designed around a filesystem-first architecture, where each capability is represented as a file.

## Key Takeaways

- Developers configure an agent through a single configuration file, define its behavior using Markdown instructions, add tools as TypeScript files, and organize reusable knowledge as skills.
- During build time, the framework automatically discovers these components and exposes them to the agent without additional registration code.
- The framework includes several production-oriented capabilities, including durable execution, sandboxed code execution, human approval workflows, subagents, tracing, and evaluation tools.

---
_Auto-generated daily digest entry._
