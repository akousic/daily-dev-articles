# Google BigQuery Previews Cross-Region SQL Queries for Distributed Data

- **Source:** InfoQ
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-08 14:32
- **Original:** https://www.infoq.com/news/2026/03/google-bigquery-cross-region-sql/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Google Cloud has recently announced the preview of a global queries feature for BigQuery. The new option lets developers run SQL queries across data stored in different geographic regions without first moving or copying the data to aggregate the results. Removing the need for ETL pipelines, global queries automatically fetch and combine results from each region, simplifying analytics for companies with distributed datasets while letting them control where the query runs.

## Key Takeaways

- Wawrzek Hyska, product manager at Google, and Oleh Khoma, software engineer at Google, write: In the background, BigQuery automatically handles the data movement required to execute the query, giving you a seamless, zero-ETL experience for multi-location analytics.
- BigQuery identifies different parts of the query that must be executed in different regions and runs them accordingly.
- Next, results of these partial queries are transferred to a selected location when the main query is run (with an optimization attempt to minimize the size of transfer).

---
_Auto-generated daily digest entry._
