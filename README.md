# EA Learnings

Progressive Web App für die Enterprise-Architecture-Lernbibliothek im Behördenkontext.

## Funktionen

- 25 Projektmodule als Markdown-Inhalte
- abgeleitete Lernmodule aus dem Projekt-Chat
- Volltextsuche
- Kategorien und Filter
- Favoriten
- lokaler Lernfortschritt
- persönliche Notizen
- Offline-Nutzung als PWA
- Installierbarkeit auf Desktop/Mobilgerät
- Content-Versionierung und Update-Hinweis

## Inhalte erweitern

1. Neue Markdown-Datei unter `content/modules/` oder `content/derived/` ablegen.
2. Eintrag in `content/index.json` ergänzen.
3. Suchtext in `content/search-index.json` ergänzen.
4. `content/version.json` hochzählen, z. B. von `1.0.0` auf `1.1.0`.
5. Cache-Version in `sw.js` ebenfalls hochzählen.

Bestehende Nutzer erhalten beim nächsten Öffnen/Fokus einen Hinweis, dass eine neue Inhaltsversion verfügbar ist.

## GitHub Pages

Das Repository enthält einen GitHub-Actions-Workflow für GitHub Pages. Falls Pages noch nicht aktiviert ist: Repository → **Settings → Pages → Source: GitHub Actions**.

Die App ist für den Repository-Pfad `https://empishaj.github.io/eaapp/` ausgelegt.

## Lokale Entwicklung

Da Markdown-Dateien per `fetch()` geladen werden, bitte über einen lokalen HTTP-Server öffnen, z. B.:

```bash
python -m http.server 8080
```

Dann `http://localhost:8080` öffnen.
