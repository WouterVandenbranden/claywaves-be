#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bouwt de statische site van claywaves.be uit content/content.py.

Gebruik:   python generate.py
Resultaat: index.html, werk.html, workshops.html, borden.html, contact.html,
           404.html, sitemap.xml en robots.txt in deze map.

Je hoeft dit script niet aan te raken om teksten, prijzen of workshopdata te
wijzigen — dat doe je in content/content.py.
"""

import hashlib
import html
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
sys.path.insert(0, str(ROOT / "content"))

import content as C  # noqa: E402

S = C.SITE


# --------------------------------------------------------------------------- helpers

def e(tekst):
    """Escape tekst voor HTML."""
    return html.escape(str(tekst), quote=True)


def paragrafen(regels):
    return "\n".join("<p>%s</p>" % e(r) for r in regels)


_versies = {}


def versie(pad):
    """Hangt een korte code op basis van de bestandsinhoud achter een pad.

    Browsers en de CDN mogen CSS, JavaScript en foto's lang bewaren (dat staat
    zo in netlify.toml). Zonder zo'n code zouden bezoekers na een wijziging nog
    dagenlang de oude versie zien. Verandert het bestand, dan verandert de code,
    en haalt de browser het opnieuw op.
    """
    if pad not in _versies:
        bestand = ROOT / pad
        if bestand.exists():
            code = hashlib.md5(bestand.read_bytes()).hexdigest()[:8]
            _versies[pad] = "%s?v=%s" % (pad, code)
        else:
            _versies[pad] = pad
    return _versies[pad]


def beeldpad(naam):
    return versie("images/%s" % naam)


# --------------------------------------------------------------------------- chrome

def head(titel, beschrijving, pad):
    gc = ""
    if S.get("goatcounter"):
        gc = (
            '\n  <script data-goatcounter="https://%s.goatcounter.com/count"\n'
            '          async src="//gc.zgo.at/count.js"></script>' % e(S["goatcounter"])
        )
    return """<!doctype html>
<html lang="%(taal)s">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>%(titel)s</title>
  <meta name="description" content="%(beschrijving)s">
  <link rel="canonical" href="%(domein)s/%(pad)s">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="ClayWaves">
  <meta property="og:title" content="%(titel)s">
  <meta property="og:description" content="%(beschrijving)s">
  <meta property="og:url" content="%(domein)s/%(pad)s">
  <meta property="og:locale" content="nl_BE">
  <meta property="og:image" content="%(domein)s/images/claywaves-logo.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="images/claywaves-logo.jpg">
  <link rel="apple-touch-icon" href="images/claywaves-logo.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;500&family=Inter:wght@400;500;600&display=swap">
  <link rel="stylesheet" href="%(css)s">%(gc)s
</head>
<body>
<a class="skip" href="#inhoud">Naar de inhoud</a>
""" % {
        "taal": e(S["taal"]),
        "titel": e(titel),
        "beschrijving": e(beschrijving),
        "domein": e(S["domein"]),
        "pad": e("" if pad == "index.html" else pad),
        "css": e(versie("assets/style.css")),
        "gc": gc,
    }


def header(actief):
    links = []
    for pad, label in C.NAV:
        cur = ' aria-current="page"' if pad == actief else ""
        links.append('<a href="%s"%s>%s</a>' % (e(pad), cur, e(label)))
    return """<header class="kop">
  <div class="wrap kop-in">
    <a class="merk" href="index.html">
      <img src="%s" alt="" width="38" height="38">
      <span class="merk-naam">ClayWaves<span class="merk-sub">%s</span></span>
    </a>
    <button class="nav-knop" type="button" aria-expanded="false" aria-controls="hoofdnav">Menu</button>
    <nav class="nav" id="hoofdnav" aria-label="Hoofdnavigatie">
      %s
    </nav>
  </div>
</header>
<main id="inhoud">
""" % (e(beeldpad("claywaves-logo.jpg")), e(S["ondertitel"]), "\n      ".join(links))


def footer():
    links = " ".join('<a href="%s">%s</a>' % (e(p), e(l)) for p, l in C.NAV)
    return """</main>
<footer class="voet">
  <div class="wrap voet-in">
    <div>
      <p><strong>%(bedrijf)s</strong><br>%(adres)s<br>BTW %(btw)s</p>
      <p><a href="tel:%(tel_link)s">%(tel)s</a> · <a href="mailto:%(mail)s">%(mail)s</a></p>
    </div>
    <div>
      <nav class="voet-nav" aria-label="Voettekst">%(links)s</nav>
      <p style="margin-top:14px"><a href="%(insta)s" rel="noopener">Instagram</a> · <a href="%(portfolio)s" rel="noopener">woutervandenbranden.be</a></p>
      <p>© %(jaar)s ClayWaves — alle rechten voorbehouden</p>
    </div>
  </div>
</footer>
<dialog class="licht" id="lichtbak" aria-label="Vergrote afbeelding">
  <button class="sluit" type="button" aria-label="Sluiten">&times;</button>
  <img alt="">
  <p class="bijschrift"></p>
</dialog>
<script src="%(js)s" defer></script>
</body>
</html>
""" % {
        "bedrijf": e(S["bedrijf"]), "adres": e(S["adres"]), "btw": e(S["btw"]),
        "tel": e(S["telefoon"]), "tel_link": e(S["telefoon_link"]), "mail": e(S["email"]),
        "links": links, "insta": e(S["instagram"]), "portfolio": e(S["portfolio_url"]),
        "jaar": date.today().year,
        "js": e(versie("assets/script.js")),
    }


def schrijf(pad, titel, beschrijving, romp):
    doel = ROOT / pad
    doel.write_text(head(titel, beschrijving, pad) + header(pad) + romp + footer(), encoding="utf-8")
    print("  geschreven:  %s" % pad)


def banner(naam, titel):
    """Brede bannerfoto met de sectietitel erover, zoals op de oude site.

    De foto staat rechtstreeks in het style-attribuut, niet via een
    CSS-variabele: een relatief pad in een variabele wordt door de browser
    opgezocht vanaf assets/style.css en dus vanuit de verkeerde map.
    """
    return ('<div class="banner" style="background-image:url(%s)"><h2>%s</h2></div>'
            % (e(beeldpad(naam)), e(titel)))


def galerij(beelden):
    stukken = []
    for naam, alt in beelden:
        stukken.append(
            '<figure>'
            '<button type="button" data-licht data-bijschrift="%(alt)s">'
            '<img src="%(src)s" alt="%(alt)s" loading="lazy">'
            '</button>'
            '<figcaption>%(alt)s</figcaption>'
            '</figure>' % {"src": e(beeldpad(naam)), "alt": e(alt)}
        )
    return '<div class="galerij">\n  %s\n</div>' % "\n  ".join(stukken)


# --------------------------------------------------------------------------- pagina's

def bouw_home():
    h = C.HOME
    secties = []
    for s in h["secties"]:
        tekst = "<h2>%s</h2>\n%s" % (e(s["kop"]), paragrafen(s["tekst"]))
        if s.get("beeld"):
            secties.append(
                '<section class="sectie-lijn"><div class="wrap split">'
                '<div class="tekstblok">%s</div>'
                '<img src="%s" alt="%s" loading="lazy">'
                '</div></section>' % (tekst, e(beeldpad(s["beeld"])), e(s.get("beeld_alt", "")))
            )
        else:
            secties.append(
                '<section class="sectie-lijn"><div class="wrap">'
                '<div class="tekstblok">%s</div></div></section>' % tekst
            )

    kaarten = "\n".join(
        '<article class="kaart"><h3>%s</h3><p>%s</p><a href="%s">%s</a></article>'
        % (e(k["titel"]), e(k["tekst"]), e(k["link"]), e(k["label"]))
        for k in h["kaarten"]
    )

    romp = """<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="oogje">%(oogje)s</p>
      <h1>ClayWaves</h1>
      <p class="lead">%(intro)s</p>
      <p style="margin-top:26px">
        <a class="knop" href="borden.html">Borden op bestelling</a>
        <a class="knop knop-licht" href="workshops.html" style="margin-left:8px">Workshops</a>
      </p>
    </div>
    <div class="hero-beeld">
      <img src="%(hero)s" alt="%(hero_alt)s" fetchpriority="high">
    </div>
  </div>
</section>

%(secties)s

<section class="sectie-lijn">
  <div class="wrap">
    <div class="kaarten">%(kaarten)s</div>
    <p class="notitie" style="margin-top:28px">Volg ons op <a href="%(insta)s" rel="noopener">Instagram</a>.</p>
  </div>
</section>
""" % {
        "oogje": e(S["ondertitel"]), "intro": e(h["intro"]),
        "hero": e(beeldpad(h["hero_beeld"])), "hero_alt": e(h["hero_alt"]),
        "secties": "\n\n".join(secties), "kaarten": kaarten, "insta": e(S["instagram"]),
    }
    schrijf("index.html", h["title"], h["description"], romp)


def bouw_werk():
    w = C.WERK
    romp = """<section class="hero">
  <div class="wrap smal">
    <p class="oogje">Portfolio</p>
    <h1>%(kop)s</h1>
    %(tekst)s
    <p style="margin-top:26px"><a class="knop" href="%(url)s" rel="noopener">%(cta)s</a></p>
  </div>
</section>
""" % {
        "kop": e(w["kop"]), "tekst": paragrafen(w["tekst"]),
        "url": e(S["portfolio_url"]), "cta": e(w["cta_label"]),
    }
    schrijf("werk.html", w["title"], w["description"], romp)


def bouw_workshops():
    w = C.WORKSHOPS

    if C.AGENDA:
        rijen = []
        for a in C.AGENDA:
            plek = e(a.get("locatie", ""))
            if a.get("link"):
                plek += ' — <a href="%s" rel="noopener">%s</a>' % (
                    e(a["link"]), e(a.get("linktekst") or a["link"])
                )
            rijen.append(
                '<li><span class="datum">%s</span><span><strong>%s</strong>'
                '<span class="plek"><br>%s</span></span></li>'
                % (e(a["datum"]), e(a["titel"]), plek)
            )
        agenda = '<ul class="agenda">\n  %s\n</ul>' % "\n  ".join(rijen)
    else:
        agenda = '<div class="leegmelding"><p>%s</p><p style="margin-top:14px">' \
                 '<a class="knop" href="contact.html">Neem contact op</a></p></div>' % e(w["agenda_leeg"])

    blokken = []
    for item in w["items"]:
        feiten = "\n".join(
            "<li><b>%s</b><span>%s</span></li>" % (e(k), e(v)) for k, v in item.get("feiten", [])
        )
        extra = ""
        if item.get("blok_tekst"):
            extra += "<h3>%s</h3>\n%s" % (e(item["blok_kop"]), paragrafen(item["blok_tekst"]))
        for kop, punten in item.get("lijsten", []):
            extra += "<h3>%s</h3>\n<ul>%s</ul>" % (
                e(kop), "".join("<li>%s</li>" % e(p) for p in punten)
            )
        beelden = ""
        if item.get("beelden"):
            beelden = '<div style="margin-top:26px">%s</div>' % galerij(item["beelden"])

        if item.get("banner"):
            kop = banner(item["banner"], item["titel"])
            klasse = "sectie-lijn sectie-banner"
            titelblok = ""
        else:
            kop = ""
            klasse = "sectie-lijn"
            titelblok = "<h2>%s</h2>" % e(item["titel"])

        blokken.append(
            '<section class="%s">%s<div class="wrap">'
            '<div class="tekstblok">%s%s%s</div>'
            '%s'
            '<ul class="feiten">%s</ul>'
            '</div></section>' % (klasse, kop, titelblok, paragrafen(item["tekst"]),
                                  extra, beelden, feiten)
        )

    romp = """<section class="hero">
  <div class="wrap smal">
    <p class="oogje">Workshops</p>
    <h1>Workshops</h1>
    <p class="lead">%(intro)s</p>
  </div>
</section>

<section class="sectie-lijn">
  <div class="wrap">
    <h2>Agenda</h2>
    %(agenda)s
  </div>
</section>

%(blokken)s
""" % {"intro": e(w["intro"]), "agenda": agenda, "blokken": "\n\n".join(blokken)}
    schrijf("workshops.html", w["title"], w["description"], romp)


def bouw_borden():
    b = C.BORDEN
    reeksen = []
    for r in b["reeksen"]:
        prijzen = "\n".join(
            '<div class="prijskaart"><h4>%s</h4><table><tbody>%s</tbody></table></div>' % (
                e(p["maat"]),
                "".join("<tr><td>%s</td><td>%s</td></tr>" % (e(k), e(v)) for k, v in p["rijen"]),
            )
            for p in r["prijzen"]
        )
        kleuren = "".join("<li>%s</li>" % e(k) for k in r["kleuren"])
        reeksen.append("""<section class="sectie-lijn" id="%(slug)s">
  <div class="wrap">
    <div class="tekstblok">
      <p class="oogje">Bordenreeks</p>
      <h2>%(naam)s</h2>
      %(tekst)s
      <h4 style="margin-top:22px">%(aantal)d kleuren</h4>
      <ul class="kleurlijst">%(kleuren)s</ul>
    </div>
    <div style="margin-top:28px">%(galerij)s</div>
    <div class="prijsblok" style="margin-top:30px">%(prijzen)s</div>
    <p class="notitie">%(disclaimer)s</p>
  </div>
</section>""" % {
            "slug": e(r["slug"]), "naam": e(r["naam"]), "tekst": paragrafen(r["tekst"]),
            "aantal": len(r["kleuren"]), "kleuren": kleuren,
            "galerij": galerij(r["beelden"]), "prijzen": prijzen,
            "disclaimer": e(r["disclaimer"]),
        })

    best = b["bestellen"]
    punten = "\n".join(
        '<article class="kaart"><h3>%s</h3><p>%s</p></article>' % (e(k), e(v))
        for k, v in best["punten"]
    )
    stappen = "\n".join(
        "<li><div><h4>%s</h4><p>%s</p></div></li>" % (e(k), e(v)) for k, v in best["stappen"]
    )

    romp = """<section class="hero">
  <div class="wrap smal">
    <p class="oogje">Op bestelling</p>
    <h1>Borden</h1>
    <p class="lead">%(intro)s</p>
  </div>
</section>

%(reeksen)s

<section class="%(bklasse)s">%(bbanner)s
  <div class="wrap">
    <div class="tekstblok">%(btitel)s%(bintro)s</div>
    <div class="kaarten" style="margin-top:26px">%(punten)s</div>
    <h3 style="margin-top:44px">%(skop)s</h3>
    <ol class="stappen">%(stappen)s</ol>
    <p class="notitie">%(slot)s</p>
    <p style="margin-top:26px"><a class="knop" href="contact.html">Stel je vraag of bestel</a></p>
  </div>
</section>
""" % {
        "intro": e(b["intro"]), "reeksen": "\n\n".join(reeksen),
        "bklasse": "sectie-lijn sectie-banner" if best.get("banner") else "sectie-lijn",
        "bbanner": banner(best["banner"], best["kop"]) if best.get("banner") else "",
        "btitel": "" if best.get("banner") else "<h2>%s</h2>" % e(best["kop"]),
        "bintro": paragrafen(best["intro"]),
        "punten": punten, "skop": e(best["stappen_kop"]), "stappen": stappen,
        "slot": e(best["slot"]),
    }
    schrijf("borden.html", b["title"], b["description"], romp)


def bouw_contact():
    c = C.CONTACT
    romp = """<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="oogje">Contact</p>
      <h1>%(kop)s</h1>
      <p class="lead">%(intro)s</p>

      <form class="contact" name="contact" method="POST" data-netlify="true"
            netlify-honeypot="bot-veld" action="/bedankt.html" style="margin-top:30px">
        <input type="hidden" name="form-name" value="contact">
        <p class="verborgen"><label>Laat dit veld leeg <input name="bot-veld"></label></p>
        <label>Naam *<input type="text" name="naam" required autocomplete="name"></label>
        <label>E-mail *<input type="email" name="email" required autocomplete="email"></label>
        <label>Onderwerp *<input type="text" name="onderwerp" required></label>
        <label>Bericht *<textarea name="bericht" required></textarea></label>
        <p style="margin:0"><button class="knop" type="submit">Verstuur</button></p>
      </form>
    </div>

    <div>
      <ul class="gegevens">
        <li><span class="etiket">Telefoon</span><a href="tel:%(tel_link)s">%(tel)s</a></li>
        <li><span class="etiket">E-mail</span><a href="mailto:%(mail)s">%(mail)s</a></li>
        <li><span class="etiket">Adres</span>%(adres)s</li>
        <li><span class="etiket">IBAN</span>%(iban)s</li>
        <li><span class="etiket">BTW</span>%(btw)s (mSENSE bv)</li>
        <li><span class="etiket">Instagram</span><a href="%(insta)s" rel="noopener">@claywaves_atelier</a></li>
      </ul>
    </div>
  </div>
</section>
""" % {
        "kop": e(c["kop"]), "intro": e(c["intro"]),
        "tel": e(S["telefoon"]), "tel_link": e(S["telefoon_link"]), "mail": e(S["email"]),
        "adres": e(S["adres"]), "iban": e(S["iban"]), "btw": e(S["btw"]),
        "insta": e(S["instagram"]),
    }
    schrijf("contact.html", c["title"], c["description"], romp)


def bouw_bedankt():
    romp = """<section class="hero">
  <div class="wrap smal">
    <p class="oogje">Contact</p>
    <h1>Bedankt</h1>
    <p class="lead">Je bericht is verstuurd. We nemen zo snel mogelijk contact op.</p>
    <p style="margin-top:26px"><a class="knop" href="index.html">Terug naar de homepagina</a></p>
  </div>
</section>
"""
    schrijf("bedankt.html", "Bedankt — ClayWaves", "Je bericht is verstuurd.", romp)


def bouw_404():
    romp = """<section class="hero">
  <div class="wrap smal">
    <p class="oogje">404</p>
    <h1>Deze pagina bestaat niet</h1>
    <p class="lead">De pagina die je zocht is verplaatst of verdwenen.</p>
    <p style="margin-top:26px"><a class="knop" href="index.html">Terug naar de homepagina</a></p>
  </div>
</section>
"""
    schrijf("404.html", "Pagina niet gevonden — ClayWaves", "Pagina niet gevonden.", romp)


def bouw_sitemap():
    vandaag = date.today().isoformat()
    paden = [p for p, _ in C.NAV]
    items = "\n".join(
        "  <url><loc>%s/%s</loc><lastmod>%s</lastmod></url>"
        % (S["domein"], "" if p == "index.html" else p, vandaag)
        for p in paden
    )
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % items,
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % S["domein"], encoding="utf-8"
    )
    print("  geschreven:  sitemap.xml, robots.txt")


def main():
    print("ClayWaves — site bouwen")
    bouw_home()
    bouw_werk()
    bouw_workshops()
    bouw_borden()
    bouw_contact()
    bouw_bedankt()
    bouw_404()
    bouw_sitemap()
    ontbrekend = controleer_beelden()
    print("Klaar.")
    if ontbrekend:
        print("\nLet op — deze afbeeldingen ontbreken nog in images/:")
        for n in ontbrekend:
            print("   - %s" % n)
        print("Draai 'python scripts/download_images.py' om ze van de oude site te halen.")


def controleer_beelden():
    nodig = ["claywaves-logo.jpg", C.HOME["hero_beeld"]]
    nodig += [s["beeld"] for s in C.HOME["secties"] if s.get("beeld")]
    for item in C.WORKSHOPS["items"]:
        nodig += [n for n, _ in item.get("beelden", [])]
        if item.get("banner"):
            nodig.append(item["banner"])
    for r in C.BORDEN["reeksen"]:
        nodig += [n for n, _ in r["beelden"]]
    if C.BORDEN["bestellen"].get("banner"):
        nodig.append(C.BORDEN["bestellen"]["banner"])
    return [n for n in dict.fromkeys(nodig) if not (ROOT / "images" / n).exists()]


if __name__ == "__main__":
    main()
