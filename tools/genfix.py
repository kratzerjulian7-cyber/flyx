# Erzeugt fix/index.html und en/fix/index.html (Stand Flyx Fix 1.0).
# Screenshots: img/fix/01.jpg..08.jpg (1320x2868 oder 1284x2778) ablegen und neu laufen lassen; Abschnitt "Einblicke" erscheint dann automatisch.
import os, html, sys
ROOT = sys.argv[1]
BASE = "https://kratzerjulian7-cyber.github.io/flyx/"
shots = sorted(f for f in os.listdir(os.path.join(ROOT, "img/fix")) if f.endswith(".jpg")) if os.path.isdir(os.path.join(ROOT, "img/fix")) else []

T = {
"de": dict(
  path="fix/", other="en/fix/", css="../style.css", img="../img/fix/", icon="../img/fix-icon/", home="../", privacy="../fix-datenschutz.html", lang="EN", other_rel="../en/fix/", lang_code="en",
  title="Flyx Fix – Messen, ausschreiben, Angebote vergleichen",
  desc="Flyx Fix: Räume vermessen, Projekte durchrechnen, Aufträge an Betriebe ausschreiben und Angebote Posten für Posten vergleichen. Keine Zahlungen in der App, keine Werbung, kein Tracking.",
  nav=[("#werkzeuge","Werkzeuge"),("#ausschreiben","Aufträge"),("#betriebe","Für Betriebe"),("#faq","Fragen"),("#support","Support")], navpriv="Datenschutz",
  eyebrow="Für Haus und Wohnung",
  h1="Messen, ausschreiben, vergleichen.",
  lead="Flyx Fix verbindet deine Werkzeuge für Haus und Wohnung mit einem geführten Angebots- und Rechnungssystem. Raum vermessen, Auftrag direkt aus dem Werkzeug ausschreiben, Angebote Posten für Posten vergleichen.",
  soon="Bald im App Store", more="Alle Funktionen",
  facts=["Kostenlos","Kein eigenes Konto","Ende-zu-Ende verschlüsselt","Keine Zahlungen in der App","Keine Werbung, kein Tracking"],
  shots_eyebrow="Einblicke", shots_h="So sieht Flyx Fix aus",
  sections=[
    ("werkzeuge","Werkzeuge","Erst messen, dann ausschreiben","Drei Reiter: Werkzeuge, Mein Zuhause und Aufträge. Die App startet bei den Werkzeugen, und aus jedem Werkzeug schreibst du direkt einen Auftrag aus, die Angaben sind schon vorausgefüllt.",
      [("Raummaß","Räume mit LiDAR scannen, Flächen mit Abzug für Fenster und Türen, Aufmaß als PDF oder CSV."),
       ("Rechner","Umzug, Solar und Maler. Sie rechnen Mengen, Dauer und Leistung, keine Preise."),
       ("Zählerstände","Strom, Gas und Wasser im Blick."),
       ("Nebenkosten-Prüfer","Die Abrechnung Posten für Posten durchgehen."),
       ("Mängel- und Übergabeprotokoll","Mit Fotos, Datum und Lärmmessung."),
       ("Hausrat-Inventar","Für Umzug, Versicherung und Entrümpelung.")]),
    ("ausschreiben","Für Auftraggeber","Angebote, die du wirklich vergleichen kannst","Schreib deinen Auftrag aus, Betriebe antworten mit einem Angebot. Du vergleichst Posten für Posten, stellst Rückfragen und beauftragst über „Kostenpflichtig beauftragen“.",
      [("14 Kategorien","Entrümpelung, Umzug, Reinigung, Renovierung, Maler/Boden, Bad/Küche, Fenster/Türen, Dach/Fassade, Elektrik/Sanitär, PV/Wärmepumpe/Wallbox, Garten, Fahrzeug, Netzwerk/Smart Home, Montage."),
       ("Kostenschätzung","Eine erste Einschätzung des Betriebs."),
       ("Unverbindliches Angebot","Ein konkretes Angebot zum Vergleichen."),
       ("Verbindliches Angebot","Gilt bis zu einem Datum, das der Betrieb festlegt."),
       ("Vergleich Posten für Posten","Gleiche Leistungen nebeneinander, offene Fragen auf einen Blick."),
       ("Ehrliche Preisspannen","Regionale Spannen erst ab 5 echten, anonymen Angeboten, mit Anzahl und Datenstand. Sonst steht da: „Noch keine verlässliche Preisspanne“.")]),
    ("auftrag","Nach der Beauftragung","Alles bis zur Rechnung an einem Ort","Vom Auftrag bis zur Abnahme bleibt alles nachvollziehbar.",
      [("Nachträge","Änderungen werden als neue Version festgehalten."),
       ("Abnahme","Mit Fotos dokumentiert."),
       ("Rechnung","Der Betrieb stellt sie in eigenem Namen als PDF aus."),
       ("Rechnungsprüfung","Formal auf die Pflichtangaben nach § 14 UStG, keine Steuerberatung."),
       ("Verschlüsselt","Angebote, Kontaktdaten und Projektverlauf sind Ende-zu-Ende verschlüsselt."),
       ("Kontaktdaten erst nach Beauftragung","Vorher sehen Betriebe nur den PLZ-Bereich und den Auftragsinhalt.")]),
    ("betriebe","Für Betriebe","Firmenprofil einmal anlegen","Aus deinem Firmenprofil füllt Flyx Fix jedes Angebot automatisch. Du entscheidest, ob du schätzt, unverbindlich oder verbindlich anbietest.",
      [("Angebote schneller","Firmendaten sind schon drin, du ergänzt nur die Posten."),
       ("Nachträge und Abnahme","Versioniert und mit Fotos, für beide Seiten nachvollziehbar."),
       ("Rechnung als PDF","In deinem Namen, direkt aus dem Auftrag.")]),
  ],
  promise=[("Keine Zahlungen","Keine Gebühren und keine Zahlungsdaten in der App."),("Kein eigenes Konto","Alles läuft über dein iCloud, ohne Passwort."),("Keine Werbung, kein Tracking","Deine Werkzeug-Daten bleiben auf deinem iPhone.")],
  hint="Flyx Fix ist eine technische Plattform. Auftraggeber ist der Kunde, Auftragnehmer der Betrieb; Verträge kommen direkt zwischen beiden zustande, Flyx Fix ist keine Vertragspartei. Rechner und Prüfer liefern Richtwerte und ersetzen keine Fach-, Rechts- oder Steuerberatung.",
  faq_h="Häufige Fragen",
  faq=[("Was kostet Flyx Fix?","Nichts. In der App wird nichts bezahlt und es gibt keine Gebühren. Den Auftrag bezahlst du direkt beim Betrieb."),
       ("Brauche ich ein Konto?","Nein. Flyx Fix nutzt dein iCloud, es gibt kein eigenes Konto und kein Passwort."),
       ("Wer ist mein Vertragspartner?","Der Betrieb, den du beauftragst. Flyx Fix stellt nur die Plattform bereit und ist keine Vertragspartei."),
       ("Welche Angebotsarten gibt es?","Kostenschätzung, unverbindliches Angebot und verbindliches Angebot bis zu einem Datum."),
       ("Wo liegen meine Daten?","Werkzeug-Daten auf deinem iPhone. Aufträge, Angebote und Rechnungen in Apples iCloud (CloudKit); Angebote, Kontaktdaten und Projektverlauf sind Ende-zu-Ende verschlüsselt. Details stehen im Datenschutz."),
       ("Was sehen Betriebe vor der Beauftragung?","Nur den PLZ-Bereich und den Inhalt deines Auftrags. Deine Kontaktdaten bleiben verborgen, bis du einen Betrieb beauftragst."),
       ("Zeigen die Rechner Preise?","Nein. Sie rechnen Mengen, Dauer und Leistung. Regionale Preisspannen gibt es erst ab 5 echten, anonymen Angeboten."),
       ("Kann ich meine Daten löschen?","Ja, in der App."),
       ("Brauche ich ein iPhone mit LiDAR?","Für den Raumscan ja. Alle anderen Werkzeuge laufen auf jedem iPhone."),
       ("In welcher Sprache gibt es die App?","Im Moment auf Deutsch."),
       ("Gibt es Flyx Fix für Android?","Im Moment nur fürs iPhone.")],
  sup_h="Fragen, Fehler, Wünsche?", sup_p="Schreib mir einfach eine E-Mail, ich antworte persönlich.",
  foot_other="English", foot_home="Flyx Map",
),
"en": dict(
  path="en/fix/", other="fix/", css="../../style.css", img="../../img/fix/", icon="../../img/fix-icon/", home="../", privacy="../fix-privacy.html", lang="DE", other_rel="../../fix/", lang_code="de",
  title="Flyx Fix – Measure, request, compare quotes",
  desc="Flyx Fix: measure rooms, run the numbers, send job requests to local businesses and compare quotes line by line. No payments in the app, no ads, no tracking.",
  nav=[("#tools","Tools"),("#request","Jobs"),("#businesses","For businesses"),("#faq","FAQ"),("#support","Support")], navpriv="Privacy",
  eyebrow="For your home and apartment",
  h1="Measure, request, compare.",
  lead="Flyx Fix connects your home tools with a guided quote and invoice system. Measure a room, create a job request straight from the tool, compare quotes line by line.",
  soon="Coming soon to the App Store", more="All features",
  facts=["Free","No separate account","End-to-end encrypted","No payments in the app","No ads, no tracking"],
  shots_eyebrow="A closer look", shots_h="What Flyx Fix looks like",
  sections=[
    ("tools","Tools","Measure first, then request","Three tabs: Tools, My Home and Jobs. The app opens in the tools, and from any tool you can create a job request right away, with the details already filled in.",
      [("Room measure","Scan rooms with LiDAR, areas minus windows and doors, export as PDF or CSV."),
       ("Calculators","Moving, solar and painting. They calculate quantities, duration and output, not prices."),
       ("Meter readings","Electricity, gas and water at a glance."),
       ("Utility bill checker","Go through your bill line by line."),
       ("Defect and handover report","With photos, date and noise measurement."),
       ("Home inventory","For moving, insurance and decluttering.")]),
    ("request","For clients","Quotes you can actually compare","Post your job, businesses reply with a quote. Compare line by line, ask questions and hire through “Kostenpflichtig beauftragen” (order with obligation to pay).",
      [("14 categories","Decluttering, moving, cleaning, renovation, painting/flooring, bathroom/kitchen, windows/doors, roof/facade, electrical/plumbing, solar/heat pump/wallbox, garden, vehicle, network/smart home, assembly."),
       ("Cost estimate","A first estimate from the business."),
       ("Non-binding quote","A concrete quote to compare."),
       ("Binding quote","Valid until a date set by the business."),
       ("Line-by-line comparison","Same services side by side, open questions at a glance."),
       ("Honest price ranges","Regional ranges only from 5 real, anonymous quotes, with count and data date. Otherwise it says there is no reliable price range yet.")]),
    ("job","After hiring","Everything up to the invoice in one place","From order to sign-off, everything stays traceable.",
      [("Change orders","Changes are kept as new versions."),
       ("Sign-off","Documented with photos."),
       ("Invoice","Issued by the business in its own name as a PDF."),
       ("Invoice check","A formal check of the mandatory details (Section 14 German VAT Act), not tax advice."),
       ("Encrypted","Quotes, contact details and project history are end-to-end encrypted."),
       ("Contact details only after hiring","Before that, businesses only see the postal code area and the job content.")]),
    ("businesses","For businesses","Set up your business profile once","Flyx Fix fills every quote from your business profile. You choose whether to send an estimate, a non-binding or a binding quote.",
      [("Faster quotes","Your business details are already in, you only add the line items."),
       ("Change orders and sign-off","Versioned and with photos, traceable for both sides."),
       ("Invoice as PDF","In your name, straight from the job.")]),
  ],
  promise=[("No payments","No fees and no payment data in the app."),("No separate account","Everything runs through your iCloud, no password."),("No ads, no tracking","Your tool data stays on your iPhone.")],
  hint="Flyx Fix is a technical platform. The client is the customer, the contractor is the business; contracts are made directly between them, Flyx Fix is not a party to the contract. Calculators and checkers give estimates and do not replace professional, legal or tax advice.",
  faq_h="Frequently asked questions",
  faq=[("How much does Flyx Fix cost?","Nothing. Nothing is paid in the app and there are no fees. You pay the business directly for the job."),
       ("Do I need an account?","No. Flyx Fix uses your iCloud, there is no separate account and no password."),
       ("Who is my contract partner?","The business you hire. Flyx Fix only provides the platform and is not a party to the contract."),
       ("Which types of quotes are there?","Cost estimate, non-binding quote and binding quote valid until a set date."),
       ("Where is my data stored?","Tool data on your iPhone. Jobs, quotes and invoices in Apple's iCloud (CloudKit); quotes, contact details and project history are end-to-end encrypted. See the privacy policy for details."),
       ("What do businesses see before I hire them?","Only the postal code area and the content of your job. Your contact details stay hidden until you hire a business."),
       ("Do the calculators show prices?","No. They calculate quantities, duration and output. Regional price ranges only appear once there are 5 real, anonymous quotes."),
       ("Can I delete my data?","Yes, in the app."),
       ("Do I need an iPhone with LiDAR?","For the room scan, yes. All other tools work on any iPhone."),
       ("Which languages are available?","The app is currently available in German only."),
       ("Is Flyx Fix available for Android?","Currently iPhone only.")],
  sup_h="Questions, bugs, ideas?", sup_p="Just send me an email, I reply personally.",
  foot_other="Deutsch", foot_home="Flyx Map",
)}
e = html.escape
for code, t in T.items():
    shots_html = ""
    if shots:
        imgs = "".join(f'<div class="phone flat"><img src="{t["img"]}{s}" alt="Flyx Fix Screenshot {i+1}" loading="lazy" width="660" height="1434"></div>' for i, s in enumerate(shots))
        shots_html = f'''
  <section class="block" id="einblicke">
    <div class="wrap">
      <div class="sec-head"><p class="eyebrow">{e(t["shots_eyebrow"])}</p><h2>{e(t["shots_h"])}</h2></div>
      <div class="fix-shots">{imgs}</div>
    </div>
  </section>'''
    secs = ""
    for sid, tag, h, p, cards in t["sections"]:
        cs = "".join(f'<div class="card"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in cards)
        secs += f'''
  <section class="block" id="{sid}">
    <div class="wrap">
      <div class="sec-head"><p class="eyebrow">{e(tag)}</p><h2>{e(h)}</h2><p>{e(p)}</p></div>
      <div class="grid">{cs}</div>
    </div>
  </section>'''
    nav = "".join(f'<a href="{a}">{e(b)}</a>' for a, b in t["nav"]) + f'<a href="{t["privacy"]}">{e(t["navpriv"])}</a>'
    facts = "".join(f"<span>{e(f)}</span>" for f in t["facts"])
    promise = "".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in t["promise"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in t["faq"])
    first = t["sections"][0][0]
    doc = f'''<!doctype html>
<html lang="{code}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["desc"])}">
<meta name="theme-color" content="#1c1c1e">
<meta property="og:title" content="{e(t["title"])}">
<meta property="og:description" content="{e(t["desc"])}">
<meta property="og:url" content="{BASE}{t["path"]}">
<link rel="canonical" href="{BASE}{t["path"]}">
<link rel="alternate" hreflang="{t["lang_code"]}" href="{BASE}{t["other"]}">
<meta property="og:image" content="{BASE}img/fix-icon/icon-512.jpg">
<link rel="apple-touch-icon" href="{t["icon"]}icon-180.jpg">
<link rel="icon" href="{t["icon"]}icon-64.jpg">
<link rel="stylesheet" href="{t["css"]}">
</head>
<body>
<header class="top">
  <div class="wrap">
    <a class="brand" href="./"><img class="brand-icon" src="{t["icon"]}icon-64.jpg" alt="" width="28" height="28">Flyx <span>Fix</span></a>
    <nav class="main">{nav}</nav>
    <a class="lang" href="{t["other_rel"]}" hreflang="{t["lang_code"]}">{t["lang"]}</a>
  </div>
</header>

<main>
  <section class="hero solo">
    <div class="wrap">
      <div>
        <img class="app-icon" src="{t["icon"]}icon-256.jpg" alt="Flyx Fix App-Icon" width="112" height="112">
        <p class="eyebrow">{e(t["eyebrow"])}</p>
        <h1>{e(t["h1"])}</h1>
        <p class="lead">{e(t["lead"])}</p>
        <div class="actions"><span class="btn soon">{e(t["soon"])}</span><a class="btn ghost" href="#{first}">{e(t["more"])}</a></div>
        <div class="facts">{facts}</div>
      </div>
    </div>
  </section>
{shots_html}{secs}

  <section class="block">
    <div class="wrap">
      <div class="promise">{promise}</div>
      <p class="note">{e(t["hint"])}</p>
    </div>
  </section>

  <section class="block" id="faq">
    <div class="wrap">
      <div class="sec-head"><p class="eyebrow">FAQ</p><h2>{e(t["faq_h"])}</h2></div>
      <div class="faq">{faq}</div>
    </div>
  </section>

  <section class="block" id="support">
    <div class="wrap">
      <div class="sec-head"><p class="eyebrow">Support</p><h2>{e(t["sup_h"])}</h2></div>
      <div class="support-box">
        <p>{e(t["sup_p"])}</p>
        <p><a class="mail" href="mailto:julian_kratzer@web.de">julian_kratzer@web.de</a></p>
      </div>
    </div>
  </section>
</main>
<footer>
  <div class="wrap">
    <span>© 2026 Julian Kratzer</span>
    <a href="{t["privacy"]}">{e(t["navpriv"])}</a>
    <a href="#support">Support</a>
    <a href="{t["home"]}">{e(t["foot_home"])}</a>
    <a class="other" href="{t["other_rel"]}" hreflang="{t["lang_code"]}">{e(t["foot_other"])}</a>
  </div>
</footer>
</body>
</html>
'''
    os.makedirs(os.path.join(ROOT, t["path"]), exist_ok=True)
    open(os.path.join(ROOT, t["path"], "index.html"), "w").write(doc)
print("ok, shots:", len(shots))
