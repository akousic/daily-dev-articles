# Cloudflare/Security-Audit-Skill

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 174
- **Published (UTC):** 2026-09-17 04:36
- **Original:** https://github.com/cloudflare/security-audit-skill

## Summary

A coding-agent skill that turns your agent into a security auditor. It orchestrates isolated agents through reconnaissance, coverage-led hunting, candidate validation, structured output, independent record verification, and target-neutral reporting. This is the skill that seeded Cloudflare's vulnerability discovery harness, described in Build your own vulnerability harness.

## Key Takeaways

- The harness grew into a multi-stage, fleet-wide system; this skill is the single-repo starting point it evolved from.
- The skill runs a structured audit in six phases: - Reconnaissance -- map architecture, trust boundaries, input surfaces, prior evidence, and deterministic coverage in architecture.md andcoverage-ledger.json .
- - Coverage-led hunting -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps.

---
_Auto-generated daily digest entry._
