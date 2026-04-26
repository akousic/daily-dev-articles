# The fastest Linux timestamps

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-26 08:01
- **Original:** https://www.hmpcabral.com/2026/04/26/the-fastest-linux-timestamps/

## Summary

The fastest Linux timestamps 26 Apr 2026Table of contents Timing the timers One of my pet projects at my last job was to introduce distributed tracing to a low-latency pipeline (think 1–10 microseconds per stage) using OpenTelemetry. As part of this effort I spent a considerable amount of time designing, implementing, and optimising our own C++ tracing client library, as the official one has too much overhead. My goal was for the latency impact per component to stay under 5% so both developers and users would feel comfortable leaving traces always on in production; this translated to a budget of about 50–100 ns (a few hundred clock cycles) per span.

## Key Takeaways

- As you might imagine, at this scale you must carefully consider every aspect of the design and implementation, from ID generation to serialisation.
- One of these not-so-small details is how to timestamp spans.
- OTLP uses two time fields, one each for the start and end of the span as measured by the local wall clock.

---
_Auto-generated daily digest entry._
