# A way to exclude sensitive files issue still open for OpenAI Codex

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 86
- **Published (UTC):** 2026-06-28 12:27
- **Original:** https://github.com/openai/codex/issues/2847

## Summary

What feature would you like to see? - A mechanism to explicitly mark files/paths that the agent must not read or send to the model, at both repository and global levels (e.g., a repo-local .codexignore plus a global ignore file). - Example: keep node_modules/ searchable for implementation checks, but never read or send .env, .env.*, .pem, id_, .aws/, .ssh/.

## Key Takeaways

- - The configuration should be deterministic and shareable across the team/repo, and also support user defaults, rather than relying on project documentation or conventions.
- Are you interested in implementing this feature?
- - Yes — I can contribute and tests.

---
_Auto-generated daily digest entry._
