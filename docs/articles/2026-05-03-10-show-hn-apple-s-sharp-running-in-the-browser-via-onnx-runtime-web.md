# Show HN: Apple's Sharp Running in the Browser via ONNX Runtime Web

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 90
- **Published (UTC):** 2026-05-03 09:14
- **Original:** https://github.com/bring-shrubbery/ml-sharp-web

## Summary

A browser-based Gaussian splat generator built on top of Apple SHARP. ✨ This project lets you: - upload one image - generate Gaussian splats in the browser - preview the result - download a .ply file - Project repo: bring-shrubbery/ml-sharp-web - Follow the author on X: @bringshrubberyy - Upstream SHARP repo (Apple): apple/ml-sharp - SHARP project page: apple.github.io/ml-sharp - SHARP paper: arXiv:2512.10685 Apple's SHARP repository has separate licenses for code and model weights. - SHARP code license: LICENSE - SHARP model license: LICENSE_MODEL If you use Apple's released SHARP checkpoint/weights, you must follow LICENSE_MODEL (research-use restrictions apply).

## Key Takeaways

- - Bun installed - A modern desktop browser (Chrome or Edge recommended) - Enough disk space and RAM for the SHARP model (the exported ONNX sidecar is large, ~2.4 GB) If this project helps you, please star it: bun install This also copies ONNX Runtime Web WASM assets into public/ort/ automatically.
- bun dev Open the URL shown by Vite (usually http://localhost:5173 ).
- - Click Generate Splat .

---
_Auto-generated daily digest entry._
