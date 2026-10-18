# The Commodore 64 hardware simulator: break chips and pins, see the results

- **Source:** Hacker News
- **Rank (today):** #7
- **Ranking metrics:** HN score 223
- **Published (UTC):** 2026-10-15 07:18
- **Original:** https://github.com/antirez/c64-hw-simulator

## Summary

c64-hw-sim simulates the motherboard of the Commodore 64, ASSY 250407, pin by pin. You can lift the leg of a chip, short it to ground or to +5V, pull a chip out of its socket, or open a resistor. Then you watch what the machine does: the picture on the monitor, the keyboard, every signal on the board.

## Key Takeaways

- The program knows the board's netlist (the electrical connections on the PCB) and how each chip behaves at its pins.
- It knows nothing about what a broken Commodore 64 looks like: when you simulate a broken part and the screen fills with garbage, that garbage was computed from the circuit, not chosen by someone who knew what to expect.
- Lift pin 17 (A7) of the color RAM before power on, and the machine boots and looks healthy.

---
_Auto-generated daily digest entry._
