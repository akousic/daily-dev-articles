# The text in Claude Code’s “Extended Thinking” output

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 200
- **Published (UTC):** 2026-06-22 14:22
- **Original:** https://patrickmccanna.net/the-text-in-claude-codes-extended-thinking-output-is-not-authentic/

## Summary

Claude Code records each session to disk. Those logs include “thinking blocks” — the model’s own reasoning as it works. I went to inspect that reasoning this weekend and found a signature (600 characters long) and no text.

## Key Takeaways

- So I read the docs: https://platform.claude.com/docs/en/build-with-claude/extended-thinking Some details worth being aware of: - Claude encrypts its reasoning into that signature.
- - Anthropic holds the key.
- Your machine doesn’t receive it.

---
_Auto-generated daily digest entry._
