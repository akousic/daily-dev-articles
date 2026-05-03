# DuckLake 1.0: Data Lake Format with SQL Catalog Metadata

- **Source:** InfoQ
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-03 14:56
- **Original:** https://www.infoq.com/news/2026/05/ducklake-sql-catalog/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

DuckDB Labs recently released DuckLake 1.0, a data lake format that stores table metadata in a SQL database rather than across many files in object storage. The first implementation is available as a DuckDB extension and includes catalog-stored small updates, improved sorting and partitioning options, and compatibility with Iceberg-style data features. According to the DuckDB team, file-based metadata in lake formats leads to complex coordination, slow metadata operations, and many small files in object storage.

## Key Takeaways

- While Apache Iceberg, Delta Lake, and Apache Hudi store metadata mainly as files in object storage, sometimes adding catalog services on top, DuckLake stores it directly in a SQL database.
- A year ago, the so-called "DuckLake manifesto" was published, arguing that lakehouse metadata should be stored in a database rather than spread across many files in object storage.
- The team writes: We are happy to announce DuckLake v1.0, almost a year after we released our first sketch of the specification.

---
_Auto-generated daily digest entry._
