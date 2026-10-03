#!/usr/bin/env python3
"""Extract authentic research figures for the website.

Sources:
  1. pub/*.pdf                               -> every embedded figure (>15 KB) + rendered first pages
  2. port stuff/cov_stuff/*/figures/*.pdf    -> vector figures rendered to PNG
  3. port stuff/port_v1.pptx                 -> embedded slide media

Raw output goes to "port stuff/_review/" (untracked; some figures are >10 MB).
bin/build_web_assets.py then crops/resizes the chosen figures into
assets/img/research/ and assets/img/publications/.

Usage:  python3 bin/extract_research_assets.py && python3 bin/build_web_assets.py
Requires: pip install pymupdf pillow
"""
import os
import re
import zipfile

import pymupdf as fitz

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB_DIR = os.path.join(ROOT, "pub")
REVIEW = os.path.join(ROOT, "port stuff", "_review")
OUT_PUB = os.path.join(REVIEW, "raw")
MIN_BYTES = 15000

# Short, stable prefixes for each paper PDF.
PREFIX = {
    "GESCE_Graph-based_Ergodic_Search_in_Cluttered_Environments.pdf": "gesce",
    "CAP_A_Connectivity-Aware_Hierarchical_Coverage_Path_Planning_Algorithm_for_Unknown_Environments_using_Coverage_Guidance_Graph.pdf": "cap",
    "A_Bayesian_Modeling_Framework_for_Estimation_and_Ground_Segmentation_of_Cluttered_Staircases.pdf": "stairs",
    "Design_of_a_Remotely_Operated_Vehicle_ROV_for_Biofoul_Cleaning_and_Inspection_of_Variety_of_Underwater_Structures.pdf": "rov",
    "Shirose_2022_J._Phys.%3A_Conf._Ser._2251_012002.pdf": "brakearm",
    "2025-01-0433.pdf": "convoy",
}


def slug(name):
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def extract_pub_figures():
    os.makedirs(OUT_PUB, exist_ok=True)
    os.makedirs(os.path.join(REVIEW, "pages"), exist_ok=True)
    for pdf_file in sorted(os.listdir(PUB_DIR)):
        if not pdf_file.endswith(".pdf"):
            continue
        prefix = PREFIX.get(pdf_file, slug(os.path.splitext(pdf_file)[0])[:24])
        doc = fitz.open(os.path.join(PUB_DIR, pdf_file))
        img_idx = 0
        seen = set()
        for page_idx, page in enumerate(doc):
            for img in page.get_images(full=True):
                xref = img[0]
                if xref in seen:
                    continue
                seen.add(xref)
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                if len(image_bytes) <= MIN_BYTES:
                    continue
                ext = base_image["ext"]
                fn = os.path.join(OUT_PUB, f"{prefix}_p{page_idx + 1}_fig{img_idx}.{ext}")
                with open(fn, "wb") as f:
                    f.write(image_bytes)
                img_idx += 1
        # Render the first pages (Figure 1 is usually on page 1-2) for review / cropping.
        for page_idx in range(min(len(doc), 8)):
            pix = doc[page_idx].get_pixmap(dpi=110)
            pix.save(os.path.join(REVIEW, "pages", f"{prefix}_page{page_idx + 1}.png"))
        print(f"{prefix}: {img_idx} embedded figures, {len(doc)} pages")


def render_latex_figures():
    for proj in ("CAP__IROS_2025_", "TAP__Journal_"):
        src = os.path.join(ROOT, "port stuff", "cov_stuff", proj, "figures")
        dst = os.path.join(REVIEW, "latex", slug(proj))
        os.makedirs(dst, exist_ok=True)
        for fn in sorted(os.listdir(src)):
            if not fn.endswith(".pdf"):
                continue
            doc = fitz.open(os.path.join(src, fn))
            pix = doc[0].get_pixmap(dpi=200)
            pix.save(os.path.join(dst, fn[:-4] + ".png"))
        print(f"{proj}: rendered")


def extract_pptx_media(pptx="port_v1.pptx"):
    dst = os.path.join(REVIEW, "pptx")
    os.makedirs(dst, exist_ok=True)
    with zipfile.ZipFile(os.path.join(ROOT, "port stuff", pptx)) as z:
        names = [n for n in z.namelist() if n.startswith("ppt/media/")]
        for n in names:
            out = os.path.join(dst, os.path.basename(n))
            with open(out, "wb") as f:
                f.write(z.read(n))
        print(f"{pptx}: {len(names)} media files")
        # map media -> slide for context
        rel_re = re.compile(r'Target="\.\./media/([^"]+)"')
        with open(os.path.join(dst, "_slide_map.txt"), "w") as f:
            for n in sorted(z.namelist()):
                m = re.match(r"ppt/slides/_rels/slide(\d+)\.xml\.rels", n)
                if m:
                    media = rel_re.findall(z.read(n).decode("utf8", "ignore"))
                    f.write(f"slide{m.group(1)}: {' '.join(media)}\n")


if __name__ == "__main__":
    extract_pub_figures()
    render_latex_figures()
    extract_pptx_media()
