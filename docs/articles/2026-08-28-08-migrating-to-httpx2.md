# Migrating to HTTPX2

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 180
- **Published (UTC):** 2026-08-28 11:51
- **Original:** https://github.com/openai/openai-python/blob/main/httpx2.md

## Summary

The OpenAI Python SDK now uses HTTPX2 for its synchronous and asynchronous HTTP clients. HTTPX2 is installed automatically with openai; the previous httpx package is not. This guide explains what changes for applications that interact with the SDK's HTTP layer.

## Key Takeaways

- If you construct an OpenAI or AsyncOpenAI client without providing http_client, your existing API calls, parsed response models, streaming APIs, authentication, retries, and numeric timeouts continue to work: from openai import OpenAI client = OpenAI(timeout=30.0) response = client.responses.create(model="gpt-5.5", input="Hello") No HTTPX2 extra or separate installation is required: pip install openai If your application imported httpx only because an earlier SDK installed it transitively, add your own httpx dependency or migrate those imports to httpx2.
- Installing the SDK no longer installs httpx for you.
- HTTPX2 changes the default TLS trust store, including for applications that use the SDK's default HTTP client.

---
_Auto-generated daily digest entry._
