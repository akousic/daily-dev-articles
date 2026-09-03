# Cursor Cloud Agents can now run in Vercel Sandbox

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-09-03 17:46
- **Original:** https://vercel.com/changelog/run-cursor-cloud-agents-vercel-sandbox

## Summary

Cursor Cloud Agents can now run in Vercel Sandbox instead of Cursor's hosted machines. Cursor manages the agent harness and inference loop. Its Self-Hosted Machines APIs let you supply the execution environment where agents clone repositories, edit files, and run commands and tests.

## Key Takeaways

- Self-Hosted Machines requires a Cursor Enterprise plan.
- Vercel Sandbox provides that execution environment as an isolated Firecracker microVM for each agent request.
- Vercel Functions and Vercel Workflow form a durable control plane that claims queued agent requests, provisions workers, monitors sessions, and cleans up automatically.

---
_Auto-generated daily digest entry._
