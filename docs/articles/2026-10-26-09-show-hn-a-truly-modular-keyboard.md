# Show HN: A Truly Modular Keyboard

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 263
- **Published (UTC):** 2026-10-25 03:47
- **Original:** https://github.com/notaroomba/keybytes

## Summary

Key Features • Video Demo • PCB • Case • Credits • License keybytes-demo.mp4 - Rearrangeable layout where every key is its own 1u PCB - CH32V003 RISC-V microcontroller on every key - STM32WB55RGV6 main board with Bluetooth and USB - Pogo pins on all 4 sides of every key for power and I2C - Magnetic cases to hold the modules together - Key programming from the main board over pogo pins - 2MB QSPI flash (W25Q16JV) to store the key firmware - Battery charging with the BQ25895 and solder pads for a 1S LiPo - Buck-Boost converter (TPS631000) - RGB status LED - USB-C with ESD protection - Ceramic Bluetooth antenna Designed in KiCad! There are two boards, the Keybit and the Keyword, and both are 1u (19.05mm x 19.05mm). A single key with a Cherry MX switch and a CH32V003.

## Key Takeaways

- Every side has pogo pins for 3.3V, GND and I2C so it can connect to the keyword or to other keybits, and the pads on the corners are for programming.
- Schematic: Layout: The main board that the keybits connect to.
- It is split into two PCBs that stack on top of each other.

---
_Auto-generated daily digest entry._
