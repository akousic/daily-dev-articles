# WiiFin – Jellyfin Client for Nintendo Wii

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 208
- **Published (UTC):** 2026-04-13 23:33
- **Original:** https://github.com/fabienmillet/WiiFin

## Summary

Jellyfin client for the Nintendo Wii WiiFin is an experimental homebrew client for Jellyfin, built specifically for the Nintendo Wii. It provides a lightweight, console-friendly media browsing and playback experience, written in C++ using GRRLIB and MPlayer CE. 🚧 Experimental – functional but still under active development.

## Key Takeaways

- Expect rough edges on real hardware.
- - Authentication: login with username/password or via QuickConnect (approve on another device) - Saved profiles: multiple accounts stored securely (access token only, no password stored) - Library browsing: movies, TV shows, music libraries with cover art loaded from the server - Detail view: synopsis, rating, genres, cast, director, audio/subtitle track selection - Continue Watching and Next Up rows - TV shows: season and episode navigation - Video playback: server-side transcoding streamed through the integrated MPlayer CE engine - Music playback: audio libraries, album/track navigation - Player overlay: seek bar, volume control, next/prev episode, audio & subtitle track switching, intro skip - Playback reporting: progress sent back to the Jellyfin server (resume where you left off) - HTTPS: TLS connections via mbedTLS (self-signed certificates supported) - Wiimote IR pointer and virtual on-screen keyboard - Background music on menus - Ships as a ready-to-use .dol and installable.wad (Wii / vWii) - Direct-play is not supported; all video is transcoded by the server - No 5.1 multi-channel audio (stereo only via transcoding) - Subtitle rendering relies on the server embedding them into the video stream - devkitPro with devkitPPC ,libogc , andwii-dev portlibs - Graphics: GRRLIB ,libpngu ,freetype ,libjpeg - mbedTLS (bundled under libs/ , cross-compiled automatically by the CI) - Optional: MPlayer CE compiled as libmplayer.a — required for video playback.
- See MPLAYER_CE_BUILD.md for instructions.

---
_Auto-generated daily digest entry._
