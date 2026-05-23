# Bun support is now limited and deprecated

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 525
- **Published (UTC):** 2026-05-22 17:24
- **Original:** https://github.com/yt-dlp/yt-dlp/issues/16766

## Summary

Due to foreseeable compatibility and security issues, yt-dlp's support for Bun as an ejs -compatible JavaScript runtime is being both limited and deprecated. As of the next yt-dlp and/or ejs release, only Bun versions 1.2.11 through 1.3.14 will be supported. The rationale for this change is twofold: - The minimum required version is being raised from 1.0.31 to 1.2.11 because building the ejs package with a version earlier than 1.2.0 results in the ejs lockfile being ignored, which is a significant security concern for users when considering all of the recent npm supply chain attacks.

## Key Takeaways

- Additionally, the support floor is being bumped to 1.2.11 instead of 1.2.0 because the ejs test suite cannot be run with versions of Bun earlier than 1.2.11 .
- - Bun was recently rewritten in Rust using Claude, and its development seems to have taken a turn towards being fully vibe-coded.
- This is alarming and disappointing for a number of reasons, and frankly it seems like a future headache that we'd prefer to avoid.

---
_Auto-generated daily digest entry._
