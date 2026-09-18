# Changelog

## 2.0.0 – 2026-09-18

### Smartphone-first
- feste Bottom-Navigation: Heute, Lernen, Wissen, Ich
- mobile Suche jederzeit in der Topbar
- 48-px-Touchziele und Safe-Area-Unterstützung
- Dark Mode / Systemmodus
- skalierbare Schriftgröße
- `prefers-reduced-motion`
- Reader mit mobilem Inhaltsverzeichnis und Fokusmodus

### Lernengine
- Tageslernplan
- Spaced Repetition
- Retrieval Practice mit vier Sicherheitsstufen
- 3-, 5-, 10- und 20-Minuten-Sessions
- 43 initiale Lern- und Fallkarten
- fünf Lernpfade
- EA-Falltraining
- Modul-Quiz
- Kompetenzprofil und Wissenslückenhinweis

### Lokales Gedächtnis
- IndexedDB für Lernstand, Wiederholungsplan und Historie
- Migration bestehender v1-Lerndaten
- Leseposition, Notizen, Favoriten und Einstellungen
- Backup/Restore als JSON
- Cache und Lerndaten getrennt löschbar
- vollständiger Offline-Pack auf Wunsch

### PWA
- Version 2.0.0 Service Worker
- PWA-Shortcuts
- neues Manifest für Education/Productivity
- Update-Hinweis erhält lokale Lerndaten

## 2.1.0 – Kontextuelles EA-Lexikon

- Zentrales EA-Lexikon mit 74 kuratierten Begriffen.
- Jeder Lexikoneintrag besitzt eine Kurzdefinition und mindestens zwei, meist drei Beispiele aus unterschiedlichen Projekttexten.
- Beispiele verlinken direkt in den jeweiligen Ursprungstext und die passende Überschrift.
- Fachbegriffe werden im Reader automatisch dezent mit dem Lexikon verknüpft – pro Abschnitt einmal, um Überverlinkung zu vermeiden.
- Beim Öffnen eines Lexikonbegriffs aus einem Lerntext wird die ursprüngliche Leseposition gespeichert; „Zurück zum ursprünglichen Text“ springt exakt zurück.
- Öffnet man ein Beispiel aus dem Lexikon, zeigt der Reader einen direkten Rückweg zum Lexikoneintrag.
- Jeder Lerntext erhält am Ende „Begriffe in diesem Text“ mit Direktdefinitionen; die wichtigsten zwölf sind sofort sichtbar, weitere bleiben aufklappbar.
- Volltextsuche durchsucht jetzt zusätzlich das Lexikon.
- Lexikon ist Teil des Offline-Pakets und als PWA-Shortcut verfügbar.
