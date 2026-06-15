# pyinfra — agentless infrastructure automation, in plain Python

- **Source:** Lobsters
- **Rank (today):** #4
- **Ranking metrics:** RSS curated source
- **Published (UTC):** 2026-06-15 06:05
- **Original:** https://pyinfra.com

## Summary

Your editor already understands it. pyinfra is a python-native, agentless automation tool that runs commands over ssh — concurrently, idempotently, and 6× faster than ansible. 1# deploy.py · 23 hosts 2 3from pyinfra.operations import apt, files, systemd 4 5apt.packages( 6 packages=["nginx", "certbot"], 7 update=True, 8) 9 10files.template( 11 src="templates/nginx.conf.j2", 12 dest="/etc/nginx/sites-enabled/api", 13) 14 15systemd.service("nginx", reloaded=True) 1# inventory.py · groups + hosts 2 3web = [ 4 ("web-01.prod", {"role": "edge"}), 5 ("web-02.prod", {"role": "edge"}), 6 *[(f"web-{i:02}.prod", {}) for i in range(3, 24)], 7] 8 9db = [ 10 ("db-01.prod", {"role": "primary"}), 11 ("db-02.prod", {"role": "replica"}), 12] 13 14# $ pyinfra inventory.py deploy.py --limit web 15# → 23 hosts targeted $ pyinfra inventory.py deploy.py --limit web --> Loading inventory… Hosts: web-01..web-23 --> Gathering facts (concurrent)… 23 hosts · 0.6s --> Running deploy.py… ✓ web-01.prod 3 ops changed=2 0.42s ✓ web-02.prod 3 ops changed=2 0.39s ⟳ web-03.prod running… apt.packages --> Summary successful: 23 changed: 18 failed: 0 total: 2.1s Run with --dry for a per-host diff of every operation pyinfra would perform.

## Key Takeaways

- Run for real and watch results stream back in parallel.
- $ pyinfra inventory.py deploy.py --limit web--> Loading inventory…Hosts: web-01..web-24, db-01..db-04--> Gathering facts (concurrent)…24 hosts · 0.6s--> Running deploy.py…✓ web-01.prod 3 ops changed=2 0.42s ✓ web-02.prod 3 ops changed=2 0.39s ✓ web-03.prod 3 ops changed=0 0.18s ✓ web-04.prod 3 ops changed=2 0.44s ⟳ web-05.prod running… apt.packages … 19 more--> Summarysuccessful: 24 changed: 18 no-change: 6 failed: 0 total: 2.1s No yaml.
- Your editor already understands it.

---
_Auto-generated daily digest entry._
