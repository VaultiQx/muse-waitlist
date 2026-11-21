#!/usr/bin/env python3
"""Shrink waitlist images for slow connections (Archer's phone: ~6 KB/s).
hero 1000px -> 720px q75, logo 320px -> 96px q80, gallery 640px -> 480px q72.
Same filenames, same square aspect, so no HTML changes needed except the
hero width/height attributes (updated separately). Run in waitlist-site/assets.
"""
import os
from PIL import Image

TARGETS = {
    "hero.webp": (720, 75),
    "logo.webp": (96, 80),
    "muse-01.webp": (480, 72),
    "muse-02.webp": (480, 72),
    "muse-03.webp": (480, 72),
    "muse-05.webp": (480, 72),
    "muse-07.webp": (480, 72),
    "muse-09.webp": (480, 72),
}

here = os.path.dirname(os.path.abspath(__file__))
for name, (size, q) in TARGETS.items():
    path = os.path.join(here, name)
    im = Image.open(path)
    before = os.path.getsize(path) // 1024
    im = im.resize((size, size), Image.LANCZOS)
    im.save(path, "WEBP", quality=q, method=6)
    after = os.path.getsize(path) // 1024
    print(f"{name}: {before}KB -> {after}KB ({im.size[0]}px q{q})")
