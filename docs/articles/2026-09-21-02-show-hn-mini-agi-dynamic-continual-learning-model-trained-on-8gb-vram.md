# Show HN: Mini-AGI – Dynamic continual learning model trained on 8GB VRAM

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 234
- **Published (UTC):** 2026-09-21 04:42
- **Original:** https://github.com/volotat/mini-AGI/

## Summary

mini-AGI - is a continual learning byte-level language model that assembles its own architecture, trains from scratch on a single 8 GB VRAM GPU, and keeps learning from everything it reads. It stores its weights as ordinary files on disk and pages them onto the card as it needs them, so the parameter count is bounded by free disk space rather than by VRAM. It grows new capacity while training when it runs short, prunes what nothing asks for, and reads through exactly the same code path it serves on.

## Key Takeaways

- Targeted at a PC or laptop with at least an 8 GB VRAM GPU on the board.
- NOTE: as of now this is a small toy-level model.
- Do not expect a frontier level capabilities.

---
_Auto-generated daily digest entry._
