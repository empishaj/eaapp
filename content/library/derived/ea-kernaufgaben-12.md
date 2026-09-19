# 12 Kernaufgaben eines Enterprise Architects im Behördenkontext

Diese Darstellung behandelt den Enterprise Architect bewusst als **externen Dienstleister**. Der EA erhebt, analysiert, strukturiert, visualisiert, bewertet, entwickelt Optionen, spricht Empfehlungen aus und bereitet Entscheidungen vor. Die fachliche, organisatorische und hoheitliche Entscheidung bleibt bei den zuständigen Rollen der Behörde.

## 1. Architekturauftrag und Scope klären

**Behördenbeispiel:** Eine Bundesbehörde beauftragt Unterstützung für die „Zielarchitektur eines Fachverfahrens“. Der Auftrag ist zu unscharf. Der EA führt Gespräche mit Sponsor, Fachverantwortung, IT, Programmleitung und vorhandener Architekturorganisation und klärt Problem, Scope, Nicht-Scope, Entscheidungsrechte, Gremien, verbindliche Standards und Liefergegenstände.

**Typische Fragen:** Welche Entscheidung soll vorbereitet werden? Welche Organisationseinheiten und Verfahren sind betroffen? Welche Systeme liegen im Scope? Welche Vorgaben gelten? Welche Rolle hat der externe Dienstleister? Wer entscheidet Ausnahmen?

**Artefakte:** Mandatssteckbrief, Architecture Working Agreement, Stakeholder- und Gremienlandkarte.

**Dienstleistergrenze:** Nicht „Ich entscheide die Architektur“, sondern „Ich bereite die Entscheidung belastbar vor und dokumentiere Konsequenzen.“

## 2. Ist-Architektur verstehen

**Behördenbeispiel:** Ein historisch gewachsener Verwaltungsprozess nutzt mehrere Fachverfahren, Excel-Auswertungen, DMS, Registerabfragen, Dateitransfers und externe Dienstleister. Niemand besitzt ein konsistentes Gesamtbild.

Der EA untersucht Fähigkeiten, Prozesse, Datenobjekte, Anwendungen, Schnittstellen, Betreiber, Abhängigkeiten, technische Schulden und Medienbrüche. Interviews werden mit Fachbearbeitung, Systemverantwortlichen, Betrieb, Informationssicherheit, Datenschutz und Lieferanten geführt.

**Beispielhafte Erkenntnis:** System A erzeugt den Vorgang, System B führt Dokumente, System C erzeugt Reporting; für offene Rückmeldungen existiert zusätzlich eine Excel-Liste; Statusinformationen widersprechen sich.

**Artefakte:** Capability Map, Systemlandkarte, Datenlandkarte, Schnittstellenkatalog, Risiko- und Pain-Point-Liste.

**EA-Mehrwert:** Nicht nur „17 Systeme existieren“, sondern „diese fünf Abhängigkeiten erzeugen den größten fachlichen und technischen Handlungsdruck“.

## 3. Zielarchitektur entwickeln

**Behördenbeispiel:** Ein Modernisierungsvorhaben besitzt viele technische Maßnahmen, aber kein konsistentes Zielbild. Der EA verbindet fachliche Ziele mit Daten, Anwendungen, Integration, IAM, DMS/eAkte, Plattform, Betrieb und Governance.

Ein mögliches Zielbild enthält klare Domänengrenzen, eindeutige Datenführerschaft, standardisierte Schnittstellen, zentrale Identitätsdienste, nachvollziehbare Protokollierung, definierte Betriebsverantwortung und eine tragfähige Plattformstrategie.

**Artefakte:** Architecture Vision, Target Architecture, ArchiMate-Sichten, Ziel-Datenlandkarte, Ziel-Systemlandkarte, Prinzipien und Gap-Matrix.

**Dienstleistergrenze:** Das Zielbild wird gemeinsam erarbeitet. Offene Entscheidungen werden sichtbar gemacht und der zuständigen internen Instanz zur Entscheidung vorgelegt.

## 4. Architekturentscheidungen vorbereiten

**Behördenbeispiel:** Zwei Fachverfahren sollen künftig Daten austauschen. Zur Wahl stehen synchrone REST-API, asynchrones Messaging oder ein bestehender Batch-Prozess.

Der EA beschreibt Kontext und fachliche Treiber, vergleicht Alternativen anhand von Aktualität, Kopplung, Komplexität, Security, Betrieb, Fehlerverhalten, Kosten und vorhandenen Fähigkeiten und formuliert anschließend eine Empfehlung.

**Artefakte:** Entscheidungsoptionen, Kriterienmatrix, ADR-Entwurf, Risikoanalyse.

**Arbeitsmuster:** Kontext → Optionen → Kriterien → Konsequenzen → Empfehlung → Entscheidung durch zuständige Stelle.

## 5. Architekturprinzipien und Standards definieren

**Behördenbeispiel:** Verschiedene Projekte lösen Integration unterschiedlich: REST, Dateien, direkte Datenbankzugriffe, Messaging. Statt jeden Einzelfall neu zu verhandeln, entwickelt der EA mit internen Architekten Leitplanken.

**Beispielprinzip:** „Datenzugriffe zwischen Fachverfahren erfolgen über definierte Schnittstellen; direkte Zugriffe auf fremde Datenbanken sind begründungspflichtige Ausnahmen.“

Ein gutes Prinzip enthält **Aussage, Begründung, Konsequenzen, Reviewfrage und Ausnahmeweg**.

**Weitere Beispiele:** zentrale Identitätsdienste, führende Datenquellen, standardisierte Schnittstellenverträge, Observability by Design, Security by Architecture, kontrollierte Punkt-zu-Punkt-Integrationen.

## 6. Datenführerschaft klären

**Behördenbeispiel:** Drei Systeme zeigen für denselben Vorgang unterschiedliche Statuswerte. Niemand kann eindeutig sagen, welcher Status verbindlich ist.

Der EA moderiert die Klärung: Wo entsteht der Status? Wer darf ihn verändern? Welche Fachhandlung löst den Wechsel aus? Welche Systeme konsumieren ihn? Wie werden Konflikte behandelt?

**Artefakte:** Datenobjektkatalog, Data-Ownership-Matrix, Source-of-Truth-/System-of-Record-Entscheidungen, Data Lineage.

**Kernfrage:** „Wer darf dieses Datum fachlich verbindlich ändern?“

**Mehrwert:** weniger Doppelpflege, widersprüchliches Reporting, manuelle Korrekturen und Schnittstellenkomplexität.

## 7. Systemrollen und Domänengrenzen klären

**Behördenbeispiel:** Ein Fachverfahren, ein DMS, ein Identitätsdienst und eine Reporting-Lösung übernehmen zunehmend überlappende Aufgaben. Das Reporting korrigiert operative Daten; das DMS besitzt eigene Statuslogik; das Fachverfahren speichert Dokumente zusätzlich selbst.

Der EA beschreibt Zielrollen, Verantwortungsgrenzen und erlaubte Interaktionen. Eine mögliche Regel lautet: „Reporting darf operative Daten auswerten, aber nicht eigenständig fachlich korrigieren.“

**Artefakte:** Systemrollenmatrix, Capability-to-Application-Mapping, Bounded-Context-/Domänensichten, Applikationsportfolio.

**Merksatz:** Das Problem ist nicht, dass mehrere Systeme eine Information kennen. Problematisch wird es, wenn mehrere Systeme glauben, sie fachlich führen zu dürfen.

## 8. Integrationsarchitektur gestalten

**Behördenbeispiel:** Die Behörde kommuniziert mit eigenen Fachverfahren, DMS/eAkte, Registern, Ländern, Kommunen, anderen Bundesbehörden und Dienstleistern.

Der EA ordnet Integrationsbedarfe nach fachlicher Semantik: synchrone Abfrage, Ereignismeldung, Batch, Dokumentenübergabe oder sicheres Gateway. Für kritische Integrationen werden Provider, Consumer, fachlicher Zweck, Datenobjekte, Authentifizierung, Autorisierung, Fehlerfall, Quittierung, Versionierung und Monitoring geklärt.

**Wichtig:** Eine Schnittstelle wird nicht nur als Endpoint beschrieben. Entscheidend ist die fachliche Übergabe und Verantwortung.

**Artefakte:** Integrationsprinzipien, Schnittstellenkatalog, Schnittstellenvertrag, Event-/API-Verträge, Fehlerfallmatrix.

## 9. Transformationsroadmap entwickeln

**Behördenbeispiel:** Eine Legacy-Anwendung kann nicht kurzfristig ersetzt werden. Ziel sind zentrale Identitäten, standardisierte Schnittstellen, klare Datenführerschaft, DMS-Integration und eine neue Plattform.

Der EA plant keine Big-Bang-Ablösung, sondern Übergangsarchitekturen: zunächst IAM standardisieren, dann Integrationen entkoppeln, Datenführerschaft bereinigen, DMS-Übergaben stabilisieren, neues Fachverfahren einführen und schließlich Legacy abbauen.

**Artefakte:** Baseline, Target, Gap Matrix, Transition Architectures, Work Packages, Dependency Map, Architecture Roadmap, Entscheidungsfenster.

**EA-Frage:** Nicht nur „Wann wird etwas umgesetzt?“, sondern „Welche Architekturabhängigkeit erzwingt welche Reihenfolge?“

## 10. Architektur-Governance etablieren

**Behördenbeispiel:** Projekte treffen Architekturentscheidungen dezentral und zentrale Probleme werden erst kurz vor Abnahme sichtbar.

Der EA schlägt eine leichte Review-Triage vor: lokale reversible Entscheidung im Team; systemübergreifende Daten-/Schnittstellenänderung im Architekturreview; strategische Abweichung mit ADR und zuständigem Gremium; Ausnahme mit Befristung und Kompensation.

**Artefakte:** Architecture Brief, Reviewprozess, ADR-Register, Ausnahmeformular, Maßnahmenregister, Architecture Situation Report.

**Dienstleistergrenze:** Governance muss Eigentum der Behörde bleiben. Der externe EA hilft, sie aufzubauen, moderiert Reviews und macht Entscheidungen nachvollziehbar.

## 11. Architekturrisiken sichtbar machen

**Behördenbeispiel:** Mehrere Systeme führen dieselben Daten; eine Schnittstelle hat keinen Owner; eine Technologie ist End-of-Life; Restore wurde nie getestet; kritisches Spezialwissen liegt ausschließlich beim Lieferanten.

Der EA übersetzt Beobachtungen in steuerbare Risiken: Ursache, fachliche Wirkung, Eintrittsszenario, betroffene Architekturdomänen, Gegenmaßnahme, Owner und Restrestrisiko.

**Artefakte:** Architecture Risk Register, Technical Debt Register, Heatmap, Decision Log.

**Professionelle Sprache:** Nicht „System X ist schlecht“, sondern „Entscheidung/Altlast X erzeugt Risiko Y; Maßnahme Z reduziert es unter den Bedingungen A und B.“

## 12. Architektur über Vorhaben hinweg synchronisieren

**Behördenbeispiel:** Ein Vorhaben modernisiert ein Fachverfahren, ein zweites führt eine Datenplattform ein, ein drittes modernisiert IAM und ein viertes baut eine neue Behörden-Schnittstelle. Jedes Vorhaben optimiert lokal, gemeinsam entstehen aber widersprüchliche Datenmodelle, Identitätslösungen und Integrationsmuster.

Der EA baut eine Vorhaben- und Abhängigkeitslandkarte und identifiziert gemeinsame Entscheidungen. Er moderiert die Klärung nicht als Kritik einzelner Projekte, sondern als Enterprise-Frage: „Mehrere Vorhaben hängen an derselben Architekturentscheidung; wenn sie separat entscheiden, entstehen widersprüchliche Lösungen.“

**Artefakte:** Portfolio-Landkarte, Capability-to-Initiative-Mapping, Dependency Matrix, Decision Roadmap, Zielarchitektur.

## Arbeitsformel für die Dienstleisterrolle

**Erheben → analysieren → strukturieren → visualisieren → Optionen entwickeln → Risiken und Konsequenzen erklären → Empfehlung aussprechen → Entscheidung vorbereiten → Entscheidung dokumentieren → Umsetzung architektonisch begleiten.**

Die Entscheidungshoheit bleibt bei der zuständigen Behörde.
