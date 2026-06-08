# What is the purpose of the lost+found folder in Linux and Unix? (2014)

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 223
- **Published (UTC):** 2026-06-05 08:08
- **Original:** https://unix.stackexchange.com/questions/18154/what-is-the-purpose-of-the-lostfound-folder-in-linux-and-unix

## Summary

There is a folder at the root of Linux and Unix operating systems called /lost+found/ What is it for? Under what circumstances would I interact with it? How would I interact with it?

## Key Takeaways

- If you run fsck, the filesystem check and repair command, it might find data fragments that are not referenced anywhere in the filesystem.
- In particular, fsck might find data that looks like a complete file but doesn't have a name on the system — an inode with no corresponding file name.
- This data is still using up space, but it isn't accessible by any normal means.

---
_Auto-generated daily digest entry._
