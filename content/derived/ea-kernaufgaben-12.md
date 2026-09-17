# 12 Kernaufgaben eines Enterprise Architects im Behördenkontext

Diese Übersicht behandelt den Enterprise Architect als **externen Dienstleister**: Er analysiert, strukturiert, entwickelt Optionen, macht Risiken sichtbar, bereitet Entscheidungen vor und begleitet die Umsetzung. Die fachliche bzw. hoheitliche Entscheidung bleibt bei der zuständigen Stelle der Behörde.

## 1. Architekturauftrag und Scope klären

**Beispiel:** Der Auftrag „Unterstützen Sie uns bei der Zielarchitektur des Fachverfahrens“ wird in Sponsor, Scope, Nicht-Scope, Entscheidungswege, vorhandene Standards, Gremien und Liefergegenstände zerlegt.

**Typische Artefakte:** Mandatssteckbrief, Architecture Working Agreement, Stakeholderlandkarte.

## 2. Ist-Architektur verstehen

**Beispiel:** Mehrere Fachverfahren, Excel-Nebenlisten, DMS, Registerabfragen und Dienstleister werden zu Capability-, System-, Daten- und Schnittstellenlandkarten zusammengeführt. Der EA benennt nicht nur Systeme, sondern die kritischen Abhängigkeiten und Risiken.

## 3. Zielarchitektur entwickeln

**Beispiel:** Aus einer technischen Modernisierungsliste entsteht ein konsistentes Zielbild mit klaren Domänengrenzen, Datenführerschaft, IAM, DMS/eAkte, Schnittstellen, Plattform- und Betriebsbedingungen.

## 4. Architekturentscheidungen vorbereiten

**Beispiel:** REST, Messaging und Batch werden anhand fachlicher Anforderungen, Betriebsfolgen, Security, Kosten, Migration und Risiken verglichen. Ergebnis ist ein ADR-Entwurf mit Empfehlung; entschieden wird durch die Behörde.

## 5. Architekturprinzipien und Standards definieren

**Beispiel:** „Datenzugriffe zwischen Fachverfahren erfolgen über definierte Schnittstellen und nicht über direkte Zugriffe auf fremde Datenbanken.“ Ein Prinzip enthält Begründung, Konsequenzen, Reviewfragen und Ausnahmebedingungen.

## 6. Datenführerschaft klären

**Beispiel:** Wenn drei Systeme unterschiedliche Vorgangsstatus führen, wird je Datenobjekt geklärt: führende Quelle, Änderer, Konsumenten, Korrekturweg, Qualität und Schutzbedarf.

## 7. Systemrollen und Domänengrenzen klären

**Beispiel:** Vorgangsführung, Dokumenten-/Aktenführung, Registerinformation und Reporting erhalten klare Zielrollen. Reporting darf operative Daten auswerten, aber nicht eigenständig korrigieren.

## 8. Integrationsarchitektur gestalten

**Beispiel:** Je Bedarf wird ein passendes Integrationsmuster gewählt: synchrone API, Event, Batch, Dokumentenservice oder Gateway. Provider, Consumer, fachlicher Zweck, Fehlerfall, Quittierung, Versionierung und Monitoring werden definiert.

## 9. Transformationsroadmap entwickeln

**Beispiel:** Statt Big Bang werden Plateaus geplant: IAM standardisieren, Schnittstellen entkoppeln, Datenführerschaft klären, DMS integrieren, neues Fachverfahren einführen, Legacy abbauen.

## 10. Architektur-Governance etablieren

**Beispiel:** R0–R4-Triage, Architecture Reviews, ADR-Register, Ausnahmeprozess und Maßnahmenregister werden als leichter Steuerungsrahmen eingeführt. Die Behörde bleibt Owner der Governance.

## 11. Architekturrisiken sichtbar machen

**Beispiel:** Mehrere führende Datenquellen, EOL-Technologie, DLQ ohne Owner, fehlender Restore-Test oder Dienstleisterabhängigkeit werden als Enterprise-Risiken mit Ursache, Wirkung, Maßnahme und Owner dargestellt.

## 12. Architektur über Vorhaben hinweg synchronisieren

**Beispiel:** Fachverfahrensmodernisierung, Datenplattform, IAM-Modernisierung und externe Schnittstellen werden über eine Abhängigkeitsmatrix verbunden. Gemeinsame Architekturentscheidungen werden programmübergreifend vorbereitet.

## Dienstleisterregel

> Du erhebst, analysierst, strukturierst, visualisierst, bewertest, entwickelst Optionen, gibst eine begründete Empfehlung, bereitest Entscheidungen vor, dokumentierst Konsequenzen und begleitest die Umsetzung. Die Entscheidung verbleibt bei der zuständigen Rolle der Behörde.
