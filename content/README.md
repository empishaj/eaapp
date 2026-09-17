# Inhalte erweitern

## Neues Lernmodul

1. Markdown-Datei unter `content/modules/` anlegen.
2. In `content/index.json` einen neuen Modul-Eintrag ergänzen:

```json
{
  "id": "mein-neues-modul",
  "title": "Mein neues Modul",
  "sourceTitle": "Eigener Inhalt",
  "category": "Technische Vertiefung",
  "tags": ["API", "Beispiel"],
  "path": "content/modules/mein-neues-modul.md",
  "summary": "Kurze Beschreibung",
  "words": 1200,
  "minutes": 6,
  "kind": "project-source"
}
```

3. `content/version.json` hochzählen, z. B. `1.0.0` → `1.1.0`, und eine kurze Update-Nachricht eintragen.
4. In `sw.js` die Cache-Konstante ebenfalls hochzählen, z. B. `ea-learnings-v1.0.0` → `ea-learnings-v1.1.0`.
5. Committen und pushen.

Der GitHub-Actions-Workflow erzeugt den Volltext-Suchindex automatisch neu und veröffentlicht anschließend die PWA.
