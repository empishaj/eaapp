# EA Learnings 2.0

Smartphone-first Progressive Web App für Enterprise Architecture im Behördenkontext.

## Lernkonzept

- **Heute**: persönlicher Tagesplan aus fälligen Wiederholungen, Weiterlernen und EA des Tages
- **Spaced Repetition**: lokale Wiederholungsplanung je Lernkarte
- **Retrieval Practice**: Antwort erst selbst abrufen, danach aufdecken und Sicherheit bewerten
- **Microlearning**: 3-, 5-, 10- und 20-Minuten-Sessions
- **Falltraining**: EA-Szenarien mit Musterlösung und Selbsteinschätzung
- **Lernpfade**: EA Grundlagen, Integration, Production Architecture, Behörden-EA, technische Vertiefung
- **Kompetenzprofil**: nachgewiesener Abrufstand nach Themengebiet
- **Reader 2.0**: Fokusmodus, Leseposition, Notizen, Modul-Quiz, mobile Inhaltsübersicht

## Smartphone UX

- Bottom Navigation: Heute · Lernen · Wissen · Ich
- Suche jederzeit über die Topbar
- mindestens 48 px Touch-Ziele
- Safe Areas für iPhone/Android
- Dark Mode / Systemmodus
- skalierbare Textgröße
- `prefers-reduced-motion`
- responsive Reader und Tabellen
- installierbar und offline nutzbar

## Lokales Gedächtnis

Es gibt **keine Server-Datenbank**. Persönliche Daten werden in IndexedDB des Browsers gespeichert:

- Karten- und Wiederholungsstatus
- Lernhistorie
- Lesefortschritt / Leseposition
- Favoriten
- Notizen
- Einstellungen

App- und Content-Dateien liegen separat im Cache Storage. Cache und Lerndaten können getrennt zurückgesetzt werden. Backup/Restore erfolgt als JSON-Datei.

## Inhalte

- alle 25 Projektquellen vollständig
- abgeleitete EA-Lernmodule aus dem Projekt
- 43 initiale Retrieval-/Szenario-Karten
- 5 geführte Lernpfade

Neue Markdown-Module werden unter `content/modules/` oder `content/derived/` ergänzt und in `content/index.json` registriert. Lernkarten und Lernpfade liegen unabhängig davon in `content/learning.json`.

## GitHub Pages

Der Workflow `.github/workflows/pages.yml` publiziert das Repository als statische GitHub-Pages-App. Für das Repository `empishaj/eaapp` ist die erwartete URL:

`https://empishaj.github.io/eaapp/`
