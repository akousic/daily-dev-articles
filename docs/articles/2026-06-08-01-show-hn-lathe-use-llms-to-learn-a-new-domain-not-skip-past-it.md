# Show HN: Lathe – Use LLMs to learn a new domain, not skip past it

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 371
- **Published (UTC):** 2026-06-07 11:16
- **Original:** https://github.com/devenjarvis/lathe

## Summary

An experiment in using LLMs to teach you, rather than think for you. Lathe generates hands-on, multi-part technical tutorials on demand, with skills tuned to make content approachable. Then you work through them yourself, by hand, in a local UI built from the ground up for pleasant learning.

## Key Takeaways

- (Just like we did it in the stone age 😎) - Generate hands-on technical tutorials (single-part or a multi-part series) from any prompt - Work through the tutorial yourself in a purpose-built local UI - Use skills to ask questions, verify the tutorial, and extend it with a new part - Search, filter, and manage tutorials from your library - Every tutorial documents its sources, which model was used, and what prompt drove the "voice" for the tutorial Lathe is a combination of LLM skills and a Golang CLI used to store, manage, and view generated tutorials.
- After install (below), you can generate a tutorial inside any LLM session (Claude Code, Cursor, and Codex supported) by prompting something like: /lathe build a 3D Slicer in Erlang Then open lathe from any terminal: lathe serve # starts the web server, opens the browserDon't worry, we also have dark mode: Click the tutorial you want to read and start learning!
- The CLI has a bunch of other commands, but honestly those were built to give the LLM a deterministic way to manage tutorials.

---
_Auto-generated daily digest entry._
