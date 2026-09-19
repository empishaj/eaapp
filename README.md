# EA Mastery 5.0

Neu konzipierte Progressive Web App für Enterprise-Architecture-Lernen im deutschen Behördenkontext.

## Kernidee
Die App trennt **Akademie**, **Training** und **Wissensbasis**. Kompetenz wird nicht über gelesene Seiten, sondern über vier Evidenzarten gemessen: Lernen, Recall, Fallanwendung und professionelles Artefakt.

## Enthalten
- 16 Kompetenzdomänen
- 96 aufeinander aufbauende Lerneinheiten
- 480 Lernkarten
- 96 Behördenfälle
- 316 Lexikonbegriffe
- 160 Fachbuch-Einträge
- 37 vollständige Projektquellen
- Spaced Repetition
- Artefakt-Lab
- lokaler Lernstand über IndexedDB
- Backup/Import/Reset
- Offline-PWA

## Start auf GitHub Pages
Repository-Inhalt in den Branch `main` übernehmen und GitHub Pages auf **GitHub Actions** stellen. Der Workflow `.github/workflows/pages.yml` veröffentlicht die statische App.

## Content erweitern
Die UI enthält keine themenspezifische Logik. Neue Inhalte werden in den JSON-Dateien unter `content/` und als Markdown-Quellen ergänzt. Danach ausführen:

```bash
python tools/validate_content.py
```

## Architektur
Siehe `APP_CONCEPT.md`.

## Vektordiagramme (5.1.0)

EA Mastery nutzt Mermaid 12.0.0, um Lernzusammenhänge im Browser als SVG zu rendern. Die Definitionen sind vom UI getrennt und liegen unter `content/visuals/diagrams.json`.

Aktuell enthält die App:
- 32 Kursdiagramme (mentales Modell + EA-Systembild je Kompetenzfeld)
- 192 Lesson-Diagramme (mentales Modell + Querverbindungen je Lerneinheit)
- Vollbild-/Zoomansicht
- SVG-Export

Neue Diagramme können durch einen zusätzlichen Datensatz in `diagrams.json` ergänzt werden. Die UI muss dafür nicht verändert werden.

## Artefakt-Lab (5.2.0)
EA Mastery enthält 48 ausgefüllte Muster-Arbeitsergebnisse. Für jedes der 16 Kompetenzfelder gibt es ein Arbeitsartefakt, eine Entscheidungsvorlage und ein Master-Arbeitsergebnis. Muster dienen als Referenz; über „Struktur übernehmen“ wird ein leeres eigenes Arbeitsgerüst erzeugt, das separat im lokalen Lernspeicher fortgeschrieben wird.

## BSI Master Academy (5.5.0)
Die App enthält zusätzlich eine eigenständige BSI-IT-Grundschutz-Akademie mit 950 ausführlichen Lernkarten, 15 Modulen, 83 Kernthemen, getrenntem SRS-Fortschritt und Prüfungssimulator. Die BSI-Daten liegen unter `content/bsi/` und werden unabhängig vom EA-Kartenmodell geladen.

### Kartengedächtnis (5.5.0)
Jede BSI- und EA-Lernkarte speichert lokal Sichtung, vollständiges Lesen, Bewertungen, Bewertungshistorie und SRS-Wiederholungsdaten. Lern- und Review-Sessions werden zufällig gemischt; kürzlich gezeigte Karten werden nach Möglichkeit nicht zuerst erneut präsentiert.

### Responsive Fachinhalte ab 5.6.0
Projektquellen und Markdown-Inhalte werden über die responsive Content Engine gerendert. Tabellen erscheinen auf Desktop als echte Tabellen und auf Smartphones als beschriftete Karten. Lange Texte nutzen optimierte Lesebreite, Abstände und Abschnittshierarchie.
