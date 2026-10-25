# We should be more ambitious with the software we build

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 622
- **Published (UTC):** 2026-10-24 21:47
- **Original:** https://danluu.com/ambitious/

## Summary

Since early this year, Michael Malis (of pgrust) has been showing me interesting things he's done and saying [W]e should be more ambitious with the software we build There is, understandably, a lot of skepticism about projects like pgrust because there are so many low-quality AI-generated projects out there. If I didn't know Malis and didn't look into it, I would just assume that pgrust was another vibe slopped project that's never going to work. But I know Malis well enough to trust his work without looking into it, and if you look into it a bit, you'll see that in testing pgrust, he's testing thoroughly enough that he's even uncovering real bugs in Postgres, such as this numerical bug that can cause valid SP-GiST operations to fail, this format cache bug that can cause incorrect results from JSONPath, this pgcrypto bug that can cause later operations to fail, multiple memory safety bugs in the dictionary loader, this money overflow bug, etc.

## Key Takeaways

- This isn't to say that pgrust is bug free, but it does indicate that there's a substantial amount of testing happening and, even if pgrust itself is never successful, just making the attempt will have improved Postgres in a durable way.
- The main pitch for pgrust is actually performance, and that's where the really interesting work is happening; if pgrust fails, it's possible that some of the optimizations they've demonstrated will make it into Postgres, Clickhouse, etc., but that's obviously less direct than filing Postgres bugs which get fixed.
- That being said, I find it understandable that, every time I see pgrust discussed on a news aggregator, most people dismiss it as vibeslop garbage because almost all of these rewrite projects are slop.

---
_Auto-generated daily digest entry._
