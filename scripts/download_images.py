#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Haalt de foto's van de oude claywaves.be (one.com) op en zet ze met nette
bestandsnamen in images/.

Draai dit ÉÉN keer, zolang de oude site nog online staat:

    python scripts/download_images.py

Daarna staan de foto's lokaal in de repo en is one.com niet meer nodig.
Heb je zelf betere originelen? Zet die dan gewoon over de gedownloade
bestanden heen — de bestandsnamen in images/ zijn wat telt.
"""

import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOEL = ROOT / "images"

BASIS = ("https://impro.usercontent.one/appid/oneComWsb/domain/claywaves.be"
         "/media/claywaves.be/onewebmedia/")

# (bestandsnaam op de oude site, nieuwe naam, extra parameters)
# rotate=90 staat erbij waar de oude site de foto rechtzette.
BEELDEN = [
    ("ClayWaves logo.jpg",                          "claywaves-logo.jpg",     ""),
    ("2023-09-01 21.02.14.jpg",                     "atelier-werk.jpg",       ""),
    ("WhatsApp Image 2023-08-27 at 15.50.30.jpeg",  "werk-detail.jpg",        ""),
    ("2023-05-21 12.28.02-1.jpg",                   "raku-stook.jpg",         "&rotate=90"),
    ("2023-06-11 19.40.22.jpg",                     "raku-rookton.jpg",       ""),
    ("2023-06-11 19.39.23.jpg",                     "raku-resultaat.jpg",     "&rotate=90"),
    ("2024-09-15 09.04.28-1.jpg",                   "workshop-textuur.jpg",   "&rotate=90"),

    ("graniet overzicht.jpg",                       "graniet-overzicht.jpg",  ""),
    ("graniet gestapeld.jpg",                       "graniet-gestapeld.jpg",  ""),
    ("graniet grijs.jpg",                           "graniet-graniet.jpg",    ""),
    ("graniet geel.jpg",                            "graniet-zon.jpg",        ""),
    ("graniet aqua .jpg",                           "graniet-aqua.jpg",       ""),
    ("graniet sky.jpg",                             "graniet-sky.jpg",        ""),
    ("graniet marine.jpg",                          "graniet-marine.jpg",     ""),
    ("graniet i love you.jpg",                      "graniet-i-love-you.jpg", ""),
    ("graniet laurier.jpg",                         "graniet-laurier.jpg",    ""),

    ("natuur overzicht.jpg",                        "natuur-overzicht.jpg",   ""),
    ("natuur gestapeld.jpg",                        "natuur-gestapeld.jpg",   ""),
    ("natuur plas.jpg",                             "natuur-plas.jpg",        ""),
    ("natuur vulkaan.jpg",                          "natuur-vulkaan.jpg",     ""),
    ("natuur zeemeermin.jpg",                       "natuur-zeemeermin.jpg",  ""),
    ("natuur zeeschilpad.jpg",                      "natuur-zeeschilpad.jpg", ""),
    ("natuur atlantis.jpg",                         "natuur-atlantis.jpg",    ""),
    ("natuur bloesem.jpg",                          "natuur-bloesem.jpg",     ""),
    ("natuur rivierbodem.jpg",                      "natuur-rivierbodem.jpg", ""),
    ("natuur rots.jpg",                             "natuur-rots.jpg",        ""),
    ("natuur strand.jpg",                           "natuur-strand.jpg",      ""),
]

# Maximaal 1600 px breed/hoog — ruim genoeg voor het web, en veel lichter.
PARAMS = "?withoutEnlargement&resize=1600,1600&quality=85"


def plaatshouders():
    """Namen van tijdelijke afbeeldingen — die mogen overschreven worden."""
    merker = DOEL / "PLACEHOLDERS.txt"
    if merker.exists():
        return set(merker.read_text(encoding="utf-8").split())
    return set()


def main():
    DOEL.mkdir(exist_ok=True)
    tijdelijk = plaatshouders()
    vervangen = set()
    ok, mis = 0, []
    for bron, naam, extra in BEELDEN:
        pad = DOEL / naam
        if pad.exists() and pad.stat().st_size > 0 and naam not in tijdelijk:
            print("  bestaat al:  %s" % naam)
            ok += 1
            continue
        url = BASIS + urllib.parse.quote(bron) + PARAMS + extra
        try:
            verzoek = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(verzoek, timeout=45) as r:
                data = r.read()
            if len(data) < 500:
                raise ValueError("bestand te klein (%d bytes)" % len(data))
            pad.write_bytes(data)
            print("  gedownload:  %-24s %6.0f kB" % (naam, len(data) / 1024))
            vervangen.add(naam)
            ok += 1
        except Exception as fout:  # noqa: BLE001
            print("  MISLUKT:     %-24s %s" % (naam, fout))
            mis.append((naam, bron))

    rest = tijdelijk - vervangen
    merker = DOEL / "PLACEHOLDERS.txt"
    if rest:
        merker.write_text("\n".join(sorted(rest)) + "\n", encoding="utf-8")
    elif merker.exists():
        merker.unlink()

    print("\n%d van %d afbeeldingen staan in images/." % (ok, len(BEELDEN)))
    if mis:
        print("\nNiet gelukt voor:")
        for naam, bron in mis:
            print("   %s  (oude naam: %s)" % (naam, bron))
        print("Staat de oude site al offline? Zet de foto's dan zelf in images/ "
              "onder exact deze bestandsnamen.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
