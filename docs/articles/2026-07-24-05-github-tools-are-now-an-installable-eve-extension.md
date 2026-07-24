# GitHub tools are now an installable eve extension

- **Source:** Vercel
- **Rank (today):** #5
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-24 15:35
- **Original:** https://vercel.com/changelog/github-tools-eve-extension

## Summary

You can now add GitHub tools to your eve agent as an extension. Add the package, drop one file in agent/extensions/, and your agent gets every tool with Vercel Connect auth, presets, and approval rules built in. Install @github-tools/eve-extension: pnpm add @github-tools/eve-extensionThen register it from a file in agent/extensions/: import githubExtension from '@github-tools/eve-extension' export default githubExtension({ connector: 'github/my-connector', preset: 'code-review', requireApproval: { addPullRequestComment: ({ toolInput }) => toolInput?.owner !== 'vercel-labs', },}) One file registers the code-review toolset, with approval required before commenting outside your own org.

## Key Takeaways

- - Connector-backed auth: Pass a Vercel Connect connector and the extension mints short-lived, scoped GitHub tokens at runtime.
- - Presets scope the toolset: - code-review,- issue-triage,- repo-explorer,- ci-ops, and- maintainermap to Connect scopes automatically, so tokens carry only the permissions the tools need.
- - Approval rules travel with the config: Every write tool requires approval by default.

---
_Auto-generated daily digest entry._
