#!/usr/bin/env python3
"""Curate extracted research figures into web-sized assets.

Run after bin/extract_research_assets.py. Writes:
  assets/img/research/*        project figures for the bento grid (max 1400 px)
  assets/img/publications/*    publication thumbnails (max 640 px)
Every output is an unmodified crop/resize of a figure from a paper, LaTeX
source, slide deck, or experiment video. Nothing is generated.
"""
import os
from PIL import Image, ImageChops

Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.join(ROOT, "port stuff", "_review")
PS = os.path.join(ROOT, "port stuff")

RESEARCH = {
    # name: (source, max_width)
    "cap_warehouse.jpg": (f"{R}/latex/tap_journal/main.png", 1400),
    "cap_method.png": (f"{PS}/cov_stuff/iros_selected_figs/iros_methodology_fig.png", 1400),
    "cap_multi_results.png": (f"{PS}/cov_stuff/multi-cap_results.png", 1400),
    "cap_realworld_rviz.jpg": (f"{PS}/cov_stuff/iros_selected_figs/tap_ex1.png", 1400),
    "gesce_fig1.png": (f"{R}/raw/gesce_p1_fig0.png", 1200),
    "gesce_baselines.png": (f"{R}/raw/gesce_p4_fig2.png", 1200),
    "gesce_benchmark_maps.png": (f"{R}/raw/gesce_p5_fig4.png", 1200),
    "snake_binsat_pipeline.png": (f"{R}/snake/image11_r.png", 1400),
    "snake_hardware.jpg": (f"{R}/snake/image10.png", 1200),
    "convoy_fleet.jpg": (f"{R}/raw/convoy_p5_fig0.jpeg", 1200),
    "convoy_network_aerial.jpg": (f"{R}/raw/convoy_p18_fig31.png", 1200),
}

THUMBS = {
    "gesce.png": f"{R}/raw/gesce_p1_fig0.png",
    "cap.jpg": f"{R}/raw/cap_p4_fig3.png",
    "convoy.jpg": f"{R}/raw/convoy_p18_fig31.png",
    "stairs.jpg": f"{R}/raw/stairs_p1_fig0.jpeg",
    "rov.jpg": f"{R}/raw/rov_p3_fig6.jpeg",
    "brakearm.jpg": f"{R}/raw/brakearm_p4_fig3.jpeg",
}


def trim(im, pad=8):
    """Remove uniform white margins left over from PDF rendering."""
    rgb = im.convert("RGB")
    bg = Image.new("RGB", rgb.size, (255, 255, 255))
    diff = ImageChops.difference(rgb, bg).convert("L").point(lambda p: 255 if p > 12 else 0)
    box = diff.getbbox()
    if not box:
        return im
    l, t, r, b = box
    return im.crop((max(l - pad, 0), max(t - pad, 0), min(r + pad, im.width), min(b + pad, im.height)))


def save(im, path, max_w):
    im = trim(im)
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    if path.endswith(".jpg"):
        im.convert("RGB").save(path, quality=82, optimize=True, progressive=True)
    else:
        if im.mode not in ("RGB", "RGBA", "P"):
            im = im.convert("RGB")
        im.save(path, optimize=True)
    print(f"{os.path.relpath(path, ROOT)}  {im.width}x{im.height}  {os.path.getsize(path)//1024} KB")


if __name__ == "__main__":
    out_r = os.path.join(ROOT, "assets", "img", "research")
    out_p = os.path.join(ROOT, "assets", "img", "publications")
    os.makedirs(out_r, exist_ok=True)
    os.makedirs(out_p, exist_ok=True)
    for name, (src, w) in RESEARCH.items():
        save(Image.open(src), os.path.join(out_r, name), w)
    for name, src in THUMBS.items():
        save(Image.open(src), os.path.join(out_p, name), 640)
