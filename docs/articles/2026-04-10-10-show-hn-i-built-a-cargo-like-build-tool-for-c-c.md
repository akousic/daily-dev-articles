# Show HN: I built a Cargo-like build tool for C/C++

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 158
- **Published (UTC):** 2026-04-09 16:04
- **Original:** https://github.com/randerson112/craft

## Summary

A lightweight build tool for C and C++ projects — think Cargo, but for C/C++. C and C++ development has always required wrestling with CMake, configuring build systems, and manually managing dependencies. Craft eliminates that friction.

## Key Takeaways

- You describe your project in a simple craft.toml file and Craft handles the rest by generating CMake configuration, managing dependencies, and providing a clean command-line interface that feels modern and smooth.
- - Define your project in craft.toml - Craft generates CMakeLists.txt - Dependencies are fetched automatically - CMake builds your project behind the scenes # Create a new project craft project my_app cd my_app # Add a dependency craft add --git https://github.com/raysan5/raylib.git --links raylib # Build it craft build # Run it craft run Describe your project in a simple, readable config: [project] name = "my_app" version = "0.1.0" language = "cpp" cpp_standard = 17 [build] type = "executable" include_dirs = ["include"] source_dirs = ["src"] Craft turns this into a working CMakeLists.txt automatically.
- Add dependecies to your project with a single command.

---
_Auto-generated daily digest entry._
