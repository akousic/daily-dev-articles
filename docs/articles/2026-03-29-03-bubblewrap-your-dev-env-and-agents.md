# BubbleWrap your dev env and agents

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-28 14:13
- **Original:** https://dpc.pw/posts/bubblewrap-your-dev-env-and-agents/

## Summary

OK, so the world is collapsing, everything is getting hacked, all dependencies are probably stealing keys and mining crypto, slop is everywhere, and I'm part of the problem. I'm going to isolate! I had this in mind for a long while, but only recently LLM agents became good enough that I actually find it really useful to let them go without babysitting every command they are trying to run.

## Key Takeaways

- So the goals are: - protect my systems from the slopus, - protect my systems from malicious dependencies (at least somewhat), - retain the usual UX.
- Because of the last point, I am not going to be doing separate user account, or a separate VM, or play with dockers.
- What I'm going to do is to use the BubbleWrap, to remount only parts of host system and home directory, and most of them in read-only mode.

---
_Auto-generated daily digest entry._
