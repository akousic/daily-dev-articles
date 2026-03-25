# Show HN: Gemini can now natively embed video, so I built sub-second video search

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 384
- **Published (UTC):** 2026-03-24 14:58
- **Original:** https://github.com/ssrajadh/sentrysearch

## Summary

Semantic search over dashcam footage. Type what you're looking for, get a trimmed clip back. demo.mp4 SentrySearch splits your dashcam videos into overlapping chunks, embeds each chunk directly as video using Google's Gemini Embedding model, and stores the vectors in a local ChromaDB database.

## Key Takeaways

- When you search, your text query is embedded into the same vector space and matched against the stored video embeddings.
- The top match is automatically trimmed from the original file and saved as a clip.
- - Clone and install: git clone https://github.com/ssrajadh/sentrysearch.git cd sentrysearch python -m venv venv && source venv/bin/activate pip install -e .

---
_Auto-generated daily digest entry._
