# SDL Now Supports DOS

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 267
- **Published (UTC):** 2026-04-24 16:20
- **Original:** https://github.com/libsdl-org/SDL/pull/15377

## Summary

Add DOS platform support (DJGPP)#15377 Conversation Seeking breaks otherwise. We might be able to just fflush() before or seeking instead? Turns out DosBox-X was having trouble with the Sound Blaster or something; standard DosBox works correctly directly from the interrupt handler, and without doubling the buffer size.

## Key Takeaways

- This is MUCH faster than just leaving buffering disabled, and also works around getting bogus reads after an fseek.
- SDL_LoadWAV on test/sample.wav no longer takes several seconds to finish, and comes up with the correct data.
- I wonder if we're triggering this in LoadWAV because we're malloc'ing data between seeks/reads, and it's causing the djgpp transfer buffer to change.

---
_Auto-generated daily digest entry._
