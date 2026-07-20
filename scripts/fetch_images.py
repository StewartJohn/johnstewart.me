#!/usr/bin/env python3
"""Fetch old-blog images from the Wayback Machine into Hugo page bundles.

Reads _incoming/image_manifest.json (written by migrate.py). Skips files
already downloaded, so it can be re-run to retry failures. Rate-limits
politely and backs off when archive.org refuses connections. For URLs with
no capture, retries the un-resized original (WordPress -WxH suffix removed).
"""
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "_incoming" / "image_manifest.json"
FAILURES = ROOT / "_incoming" / "image_failures.json"

UA = {"User-Agent": "Mozilla/5.0 (personal blog migration; contact site owner)"}
PACE = 4  # seconds between requests
SIZE_SUFFIX = re.compile(r"-\d+x\d+(?=\.\w+$)")


def get(url: str) -> bytes:
    """GET with backoff on connection-refused/5xx (archive.org rate limiting)."""
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read()
        except urllib.error.HTTPError:
            raise  # 404 etc. — real answer, don't retry
        except Exception:
            if attempt == 3:
                raise
            wait = 30 * (attempt + 1)
            print(f"    connection trouble, backing off {wait}s...")
            time.sleep(wait)


def fetch(url: str, dest: Path) -> str:
    candidates = [url]
    stripped = SIZE_SUFFIX.sub("", url)
    if stripped != url:
        candidates.append(stripped)
    # The Wayback Machine often captured the Jetpack CDN form of the URL
    # rather than the origin form; try those too.
    for base in list(candidates):
        candidates.append(base.replace("https://johnastewart.org/", "https://i0.wp.com/johnastewart.org/"))
    last_err = None
    for cand in candidates:
        try:
            data = get(f"https://web.archive.org/web/2024im_/{cand}")
            if not data or b"<!DOCTYPE" in data[:200] or data[:6] == b"<html>":
                raise ValueError("got HTML instead of an image (no capture?)")
            dest.write_bytes(data)
            note = " (full-size fallback)" if cand != url else ""
            return f"{len(data)//1024} KB{note}"
        except Exception as e:
            last_err = e
            time.sleep(PACE)
    raise last_err


def main():
    items = json.loads(MANIFEST.read_text())
    failures = []
    done = skipped = 0
    for i, item in enumerate(items, 1):
        dest = ROOT / "content" / item["post"] / item["file"]
        if dest.exists() and dest.stat().st_size > 0:
            skipped += 1
            continue
        try:
            size = fetch(item["url"], dest)
            done += 1
            print(f"[{i}/{len(items)}] ok {item['post']}/{item['file']} ({size})")
        except Exception as e:
            failures.append({**item, "error": str(e)})
            print(f"[{i}/{len(items)}] FAIL {item['url']} — {e}")
        time.sleep(PACE)
    FAILURES.write_text(json.dumps(failures, indent=2))
    print(f"\ndownloaded {done}, skipped (already present) {skipped}, failed {len(failures)}")


if __name__ == "__main__":
    main()
