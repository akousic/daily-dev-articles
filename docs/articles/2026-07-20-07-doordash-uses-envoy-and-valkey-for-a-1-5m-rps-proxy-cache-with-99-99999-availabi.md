# DoorDash Uses Envoy and Valkey for a 1.5M RPS Proxy Cache with 99.99999% Availability

- **Source:** InfoQ
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-20 15:56
- **Original:** https://www.infoq.com/news/2026/07/doordash-entity-cache-proxy/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

DoorDash has developed Entity Cache, a transparent proxy caching platform to reduce redundant service-to-service requests across its microservices architecture. The company built the platform to address repeated requests for frequently accessed but infrequently changing data, which increased backend load, consumed additional compute resources, and contributed to higher tail latency as its microservices ecosystem expanded. According to DoorDash, the platform supports more than 100 endpoints across 50 services, serving over 1.5 million requests per second with 99.99999% availability.

## Key Takeaways

- Built on Envoy and Valkey, Entity Cache operates within DoorDash’s Envoy-based service mesh and intercepts HTTP and gRPC requests before they reach upstream services.
- The platform moves caching into the infrastructure layer by placing a transparent proxy between client services and upstream applications.
- Services continue making existing requests without requiring application code changes, while cache behavior is managed centrally through the service mesh.

---
_Auto-generated daily digest entry._
