# We found an undocumented bug in the Apollo 11 guidance computer code

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 235
- **Published (UTC):** 2026-04-07 10:25
- **Original:** https://www.juxt.pro/blog/a-bug-on-the-dark-side-of-the-moon/

## Summary

The Apollo Guidance Computer (AGC) is one of the most scrutinised codebases in history. Thousands of developers have read it. Academics have published papers on its reliability.

## Key Takeaways

- Emulators run it instruction by instruction.
- We found a bug in it that had been missed for fifty-seven years: a resource lock in the gyro control code that leaks on an error path, silently disabling the guidance platform's ability to realign.
- We used Claude and Allium, our open-source behavioural specification language, to distil 130,000 lines of AGC assembly into 12,500 lines of specs.

---
_Auto-generated daily digest entry._
