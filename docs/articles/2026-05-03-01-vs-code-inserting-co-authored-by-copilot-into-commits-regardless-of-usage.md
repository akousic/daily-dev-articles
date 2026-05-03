# VS Code inserting 'Co-Authored-by Copilot' into commits regardless of usage

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 1346
- **Published (UTC):** 2026-05-02 19:57
- **Original:** https://github.com/microsoft/vscode/pull/310226

## Summary

Conversation 📬 CODENOTIFYThe following users are being notified based on files changed in this PR: @lszomoruMatched files: | There was a problem hiding this comment. Pull request overview This PR changes the Git extension’s git.addAICoAuthor setting so that AI co-author trailers are enabled by default, making the default behavior automatically add a Co-authored-by trailer when AI-generated code contributions are detected. Changes: - Updates git.addAICoAuthor configuration default from"off" to"all" .

## Key Takeaways

- Show a summary per file | File | Description | |---|---| extensions/git/package.json | Switches the default value of git.addAICoAuthor to enable AI co-author trailers by default.
- | Copilot's findings - Files reviewed: 1/1 changed files - Comments generated: 1 | ], | || | "scope": "resource", | || | "default": "off", | || | "default": "all", | There was a problem hiding this comment.
- The configuration schema default was changed to "all", but the runtime fallback in extensions/git/src/repository.ts still calls config.get('addAICoAuthor', 'off') .

---
_Auto-generated daily digest entry._
