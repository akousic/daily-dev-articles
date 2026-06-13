# How to setup a local coding agent on macOS

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 428
- **Published (UTC):** 2026-06-12 17:34
- **Original:** https://ikyle.me/blog/2026/how-to-setup-a-local-coding-agent-on-macos

## Summary

How to Setup a Local Coding Agent on macOS Running Gemma 4 26B-A4B and Qwen3.6 35B-A3B locally with llama.cpp, MTP speculative decoding, multimodal support, and PI as a coding agent. I'd had my internet fail a few times recently leaving me stranded without a coding agent, and so when I saw the "Gemma 4 now runs 2x faster with MTP" Multi-Token Prediction update for Gemma 4 I decided to have a go at getting it running. I wanted a local coding agent setup that: - was fast enough to actually use on my Mac - worked through an OpenAI compatible API (so I could use it in other tools) - and preferably could handle screenshots/images when needed, so I can feed it screenshots of what it has made.

## Key Takeaways

- This video is realtime.
- And shows the agent responding at a perfectly usable speed.
- After a bit of testing the final setup I ended up with is: - llama.cpp built with Metal on macOS - Gemma 4 26B-A4B in GGUF format - A Q8 MTP draft model for speculative decoding - The Gemma 4 multimodal projector - Pi as the terminal coding agent This was tested on an Apple M1 Max with 64 GB unified memory, running macOS 15.7.7.

---
_Auto-generated daily digest entry._
