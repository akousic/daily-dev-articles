# Cloudflare Optimizes Edge Stack for High-Core CPUs Instead of Large Cache

- **Source:** InfoQ
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-25 14:53
- **Original:** https://www.infoq.com/news/2026/04/cache-parallelism-cloudflare/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Cloudflare recently introduced its Gen 13 servers, marking a shift in how its network handles traffic. Instead of relying on large CPU caches for speed, the company redesigned its software to leverage many more processor cores working in parallel in its latest AMD-based servers. Highlighting the importance of hardware–software co-design, Cloudflare moved away from relying on very large CPU caches that had compensated for software that did not scale well across many cores.

## Key Takeaways

- The hardware and software changes enable greater capacity per server and improved performance for edge applications, while enhancing energy efficiency.
- According to the specifications, Gen 13 is designed with a 192-core AMD EPYC Turin 9965 processor, 768 GB of DDR5-6400 memory, 24 TB of PCIe 5.0 NVMe storage, and a dual 100 GbE network interface card.
- The new specs allow Gen 13 servers to handle up to twice as much traffic as the previous Gen 12, which runs on the AMD Genoa-X 9684X, while meeting the same response-time targets.

---
_Auto-generated daily digest entry._
