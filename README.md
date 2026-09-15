# claywaves.be

Statische site voor ClayWaves (Anja en Wouter). Eigen HTML/CSS/JS, geen
one.com-builder, geen frameworks, geen database.

## Hoe het werkt

Alle teksten, prijzen, kleuren en workshopdata staan in **één bestand**:
`content/content.py`. Het script `generate.py` zet dat om in de HTML-pagina's.

```
content/content.py   ← hier pas je alles aan
generate.py          ← bouwt de pagina's
assets/style.css     ← vormgeving
assets/script.js     ← mobiel menu + vergroten van foto's
images/              ← alle foto's
```

## Iets aanpassen

1. Pas `content/content.py` aan (tekst, prijs, agenda …).
2. Draai `python generate.py`.
3. Commit en push. Netlify zet de nieuwe versie automatisch live.

De gegenereerde HTML-bestanden staan mee in de repo — Netlify hoeft niets te
bouwen, en dus kan er ook niets misgaan in een build.

## Foto's

De foto's van de oude site haal je één keer binnen met:

```
python scripts/download_images.py
```

Dat werkt zolang de oude one.com-site nog online staat. Heb je zelf betere
originelen, zet die dan over de gedownloade bestanden heen — de bestandsnamen
in `images/` zijn wat telt.

## Workshopagenda

`AGENDA` in `content/content.py` is een lijst. Staat er niets in, dan toont de
workshoppagina automatisch een nette melding met een link naar contact in
plaats van een lege agenda. Een regel ziet er zo uit:

```python
AGENDA = [
    {"datum": "30 mei 2027", "titel": "Raku en Saggar",
     "locatie": "Clay Days — Muizen, Mechelen"},
]
```

## Contactformulier

Het formulier op `contact.html` gebruikt **Netlify Forms**: geen server, geen
databank. Netlify herkent het formulier bij de eerste deploy en verzamelt de
berichten onder *Forms* in het Netlify-dashboard. Zet daar een e-mailnotificatie
aan naar `wouter@claywaves.be`, anders blijven de berichten in het dashboard
staan. Het gratis niveau geeft 100 inzendingen per maand.

## Bezoekersstatistieken

`SITE["goatcounter"]` in `content/content.py` is leeg. Vul daar je
GoatCounter-sitecode in (hetzelfde principe als op woutervandenbranden.be) en
draai `generate.py` opnieuw — dan komt het telscript op elke pagina. Leeg
laten betekent: geen tracking, geen cookiebanner nodig.

## Publiceren

- GitHub-repo: `claywaves-be`
- Netlify: nieuwe site in het bestaande team, gekoppeld aan deze repo
- Domein: `claywaves.be` en `www.claywaves.be` naar Netlify verwijzen
- one.com: enkel domein + e-mail behouden, hosting/Website Builder afzetten
