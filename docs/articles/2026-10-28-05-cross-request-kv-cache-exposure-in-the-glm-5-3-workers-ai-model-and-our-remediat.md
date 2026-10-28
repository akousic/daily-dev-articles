# Cross-request KV cache exposure in the GLM-5.3 Workers AI model, and our remediation with SGLang

- **Source:** Cloudflare
- **Rank (today):** #5
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-10-28 19:25
- **Original:** https://blog.cloudflare.com/kv-cache-exposure-remediation/

## Summary

Cross-request KV cache exposure in the GLM-5.3 Workers AI model, and our remediation with SGLang On September 8, 2026, we were alerted by a security researcher, Gadi Evron from Knostic, to a tenant isolation issue affecting the GLM-5.3 Workers AI model (@cf/zai-org/glm-5.3) starting on August 27, 2026. We have remediated the issue, and we restored the model on September 9. We have confirmed that no other model hosted on Workers AI was affected.

## Key Takeaways

- Between August 27 and September 9, a small number of customers using the GLM 5.3 Workers AI model received responses that contained data from other customers' requests made to the same model shortly before theirs.
- In total, 155 responses were affected, all to prompts longer than 681,280 tokens.
- After excluding our own testing and the researcher's, the requests we identified are consistent in timing and volume with ordinary long-context use, not with someone repeatedly exploiting the bug.

---
_Auto-generated daily digest entry._
