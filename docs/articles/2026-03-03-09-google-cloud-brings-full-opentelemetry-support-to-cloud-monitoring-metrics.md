# Google Cloud Brings Full OpenTelemetry Support to Cloud Monitoring Metrics

- **Source:** InfoQ
- **Rank (today):** #9
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-03-03 14:54
- **Original:** https://www.infoq.com/news/2026/03/google-cloud-opentelemetry/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Google Cloud recently unveiled broad support for the OpenTelemetry Protocol (OTLP) in Cloud Monitoring, marking a step toward unifying telemetry collection across its observability stack. With this rollout, users can now send metrics in OTLP format, alongside traces and logs, to Cloud Monitoring through a vendor-agnostic pipeline, enabling more flexible, standard-based instrumentation and simpler, more consistent telemetry ingestion. The update builds on previous support for OTLP trace ingestion and underscores Google Cloud's commitment to OpenTelemetry as a universal format and API for telemetry data.

## Key Takeaways

- Developers can use OpenTelemetry SDKs to generate metrics, then send them via OTLP either directly to Cloud Monitoring or through an OpenTelemetry Collector.
- By default, ingested OTLP metrics are stored like Prometheus-formatted data and are fully queryable using standard Monitoring tools.
- Support for OTLP metrics introduces several enhancements that improve observability workflows: delta-type metrics, which reduce client-side memory use by reporting only counter changes; exponential histograms for dynamic bucket sizing; and expanded naming conventions that embrace dots and slashes, enabling better alignment with standard OpenTelemetry semantic conventions.

---
_Auto-generated daily digest entry._
