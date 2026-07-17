# Vercel Connect support in GitHub Tools

- **Source:** Vercel
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-17 15:19
- **Original:** https://vercel.com/changelog/vercel-connect-support-in-github-tools

## Summary

GitHub Tools now has first-class support for Vercel Connect through the new @github-tools/sdk/connect subpath. Instead of storing a long-lived personal access token, your agent mints short-lived, scoped GitHub tokens at runtime from a connector. There is no secret to store, rotate, or leak.

## Key Takeaways

- Attach a GitHub connector to your project and pick a preset: import { connectGithubTools } from "@github-tools/sdk/connect";import { generateText } from "ai"; const tools = connectGithubTools("github/my-connector", { preset: "code-review",}); const { text } = await generateText({ model: "anthropic/claude-sonnet-5", tools, prompt: "Summarize open PRs on vercel-labs/github-tools.",});Review GitHub PRs with a custom agent - Scopes from presets: Presets such as - code-review,- issue-triage, and- maintainermap to Connect scopes automatically, so tokens carry only the permissions the toolset needs.
- - Works with eve: Import from - @github-tools/sdk/connect/eveand one file in- agent/tools/registers the full toolset with Connect-backed auth.
- - Multi-tenant ready: Override - installationId,- repositories, or- scopesper call to target a specific installation or narrow access to individual repos.

---
_Auto-generated daily digest entry._
