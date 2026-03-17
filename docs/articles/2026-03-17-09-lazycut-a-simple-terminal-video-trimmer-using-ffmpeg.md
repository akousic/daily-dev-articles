# Lazycut: A simple terminal video trimmer using FFmpeg

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 204
- **Published (UTC):** 2026-03-16 12:05
- **Original:** https://github.com/emin-ozata/lazycut

## Summary

Terminal-based video trimming tool. Mark in/out points and export trimmed clips with aspect ratio control. brew tap emin-ozata/homebrew-tap brew install lazycut Download the latest Windows binary from the releases page: lazycut_X.X.X_windows_amd64.zip Extract and add to your PATH, or run directly.

## Key Takeaways

- Dependencies: - ffmpeg: winget install ffmpeg or download from ffmpeg.org - chafa: Install via Scoop: scoop install chafa Or build from source: git clone https://github.com/emin-ozata/lazycut.git cd lazycut go build ./lazycut video.mp4 lazycut <video-file> | Key | Action | |---|---| Space | Play/Pause | h / l | Seek ±1s | H / L | Seek ±5s | i / o | Set in/out points | Enter | Export | ?
- | Help | q | Quit | Repeat counts work: 5l = seek forward 5 seconds.

---
_Auto-generated daily digest entry._
