# SQLite WAL-reset database corruption bug

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-11 04:18
- **Original:** https://sqlite.org/wal.html#walresetbug

## Summary

The default method by which SQLite implements atomic commit and rollback is a rollback journal. Beginning with version 3.7.0 (2010-07-21), a new "Write-Ahead Log" option (hereafter referred to as "WAL") is available. There are advantages and disadvantages to using WAL instead of a rollback journal.

## Key Takeaways

- Advantages include: But there are also disadvantages: The traditional rollback journal works by writing a copy of the original unchanged database content into a separate rollback journal file and then writing changes directly into the database file.
- In the event of a crash or ROLLBACK, the original content contained in the rollback journal is played back into the database file to revert the database file to its original state.
- The COMMIT occurs when the rollback journal is deleted.

---
_Auto-generated daily digest entry._
