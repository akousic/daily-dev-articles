# Show HN: Esp32sim – Run ESP32 firmware in the browser

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 188
- **Published (UTC):** 2026-10-17 13:51
- **Original:** https://github.com/mikroverk/esp32sim

## Summary

Instruction-level emulation of four ESP32 SoCs, across both of Espressif's CPU architectures. Each boots the real mask ROM, the real 2nd-stage bootloader and an unmodified application image — no patched firmware, no stubs in the way — with enough of the SoC modelled to run real projects end to end. No cloud, no accounts.

## Key Takeaways

- The classic ESP32 also boots its ECO3 ROM on dual LX6 cores, with GPIO, UART and timers; --board ttgo-tdisplay adds the LilyGO TTGO T-Display's ST7789 and buttons.
- | | ESP32-S3 | ESP32-C3 | ESP32-C6 | |---|---|---|---| | CPU | 2 × Xtensa LX7 @ 240 MHz | 1 × RISC-V RV32IMC @ 160 MHz | 1 × RISC-V RV32IMAC @ 160 MHz | | Command | esp32sim | esp32sim-c3 | esp32sim-c6 | | Core crate | xtensa-lx7 | riscv-rv32 | riscv-rv32 (+ the A extension) | | Reported full-listing decoder checks | 977 k instructions, 0 mismatches | 161 k instructions, 0 mismatches | 126 k instructions, 0 mismatches | | Boots | ROM → bootloader → FreeRTOS → app | ROM → bootloader → FreeRTOS → app | ROM → bootloader → FreeRTOS → app | | Boards / displays | ST7735, ST7701S 480×480 + touch, WS2812, camera, audio | none — console only | ST7789 172×320 over SPI+DMA, WS2812, an 802.15.4 energy-detect stand-in | | WiFi | virtual AP, WPA2, DHCP/DNS/NTP, NAT to the real network, HTTPS | the same virtual AP and network: scan, WPA2, DHCP, NAT (one station) | the same virtual AP and network: scan, WPA2, DHCP, NAT (one station, legacy rates) | | Speed | block interpreter + AArch64 JIT, ~150–240 Minsn/s | plain interpreter (no block cache or JIT yet) — still well above real time on hello_world | same interpreter | | In the browser | yes (WebAssembly) | yes (WebAssembly) | yes (WebAssembly) | | Reported hardware comparisons | JTAG trace, 8000 steps after timing-loop resynchronization | console diff, 205/208 lines identical | console diff, 203/204 lines identical | | Status | mature | draft — see docs/esp32c3.md | draft — see docs/esp32c6.md | These full-listing and hardware counts describe earlier manual runs.
- CI runs the checked-in sampled decoder corpora and emulator golden outputs; it excludes the external full-listing tests.

---
_Auto-generated daily digest entry._
