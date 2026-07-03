# Arbitrary code execution breaking sandboxes in KDE Plasma

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-07-02 21:39
- **Original:** https://blog.kimiblock.top/2026/07/01/arbitrary-code-execution-in-kde-plasma/

## Summary

Arbitrary code execution breaking sandboxes in KDE Plasma PoC This proof of concept demonstrates a mean for malicious sandboxed (Flatpak here, but any sandbox apply. With or without the security context support.) applications to impersonate and, more importantly, spawn arbitrary binaries on the host when user invokes Open New Window action. This demonstration utilises Arch Linux host with some dependencies (wget, unzip, meson) to build the malicious binary, and a Flatpak application io.github.johannesboehler2.BmiCalculator with no granted permission (except for the evil binary we have to pass in, because building things inside Flatpak is not easy).

## Key Takeaways

- You will need kcalc (/usr/bin/kcalc) as the designated target.
- Build the evil binary on host: | 1 | cd /tmp | Install the Flatpak app and provide said binary to it.
- | 1 | flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo | Now that it’s all set, let’s run the evil binary: | 1 | flatpak run --command=/tmp/mesa-demos-argv0-argv0/build/src/egl/opengl/eglgears_wayland io.github.johannesboehler2.BmiCalculator | Notice that in the task bar, KCalc‘s icon is being shown.

---
_Auto-generated daily digest entry._
