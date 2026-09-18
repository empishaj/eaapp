# EA Learnings 2.2.0

Smartphone-first Progressive Web App für Enterprise Architecture im Behördenkontext.

## Schwerpunkte

- 37 Lernmodule aus dem Projekt
- 43 Start-Lernkarten mit Spaced Repetition
- Microlearning, EA-Falltraining und Kompetenzprofil
- vollständig lokale Lerndaten in IndexedDB
- Offline-PWA ohne Server-Datenbank
- **EA-Lexikon mit 74 Begriffen und 218 kontextuellen Textbeispielen**
- automatische Begriffsverlinkung in Lerntexten
- Rücksprung vom Lexikon zur ursprünglichen Leseposition
- Begriffserklärungen direkt am Ende jedes Lerntextes
- Suche über Module, Lexikon, Lernkarten und eigene Notizen

## Lexikonprinzip

Ein Begriff wird nicht isoliert erklärt. Jeder Eintrag besteht aus:

1. kompakter Definition,
2. mehreren Beispielen aus unterschiedlichen Projekttexten,
3. Direktlinks zu den jeweiligen Textstellen,
4. Rücknavigation zum aufrufenden Lerntext.

Die Begriffe werden beim Rendern automatisch erkannt. Um die Lesbarkeit auf Smartphones zu erhalten, wird ein Begriff innerhalb eines Abschnitts nur beim ersten Auftreten verlinkt. Am Ende des Lerntextes werden die dort vorkommenden Lexikonbegriffe zusätzlich kompakt erklärt.

## Inhalte erweitern

Lerninhalte liegen unter `content/modules/` und `content/derived/`. Der Katalog befindet sich in `content/index.json`.

Das Lexikon liegt in `content/lexicon.json`. Die Quellexemplare werden mit `tools/rebuild_lexicon.py` aus den vorhandenen Modulen neu ermittelt.

```bash
python tools/rebuild_lexicon.py
python tools/rebuild_search.py
```

Danach `content/version.json` erhöhen und deployen.

## GitHub Pages

Der mitgelieferte Workflow unter `.github/workflows/pages.yml` veröffentlicht die statische PWA aus dem Repository-Root.

## Curriculum 2.2
- 28 quellengebundene Lerneinheiten
- 155 aktive Lernkarten
- Transferfälle und Praxis-Reviewfragen
- Quellenbezug pro Einheit
- Behörden-Capstone
