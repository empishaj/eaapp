# EA-Aufgabenmodell – Kern, Mittelring und Peripherie

Das Modell verhindert, dass ein Enterprise Architect entweder zu abstrakt arbeitet oder zum „Super-Techniker für alles“ wird. Im Behördenmandat ist die Rollenabgrenzung besonders wichtig, weil Fachseite, Informationssicherheit, Datenschutz, Betrieb, Vergabe, Projektleitung, Plattformteams und externe Lieferanten jeweils eigene Verantwortungen besitzen.

## Kern – Enterprise Architecture im engsten Sinn

1. Architekturauftrag und Scope klären
2. Ist-Architektur verstehen
3. Zielarchitektur entwickeln
4. Architekturentscheidungen vorbereiten
5. Architekturprinzipien und Standards entwickeln
6. Datenführerschaft klären
7. Systemrollen und Domänengrenzen klären
8. Integrationsarchitektur gestalten
9. Transformationsroadmap entwickeln
10. Architektur-Governance etablieren
11. Architekturrisiken sichtbar machen
12. Architektur über Vorhaben hinweg synchronisieren

### Sechs Kernfragen

- Was muss die Organisation können?
- Welche Informationen braucht sie?
- Welche Systeme tragen diese Fähigkeiten?
- Wie arbeiten die Systeme zusammen?
- Wie soll die Landschaft künftig aussehen?
- Welche Entscheidungen und Schritte bringen uns dorthin?

## Mittelring – sehr wichtige EA-Disziplinen

Diese Themen muss der EA sehr gut verstehen und in die Gesamtarchitektur integrieren, besitzt sie aber häufig nicht allein:

- Capability Mapping und Prozessarchitektur
- Datenarchitektur und Data Governance
- Applikationsportfolio
- Schnittstellen- und Integrationsmanagement
- Security-by-Architecture
- Datenschutz-by-Architecture
- Betriebsarchitektur, RTO/RPO und Observability
- Cloud-, Plattform- und Kubernetes-Architektur
- Technologieportfolio und Lifecycle
- Architektur-Reviews und ADR-Steuerung
- technische Schulden und Abhängigkeiten
- Portfolio-/Programmabgleich
- DMS/eAkte und Dokumentenarchitektur
- Register- und Behördenintegration
- Dienstleistersteuerung und Architekturabnahme

## Peripherie – verstehen und beeinflussen, aber nicht automatisch übernehmen

- Projekt- und Programmmanagement
- Requirements Engineering im Detail
- Softwaredesign und Entwicklung
- Testmanagement
- DevOps und Plattformbetrieb
- Kubernetes-, Datenbank- und Netzwerkadministration
- Incident Management
- Informationssicherheitsmanagement
- Datenschutzmanagement
- Vergabe- und Vertragsmanagement
- Budgetsteuerung
- organisatorisches Change Management
- Schulungsorganisation
- operativer Support und Betriebsführung

## Rollenregel

Der Enterprise Architect muss nicht jede Spezialdisziplin ausführen. Er muss erkennen, **wann eine Spezialdisziplin architekturrelevant wird**, die richtige Rolle einbinden und deren Ergebnisse in eine konsistente Gesamtentscheidung überführen.

### Typische Abgrenzung

**Enterprise Architect:** Fähigkeiten, Zielarchitektur, Systemrollen, Datenownership, Integrationsprinzipien, Standards, Roadmap, Governance und vorhabenübergreifende Synchronisation.

**Solution Architect:** konkrete Lösung, Komponenten, APIs, Deployment- und Technologieentscheidungen eines Vorhabens.

**Software Architect:** Module, Codebasis, interne Patterns, Libraries, technische Detailstruktur.

**Platform Architect:** Runtime, Cloud/Kubernetes, Netzwerk-/Plattformdienste, CI/CD, Plattformstandards.

**Fachverantwortung:** fachliche Ziele, Prozess- und Leistungsentscheidungen.

**ISB/Informationssicherheit:** Sicherheitsorganisation, Sicherheitsvorgaben und formale Sicherheitsverantwortung.

**Datenschutz:** datenschutzrechtliche Bewertung und formale Datenschutzverantwortung.

**Betrieb:** operative Betriebsverantwortung, Incident/Problem, Runbooks und Betriebsprozesse.

## Merksatz

**Kern:** Richtung und Entscheidungen.  
**Mittelring:** Architekturdomänen und Qualitätsanforderungen.  
**Peripherie:** Umsetzung, Spezialprüfung und operativer Betrieb.
