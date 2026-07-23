# AI Gateway now supports streaming transcription

- **Source:** Vercel
- **Rank (today):** #7
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-23 15:57
- **Original:** https://vercel.com/changelog/ai-gateway-now-supports-streaming-transcription

## Summary

AI Gateway now supports streaming transcription. Previously, transcription required a complete audio file and returned the full transcript in a single response. Now you can stream audio in as it's captured and get transcript updates back as the model produces them, keeping latency low for uses like live captioning and voice input.

## Key Takeaways

- Streaming transcription is in beta and available through the AI SDK's streamTranscribe function with any streaming-capable transcription model.
- The example below streams raw PCM audio to openai/gpt-realtime-whisper and prints each transcript delta as it arrives.
- The result stream also carries partial and final transcripts: import { experimental_streamTranscribe as streamTranscribe } from 'ai'; const result = streamTranscribe({ model: 'openai/gpt-realtime-whisper', audio: audioStream, // ReadableStream<Uint8Array | string> inputAudioFormat: { type: 'audio/pcm', rate: 24000 },}); for await (const part of result.fullStream) { if (part.type === 'transcript-delta') { process.stdout.write(part.delta); }}The same code works across providers: swap the model string to use xai/grok-stt or any other streaming-capable transcription model.

---
_Auto-generated daily digest entry._
