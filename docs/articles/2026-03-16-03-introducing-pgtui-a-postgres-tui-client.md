# Introducing pgtui, a Postgres TUI client

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-16 00:08
- **Original:** https://kdwarn.net/programming/blog/227

## Summary

March 16, 2026 terminal, database, rust | permalink A couple years ago or so, I had an idea: "Write in markdown, save in database. This is how I'd like to interact with a database: use my favorite text editor and markdown to create a record (and mostly I'm thinking blog posts and the like), then that gets parsed out and stored in a database to get all the benefits of a database." Since then, the idea has evolved slightly, but not terribly much. Rather than markdown, it's TOML, though it could be markdown (or HTML or plaintext or, I suppose, something else entirely) within the TOML.

## Key Takeaways

- (And that is exactly how I'm writing at the moment.) Mostly, it's been a lot of work to implement the idea, and pgtui, a Postgres TUI client, is the result.
- Since the initial 0.1 release in April 2025, which was just a placeholder, there have been many features added and even more bugfixes.
- One of the more difficult things was figuring out how to go back and forth between TOML and Postgres types, and sqlx was leaned on quite heavily for that.

---
_Auto-generated daily digest entry._
