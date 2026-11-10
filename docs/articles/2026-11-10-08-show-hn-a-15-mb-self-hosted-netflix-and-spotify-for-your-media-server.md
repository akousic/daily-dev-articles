# Show HN: A 15 MB self-hosted Netflix and Spotify for your media server

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 160
- **Published (UTC):** 2026-11-10 11:51
- **Original:** https://github.com/HolyArrs/HolyArrs

## Summary

English · 简体中文 · हिन्दी · Español · Français · العربية · Português · Русский · 日本語 · Deutsch · 한국어 · Italiano · Polski · Nederlands · Türkçe · Українська HolyArrs is one self-hosted app for your shows, movies and music. Browse like a streaming app, ask for what you want, and it handles the rest. About 15 MB to download · about 140 MB of RAM idle with 10,000 titles · amd64, arm64, armv7 The six apps it replaces download 718.2 MB together.

## Key Takeaways

- Quick start · Why · What it does · Moving from other apps · The manual · Help Save this as docker-compose.yml in a new folder on a local disk: name: HolyArrs services: holyarrs: image: holyarrs/holyarrs:latest container_name: holyarrs environment: - PUID=1000 - PGID=1000 - TZ=America/New_York volumes: - /your/local/path:/config - /path/to/movies:/movies #optional - /path/to/tv:/tv #optional - /path/to/music:/music #optional - /path/to/downloads:/downloads #optional ports: - 6262:6262 restart: unless-stoppeddocker compose up -d Open http://your-server:6262 and make the owner account.
- A short setup walks you through folders, a downloader and a Source.
- No API keys to hunt down.

---
_Auto-generated daily digest entry._
