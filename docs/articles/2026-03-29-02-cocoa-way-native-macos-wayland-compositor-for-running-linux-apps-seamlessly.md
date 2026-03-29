# Cocoa-Way – Native macOS Wayland compositor for running Linux apps seamlessly

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 313
- **Published (UTC):** 2026-03-28 10:06
- **Original:** https://github.com/J-x-Z/cocoa-way

## Summary

Native macOS Wayland compositor for running Linux apps seamlessly True protocol portability: Cocoa-Way rendering Linux apps from OrbStack via Unix sockets. | Feature | Description | |---|---| | 🍎 Native macOS | Metal/OpenGL rendering, seamless desktop integration | | 🚀 Zero VM Overhead | Direct Wayland protocol via socket, no virtualization | | 📺 HiDPI Ready | Optimized for Retina displays with proper scaling | | 🎨 Polished UI | Server-side decorations with shadows and focus indicators | | ⚡ Hardware Accelerated | Efficient OpenGL rendering pipeline | brew tap J-x-Z/tap brew install cocoa-way waypipe-darwin Download the latest .dmg or .zip from Releases. # Install dependencies brew install libxkbcommon pixman pkg-config # Clone and build git clone https://github.com/J-x-Z/cocoa-way.git cd cocoa-way cargo build --release ⚠️ Required: You must install waypipe-darwin to connect Linux apps.brew tap J-x-Z/tap && brew install waypipe-darwin - Start the compositor: cocoa-way - Connect Linux apps via SSH: ./run_waypipe.sh ssh user@linux-host firefox graph LR subgraph macOS CW[Cocoa-Way<br/>Compositor] WP1[waypipe<br/>client] end subgraph Linux VM/Container WP2[waypipe<br/>server] APP[Linux App<br/>Firefox, etc] end APP -->|Wayland Protocol| WP2 WP2 <-->|SSH/Socket| WP1 WP1 -->|Wayland Protocol| CW CW -->|Metal/OpenGL| Display[macOS Display] | Solution | Latency | HiDPI | Native Integration | Setup Complexity | |---|---|---|---|---| | Cocoa-Way | ⚡ Low | ✅ | ✅ Native windows | 🟢 Easy | | XQuartz | 🐢 High | 🟡 Medium | || | VNC | 🐢 High | ❌ | ❌ Full screen | 🟡 Medium | | VM GUI | 🐢 High | ❌ Separate window | 🔴 Complex | - macOS backend (Metal/OpenGL) - Waypipe integration - HiDPI scaling - 🚧 Windows backend (win-way) - 📱 Android NDK backend (planned) - Multi-monitor support - Clipboard sync This project is part of the "Turbo-Charged Protocol Virtualization" research initiative exploring zero-cost cross-platform Wayland via Rust trait monomorphization + SIMD-accelerated pixel conversion.

## Key Takeaways

- SSH: "remote port forwarding failed" A stale socket file exists on the remote host.
- Our run_waypipe.sh script handles this automatically with -o StreamLocalBindUnlink=yes .
- If running manually: waypipe ssh -o StreamLocalBindUnlink=yes user@host ...

---
_Auto-generated daily digest entry._
