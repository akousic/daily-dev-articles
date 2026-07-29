# Codex Security

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 575
- **Published (UTC):** 2026-07-28 20:52
- **Original:** https://github.com/openai/codex-security

## Summary

@openai/codex-security is a CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in your code. Scan repositories, review changes, track findings over time, and run security checks in CI. Requires Node.js 22 or later, Python 3.10 or later, and access to Codex Security.

## Key Takeaways

- npm install @openai/codex-security npx codex-security login npx codex-security scan .For CI, set OPENAI_API_KEY instead of signing in.
- If both a ChatGPT sign-in and an API key are available, interactive scans ask which credential to use.
- CI and other noninteractive scans keep the existing API-key precedence.

---
_Auto-generated daily digest entry._
