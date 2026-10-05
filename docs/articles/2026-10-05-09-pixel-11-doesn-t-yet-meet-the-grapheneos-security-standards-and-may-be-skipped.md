# Pixel 11 doesn't yet meet the GrapheneOS security standards and may be skipped

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 380
- **Published (UTC):** 2026-10-05 13:02
- **Original:** https://discuss.grapheneos.org/d/41564-pixel-11-doesnt-yet-meet-the-grapheneos-security-standards-and-may-be-skipped

## Summary

We have a partial port of GrapheneOS to the Pixel 11 series after a week of work on it. We're unable to complete the port due to lack of support for ARM hardware memory tagging in software, firmware and near certainly hardware. It appears Google cut an important security feature to save money.

## Key Takeaways

- ARM hardware memory tagging (MTE) is used by GrapheneOS across the entire base OS including the kernel and every standard base OS process.
- It's only temporarily disabled for a few device-specific processes.
- It greatly improves protection against nearly all remote exploits and many local exploits.

---
_Auto-generated daily digest entry._
