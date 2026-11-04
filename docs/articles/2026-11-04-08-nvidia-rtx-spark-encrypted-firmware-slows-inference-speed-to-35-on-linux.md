# Nvidia RTX Spark encrypted firmware slows inference speed to 35% on Linux

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 536
- **Published (UTC):** 2026-11-04 08:46
- **Original:** https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop

## Summary

Linux on the Nvidia RTX Spark Laptop: What Actually Works A hands-on look at dual-booting Linux on the Nvidia RTX Spark laptop, the GPU clock throttling bug found, and why WSL still wins. Can you run Linux on the Nvidia RTX Spark laptop? Yes, but it comes with a serious catch.

## Key Takeaways

- Linux installs and runs on RTX Spark laptops like the MSI Prestige N16 Flip AI Plus, including GPU acceleration through Nvidia’s open kernel driver.
- The problem is clock speed: once the laptop is plugged into wall power, the GPU gets locked to roughly 780 MHz on Linux instead of the 2 GHz-plus it hits on Windows.
- That turns a chip capable of around 65 tokens per second on a 120 billion parameter model into one struggling to break 14 tokens per second, for reasons tied to power management firmware that Linux currently can’t read.

---
_Auto-generated daily digest entry._
