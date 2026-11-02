# Show HN: I've updated my Linux System Call website and API

- **Source:** Hacker News
- **Rank (today):** #9
- **Ranking metrics:** HN score 194
- **Published (UTC):** 2026-11-02 09:29
- **Original:** https://syscall.sh/

## Summary

Linux syscall tables Architectures Every architecture's table, with the full history of when each syscall appeared and when it was dropped, is also a plain JSON file at /<arch>/syscalls.json, for example /x64/syscalls.json. Calling conventions Number in NR, arguments in ARG0 to ARG5, then the instruction. The result comes back in RETURN.

## Key Takeaways

- | ARCH | INSTRUCTION | NR | RETURN | ARG0 | ARG1 | ARG2 | ARG3 | ARG4 | ARG5 | |---|---|---|---|---|---|---|---|---|---| | x64 | syscall | rax | rax | rdi | rsi | rdx | r10 | r8 | r9 | | x86 | int 0x80 | eax | eax | ebx | ecx | edx | esi | edi | ebp | | arm64 | svc #0 | x8 | x0 | x0 | x1 | x2 | x3 | x4 | x5 | | arm | svc #0 | r7 | r0 | r0 | r1 | r2 | r3 | r4 | r5 | | riscv64 | ecall | a7 | a0 | a0 | a1 | a2 | a3 | a4 | a5 | | ia32 | int 0x80 | eax | eax | ebx | ecx | edx | esi | edi | ebp | | x32 | syscall | rax | rax | rdi | rsi | rdx | r10 | r8 | r9 | | loongarch64 | syscall 0 | a7 | a0 | a0 | a1 | a2 | a3 | a4 | a5 | | ppc64 | sc | r0 | r3 | r3 | r4 | r5 | r6 | r7 | r8 | | ppc | sc | r0 | r3 | r3 | r4 | r5 | r6 | r7 | r8 | | s390x | svc 0 | r1 | r2 | r2 | r3 | r4 | r5 | r6 | r7 | | mips64 | syscall | v0 | v0 | a0 | a1 | a2 | a3 | a4 | a5 | | mipsn32 | syscall | v0 | v0 | a0 | a1 | a2 | a3 | a4 | a5 | | mipso32 | syscall | v0 | v0 | a0 | a1 | a2 | a3 | sp+16 | sp+20 | | alpha | callsys | v0 | v0 | a0 | a1 | a2 | a3 | a4 | a5 | | arc | trap0 | r8 | r0 | r0 | r1 | r2 | r3 | r4 | r5 | | csky | trap 0 | r7 | a0 | a0 | a1 | a2 | a3 | r4 | r5 | | hexagon | trap0(#1) | r6 | r0 | r0 | r1 | r2 | r3 | r4 | r5 | | m68k | trap #0 | d0 | d0 | d1 | d2 | d3 | d4 | d5 | a0 | | microblaze | brki r14,8 | r12 | r3 | r5 | r6 | r7 | r8 | r9 | r10 | | nios2 | trap | r2 | r2 | r4 | r5 | r6 | r7 | r8 | r9 | | openrisc | l.sys 1 | r11 | r11 | r3 | r4 | r5 | r6 | r7 | r8 | | parisc | ble 0x100(%sr2, %r0) | r20 | r28 | r26 | r25 | r24 | r23 | r22 | r21 | | sh | trapa #31 | r3 | r0 | r4 | r5 | r6 | r7 | r0 | r1 | | sparc | t 0x10 | g1 | o0 | o0 | o1 | o2 | o3 | o4 | o5 | | sparc64 | t 0x6d | g1 | o0 | o0 | o1 | o2 | o3 | o4 | o5 | | xtensa | syscall | a2 | a2 | a6 | a3 | a4 | a5 | a8 | a9 | API curl https://api.syscall.sh/v2/syscalls/x64/read Any kernel release, diffs between releases and more in the API docs.
- Syscall tables across kernel versions Entries get added and, rarely, removed between releases.
- Each architecture page has a kernel selector, and its JSON download records when each entry first appeared (since) and when it was dropped (removed_in).

---
_Auto-generated daily digest entry._
