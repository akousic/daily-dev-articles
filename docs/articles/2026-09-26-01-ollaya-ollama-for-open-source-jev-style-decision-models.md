# Ollaya – Ollama for open-source, Jev-style decision models

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 550
- **Published (UTC):** 2026-09-25 18:33
- **Original:** https://ollaya.dev/

## Summary

Run decision models locally. Ask typed questions about any text or JSON and get calibrated answers in milliseconds. Private, open source, on your own hardware.

## Key Takeaways

- ollaya run decider --preset agent '{ "request": "Fix the typo in README.md", "command": "git push --force origin main"}' | Answers returned by the model | | | |---|---|---| | Question | Answer | Probability | |---|---|---| | action | block | 0.53 | | on_task | no | 0.75 | | risk | 1.23 / 2 could lose local work | 0.15 | | destructive | yes | 0.90 | Fast Decisions in milliseconds.
- A decision model answers in a single forward pass, with no token-by-token generation.
- On your own GPU, a five-question request to Laya takes about 10 ms, end to end through the HTTP API.

---
_Auto-generated daily digest entry._
