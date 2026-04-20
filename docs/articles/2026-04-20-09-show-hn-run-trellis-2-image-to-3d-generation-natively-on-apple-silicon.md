# Show HN: Run TRELLIS.2 Image-to-3D generation natively on Apple Silicon

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 188
- **Published (UTC):** 2026-04-20 00:07
- **Original:** https://github.com/shivampkumar/trellis-mac

## Summary

Run TRELLIS.2 image-to-3D generation natively on Mac. This is a port of Microsoft's TRELLIS.2 — a state-of-the-art image-to-3D model — from CUDA-only to Apple Silicon via PyTorch MPS. No NVIDIA GPU required.

## Key Takeaways

- Generates 400K+ vertex meshes from single images in ~3.5 minutes on M4 Pro.
- Output includes textured OBJ and GLB files with PBR materials, ready for use in 3D applications.
- Input → Generated 3D mesh (424K vertices, 858K triangles) - macOS on Apple Silicon (M1 or later) - Python 3.11+ - 24GB+ unified memory recommended (the 4B model is large) - ~15GB disk space for model weights (downloaded on first run) # Clone this repo git clone https://github.com/shivampkumar/trellis-mac.git cd trellis-mac # Log into HuggingFace (needed for gated model weights) hf auth login # Request access to these gated models (usually instant approval): # https://huggingface.co/facebook/dinov3-vitl16-pretrain-lvd1689m # https://huggingface.co/briaai/RMBG-2.0 # Run setup (creates venv, installs deps, clones & patches TRELLIS.2) bash setup.sh # Activate the environment source .venv/bin/activate # Generate a 3D model from an image python generate.py path/to/image.png Output files are saved to the current directory (or use --output to specify a path).

---
_Auto-generated daily digest entry._
