#!/usr/bin/env python3
"""Download the 31 research PDFs listed in manifest.json and verify their hashes.

Usage: python3 research/download_papers.py [output_dir]
Default output_dir: research/papers (git-ignored).

Some publishers update files; a hash mismatch usually means a newer revision,
not a broken download. The script keeps the file and reports the mismatch.
"""
import hashlib
import json
import os
import sys
import urllib.request

here = os.path.dirname(os.path.abspath(__file__))
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "papers")
os.makedirs(out, exist_ok=True)
manifest = json.load(open(os.path.join(here, "manifest.json")))

ok = mismatch = failed = 0
for p in manifest:
    dest = os.path.join(out, p["file"])
    if not os.path.exists(dest):
        try:
            req = urllib.request.Request(p["url"], headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
                f.write(r.read())
        except Exception as e:
            print(f"FAILED  {p['number']:02d} {p['title']}: {e}")
            failed += 1
            continue
    digest = hashlib.sha256(open(dest, "rb").read()).hexdigest()
    if digest == p.get("sha256"):
        ok += 1
        print(f"ok      {p['number']:02d} {p['title']}")
    else:
        mismatch += 1
        print(f"CHANGED {p['number']:02d} {p['title']} (hash differs from manifest)")

print(f"\n{ok} verified, {mismatch} changed, {failed} failed. Files in {out}")
