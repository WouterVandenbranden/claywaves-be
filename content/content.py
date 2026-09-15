# -*- coding: utf-8 -*-
"""
Alle inhoud van claywaves.be staat in dit bestand.
Wil je een tekst, prijs of workshopdatum aanpassen? Pas het hier aan en
draai daarna:  python generate.py
"""

SITE = {
    "naam": "ClayWaves",
    "ondertitel": "Keramiek atelier",
    "domein": "https://www.claywaves.be",
    "taal": "nl-BE",
    "instagram": "https://www.instagram.com/claywaves_atelier",
    "telefoon": "0476 484803",
    "telefoon_link": "+32476484803",
    "email": "wouter@claywaves.be",
    "iban": "BE95 0688 9593 3958",
    "btw": "BE0849.727.819",
    "bedrijf": "Wouter Vandenbranden — mSENSE bv",
    "adres": "Steilvoordehof 7 — 9070 Heusden",
    "portfolio_url": "https://www.woutervandenbranden.be",
    # GoatCounter: vul hier je sitecode in (bv. "claywaves"), leeg = geen statistieken
    "goatcounter": "",
}

NAV = [
    ("index.html", "Home"),
    ("werk.html", "Werk"),
    ("workshops.html", "Workshops"),
    ("borden.html", "Borden op bestelling"),
    ("contact.html", "Contact"),
]

# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------

HOME = {
    "title": "ClayWaves — keramiek atelier",
    "description": "ClayWaves is Anja en Wouter. Keramiek die de schoonheid van het "
                   "onvolmaakte omarmt: wabi-sabi, aardse tinten en verweerde texturen.",
    "hero_beeld": "atelier-werk.jpg",
    "hero_alt": "Keramiek van ClayWaves",
    "intro": "ClayWaves is Anja en Wouter. Zij bouwt op, hij draait.",
    "secties": [
        {
            "kop": "Het onvolmaakte",
            "tekst": [
                "Claywaves schept keramiek die de schoonheid van het onvolmaakte omarmt. "
                "We voelen verwantschap met de wabi-sabi filosofie – een benadering die "
                "schoonheid vindt in imperfectie en vergankelijkheid. Het gaat niet om het "
                "vermijden van fouten, maar om het omarmen van wat er spontaan ontstaat – "
                "alsof de klei zelf spreekt en aangeeft wat moet gebeuren.",
            ],
        },
        {
            "kop": "De natuur als bron",
            "tekst": [
                "De natuur is onze primaire inspiratiebron. We vertalen landschappen in een "
                "zacht palet van aardse tinten – zachte bruinen, gedempte groenen en grijzen "
                "die de sporen van tijd weerspiegelen. Occasioneel doorbreken we deze rust "
                "met fellere accenten die de aandacht vestigen op de onderliggende structuur.",
                "Door te werken met verweerde structuren en kleuren worden we geconfronteerd "
                "met vergankelijkheid. We creëren objecten die gedragen lijken, die een "
                "verhaal vertellen van slijtage en tijd – terwijl we tegelijkertijd werken "
                "met keramiek, een materiaal dat praktisch eeuwig is.",
            ],
            "beeld": "werk-detail.jpg",
            "beeld_alt": "Detail van een keramisch werk met verweerde textuur",
        },
        {
            "kop": "Draaien en opbouwen",
            "tekst": [
                "Ons werk beweegt zich tussen draaien en opbouwtechnieken. We zien onze "
                "technieken niet als vaststaand, maar als een voortdurende dialoog tussen "
                "maker, materiaal en toeval. De draaitechniek vormt meestal de basis, maar "
                "wordt vaak aangevuld en uitgedaagd door verdere bewerkingen.",
            ],
        },
        {
            "kop": "Functionaliteit, maar niet ten koste van alles",
            "tekst": [
                "Functionaliteit blijft voor ons een wezenlijk aspect van keramiek, maar niet "
                "ten koste van alles. We zijn bereid om een deel van de praktische "
                "bruikbaarheid op te offeren voor artistieke expressie. Een vaas hoeft niet "
                "perfect praktisch te zijn – soms is een beperkte openingsbreedte of een "
                "onverwachte hoogte net wat het object zijn unieke karakter geeft.",
            ],
        },
        {
            "kop": "Experiment",
            "tekst": [
                "Experimenteren zit in de kern van ons creatieproces. Soms gebruiken we "
                "bijvoorbeeld onverwachte dragers die tijdens het stookproces wegbranden – "
                "alledaagse objecten die onregelmatige vormen creëren. Elke stook is een "
                "avontuur waarbij materialen hun eigen verhaal vertellen.",
            ],
        },
        {
            "kop": "Vernieuwing zit in de verschuiving",
            "tekst": [
                "Innovatie is voor ons geen zoektocht naar het absolute nieuwe, maar een "
                "subtiel spel van herschikking en nuance. We geloven dat niets echt origineel "
                "is – alles is reeds gedacht of gemaakt. Onze uitdaging zit in het "
                "herinterpreteren van bestaande elementen, het toevoegen van een persoonlijke "
                "toets die bekende vormen net een andere resonantie geeft. Elk object is een "
                "nieuwe vertaling van eeuwenoude verhalen, door iets toe te voegen, of door "
                "anders te verbinden. Onze vernieuwing zit in subtiele verschuivingen, in het "
                "zacht oprekken van bekende grenzen en het introduceren van net die kleine "
                "onverwachte elementen die verrassen.",
            ],
        },
        {
            "kop": "Klank",
            "tekst": [
                "Onze keramische installaties worden vergezeld door een zorgvuldig "
                "samengestelde soundtrack die de zintuiglijke beleving verrijkt. Net zoals elk "
                "keramisch object zijn eigen verhaal vertelt, creëren de muzikale lijnen een "
                "extra laag van beleving. De gekozen nummers resoneren met de textuur, energie "
                "en emotie van onze werken – een auditieve dialoog die de grenzen tussen "
                "geluid en vorm verkent, waarbij toeval en intentie elkaar ontmoeten.",
            ],
        },
    ],
    "kaarten": [
        {
            "titel": "Workshops",
            "tekst": "Raku, Obvara en Saggar, en draaien met textuur — op verplaatsing in "
                     "jouw atelier of op locatie.",
            "link": "workshops.html",
            "label": "Bekijk de workshops",
        },
        {
            "titel": "Borden op bestelling",
            "tekst": "Twee handgemaakte bordenreeksen, GRANIET en NATUUR, in zestien kleuren.",
            "link": "borden.html",
            "label": "Bekijk de borden",
        },
        {
            "titel": "Autonoom werk",
            "tekst": "Het vrije keramiekwerk van Wouter — portfolio, tentoonstellingen en "
                     "artistiek statement.",
            "link": "werk.html",
            "label": "Naar het portfolio",
        },
    ],
}

# ---------------------------------------------------------------------------
# WERK (doorverwijzing naar het portfolio)
# ---------------------------------------------------------------------------

WERK = {
    "title": "Werk — ClayWaves",
    "description": "Het autonome keramiekwerk van Wouter Vandenbranden vind je op "
                   "woutervandenbranden.be.",
    "kop": "Autonoom werk",
    "tekst": [
        "ClayWaves staat voor het gedeelde atelierwerk van Anja en Wouter: de workshops, "
        "de bordenreeksen en het werk dat daaruit voortkomt.",
        "Het autonome, vrije keramiekwerk van Wouter — de tentoonstellingen, het portfolio "
        "per jaar en het artistieke statement — staat op een eigen site.",
    ],
    "cta_label": "Ga naar woutervandenbranden.be",
}

# ---------------------------------------------------------------------------
# WORKSHOPS
# ---------------------------------------------------------------------------

# Agenda: voeg hier data toe in de vorm
#     {"datum": "30 mei 2027", "titel": "Raku en Saggar", "locatie": "Clay Days — Muizen, Mechelen", "link": ""}
# Laat de lijst leeg als er niets gepland staat; de pagina toont dan automatisch
# een nette melding in plaats van een lege agenda.
#
# LET OP — de oude site toonde nog deze data zonder jaartal (achterhaald):
#     Raku en Saggar:        30 mei — Clay Days, Muizen (Mechelen)
#                            13 juni — ClayMates, Gent
#     Theepotten draaien:    6-13-20-27 mei, 10-24 juni — Cultuurhuis Merelbeke
# Vul ze hieronder opnieuw in mét jaartal zodra de nieuwe data vastliggen.
AGENDA = []

WORKSHOPS = {
    "title": "Workshops — ClayWaves",
    "description": "Raku, Obvara en Saggar, en draaien met textuur. Workshops op "
                   "verplaatsing, gegeven door Wouter Vandenbranden.",
    "intro": "Wouter geeft de onderstaande workshops op verplaatsing. Heb je een atelier "
             "of een locatie en wil je een workshop hosten? Laat het weten via "
             "wouter@claywaves.be.",
    "agenda_leeg": "Er staan op dit moment geen publieke data gepland. Wil je een workshop "
                   "hosten of op de hoogte blijven van nieuwe data? Stuur een bericht.",
    "beelden": [
        ("raku-stook.jpg", "Raku-stook: roodgloeiende potten uit de oven"),
        ("raku-rookton.jpg", "Potten in de Raku-rookton"),
        ("raku-resultaat.jpg", "Resultaat van een Raku-stook"),
        ("workshop-textuur.jpg", "Draaien met textuur op de draaischijf"),
    ],
    "items": [
        {
            "titel": "Raku, Obvara en Saggar",
            "tekst": [
                "Breng je bisquit gebakken werkstukken mee om te glazuren en stoken gedurende "
                "de workshop (3 stuks, max 20 cm hoog, max 20 cm diameter — meer stukken "
                "kunnen als het ovenplaatoppervlak maximaal overeen blijft komen met de "
                "3× diameter 20 cm).",
                "Als klei kies je best voor een zwaarder gechammotteerde klei (minstens 40% "
                "0,5 mm of 25% 1 mm) of een klei met hoog aluminiumgehalte (bijvoorbeeld door "
                "toevoeging van 30% zilverzand). Voor draaiers is de zware chamotte niet "
                "altijd even praktisch, maar zorg zeker voor chamotte in je klei, en voor "
                "gecomprimeerde randen (laat de laatste beweging bij het draaien een sluitende "
                "beweging zijn).",
                "Voor de personen die zelf geen bisquit gebakken potten beschikbaar hebben, "
                "maar zich toch willen onderdompelen in de wondere wereld van Raku, Obvara en "
                "Saggar, heb ik potjes beschikbaar aan 10–20 €/stuk al naargelang de grootte.",
            ],
            "blok_kop": "Hoe ziet een typische raku-dag eruit?",
            "blok_tekst": [
                "We starten om 10u met een woordje uitleg over Raku, Obvara en Saggar, "
                "gevolgd door het glazuren en voorbereiden van de bisquit gebakken potten. "
                "Rond 11u30 gaan de ovens aan, terwijl we lunchen (lunch zelf mee te brengen, "
                "of wij voorzien een broodje voor jou aan kostprijs). We stoken de potten tot "
                "ongeveer 1000 °C.",
                "Na het stoken komt het spektakel: de potten worden roodgloeiend uit de oven "
                "gehaald en gaan in de Raku-rookton of de Obvara-soep. Alles gebeurt uiteraard "
                "buiten (afgelasting mogelijk bij slecht weer). De dag sluiten we af rond "
                "17–18u, afhankelijk van het aantal deelnemers en de grootte van het "
                "keramiekwerk.",
                "Andere formules zijn ook mogelijk, zoals een avondsessie waarbij we — omwille "
                "van de beperktere tijd — focussen op Raku. Een avondsessie loopt typisch van "
                "17u30 tot ongeveer 22u.",
            ],
            "feiten": [
                ("Duur", "Volledige dag, 10u – 17/18u (avondsessie: 17u30 – 22u)"),
                ("Meebrengen", "3 bisquit gebakken stukken, max 20 cm hoog en breed"),
                ("Klei", "Zwaar gechamotteerd of hoog aluminiumgehalte"),
                ("Potjes ter plaatse", "10–20 € per stuk"),
            ],
        },
        {
            "titel": "Draaien met textuur",
            "tekst": [
                "We gaan dieper in op hoe je vormen met mooie, ruwe texturen kan draaien op de "
                "draaischijf. Tijdens de workshop kruipen we achter de draaischijf en gaan we "
                "experimenteren.",
                "We gaan aan de slag met waterglas, kleipoeder, slibs, massagerollertjes, "
                "kaasschaven, enzovoort. Om deel te kunnen nemen aan deze workshop moet je "
                "vlot met 1 kg klei aan de slag kunnen op de draaischijf, zodat we voldoende "
                "kunnen focussen op de textuurtechnieken zelf.",
                "Deze workshop kan ik in jouw atelier komen geven voor maximaal 10 personen.",
            ],
            "blok_kop": "Praktisch",
            "blok_tekst": [],
            "lijsten": [
                ("Dit breng je zelf mee", [
                    "handdoek en schort",
                    "dozen, bakken … om je pas gedraaide stukken mee naar huis te nemen "
                    "(tip: draai je op je eigen bats, dan kan je de stukken daarop meenemen)",
                    "lunchpakket",
                ]),
                ("Ik zorg voor", [
                    "de specifieke tools en producten",
                ]),
            ],
            "feiten": [
                ("Duur", "Volledige dag, 10u – 16u30"),
                ("Groepsgrootte", "Maximaal 10 personen"),
                ("Niveau", "Je draait vlot met 1 kg klei"),
                ("Locatie", "Op verplaatsing, in jouw atelier"),
            ],
        },
    ],
}

# ---------------------------------------------------------------------------
# BORDEN
# ---------------------------------------------------------------------------

BORDEN = {
    "title": "Borden op bestelling — ClayWaves",
    "description": "Handgemaakte borden in twee reeksen: GRANIET (7 kleuren) en NATUUR "
                   "(9 effectglazuren). Vaatwas- en microgolfbestendig.",
    "intro": "Twee reeksen, met de hand gedraaid en geglazuurd. Elk bord wordt op "
             "bestelling gemaakt — er is geen voorraad.",
    "reeksen": [
        {
            "naam": "GRANIET",
            "slug": "graniet",
            "tekst": [
                "Deze bordenreeks is gemaakt uit lichtgrijze spikkelklei die zichtbaar blijft "
                "door de gekleurd transparante glazuur. De borden werden op hoge temperatuur "
                "gebakken waardoor ze vaatwas- en microgolfovenbestendig zijn.",
                "Binnenkant en onderkant zijn geglazuurd, maar op de zijkant is de klei "
                "ongeglazuurd gelaten zodat deze borden een ruw karakter krijgen.",
            ],
            "kleuren": ["graniet", "zon", "aqua", "sky", "marine", "i love you", "laurier"],
            "prijzen": [
                {"maat": "diameter 26 cm", "rijen": [("1 – 5 borden", "25 €"),
                                                      ("vanaf 6 borden", "22 €"),
                                                      ("vanaf 12 borden", "20 €")]},
                {"maat": "diameter 21 cm", "rijen": [("1 – 5 borden", "22 €"),
                                                      ("vanaf 6 borden", "20 €"),
                                                      ("vanaf 12 borden", "18 €")]},
            ],
            "beelden": [
                ("graniet-overzicht.jpg", "Overzicht van de reeks GRANIET"),
                ("graniet-gestapeld.jpg", "De GRANIET-borden gestapeld"),
                ("graniet-graniet.jpg", "Bord GRANIET, kleur graniet"),
                ("graniet-zon.jpg", "Bord GRANIET, kleur zon"),
                ("graniet-aqua.jpg", "Bord GRANIET, kleur aqua"),
                ("graniet-sky.jpg", "Bord GRANIET, kleur sky"),
                ("graniet-marine.jpg", "Bord GRANIET, kleur marine"),
                ("graniet-i-love-you.jpg", "Bord GRANIET, kleur i love you"),
                ("graniet-laurier.jpg", "Bord GRANIET, kleur laurier"),
            ],
            "disclaimer": "Deze borden zijn handwerk en unieke stukken. Dat wil zeggen dat "
                          "grootte, kleur en vorm licht kunnen verschillen van de getoonde "
                          "voorbeelden.",
        },
        {
            "naam": "NATUUR",
            "slug": "natuur",
            "tekst": [
                "Deze bordenreeks is gemaakt met effectglazuren. Die effectglazuren hebben "
                "allemaal een basiskleur, en daar waar de glazuur dikker wordt aangebracht "
                "komt een tweede kleur naar boven. Alle borden worden op hoge temperatuur "
                "gebakken waardoor ze vaatwas- en microgolfovenbestendig zijn.",
            ],
            "kleuren": ["plas", "vulkaan", "zeemeermin", "zeeschilpad", "atlantis",
                        "bloesem", "rivierbodem", "rots", "strand"],
            "prijzen": [
                {"maat": "diameter 25 cm", "rijen": [("1 – 5 borden", "25 €"),
                                                      ("vanaf 6 borden", "22 €"),
                                                      ("vanaf 12 borden", "20 €")]},
                {"maat": "diameter 20 cm", "rijen": [("1 – 5 borden", "22 €"),
                                                      ("vanaf 6 borden", "20 €"),
                                                      ("vanaf 12 borden", "18 €")]},
            ],
            "beelden": [
                ("natuur-overzicht.jpg", "Overzicht van de reeks NATUUR"),
                ("natuur-gestapeld.jpg", "De NATUUR-borden gestapeld"),
                ("natuur-plas.jpg", "Bord NATUUR, plas — lichtbruin met blauw accent"),
                ("natuur-vulkaan.jpg", "Bord NATUUR, vulkaan — rood met zwarte spikkel"),
                ("natuur-zeemeermin.jpg", "Bord NATUUR, zeemeermin — lichtbruin met lichtblauw"),
                ("natuur-zeeschilpad.jpg", "Bord NATUUR, zeeschilpad — bruin met groen-grijs"),
                ("natuur-atlantis.jpg", "Bord NATUUR, atlantis — bruin met blauw accent"),
                ("natuur-bloesem.jpg", "Bord NATUUR, bloesem — bruin met roze accent"),
                ("natuur-rivierbodem.jpg", "Bord NATUUR, rivierbodem — donkerbruin met blauw accent"),
                ("natuur-rots.jpg", "Bord NATUUR, rots — donkerbruin met lichtgrijs accent"),
                ("natuur-strand.jpg", "Bord NATUUR, strand — bruin met geelbruin accent"),
            ],
            "disclaimer": "Deze borden zijn handwerk en unieke stukken. Dat wil zeggen dat "
                          "grootte, kleur en vorm licht kunnen verschillen van de getoonde "
                          "voorbeelden. Op sommige borden ontstaan spikkels (zoals op de foto "
                          "van het atlantis-bord), maar die spikkels kunnen niet gegarandeerd "
                          "worden — die hangen af van de magie die in de keramiekoven gebeurt.",
        },
    ],
    "bestellen": {
        "kop": "Wat moet je weten als je wil bestellen",
        "intro": [
            "Bij ClayWaves koop je ambachtelijk vakmanschap. Onze borden worden met liefde en "
            "zorg met de hand gemaakt, speciaal voor jou. We hebben geen voorraad liggen, "
            "omdat elk bord uniek is en aandacht verdient.",
        ],
        "punten": [
            ("Uniek en persoonlijk",
             "Elk bord vertelt een verhaal. Geen twee zijn hetzelfde. Jouw bestelling wordt "
             "met precisie en passie vervaardigd."),
            ("Kwaliteit",
             "We gebruiken alleen hoogwaardige materialen. Onze borden zijn duurzaam en gaan "
             "lang mee. Ze zijn vaatwasbestendig en je kan ze in de microgolfoven gebruiken "
             "(een heteluchtoven raden we af)."),
            ("Geduld en tijd",
             "Omdat we elk bord op bestelling maken, vragen we je rekening te houden met een "
             "levertijd van ongeveer vier maanden. Goede dingen kosten tijd, en we willen "
             "ervoor zorgen dat jouw bord perfect is."),
        ],
        "stappen_kop": "Hoe werkt het?",
        "stappen": [
            ("Bestellen", "Kies het gewenste bord uit de collectie of neem contact op voor "
                          "een gepersonaliseerd ontwerp."),
            ("Creatie", "Wouter gaat aan de slag met jouw bestelling en draait en glazuurt "
                        "alles met de hand."),
            ("Levering", "Als ze klaar zijn, spreken we af hoe de borden tot bij jou geraken."),
        ],
        "slot": "Bedankt voor je geduld en vertrouwen in ons vakmanschap. We kijken ernaar uit "
                "om iets moois voor jou te creëren. Heb je nog vragen? Neem gerust contact op.",
    },
}

# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------

CONTACT = {
    "title": "Contact — ClayWaves",
    "description": "Contacteer ClayWaves — Wouter Vandenbranden, mSENSE bv, Heusden.",
    "kop": "Neem contact op",
    "intro": "Een vraag over een workshop, een bestelling of iets anders? Stuur een bericht, "
             "of bel gerust.",
}
