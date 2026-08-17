# GLM 5.2 free for eve agents through August 27 via Blackbox on AI Gateway

- **Source:** Vercel
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-08-17 14:35
- **Original:** https://vercel.com/changelog/glm-5-2-free-for-eve-agents-through-august-27-via-blackbox-on-ai-gateway

## Summary

GLM 5.2, the open-weights coding model from Z.ai with a 1M-token context window, is free for eve agents through August 27, served by Blackbox AI on AI Gateway. New eve agents come with GLM 5.2 as their default model. Use npx eve@latest init my-agent to get started.

## Key Takeaways

- Existing agents can benefit from this as well with a one-line change in agent/agent.ts: agent/agent.ts import { defineAgent } from "eve"; export default defineAgent({ model: "zai/glm-5.2",}); Setting the promo model in the agent definition Or run eve set from the CLI: eve set --model zai/glm-5.2 The command edits the agent definition in place This offer does not apply to Fast mode or the zai/glm-5.2-fast variant of the model.
- After August 27, GLM 5.2 stays available on AI Gateway at standard provider rates.
- Try GLM 5.2 in the model playground.

---
_Auto-generated daily digest entry._
