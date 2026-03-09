# We should revisit literate programming in the agent era

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 269
- **Published (UTC):** 2026-03-08 19:58
- **Original:** https://silly.business/blog/we-should-revisit-literate-programming-in-the-agent-era/

## Summary

We Should Revisit Literate Programming in the Agent Era Literate programming is the idea that code should be intermingled with prose such that an uninformed reader could read a code base as a narrative, and come away with an understanding of how it works and what it does. Although I have long been intrigued by this idea, and have found uses for it in a couple1 of different cases2, I have found that in practice literate programming turns into a chore of maintaining two parallel narratives: the code itself, and the prose. This has obviously limited its adoption.

## Key Takeaways

- Historically in practice literate programming is most commonly found as Jupyter notebooks in the data science community, where explanations live alongside calculations and their results in a web browser.
- Frequent readers of this blog will be aware that Emacs Org Mode supports polyglot literate programming through its org-babel package, allowing execution of arbitrary languages with results captured back into the document, but this has remained a niche pattern for nerds like me.
- Even for someone as enthusiastic about this pattern as I am, it becomes cumbersome to use Org as the source of truth for larger software projects, as the source code essentially becomes a compiled output, and after every edit in the Org file, the code must be re-extracted and placed into its destination ("tangled", in Org Mode parlance).

---
_Auto-generated daily digest entry._
