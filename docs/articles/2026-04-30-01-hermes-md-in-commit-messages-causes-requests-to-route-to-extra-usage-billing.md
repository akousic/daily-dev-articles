# HERMES.md in commit messages causes requests to route to extra usage billing

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 1201
- **Published (UTC):** 2026-04-29 18:54
- **Original:** https://github.com/anthropics/claude-code/issues/53262

## Summary

Summary When a git repository's recent commit history contains the case-sensitive string HERMES.md , Claude Code routes API requests to "extra usage" billing instead of the included Max plan quota. This silently burned through $200 in extra usage credits while my Max 20x plan capacity remained largely untouched (13% weekly usage). Environment - Claude Code v2.1.119 - macOS (Apple Silicon) - Max 20x plan ($200/month) - Model: claude-opus-4-6[1m] (also reproduces with claude-opus-4-7 ) Reproduction Minimal reproduction — no project files needed: # This FAILS with "out of extra usage" (routes to extra usage billing) mkdir /tmp/test-fail && cd /tmp/test-fail git init && echo test > test.txt && git add .

## Key Takeaways

- && git commit -m "add HERMES.md" claude -p "say hello" --model "claude-opus-4-6[1m]" # => API Error: 400 "You're out of extra usage..." # This WORKS (routes to plan quota) mkdir /tmp/test-pass && cd /tmp/test-pass git init && echo test > test.txt && git add .
- && git commit -m "add hermes.md" claude -p "say hello" --model "claude-opus-4-6[1m]" # => "Hello!" # Cleanup rm -rf /tmp/test-fail /tmp/test-pass The trigger is the string HERMES.md in git commit messages — not the presence of a file with that name on disk.
- Claude Code includes recent commits in its system prompt, and something server-side routes the request differently when this string is present.

---
_Auto-generated daily digest entry._
