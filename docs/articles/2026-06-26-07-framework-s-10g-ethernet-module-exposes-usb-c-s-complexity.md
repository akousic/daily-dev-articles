# Framework's 10G Ethernet module exposes USB-C's complexity

- **Source:** Hacker News
- **Rank (today):** #7
- **Ranking metrics:** HN score 271
- **Published (UTC):** 2026-06-26 01:10
- **Original:** https://www.jeffgeerling.com/blog/2026/framework-10g-ethernet-module-usb-c-complexity/

## Summary

Framework's 10G Ethernet module exposes USB-C's complexity I've been following WisdPi's development of various 5 Gbps and 10 Gbps Ethernet adapters for the past couple years. They use newer Realtek Ethernet chips, which sometimes have performance quirks—most frequently encountered under Linux. In today's video, I tested the new WisdPi 10G Ethernet Expansion Card for Framework computers.

## Key Takeaways

- It fits in any available Framework Expansion slot—even on the Framework Desktop.
- But Expansion Cards use USB-C for their connection to the mainboard—and therein lies the rub...
- The main problem is USB-C's bandwidth complexity—especially when paired with the Realtek RTL8159 Ethernet controller, which requires USB 3.2 Gen 2x2 (20 Gbps) to get the full rated 10 Gbps speeds.

---
_Auto-generated daily digest entry._
