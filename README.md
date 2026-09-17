# EA Learnings

Progressive Web App für die Enterprise-Architecture-Lernbibliothek im Behördenkontext.

## Funktionen

- alle 25 Projektquellen vollständig als Markdown-Module
- abgeleitete Lernmodule aus den Projektgesprächen
- Volltextsuche, Kategorien und Filter
- Favoriten, Lernstatus und Fortschritt
- persönliche Notizen
- zuletzt geöffnete Module und gespeicherte Leseposition
- optional automatische Wiederaufnahme an der letzten Leseposition
- lokales Gedächtnis ohne Server-Datenbank
- Export/Import des persönlichen Gedächtnisses als JSON
- getrennte Reset-Funktionen für Lernverlauf, Notizen/Favoriten, Offline-Cache und Vollreset
- Offline-Nutzung als PWA
- Installierbarkeit auf Desktop/Mobilgerät
- Content-Versionierung und Update-Hinweis

## Lokales Gedächtnis

Persönliche Lerndaten werden in `localStorage` gespeichert. Der PWA-Offline-Cache wird separat über die Cache Storage API verwaltet. Dadurch kann der Cache geleert werden, ohne den Lernfortschritt oder Notizen zu löschen.

Gespeichert werden:

- Fortschritt
- Favoriten
- Notizen
- zuletzt geöffnete Module
- Lesepositionen
- Lernstatus
- App-Einstellungen

Unter **Speicher & Reset** kann alles exportiert, importiert oder gezielt zurückgesetzt werden.

## Inhalte erweitern

1. Neue Markdown-Datei unter `content/modules/` oder `content/derived/` ablegen.
2. Eintrag in `content/index.json` ergänzen.
3. `python tools/rebuild_search.py` ausführen.
4. `content/version.json` und `contentVersion` in `content/index.json` hochzählen.
5. Cache-Version in `sw.js` hochzählen.

Bestehende Nutzer erhalten beim nächsten Öffnen/Fokus einen Update-Hinweis.

## GitHub Pages

Repository → **Settings → Pages → Source: GitHub Actions**.

Zielpfad: `https://empishaj.github.io/eaapp/`

## Lokale Entwicklung

```bash
python -m http.server 8080
```

Dann `http://localhost:8080` öffnen.
