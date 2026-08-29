# Boot a Virtual iPhone via Apple's Virtualization.framework

- **Source:** Hacker News
- **Rank (today):** #2
- **Ranking metrics:** HN score 349
- **Published (UTC):** 2026-08-28 23:02
- **Original:** https://github.com/Lakr233/vphone-cli

## Summary

Boot a virtual iPhone via Apple's Virtualization.framework using PCC research VM infrastructure. Host: - Apple Silicon - macOS 15+ (Sequoia) - Xcode + iOS SDK (cross-compiles the guest daemon) - SIP/AMFI relaxation to allow private PV=3 entitlements with unsigned-binary Dependencies: brew install python@3.13 aria2 wget gnu-tar openssl@3 ldid-procursus sshpass keystone cmake libusb ipsw zstdbrew install zqxwce/tap/vphone-cligit clone --recurse-submodules https://github.com/Lakr233/vphone-cli.git ./scripts/setup_tools.sh # install deps, build toolchain submodules, create the Python venv ./scripts/build.sh # build + sign vphone-cli, bundle the .app, cross-compile vphoned cd .build/vphone-cli.app/Contents/MacOS/ vphone-cli --help One command creates a VM end-to-end (download → patch → DFU restore → CFW install → first boot): vphone-cli vm create myphone -V jb # -V / --variant vphone-cli vm launch myphone vphone-cli vm create runs the whole pipeline; the individual steps below let you drive it manually or re-run one stage. vphone-cli vm list # list VMs (--json for scripting) vphone-cli vm info myphone # show one VM vphone-cli vm new myphone # create an empty bundle (cpu/mem/disk options) vphone-cli vm config myphone --cpu 8 --memory 8192 vphone-cli vm clone myphone myphone-2 # fast APFS clone, fresh device identity vphone-cli vm export myphone --out myphone.tzst # zstd fast by default (--max = xz -9); --out may be a dir (auto-names <vm>.tzst/.txz); skips restore dir + staging files vphone-cli vm import myphone.tzst --name restored vphone-cli vm rename myphone iphone16 vphone-cli vm delete iphone16vphone-cli vm new myphone # 1.

## Key Takeaways

- empty bundle vphone-cli fw prepare myphone --iphone-version 26.1 # 2.
- download + merge IPSWs vphone-cli fw patch myphone --variant jb # 3.
- patch the boot chain vphone-cli vm launch myphone --dfu & # 4.

---
_Auto-generated daily digest entry._
