# Codex logging bug may write TBs to local SSDs

- **Source:** Hacker News
- **Rank (today):** #7
- **Ranking metrics:** HN score 357
- **Published (UTC):** 2026-06-22 07:30
- **Original:** https://github.com/openai/codex/issues/28224

## Summary

Codex SQLite feedback logs can write ~640 TB/year and rapidly consume SSD endurance Issue Codex is continuously writing a large amount of data to the local SQLite feedback log database: - ~/.codex/logs_2.sqlite - ~/.codex/logs_2.sqlite-wal - ~/.codex/logs_2.sqlite-shm On my machine, after about 21 days of uptime, the main SSD has written about 37 TB. Process/file-level checks show Codex SQLite logs are the main continuous writer. That extrapolates to roughly 640 TB/year.

## Key Takeaways

- On a 1 TB SSD, that is about 640 full-drive writes per year.
- Some consumer SSDs are rated around 600 TBW, so this could consume roughly a full drive's warranted write endurance in less than a year.
- Evidence Current retained rows in logs_2.sqlite: | metric | value | | retained rows | 681,774 | | estimated retained log content | 1,035.6 MiB | Level distribution: | level | estimated MiB | byte % | | TRACE | 732.5 | 70.7% | | INFO | 266.5 | 25.7% | | DEBUG | 30.6 | 3.0% | | WARN | 5.9 | 0.6% | Largest target+level pairs: | target | level | estimated MiB | | codex_api::endpoint::responses_websocket | TRACE | 527.4 | | codex_otel.log_only | INFO | 141.2 | | codex_otel.trace_safe | INFO | 121.2 | | log | TRACE | 97.4 | | codex_client::transport | TRACE | 60.1 | | codex_core::stream_events_utils | DEBUG | 27.5 | | codex_api::sse::responses | TRACE | 19.1 | The top sources are mostly global TRACE logs, mirrored telemetry logs, and raw websocket/SSE payload logging.

---
_Auto-generated daily digest entry._
