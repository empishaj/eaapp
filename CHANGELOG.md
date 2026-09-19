## 5.5.0
- Alle 1.430 Lernkarten (950 BSI + 480 EA) besitzen ein persistentes Kartengedächtnis.
- Getrennte Zustände für erstmals/zuletzt gesehen, vollständig gelesen und bewertet.
- Anzahl der Aufrufe, Lesevorgänge und Bewertungen wird je Karte gespeichert.
- Bewertungshistorie mit Zeitstempel sowie bestehende SRS-Daten bleiben sichtbar.
- Alte 5.3/5.4-Bewertungen werden automatisch in das neue Gedächtnismodell migriert.
- BSI- und EA-Lern-/Review-Sessions werden bei jedem Start zufällig gemischt.
- Neue Karten werden zufällig aus dem gesamten verfügbaren Pool gewählt statt aus einer festen Dateireihenfolge.
- Kürzlich gezeigte Karten werden nach Möglichkeit nach hinten gestellt.
- Themenkatalog zeigt pro Karte Neu / gesehen / gelesen / bewertet.

## 5.4.0
- BSI Master Academy auf 950 Lernkarten erweitert.
- 15 Module, 83 Kernthemen und 83 Prüfungskarten.
- Neue Vertiefungen: Recht/Compliance, BSI-Rolle Bund, KRITIS/NIS2-Kontext, ISO 27001/27002/31000/22301, Grundschutz-Profile, Mindeststandards/TR, Audit/Zertifizierung, BCM 200-4 Deep Dive, Awareness, Lieferanten/Cloud/OT, Bundesbehörden-Security-Architecture, Vergabe/Abnahme und Security-Metriken.

# Changelog

## 5.0.0 – 2026-09-19
- vollständige Neuentwicklung der Informations- und Lernarchitektur
- neue Hauptnavigation: Heute, Akademie, Trainieren, Wissen, Profil
- getrennte Content-, Learning-, Memory- und UI-Schichten
- Mastery Engine mit vier Evidenzarten
- Spaced-Repetition-Engine neu gekapselt
- 16 Kompetenzdomänen mit je sechs Lernstufen
- 96 Behördenfälle als eigener Trainingsmodus
- Artefakt-Lab für professionelle Lieferfähigkeit
- erste Startdiagnostik
- Local-first-Lernakte mit Migration aus älteren App-Versionen
- neue Content-Katalogisierung
- Lexikon mit hochwertigen Projektdefinitionen für zentrale Begriffe und Curriculum-Kontexten
- responsive Smartphone-first UI mit 5-Punkt-Bottom-Navigation

## 5.1.0 – 2026-09-19
- Mermaid 12.0.0 als SVG-Diagramm-Engine integriert.
- 224 datengetriebene Vektordiagramme: Kurs-Systembilder, mentale Modelle und Querverbindungsgraphen.
- Diagramme werden direkt in den Lernschritten „Erklären“ und „Verbinden“ angezeigt.
- Vollbildansicht, Zoom und SVG-Export ergänzt.
- Diagrammdefinitionen liegen getrennt unter `content/visuals/diagrams.json` und sind ohne UI-Code erweiterbar.
- Service Worker cached Mermaid-CDN-Ressourcen nach der ersten Nutzung für spätere Offline-Verwendung.

## 5.2.0 – 2026-09-19
- 48 ausgefüllte EA-Muster-Arbeitsergebnisse integriert
- je Kompetenzfeld: Arbeitsartefakt, Decision Brief und Master-Paket
- Muster enthalten Zweck, Adressaten, Behördenfall, ausgefüllte Inhalte, Qualitätskriterien und Anti-Patterns
- Artefakt-Lab vollständig neu strukturiert
- „Struktur übernehmen“ erzeugt ein eigenes Arbeitsgerüst ohne Musterinhalt zu kopieren
- Artefakte in globaler Suche und Offline-Paket integriert

## 5.3.0 – BSI Master Academy
- 500 ausführliche BSI-IT-Grundschutz-Lernkarten integriert.
- 9 Module und 53 Kernthemen als eigenes Curriculum.
- Eigenständiger BSI-Lernstand und Spaced-Repetition-Status.
- BSI Review mit fälligen Wiederholungen plus kontrollierter Neu-Karten-Zufuhr.
- Prüfungssimulator mit 50 zufällig ausgewählten Prüfungskarten und 60-Minuten-Timer.
- Fehleranalyse nach Prüfung mit direkter Verlinkung in die Lernkarten.
- BSI-Inhalte in globale Suche, Dashboard, Training, Profil, Backup und Offline-Paket integriert.

## 5.6.0 – Responsive Content Engine
- Markdown-Tabellen werden als semantische HTML-Tabellen gerendert.
- Desktop: kompakte, scanbare Tabellen mit Sticky Header und sauberer Typografie.
- Smartphone: jede Tabellenzeile wird automatisch als beschriftete Datenkarte dargestellt.
- Neue Lesebreite, Abschnittsrhythmik, Callouts, Codeblöcke und Listenformatierung für lange Fachquellen.
- Wissensquellen erhalten einen dedizierten Reading-Shell statt unstrukturierter Rohdarstellung.
- Keine fachlichen Inhalte verändert; nur Rendering und Layout.
