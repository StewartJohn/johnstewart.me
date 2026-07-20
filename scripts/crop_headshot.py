#!/usr/bin/env python3
"""Crop the source portrait into a square headshot.

Usage: crop_headshot.py SRC OUT cx cy frac
  cx, cy : center of the square as fractions of the upright image (0..1)
  frac   : square side length as a fraction of the image width
Applies EXIF orientation first, clamps the square to the image bounds,
and writes a 512x512 JPEG.
"""
import sys
from PIL import Image, ImageOps

src, out = sys.argv[1], sys.argv[2]
cx, cy, frac = float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])

img = ImageOps.exif_transpose(Image.open(src))
W, H = img.size
side = int(frac * W)
left = int(cx * W - side / 2)
top = int(cy * H - side / 2)
left = max(0, min(left, W - side))
top = max(0, min(top, H - side))
crop = img.crop((left, top, left + side, top + side)).resize((512, 512), Image.LANCZOS)
crop.convert("RGB").save(out, "JPEG", quality=88, optimize=True, progressive=True)
print(f"upright={W}x{H} side={side} box=({left},{top},{left+side},{top+side}) -> {out}")
