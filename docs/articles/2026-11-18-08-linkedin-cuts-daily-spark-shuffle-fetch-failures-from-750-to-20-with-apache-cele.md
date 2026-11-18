# LinkedIn Cuts Daily Spark Shuffle Fetch Failures from 750 to 20 with Apache Celeborn

- **Source:** InfoQ
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-18 21:47
- **Original:** https://www.infoq.com/news/2026/11/linkedin-celeborn-remote-shuffle/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

LinkedIn has deployed Apache Celeborn as a shared remote shuffle platform across the majority of its Apache Spark and Apache Flink workloads, separating intermediate data storage from compute infrastructure. The deployment reduces daily shuffle fetch failures from approximately 750 to 20, lowers compute costs by 10%, and improves application runtimes by 14%, compared with its previous Magnet implementation. Daily shuffle fetch failures decreased from approximately 750 to 20 (Source: LinkedIn Blog Post) LinkedIn's offline data platform executes more than 300,000 Spark jobs daily across thousands of production nodes, consuming approximately 200 petabyte-hours of compute.

## Key Takeaways

- As the company moves toward a unified Flink architecture for real-time and historical processing, large-scale backfills introduce additional shuffle workloads.
- Shuffle moves intermediate data between processing stages, potentially stressing networks, disks, and application runtimes.
- LinkedIn previously addressed shuffle read inefficiencies with Magnet, its push-based shuffle implementation contributed to Apache Spark 3.2.

---
_Auto-generated daily digest entry._
