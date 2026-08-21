# Vomit: Clean up Claude 5's token output with a separate LLM

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 284
- **Published (UTC):** 2026-08-20 15:26
- **Original:** https://github.com/zachahn/vomit

## Summary

Vomit converts Claude's token vomit into English by piping it through a local LLM. It's fully local (no telemetry) and has no external dependencies. I wrote a small blog post about this project: https://zachahn.com/posts/1787191554 Disclaimer: - The local LLM can only see what Claude tries to communicate (no access to any actions or files), so it hallucinates a bit - It's pretty slow - This is totally vibe-coded, only tested on Mac - There is a possibility you'll completely miss Claude's message.

## Key Takeaways

- You can use something like AgentsView to get the original messages, as Vomit does not touch anything during runtime (except technically it writes files to your TMPDIR) # Install the binary to your GOPATH go install github.com/zachahn/vomit@latest # Setup connection details to your LLM vomit init # Instructions on how to replace Claude's output via hooks vomit scrub -claude In addition, there's a non-invasive mode if you want to run Vomit on the side.
- List Claude session identifiers - vomit tail [<session_identifier>] .
- Translate Claude's tokens for the specified session, or follow the latest one - vomit help .

---
_Auto-generated daily digest entry._
