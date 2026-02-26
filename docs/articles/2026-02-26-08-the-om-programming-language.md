# The Om Programming Language

- **Source:** Hacker News
- **Rank (today):** #8
- **Ranking metrics:** HN score 284
- **Published (UTC):** 2026-02-25 17:48
- **Original:** https://www.om-language.com/

## Summary

| Om | The Om language is: The Om language is not: This program and the accompanying materials are made available under the terms of the Eclipse Public License, Version 1.0, which accompanies this distribution. For more information about this license, please see the Eclipse Public License FAQ. The Om source code can be used for: The Om source code is downloadable from the Om GitHub repository: To run scripts which build the dependency Libraries and generate the build project, the following programs are required: sudo apt-get install build-essential )To build the Documentation in the build project, the following additional programs are required: To ensure that correct programs are used, programs should be listed in the command line path in the following order: The following libraries are required to build the Om code: A build project, containing targets for building the interpreter, tests, and documentation, can be generated into "[builds directory path]/Om/projects/[project]" by running the appropriate "generate" script from the desired builds directory: Arguments include the desired project name (required), followed by any desired CMake arguments.

## Key Takeaways

- By default, this script automatically installs all external dependency libraries (downloading and building as necessary) into "[builds directory path]/[dependency name]/downloads/[MD5]/build/[platform]/install".
- This behaviour can be overridden by passing paths of pre-installed dependency libraries to the script: -D Icu4cInstallDirectory:Path="[absolute ICU4C install directory path]" -D BoostInstallDirectory:Path="[absolute Boost install directory path]" The Om.Interpreter target builds the interpreter executable as "[Om build directory path]/executables/[platform]/[configuration]/Om.Interpreter".
- The interpreter: The Om.Test target builds the test executable, which runs all unit tests, as "[Om build directory path]/executables/[platform]/[configuration]/Om.Test".

---
_Auto-generated daily digest entry._
