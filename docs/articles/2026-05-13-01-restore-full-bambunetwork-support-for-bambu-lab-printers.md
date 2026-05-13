# Restore full BambuNetwork support for Bambu Lab printers

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 601
- **Published (UTC):** 2026-05-12 21:55
- **Original:** https://github.com/FULU-Foundation/OrcaSlicer-bambulab

## Summary

You are not limited to LAN only. It works over the internet just like before, through BambuNetwork, with full functionality for normal use and printing. Windows requires WSL 2.

## Key Takeaways

- Before first launch, open Command Prompt or PowerShell as Administrator and run: dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart Restart Windows, then launch Orca Studio.
- On Linux, a normal installation is enough.
- I also encourage you to use BMCU.

---
_Auto-generated daily digest entry._
