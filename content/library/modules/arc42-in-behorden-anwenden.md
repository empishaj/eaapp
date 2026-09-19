## Checkliste: arc42 in Bundesbehörden richtig einsetzen

- [ ] Architekturzweck klären: Entscheidungsvorlage, Lieferdokumentation, Review-Unterlage, Betriebsübergabe oder Zielbild?
- [ ] Stakeholder sauber trennen: Fachseite, IT, Security, Betrieb, Datenschutz, Dienstleister, Architekturboard, Projektleitung.
- [ ] Systemgrenze eindeutig ziehen: Was gehört zum Fachverfahren, was ist Nachbarsystem, was ist Plattformleistung?
- [ ] Fachlichen Kontext zuerst beschreiben, bevor technische Bausteine modelliert werden.
- [ ] Randbedingungen explizit aufnehmen: Gesetze, Standards, Behördenvorgaben, Plattformvorgaben, Vergabe-/Dienstleisterrahmen.
- [ ] Qualitätsziele messbar formulieren: Verfügbarkeit, Nachvollziehbarkeit, Wartbarkeit, Sicherheit, Betriebsfähigkeit, Änderbarkeit.
- [ ] Bausteinsicht nicht mit Quellcode-Struktur verwechseln: Für Behörden zählt zuerst die fachlich-technische Verantwortungsstruktur.
- [ ] Laufzeitsichten für kritische Vorgänge erstellen: Antrag einreichen, Registerabfrage, Dokumentablage, Bescheiderstellung, Fehlerfall.
- [ ] Verteilungssicht mit Betriebsmodell verbinden: Umgebungen, Netzzonen, Mandantentrennung, Schnittstellen, Monitoring, Backup.
- [ ] Querschnittskonzepte ernst nehmen: IAM, Logging, Datenschutz, Fehlerbehandlung, Datenhaltung, Schnittstellen, Observability, Archivierung.
- [ ] Architekturentscheidungen als ADRs dokumentieren: Entscheidung, Alternativen, Begründung, Konsequenzen, Gültigkeit.
- [ ] Risiken und technische Schulden nicht verstecken, sondern priorisiert mit Maßnahmen führen.
- [ ] arc42 schlank halten: keine Textwüste, sondern entscheidungsfähige Architekturkommunikation.
- [ ] Jede Sicht mit einer konkreten Nutzungsfrage verbinden: „Wer braucht diese Information, um welche Entscheidung zu treffen?“

<>

## 1. Grundidee: arc42 ist kein Formular, sondern ein Kommunikationssystem für Architektur

arc42 ist offiziell als Vorlage für Architekturkommunikation und Architekturdokumentation beschrieben. Der Kern ist nicht, möglichst viele Kapitel zu füllen, sondern die zwei praktischen Fragen zu beantworten: Was muss über die Architektur kommuniziert werden, und wie soll es kommuniziert werden? Die offizielle arc42-Struktur umfasst Einführung und Ziele, Randbedingungen, Kontextabgrenzung, Lösungsstrategie, Bausteinsicht, Laufzeitsicht, Verteilungssicht, Querschnittskonzepte, Architekturentscheidungen, Qualitätsanforderungen, Risiken/technische Schulden und Glossar. ([arc42.org](https://arc42.org/overview))

Für deinen Kontext als Enterprise Architekt in Bundesbehörden ist der entscheidende Punkt: Du verwendest arc42 nicht nur als Softwarearchitektur-Dokumentation, sondern als übersetzbare Architekturakte. Diese Akte muss verschiedenen Gruppen dienen. Die Fachseite muss verstehen, welche fachlichen Fähigkeiten unterstützt werden. Die IT muss verstehen, welche Systeme, Schnittstellen und Datenflüsse beteiligt sind. Security muss Schutzbedarf, IAM, Protokollierung, Netz- und Betriebsrisiken erkennen. Der Betrieb muss wissen, wie das System deployt, überwacht, gesichert, wiederhergestellt und betrieben wird. Dienstleister müssen wissen, was sie liefern, dokumentieren und verantworten. Das Architekturboard muss nachvollziehen können, welche Entscheidungen getroffen wurden und welche Risiken verbleiben.

Die häufigste Fehlannahme lautet: „arc42 ist zu technisch für Enterprise Architecture.“ Das ist falsch. Richtig ist: arc42 muss auf der richtigen Abstraktionsebene angewendet werden. Auf Solution-Ebene dokumentierst du konkrete Bausteine, Schnittstellen, Laufzeitszenarien und Deployment. Auf Enterprise-Ebene dokumentierst du Fähigkeiten, Systemrollen, Standards, Integrationsmuster, Zielbildprinzipien, Plattformvorgaben, Governance und Übergangspfade. Die Struktur bleibt nützlich, aber die Tiefe und Sprache werden angepasst.

## 2. Merksatz für Behörden: arc42 beantwortet zwölf Führungsfragen

Wenn du arc42 professionell nutzt, beantwortet jedes Kapitel eine konkrete Steuerungsfrage. Genau dadurch wird aus einem Dokument ein Führungsinstrument.

| Aspekt | Details/Erklärung | Beispiel im Behörden-Fachverfahren | Literatur/Quelle |
|---|---|---|---|
| Einführung und Ziele | Klärt, warum das System existiert, welche Stakeholder relevant sind und welche Qualitätsziele treiben. | „Das Verfahren unterstützt digitale Antragstellung, Sachbearbeitung, Bescheiderstellung und revisionsfähige Ablage.“ | arc42 beschreibt hier Anforderungen, Stakeholder und Top-Qualitätsziele. ([arc42.org](https://arc42.org/overview)) |
| Randbedingungen | Beschreibt Vorgaben, die Architekturentscheidungen begrenzen. | Datenschutz, BSI-Grundschutz, bestehende Registerschnittstelle, DMS-Vorgabe, Plattformstandard, Vergaberahmen. | arc42 nennt hier technische, organisatorische und regulatorische Randbedingungen. ([arc42.org](https://arc42.org/overview)) |
| Kontextabgrenzung | Trennt System, Nachbarsysteme, Nutzergruppen und Schnittstellen. | Portal, IAM, Register, DMS/eAkte, Zahlungsdienst, Monitoring, Fachaufsicht. | arc42 sieht hier externe Systeme, Nutzer und Schnittstellen vor. ([arc42.org](https://arc42.org/overview)) |
| Lösungsstrategie | Verdichtet die wichtigsten architektonischen Leitentscheidungen. | „API-first, zentrale Identität, führendes Fachverfahren für Vorgangsdaten, DMS als führendes System für Aktenmetadaten.“ | arc42 beschreibt hier grundlegende Entscheidungen und Lösungsansätze. ([arc42.org](https://arc42.org/overview)) |
| Bausteinsicht | Zeigt statische Struktur und Verantwortlichkeiten. | Portal, API-Gateway, Fachlogik, Registeradapter, DMS-Adapter, Datenbank, Audit-Komponente. | arc42 beschreibt die hierarchische statische Zerlegung. ([arc42.org](https://arc42.org/overview)) |
| Laufzeitsicht | Zeigt wichtige Abläufe, Interaktionen und Fehlerfälle. | Antrag einreichen, Registerdaten prüfen, Dokument ablegen, Bescheid erstellen, Register nicht erreichbar. | arc42 beschreibt hier Szenarien, Schnittstelleninteraktion, Betrieb und Fehlerverhalten. ([arc42.org](https://arc42.org/overview)) |
| Verteilungssicht | Verknüpft Softwarebausteine mit Infrastruktur, Umgebungen und Topologien. | Portal in DMZ, API-Gateway in Integrationszone, Fachverfahren in Fachzone, Datenbank in Datenzone. | arc42 beschreibt technische Infrastruktur und Mapping von Software auf Infrastruktur. ([arc42.org](https://arc42.org/overview)) |
| Querschnittskonzepte | Beschreibt Regeln, die mehrere Bausteine betreffen. | IAM, Logging, Fehlerbehandlung, Datenklassifikation, Schnittstellenstandard, Mandantentrennung. | arc42 nennt wiederkehrende, bausteinübergreifende Lösungskonzepte. ([arc42.org](https://arc42.org/overview)) |
| Architekturentscheidungen | Macht zentrale Entscheidungen nachvollziehbar. | „REST für Registerabfrage, DMS-Integration über definierte Fachschnittstelle, zentrales IAM statt lokaler Nutzerverwaltung.“ | arc42 sieht hier wichtige, teure, kritische oder riskante Entscheidungen mit Begründung vor. ([arc42.org](https://arc42.org/overview)) |
| Qualitätsanforderungen | Übersetzt Qualität in prüfbare Szenarien. | „Bei Registerausfall wird der Vorgang als wartend markiert; Sachbearbeitung erhält nachvollziehbare Statusinformation.“ | Das arc42-Qualitätsmodell arbeitet mit messbaren Anforderungen, Kontext, Triggern und Akzeptanzkriterien. ([quality.arc42.org](https://quality.arc42.org/requirements/)) |
| Risiken und technische Schulden | Führt bekannte Unsicherheiten, Schwachstellen und Maßnahmen. | „Register-SLA unklar“, „DMS-Fehlerfälle nicht spezifiziert“, „IAM-Rollenmodell fachlich nicht abgenommen“. | arc42 empfiehlt priorisierte Risiken und technische Schulden inklusive Gegenmaßnahmen. ([docs.arc42.org](https://docs.arc42.org/section-11/)) |
| Glossar | Sichert gemeinsame Sprache. | Antrag, Vorgang, Nachweis, Bescheid, Akte, Fall, Status, führendes System, Sachbearbeitung. | arc42 sieht hier Fach- und Technikbegriffe als gemeinsame Sprache vor. ([arc42.org](https://arc42.org/overview)) |

## 3. Das Beispiel-Fachverfahren: „Digitales Leistungs- und Bescheidverfahren“

Als Arbeitsbeispiel verwenden wir ein fiktives, aber realistisches Behördenverfahren. Bürgerinnen und Bürger stellen über ein Portal einen Antrag. Das Portal authentifiziert über ein zentrales IAM. Das Fachverfahren prüft Antragsdaten, ruft Registerdaten ab, speichert Vorgangs- und Entscheidungsdaten in einer Fachverfahrensdatenbank, legt Nachweise und Bescheide im DMS beziehungsweise in der eAkte ab, veröffentlicht Statusinformationen über ein API-Gateway und liefert technische Betriebsdaten an Monitoring und Logging. Der Betrieb erfolgt über definierte Umgebungen, mit Betriebsmodell, Backup, Wiederanlauf, Rollenmodell und Dienstleisterzuständigkeiten.

Die wichtigsten Bausteine sind Portal, API-Gateway, IAM, Fachverfahren, Fachverfahrensdatenbank, Registeradapter, DMS/eAkte-Adapter, Dokumentenerzeugung, Benachrichtigungsdienst, Monitoring/Logging und Betriebsplattform. Die wichtigsten Datenobjekte sind Personendaten, Antragsdaten, Vorgangsdaten, Nachweisdokumente, Registerauskünfte, Bescheiddaten, Zahlungsdaten, Kommunikationsdaten und Audit-/Protokolldaten.

Der Architekturwert dieses Beispiels liegt darin, dass es typische Behördenprobleme sichtbar macht: unklare Systemgrenzen, mehrere führende Systeme, Schnittstellenabhängigkeiten, Schutzbedarf, lange Betriebslebenszyklen, Dienstleisterübergaben, Nachweisfähigkeit, manuelle Ersatzprozesse und technische Schulden in gewachsenen Fachverfahren.

## 4. Behörden-taugliche arc42-Vorlage als Kopiervorlage

Die folgende Vorlage kannst du als Ausgangspunkt für ein Architekturpaket verwenden. Sie ist bewusst nicht maximal ausführlich, sondern gremiumstauglich, reviewfähig und erweiterbar.

:::writing{variant="document" id="73942"}
# arc42-Architekturdokumentation: [Name des Fachverfahrens]

## 0. Dokumentsteuerung

**System / Vorhaben:** [Name]  
**Version:** [Version]  
**Status:** Entwurf / in Review / freigegeben / abgelöst  
**Owner Architektur:** [Name/Rolle]  
**Fachlicher Owner:** [Name/Rolle]  
**Technischer Owner:** [Name/Rolle]  
**Security-Ansprechpartner:** [Name/Rolle]  
**Betriebsverantwortung:** [Name/Rolle/Organisation]  
**Letztes Review:** [Datum]  
**Nächstes Review:** [Datum oder Ereignis]

## 1. Einführung und Ziele

### 1.1 Zweck des Systems

[Beschreibe in 5 bis 10 Sätzen, welchen fachlichen Zweck das System erfüllt, welche Leistungen oder Verwaltungsprozesse unterstützt werden und warum das System für die Behörde relevant ist.]

### 1.2 Stakeholder und Erwartungen

[Liste Fachseite, Sachbearbeitung, Fachaufsicht, IT, Security, Datenschutz, Betrieb, Dienstleister, Architekturboard und Nutzergruppen mit ihren Erwartungen.]

### 1.3 Top-Qualitätsziele

[Definiere maximal fünf priorisierte Qualitätsziele, zum Beispiel Verfügbarkeit, Nachvollziehbarkeit, Schutzbedarfserfüllung, Änderbarkeit, Betriebsfähigkeit.]

## 2. Randbedingungen

[Dokumentiere rechtliche, organisatorische, technische, sicherheitsbezogene, betriebliche und vertragliche Vorgaben.]

## 3. Kontextabgrenzung

### 3.1 Fachlicher Kontext

[Beschreibe Nutzergruppen, Nachbarsysteme, fachliche Datenflüsse und Kommunikationsbeziehungen.]

### 3.2 Technischer Kontext

[Beschreibe technische Schnittstellen, Protokolle, Authentifizierung, Autorisierung, Datenformate, Netz- und Betriebsgrenzen.]

## 4. Lösungsstrategie

[Verdichte die wichtigsten Architekturleitentscheidungen: Integrationsstil, IAM-Ansatz, Datenverantwortung, Plattformstrategie, Betriebsstrategie, Sicherheitsstrategie.]

## 5. Bausteinsicht

[Beschreibe die wesentlichen Architekturbausteine, ihre Verantwortlichkeiten, Schnittstellen und Abhängigkeiten. Beginne mit einer groben Ebene und verfeinere nur dort, wo Entscheidungen, Risiken oder Übergaben davon abhängen.]

## 6. Laufzeitsicht

[Beschreibe die wichtigsten Abläufe als Szenarien: Normalfall, Ausnahmefall, Fehlerfall, Betriebsfall. Mindestens: Antrag einreichen, Registerabfrage, Dokumentablage, Bescheiderstellung, Fehlerbehandlung.]

## 7. Verteilungssicht

[Beschreibe Umgebungen, Plattformen, Netzzonen, technische Knoten, Deployment, Datenhaltung, Backup, Monitoring, Betriebsverantwortung und externe Abhängigkeiten.]

## 8. Querschnittskonzepte

[Dokumentiere IAM, Rollen/Rechte, Logging, Monitoring, Datenschutz, Fehlerbehandlung, Schnittstellenstandard, Datenhaltung, Archivierung, Löschung, Konfiguration, Secrets, Backup/Restore und Betriebsübergabe.]

## 9. Architekturentscheidungen

[Verweise auf ADRs oder dokumentiere zentrale Entscheidungen mit Kontext, Optionen, Entscheidung, Begründung, Konsequenzen, Owner, Datum und Review-Zeitpunkt.]

## 10. Qualitätsanforderungen

[Formuliere Qualitätsszenarien mit Auslöser, Situation, erwarteter Reaktion und messbarem Akzeptanzkriterium.]

## 11. Risiken und technische Schulden

[Dokumentiere Risiken und technische Schulden priorisiert nach Auswirkung, Eintrittswahrscheinlichkeit, Maßnahme, Owner und Zieltermin.]

## 12. Glossar

[Definiere zentrale Fach- und Technikbegriffe eindeutig.]
:::

## 5. So füllst du die arc42-Kapitel richtig aus

### 5.1 Einführung und Ziele: Beginne nicht mit Technik, sondern mit Architekturauftrag

Dieses Kapitel beantwortet: Warum existiert das System, wer braucht es, was muss es besonders gut können? Im Behördenkontext ist das ein Führungsabschnitt. Er muss kurz genug für Führung und klar genug für Umsetzung sein. Gute Qualitätsziele sind nicht „modern“, „sicher“ oder „skalierbar“, sondern prüfbar. Besser ist: „Die Sachbearbeitung kann einen eingereichten Antrag inklusive Registerstatus, Nachweisen, Bearbeitungsstand und Aktenreferenz innerhalb eines Vorgangsbilds nachvollziehen.“ Noch besser wird es, wenn du Messbarkeit ergänzt: „Statusänderungen werden innerhalb von 60 Sekunden im Vorgang sichtbar; technische Fehler sind über Korrelations-ID nachvollziehbar.“

Typischer Fehler: In Kapitel 1 werden alle Features gelistet. Korrektur: Funktionen gehören in Fachkonzept oder Requirements; arc42 Kapitel 1 enthält Zweck, Stakeholder und Qualitätsziele.

### 5.2 Randbedingungen: Hier steht, was nicht frei verhandelbar ist

Randbedingungen sind keine Wünsche. Sie sind Begrenzungen des Lösungsraums. In Bundesbehörden gehören dazu insbesondere gesetzliche Vorgaben, Datenschutz, BSI-orientierte Sicherheitsanforderungen, bestehende Plattformen, Netzzonen, IAM-Vorgaben, DMS/eAkte-Vorgaben, Vergabe- und Vertragsgrenzen, bestehende Fachverfahren, Migrationsfenster, Betriebszeiten und Dienstleisterzuständigkeiten. Der BSI-Standard 200-2 bildet die Grundlage für den Aufbau eines Informationssicherheitsmanagements, und die Schutzbedarfsfeststellung fragt danach, welcher Schaden entstehen kann, wenn Vertraulichkeit, Integrität oder Verfügbarkeit eines Zielobjekts beeinträchtigt werden. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-200-2-IT-Grundschutz-Methodik/bsi-standard-200-2-it-grundschutz-methodik_node.html?utm_source=chatgpt.com))

Typischer Fehler: Randbedingungen werden als „Anforderungen“ verstreut. Korrektur: Alles, was Architekturentscheidungen begrenzt, kommt sichtbar in Kapitel 2. Dadurch versteht ein Gremium später, warum bestimmte Optionen nicht gewählt wurden.

### 5.3 Kontextabgrenzung: Die wichtigste Sicht für Fachseite und Integration

Kontextabgrenzung ist die Antwort auf: Was ist innen, was ist außen, und über welche fachlichen oder technischen Beziehungen kommuniziert das System? Im Beispiel gehören Bürgerportal, Sachbearbeitung, Fachaufsicht, zentrales IAM, Register, DMS/eAkte, Zahlungsdienst, Benachrichtigungsdienst und Monitoring in den Kontext. Wichtig: Nicht alles ist Baustein deines Systems. Ein Register ist meist Nachbarsystem. Ein zentrales IAM ist meistens Plattform- oder Querschnittsdienst. Das Fachverfahren ist dein Systemkern.

Für Behörden solltest du die Kontextabgrenzung immer zweifach führen: fachlich und technisch. Fachlich beschreibst du Akteure, Datenobjekte und Verwaltungsbeziehungen. Technisch beschreibst du Protokolle, Authentifizierung, Autorisierung, Datenformate, Netzgrenzen und Betriebszuständigkeiten.

### 5.4 Lösungsstrategie: Die Architektur in zehn Sätzen

Die Lösungsstrategie ist nicht die gesamte Architektur. Sie ist die Verdichtung der wichtigsten Leitentscheidungen. Für unser Beispiel könnte sie so lauten: Das Fachverfahren wird als zentraler Vorgangsführer aufgebaut. Externe Kommunikation erfolgt über ein API-Gateway. Authentifizierung und Single Sign-on erfolgen über das zentrale IAM. Registerabfragen werden über einen fachlich gekapselten Registeradapter ausgeführt. Dokumente und Bescheide werden nicht in der Fachverfahrensdatenbank archiviert, sondern revisionsfähig an DMS/eAkte übergeben. Das Fachverfahren speichert fachliche Bearbeitungsstände, technische Korrelations-IDs und Verweise auf Aktenobjekte. Monitoring, Logging und Fehlerbehandlung werden als Querschnittskonzepte verbindlich umgesetzt.

Das ist gremiumstauglich, weil man darüber entscheiden kann. Es ist auch dienstleisterfähig, weil daraus konkrete Liefergegenstände entstehen.

### 5.5 Bausteinsicht: Verantwortlichkeiten statt Kästchenmalerei

Die Bausteinsicht muss nicht hübsch sein; sie muss trennscharf sein. Jeder Baustein braucht eine Verantwortung. Portal zeigt Eingaben und Status. API-Gateway bündelt externe API-Zugriffe und technische Sicherheitsfunktionen. Fachverfahren orchestriert Vorgänge. Registeradapter kapselt Registerlogik. DMS-Adapter kapselt Aktenablage. Datenbank hält Vorgangs- und Bearbeitungsdaten. Monitoring sammelt technische und fachliche Betriebsereignisse. IAM verwaltet Identitäten, Rollen und Token.

Die beste Prüffrage lautet: Kann ich für jeden Baustein sagen, welche Daten er erzeugt, liest, verändert, weitergibt und verantwortet? Wenn nicht, ist die Bausteinsicht noch zu dekorativ.

### 5.6 Laufzeitsicht: Hier erkennt man, ob die Architektur wirklich funktioniert

Die Laufzeitsicht zeigt Verhalten. Behördenarchitektur scheitert selten daran, dass ein Systemdiagramm fehlt. Sie scheitert daran, dass Fehlerfälle, Ersatzprozesse, Abhängigkeiten und Statusübergänge nicht beschrieben sind. Deshalb brauchst du für unser Beispiel mindestens diese Laufzeitszenarien: Antrag einreichen, Registerabfrage erfolgreich, Register nicht erreichbar, Nachweis hochladen, Dokument an DMS/eAkte übergeben, Bescheid erzeugen, Bescheid zustellen, Sachbearbeitung korrigiert Daten, technischer Fehler wird protokolliert und über Korrelations-ID nachverfolgt.

Gute Laufzeitsichten enthalten nicht nur Happy Path. Sie zeigen Timeouts, Retry, fachliche Wartestatus, technische Fehlerobjekte, manuelle Klärung und Monitoring-Signale.

### 5.7 Verteilungssicht: Betrieb ist Architektur, nicht Nacharbeit

In der Verteilungssicht beschreibst du Umgebungen, Netzzonen, Plattformen, technische Knoten, Datenbanken, Secrets, Zertifikate, Monitoring, Logging, Backup, Restore und Betriebsverantwortung. Für Bundesbehörden ist dieses Kapitel besonders wichtig, weil Schutzbedarf, Mandantentrennung, Dienstleisterzugriffe und Betriebsübergabe dort konkret werden.

Eine brauchbare Verteilungssicht beantwortet: Wo läuft was? Wer betreibt was? Welche Zone darf mit welcher Zone sprechen? Wo liegen Daten? Wie wird deployt? Wie wird überwacht? Wie wird wiederhergestellt? Welche Komponenten sind kritisch für Verfügbarkeit? Welche externen Dienste sind Single Points of Failure?

### 5.8 Querschnittskonzepte: Der Ort für Architekturdisziplin

Querschnittskonzepte sind die Kapitel, in denen professionelle Architektur sichtbar wird. Hier gehören IAM, Rollenmodell, Berechtigungsprüfung, Logging, Monitoring, Fehlerbehandlung, Schnittstellenkonventionen, Datenklassifikation, Verschlüsselung, Konfiguration, Secrets, Datenschutz, Löschung, Archivierung, Auditierbarkeit, Observability und Betriebsübergabe hinein. arc42 beschreibt Querschnittskonzepte als übergreifende Regeln und Lösungsansätze, die mehrere Bausteine betreffen. ([arc42.org](https://arc42.org/overview))

Für dich als Enterprise Architekt ist dieses Kapitel ein Hebel: Hier formulierst du Standards, die nicht nur für eine Komponente gelten. Wenn du etwa sagst, „jede externe Schnittstelle muss Korrelations-ID, strukturierte Fehlercodes, Authentifizierungsverfahren, Autorisierung, Monitoring-Metriken und fachliche Owner enthalten“, dann machst du Architektur steuerbar.

## 6. Beispielkapitel für das Fachverfahren

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Kapitel 1: Einführung und Ziele | Dieses Kapitel beschreibt Zweck, Stakeholder und Top-Qualitätsziele. | „Das digitale Leistungs- und Bescheidverfahren unterstützt die elektronische Antragstellung, die sachbearbeitende Prüfung, Registerabfragen, Dokumentenablage, Bescheiderstellung und Statuskommunikation. Ziel ist eine nachvollziehbare, medienbrucharme und betriebsfähige Vorgangsbearbeitung. Die Architektur priorisiert Nachvollziehbarkeit, Schutzbedarfserfüllung, Änderbarkeit, Betriebsfähigkeit und klare Datenverantwortung.“ | arc42 Kapitel 1 umfasst Anforderungen, Stakeholder und Top-Qualitätsziele. ([arc42.org](https://arc42.org/overview)) |
| Kapitel 3: Kontextabgrenzung | Dieses Kapitel trennt System und Nachbarsysteme. | „Das Fachverfahren wird von Antragstellenden über das Portal und von Sachbearbeitenden über die interne Oberfläche genutzt. Es kommuniziert mit IAM zur Authentifizierung, mit Registern zur Datenprüfung, mit DMS/eAkte zur Dokumentenablage, mit einem Benachrichtigungsdienst zur Statuskommunikation und mit Monitoring/Logging zur Betriebsüberwachung.“ | arc42 beschreibt hier externe Kommunikationspartner und Schnittstellen. ([arc42.org](https://arc42.org/overview)) |
| Kapitel 4: Lösungsstrategie | Dieses Kapitel fasst die tragenden Architekturentscheidungen zusammen. | „Die Lösung trennt fachliche Vorgangsführung, Dokumentenablage und Identitätsmanagement. Das Fachverfahren ist führend für Vorgangsstatus und Bearbeitungsdaten. DMS/eAkte ist führend für abgelegte Dokumente und Aktenreferenzen. IAM ist führend für Identitäten und Rollen. Integrationen erfolgen über definierte Schnittstellen mit Fehlerobjekten, Korrelations-ID und Monitoring.“ | arc42 Kapitel 4 umfasst grundlegende Entscheidungen und Lösungsansätze. ([arc42.org](https://arc42.org/overview)) |
| Kapitel 6: Laufzeitsicht | Dieses Kapitel beschreibt kritische Abläufe. | „Beim Eingang eines Antrags validiert das Portal die Eingaben, übergibt den Antrag über das API-Gateway an das Fachverfahren, das einen Vorgang erzeugt, eine Registerprüfung anstößt, den Status setzt und ein Ereignis für Monitoring und Sachbearbeitung schreibt. Ist das Register nicht erreichbar, wird der Vorgang nicht verworfen, sondern in den Status ‚Registerprüfung ausstehend‘ gesetzt.“ | arc42 Kapitel 6 beschreibt Szenarien, Schnittstelleninteraktionen und Fehlerverhalten. ([arc42.org](https://arc42.org/overview)) |
| Kapitel 10: Qualitätsanforderungen | Dieses Kapitel macht Qualität prüfbar. | „Wenn eine Registerabfrage im Regelbetrieb länger als 10 Sekunden dauert, muss das Fachverfahren einen technischen Timeout protokollieren, den Vorgang fachlich wartend markieren und der Sachbearbeitung eine verständliche Statusinformation anzeigen. Akzeptanzkriterium: Fehler ist über Korrelations-ID in Monitoring und Fachverfahren nachvollziehbar.“ | Das arc42-Qualitätsmodell arbeitet mit messbaren Anforderungen inklusive Kontext, Triggern und Akzeptanzkriterien. ([quality.arc42.org](https://quality.arc42.org/requirements/)) |
| Kapitel 11: Risiken und technische Schulden | Dieses Kapitel macht bekannte Schwächen steuerbar. | „Risiko: Die fachliche Datenverantwortung zwischen Fachverfahren und DMS/eAkte ist für Aktenmetadaten nicht entschieden. Auswirkung: widersprüchliche Statusinformationen, fehlerhafte Recherche und Streit in Betriebsfällen. Maßnahme: Data-Owner-Entscheidung im Architekturboard, Schnittstellenvertrag aktualisieren, Testfall in Abnahme aufnehmen.“ | arc42 empfiehlt Risiken und technische Schulden priorisiert inklusive Maßnahmen zu führen. ([docs.arc42.org](https://docs.arc42.org/section-11/)) |

## 7. Behörden-taugliche Qualitätskriterien für arc42-Dokumente

Ein gutes arc42-Dokument ist nicht daran erkennbar, dass alle Kapitel lang sind. Es ist daran erkennbar, dass es Entscheidungen ermöglicht, Risiken sichtbar macht, Übergaben erleichtert und Architektur überprüfbar macht.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Zweckklarheit | Das Dokument sagt, wofür es verwendet wird: Review, Zielbild, Ausschreibung, Betrieb, Abnahme oder Übergabe. | „Dieses Dokument dient als Review- und Abnahmegrundlage für Release 1.0.“ | arc42 versteht sich als Kommunikations- und Dokumentationsvorlage. ([arc42.org](https://arc42.org/overview)) |
| Stakeholder-Tauglichkeit | Fachseite, IT, Security und Betrieb finden ihre relevanten Informationen. | Fachseite liest Kontext und Ziele; Betrieb liest Verteilungssicht und Betriebsmodell; Security liest Schutzbedarf, IAM und Logging. | arc42 Kapitel 1 enthält Stakeholder und Erwartungen. ([arc42.org](https://arc42.org/overview)) |
| Kontextschärfe | Systemgrenzen, Nachbarsysteme und Schnittstellen sind eindeutig. | Register ist Nachbarsystem, nicht interner Baustein. IAM ist zentraler Querschnittsdienst. | arc42 Kapitel 3 fordert Abgrenzung gegenüber externen Kommunikationspartnern. ([arc42.org](https://arc42.org/overview)) |
| Entscheidbarkeit | Architekturentscheidungen sind mit Alternativen, Begründung und Konsequenzen dokumentiert. | „Zentrales IAM statt lokaler Nutzerverwaltung, weil Rollenrezertifizierung und SSO behördenweit gefordert sind.“ | arc42 Kapitel 9 adressiert wichtige, kritische oder riskante Architekturentscheidungen. ([arc42.org](https://arc42.org/overview)) |
| Prüfbarkeit | Qualitätsanforderungen sind als Szenarien formuliert. | „Bei DMS-Ausfall wird der Bescheid nicht als zugestellt markiert; erneute Übergabe erfolgt kontrolliert.“ | Das arc42-Qualitätsmodell empfiehlt messbare Anforderungen mit Trigger und Akzeptanzkriterien. ([quality.arc42.org](https://quality.arc42.org/requirements/)) |
| Betriebsfähigkeit | Deployment, Monitoring, Logging, Backup, Restore und Verantwortlichkeiten sind beschrieben. | „Restore-Test quartalsweise; RPO 15 Minuten für Vorgangsdaten; Runbook für Registerausfall.“ | arc42 Kapitel 7 beschreibt Infrastruktur und Deployment; Kapitel 8 Querschnittskonzepte. ([arc42.org](https://arc42.org/overview)) |
| Sicherheitsanschlussfähigkeit | Schutzbedarf, IAM, Protokollierung, Berechtigungen und Dienstleisterzugriffe sind anschlussfähig an Security-Reviews. | „Schutzbedarf hoch für Vertraulichkeit; rollenbasierte Sachbearbeitungsrechte; technische Konten rezertifiziert.“ | BSI-Grundschutz arbeitet mit Schutzbedarf entlang Vertraulichkeit, Integrität und Verfügbarkeit. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Aktualität | Dokument hat Owner, Status, Review-Zeitpunkt und Änderungsverlauf. | „Review bei jeder wesentlichen Schnittstellenänderung oder vor Produktivsetzung.“ | arc42 bietet eine strukturierte Dokumentationsvorlage; Governance ergänzt Owner und Lebenszyklus. ([arc42.org](https://arc42.org/overview)) |
| Risikotransparenz | Risiken stehen nicht im Fließtext versteckt, sondern priorisiert mit Maßnahmen. | „Register-SLA unklar; Maßnahme: SLA-Klärung vor Abnahme.“ | arc42 Kapitel 11 fordert priorisierte Risiken und technische Schulden. ([docs.arc42.org](https://docs.arc42.org/section-11/)) |
| Anschluss an Liefersteuerung | Architekturkapitel führen zu Liefergegenständen und Abnahmekriterien. | OpenAPI-Spezifikation, IAM-Rollenkonzept, Deployment-Diagramm, Runbook, ADR-Log. | arc42 beantwortet, was und wie über Architektur kommuniziert werden soll. ([arc42.org](https://arc42.org/overview)) |

## 8. Typische Dokumentationsfehler und klare Korrektur

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Kapitel werden ausgefüllt, aber nicht genutzt | Das Dokument existiert formal, steuert aber keine Entscheidung. | 80 Seiten, aber kein Architekturboard kann daraus eine Freigabe ableiten. | arc42 ist ausdrücklich Kommunikations- und Dokumentationsvorlage, nicht nur Ablageform. ([arc42.org](https://arc42.org/overview)) |
| Kontext und Bausteine werden vermischt | Nachbarsysteme erscheinen als interne Module. | Register wird als interner Baustein modelliert, obwohl es extern betrieben wird. | arc42 trennt Kontextabgrenzung und Bausteinsicht. ([arc42.org](https://arc42.org/overview)) |
| Qualitätsziele bleiben abstrakt | Begriffe wie „sicher“, „performant“, „modern“ sind nicht prüfbar. | „Das System muss stabil sein.“ | arc42 Quality arbeitet mit Szenarien und messbaren Akzeptanzkriterien. ([quality.arc42.org](https://quality.arc42.org/requirements/)) |
| Laufzeitsicht zeigt nur Happy Path | Fehler, Timeouts, Retries und Ersatzprozesse fehlen. | DMS-Ausfall ist nicht beschrieben. | arc42 Kapitel 6 umfasst auch Fehler- und Ausnahmeverhalten. ([arc42.org](https://arc42.org/overview)) |
| Querschnittskonzepte fehlen | IAM, Logging, Monitoring und Fehlerbehandlung werden je Baustein uneinheitlich gelöst. | Jeder Dienst definiert eigene Fehlercodes. | arc42 Kapitel 8 adressiert wiederkehrende bausteinübergreifende Lösungskonzepte. ([arc42.org](https://arc42.org/overview)) |
| Entscheidungen verschwinden im Text | Niemand erkennt später, warum eine Lösung gewählt wurde. | „Wir nutzen REST“, aber ohne Alternativen und Konsequenzen. | arc42 Kapitel 9 dokumentiert wichtige Architekturentscheidungen mit Begründung. ([arc42.org](https://arc42.org/overview)) |
| Risiken werden beschönigt | Dokument wirkt sauber, aber reale Unsicherheiten bleiben unsichtbar. | Register-SLA unbekannt, aber kein Risiko eingetragen. | arc42 Kapitel 11 fordert bekannte Risiken und technische Schulden mit Maßnahmen. ([docs.arc42.org](https://docs.arc42.org/section-11/)) |
| Betrieb wird nachgelagert | Verteilungssicht enthält nur Servernamen, aber keine Betriebsfähigkeit. | Kein Restore-Test, kein Runbook, kein Monitoring-Signal. | arc42 Kapitel 7 und 8 decken Infrastruktur, Deployment und Querschnittskonzepte ab. ([arc42.org](https://arc42.org/overview)) |
| Glossar fehlt | Fachseite und IT verwenden gleiche Begriffe unterschiedlich. | „Fall“, „Vorgang“, „Akte“ und „Antrag“ werden vermischt. | arc42 Kapitel 12 dient der Definition wichtiger Fach- und Technikbegriffe. ([arc42.org](https://arc42.org/overview)) |
| Dokument ist nicht versioniert | Niemand weiß, ob es noch gilt. | Architekturstand passt nicht zum produktiven Release. | arc42 liefert Struktur; für Behörden muss Dokumentsteuerung ergänzt werden. ([arc42.org](https://arc42.org/overview)) |

## 9. Konkrete Arbeitsmethode: So erstellst du ein arc42-Architekturpaket realistisch

Starte nicht mit dem leeren Dokument. Starte mit einem 90-minütigen Architektur-Kickoff. In diesem Termin klärst du Zweck, Systemgrenze, wichtigste Stakeholder, Top-Qualitätsziele, bekannte Randbedingungen, kritische Schnittstellen und bekannte Risiken. Danach erstellst du eine erste Version mit maximal zehn Seiten. Diese Version ist kein Enddokument, sondern ein Diskussionsanker.

Im zweiten Schritt führst du drei fokussierte Interviews. Mit der Fachseite klärst du Verwaltungsprozess, Datenobjekte, fachliche Status, Ausnahmen und Verantwortlichkeiten. Mit IT/Solution klärst du Bausteine, Schnittstellen, Datenhaltung, Integrationsmuster und Abhängigkeiten. Mit Security/Betrieb klärst du Schutzbedarf, IAM, Protokollierung, Monitoring, Backup, Wiederanlauf, Dienstleisterzugriffe und Betriebsmodell. Die Ergebnisse wandern nicht ungefiltert in arc42; du verdichtest sie in die passenden Kapitel.

Im dritten Schritt baust du drei zentrale Diagramme: Kontextdiagramm, Bausteindiagramm und mindestens ein Laufzeitszenario. Mehr Diagramme sind nur sinnvoll, wenn sie eine Entscheidung oder ein Risiko erklären. Ein Diagramm ohne Aussage ist Dekoration.

Im vierten Schritt formulierst du Architekturentscheidungen als ADRs. Mindestens dokumentierst du Entscheidungen zu IAM, Datenverantwortung, Integrationsstil, DMS/eAkte-Anbindung, Registerintegration, Betriebsmodell und Observability.

Im fünften Schritt führst du ein Architekturreview durch. Dabei gehst du nicht Kapitel für Kapitel formal durch, sondern prüfst entlang von Reviewfragen: Ist die Systemgrenze klar? Sind die führenden Systeme je Datenobjekt klar? Sind kritische Laufzeitfehler beschrieben? Sind Sicherheits- und Betriebsanforderungen prüfbar? Sind Risiken priorisiert? Sind offene Entscheidungen sichtbar?

Im sechsten Schritt machst du daraus ein Architekturpaket. Dieses Paket besteht aus arc42-Dokument, Kontextdiagramm, Bausteinsicht, Laufzeitsichten, Schnittstellenübersicht, ADR-Log, Risiko- und Schuldenliste, Qualitätsanforderungen, Glossar und Reviewprotokoll. Genau damit kannst du Fachseite, IT, Security, Betrieb und Dienstleister gemeinsam steuerbar machen.

## 10. Mini-arc42-Übung für dich

Deine Übung ist bewusst praxisnah: Du erstellst ein Mini-arc42-Dokument für ein fiktives Fachverfahren „Digitale Antragstellung für Förderleistungen“. Es umfasst Portal, Fachverfahren, Registerschnittstelle, DMS/eAkte, IAM, API-Gateway, Datenbank, Monitoring und Betriebsmodell.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Aufgabe 1: Einführung und Ziele | Formuliere Zweck, drei Stakeholder und fünf Top-Qualitätsziele. | Stakeholder: Antragstellende, Sachbearbeitung, Betrieb. Qualitätsziel: nachvollziehbarer Vorgangsstatus. | arc42 Kapitel 1 umfasst Zweck, Stakeholder und Qualitätsziele. ([arc42.org](https://arc42.org/overview)) |
| Aufgabe 2: Randbedingungen | Liste mindestens zehn Randbedingungen. | BSI-orientierter Schutzbedarf, zentrales IAM, DMS-Vorgabe, bestehendes Register, Betriebszeiten. | arc42 Kapitel 2 adressiert regulatorische, technische und organisatorische Randbedingungen. ([arc42.org](https://arc42.org/overview)) |
| Aufgabe 3: Kontextabgrenzung | Beschreibe fachlichen und technischen Kontext in Textform. | Portal nutzt API-Gateway; Fachverfahren ruft Register ab; DMS speichert Nachweise und Bescheide. | arc42 Kapitel 3 beschreibt externe Kommunikationspartner und Schnittstellen. ([arc42.org](https://arc42.org/overview)) |
| Aufgabe 4: Lösungsstrategie | Schreibe zehn Sätze zu den wichtigsten Architekturentscheidungen. | „Das Fachverfahren ist führend für Vorgangsstatus; DMS/eAkte ist führend für Aktenobjekte.“ | arc42 Kapitel 4 umfasst grundlegende Entscheidungen und Lösungsansätze. ([arc42.org](https://arc42.org/overview)) |
| Aufgabe 5: Bausteinsicht | Definiere acht Bausteine mit Verantwortung. | Registeradapter kapselt Registerlogik und Fehlerbehandlung. | arc42 Kapitel 5 beschreibt statische Zerlegung in Bausteine. ([arc42.org](https://arc42.org/overview)) |
| Aufgabe 6: Laufzeitsicht | Beschreibe drei Abläufe: Normalfall, Registerausfall, DMS-Ausfall. | Bei DMS-Ausfall wird Bescheid nicht als abgelegt markiert. | arc42 Kapitel 6 umfasst Szenarien und Fehlerverhalten. ([arc42.org](https://arc42.org/overview)) |
| Aufgabe 7: Querschnittskonzepte | Beschreibe IAM, Logging, Fehlerbehandlung, Monitoring und Datenlöschung. | Jede Transaktion erhält Korrelations-ID; fachliche Fehler sind von technischen Fehlern getrennt. | arc42 Kapitel 8 adressiert bausteinübergreifende Konzepte. ([arc42.org](https://arc42.org/overview)) |
| Aufgabe 8: Qualitätsanforderungen | Formuliere fünf Qualitätsszenarien mit Trigger und Akzeptanzkriterium. | Trigger: Register nicht erreichbar. Reaktion: Wartestatus, Protokollierung, Retry-Konzept. | arc42 Quality empfiehlt messbare Anforderungen mit Kontext, Trigger und Akzeptanzkriterien. ([quality.arc42.org](https://quality.arc42.org/requirements/)) |
| Aufgabe 9: Risiken | Erfasse fünf Risiken mit Maßnahme, Owner und Termin. | „Datenverantwortung für Aktenmetadaten ungeklärt.“ | arc42 Kapitel 11 empfiehlt priorisierte Risiken und technische Schulden mit Maßnahmen. ([docs.arc42.org](https://docs.arc42.org/section-11/)) |
| Aufgabe 10: Executive Summary | Verdichte die Architektur auf eine Seite für ein Gremium. | Zweck, Zielbild, Risiken, Entscheidungen, benötigte Beschlüsse. | arc42 dient Architekturkommunikation; Behördenkontext erfordert entscheidungsfähige Verdichtung. ([arc42.org](https://arc42.org/overview)) |

## 11. Bewertung deines Mini-arc42-Dokuments

Dein Mini-arc42 ist gut, wenn ein fachlicher Entscheider danach versteht, wofür das Verfahren gebaut wird, ein Security-Reviewer Schutzbedarf und Kontrollpunkte erkennt, ein Betriebsverantwortlicher Betriebsanforderungen ableiten kann, ein Dienstleister konkrete Liefergegenstände sieht und ein Architekturboard offene Entscheidungen sauber beschließen kann.

Die harte Prüffrage lautet: Kann jemand, der nicht im Projekt war, nach 30 Minuten Lektüre die Architektur erklären, die drei größten Risiken benennen, die wichtigsten Entscheidungen nachvollziehen und die nächsten offenen Punkte erkennen? Wenn nein, ist das Dokument noch nicht fertig. Nicht, weil es zu kurz ist, sondern weil es seinen Zweck noch nicht erfüllt.

## 12. Executive-Formulierungen für Gremien

Für eine Gremiumsvorstellung solltest du nicht sagen: „Wir haben arc42 ausgefüllt.“ Das klingt nach Dokumentationspflicht. Besser ist: „Wir haben die Architektur entlang einer standardisierten Struktur so dokumentiert, dass fachlicher Zweck, Systemgrenzen, Integrationen, Betriebsfähigkeit, Sicherheitsanforderungen, Entscheidungen und Risiken nachvollziehbar sind.“

Noch stärker: „Das Architekturpaket dient als gemeinsame Entscheidungs- und Steuerungsgrundlage für Fachseite, IT, Security, Betrieb und Dienstleister. Offene Architekturentscheidungen und Risiken sind explizit ausgewiesen und mit Maßnahmen hinterlegt.“

Und für Dienstleistersteuerung: „Die arc42-Struktur wird als verbindlicher Rahmen für die Architekturübergabe verwendet. Liefergegenstände sind Kontextabgrenzung, Bausteinsicht, Laufzeitszenarien, Verteilungssicht, Querschnittskonzepte, ADRs, Qualitätsanforderungen, Risiken und Glossar.“

## 13. Dein nächster konkreter Schritt

Nimm ein echtes oder fiktives Fachverfahren und schreibe nur diese fünf Artefakte: eine halbe Seite Einführung und Ziele, eine Kontextabgrenzung mit zehn Nachbarsystemen/Akteuren, eine Lösungsstrategie in zehn Sätzen, eine Bausteinliste mit Verantwortlichkeiten und drei Laufzeitszenarien. Danach prüfst du, welche Querschnittskonzepte und ADRs fehlen. Genau so wächst aus arc42 keine Dokumentationslast, sondern ein belastbares Architekturpaket.