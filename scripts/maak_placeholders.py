#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zet tijdelijke vervangfoto's in images/ zodat de site meteen te bekijken is
terwijl de echte foto's er nog niet zijn.

De namen van de aangemaakte bestanden komen in images/PLACEHOLDERS.txt.
download_images.py overschrijft precies die bestanden met de echte foto's.
"""

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "content"))
import content as C  # noqa: E402

DOEL = ROOT / "images"

PALET = {
    "graniet": (196, 200, 199),
    "natuur": (150, 126, 100),
    "raku": (128, 96, 78),
    "workshop": (132, 122, 100),
    "atelier": (158, 136, 112),
    "werk": (142, 124, 104),
    "claywaves": (154, 106, 69),
}


def kleur_voor(naam):
    for sleutel, rgb in PALET.items():
        if naam.startswith(sleutel):
            return rgb
    return (160, 148, 132)


def maak(naam, breedte=1200, hoogte=1200):
    grond = kleur_voor(naam)
    afb = Image.new("RGB", (breedte, hoogte), grond)
    tek = ImageDraw.Draw(afb)
    # zachte diagonale banden, zodat het duidelijk een plaatshouder is
    for i in range(-hoogte, breedte, 90):
        tek.line([(i, 0), (i + hoogte, hoogte)],
                 fill=tuple(max(0, k - 12) for k in grond), width=34)
    label = naam.rsplit(".", 1)[0].replace("-", " ")
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 42)
    except OSError:
        font = ImageFont.load_default()
    doos = tek.textbbox((0, 0), label, font=font)
    tek.text(((breedte - doos[2]) / 2, (hoogte - doos[3]) / 2), label,
             fill=(255, 252, 246), font=font)
    tek.text((28, hoogte - 60), "tijdelijke afbeelding", fill=(255, 252, 246), font=font)
    afb.save(DOEL / naam, "JPEG", quality=72)


def main():
    DOEL.mkdir(exist_ok=True)
    nodig = ["claywaves-logo.jpg", C.HOME["hero_beeld"]]
    nodig += [s["beeld"] for s in C.HOME["secties"] if s.get("beeld")]
    nodig += [n for n, _ in C.WORKSHOPS["beelden"]]
    for r in C.BORDEN["reeksen"]:
        nodig += [n for n, _ in r["beelden"]]

    gemaakt = []
    for naam in dict.fromkeys(nodig):
        if (DOEL / naam).exists():
            continue
        maak(naam)
        gemaakt.append(naam)

    if gemaakt:
        merker = DOEL / "PLACEHOLDERS.txt"
        bestaand = merker.read_text(encoding="utf-8").split() if merker.exists() else []
        merker.write_text("\n".join(sorted(set(bestaand) | set(gemaakt))) + "\n", encoding="utf-8")
    print("%d tijdelijke afbeeldingen aangemaakt." % len(gemaakt))


if __name__ == "__main__":
    main()
