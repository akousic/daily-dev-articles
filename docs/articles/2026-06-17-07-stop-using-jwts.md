# Stop Using JWTs

- **Source:** Hacker News
- **Rank (today):** #7
- **Ranking metrics:** HN score 462
- **Published (UTC):** 2026-06-16 16:49
- **Original:** https://gist.github.com/samsch/0d1f3d3b4745d778f78b230cf6061452

## Summary

TLDR: JWTs should not be used for keeping your user logged in. They are not designed for this purpose, they are not secure, and there is a much better tool which is designed for it: regular cookie sessions. If you've got a bit of time to watch a presentation on it, I highly recommend this talk: https://www.youtube.com/watch?v=pYeekwv3vC4 (Note that other topics are largely skimmed over, such as CSRF protection.

## Key Takeaways

- You should learn about other topics from other sources.
- Also note that "valid" usecases for JWTs at the end of the video can also be easily handled by other, better, and more secure tools.
- Specifically, PASETO.) A related topic: Don't use localStorage (or sessionStorage) for authentication credentials, including JWT tokens: https://www.rdegges.com/2018/please-stop-using-local-storage/ The reason to avoid JWTs comes down to a couple different points: - The JWT specification is specifically designed only for very short-live tokens (~5 minute or less).

---
_Auto-generated daily digest entry._
