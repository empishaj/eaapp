# Content-Modell

Die App trennt Lerninhalte von der UI.

## Module

`content/index.json` registriert alle Module. Die eigentlichen Texte liegen unter:

- `content/modules/` – vollständige Projektquellen
- `content/derived/` – aus Projektgesprächen abgeleitete Lerninhalte

## Lernengine

`content/learning.json` enthält:

- `cards` – Retrieval-, Definitions-, Unterschieds- und Szenariokarten
- `paths` – geführte Lernpfade
- `competencies` – Kompetenzbereiche für das Profil
- `sessionMinutes` – angebotene Microlearning-Zeiten

Neue Karten lassen sich ohne Codeänderung ergänzen. Jede Karte referenziert ein vorhandenes `module` über dessen ID.

## Suche

`content/search-index.json` wird mit `python tools/rebuild_search.py` aus den registrierten Markdown-Modulen erzeugt. Lernkarten und persönliche Notizen werden zur Laufzeit zusätzlich durchsucht.

## Versionen

Bei Content-Änderungen `contentVersion` in `content/index.json` und `version` in `content/version.json` erhöhen. Für App-/Cache-Änderungen auch den Cache-Namen in `sw.js` erhöhen.

## Lexikon

`lexicon.json` enthält das zentrale Begriffssystem der App. Jeder Eintrag hat:

- `term` und optionale `aliases`
- eine verdichtete `definition`
- mehrere `examples` aus unterschiedlichen Lernmodulen
- Modul-ID, Abschnitt und Anchor für den Rücksprung in den Ursprungstext

`tools/rebuild_lexicon.py` ermittelt die Beispiele neu aus den vorhandenen Projektmodulen. Definitionen bleiben kuratiert; Beispiele bleiben quellengebunden.
