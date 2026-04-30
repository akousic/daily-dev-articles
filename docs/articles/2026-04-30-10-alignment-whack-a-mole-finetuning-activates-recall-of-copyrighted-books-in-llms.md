# Alignment whack-a-mole: Finetuning activates recall of copyrighted books in LLMs

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 179
- **Published (UTC):** 2026-04-30 03:11
- **Original:** https://github.com/cauchy221/Alignment-Whack-a-Mole-Code

## Summary

Alignment Whack-a-Mole: Finetuning Activates Verbatim Recall of Copyrighted Books in Large Language Models The paper is now on arxiv and check out our demo! This repository contains the data preprocessing pipeline, finetuning scripts, memorization evaluation code, and analysis scripts for our paper. We provide partial example files in data/ containing a small subset of excerpts and generations from The Road by Cormac McCarthy.

## Key Takeaways

- Full book content and model generations are not included because the books are copyrighted and the generations contain large portions of verbatim text.
- We use uv for dependency management.
- Install uv if you haven't already: curl -LsSf https://astral.sh/uv/install.sh | sh Create a virtual environment and install all dependencies: uv venv --python 3.11 source .venv/bin/activate uv pip install html2text natsort ftfy openai tqdm nltk numpy For Gemini finetuning and generation, also install: uv pip install google-genai google-cloud-storage vertexai For DeepSeek finetuning and generation via Tinker, also install: uv pip install tinker tinker-cookbook datasets Set your Tinker API key (sign up at https://auth.thinkingmachines.ai/sign-up): export TINKER_API_KEY="your-key-here" Set your OpenAI API key (required for preprocessing and GPT-4o finetuning/generation): export OPENAI_API_KEY="your-key-here" Download the required NLTK data (one-time, for evaluation and analysis): import nltk nltk.download('punkt_tab') We assume you already have the EPUB file for each book.

---
_Auto-generated daily digest entry._
