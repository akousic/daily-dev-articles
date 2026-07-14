# git-absorb: git commit --fixup, but automatic

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-14 03:45
- **Original:** https://github.com/tummychow/git-absorb

## Summary

This is a port of Facebook's hg absorb, which I first read about on mozilla.dev.version-control: - Facebook demoed hg absorbwhich is probably the coolest workflow enhancement I've seen to version control in years. Essentially, when your working directory has uncommitted changes on top of draft changesets, you can runhg absorband the uncommitted modifications are automagically folded ("absorbed") into the appropriate draft ancestor changesets. This is essentially doinghg histedit+ "roll" actions without having to make a commit or manually make history modification rules.

## Key Takeaways

- The command essentially looks at the lines that were modified, finds a changeset modifying those lines, and amends that changeset to include your uncommitted changes.
- If the changes can't be made without conflicts, they remain uncommitted.
- This workflow is insanely useful for things like applying review feedback.

---
_Auto-generated daily digest entry._
