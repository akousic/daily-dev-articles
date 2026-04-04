# Run Linux containers on Android, no root required

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 172
- **Published (UTC):** 2026-04-03 22:23
- **Original:** https://github.com/ExTV/Podroid

## Summary

Run Linux containers on Android — no root required. Podroid spins up a lightweight Alpine Linux VM on your phone using QEMU and gives you a fully working Podman container runtime with a built-in serial terminal. | Containers | Pull and run any OCI image — podman run --rm -it alpine sh | | Terminal | Full xterm emulation with Ctrl, Alt, F1-F12, arrows, and more | | Persistence | Packages, configs, and container images survive restarts | | Networking | Internet access out of the box, port forwarding to Android host | | Self-contained | No root, no Termux, no host binaries — just install the APK | - arm64 Android device - Android 8.0+ (API 26) - ~150 MB free storage - Install the APK from Releases - Open Podroid and tap Start Podman - Wait for boot (~20 s) — progress is shown on screen and in the notification - Tap Open Terminal - Run containers: podman run --rm alpine echo hello podman run --rm -it alpine sh podman run -d -p 8080:80 nginx The terminal is powered by Termux's TerminalView with full VT100/xterm emulation wired directly to the VM's serial console.

## Key Takeaways

- Extra keys bar (scrollable): ESC TAB SYNC CTRL ALT arrows HOME END PGUP PGDN F1–F12 - / | - CTRL / ALT are sticky toggles — tap once, then press a letter - SYNC manually pushes the terminal dimensions to the VM - Terminal size auto-syncs on keyboard open/close so TUI apps (vim, btop, htop) render correctly - Bell character triggers haptic feedback Forward ports from the VM to your Android device: - Go to Settings - Add a rule (e.g.
- TCP 8080 -> 80) - Access the service at localhost:8080 on your phone Rules persist across restarts and can be added or removed while the VM is running.
- Android App ├── Foreground Service (keeps VM alive) ├── PodroidQemu │ ├── libqemu-system-aarch64.so (QEMU TCG, no KVM) │ ├── Serial stdio ←→ TerminalEmulator │ └── QMP socket (port forwarding, VM control) └── Alpine Linux VM ├── initramfs (read-only base layer) ├── ext4 disk (persistent overlay) ├── getty on ttyAMA0 (job control) └── Podman + crun + netavark + slirp4netns Boot sequence: QEMU loads vmlinuz-virt + initrd.img .

---
_Auto-generated daily digest entry._
