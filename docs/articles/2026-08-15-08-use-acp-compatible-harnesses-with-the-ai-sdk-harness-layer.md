# Use ACP-compatible harnesses with the AI SDK harness layer

- **Source:** Vercel
- **Rank (today):** #8
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-08-15 14:30
- **Original:** https://vercel.com/changelog/use-acp-compatible-harnesses-with-the-ai-sdk-harness-layer

## Summary

The AI SDK harness layer now supports any Agent Client Protocol (ACP)-compatible harness with HarnessAgent through the new @ai-sdk/harness-acp package. Previously, every harness adapter wrapped one specific runtime (Claude Code, Codex, Pi, Deep Agents, OpenCode). @ai-sdk/harness-acp wraps the protocol instead.

## Key Takeaways

- It is a meta adapter: rather than adapting a single harness, it lets you build an adapter for any harness that ships an ACP-compatible package.
- Implement a harness by passing that package to createACP and configure basic harness mapping.
- import { createACP } from '@ai-sdk/harness-acp'; export function createCodexACP() { return createACP({ harnessId: 'codex-acp', source: { type: 'npm-simple', packageName: '@agentclientprotocol/codex-acp', }, executable: 'codex-acp', forwardEnv: ['CODEX_API_KEY', 'OPENAI_API_KEY'], permissionModeMapping: { 'allow-reads': null, 'allow-edits': null, 'allow-all': { type: 'session-mode', modeId: 'agent-full-access' }, }, authentication: { methodId: 'api-key', }, });} Basic ACP harness example implementation for Codex on top of the ACP meta harness Then pass it to HarnessAgent like any other harness: import { HarnessAgent } from '@ai-sdk/harness/agent';import { createCodexACP } from './codex-acp-harness'; const agent = new HarnessAgent({ harness: createCodexACP(),}); Basic example for using the above Codex ACP harness with HarnessAgent ACP is an abstraction over coding harnesses, but the AI SDK harness layer stays deliberately decoupled from it.

---
_Auto-generated daily digest entry._
