# Chat SDK now includes AI SDK tools

- **Source:** Vercel
- **Rank (today):** #6
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-05-26 17:30
- **Original:** https://vercel.com/changelog/chat-sdk-now-includes-ai-sdk-tools

## Summary

1 min read Chat SDK now ships a built-in AI SDK toolset through the new chat/ai subpath. One createChatTools(chat) call wires Chat SDK's read and write actions into your agent. import { Chat } from "chat";import { createChatTools } from "chat/ai";import { ToolLoopAgent } from "ai"; const chat = new Chat({ userName: "mybot" /* ...

## Key Takeaways

- */ }); const agent = new ToolLoopAgent({ model: "openai/gpt-5.4", instructions: 'You are a helpful assistant.' tools: createChatTools(chat, { preset: "messenger" }),}); Create a chat agent with the messenger preset Approval by default: write tools are gated by a requireApproval option.Presets: reader ,messenger , andmoderator scope the toolset.Lazy loading: only the tools your preset allows are constructed.
- toAiMessages and its supporting types have moved to chat/ai .
- The previous chat re-exports are flagged @deprecated .

---
_Auto-generated daily digest entry._
