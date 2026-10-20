# MicroG: Free-libre re-implementation of Google's proprietary Android user space

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 318
- **Published (UTC):** 2026-10-20 06:37
- **Original:** https://github.com/microg/GmsCore/wiki

## Summary

Repository navigation Home microG GmsCore is a free software reimplementation of Google's Play Services. It allows applications calling proprietary Google APIs to run on AOSP-based ROMs like LineageOS, acting as a free replacement for the non-free, proprietary Google Play Services (sometimes referred to as the more generic term "GApps"). It is a powerful tool to reclaim your privacy and freedom while enjoying Android core features (although apps you use that take advantage of it may still be using proprietary libraries to communicate with microG, just as they do when communicating with the actual Google Play Services).

## Key Takeaways

- - Opt-in to Google Services and extend application support - On-/Offline location service - Easy on battery, memory and CPU - No bloatware - Works on real devices, test emulators and virtual mobile infrastructure - Free (open source) (Apache 2.0 licensed) Your Android system needs to support signature spoofing so GmsCore can pretend the existence of the official Play Services to applications calling Google APIs.
- See the linked page to know about ROM providing out-of-the-box support and what you can do about the other ones.
- GmsCore includes the Unified Network Location Provider module (UnifiedNlp) which handles application calls to Google's network location provider.

---
_Auto-generated daily digest entry._
