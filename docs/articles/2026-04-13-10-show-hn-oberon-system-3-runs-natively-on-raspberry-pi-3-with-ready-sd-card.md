# Show HN: Oberon System 3 runs natively on Raspberry Pi 3 (with ready SD card)

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 216
- **Published (UTC):** 2026-04-12 13:06
- **Original:** https://github.com/rochus-keller/OberonSystem3Native/releases

## Summary

Releases: rochus-keller/OberonSystem3Native Native Raspberry Pi 3b version of the Oberon System 3 Finally it works on the Raspberry Pi 3b! Here is an image of the running system; I'm using the original Raspberry Pi monitor and a Lenovo ThinkPad TrackPoint keyboard which has three mouse buttons (as suggested for the Oberon system). I attached a ready image (oberon-rpi3.img) which you can flash onto an SD card if you want to run the system on your Raspi 3b yourself.

## Key Takeaways

- To do so, unpack the image; on Linux, run this command to flash the SD card: sudo dd if=oberon-rpi3.img of=/dev/sdX bs=4M conv=fsync status=progress && sync ; on Windows or Mac you can use the Raspberry Pi Imager or e.g.
- Of course you can also build the whole system yourself, and even the toolchain if you want.
- I attached the required Raspberry Pi bootfiles and a pre-compiled toolchain for Linux x64 for convenience.

---
_Auto-generated daily digest entry._
