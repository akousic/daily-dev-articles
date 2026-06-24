# Show HN: Nub – A Bun-like all-in-one toolkit for Node.js

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 81
- **Published (UTC):** 2026-06-24 14:14
- **Original:** https://github.com/nubjs/nub

## Summary

A fast all-in-one toolkit that augments Node.js instead of replacing it A Bun-like DX on top of stock node, written in Rust. nub index.ts # TypeScript-first Node.js runtime nub run dev # 24× faster pnpm run nubx prisma generate # 19× faster npx nub install # 2.5× faster pnpm install nub watch src/server.ts # native watch mode nub pm shim # built-in Corepack-style shims nub node install 26 # Node version manager nub upgrade # self updateOne tool to run your files and scripts, install dependencies, and manage Node itself. No new runtime, no vendor-specific API surface, no lock-in.

## Key Takeaways

- | Nub | Instead of | |---|---| | nub <file> | node,tsx,ts-node,dotenv-cli | | nub run <script> | npm run,pnpm run | | nubx | npx,pnpm dlx / exec | | nub install | npm,pnpm | | nub watch | nodemon,node --watch,tsx watch | | nub node | nvm,fnm,n,volta | | nub pm | corepack | # macOS / Linux curl -fsSL https://nubjs.com/install.sh | bash # Windows (PowerShell) irm https://nubjs.com/install.ps1 | iex # Or via npm (pnpm / yarn global add work too) npm install -g --ignore-scripts=false @nubjs/nubFor GitHub Actions, use nubjs/setup-nub in place of actions/setup-node.
- It's one-to-one compatible.
- - - uses: actions/setup-node@v4 + - uses: nubjs/setup-nub@v0Run a file.

---
_Auto-generated daily digest entry._
