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

## Einheit 1 – Gesamtmodell und Grundbegriffe

### Was ist TOGAF?
TOGAF ist ein Framework und eine Methode zur Entwicklung, Steuerung und Weiterentwicklung von Enterprise Architecture. Für die praktische Arbeit ist die **Architecture Development Method (ADM)** der zentrale Ordnungsrahmen.

TOGAF ist keine Modellierungssprache, keine Projektmanagementmethode und kein Softwareentwicklungsprozess. Es ist an den Kontext des Mandats anzupassen.

### ADM – mentales Modell

Preliminary → A Architecture Vision → B Business Architecture → C Data & Application Architecture → D Technology Architecture → E Opportunities & Solutions → F Migration Planning → G Implementation Governance → H Architecture Change Management. **Requirements Management** begleitet den gesamten Zyklus.

### Vier zentrale Domänen

**Business:** Was muss die Organisation können und wie arbeitet sie?

**Data:** Welche Informationen werden benötigt, wer führt sie, wie fließen und leben sie?

**Application:** Welche Anwendungen unterstützen Fähigkeiten und Daten?

**Technology:** Welche technische und betriebliche Basis trägt die Anwendungen?

### Baseline, Target, Gap

- Baseline Architecture: heutiger Zustand.
- Target Architecture: angestrebter Zustand.
- Gap: notwendige Veränderung zwischen Ist und Ziel.

### Behördenübersetzung

Nicht „Wir machen ADM Phase B/C/D“, sondern: „Wir klären Fähigkeiten, Daten, Systeme und Plattformbedingungen und leiten daraus Optionen, Roadmap und Governance ab.“

### Merksätze

1. TOGAF ist ein Denk- und Vorgehensrahmen, keine Dokumentenmaschine.
2. ADM führt von Unsicherheit zu Architekturentscheidungen.
3. Business erklärt Fähigkeiten und fachliche Arbeit.
4. Data klärt Information und Verantwortung.
5. Application klärt Systemrollen und Services.
6. Technology klärt technische und betriebliche Basis.
7. Requirements Management läuft durch den gesamten Zyklus.
8. Baseline → Target → Gap erzeugt Veränderungsbedarf.
9. ADM ist iterativ.
10. TOGAF wird an das Mandat angepasst.
11. Nicht jedes theoretisch mögliche Artefakt ist notwendig.
12. Jede Phase sollte eine bessere Entscheidung ermöglichen.

## Praxisfall Bundesbehörde

Ausgangslage: Drei Fachverfahren, zwei Legacy. Registerdaten werden teilweise manuell abgeglichen. DMS-Anbindungen unterscheiden sich. Jedes Verfahren besitzt eigene Benutzerverwaltung. Monitoring und Betrieb sind auf mehrere Dienstleister verteilt.

**Schwache Reaktion:** sofort Kubernetes, Microservices, Kafka oder Cloud vorschlagen.

**EA-Reaktion:** Erst Sponsor, Scope und Governance klären; dann Fähigkeiten und Arbeitsrealität; anschließend Datenführerschaft und Anwendungen; danach Technologie/Betrieb; erst dann Lösungsoptionen, Roadmap und Governance.

## Selbsttest

1. Was ist die wichtigste Rolle der ADM?
2. Ist ADM ein linearer Wasserfall?
3. Was unterscheidet Business Architecture von Application Architecture?
4. In welcher Domäne liegt primär die Frage nach der führenden Quelle des Vorgangsstatus?
5. Was ist ein Gap?
6. Was begleitet sämtliche ADM-Phasen?
7. Warum wird TOGAF an eine Bundesbehörde angepasst?
