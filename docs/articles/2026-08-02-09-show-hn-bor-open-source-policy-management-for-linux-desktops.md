# Show HN: Bor – Open-source policy management for Linux desktops

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 107
- **Published (UTC):** 2026-08-02 09:06
- **Original:** https://getbor.dev/blog/2026-08-02-bor-v080-release/

## Summary

This release adds three new policy types — Thunderbird, Microsoft Edge for Business, and Firewalld zones — alongside a full web UI overhaul, finer-grained RBAC, and a dedicated security hardening pass. The complete changelog is on the GitHub release page. Thunderbird policy type Mozilla Thunderbird can now be managed on enrolled desktops with the same mechanism used for Firefox ESR.

## Key Takeaways

- The agent writes the managed policies.json that Thunderbird expects, merged from all bound policies, and removing the last policy restores the original file.
- Flatpak installations are detected and enforced alongside RPM/DEB installations, and the managed file is protected by the tamper watcher — external edits are detected and immediately restored.
- The web UI ships a full policy editor with the complete Thunderbird policy catalogue.

---
_Auto-generated daily digest entry._
