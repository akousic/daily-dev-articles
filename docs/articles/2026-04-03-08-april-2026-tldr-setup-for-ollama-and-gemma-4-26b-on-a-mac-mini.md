# April 2026 TLDR Setup for Ollama and Gemma 4 26B on a Mac mini

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 146
- **Published (UTC):** 2026-04-03 09:35
- **Original:** https://gist.github.com/greenstevester/fc49b4e60a4fef9effc79066c1033ae5

## Summary

- Mac mini with Apple Silicon (M1/M2/M3/M4/M5) - At least 24GB unified memory for Gemma 4 26B - macOS with Homebrew installed Install the Ollama macOS app via Homebrew cask (includes auto-updates and MLX backend): brew install --cask ollama-app This installs: Ollama.app in/Applications/ ollama CLI at/opt/homebrew/bin/ollama open -a Ollama The Ollama icon will appear in the menu bar. Wait a few seconds for the server to initialize. Verify it's running: ollama list ollama pull gemma4:26b This downloads ~17GB.

## Key Takeaways

- Verify: ollama list # NAME ID SIZE MODIFIED # gemma4:26b 5571076f3d70 17 GB ...
- ollama run gemma4:26b "Hello, what model are you?" Check that it's using GPU acceleration: ollama ps # Should show CPU/GPU split, e.g.
- 14%/86% CPU/GPU Click the Ollama icon in the menu bar > Launch at Login (enable it).

---
_Auto-generated daily digest entry._
