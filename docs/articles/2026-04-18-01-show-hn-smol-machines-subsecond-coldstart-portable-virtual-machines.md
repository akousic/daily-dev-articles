# Show HN: Smol machines – subsecond coldstart, portable virtual machines

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 380
- **Published (UTC):** 2026-04-17 17:18
- **Original:** https://github.com/smol-machines/smolvm

## Summary

Ship and run software with isolation by default. This is a CLI tool that lets you: - Manage and run custom Linux virtual machines locally with: sub-second cold start, cross-platform (macOS, Linux), elastic memory usage. - Pack a stateful virtual machine into a single file (.smolmachine) to rehydrate on any supported platform.

## Key Takeaways

- # install (macOS + Linux) curl -sSL https://smolmachines.com/install.sh | bash # for coding agents — install + discover all commands curl -sSL https://smolmachines.com/install.sh | bash && smolvm --help Or download from GitHub Releases.
- # run a command in an ephemeral VM (cleaned up after exit) smolvm machine run --net --image alpine -- sh -c "echo 'Hello world from a microVM' && uname -a" # interactive shell smolvm machine run --net -it --image alpine -- /bin/sh # inside the VM: apk add sl && sl && exit Sandbox untrusted code — run untrusted programs in a hardware-isolated VM.
- Host filesystem, network, and credentials are separated by a hypervisor boundary.

---
_Auto-generated daily digest entry._
