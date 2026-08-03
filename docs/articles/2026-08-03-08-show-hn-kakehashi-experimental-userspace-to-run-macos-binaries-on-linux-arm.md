# Show HN: Kakehashi – Experimental userspace to run macOS binaries on Linux ARM

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 240
- **Published (UTC):** 2026-08-02 16:26
- **Original:** https://github.com/wie-project/kakehashi

## Summary

Userspace macOS ARM64 → Linux aarch64 translation layer (CLI-first, no JIT). Load Darwin Mach-O on Linux aarch64, map a freestanding libSystem, translate BSD syscalls, and run real guests (clang probes, 7-Zip 7zz, curl, threads). | Live execution | Linux aarch64 (bare metal, VM, Colima/Docker) | | Dry-load / inspect | Any host (including macOS) | | Design reference | docs/ | Verified on Docker/Colima and UTM (Linux aarch64).

## Key Takeaways

- Install once: cargo install kakehashi # or from a checkout: cargo install --path crates/kh-cli --force kh bottle ensure kh install 7zip # Darwin 7zz → guest /usr/local/bin/7zz kh install curl # Darwin curl → guest /usr/local/bin/curl Relative -o / archive paths resolve against the host CWD of the kh process (create parent dirs yourself, or rely on auto-mkdir for O_CREAT).
- Through the bottle, /Volumes/linux/… bridges to the host root (/ → host /).
- # Version / help kh run 7zz -- kh run 7zz -- --help # Create archive (cwd-relative) kh run 7zz -- a demo.7z README.md kh run 7zz -- t demo.7z kh run 7zz -- l demo.7z kh run 7zz -- x -o./out demo.7z # Multi-thread compress (correctness gate) kh run 7zz -- a -t7z -m0=lzma2 -mx=5 -mmt=4 mt.7z README.md kh run 7zz -- t mt.7z # expect: Everything is Ok, exit 0 Docker helpers (artifacts under host .tmp/kh-out/): ./scripts/docker-7zz.sh --help ./scripts/docker-7zz.sh a /Volumes/linux/out/demo.7z /Volumes/linux/src/README.md ls -lh .tmp/kh-out/demo.7z KAKEHASHI_HYPERCALL=1 ./scripts/docker-7zz.sh a -t7z -m0=lzma2 -mx=5 -mmt=4 \ /Volumes/linux/out/mt.7z /Volumes/linux/src/README.md ./scripts/docker-7zz.sh t /Volumes/linux/out/mt.7z# Banner (G1) kh run curl -- --version # HTTP GET → file (G3 / G5).

---
_Auto-generated daily digest entry._
