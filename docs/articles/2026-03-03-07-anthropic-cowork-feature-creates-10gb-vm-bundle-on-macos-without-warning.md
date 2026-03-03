# Anthropic Cowork feature creates 10GB VM bundle on macOS without warning

- **Source:** Hacker News
- **Rank (today):** #7
- **Ranking metrics:** HN score 366
- **Published (UTC):** 2026-03-02 14:21
- **Original:** https://github.com/anthropics/claude-code/issues/22543

## Summary

- Notifications You must be signed in to change notification settings - Fork 5.8k Description Description After using the cowork feature, Claude Desktop becomes extremely slow - slow startup, UI lag, and slow responses. Performance degrades over time even during a single session. Investigation VM Bundle (10GB) The cowork feature creates a VM bundle at: ~/Library/Application Support/Claude/vm_bundles/claudevm.bundle/rootfs.img This file grows to 10GB and is never cleaned up.

## Key Takeaways

- It regenerates quickly after deletion (deleted one day, back to 10GB the next).
- Cleanup Test Results Deleted vm_bundles, Cache, and Code Cache directories (reduced from 11GB to 639MB).
- Result: ~75% faster immediately after cleanup on tasks that previously failed/hung.

---
_Auto-generated daily digest entry._
