# Content-Modell – EA Learnings 3.0

Die App trennt drei Ebenen strikt voneinander.

## 1. Referenzbibliothek

`content/index.json` registriert die Projektmodule. Die ursprünglichen Projekttexte liegen unter `content/modules/`. Frühere abgeleitete Projektartefakte liegen unter `content/derived/` und dienen weiterhin als Referenzmaterial.

## 2. Professoren-Curriculum

`content/units.json` enthält 64 neu geschriebene Lerneinheiten. Jede Einheit enthält unter anderem:

- Kompetenzfeld und Track
- Quellenbasis / Kennzeichnung fachlicher Erweiterung
- Lernziele
- Kernidee und Why-it-matters
- mentales Modell
- Professoren-Erklärung
- explizite Querverbindungen
- Abgrenzungen
- typische Fehlannahmen und Korrekturen
- Beispiele
- sokratische Fragen
- Behörden-Transferfall
- Profi-Liefergegenstand
- Lernchecks
- Reviewfragen
- vier Beherrschungsstufen
- sechs verwandte Lerneinheiten

## 3. Lernengine

`content/learning.json` enthält:

- `cards` – 256 Lern-, Verbindungs-, Szenario- und Delivery-Karten
- `curriculumPaths` – 10 geführte Pfade über die Professoren-Einheiten
- `paths` – Referenzpfade durch die bestehende Projektbibliothek
- `competencies` – Kompetenzfelder für das Profil
- `sessionMinutes` – Microlearning-Zeiten

## Lexikon

`content/lexicon.json` enthält 316 Begriffe. Beispiele können aus Originalmodulen oder aus Professoren-Einheiten stammen. Die UI kennzeichnet den Kontext und verlinkt in beide Richtungen.

## Quellenprinzip

Projektquellen werden nicht stillschweigend korrigiert oder ersetzt. Fachliche Synthese und Erweiterungen werden in `basis` und `sourceNote` der jeweiligen Einheit kenntlich gemacht.

## Pflege

Bei Inhaltsänderungen:

```bash
python tools/validate_professor_curriculum.py
python tools/rebuild_search.py
```

Danach Versionsnummer in `content/version.json`, `content/index.json` und Service-Worker-Cache konsistent halten.
