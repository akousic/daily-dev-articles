# Introducing eve, an open-source agent framework

- **Source:** Vercel
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-17 17:13
- **Original:** https://vercel.com/changelog/introducing-eve-an-open-source-agent-framework

## Summary

eve is now available in public preview. eve is an open-source framework for building, running, and scaling agents. An agent is just a directory of files, and production comes built in: - Durable execution - Sandboxed compute - Human-in-the-loop approvals - Subagents - Evals agent/ agent.ts # the model it runs on instructions.md # who it is tools/ run_sql.ts # what it can do post_chart.ts skills/ revenue-definitions.md # what it knows subagents/ investigator/ # who it delegates to channels/ slack.ts # where it lives schedules/ monday-summary.ts # when it acts on its ownA data analyst agent, readable at a glance The smallest agent that runs is just two files, a model and a set of instructions.

## Key Takeaways

- import { defineAgent } from "eve"; export default defineAgent({ model: "anthropic/claude-opus-4.8",});Configuring the agent and its model in one file You are a senior data analyst.
- You answer questions about the team's data.
- - Prefer exact numbers to hand-waving.

---
_Auto-generated daily digest entry._
