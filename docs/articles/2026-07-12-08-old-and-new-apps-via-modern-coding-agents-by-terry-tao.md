# Old and new apps, via modern coding agents by Terry Tao

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 173
- **Published (UTC):** 2026-07-12 11:09
- **Original:** https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/

## Summary

I have been interested in machine-assisted ways to do and teach mathematics from as far back as 1999, when I started coding several applets in Java 1.0, both for my complex analysis and linear algebra courses, to visualize various mathematical objects I was interested in (such as honeycombs or Besicovitch sets). This was moderately successful; but the applets were time-consuming to program, and eventually the standards for web pages stopped supporting this version of Java, and the applets became non-functional. However, in the last few days I have begun the process of migrating much of my old web page and blog data to a more maintainable repository, using modern AI assistance.

## Key Takeaways

- As an experiment, I asked the agent to port my old applets to a modern supported language (we landed on Javascript), and it managed to do so in a matter of hours, with all of my old applets now functional again, with even a few graphical upgrades (for instance, the Besicovitch set applet is now colorized, in contrast to my original monochrome version).
- I am particularly pleased to see the honeycomb applet that I wrote with Allen Knutson in 1999 come back to life, as this was a particularly tricky one to code by hand: Notoriously, LLM-based coding agents can create various blatant or subtle bugs in their code; but in the porting of these two dozen or so applets, I could only find one minor bug (the handling of a drag event in one of the complex analysis applets had unwanted behavior when dragging outside of the main box), and in fact the agent identified two bugs in the original code that I was not aware of, so it ended up being a net wash as far as code quality was concerned.
- In any event, as these applets are meant to be secondary visual aids rather than critical components of a mathematical argument, the downside risk of such bugs is relatively low.

---
_Auto-generated daily digest entry._
