## Checkliste: ArchiMate in Behörden-EA praktisch beherrschen

1. **Zuerst die Stakeholderfrage klären:** Wer soll mit der Sicht welche Entscheidung treffen?  
2. **Nicht mit Symbolen beginnen, sondern mit Architekturfragen:** Fähigkeit, Prozess, Anwendung, Daten, Schnittstelle, Plattform, Migration.  
3. **Business, Application und Technology sauber trennen:** Facharbeit ist nicht Anwendung, Anwendung ist nicht Server, Server ist nicht Zielarchitektur.  
4. **Services konsequent nutzen:** Services zeigen, was ein Element nach außen leistet; Komponenten zeigen, wer oder was es leistet.  
5. **Flow nur für Austausch verwenden:** Daten-, Ereignis- oder Informationsflüsse sind keine „nutzt“-Beziehungen.  
6. **Serving für Abhängigkeit verwenden:** Ein Service dient einem Prozess, einer Anwendung oder einem anderen Element.  
7. **Realization für Umsetzung verwenden:** Eine Komponente realisiert einen Service; ein Work Package realisiert einen Liefergegenstand oder Zielzustand.  
8. **Data Object fachlich-digital modellieren:** Nicht jede Datenbanktabelle gehört in ArchiMate.  
9. **Plateau, Gap und Work Package für Transformation nutzen:** Ist-Zustand, Zielzustand, Lücke und Maßnahme müssen zusammen sichtbar werden.  
10. **Sichten klein halten:** Eine gute EA-Sicht beantwortet eine Frage, nicht alle Fragen gleichzeitig.  
11. **Capability-to-Technology als rote Linie beherrschen:** Von Fähigkeit über Prozess und Anwendung bis Infrastruktur muss Nachvollziehbarkeit entstehen.  
12. **ArchiMate nicht mit BPMN, UML oder Betriebsdokumentation verwechseln:** ArchiMate liefert Überblick, Abhängigkeit und Entscheidungsfähigkeit; Detailmodellierung gehört in passende Spezialnotationen.

## 1. Was ArchiMate für dich als Enterprise Architekt leisten soll

ArchiMate ist eine standardisierte Modellierungssprache für Enterprise Architecture. Der Kernnutzen liegt nicht darin, „schöne Kästchen“ zu malen, sondern fachliche, organisatorische, anwendungsbezogene, technische und transformationsbezogene Zusammenhänge in einer gemeinsamen Sprache darzustellen. The Open Group beschreibt ArchiMate als offene, unabhängige Modellierungssprache für Enterprise Architecture, mit der Beziehungen zwischen Geschäftsdomänen beschrieben, analysiert und visualisiert werden können. Die aktuell herangezogene Referenz ist ArchiMate 3.2. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com))

Für Bundesbehörden ist ArchiMate besonders wertvoll, weil Behördenarchitekturen selten nur technische Systeme sind. Meist geht es um Fachverfahren, Zuständigkeiten, gesetzliche Randbedingungen, Register, Aktenführung, Bescheide, Datenschutz, Betrieb, Dienstleistersteuerung, Migration und Gremienentscheidungen. Genau hier hilft ArchiMate: Es verbindet die Frage „Welche Fähigkeit braucht die Behörde?“ mit „Welcher Prozess nutzt welche Anwendung, welche Daten, welche Schnittstelle und welche Plattform?“

Wichtig ist eine fachliche Korrektur: ArchiMate ersetzt **nicht** BPMN. BPMN ist stärker, wenn du einen Prozessablauf mit Ereignissen, Gateways, Wartezeiten, Nachforderungen und Sonderfällen detailliert beschreiben willst. ArchiMate ist stärker, wenn du zeigen willst, wie dieser Prozess in eine Gesamtarchitektur eingebettet ist: welche Capability er unterstützt, welche Anwendungen beteiligt sind, welche Datenobjekte fließen, welche Plattformdienste gebraucht werden und welche Migrationslücken bestehen. Die Open-Group-Community beschreibt ArchiMate ebenfalls als Sprache für Überblick, Kommunikation und kohärente Architekturmodelle, während Detailphasen häufig Spezialsprachen wie BPMN oder UML benötigen. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/))

## 2. Das mentale Modell: ArchiMate als Architektur-Grammatik

Du kannst ArchiMate wie eine Grammatik lesen. Ein gutes Modell beantwortet Sätze wie: „Die Business Role Sachbearbeitung führt den Business Process Fachprüfung durch.“ Oder: „Der Business Process Fachprüfung wird durch den Application Service Vorgangsführung unterstützt.“ Oder: „Die Application Component Fachverfahren realisiert den Application Service Vorgangsführung und greift auf das Data Object Vorgang zu.“ Oder: „Der Technology Node Kubernetes-Cluster stellt die Laufzeitumgebung bereit, auf der die Anwendung betrieben wird.“

Diese Grammatik ist entscheidend, weil viele schlechte EA-Modelle nur aus Kästchen bestehen, deren Beziehungen unklar sind. Dann sieht man zwar viele Systeme, aber keine Architekturentscheidung. Ein ArchiMate-Modell wird erst wertvoll, wenn du Beziehungen gezielt setzt: **Serving** für Dienstbereitstellung, **Flow** für Austausch, **Realization** für Umsetzung, **Access** für Datenzugriff, **Assignment** für Zuordnung von Struktur zu Verhalten, **Composition/Aggregation** für Zerlegung und Gruppierung.

ArchiMate unterscheidet grob vier große Domänen: **Motivation**, **Strategy**, **Core** mit Business, Application und Technology sowie **Implementation & Migration**. Die praktische Open-Group-Einführung beschreibt diese Domänen genau in diesem Sinne: Motivation erklärt Gründe für Architekturveränderung, Strategy beschreibt Richtung, Wertschöpfung und benötigte Fähigkeiten, Core beschreibt die Lösung über Business, Application und Technology, und Implementation & Migration beschreibt Programme, Projekte und Migrationsplanung. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/))

## 3. Die wichtigsten Ebenen im Behördenkontext

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Motivation | Beschreibt Gründe, Ziele, Anforderungen, Prinzipien, Einschränkungen und Treiber einer Architekturveränderung. | Treiber: steigende Verfahrenslast; Ziel: medienbrucharme Bearbeitung; Constraint: hoher Schutzbedarf. | The Open Group beschreibt Motivation als Domäne für Gründe, die Architekturdesign oder Veränderung leiten. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |
| Strategy | Beschreibt Fähigkeiten, Ressourcen, Wertströme und strategische Handlungsrichtungen. | Capability: Anträge bearbeiten; Value Stream: Antrag einreichen bis Bescheid bereitstellen. | ArchiMate umfasst u. a. Strategy, Motivation, Transformation, Business, Application und Technology. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |
| Business | Beschreibt Rollen, Prozesse, Services, fachliche Objekte und organisatorische Zusammenarbeit. | Business Role: Sachbearbeitung; Business Process: Fachprüfung durchführen. | Die Business Layer dient zur Modellierung der Organisation, fachlicher Aktivitäten, Services und Informationen auf konzeptioneller Ebene. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |
| Application | Beschreibt Anwendungen, Anwendungskomponenten, Anwendungsschnittstellen, Services und Datenobjekte. | Application Component: Fachverfahren; Application Service: Vorgangsführung; Data Object: Antrag. | ArchiMate Core umfasst Business, Application und Technology als zentrale Lösungsebenen. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |
| Technology | Beschreibt technische Laufzeit, Plattformen, Knoten, Netzwerke, technische Services und Schnittstellen. | Technology Node: Kubernetes-Cluster; Technology Service: Datenbankdienst; Technology Interface: REST-Endpunkt. | The Open Group ordnet Technology dem Core-Bereich der Lösungsmodellierung zu. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |
| Physical | Beschreibt physische Ressourcen, Anlagen, Standorte, Geräte, Materialflüsse. In Behörden-IT oft nur relevant bei Rechenzentrum, Scannerstraßen, Druckzentrum, Aktenlogistik oder Spezialhardware. | Scanstraße im Posteingang, Druck- und Versandzentrum, Sicherheitszone im Rechenzentrum. | ArchiMate 3.x umfasst Physical zusätzlich zu Business, Application und Technology. ([guides.visual-paradigm.com](https://guides.visual-paradigm.com/de/docs/archimate-explained-a-guide-to-ai-powered-enterprise-architecture/part-i-introduction-to-archimate-and-enterprise-architecture/chapter-1-understanding-archimate/archimate-3-2-latest-enhancements-and-specification-overview/?utm_source=chatgpt.com)) |
| Implementation & Migration | Beschreibt Zielzustände, Übergangszustände, Lücken, Arbeitspakete, Liefergegenstände und Migrationsplanung. | Plateau Ist 2026, Plateau Ziel 2027, Gap zentrale IAM-Anbindung fehlt, Work Package OIDC-Integration. | The Open Group beschreibt Implementation & Migration als Domäne für Programme, Projekte und Migrationsplanung. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |

## 4. Die Kernelemente, die du wirklich brauchst

Eine **Capability** beschreibt, was die Organisation können muss, unabhängig davon, wie sie es heute organisatorisch oder technisch umsetzt. Im Behördenkontext ist das zum Beispiel „Anträge entgegennehmen“, „Identität prüfen“, „Fachentscheidung treffen“, „Bescheid erstellen“, „Akte führen“, „Zahlung auslösen“ oder „Widerspruch bearbeiten“. Eine Capability ist kein Prozess und keine Anwendung. Sie ist eine stabile Fähigkeit der Organisation.

Ein **Value Stream** beschreibt, wie aus Sicht der Wertentstehung oder Wirkung ein Ergebnis entsteht. In einer Behörde bedeutet „Value“ nicht Gewinn, sondern fachliche Wirkung: ein Antrag wird rechtssicher, nachvollziehbar und fristgerecht zu einer Entscheidung geführt. Ein Value Stream kann zum Beispiel lauten: „Anliegen erfassen → Anspruch prüfen → Entscheidung treffen → Bescheid bereitstellen → Vorgang abschließen.“

Ein **Business Process** beschreibt fachliches Verhalten. Er ist näher am Ablauf als die Capability, aber in ArchiMate meist gröber als BPMN. „Fachprüfung durchführen“ kann in ArchiMate ein Business Process sein; die genauen Schritte mit Gateways und Fristen gehören dann in BPMN.

Eine **Business Role** beschreibt eine Verantwortung oder Rolle, nicht zwingend eine konkrete Person oder Organisationseinheit. „Sachbearbeitung“, „Fachaufsicht“, „Poststelle“, „IT-Betrieb“, „Datenschutzkoordination“ oder „Antragsteller“ können Rollen sein. Eine Organisationseinheit kann einer Rolle zugeordnet werden, aber Rolle und Organigramm solltest du nicht vermischen.

Eine **Application Component** ist ein abgrenzbarer Softwarebaustein. „Fachverfahren Antrag“, „Online-Portal“, „DMS/eAkte“, „IAM-System“, „Registeradapter“ oder „Benachrichtigungsdienst“ sind typische Beispiele. Eine Application Component ist nicht der Service selbst. Sie realisiert Services.

Ein **Application Service** beschreibt, was eine Anwendung nach außen anbietet. „Antragserfassung“, „Vorgangsführung“, „Registerdatenabruf“, „Dokumentenablage“, „Statusauskunft“ oder „Authentifizierung“ sind Services. Services sind für EA besonders wichtig, weil sie eine stabile Schnittstelle zwischen Fachlichkeit und technischer Realisierung bilden.

Ein **Data Object** beschreibt digitale Daten, die von Anwendungen verarbeitet werden. Beispiele sind „Antrag“, „Personendatensatz“, „Nachweis“, „Bescheid“, „Aktenmetadaten“, „Statusereignis“ oder „Zahlungsanordnung“. Nicht jedes Datenbankdetail gehört hier hinein. Für EA reichen meist die fachlich relevanten Datenobjekte.

Ein **Technology Node** beschreibt einen technischen Ausführungs- oder Infrastrukturknoten. Beispiele sind „Containerplattform“, „Datenbankcluster“, „API-Gateway“, „Message Broker“, „Monitoring-Plattform“ oder „DMS-Betriebsumgebung“. In Behörden solltest du Technology Nodes besonders dann zeigen, wenn Schutzbedarf, Mandantentrennung, Betrieb, Netzsegmentierung oder Plattformstrategie entscheidungsrelevant sind.

Ein **Interface** ist ein Zugriffspunkt. Wichtig: In ArchiMate ist „Interface“ nicht einfach eine Linie. Ein Application Interface kann ein API-Endpunkt, ein Portalzugang, ein OIDC-Client, ein Event Topic oder eine Dateischnittstelle sein. Ein Technology Interface kann ein Netzwerkzugang, ein Datenbankport, ein Container-Ingress oder ein Messaging-Endpunkt sein.

**Flow** zeigt, dass etwas von A nach B fließt: Daten, Dokumente, Ereignisse, Informationen. **Serving** zeigt, dass ein Service einem Konsumenten zur Verfügung steht. **Realization** zeigt, dass ein Element ein abstrakteres Element umsetzt oder erfüllt. Genau diese drei Beziehungen brauchst du ständig, darfst sie aber nicht verwechseln.

**Plateau** beschreibt einen Architekturzustand zu einem Zeitpunkt oder in einer Phase. **Gap** beschreibt die Lücke zwischen zwei Plateaus. **Work Package** beschreibt eine Maßnahme, ein Projekt oder ein Arbeitspaket, das die Lücke schließt. Damit wird ArchiMate transformationsfähig.

## 5. Das Behördenbeispiel: Fachverfahren „Antrags- und Bescheidmanagement“

Nehmen wir ein generisches Bundesbehörden-Fachverfahren. Bürger oder Organisationen stellen einen Antrag. Die Behörde nimmt den Antrag entgegen, prüft Nachweise, ruft Registerdaten ab, führt eine Fachprüfung durch, erstellt einen Bescheid, legt Dokumente in der eAkte ab und stellt Statusinformationen bereit. Es gibt ein Online-Portal, ein Fachverfahren, eine Registerschnittstelle, ein DMS/eAkte-System, ein IAM-System, eine Datenbank, ein API-Gateway, eine Containerplattform und ein zentrales Monitoring.

### 5.1 Motivation View: Warum verändern wir die Architektur?

Diese Sicht ist für Leitung, Architekturboard, Fachbereichsleitung, Datenschutz, Informationssicherheit und Programmsteuerung geeignet. Sie beantwortet nicht die Frage „Wie ist das technisch gebaut?“, sondern „Warum brauchen wir Veränderung und welche Anforderungen leiten daraus Architekturentscheidungen ab?“

Textuell modelliert sieht das so aus: Der **Driver** „steigende Verfahrenslast und wachsende Nachweispflichten“ beeinflusst das **Goal** „Anträge fristgerecht, nachvollziehbar und medienbrucharm bearbeiten“. Dieses Ziel wird durch die **Requirement** „zentrale digitale Antragserfassung“, die **Requirement** „nachvollziehbare Statusführung“ und die **Requirement** „Integration in DMS/eAkte“ konkretisiert. Zusätzlich gibt es den **Constraint** „Schutzbedarf hoch für personenbezogene Vorgangs- und Bescheiddaten“ sowie das **Principle** „API-first bei systemübergreifenden Integrationen“.

Der Fehler wäre hier, direkt mit Kubernetes, Datenbanken und APIs zu starten. Auf Motivationsebene geht es um Begründbarkeit. Ein Architekturboard will verstehen, warum die Zielarchitektur notwendig ist und welche Anforderungen nicht verhandelbar sind.

### 5.2 Strategy View: Welche Fähigkeiten braucht die Behörde?

Diese Sicht ist für Enterprise Architecture, Facharchitektur, strategische IT-Steuerung und Gremien geeignet. Sie beantwortet: „Welche Fähigkeiten müssen gestärkt, aufgebaut, konsolidiert oder abgelöst werden?“

Die zentrale **Capability** lautet „Anträge bearbeiten“. Darunter kannst du Fähigkeiten strukturieren: „Antrag entgegennehmen“, „Identität prüfen“, „Nachweise verwalten“, „Fachprüfung durchführen“, „Bescheid erstellen“, „Akte führen“, „Status kommunizieren“, „Widerspruch bearbeiten“. Der **Value Stream** lautet: „Anliegen erfassen → Unterlagen prüfen → Entscheidung vorbereiten → Bescheid erstellen → Ergebnis bereitstellen → Vorgang archivieren.“

Wichtig ist: Eine Capability ist stabiler als die Anwendung. Heute kann „Nachweise verwalten“ durch E-Mail, Dateiupload und manuelle Ablage erfolgen. Morgen kann dieselbe Capability durch Portal, DMS-Integration und Registerabruf unterstützt werden. Genau deshalb ist Capability-Modellierung für Behördenmodernisierung so wichtig.

### 5.3 Business View: Wer tut fachlich was?

Diese Sicht ist für Fachbereich, Organisationsreferat, Prozessmanagement und Anforderungsmanagement geeignet. Sie beantwortet: „Welche Rollen und fachlichen Prozesse sind betroffen?“

Die **Business Role** „Antragsteller“ initiiert den **Business Process** „Antrag einreichen“. Die **Business Role** „Poststelle“ oder „Eingangsmanagement“ ist dem Prozess „Antragseingang vorprüfen“ zugeordnet. Die **Business Role** „Sachbearbeitung“ führt „Fachprüfung durchführen“ aus. Die **Business Role** „Fachaufsicht“ unterstützt oder prüft „Entscheidung freigeben“. Der **Business Process** „Bescheid erstellen“ erzeugt das fachliche Ergebnis „Bescheid“. Der **Business Process** „Akte abschließen“ nutzt die eAkte.

In ArchiMate modellierst du diese Prozesse bewusst gröber als in BPMN. Du zeigst Abhängigkeiten und Architekturbezug. Wenn du Wartezeiten, Nachforderungen, parallele Prüfpfade, Fristen, Timer oder Eskalationen brauchst, modellierst du diese Detailtiefe ergänzend in BPMN.

### 5.4 Application View: Welche Anwendungen unterstützen die Facharbeit?

Diese Sicht ist für IT-Leitung, Solution Architecture, Fachverfahrensverantwortliche, Dienstleister und Enterprise Architecture geeignet. Sie beantwortet: „Welche Anwendungen liefern welche Services und wie hängen sie zusammen?“

Die **Application Component** „Online-Portal“ realisiert den **Application Service** „Antragserfassung“. Die **Application Component** „Fachverfahren Antrag“ realisiert die **Application Services** „Vorgangsführung“, „Fachprüfung unterstützen“ und „Bescheiderstellung“. Die **Application Component** „Registeradapter“ realisiert den **Application Service** „Registerdatenabruf“. Die **Application Component** „DMS/eAkte“ realisiert den **Application Service** „Dokumentenablage“. Die **Application Component** „IAM-System“ realisiert den **Application Service** „Authentifizierung und Autorisierung“.

Der **Business Process** „Antrag einreichen“ wird durch den Application Service „Antragserfassung“ bedient. Der **Business Process** „Fachprüfung durchführen“ wird durch „Vorgangsführung“ und „Registerdatenabruf“ bedient. Der **Business Process** „Bescheid erstellen“ wird durch „Bescheiderstellung“ und „Dokumentenablage“ bedient.

Hier ist **Serving** die zentrale Beziehung: Der Application Service „Vorgangsführung“ dient dem Business Process „Fachprüfung durchführen“. Die Application Component „Fachverfahren Antrag“ realisiert diesen Application Service. Wenn du stattdessen eine direkte Linie „Fachverfahren → Fachprüfung“ ohne Service ziehst, verlierst du die fachlich-technische Entkopplung.

### 5.5 Data & Interface View: Welche Daten fließen wohin?

Diese Sicht ist für Datenarchitektur, Datenschutz, Security, Schnittstellenarchitektur und Betrieb sehr wichtig. Sie beantwortet: „Welche Datenobjekte werden von welchen Anwendungen verarbeitet, übertragen oder gespeichert?“

Das **Data Object** „Antrag“ wird vom Online-Portal erzeugt und vom Fachverfahren verarbeitet. Das **Data Object** „Personendatensatz“ wird über den Registeradapter abgerufen. Das **Data Object** „Nachweis“ wird vom Portal entgegengenommen und im DMS abgelegt. Das **Data Object** „Bescheid“ wird vom Fachverfahren erstellt und an DMS/eAkte übergeben. Das **Data Object** „Statusereignis“ wird vom Fachverfahren erzeugt und über einen Messaging-Dienst an Benachrichtigung oder Portalstatus übermittelt.

Der **Flow** „Antrag“ läuft vom Online-Portal zum Fachverfahren. Der **Flow** „Registeranfrage/Registerantwort“ läuft zwischen Fachverfahren und Registeradapter. Der **Flow** „Bescheiddokument“ läuft vom Fachverfahren zum DMS/eAkte. Der **Flow** „Statusereignis“ läuft vom Fachverfahren zum Message Broker.

Hier liegt ein häufiger Fehler: Viele modellieren „Fachverfahren nutzt DMS“ als Flow. Das ist falsch, wenn du eine Nutzungsbeziehung meinst. Dafür nutzt du Serving. Flow ist nur sinnvoll, wenn wirklich etwas übertragen wird: Dokument, Datensatz, Ereignis, Nachricht, Aktenmetadatum.

### 5.6 Technology View: Worauf läuft das Ganze?

Diese Sicht ist für IT-Betrieb, Plattformteam, Security Architecture, Dienstleistersteuerung und technische Abnahme geeignet. Sie beantwortet: „Welche technischen Plattformen und Betriebsbausteine tragen die Anwendung?“

Der **Technology Node** „Kubernetes-Cluster“ stellt eine Laufzeitumgebung für die Application Components „Online-Portal“, „Fachverfahren Antrag“ und „Registeradapter“ bereit. Der **Technology Node** „Datenbankcluster“ unterstützt die Persistenz des Fachverfahrens. Der **Technology Node** „API-Gateway“ stellt kontrollierte externe und interne API-Zugänge bereit. Der **Technology Node** „Message Broker“ stellt asynchrone Ereignisverarbeitung bereit. Der **Technology Node** „Monitoring- und Logging-Plattform“ unterstützt Observability, Auditierbarkeit und Betriebsüberwachung.

Für Bundesbehörden solltest du Technology Views nicht unnötig tief zeichnen. Du musst nicht jeden Pod, jedes Volume und jede Firewallregel modellieren. Aber du solltest zeigen, welche Plattformdienste architekturentscheidend sind: IAM, API-Gateway, Netzsegmentierung, Secrets Management, Logging, Monitoring, Backup, Mandantentrennung, Verschlüsselung und Betriebshoheit.

### 5.7 Implementation & Migration View: Wie kommen wir vom Ist zum Ziel?

Diese Sicht ist für Programmleitung, Architekturboard, IT-Steuerung, Haushalts-/Planungsverantwortliche und Dienstleistersteuerung geeignet. Sie beantwortet: „Welche Lücken bestehen und welche Maßnahmen schließen sie?“

**Plateau Ist 2026** enthält: papierbasierter Antragseingang, manuelle Nachweiserfassung, dezentrale Benutzerverwaltung, dateibasierte DMS-Übergabe, unvollständiges Schnittstellenmonitoring. **Plateau Ziel 2027** enthält: Portal-Antragserfassung, zentrale IAM-Anbindung, standardisierte Register-API, DMS/eAkte-Integration, zentrale Observability, klare Datenverantwortung.

Dazwischen liegen **Gaps**: „G1: zentrale digitale Antragserfassung fehlt“, „G2: Registerintegration nicht standardisiert“, „G3: IAM nicht zentral angebunden“, „G4: DMS-Übergabe nicht API-basiert“, „G5: Ende-zu-Ende-Monitoring fehlt“, „G6: führendes System für Statusinformationen unklar“.

Die **Work Packages** lauten: „WP1 Portal-Antragserfassung einführen“, „WP2 Registeradapter bauen und Schnittstellenvertrag abstimmen“, „WP3 OIDC-Anbindung an zentrales IAM umsetzen“, „WP4 DMS/eAkte-API integrieren“, „WP5 Observability-Standard einführen“, „WP6 Datenverantwortung und führende Systeme klären.“

Damit wird ArchiMate zur Transformationssprache. Du kannst zeigen, dass ein Architekturziel nicht nur ein Wunschbild ist, sondern über konkrete Lücken und Maßnahmen gesteuert wird.

## 6. Capability-to-Technology-View: So baust du die wichtigste EA-Sicht

Die Capability-to-Technology-View ist für dich eine der wichtigsten Sichten, weil sie die Brücke zwischen Fachstrategie und technischer Realität schlägt. Sie zeigt: Welche Fähigkeit wird durch welchen Prozess ausgeprägt, welcher Application Service unterstützt diesen Prozess, welche Application Component realisiert den Service, welche Datenobjekte werden verarbeitet, welche Schnittstellen verbinden die Komponenten und welche technischen Plattformen tragen das Ganze.

Eine saubere textuelle Modellierung könnte so lauten:

Die **Capability** „Anträge bearbeiten“ wird durch den **Value Stream** „Antrag bis Bescheid“ konkretisiert. Der Value Stream umfasst die fachlichen Stufen „Antrag erfassen“, „Nachweise prüfen“, „Fachentscheidung vorbereiten“, „Bescheid erstellen“ und „Akte abschließen“. Der **Business Process** „Fachprüfung durchführen“ ist Teil dieser Wertschöpfung. Dieser Prozess wird durch den **Application Service** „Vorgangsführung“ unterstützt. Der Application Service „Vorgangsführung“ wird durch die **Application Component** „Fachverfahren Antrag“ realisiert. Das Fachverfahren greift auf die **Data Objects** „Vorgang“, „Antrag“, „Nachweis“, „Personendatensatz“ und „Bescheid“ zu. Für Registerdaten nutzt das Fachverfahren den **Application Service** „Registerdatenabruf“, der durch die **Application Component** „Registeradapter“ realisiert wird. Der Registeradapter stellt den Zugriff über ein **Application Interface** „Register-REST-API“ bereit. Das Fachverfahren wird auf dem **Technology Node** „Containerplattform“ betrieben und nutzt die technischen Services „Datenbankdienst“, „Loggingdienst“, „Secrets Management“ und „API-Gateway“.

In einer Zeichnung würdest du das vertikal oder leicht gestuft anordnen: oben Capability und Value Stream, darunter Business Process, darunter Application Services und Components, darunter Data Objects und Interfaces, darunter Technology Services und Nodes. Diese Sicht sollte nicht mehr als eine bis zwei zentrale Capabilities zeigen. Wenn du zehn Capabilities gleichzeitig modellierst, entsteht ein Poster, aber keine Entscheidungshilfe.

## 7. Application Landscape: So modellierst du die Anwendungslandschaft

Eine Application Landscape zeigt nicht primär Infrastruktur, sondern fachlich relevante Anwendungen und ihre Beziehungen. Für Behörden solltest du Anwendungen nach Domänen oder Fähigkeiten gruppieren. Typische Gruppen sind „Eingangskanal“, „Kernfachverfahren“, „Registerintegration“, „Dokumentenmanagement/eAkte“, „Identität und Zugriff“, „Kommunikation“, „Reporting“, „Betrieb und Observability“.

In unserem Beispiel enthält die Application Landscape folgende Komponenten: „Online-Portal“, „Fachverfahren Antrag“, „Registeradapter“, „DMS/eAkte“, „IAM-System“, „Benachrichtigungsdienst“, „Reporting-Plattform“, „Monitoring-Plattform“. Zwischen diesen Komponenten modellierst du nicht einfach Linien, sondern klare Beziehungen: Das Online-Portal überträgt den Antrag an das Fachverfahren als Flow. Das Fachverfahren nutzt den Registerdatenabruf als Serving-Beziehung. Das Fachverfahren übergibt Bescheiddokumente an DMS/eAkte als Flow. Das IAM-System stellt Authentifizierung und Autorisierung als Application Service bereit. Die Monitoring-Plattform erhält technische und fachliche Ereignisse als Flow.

Eine gute Application Landscape beantwortet drei Fragen: Erstens, welche Anwendungen gibt es? Zweitens, welche Services bieten sie an? Drittens, welche kritischen Flüsse und Abhängigkeiten bestehen? Eine schlechte Application Landscape ist nur eine Inventarliste mit Systemnamen.

## 8. Welche Sicht für welche Zielgruppe sinnvoll ist

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Behördenleitung / Gremium | Braucht Wirkung, Risiken, Zielbild, Abhängigkeiten und Entscheidungsbedarf; keine technische Detailtiefe. | Motivation + Capability + Plateau/Gaps: „Welche Fähigkeiten werden verbessert und welche Lücken kosten Zeit/Risiko?“ | ArchiMate-Viewpoints sollen Stakeholder, Zweck und Inhalt berücksichtigen. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |
| Fachbereich | Braucht Rollen, Prozesse, fachliche Services, Medienbrüche und Datenverantwortung. | Business View mit Sachbearbeitung, Fachprüfung, Bescheid, Akte, Nachforderung. | Die Business Layer modelliert Organisation, Aktivitäten, Services und fachliche Informationen. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |
| Enterprise Architecture | Braucht Ende-zu-Ende-Nachvollziehbarkeit von Capability bis Technologie. | Capability-to-Technology-View: Antrag bearbeiten → Fachprüfung → Fachverfahren → Datenobjekte → Plattform. | ArchiMate dient der kohärenten Architekturkommunikation über mehrere Domänen. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |
| Solution Architecture | Braucht Anwendungskomponenten, Services, Datenobjekte, Schnittstellen und technische Randbedingungen. | Application Cooperation View mit Portal, Fachverfahren, Registeradapter, DMS und IAM. | ArchiMate Core umfasst Business, Application und Technology. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |
| Security / Datenschutz | Braucht Datenflüsse, Schutzbedarf, Identitäten, Schnittstellen, Logging und Betriebsgrenzen. | Data & Interface View mit Personendaten, Bescheid, Registerabruf, DMS-Übergabe und IAM. | ArchiMate unterstützt die Visualisierung von Beziehungen zwischen Domänen. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com)) |
| Betrieb / Plattformteam | Braucht Nodes, Technology Services, Laufzeitumgebung, Monitoring, Backup, Netzwerkzonen und Verantwortlichkeiten. | Technology View mit Kubernetes, API-Gateway, Datenbank, Broker, Logging. | Technology ist Teil der Core-Domäne der Lösungsmodellierung. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |
| Programmsteuerung | Braucht Plateaus, Gaps, Work Packages, Abhängigkeiten und Umsetzungsreihenfolge. | Ist 2026 → Transition 2027 → Ziel 2028; Gaps und Arbeitspakete je Zielzustand. | Implementation & Migration beschreibt Programme, Projekte und Migrationsplanung. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |

## 9. Modellierungsregeln für belastbare ArchiMate-Sichten

Regel eins: **Jede Sicht braucht eine Leitfrage.** Eine Sicht ohne Leitfrage wird eine Tapete. Gute Leitfragen sind: „Welche Anwendungen unterstützen die Fähigkeit Anträge bearbeiten?“, „Welche Datenobjekte fließen zwischen Fachverfahren und DMS?“, „Welche Gaps verhindern die Zielarchitektur?“, „Welche Plattformdienste sind für den Betrieb erforderlich?“

Regel zwei: **Trenne Fähigkeit, Prozess, Service und Anwendung.** „Antrag bearbeiten“ als Capability, „Fachprüfung durchführen“ als Business Process, „Vorgangsführung“ als Application Service und „Fachverfahren Antrag“ als Application Component sind vier unterschiedliche Dinge. Wenn du sie vermischst, erzeugst du ein Modell, das niemand sauber interpretieren kann.

Regel drei: **Nutze Services als Architekturvertrag.** Ein Application Service beschreibt, was ein System anbietet. Die Komponente beschreibt, wer es realisiert. Dadurch kannst du später Komponenten austauschen, ohne das fachliche Modell neu zu bauen.

Regel vier: **Nutze Flow nur bei tatsächlicher Übertragung.** Wenn ein Antrag, Dokument, Datensatz, Ereignis oder Status von A nach B geht, ist Flow passend. Wenn A eine Fähigkeit von B nutzt, ist Serving passender.

Regel fünf: **Modelliere Interfaces als Zugriffspunkte.** Eine REST-API, ein Event Topic, ein OIDC-Endpunkt, eine SFTP-Schnittstelle oder ein Portalzugang kann als Interface modelliert werden. Das Interface ist nicht die Verbindungslinie, sondern der angebotene Zugang.

Regel sechs: **Data Objects sind nicht Datenbanken.** „Bescheid“ ist ein Data Object. „PostgreSQL“ ist eher Technology Node beziehungsweise Technology Service. „Tabelle tbl_bescheid_v2“ gehört in der Regel nicht in ArchiMate, sondern in Datenmodellierung.

Regel sieben: **Plateaus brauchen Zeit- und Zustandsbezug.** Ein Plateau ohne Zeitpunkt ist schwach. Besser: „Ist-Architektur Q4/2026“, „Übergangsarchitektur Q2/2027“, „Zielarchitektur Q4/2027“.

Regel acht: **Jeder Gap braucht mindestens eine Maßnahme oder eine offene Entscheidung.** Ein Gap ohne Work Package ist nur ein Problemhinweis. Ein Gap mit Work Package wird steuerbar.

Regel neun: **Zeige nur entscheidungsrelevante Technologie.** Nicht jeder technische Baustein gehört auf jede EA-Sicht. API-Gateway, IAM, Message Broker, Datenbank, Containerplattform und Observability sind meistens relevant; einzelne Container-Ports eher nicht.

Regel zehn: **Halte Beziehungen semantisch sauber.** Lieber fünf präzise Beziehungen als zwanzig beliebige Linien. Ein Modell wird nicht durch Menge professionell, sondern durch richtige Abstraktion.

Regel elf: **Nutze konsistente Namen.** Capabilities als Substantiv oder substantivierte Fähigkeit: „Antragsbearbeitung“, „Bescheiderstellung“. Prozesse als Verb-Nomen: „Antrag prüfen“, „Bescheid erstellen“. Services als angebotene Fähigkeit: „Vorgangsführung“, „Dokumentenablage“. Work Packages als aktive Maßnahme: „IAM-Anbindung umsetzen“.

Regel zwölf: **Versioniere Sichten.** Jede Architekturansicht sollte Titel, Zweck, Zielgruppe, Stand, Owner, Gültigkeit und offene Fragen enthalten. Sonst wird sie im Behördenkontext schnell zur nicht belastbaren Präsentationsgrafik.

## 10. Häufige Modellierungsfehler

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Alles wird als „System“ modelliert | Rollen, Prozesse, Services, Daten und Plattformen werden als gleichartige Kästen gezeichnet. | „Sachbearbeitung“, „Fachverfahren“, „Bescheid“ und „Kubernetes“ stehen auf einer Ebene. | ArchiMate unterscheidet Domänen und Layer, um genau diese Vermischung zu vermeiden. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |
| Capability wird mit Prozess verwechselt | Eine Fähigkeit beschreibt Können; ein Prozess beschreibt Verhalten/Ablauf. | Falsch: Capability „Antrag prüfen Schritt 1“. Besser: Capability „Antragsprüfung“, Prozess „Antrag fachlich prüfen“. | Strategy und Business haben unterschiedliche Modellierungszwecke. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |
| Application Component und Application Service werden vermischt | Der Service ist das angebotene Verhalten; die Komponente ist der Softwarebaustein. | Falsch: „Fachverfahren“ dient dem Prozess direkt. Besser: Fachverfahren realisiert „Vorgangsführung“, dieser Service dient dem Prozess. | ArchiMate nutzt serviceorientierte Sichtweisen zur Verbindung der Ebenen. ([vanharen.store](https://www.vanharen.store/samplefile/api/downloader/getId/978940180955C?srsltid=AfmBOorLYqooMCW1OFna1BxZUELXZxemsbkOm8eYkk8dYTp1U1xUxRb-&utm_source=chatgpt.com)) |
| Flow wird als allgemeine Abhängigkeit missbraucht | Flow bedeutet Austausch, nicht Nutzung. | Falsch: „Sachbearbeitung flow Fachverfahren“. Besser: Business Process wird durch Application Service bedient. | ArchiMate unterscheidet Beziehungsarten im Metamodell; nicht jede Beziehung ist beliebig gültig. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |
| Schnittstellen werden nur als Linien gezeichnet | Dadurch fehlen Zugriffspunkt, Vertrag, Protokoll und Verantwortung. | Besser: Application Interface „Register-REST-API“ mit Provider, Consumer, Datenobjekten und SLA. | Viewpoints sollen gezielt Stakeholderfragen beantworten; Schnittstellen sind oft eigene Entscheidungsobjekte. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |
| Datenobjekte werden zu technisch modelliert | Tabellen, Spalten und Payload-Felder überladen EA-Sichten. | Besser: „Personendatensatz“, „Nachweis“, „Bescheid“, „Statusereignis“. | ArchiMate ist für Übersicht und Kohärenz gedacht; Details gehören in passendere Spezifikationen. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |
| Ist und Ziel werden vermischt | Man sieht nicht, ob etwas heute existiert, geplant oder abzulösen ist. | Besser: Plateaus „Ist“, „Transition“, „Ziel“ mit Gaps. | Implementation & Migration dient genau der Migrationsplanung. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |
| Views sind zu groß | Eine Sicht versucht Fachlichkeit, Daten, Infrastruktur, Roadmap und Security gleichzeitig zu zeigen. | Besser: mehrere Views mit gemeinsamer Modellbasis. | ArchiMate unterscheidet Views nach Stakeholder, Zweck und Inhalt. ([archimate-community.pages.opengroup.org](https://archimate-community.pages.opengroup.org/workgroups/archimate-101/)) |

## 11. Konkrete Umsetzung: So gehst du in einem echten Behördenprojekt vor

Beginne nicht im Tool. Beginne mit einer Architekturfrage. Zum Beispiel: „Welche Anwendungen und Plattformen sind notwendig, um die Fähigkeit Antragsbearbeitung medienbrucharm und betrieblich stabil zu unterstützen?“ Dann legst du einen kleinen Modellumfang fest: eine Capability, drei bis fünf Prozesse, fünf bis acht Anwendungen, fünf bis zehn Datenobjekte, drei bis sechs Schnittstellen, drei bis fünf Plattformbausteine, drei Plateaus und fünf bis zehn Gaps.

Danach baust du Kataloge. Ein Capability-Katalog enthält Name, Beschreibung, Owner, Reifegrad, Zielreifegrad und betroffene Fachbereiche. Ein Anwendungskatalog enthält Name, Zweck, Owner, Lebenszyklus, Kritikalität, Schutzbedarf, Schnittstellen und Datenobjekte. Ein Datenobjektkatalog enthält Name, Beschreibung, führendes System, Schutzbedarf, Verarbeitung, Aufbewahrung und Löschung. Ein Schnittstellenkatalog enthält Provider, Consumer, Zweck, Datenobjekte, Protokoll, Authentifizierung, Autorisierung, SLA/SLO, Monitoring und Änderungsprozess. Ein Work-Package-Katalog enthält Ziel, betroffene Gaps, Abhängigkeiten, Liefergegenstände, Risiken und Entscheidungspunkte.

Erst dann zeichnest du Sichten. Für die erste Iteration reichen vier Sichten: eine Capability-to-Technology-View, eine Application Landscape, eine Data & Interface View und eine Migration View mit Plateaus, Gaps und Work Packages. Diese vier Sichten sind für Behörden-EA oft wirkungsvoller als zwanzig Detaildiagramme.

Im Review prüfst du jede Sicht mit drei Fragen: Erstens, beantwortet sie die ursprüngliche Stakeholderfrage? Zweitens, sind die ArchiMate-Elemente semantisch richtig verwendet? Drittens, führt die Sicht zu einer Entscheidung, einer Klärung oder einer belastbaren nächsten Maßnahme? Wenn die Antwort dreimal Nein ist, ist die Sicht Dekoration.

## 12. Übungsaufgaben

### Übung 1: Capability Map für ein Fachverfahren

Modelliere für ein Antragsverfahren folgende Capabilities: „Antrag entgegennehmen“, „Identität prüfen“, „Nachweise verwalten“, „Fachprüfung durchführen“, „Bescheid erstellen“, „Akte führen“, „Status kommunizieren“, „Widerspruch bearbeiten“. Ordne jede Capability einem Reifegrad zu: niedrig, mittel, hoch. Markiere zwei Capabilities, die Zielarchitektur-relevant sind.

### Übung 2: Capability-to-Technology-Kette

Wähle die Capability „Nachweise verwalten“. Baue eine Kette aus Capability, Business Process, Business Role, Application Service, Application Component, Data Object, Interface, Technology Node. Beschreibe jede Beziehung mit Serving, Flow, Realization oder Access.

### Übung 3: Application Landscape

Erstelle eine Application Landscape mit Online-Portal, Fachverfahren, Registeradapter, DMS/eAkte, IAM-System, Message Broker und Monitoring-Plattform. Zeige nur die wichtigsten Services und Flows. Begrenze dich auf maximal zwölf Elemente.

### Übung 4: Data & Interface View

Modelliere die Datenobjekte „Antrag“, „Personendatensatz“, „Nachweis“, „Bescheid“, „Aktenmetadaten“ und „Statusereignis“. Zeige, welche Anwendung diese Daten erzeugt, verarbeitet, liest oder weitergibt. Markiere das führende System je Datenobjekt.

### Übung 5: Gap-Analyse

Definiere ein Ist-Plateau und ein Ziel-Plateau. Formuliere mindestens fünf Gaps. Für jeden Gap formulierst du ein Work Package. Beispiel: Gap „IAM nicht zentral angebunden“ → Work Package „OIDC-Anbindung an zentrales IAM umsetzen“.

### Übung 6: Review eines schlechten Modells

Nimm ein Modell, in dem alle Elemente als „Systeme“ dargestellt sind. Korrigiere es, indem du Rollen, Prozesse, Services, Komponenten, Datenobjekte und Nodes sauber trennst. Dokumentiere, welche Architekturinformation erst durch diese Trennung sichtbar wurde.

## 13. Qualitätscheckliste für ArchiMate-Sichten

Eine ArchiMate-Sicht ist gut, wenn sie eine klare Zielgruppe hat, eine konkrete Frage beantwortet, nicht mehr Elemente zeigt als nötig, Capability, Prozess, Anwendung, Daten und Technologie sauber trennt, Services konsequent als Außenverhalten nutzt, Beziehungen korrekt einsetzt, Flows nur für Austausch verwendet, Data Objects nicht mit Datenbanken verwechselt, Ist- und Zielzustände unterscheidet, Gaps mit Work Packages verbindet, offene Entscheidungen sichtbar macht, Schutzbedarf und Betriebsrelevanz nicht unterschlägt, einen Owner und Stand besitzt und in einem Gremium innerhalb weniger Minuten erklärbar ist.

## 14. Merksatz für deine EA-Praxis

ArchiMate ist dann stark, wenn du nicht zeichnest, was irgendwo existiert, sondern modellierst, was für eine Architekturentscheidung relevant ist. Für Bundesbehörden heißt das: Du machst sichtbar, welche fachliche Fähigkeit durch welche Prozesse, Anwendungen, Daten, Schnittstellen und Plattformen getragen wird; wo Lücken bestehen; welche Maßnahmen diese Lücken schließen; und welche Entscheidungen Leitung, Fachseite, IT, Security, Betrieb und Dienstleister gemeinsam treffen müssen.

<>