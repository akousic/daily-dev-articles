# Anthropic Claude Code Leak Reveals Critical Command Injection Vulnerabilities

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-18 19:59
- **Original:** https://beyondmachines.net/event_details/anthropic-claude-code-leak-reveals-critical-command-injection-vulnerabilities-e-6-c-1-k/gD2P6Ple2L

## Summary

Anthropic Claude Code Leak Reveals Critical Command Injection Vulnerabilities Take action: If you're using Claude Code, update immediately to the latest version and stop using authentication helpers. Instead, set the ANTHROPIC_API_KEY environment variable directly. Also, review any .claude/settings.json changes in pull requests as carefully as code changes, and never run the CLI against untrusted pull requests in CI/CD pipelines.

## Key Takeaways

- Learn More Analysis of the leakd Anthropic's Claude Code AI agent revealed three critical command injection vulnerabilities affecting the CLI, agent, and SDK.
- These flaws allow attackers to run arbitrary commands and steal credentials by exploiting how the tool handles environment variables, file paths, and authentication helpers.
- Vulnerabilities summary: All flaws are collectively reported as CVE-2026-35022 (CVSS score 9.8) - VULN-01 -A command injection vulnerability in the command lookup utility that occurs when the tool reads the TERMINAL environment variable.

---
_Auto-generated daily digest entry._
