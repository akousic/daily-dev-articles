# Cloudflare Introduces Private Origins for Application Services

- **Source:** InfoQ
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-11-15 19:40
- **Original:** https://www.infoq.com/news/2026/11/cloudflare-private-origins/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

## Summary

Cloudflare recently made Application Services for Private Origins generally available, allowing public traffic to reach applications hosted on private networks without exposing their IP addresses or opening inbound firewall ports. Private-to-private connectivity is not yet supported. Announced in closed beta in June, the service is now generally available with a simplified configuration: private IP addresses are automatically detected in proxied DNS records, and private routing can be configured through the DNS API.

## Key Takeaways

- Enrique Somoza, product development manager at Cloudflare, writes: We launched this capability (...) to address a problem we kept hearing from customers: Their internal APIs, AI agent backends, MCP servers, and operational tools weren’t built to face the Internet, but those services still need to accept requests from partners, customers, or agents over the Internet.
- Existing Cloudflare connectivity can be used to apply WAF, bot management, rate limiting, caching, and Workers to private origins, just as with public-facing applications.
- The service also supports private TCP/UDP origins through Spectrum and private connectivity for Workers.

---
_Auto-generated daily digest entry._
