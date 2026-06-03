# 1-Click GitHub Token Stealing via a VSCode Bug

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 606
- **Published (UTC):** 2026-06-02 15:29
- **Original:** https://blog.ammaraskar.com/github-token-stealing/

## Summary

Just by clicking a link, it’s possible for an attacker to steal a GitHub token that can read and write to your repos, including private ones. Table of Contents - Background - VSCode Webview Security Model - PoC and Protecting Yourself - What VSCode Did Well - Why Full Disclosure - Timeline Background Did you know GitHub has this really cool feature called github.dev? On any repository you have access to, if you can change the url from github.com to github.dev or you click this little menu item: You’ll be launched into a little light-weight version of VSCode that runs entirely in your browser (I guess that’s one advantage of having your app written with electron).

## Key Takeaways

- This browser instance of VSCode is pretty powerful, you can view all the files in the repo (even if it’s a private one), you can send out pull requests and even make commits.
- This functionality is achieved by github.com POSTing over an OAuth token to github.dev that allows it to interact with GitHub on your behalf.
- The token is not scoped to the particular repo you interacted with, meaning it has full access to every other repo that you have access to.

---
_Auto-generated daily digest entry._
