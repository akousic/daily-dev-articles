# Microsoft Word for Windows 1.1a, Native X64 Port

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 112
- **Published (UTC):** 2026-08-09 05:23
- **Original:** https://github.com/jmarshall23/msword

## Summary

This project is a fully working native Windows x64 port of Microsoft Word for Windows 1.1a, whose historical codename was Opus. It builds the original Word source and resources together with modern replacements for the 16-bit assembly, segmented-memory, and Win16 platform boundaries. The result is the original Word application and user experience running as a 64-bit Windows executable.

## Key Takeaways

- This is not an emulator or a reimplementation using a modern editor control.
- - 64-bit Windows - Visual Studio 2022 with Desktop development with C++ - A Windows 10 or Windows 11 SDK installed through Visual Studio - CMake 3.25 or newer - PowerShell Clone the repository, configure the included CMake preset, and build it from a PowerShell prompt: git clone https://github.com/jmarshall23/msword.git Set-Location msword\src cmake --preset x64-debug cmake --build --preset x64-debug & ..\bin\WORD1.exe For an optimized build, use the release preset instead: cmake --preset x64-release cmake --build --preset x64-release & ..\bin\WORD1.exe The presets use the Visual Studio 2022 x64 generator.
- After configuration, the generated solution can also be opened directly from out\MicrosoftWordX64Port.sln; use WORD1 as the startup project.

---
_Auto-generated daily digest entry._
