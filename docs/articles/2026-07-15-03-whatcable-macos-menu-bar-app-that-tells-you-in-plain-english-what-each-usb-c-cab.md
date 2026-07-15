# whatcable: macOS menu bar app that tells you, in plain English, what each USB-C cable plugged into your Mac can actually do

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-14 12:00
- **Original:** https://github.com/darrylmorley/whatcable

## Summary

What can this USB-C cable actually do? Website: whatcable.uk (overview, screenshots, and CLI docs) A small macOS menu bar app that tells you, in plain English, what each USB-C cable plugged into your Mac can actually do, and why your Mac might be charging slowly. USB-C hides a lot under one connector.

## Key Takeaways

- Anything from a USB 2.0 charge-only cable to a 240W / 40 Gbps Thunderbolt 4 cable, all looking identical in your drawer.
- macOS already exposes the relevant info via IOKit; WhatCable surfaces it as a friendly menu bar popover.
- Per port, in plain English: - At-a-glance headline: Thunderbolt / USB4, USB device, Display connected, Charging only, Slow USB / charge-only cable, Nothing connected - Charging diagnostic: when something's plugged in, a banner identifies the bottleneck: - "Cable is limiting charging speed" (cable rated below the charger) - "Charging at 30W (charger can do up to 96W)" (Mac is asking for less, e.g.

---
_Auto-generated daily digest entry._
