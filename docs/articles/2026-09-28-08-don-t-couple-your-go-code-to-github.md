# Don't couple your Go code to GitHub

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 319
- **Published (UTC):** 2026-09-27 16:50
- **Original:** https://iain.rocks/blog/dont-couple-your-go-code-to-github

## Summary

Iain Cambridge Don't couple your Go code to GitHub Sep 27, 2026 One of the good features of Go is that you namespace your code with the location to fetch the code. This means if you host your Go code at http://github.com/thetrueares/boneclone then you have the line import “github.com/thetrueares/boneclone” and Go will fetch it using git. This makes it super easy to know where to go to report bugs for open source libraries and really easy to fetch and distribute go libraries without a centralised package management system.

## Key Takeaways

- For many, it’s literally the location of the git hosting, but this has some downsides, and you should use your own custom domain, and I’ll explain why.
- Problem The main problem with using your git hosting location is that your code is now coupled to a hosting provider.
- That is, if you move your git hosting to GitLab then you have to change your code!

---
_Auto-generated daily digest entry._
