# Workers RPC now works across Python and JavaScript

- **Source:** Cloudflare
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-08-03 16:31
- **Original:** https://blog.cloudflare.com/python-workers-rpc/

## Summary

Workers RPC now works across Python and JavaScript Two years ago, we introduced Workers RPC, built on Cap’n Proto RPC. This made it possible for Workers to call other Workers and Durable Objects’ methods, return live objects and call their methods, return functions, streams and get all the benefits of a Remote Procedure Call (RPC) system, without defining schemas or adding any dependencies. We called it “JavaScript-native RPC” because it made using RPC feel native to the language.

## Key Takeaways

- Last year, we made this work between web browsers and servers, and introduced Cap’n Web.
- Now we’re taking it cross-language.
- Normally, getting programs written in different languages to talk to each other is complicated: developers usually have to build custom APIs or adopt language-agnostic serialization formats like protobuf, so the two systems can understand each other.

---
_Auto-generated daily digest entry._
