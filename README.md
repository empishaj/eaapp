# EA Learnings 3.0.0

Smartphone-first Progressive Web App für professionelles Enterprise-Architecture-Lernen im Behördenkontext.

## Leitidee

EA Learnings 3.0 ist kein Dokumentenordner. Das Curriculum arbeitet wie ein Coach/Professor:

1. **Verstehen** – Kernidee und mentales Modell aufbauen.
2. **Verbinden** – Querverbindungen zu Fachlichkeit, Daten, Anwendungen, Integration, Security, Betrieb, Governance, Kosten und Transformation erkennen.
3. **Anwenden** – Behördenfälle und Architekturentscheidungen lösen.
4. **Professionell liefern** – ein belastbares EA-Artefakt erstellen oder reviewen und die Entscheidung gegenüber Stakeholdern begründen.

## Curriculum 3.0

- **64 komplett neu geschriebene Professoren-Einheiten**
- **16 Kompetenzfelder**
- **256 aktive Lernkarten** für Retrieval Practice und Spaced Repetition
- **10 geführte Kompetenzpfade**
- jede Einheit mit sokratischen Fragen, mentalem Modell, Querverbindungen, Denkfehlern, Behördenfall, Reviewfragen und Profi-Liefergegenstand
- jede Einheit ist mit sechs verwandten Einheiten zu einem Wissensnetz verbunden
- **316 Lexikonbegriffe** mit Kontextbeispielen aus Quellen und Curriculum

## Die 16 Kompetenzfelder

1. EA Profession
2. Strategie & Operating Model
3. Business Architecture
4. Requirements & Qualität
5. Daten & Privacy
6. Anwendungen & Domänen
7. Integration & Distributed Systems
8. Cloud, Plattform & Netz
9. Security, IAM & Privacy
10. Betrieb & Resilienz
11. Transformation & Ökonomie
12. Governance, Entscheidungen & Vergabe
13. Behördenarchitektur
14. Consulting, Change & Leadership
15. Innovation & AI
16. EA Practice & Principal Skills

## Quellenmodell

Die 25 ursprünglichen Projektquellen bleiben vollständig als Referenzbibliothek erhalten. Die Professoren-Einheiten sind neu formulierte Lerninhalte. Jede Einheit kennzeichnet, ob sie

- aus **Projektquellen + fachlicher Synthese** entsteht oder
- bei einer bisherigen Curriculum-Lücke eine **explizite fachliche Erweiterung** enthält.

Damit bleibt nachvollziehbar, was aus dem Projektmaterial stammt und wo professionelles EA-Wissen ergänzend eingebracht wurde.

## Lernengine

- Smartphone-first Bottom Navigation
- lokales Gedächtnis in IndexedDB
- Spaced Repetition
- Retrieval Practice
- 3/5/10/20-Minuten-Sessions
- Szenario- und Transferkarten
- Kompetenzprofil
- Lernfortschritt je Professoren-Einheit
- Fokusmodus
- Dark Mode und skalierbare Schrift
- vollständiger Offline-Betrieb
- Backup/Restore und getrennte Reset-Funktionen

## Lexikon und Wissensnetz

Begriffe werden in den Referenztexten automatisch mit dem Lexikon verknüpft. Lexikoneinträge zeigen Kontextbeispiele und führen zurück in Originalquelle oder Professoren-Einheit. Jede Professoren-Einheit verlinkt zusätzlich zu fachlich verwandten Einheiten.

## Validierung

```bash
python tools/validate_professor_curriculum.py
python tools/rebuild_search.py
node --check assets/app.js
```

## GitHub Pages

Der Workflow unter `.github/workflows/pages.yml` veröffentlicht die statische PWA direkt aus dem Repository-Root.
