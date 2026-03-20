# Anthropic takes legal action against OpenCode

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 456
- **Published (UTC):** 2026-03-19 19:37
- **Original:** https://github.com/anomalyco/opencode/pull/18186

## Summary

Conversation Greptile SummaryThis PR removes Anthropic-specific references from the codebase per legal requirements, including the branded system prompt file, the Key changes: Issues found: Confidence Score: 3/5 Important Files Changed Flowchart%%{init: {'theme': 'neutral'}}%% flowchart TD A[LLM.stream called] --> B{providerID starts with 'opencode'?} B -- Yes --> C[Add x-opencode-project/session/request/client headers] B -- No --> D[No extra headers added] C --> E[Merge model.headers] D --> E E --> F[Merge plugin chat.headers] F --> G[streamText call] subgraph "Before PR (removed path)" H{providerID !== 'anthropic'?} H -- Yes --> I["Add User-Agent: opencode/VERSION"] H -- No --> J[undefined — no headers] end style D fill:#f99,stroke:#c00 style I fill:#9f9,stroke:#090 style J fill:#ccc,stroke:#999 | | headers: { | || | ...(input.model.providerID.startsWith("opencode") | || | ? { | || | "x-opencode-project": Instance.project.id, | || | "x-opencode-session": input.sessionID, | || | "x-opencode-request": input.user.id, | || | "x-opencode-client": Flag.OPENCODE_CLIENT, | || | } | || | : input.model.providerID !== "anthropic" | || | ? { | || | "User-Agent": `opencode/${Installation.VERSION}`, | || | } | || | : undefined), | || | ...(input.model.providerID.startsWith("opencode") && { | || | "x-opencode-project": Instance.project.id, | || | "x-opencode-session": input.sessionID, | || | "x-opencode-request": input.user.id, | || | "x-opencode-client": Flag.OPENCODE_CLIENT, | || | }), | There was a problem hiding this comment.

## Key Takeaways

- Silent removal of User-Agent header for third-party providers The original logic sent User-Agent: opencode/${Installation.VERSION} to all providers except opencode -prefixed and anthropic ones.
- The refactored code only adds the x-opencode-* headers for opencode providers and adds nothing for everyone else — meaning providers like openai , google , azure , openrouter , etc.
- silently lose the User-Agent header.

---
_Auto-generated daily digest entry._
