# TOGAF 10 – Lernkurs für Enterprise Architects im Behördenkontext

## Kursstruktur

1. TOGAF Gesamtmodell und Grundbegriffe
2. Preliminary Phase & Architecture Capability
3. Phase A – Architecture Vision
4. Phase B – Business Architecture
5. Phase C – Data Architecture
6. Phase C – Application Architecture
7. Phase D – Technology Architecture
8. Phase E – Opportunities & Solutions
9. Phase F – Migration Planning
10. Phase G – Implementation Governance
11. Phase H & Requirements Management
12. Repository, Continuum, Content, Governance & Practitioner-Anwendung

**Status:** Einheit 1 ist als Lernzettel ausgearbeitet. Die Einheiten 2–12 sind als nächste Kursbausteine vorgesehen und werden nicht als bereits vollständig gelernt dargestellt.

# Einheit 1 – TOGAF Gesamtmodell und Grundbegriffe

## Lernziel

Nach dieser Einheit solltest du erklären können, was TOGAF ist und nicht ist, warum die ADM existiert, welche Phasen sie besitzt, wie Business/Data/Application/Technology Architecture zusammenhängen, warum Requirements Management quer durch den Zyklus läuft und wie TOGAF im Behördenmandat pragmatisch angepasst wird.

## Lernzettel 1.1 – Was ist TOGAF?

TOGAF ist ein Framework und eine Methode zur Entwicklung, Steuerung und Weiterentwicklung von Enterprise Architecture. Für die praktische Arbeit ist die **Architecture Development Method (ADM)** der zentrale Ordnungsrahmen.

TOGAF ist keine Modellierungssprache, keine Projektmanagementmethode, kein Softwareentwicklungsprozess und keine starre Dokumentationspflicht. ArchiMate kann modellieren; Projektmethoden planen und steuern Vorhaben; Softwarearchitektur entscheidet konkrete Lösungsdetails. TOGAF ordnet die Enterprise-Architekturarbeit.

### Mentales Bild

**Mandat → Zielrichtung → Facharchitektur → Daten → Anwendungen → Technologie → Optionen → Migration → Umsetzung → Veränderung.** Requirements Management begleitet alles.

### Behördenübersetzung

Nicht: „Wir führen ADM Phase B durch.“  
Sondern: „Wir klären, welche Verwaltungsfähigkeiten betroffen sind und welche Probleme gelöst werden müssen.“

TOGAF bleibt die interne Denksystematik des EA und muss nicht als Framework-Jargon gegenüber Fachseite oder Leitung verkauft werden.

## Lernzettel 1.2 – ADM als Gesamtbild

| Phase | Leitfrage |
|---|---|
| Preliminary | Wie organisieren wir Architekturarbeit? |
| A – Architecture Vision | Wohin wollen wir und warum? |
| B – Business Architecture | Was muss die Organisation fachlich können? |
| C – Data Architecture | Welche Informationen brauchen wir und wer führt sie? |
| C – Application Architecture | Welche Anwendungen unterstützen Fähigkeiten und Daten? |
| D – Technology Architecture | Welche technische/betriebliche Basis trägt das? |
| E – Opportunities & Solutions | Welche realistischen Lösungspfade gibt es? |
| F – Migration Planning | In welcher Reihenfolge setzen wir sie um? |
| G – Implementation Governance | Wie bleiben Umsetzung und Zielarchitektur verbunden? |
| H – Architecture Change Management | Wie reagieren wir kontrolliert auf Änderungen? |
| Requirements Management | Welche Anforderungen, Constraints und Entscheidungen gelten? |

Die ADM ist **iterativ**. Eine Erkenntnis in einer späteren Phase kann eine frühere Architekturannahme verändern.

## Lernzettel 1.3 – Vier Architekturdomänen

### Business Architecture

Frage: **Was muss die Organisation können und wie arbeitet sie?**

Inhalte: Capabilities, Verwaltungsleistungen, Organisation, Rollen, Verantwortlichkeiten, Prozesse und fachliche Informationsbedarfe.

Beispiel-Capability: „Nachweise verwalten“ – anfordern, entgegennehmen, zuordnen, prüfen, nachfordern, dokumentieren und archivieren. Noch geht es nicht um ein konkretes System.

### Data Architecture

Frage: **Welche Informationen braucht die Organisation und wer ist dafür verantwortlich?**

Inhalte: Datenobjekte, Definitionen, Owner, führende Systeme, Flüsse, Qualität, Schutzbedarf, Aufbewahrung und Löschung.

Kernfrage: „Wer darf dieses Datum fachlich verbindlich ändern?“

### Application Architecture

Frage: **Welche Anwendungen und Anwendungsservices unterstützen Fähigkeiten und Daten?**

Beispiele: Portal, Fachverfahren, DMS/eAkte, Registeradapter, IAM, Reporting. Wichtig: Capability ≠ Anwendung. Eine Anwendung unterstützt eine Fähigkeit; sie ist nicht die Fähigkeit.

### Technology Architecture

Frage: **Welche technische und betriebliche Basis ermöglicht die Anwendungen?**

Beispiele: Plattform, Cloud/On-Prem, Kubernetes, Netzwerk, IAM-Infrastruktur, API Gateway, Messaging, Datenbanken, Logging, Monitoring, Backup, Secrets und Deployment.

### Beziehung

**Business (Warum/Was) → Data (Welche Information) → Application (Welche Systeme) → Technology (Worauf läuft es).**

## Lernzettel 1.4 – Baseline, Target und Gap

**Baseline Architecture:** heutiger Zustand.  
**Target Architecture:** angestrebter Zustand.  
**Gap:** notwendige Veränderung dazwischen.

Beispiel: lokale Benutzerverwaltungen → zentrales IAM = fehlende IAM-Integration als Gap. Mehrere Statusquellen → eine führende Quelle = ungeklärte Datenführerschaft als Gap.

Eine gute Gap-Analyse entpersonalisiert Diskussionen: nicht „System X ist schlecht“, sondern „für Fähigkeit Y fehlen Datenowner, Schnittstellenstandard und Betriebsnachweis“.

## Lernzettel 1.5 – Requirements Management

Requirements Management ist keine einzelne Phase, die einmal abgearbeitet wird. Es begleitet die gesamte ADM.

Im Behördenmandat werden dort unter anderem fachliche und nicht-funktionale Anforderungen, rechtliche Randbedingungen, Schutzbedarf, Datenschutz, Betrieb, Schnittstellenanforderungen, Vergabevorgaben, Prinzipien, Risiken, Annahmen und offene Entscheidungen nachverfolgt.

Praktisches Arbeitsartefakt: **Architecture Requirements & Decisions Log** mit ID, Quelle, Beschreibung, Domäne, Priorität, Risiko, Stakeholder, Status und Entscheidung/Nächstem Schritt.

Wenn in Phase D auffällt, dass eine geplante Datenreplikation aus Datenschutz- oder Integritätsgründen nicht tragfähig ist, müssen Data/Application Architecture und Roadmap angepasst werden. Dieses Zurückspringen ist normal.

## Lernzettel 1.6 – Iteration und Tailoring

TOGAF ist kein linearer Wasserfall. Professionelle Architekturarbeit arbeitet mit Hypothesen, Erkenntnissen und Rückkopplung.

```text
Hypothese → Analyse → Erkenntnis → Auswirkungen auf frühere Architektur?
                                      ├─ nein → weiter
                                      └─ ja  → nachschärfen
```

### Tailoring

Nicht jedes theoretisch mögliche Artefakt ist notwendig. Für ein begrenztes Behördenmandat kann ein minimaler Satz ausreichen:

1. Architecture Vision
2. Capability-/Prozesssicht
3. Daten-/Applikationslandkarte
4. Gap-/Risikoliste
5. Roadmap mit Governance

Zusatzartefakte entstehen bei konkretem Bedarf: ADRs, Schnittstellenverträge, Security Reviews, Betriebs-/Plattformzielbilder usw.

## Behördenfall

Ausgangslage: Drei Fachverfahren, zwei Legacy. Registerdaten werden teilweise manuell abgeglichen. DMS-Anbindungen unterscheiden sich. Jedes Fachverfahren besitzt eigene Benutzerverwaltung. Monitoring und Betrieb sind auf verschiedene Dienstleister verteilt.

**Schwache Reaktion:** sofort Kubernetes, Microservices, Kafka oder Cloud vorschlagen.

**TOGAF-orientierte EA-Reaktion:**

- Preliminary: Sponsor, Scope, Gremien und Regeln klären.
- A: Nutzen und Zielrichtung formulieren.
- B: Verwaltungsfähigkeiten und kritische Prozesse verstehen.
- C Data: Datenobjekte und Führung klären.
- C Application: Systemrollen und Abhängigkeiten ordnen.
- D: Plattform, Security und Betrieb bewerten.
- E: realistische Lösungspfade vergleichen.
- F: Reihenfolge und Übergangsarchitekturen planen.
- G: Umsetzung über Reviews/Nachweise am Zielbild halten.
- H: Änderungen kontrolliert in Zielbild und Roadmap aufnehmen.

## Merksätze Einheit 1

1. TOGAF ist Denk- und Vorgehensrahmen, keine Dokumentenmaschine.
2. ADM führt von Unsicherheit zu Architekturentscheidungen.
3. Business erklärt Fähigkeiten und fachliche Arbeit.
4. Data klärt Information und Verantwortung.
5. Application klärt Systemrollen und Services.
6. Technology klärt technische und betriebliche Basis.
7. Requirements Management läuft durch den gesamten Zyklus.
8. Baseline → Target → Gap erzeugt Veränderungsbedarf.
9. ADM ist iterativ.
10. TOGAF wird an das Mandat angepasst.
11. Nicht jedes Artefakt ist immer nötig.
12. Jede Phase sollte bessere Entscheidungen ermöglichen.

## Selbsttest

1. Was ist die wichtigste Rolle der ADM?
2. Warum ist ADM kein Wasserfall?
3. Was unterscheidet Business von Application Architecture?
4. Wo liegt primär die Frage nach der führenden Quelle des Vorgangsstatus?
5. Was ist ein Gap?
6. Was begleitet sämtliche ADM-Phasen?
7. Warum muss TOGAF im Behördenkontext angepasst werden?
8. Warum darf Technology Architecture nicht automatisch der Startpunkt sein?

## Praxisprüfung

Ein IT-Leiter sagt: „Wir wollen unsere Fachverfahren mittelfristig in die Cloud bringen. Erstellen Sie eine Cloud-Zielarchitektur.“

Eine starke EA-Reaktion klärt zuerst fachlichen Treiber, Scope, Daten und Schutzbedarf, Anwendungseignung, Betriebsanforderungen, Constraints und Alternativen. Erst daraus entsteht eine seriöse Cloud-Zielarchitektur.
