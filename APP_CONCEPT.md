# EA Mastery 5.0 – App-Konzept

## 1. Produktziel
EA Mastery ist keine digitale Bibliothek, sondern eine persönliche Lernakademie für Enterprise Architecture im deutschen Behördenkontext. Ziel ist professionelle Handlungsfähigkeit vom ersten Grundbegriff bis zur Principal-/Master-Ebene.

## 2. Leitprinzipien
1. **Lernen vor Nachschlagen.** Akademie und Wissensbasis sind getrennt.
2. **Evidenz vor Lesefortschritt.** Lesen allein beweist keine Kompetenz.
3. **Vom Einfachen zum Komplexen.** Jede Domäne besitzt sechs aufeinander aufbauende Stufen.
4. **Retrieval vor Wiederlesen.** Aktive Erinnerung wird über Spaced Repetition geplant.
5. **Transfer vor Auswendiglernen.** Behördenfälle zwingen zur Anwendung unter Unsicherheit.
6. **Lieferfähigkeit als Ziel.** Jede Lernstrecke endet in einem professionellen EA-Artefakt.
7. **Querverbindungen sichtbar machen.** EA wird als zusammenhängendes System gelernt.
8. **Local-first.** Lerndaten bleiben lokal, exportierbar und resetbar.
9. **Content-first Architecture.** Inhalte sind Daten, nicht UI-Code.
10. **Behördenkontext permanent.** Fachseite, IT, Security, Datenschutz, Betrieb, Vergabe, Dienstleister und Gremien werden systematisch einbezogen.

## 3. Informationsarchitektur
### Heute
Persönlicher Tagesplan: nächste sinnvolle Lesson, fällige Reviews, Falltraining und Kompetenzlücken.

### Akademie
16 Kompetenzdomänen × 6 Stufen:
1. Grundlagen
2. Orientierung und Abgrenzung
3. Querverbindungen / Practitioner
4. Methodenanwendung / Advanced
5. Falltraining / Advanced
6. Professionell liefern / Master

### Trainieren
Drei voneinander getrennte Evidenzformen:
- Recall / Lernkarten
- Behördenfälle
- Artefakt-Lab

### Wissen
- Lexikon
- 160 Fachbücher
- vollständige Projektquellen
- globale Suche

### Profil
- Mastery-Profil je Kompetenzdomäne
- Lernhistorie
- Einstellungen
- Backup/Import
- Offline-Paket
- getrennte Reset-Funktionen

## 4. Mastery Engine
Mastery je Lesson:
- 15 % Lerninhalt verarbeitet
- 35 % Recall-Evidenz
- 20 % Fallanwendung
- 30 % professionelles Artefakt

Lesen kann eine Lesson daher nie allein auf Master-Level bringen.

Mastery-Level:
- Neu: 0–24 %
- Foundation: 25–49 %
- Practitioner: 50–69 %
- Advanced: 70–84 %
- Master: 85–100 %

## 5. Didaktik einer Lesson
Jede Lesson hat sechs interne Lernschritte:
1. **Start** – Ziele, Relevanz, sokratische Vorfragen
2. **Erklären** – einfache Sprache, Begriffe, Beispiele, mentales Modell
3. **Verbinden** – Querverbindungen, Abgrenzungen, Denkfehler
4. **Anwenden** – realistischer Behördenfall
5. **Liefern** – professionelles Artefakt und Reviewfragen
6. **Prüfen** – Retrieval-Fragen und Übergang in Spaced Repetition

## 6. Persistenz
IndexedDB `ea-learnings-local` speichert:
- Lesson-Progress
- Lernkartenstatus / SRS
- Kartengedächtnis je EA- und BSI-Karte: gesehen, gelesen, bewertet, Zeitstempel und Bewertungshistorie
- kürzlich gezeigte Karten zur zufälligen, wiederholungsarmen Sessionsteuerung
- Fall-Evidenz
- Artefaktstatus und Notizen
- Aktivitätslog
- Einstellungen

Cache Storage speichert ausschließlich App- und Content-Ressourcen. Cache und Lernstand können unabhängig voneinander gelöscht werden.

## 7. Content-Modell
```
content/
  curriculum/
    courses.json
    lessons.json
  practice/
    cards.json
    cases.json
  knowledge/
    lexicon.json
    books.json
    sources.json
    search.json
  library/
    modules/*.md
    derived/*.md
```

## 8. Erweiterungsregel
Neue Inhalte werden nicht in JavaScript programmiert. Sie werden als Content angelegt und durch `tools/validate_content.py` geprüft. Dadurch bleiben UI, SRS und Mastery Engine unabhängig vom Umfang des Curriculums.

## 9. Qualitätsdefinition
Eine Lesson ist vollständig, wenn sie:
- einen klaren Lernzweck besitzt,
- Grundlagen ohne Jargon erklären kann,
- mindestens drei Querverbindungen zeigt,
- Abgrenzungen und Fehlannahmen benennt,
- einen realistischen Behördenfall enthält,
- einen professionellen Liefergegenstand fordert,
- Recall-Fragen besitzt,
- Quellen und Literatur nachvollziehbar referenziert.

## Visualization Layer – 5.1

Visualisierung ist eine eigene Content-Schicht. Mermaid erzeugt aus strukturierten Definitionen SVG und ist damit unabhängig von Bildschirmauflösung und Zoom.

Grundsätze:
1. Diagramme dienen einer konkreten Lernfrage, nicht Dekoration.
2. Jede Grafik benötigt Titel und Lernbotschaft.
3. Flowcharts zeigen Kausalität/Struktur, Sequence Diagrams Interaktion über Zeit.
4. Diagramme bleiben Daten (`content/visuals/diagrams.json`), nicht hart codiertes HTML.
5. Lesson-Content und Visualisierung können unabhängig erweitert werden.
6. Auf Smartphones öffnet sich jedes Diagramm in einer skalierbaren Vollbildansicht.
