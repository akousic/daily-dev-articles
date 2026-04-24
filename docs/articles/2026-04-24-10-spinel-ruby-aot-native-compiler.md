# Spinel: Ruby AOT Native Compiler

- **Source:** Hacker News
- **Rank (today):** #10
- **Ranking metrics:** HN score 194
- **Published (UTC):** 2026-04-24 08:28
- **Original:** https://github.com/matz/spinel

## Summary

Spinel compiles Ruby source code into standalone native executables. It performs whole-program type inference and generates optimized C code, achieving significant speedups over CRuby. Spinel is self-hosting: the compiler backend is written in Ruby and compiles itself into a native binary.

## Key Takeaways

- Ruby (.rb) | v spinel_parse Parse with Prism (libprism), serialize AST | (C binary, or CRuby + Prism gem as fallback) v AST text file | v spinel_codegen Type inference + C code generation | (self-hosted native binary) v C source (.c) | v cc -O2 -Ilib -lm Standard C compiler + runtime header | v Native binary Standalone, no runtime dependencies # Fetch libprism sources (from the prism gem on rubygems.org): make deps # Build everything: make # Write a Ruby program: cat > hello.rb <<'RUBY' def fib(n) if n < 2 n else fib(n - 1) + fib(n - 2) end end puts fib(34) RUBY # Compile and run: ./spinel hello.rb ./hello # prints 5702887 (instantly) ./spinel app.rb # compiles to ./app ./spinel app.rb -o myapp # compiles to ./myapp ./spinel app.rb -c # generates app.c only ./spinel app.rb -S # prints C to stdout Spinel compiles its own backend.
- The bootstrap chain: CRuby + spinel_parse.rb → AST CRuby + spinel_codegen.rb → gen1.c → bin1 bin1 + AST → gen2.c → bin2 bin2 + AST → gen3.c gen2.c == gen3.c (bootstrap loop closed) 74 tests pass.
- Geometric mean: ~11.6x faster than miniruby (Ruby 4.1.0dev) across the 28 benchmarks below.

---
_Auto-generated daily digest entry._
