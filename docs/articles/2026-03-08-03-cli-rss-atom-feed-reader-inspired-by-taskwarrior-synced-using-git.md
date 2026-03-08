# CLI RSS/Atom feed reader inspired by Taskwarrior, synced using git

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-08 08:14
- **Original:** https://github.com/kantord/blogtato

## Summary

A CLI RSS/Atom feed reader inspired by Taskwarrior. - Subscribe to RSS and Atom feeds - Simple query language for filtering by feed, read status, and date, with grouping and export - Git-based sync across machines with conflict-free merge (why git?) - No accounts, no servers, no continuous network dependency - Mark content as read - Designed to be distraction free, minimalistic and work out of the box cargo install blogtato git based synchronization is entire optional. blogtato can work entirely offline on a single device.

## Key Takeaways

- To set up git synchronization, create a private repo on your git host, then: # On your first machine blog clone user/repo # From now on, sync fetches feeds and pushes/pulls from the remote # with no remote repository, `blog sync` just pulls the latest posts from # all feeds blog sync On your device(s), run the same blog clone to pull down your feeds and posts.
- Don't worry about setting git sync up if you are just trying blogtato out: you can run blog clone user/repo later and your existing feeds will be merged with the remote automatically.
- Once you set up your git -based sync, or if you decided to skip it, subscribe to your favorite feeds using blog feed add : blog feed add https://michael.stapelberg.ch blog feed add https://www.justinmklam.com Fetch and list latest posts: blog sync blog Read whatever you found interesting by referring to its shorthand blog df read You can subscribe to blogtato releases to know when new features or fixes are available: blog feed add https://github.com/kantord/blogtato/releases.atom # Subscribe to a feed blog feed add https://news.ycombinator.com/rss # Fetch new posts and sync with git remote blog sync # Show posts (defaults to unread posts from the last 3 months, grouped by week) blog # Group by date, week, or feed blog /d blog /w blog /f # Combine groupings blog /d /f # Filter by feed shorthand blog @hn # Filter by read status blog .unread blog .read blog .all # Filter by date blog 1w..

---
_Auto-generated daily digest entry._
