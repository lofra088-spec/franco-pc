# cyber/data

- `cve.db` — SQLite, table `cve(id, cvss, summary, published)` (empty; feed from NVD).
- `exploits.db` — SQLite, table `exploits(id, cve, title, path, platform)` (empty; feed from exploit-db).
- `wordlists/` — subdomains + passwords used by recon/hashes.
- `signatures/` — drop YARA/malware signatures here.
