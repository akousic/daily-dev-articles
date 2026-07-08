# GitLost: We Tricked GitHub's AI Agent into Leaking Private Repos

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 390
- **Published (UTC):** 2026-07-08 05:25
- **Original:** https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/

## Summary

TL;DR: Noma Labs discovered a critical prompt injection vulnerability within GitHub’s new Agentic Workflows, allowing an unauthenticated attacker to silently pull data from private repositories by posting a crafted GitHub Issue in a public repository belonging to the same organization as the private repositories. Noma Labs named the vulnerability GitLost. Introduction GitHub recently launched GitHub Agentic Workflows, pairing GitHub Actions (GitHub’s automation system for running tasks in response to repository events) with an AI agent backed by Claude or GitHub Copilot.

## Key Takeaways

- GitHub Agentic Workflows allow teams to write their GitHub workflows in plain Markdown, and the GitHub agent reads issues, calls tools, and responds on its own.
- As a vulnerability researcher with a security development background, one of the first questions that came to mind after this launch was fundamental and straightforward: What will happen when the GitHub agent reads something it should not trust?
- The answer is a textbook indirect prompt-injection attack, the kind of attack that quietly sends private data to anyone on the internet.

---
_Auto-generated daily digest entry._
