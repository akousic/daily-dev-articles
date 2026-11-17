# Windows 11 is collecting data on which coding agents and developer tools you use

- **Source:** Hacker News
- **Rank (today):** #1
- **Ranking metrics:** HN score 702
- **Published (UTC):** 2026-11-16 22:58
- **Original:** https://xusheng.dev/posts/windows-coding-agent-telemetry/

## Summary

7 minutes Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You Use I recently asked AI to help me look through the latest Windows binaries for undocumented features and functionality. Among the leads it turned up, one list immediately caught my attention: coding agents such as codex.exe, claude.exe, copilot.exe, and cursor.exe, alongside familiar developer tools such as python.exe, dotnet.exe, gcc.exe, and code.exe. Why would a Windows system DLL need a list of coding agents and developer tools?

## Key Takeaways

- The names were in MissionControlAggregator.dll.
- I asked the agent to follow the references and dig into what the DLL actually does.
- That led from a handful of string comparisons to a running Windows component that records which coding agents and developer tools have been used, saves that information locally, and reports it to Windows Diagnostics.

---
_Auto-generated daily digest entry._
