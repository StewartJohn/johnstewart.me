#!/usr/bin/env python3
"""Migrate recovered johnastewart.org posts to Hugo page bundles.

Reads _incoming/old-blog/*.md (WordPress/Wayback recovery format), writes
content/<section>/<slug>/index.md, and emits _incoming/image_manifest.json
listing images to fetch from web.archive.org.
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_incoming" / "old-blog"
CONTENT = ROOT / "content"
UNSORTED = ROOT / "_incoming" / "unsorted"
MANIFEST = ROOT / "_incoming" / "image_manifest.json"

# Primary category -> section; DH/History go to history, all else it-edtech.
HISTORY_PRIMARY = {"DH", "History"}

# Manual section overrides by slug (history-of-science content whose old
# primary category was something else).
OVERRIDES = {
    "transcribing-joseph-blacks-chemistry-lectures": "history",
    "a-brief-history-of-alchemy": "history",
    "the-gods-of-norman": "history",
    "a-letter-of-apology-to-my-daughter": "personal",
    "open-letter-to-sen-jim-inhofe": "personal",
}

# Posts held back for a human decision (none currently).
SKIP = set()

OLD_DOMAIN = re.compile(r"https?://(?:www\.)?johnastewart\.org(/[^)\s\"']*)?")
IMG_HOST = re.compile(
    r"https?://(?:i\d\.wp\.com/)?(?:www\.)?johnastewart\.org(/wp-content/uploads/[^)\s\"'?]+)"
)
SCRIPT_TAG = re.compile(r"(?<!`)(<script[^>]*>(?:</script>)?|</script>)(?!`)")


def norm_image(url: str) -> str:
    """Normalize a wp CDN/origin image URL to its origin form, sans query."""
    m = IMG_HOST.search(url)
    return f"https://johnastewart.org{m.group(1)}" if m else ""


def split_post(path: Path):
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        sys.exit(f"no front matter in {path.name}")
    return yaml.safe_load(parts[1]), parts[2].lstrip("\n")


def main():
    posts = {}  # slug -> (meta, body, section)
    for path in sorted(SRC.glob("*.md")):
        meta, body = split_post(path)
        slug = meta["slug"]
        if slug in SKIP:
            UNSORTED.mkdir(parents=True, exist_ok=True)
            (UNSORTED / path.name).write_text(
                path.read_text(encoding="utf-8"), encoding="utf-8"
            )
            continue
        section = OVERRIDES.get(
            slug,
            "history" if meta.get("category") in HISTORY_PRIMARY else "it-edtech",
        )
        posts[slug] = (meta, body, section)

    manifest = []
    flags = []

    def rewrite_link(m, current_slug):
        url, path_part = m.group(0), m.group(1)
        if not path_part or path_part == "/":
            return "/"
        seg = [s for s in path_part.split("/") if s]
        slug = seg[-1] if seg else ""
        if slug in posts:
            return f"/{posts[slug][2]}/{slug}/"
        return f"https://web.archive.org/web/2024/{url}"

    for slug, (meta, body, section) in posts.items():
        bundle = CONTENT / section / slug
        bundle.mkdir(parents=True, exist_ok=True)

        # Images: rewrite to bundle-relative filenames, queue for download.
        def img_sub(m):
            origin = norm_image(m.group(0))
            fname = origin.rsplit("/", 1)[-1]
            manifest.append(
                {"post": f"{section}/{slug}", "url": origin, "file": fname}
            )
            return fname

        body = IMG_HOST.sub(img_sub, body)

        # Remaining old-domain links -> internal or wayback.
        body = OLD_DOMAIN.sub(lambda m: rewrite_link(m, slug), body)

        # Literal <script> mentions in prose would be stripped by Goldmark;
        # wrap them in code spans (skip indented code-block lines).
        fixed_lines = []
        for line in body.splitlines():
            if not line.startswith(("    ", "\t")) and SCRIPT_TAG.search(line):
                line = SCRIPT_TAG.sub(r"`\1`", line)
                if f"{section}/{slug}" not in [f[0] for f in flags]:
                    flags.append((f"{section}/{slug}", "escaped <script> in prose"))
            fixed_lines.append(line)
        body = "\n".join(fixed_lines)

        fm = {
            "title": meta["title"],
            "date": meta["published"],
            "slug": slug,
            "tags": meta.get("tags") or [],
            "summary": (meta.get("excerpt") or "").strip(),
            "originalUrl": meta.get("url", ""),
            "archiveUrl": meta.get("archive_url", ""),
        }
        if meta.get("modified") and meta["modified"] != meta["published"]:
            fm["lastmod"] = meta["modified"]
        feat = (meta.get("featured_image") or {}).get("url", "")
        origin = norm_image(feat)
        if origin:
            fname = origin.rsplit("/", 1)[-1]
            manifest.append(
                {"post": f"{section}/{slug}", "url": origin, "file": fname}
            )
            # PaperMod cover-image format
            fm["cover"] = {"image": fname, "alt": (meta.get("featured_image") or {}).get("alt", "")}

        out = "---\n" + yaml.dump(fm, allow_unicode=True, sort_keys=False) + "---\n\n" + body
        (bundle / "index.md").write_text(out, encoding="utf-8")

    # Dedupe manifest (same image referenced twice in one post).
    seen, deduped = set(), []
    for item in manifest:
        key = (item["post"], item["url"])
        if key not in seen:
            seen.add(key)
            deduped.append(item)
    MANIFEST.write_text(json.dumps(deduped, indent=2), encoding="utf-8")

    by_section = {}
    for slug, (_, _, section) in posts.items():
        by_section.setdefault(section, []).append(slug)
    for section in sorted(by_section):
        print(f"\n{section} ({len(by_section[section])}):")
        for s in sorted(by_section[section]):
            print(f"  {s}")
    print(f"\nskipped -> _incoming/unsorted: {len(SKIP)}")
    print(f"images queued: {len(deduped)}")
    for f in flags:
        print(f"flag: {f[0]} — {f[1]}")


if __name__ == "__main__":
    main()
