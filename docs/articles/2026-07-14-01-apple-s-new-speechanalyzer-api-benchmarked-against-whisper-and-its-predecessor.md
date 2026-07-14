# Apple's new SpeechAnalyzer API, benchmarked against Whisper and its predecessor

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 548
- **Published (UTC):** 2026-07-13 16:06
- **Original:** https://get-inscribe.com/blog/apple-speech-api-benchmark.html

## Summary

The result, up front Apple's new SpeechAnalyzer is the most accurate on-device speech engine we tested. It beat every Whisper model we ship, including Whisper Small, on both the clean and the noisy half of LibriSpeech, while running roughly three times faster than Small. And the API it replaces, SFSpeechRecognizer, came last on clean speech: behind even Whisper Tiny, a 40MB model.

## Key Takeaways

- | Engine | test-clean WER | test-other WER | Model size | |---|---|---|---| | Apple SpeechAnalyzer (iOS/macOS 26) | 2.12% | 4.56% | system | | Whisper Small (WhisperKit CoreML) | 3.74% | 7.95% | ~460MB | | Whisper Base | 5.42% | 12.51% | ~140MB | | Whisper Tiny | 7.88% | 17.04% | ~40MB | | Apple SFSpeechRecognizer (legacy) | 9.02% | 16.25% | system | Lower is better: WER is word error rate, the percentage of words an engine substitutes, drops, or invents.
- LibriSpeech test-clean is 2,620 utterances of clean read speech; test-other is 2,939 harder, noisier utterances.
- Every engine ran fully on-device on an Apple M2 Pro (32GB, macOS 26.5.1).

---
_Auto-generated daily digest entry._
