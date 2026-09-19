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
