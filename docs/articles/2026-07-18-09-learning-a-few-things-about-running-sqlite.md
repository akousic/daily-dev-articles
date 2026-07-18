# Learning a few things about running SQLite

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 289
- **Published (UTC):** 2026-07-17 17:45
- **Original:** https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/

## Summary

Learning a few things about running SQLite Hello! I’ve been working on a Django site recently, and I decided to use SQLite as the database. When I was getting started with using SQLite as database for a website I read a bunch of blog posts about how it is totally fine to use SQLite in production for a small site and I think it is totally fine, but what I did not fully appreciate is that SQLite is still a database, databases are complicated, and I do not know a lot about operating databases.

## Key Takeaways

- So here are a couple of small things I’ve been learning about running SQLite.
- This is the 4th website I’ve used SQLite for, and I think this one is harder because with the power of the Django ORM I’ve been making the database do more work than I was previously without Django.
- I started by turning on WAL mode like all the blog posts said to do and hoping for the best.

---
_Auto-generated daily digest entry._
