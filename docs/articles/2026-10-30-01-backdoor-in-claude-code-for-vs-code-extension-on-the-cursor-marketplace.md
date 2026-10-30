# Backdoor in Claude Code for VS Code extension on the Cursor Marketplace

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 515
- **Published (UTC):** 2026-10-30 07:09
- **Original:** https://phorion.io/blog/offical-claude-code-vsx-compromise/

## Summary

TL;DR Phorion has detected a backdoor in the official Claude Code for VS Code extension bundle on the Cursor Marketplace that drops a persistent SSH backdoor across macOS, Linux, and Windows. This write-up focuses primarily on macOS, where the extension attempts to configure an SSH backdoor and establish persistence. Organisations should immediately review their environments for use of Claude Code for VSCode 2.1.313 and engage incident response where use of the extension is discovered.

## Key Takeaways

- Phorion has discovered a compromise of the official Claude Code for VS Code extension on the Cursor Marketplace, where the backdoored extension bundle contains a persistent Secure Shell (SSH) backdoor.
- Cursor has removed the associated release from its marketplace, additionally pulling NPM and VSCode versions for 2.1.313 from their relevant registries.
- While the implant includes setup and persistence logic for macOS, Linux, and Windows, we’re going to focus primarily on macOS in this post, calling out the key differences and a few implementation bugs on the other platforms along the way.

---
_Auto-generated daily digest entry._
