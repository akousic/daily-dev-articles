# Codex CLI installs a persistent, self-updating background daemon by default

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 368
- **Published (UTC):** 2026-10-12 18:29
- **Original:** https://github.com/openai/codex/issues/48195

## Summary

Repository navigation CLI: make daemon_auto_start opt-in — a persistent, self-updating background daemon shouldn't be the default #48195 Description What variant of Codex are you using? CLI — 0.157.0, installed via npm install -g @openai/codex, Linux (WSL2) What feature would you like to see? Please make daemon_auto_start opt-in (default false) for the CLI, or at least ask once before turning it on.

## Key Takeaways

- Since 0.157.0, just opening an interactive codex session: - Starts a persistent background daemon (codex app-server --managed-daemon).
- It runs in its own session with no TTY and keeps running after every Codex window is closed (reparented to PID 1) until codex app-server daemon stop or a reboot.
- - Copies the whole platform package (~374 MB: codex, codex-code-mode-host, bundled bwrap/zsh/rg) into ~/.codex/packages/app-server-daemon/releases/<version>/ — byte-identical to what npm had just installed — and runs the daemon from that copy.

---
_Auto-generated daily digest entry._
