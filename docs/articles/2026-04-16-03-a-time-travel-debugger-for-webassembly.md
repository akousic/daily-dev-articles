# A time travel debugger for WebAssembly

- **Source:** Lobsters
- **Rank (today):** #3
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-04-16 09:10
- **Original:** https://github.com/friendlymatthew/gabagool/tree/main/gabagool-debug-adapter#gabagool-debug-adapter

## Summary

A DAP server that enables time travel debugging for WebAssembly programs. Currently, the debugger steps through .wat source files. Supporting DWARF debug symbols to step through the original source code is a future (and lofty) goal.

## Key Takeaways

- Open this repo in a GitHub Codespace Wait for the container to build and press F5 # build the adapter and copy the binary into the extension dir ./gabagool-debug-adapter/local-install.sh # symlink the extension into vscode ln -sfn "$(pwd)/gabagool-debug-adapter" ~/.vscode/extensions/gabagool-debug # reload vscode (cmd + shift + p -> "Developer: reload window") # open any .wat file and press F5, then pick a program from the dropdown https://microsoft.github.io/debug-adapter-protocol/specification.html

---
_Auto-generated daily digest entry._
