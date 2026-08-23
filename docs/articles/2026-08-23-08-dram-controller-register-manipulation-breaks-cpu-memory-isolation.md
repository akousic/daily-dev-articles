# DRAM Controller Register Manipulation Breaks CPU Memory Isolation

- **Source:** InfoQ
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-08-23 14:30
- **Original:** https://www.infoq.com/news/2026/08/amd-memory-exploit/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Security researcher Christopher Domas has unveiled skitter-creek-bath-salts, an open-source hardware security project that dismantles traditional CPU privilege boundaries by targeting the lowest layer of the physical memory hierarchy. By manipulating memory controller translation registers, the tool dynamically alters physical-to-DRAM address mappings at the hardware logic level. This enables unprivileged software to access isolated platform memory regions without triggering upstream architectural memory fences or fault exceptions.

## Key Takeaways

- Modern processor security architectures assume that physical addresses map deterministically to specific silicon storage locations.
- Standard security boundaries—including hypervisor Extended Page Tables, System Management Mode TSEG range limits, and Platform Security Processor (PSP) private carveouts—operate at the core and system fabric interconnect layer, before memory traffic reaches the controller.
- Domas discovered that memory controller translation registers sit beneath these access-control fences.

---
_Auto-generated daily digest entry._
