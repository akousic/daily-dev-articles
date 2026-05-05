# How OpenAI delivers low-latency voice AI at scale

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 460
- **Published (UTC):** 2026-05-04 19:42
- **Original:** https://openai.com/index/delivering-low-latency-voice-ai-at-scale/

## Summary

How OpenAI delivers low-latency voice AI at scale By Yi Zhang and William McDonald, Members of Technical Staff Voice AI only feels natural if conversation moves at the speed of speech. When the network gets in the way, people hear it immediately as awkward pauses, clipped interruptions, or delayed barge-in. That matters for ChatGPT voice, for developers building with the Realtime API, for agents working in interactive workflows, and for models that need to process audio while a user is still talking.

## Key Takeaways

- At OpenAI’s scale, that translates into three concrete requirements: - Global reach for more than 900 million weekly active users - Fast connection setup so a user can start speaking as soon as a session begins - Low and stable media round-trip time, with low jitter and packet loss, so turn-taking feels crisp The team at OpenAI responsible for real-time AI interactions recently rearchitected our WebRTC stack to address three constraints that started to collide at scale: one-port-per-session media termination does not fit OpenAI infrastructure well, stateful ICE (Interactive Connectivity Establishment) and DTLS (Datagram Transport Layer Security) sessions need stable ownership, and global routing has to keep first-hop latency low.
- In this post, we walk through the split relay plus transceiver architecture we built to preserve standard WebRTC behavior for clients while changing how packets are routed inside OpenAI’s infrastructure.
- WebRTC is an open standard for sending low-latency audio, video, and data between browsers, mobile apps, and servers.

---
_Auto-generated daily digest entry._
