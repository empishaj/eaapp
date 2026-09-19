## Checkliste: Was du bei Event-Driven Architecture sofort prüfen musst

☐ Ist klar, welches fachliche Ereignis tatsächlich passiert ist, oder wird nur ein technischer Zustand weitergereicht?  
☐ Ist der Unterschied zwischen *Event*, *Command* und allgemeiner *Message* sauber verstanden?  
☐ Gibt es einen fachlichen Grund für Asynchronität, oder wird EDA nur verwendet, weil es modern klingt?  
☐ Sind Producer, Consumer, Broker, Topics, Queues und Verantwortlichkeiten eindeutig beschrieben?  
☐ Ist geregelt, wer Eigentümer eines Events und seines Schemas ist?  
☐ Sind Idempotenz, Retry, Dead Letter Queue und Fehlerbehandlung verbindlich konzipiert?  
☐ Ist die Reihenfolge von Events fachlich relevant, und falls ja: pro Akte, pro Antrag, pro Person oder global?  
☐ Ist geklärt, ob Event Notification, Event Carried State Transfer, Event Sourcing oder CQRS gemeint ist?  
☐ Gibt es Observability über Event-Flüsse hinweg: Correlation ID, Trace ID, Lag, Fehlerquoten, DLQ-Bestand?  
☐ Ist Schema Evolution geregelt, ohne bestehende Consumer zu brechen?  
☐ Sind Schutzbedarf, Protokollierung, personenbezogene Daten und Aufbewahrung berücksichtigt?  
☐ Kann der Fachbereich erklären, warum ein Event existiert und welche fachliche Bedeutung es hat?  

<>

## 1. Grundgedanke: EDA ist kein Techniktrick, sondern ein Kopplungsmodell

Event-Driven Architecture bedeutet: Systeme reagieren nicht primär auf direkte synchrone Aufrufe, sondern auf Ereignisse, die in einem Geschäftsprozess bereits eingetreten sind. Ein Fachverfahren ruft also nicht zwingend aktiv jedes nachgelagerte System auf, sondern veröffentlicht zum Beispiel: *Antrag eingegangen*, *Nachweis geprüft*, *Bescheid erstellt*, *Zahlung ausgelöst* oder *Akte aktualisiert*. Andere Systeme können darauf reagieren, ohne dass das Ursprungssystem alle Empfänger kennen muss. Genau darin liegt der architektonische Reiz: fachliche Entkopplung, zeitliche Entkopplung und bessere Erweiterbarkeit. Gleichzeitig entstehen neue Risiken: verzögerte Konsistenz, schwerere Nachvollziehbarkeit, komplexere Fehlerbehandlung, Event-Versionierung, Betriebskomplexität und neue Anforderungen an Governance.

Ein Event ist dabei nicht einfach „irgendeine Nachricht“. AsyncAPI unterscheidet sauber: Eine Message transportiert Informationen zwischen Anwendungen; ein Event ist eine Message, die beschreibt, dass etwas bereits passiert ist. Eine Message kann je nach Inhalt auch Command, Query oder Event sein. Diese Unterscheidung ist für Behördenarchitektur entscheidend, weil aus ihr Zuständigkeit, Nachweisbarkeit und Fehlerbehandlung folgen. ([asyncapi.com](https://www.asyncapi.com/docs/concepts/message?utm_source=chatgpt.com))

Der wichtigste Satz für deine Praxis lautet: **Ein Event beschreibt eine fachlich relevante Tatsache in der Vergangenheit. Ein Command fordert eine Handlung in der Zukunft an.** Wenn ein System sagt: *PrüfeNachweis*, ist das ein Command. Wenn ein System sagt: *NachweisGeprüft*, ist das ein Event. Wenn ein System sagt: *Status = P*, ist das meistens kein gutes fachliches Event, sondern ein technischer Zustandsabwurf.

## 2. Die Kernbegriffe präzise erklärt

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Event | Ein Ereignis beschreibt, dass etwas fachlich Relevantes bereits passiert ist. Es ist rückblickend formuliert und sollte fachliche Bedeutung tragen. | *AntragEingegangen*, *NachweisGeprüft*, *BescheidErstellt* | AsyncAPI unterscheidet Messages und Events und beschreibt Events als Nachrichten über bereits eingetretene Sachverhalte. ([asyncapi.com](https://www.asyncapi.com/docs/concepts/message?utm_source=chatgpt.com)) |
| Command | Ein Command fordert ein anderes System oder eine Komponente auf, etwas zu tun. Es ist handlungsorientiert und zukunftsgerichtet. | *BescheidErstellen*, *ZahlungAuslösen*, *AkteAktualisieren* | Die Trennung von Commands und Queries ist Kern des CQRS-Gedankens; Microsoft beschreibt CQRS als Trennung von Schreib- und Lesemodellen. ([learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)) |
| Message | Oberbegriff für transportierte Information. Eine Message kann Event, Command oder Query sein. | JSON-Nachricht über Kafka, AMQP, HTTP Webhook oder Message Queue | AsyncAPI ist protocol-agnostisch und beschreibt message-driven APIs maschinenlesbar. ([asyncapi.com](https://www.asyncapi.com/docs/reference/specification/latest)) |
| Producer | System oder Komponente, die ein Event erzeugt und veröffentlicht. | Fachanwendung veröffentlicht *AntragEingegangen* | CloudEvents adressiert Interoperabilität zwischen Services, Plattformen und Systemen. ([github.com](https://github.com/cloudevents/spec)) |
| Consumer | System oder Komponente, die Events empfängt und verarbeitet. | DMS legt Akte an, Reporting aktualisiert Kennzahlen, Zahlungsmodul startet Prüfung | EDA entkoppelt Aufgaben von auslösenden Operationen, Consumer kennen Eventtyp und Eventdaten, aber nicht zwingend den auslösenden Prozess. ([learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)) |
| Broker | Technische Vermittlungsschicht für Nachrichten. Der Broker verteilt Events, puffert sie und ermöglicht asynchrone Verarbeitung. | Kafka, RabbitMQ, ActiveMQ, Azure Service Bus, Redpanda | AsyncAPI nennt u. a. AMQP, MQTT, WebSockets, Kafka und STOMP als mögliche Protokolle. ([asyncapi.com](https://www.asyncapi.com/docs/reference/specification/latest)) |
| Topic | Logischer Kanal für Publish/Subscribe-Kommunikation. Mehrere Consumer können dieselben Events erhalten. | Topic `antrag.events` mit *AntragEingegangen* und *AntragZurückgezogen* | AsyncAPI beschreibt Channels und Operationen wie Senden oder Empfangen über solche Kanäle. ([asyncapi.com](https://www.asyncapi.com/docs/reference/specification/latest)) |
| Queue | Punkt-zu-Punkt-Verarbeitung: Eine Nachricht wird typischerweise von einem Worker aus einer Consumer-Gruppe verarbeitet. | Warteschlange für asynchrone PDF-Erzeugung eines Bescheids | Architektonisch relevant ist die Semantik: Pub/Sub für Ereignisverteilung, Queue für Arbeitsverteilung. |
| Event Notification | Kleines Event: „Es ist etwas passiert.“ Der Consumer muss Details bei Bedarf nachladen. | *AkteAktualisiert* mit `akteId`, Consumer ruft Aktenservice ab | Fowler warnt vor unterschiedlichen Bedeutungen von „event-driven“ und betont, dass Muster nicht vermischt werden dürfen. ([martinfowler.com](https://martinfowler.com/articles/201701-event-driven.html)) |
| Event Carried State Transfer | Event enthält relevante Daten, damit Consumer ohne Rückfrage arbeiten können. | *BescheidErstellt* enthält Bescheid-ID, Datum, Bescheidart, Aktenzeichen, Status, aber nicht zwingend kompletten Bescheidinhalt | Diese Variante reduziert synchrone Rückfragen, erhöht aber Datenschutz-, Versionierungs- und Duplikationsrisiken. |
| Event Sourcing | Zustand wird aus einer chronologischen Folge unveränderlicher Events rekonstruiert. Das Event Log ist Quelle der Wahrheit. | Antrag entsteht aus *AntragEingegangen*, *NachweisNachgereicht*, *NachweisGeprüft*, *BescheidErstellt* | Microsoft beschreibt Event Sourcing als append-only Event Store, aus dem aktueller Zustand per Replay abgeleitet wird. ([learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)) |
| CQRS | Command Query Responsibility Segregation trennt Schreibmodell und Lesemodell. Oft, aber nicht zwingend, mit Events kombiniert. | Schreibmodell prüft Fachregeln; Lesemodell liefert schnelle Vorgangssuche für Sachbearbeitung | Microsoft beschreibt getrennte Read-/Write-Modelle, unabhängige Skalierung und das Risiko eventual consistency. ([learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)) |

## 3. Der Behördenfall: Ein Fachverfahren für Anträge

Stell dir ein Fachverfahren in einer Bundesbehörde vor. Externe Antragstellende reichen über ein Portal einen Antrag ein. Die Sachbearbeitung prüft Nachweise. Die Fachaufsicht überwacht bestimmte Fälle. Ein DMS führt die elektronische Akte. Ein Zahlungsdienst stößt Auszahlungen an. Ein Berichtssystem erzeugt Lagebilder und Kennzahlen. Ein IAM-System steuert Rollen und Rechte. Ein zentrales Logging-/Monitoring-System sammelt Ereignisse für Betrieb, Nachvollziehbarkeit und Sicherheitsanalyse.

In einer rein synchronen Architektur würde das Fachverfahren nach Eingang des Antrags nacheinander DMS, Benachrichtigung, Fachaufsicht, Reporting und vielleicht weitere Registerschnittstellen direkt aufrufen. Das wirkt am Anfang einfach. Es wird aber problematisch, wenn ein nachgelagertes System langsam ist, ausfällt oder später weitere Consumer hinzukommen. Jede neue Integration verändert dann das Fachverfahren.

In einer EDA veröffentlicht das Fachverfahren nach erfolgreicher fachlicher Annahme des Antrags ein Event: *AntragEingegangen*. Das DMS reagiert darauf und legt eine Akte an. Das Benachrichtigungssystem verschickt eine Eingangsbestätigung. Das Reporting aktualisiert eine Fallzahlprojektion. Die Fachaufsicht bekommt nur dann ein Folgeereignis, wenn bestimmte fachliche Kriterien erfüllt sind. Das Ursprungssystem muss nicht alle Folgeprozesse kennen. Genau das ist der architektonische Gewinn.

Aber: Die Behörde bezahlt diesen Gewinn mit zusätzlicher Betriebsverantwortung. Es muss klar sein, ob ein Event erfolgreich veröffentlicht wurde, ob Consumer es verarbeitet haben, welche Events hängen geblieben sind, ob Events doppelt verarbeitet wurden, ob eine DLQ anwächst und ob alle fachlich relevanten Schritte revisionssicher nachvollzogen werden können. Das BSI fordert für den Behördenkontext ausdrücklich angemessene Protokollierung und Detektion sicherheitsrelevanter Ereignisse; der Mindeststandard zur Protokollierung und Detektion wurde 2024 in Version 2.1 hinsichtlich Speicherfristen und Löschung konkretisiert. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Mindeststandards/PDCA/PDCA_node.html?utm_source=chatgpt.com))

## 4. EDA ist sinnvoll, wenn diese Bedingungen erfüllt sind

EDA ist besonders sinnvoll, wenn mehrere unabhängige Reaktionen auf denselben fachlichen Vorgang erforderlich sind. Beispiel: *BescheidErstellt* interessiert das DMS, das Benachrichtigungssystem, das Reporting, die Fachaufsicht, eventuell die Zahlungsstrecke und das Audit-Logging. Würde das Fachverfahren alle Empfänger direkt aufrufen, entstünde eine harte Kopplung. Mit Events kann jeder Consumer eigenständig reagieren.

EDA ist auch sinnvoll, wenn zeitliche Entkopplung wichtig ist. Nicht jeder Folgeschritt muss im Moment der Benutzeraktion abgeschlossen sein. Wenn ein Antrag gespeichert wurde, kann die Aktenanlage oder ein Berichtseintrag nachgelagert erfolgen, sofern der Fachprozess das zulässt. Genau hier muss der Architekt mit dem Fachbereich klären: Was muss sofort konsistent sein, was darf verzögert konsistent sein und welche Verzögerung ist fachlich akzeptabel? Microsoft weist beim Einsatz getrennter Schreib- und Lesemodelle ausdrücklich auf eventual consistency hin: Lesedaten können hinter dem Schreibereignis zurückliegen. ([learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs))

EDA ist sinnvoll, wenn Erweiterbarkeit ein zentrales Ziel ist. Wenn später ein Data-Warehouse, ein KI-gestütztes Fallmonitoring, ein neues DMS oder ein zusätzlicher Registerabgleich angebunden werden soll, können neue Consumer Events abonnieren, ohne die Fachanwendung jedes Mal tiefgreifend umzubauen. Dieser Vorteil gilt aber nur, wenn Event-Verträge stabil, dokumentiert und versioniert sind.

EDA ist dagegen unnötige Komplexität, wenn ein Vorgang eigentlich eine einfache synchrone Abfrage ist. Wenn die Sachbearbeitung in der Oberfläche sofort wissen muss, ob eine Registerauskunft gültig ist, dann ist ein synchroner Request/Response-Aufruf oft richtiger. EDA ist ebenfalls fragwürdig, wenn ein Team keine Betriebsreife für Broker, Monitoring, Replay, DLQ, Schema Registry, Consumer-Lag und Incident-Prozesse hat. Fowler beschreibt Event Sourcing und CQRS ausdrücklich als Muster, die an der richtigen Stelle stark, aber am falschen Ort komplexitätssteigernd und oft missverstanden sind. ([martinfowler.com](https://martinfowler.com/articles/201701-event-driven.html))

## 5. Entscheidungskriterien für oder gegen EDA

| Aspekt | Details/Erklärung | Beispiel | Entscheidung | Literatur/Quelle |
|---|---|---|---|---|
| Mehrere unabhängige Folgeprozesse | EDA lohnt sich, wenn ein Ereignis mehrere fachlich unabhängige Reaktionen auslöst. | *AntragEingegangen* → DMS, Benachrichtigung, Reporting | Pro EDA | Microsoft beschreibt Entkopplung von Event-Erzeugung und Event-Handling als Vorteil. ([learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)) |
| Sofortige Antwort erforderlich | Wenn die Benutzeraktion sofort ein verbindliches Ergebnis braucht, ist synchron oft einfacher. | Registerprüfung muss sofort Ergebnis liefern | Contra EDA oder hybride Architektur | Eventual consistency muss verstanden und fachlich akzeptiert sein. ([learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)) |
| Fachliche Historie wichtig | Wenn jede Änderung fachlich nachvollziehbar bleiben muss, kann Event Sourcing interessant sein. | Verlauf eines Antrags mit Nachreichungen, Prüfungen, Korrekturen | Event Sourcing prüfen | Event Sourcing bietet starke Audit-Fähigkeit und Rekonstruktion historischer Zustände. ([martinfowler.com](https://martinfowler.com/articles/201701-event-driven.html)) |
| Hoher Schutzbedarf | Je sensibler die Daten, desto stärker müssen Event-Inhalte minimiert, verschlüsselt, protokolliert und berechtigt werden. | Personenbezogene Nachweisdaten in Events | Nur mit strenger Governance | BSI-Schutzbedarf betrachtet Vertraulichkeit, Integrität und Verfügbarkeit. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Teamreife im Betrieb | Ohne Monitoring, DLQ-Prozess, Schema Governance und Incident-Fähigkeit wird EDA gefährlich. | DLQ wächst, niemand merkt es | Contra EDA bis Betriebsmodell steht | BSI-Protokollierung und Detektion sind im Bundeskontext besonders relevant. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Mindeststandards/PDCA/PDCA_node.html?utm_source=chatgpt.com)) |
| Datenkonsistenz | Wenn alle Daten jederzeit sofort konsistent sein müssen, wird EDA schwieriger. | Auszahlung darf erst nach rechtsgültigem Bescheid erfolgen | EDA nur mit Prozesskontrolle/Saga | Microsoft beschreibt Konsistenzherausforderungen bei getrennten Datenbanken und Event-Publishing. ([learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)) |
| Integrationslandschaft | Viele Systeme, unterschiedliche Lebenszyklen und lose Kopplung sprechen für EDA. | DMS, Fachverfahren, Zahlung, Reporting, Archiv | Pro EDA | CloudEvents zielt auf Interoperabilität über Services und Plattformen hinweg. ([github.com](https://github.com/cloudevents/spec)) |
| Dokumentierbarkeit | EDA braucht maschinenlesbare Event-Verträge. | AsyncAPI für Topics, Messages, Payloads, Bindings | Pro, wenn dokumentiert | AsyncAPI beschreibt message-driven APIs maschinenlesbar und protocol-agnostisch. ([asyncapi.com](https://www.asyncapi.com/docs/reference/specification/latest)) |
| Datenschutzrisiko | Events dürfen nicht zum unkontrollierten Schatten-Datenmodell werden. | Vollständige Nachweise in jedem Event | Contra bei Datenüberfrachtung | Schutzbedarf und Protokollierung müssen konsequent bewertet werden. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Veränderungsrate | Häufige fachliche Änderungen erfordern klare Versionierungsregeln. | Neues Feld `entscheidungsgrund` im Event *BescheidErstellt* | Pro nur mit Schema Evolution | Fowler nennt Schemaänderungen bei Event Sourcing als Problemfeld. ([martinfowler.com](https://martinfowler.com/articles/201701-event-driven.html)) |

## 6. Beispielarchitektur für ein Fachverfahren

Die Zielarchitektur kann man in sechs Zonen denken. Erstens gibt es die Eingangsschicht mit Portal, API-Gateway und Authentifizierung. Zweitens gibt es die Fachanwendung mit Domänenlogik, Validierung und Transaktionsgrenze. Drittens gibt es eine persistente Datenhaltung für den fachlichen Zustand. Viertens gibt es ein Event-Publishing-Modul, idealerweise mit Outbox-Pattern, damit Datenänderung und Event-Veröffentlichung nicht auseinanderlaufen. Fünftens gibt es den Broker mit Topics, Consumer Groups, Retry Topics und Dead Letter Queue. Sechstens gibt es Consumer wie DMS, Benachrichtigung, Reporting, Zahlungsstrecke, Audit-Service und Prozessmonitoring.

Ein sauberer Fluss sieht so aus: Antragstellender sendet Antrag. Fachanwendung validiert Pflichtdaten, Berechtigung und Fachregeln. Fachanwendung speichert Antrag in der eigenen Datenbank. In derselben lokalen Transaktion schreibt sie einen Outbox-Eintrag. Ein Publisher liest die Outbox und veröffentlicht das Event *AntragEingegangen* auf dem Topic `fachverfahren.antrag.v1`. Consumer verarbeiten das Event idempotent. Das DMS legt eine Akte an. Das Reporting aktualisiert Kennzahlen. Das Benachrichtigungssystem verschickt eine Eingangsbestätigung. Alle Consumer schreiben technische Verarbeitungsergebnisse mit Correlation ID in Logs und Metriken. Fehlerhafte Nachrichten gehen nach definierten Retry-Regeln in die DLQ. Dort gibt es einen fachlich-technischen Bearbeitungsprozess.

Das Outbox-Pattern ist in Behördenarchitektur besonders wichtig, auch wenn es im ersten Entwurf oft vergessen wird. Ohne Outbox kann folgendes passieren: Die Datenbank speichert den Antrag erfolgreich, aber das Event wird wegen Broker-Ausfall nicht veröffentlicht. Oder umgekehrt: Das Event wird veröffentlicht, aber die Datenbanktransaktion schlägt fehl. Dann reagieren Consumer auf einen Antrag, der fachlich nicht existiert. Als Architekt musst du diese Transaktionsgrenze immer aktiv prüfen.

## 7. Die wichtigsten Event-Arten im Behördenbeispiel

| Aspekt | Details/Erklärung | Beispiel | Architekturhinweis |
|---|---|---|---|
| Fachliches Eingangsevent | Signalisiert, dass ein Vorgang fachlich angenommen wurde. | *AntragEingegangen* | Nicht veröffentlichen, bevor Mindestvalidierung und Speicherung erfolgreich waren. |
| Prüfevent | Dokumentiert einen fachlichen Prüfungsschritt. | *NachweisGeprüft* | Muss Prüfer, Zeitpunkt, Prüfergebnis und Bezug zur Akte nachvollziehbar machen, aber Datenminimierung beachten. |
| Entscheidungsevent | Dokumentiert, dass eine entscheidungsrelevante Stufe erreicht wurde. | *BescheidErstellt* | Hohe Anforderungen an Integrität, Nachweisbarkeit und Korrekturmöglichkeiten. |
| Zahlungsevent | Signalisiert Zahlungsreife oder Zahlungsauslösung. | *ZahlungAusgelöst* | Sehr hohe Anforderungen an Idempotenz, Vier-Augen-Prinzip, Berechtigung und fachliche Sperren. |
| Aktenevent | Informiert über Änderungen an der elektronischen Akte. | *AkteAktualisiert* | Nicht das komplette Dokument in Events kopieren; besser Referenzen und Metadaten. |
| Korrekturevent | Korrigiert einen vorherigen fachlichen Zustand. | *BescheidKorrigiert*, *ZahlungStorniert* | Nie historische Events löschen; fachliche Korrektur als neues Event modellieren. |
| Integrationsevent | Dient Systemintegration, nicht zwingend vollständiger Domänenhistorie. | *DmsAkteAngelegt* | Muss klar von internen Domain Events getrennt werden. |
| Sicherheitsevent | Dient Detektion, Audit oder Nachweis. | *UnberechtigterZugriffsversuchErkannt* | In zentrale Protokollierung/Detektion einbinden. |

## 8. Event Notification, Event Carried State Transfer, Event Sourcing und CQRS sauber trennen

**Event Notification** bedeutet: Das Event sagt nur, dass etwas passiert ist. Es enthält meist ID, Typ, Zeitpunkt und minimale Metadaten. Beispiel: *AntragEingegangen* enthält `antragId`, `aktenzeichen`, `timestamp` und `correlationId`. Consumer holen Details bei Bedarf über eine API. Vorteil: Wenig Datenvervielfältigung, geringeres Datenschutzrisiko, einfachere Schemaänderung. Nachteil: Consumer hängen wieder synchron am Quellsystem, wenn sie Details brauchen.

**Event Carried State Transfer** bedeutet: Das Event enthält genug fachlichen Zustand, damit Consumer unabhängig arbeiten können. Beispiel: *BescheidErstellt* enthält Bescheidart, Wirksamkeitsdatum, Empfängerreferenz, Status und relevante Metadaten. Vorteil: Consumer brauchen weniger Rückfragen, Reporting und Projektionen werden einfacher. Nachteil: Daten werden repliziert, Events werden größer, personenbezogene Daten verteilen sich stärker, Versionierung wird kritischer.

**Event Sourcing** bedeutet: Events sind nicht nur Integrationssignale, sondern die eigentliche Quelle der Wahrheit. Der aktuelle Zustand wird durch Replay der Event-Historie rekonstruiert. Microsoft beschreibt Event Sourcing als append-only Store, in dem jedes Event eine logische Änderung repräsentiert und aus dem Zustand über Replay beziehungsweise Rehydration abgeleitet wird. ([learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing))

**CQRS** bedeutet: Schreibmodell und Lesemodell werden getrennt. Das Schreibmodell nimmt Commands entgegen und prüft Fachregeln. Das Lesemodell ist für Abfragen optimiert. Microsoft nennt unabhängige Skalierung, optimierte Datenmodelle und Trennung von Verantwortlichkeiten als Vorteile, weist aber zugleich auf stale data und erhöhte Komplexität hin. ([learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs))

Der häufigste Fehler ist, diese vier Muster in einen Topf zu werfen. Man kann EDA ohne Event Sourcing bauen. Man kann CQRS ohne Events bauen. Man kann Events ohne Kafka nutzen. Man kann Kafka nutzen und trotzdem schlechte fachliche Kopplung erzeugen. Deine Aufgabe als Architekt ist nicht, ein Modewort zu akzeptieren, sondern die gewählte Semantik offenzulegen.

## 9. Event-Namensregeln für Fachverfahren

Gute Event-Namen sind fachlich, vergangenheitsbezogen, konkret und stabil. Sie beschreiben nicht, was ein technisches System tun soll, sondern was in der Fachdomäne bereits geschehen ist. Für Behördenverfahren empfehle ich eine dreiteilige Regel: **Subjekt + fachliche Veränderung + Partizip Perfekt**.

| Aspekt | Details/Erklärung | Gutes Beispiel | Schlechtes Beispiel |
|---|---|---|---|
| Vergangenheitsform | Ein Event ist passiert, nicht befohlen. | *AntragEingegangen* | *AntragEinreichen* |
| Fachsprache statt Technik | Der Fachbereich muss das Event verstehen. | *NachweisGeprüft* | *ValidationCompleted* |
| Keine CRUD-Namen | CRUD beschreibt Technik, nicht Bedeutung. | *AkteGeschlossen* | *AkteUpdated* |
| Konkrete Bedeutung | Das Event muss eine klare fachliche Aussage haben. | *BescheidBekanntgegeben* | *StatusGeändert* |
| Keine Consumer-Namen | Events gehören nicht einem Empfänger. | *ZahlungAusgelöst* | *SAPZahlungSenden* |
| Keine UI-Ereignisse als Domänenereignisse | Klicks sind selten fachliche Tatsachen. | *AntragAbgesendet* | *ButtonClicked* |
| Stabiler Kontext | Der Kontext gehört in Namespace oder Topic. | `leistungen.antrag.AntragEingegangen.v1` | `misc.events` |
| Version bewusst führen | Breaking Changes brauchen neue Version. | `BescheidErstellt.v2` | Feld löschen in `v1` |
| Datenminimierung | Nur notwendige fachliche Daten transportieren. | IDs, Status, Zeitpunkte, Referenzen | kompletter Nachweisinhalt |
| Einheitliches Vokabular | Event-Katalog mit Glossar führen. | *Nachweis*, *Bescheid*, *Akte* | wechselnd *Dokument*, *File*, *Record* |

Für deine Behördenbeispiele wären folgende Event-Namen sauber:

`AntragEingegangen` bedeutet: Ein Antrag wurde technisch und fachlich angenommen und besitzt eine Vorgangsidentität.  
`NachweisGeprüft` bedeutet: Ein eingereichter Nachweis wurde durch eine berechtigte Stelle geprüft und mit Ergebnis versehen.  
`BescheidErstellt` bedeutet: Ein Bescheid wurde im Fachverfahren erzeugt, aber noch nicht zwingend bekanntgegeben.  
`BescheidBekanntgegeben` bedeutet: Der Bescheid wurde zugestellt oder auf dem definierten Bekanntgabekanal bereitgestellt.  
`ZahlungAusgelöst` bedeutet: Die Zahlungsanweisung wurde fachlich freigegeben und an die Zahlungsstrecke übergeben.  
`AkteAktualisiert` bedeutet: Die elektronische Akte wurde um einen fachlich relevanten Bestandteil ergänzt oder verändert.

Wichtig: *BescheidErstellt* und *BescheidBekanntgegeben* sind nicht dasselbe. In Behördenprozessen kann zwischen Erstellung, Freigabe, Zeichnung, Bekanntgabe, Rechtsbehelfsfrist und Bestandskraft fachlich erhebliche Bedeutung liegen. Genau diese Unterschiede müssen Events sichtbar machen.

## 10. Beispiel eines Event-Vertrags

Ein Event-Vertrag sollte nicht nur Payload-Felder enthalten, sondern auch Semantik, Erzeugungszeitpunkt, Erzeuger, Version, Schutzbedarf, Aufbewahrung, Owner, Consumer-Erwartungen und Fehlerverhalten. CloudEvents bietet für solche Interoperabilität einen standardisierten Event-Umschlag; die Spezifikation wurde entwickelt, um Eventdaten in gemeinsamen Formaten über Services, Plattformen und Systeme hinweg zu beschreiben. ([github.com](https://github.com/cloudevents/spec))

```json
{
  "specversion": "1.0",
  "type": "de.bund.fachverfahren.antrag.AntragEingegangen.v1",
  "source": "/fachverfahren/antragsservice",
  "id": "evt-2026-06-13-00000012345",
  "time": "2026-06-13T10:15:30Z",
  "subject": "antrag/ANT-2026-0004711",
  "datacontenttype": "application/json",
  "dataschema": "https://schema.example.gov/events/antrag-eingegangen-v1.json",
  "correlationid": "corr-8f4d2b7c",
  "data": {
    "antragId": "ANT-2026-0004711",
    "aktenzeichen": "AZ-2026-LE-004711",
    "antragsart": "LeistungX",
    "eingangszeitpunkt": "2026-06-13T10:15:12Z",
    "eingangskanal": "OnlinePortal",
    "mandant": "BundesbehoerdeX",
    "schutzbedarf": {
      "vertraulichkeit": "hoch",
      "integritaet": "hoch",
      "verfuegbarkeit": "normal"
    }
  }
}
```

Das Beispiel zeigt eine sinnvolle Trennung: Der CloudEvents-Umschlag beschreibt technische und semantische Metadaten. Die `data`-Struktur enthält fachliche Nutzdaten. Der Schutzbedarf ist hier exemplarisch enthalten; in realen Architekturen muss entschieden werden, ob Schutzbedarf als Event-Metadatum transportiert oder über ein zentrales Informationsklassifikationsmodell referenziert wird. Das BSI stellt Schutzbedarf anhand der Grundwerte Vertraulichkeit, Integrität und Verfügbarkeit fest. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com))

## 11. Idempotenz: Der unterschätzte Pflichtpunkt

Idempotenz bedeutet: Ein Consumer kann dasselbe Event mehrfach erhalten, ohne fachlich falsche Mehrfachwirkungen zu erzeugen. Das ist in EDA kein Sonderfall, sondern Normalbetrieb. Broker, Netzwerke, Retries, Timeouts und Consumer-Neustarts können dazu führen, dass Nachrichten erneut verarbeitet werden. Deshalb muss jeder Consumer fachlich prüfen: Habe ich dieses Event bereits verarbeitet?

Bei *ZahlungAusgelöst* ist Idempotenz kritisch. Ein doppeltes Event darf nicht zwei Auszahlungen erzeugen. Die Zahlungsstrecke braucht deshalb einen fachlichen Idempotency Key, etwa `zahlungsvorgangId` oder `eventId` plus fachlichen Kontext. Bei *AkteAktualisiert* darf ein Dokument nicht mehrfach abgelegt werden. Beim Reporting darf ein Antrag nicht doppelt gezählt werden. Idempotenz ist daher keine rein technische Eigenschaft, sondern eine fachliche Schutzmaßnahme gegen falsche Verwaltungsvorgänge.

Als Reviewfrage formulierst du: **Welche fachliche Wirkung hätte die doppelte Verarbeitung dieses Events, und welcher Mechanismus verhindert sie nachweisbar?**

## 12. Ordering: Reihenfolge immer nur dort garantieren, wo sie fachlich notwendig ist

Viele Teams fordern pauschal „garantierte Reihenfolge“. Das klingt vernünftig, ist aber architektonisch gefährlich, weil globale Ordnung Skalierung und Verfügbarkeit erschwert. Die richtige Frage lautet: **Für welchen Schlüssel muss Reihenfolge garantiert werden?**

Bei einem Antrag ist meist die Reihenfolge pro `antragId` relevant. *AntragEingegangen* muss vor *NachweisGeprüft* verarbeitet werden. *BescheidErstellt* muss vor *BescheidBekanntgegeben* liegen. Aber die Reihenfolge zwischen Antrag A und Antrag B ist meist irrelevant. Bei einer Akte kann die Reihenfolge pro `akteId` relevant sein. Bei Zahlungen pro `zahlungsvorgangId`. Bei einer Person eventuell pro `personId`, wobei dieser Schlüssel wegen Datenschutz und Kopplung sorgfältig zu prüfen ist.

Deine Architekturentscheidung lautet also nicht „Ordering ja/nein“, sondern: **Ordering Scope = Antrag, Akte, Zahlung oder global?** Globales Ordering ist fast immer ein Warnsignal.

## 13. Retry und Dead Letter Queue

Retry bedeutet: Ein fehlgeschlagener Consumer-Versuch wird erneut ausgeführt. Das ist sinnvoll bei temporären Fehlern, etwa wenn das DMS kurz nicht erreichbar ist. Retry ist gefährlich bei permanenten Fehlern, etwa wenn ein Event-Schema ungültig ist oder ein Pflichtfeld fehlt. Ohne Begrenzung entstehen Endlosschleifen, Lastspitzen und verdeckte Prozessstaus.

Eine Dead Letter Queue ist der Auffangort für Nachrichten, die nach definierten Retry-Regeln nicht verarbeitet werden konnten. Aber eine DLQ ist kein Papierkorb. Sie ist ein operativer Arbeitsvorrat mit Verantwortlichkeit. Es muss geregelt sein, wer DLQ-Einträge bewertet, wie lange sie liegen dürfen, welche Fachwirkung blockiert ist, wann ein Incident entsteht und wie Reprocessing kontrolliert erfolgt.

Für Behördenverfahren gilt: Eine wachsende DLQ kann bedeuten, dass Anträge nicht in Akten landen, Zahlungen nicht ausgelöst werden, Bescheide nicht versendet werden oder Berichtszahlen falsch sind. Darum muss die DLQ in Monitoring, Incident Management und Fachprozesssteuerung sichtbar sein.

## 14. Schema Evolution: Events leben länger als Code

Ein Event-Schema ist ein Vertrag. Wenn ein Producer ein Feld entfernt, umbenennt oder semantisch verändert, können Consumer brechen. Schema Evolution ist deshalb Governance-Arbeit. Technisch kann man mit Schema Registry, Versionierung, Kompatibilitätsregeln und Consumer-driven Contracts arbeiten. Fachlich braucht man aber zusätzlich klare Owner: Wer darf ein Event ändern? Wer genehmigt Breaking Changes? Welche Consumer sind betroffen? Wie lange werden alte Versionen unterstützt?

Kompatible Änderungen sind meist neue optionale Felder, zusätzliche Eventtypen oder neue enum-Werte, sofern Consumer robust implementiert sind. Kritische Änderungen sind Feldlöschung, Bedeutungsänderung, Typänderung, Pflichtfeldänderung oder Änderung der fachlichen Auslösebedingung. Fowler nennt Schemaänderungen bei Event Sourcing ausdrücklich als Problemfeld; Microsoft weist bei Event Sourcing ebenfalls darauf hin, dass persistierte Events nicht einfach geändert werden sollten und Schemaänderungen schwierig sein können. ([martinfowler.com](https://martinfowler.com/articles/201701-event-driven.html))

Die praktische Regel lautet: **Ändere nie heimlich die Bedeutung eines bestehenden Events. Erzeuge bei Bedarf eine neue Version oder ein neues Event.**

## 15. Observability: Ohne Sichtbarkeit ist EDA Blindflug

EDA braucht Observability entlang des gesamten Event-Flusses. Bei synchronen APIs sieht man oft direkt, dass ein Aufruf fehlschlägt. Bei asynchronen Events kann ein Vorgang scheinbar erfolgreich sein, obwohl nachgelagerte Verarbeitung hängt. Deshalb brauchst du technische und fachliche Messpunkte.

| Aspekt | Details/Erklärung | Beispiel | Metrik/Signal |
|---|---|---|---|
| Publish-Erfolg | Wurde das Event erfolgreich veröffentlicht? | *AntragEingegangen* in Topic geschrieben | Publish Success Rate |
| Consumer-Lag | Wie weit hängt ein Consumer hinterher? | Reporting verarbeitet Events 30 Minuten verzögert | Consumer Lag |
| DLQ-Bestand | Wie viele Events sind nicht verarbeitbar? | 143 Events in `dms.dlq` | DLQ Count, DLQ Age |
| End-to-End-Latenz | Wie lange dauert der fachliche Fluss? | Antrag bis Aktenanlage | P95/P99 Latenz |
| Korrelation | Können Events einem Vorgang zugeordnet werden? | `correlationId` über Portal, Fachverfahren, DMS | Trace Coverage |
| Fehlerquote | Wie viele Events scheitern je Consumer? | Zahlungsconsumer mit 2 % Fehlern | Error Rate |
| Replay-Fähigkeit | Können Events kontrolliert erneut verarbeitet werden? | Rebuild Reporting-Projektion | Replay Success Rate |
| Fachliche Vollständigkeit | Sind erwartete Folgeereignisse eingetreten? | Jeder *BescheidErstellt* braucht ggf. *BescheidBekanntgegeben* | Process Completion Rate |
| Sicherheitsrelevante Ereignisse | Werden ungewöhnliche Zugriffsmuster erkannt? | Massenhafte fehlgeschlagene Consumer-Zugriffe | Security Alerts |
| Aufbewahrung/Löschung | Werden Logs und Eventdaten regelkonform behandelt? | Löschung nach definierter Frist | Retention Compliance |

Das BSI fordert für die Bundesverwaltung Protokollierung und Detektion, um Cyberangriffe erkennen und behandeln zu können. Das ist für EDA besonders relevant, weil Event-Flüsse selbst Teil der sicherheits- und betriebsrelevanten Infrastruktur werden. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Mindeststandards/PDCA/PDCA_node.html?utm_source=chatgpt.com))

## 16. Anti-Patterns, die du in Reviews sofort erkennen solltest

| Aspekt | Details/Erklärung | Beispiel | Risiko |
|---|---|---|---|
| Event als Command verkleidet | Event fordert eine Aktion an, statt eine Tatsache zu beschreiben. | *ZahlungBitteAusführen* | Unklare Verantwortung, falsche Fehlerbehandlung |
| CRUD-Events ohne Fachbedeutung | Technische Zustandsänderung ersetzt Fachsprache. | *EntityUpdated* | Consumer verstehen Bedeutung nicht |
| Event-Suppe | Alles publiziert alles, ohne Event-Katalog. | 300 Topics ohne Owner | Unbeherrschbare Kopplung |
| Fat Events | Events enthalten zu viele Daten. | Kompletter Antrag inklusive Nachweisen | Datenschutz-, Schutzbedarfs- und Versionierungsrisiko |
| Anämische Events | Events enthalten zu wenig Kontext. | *StatusChanged* ohne Bedeutung | Consumer müssen raten oder synchron nachladen |
| Kein Outbox-Pattern | Datenbank und Broker werden getrennt ohne Absicherung beschrieben. | Antrag gespeichert, Event verloren | Inkonsistente Prozesszustände |
| Keine Idempotenz | Doppelte Events führen zu doppelten Wirkungen. | Zahlung doppelt ausgelöst | Schwerer fachlicher Schaden |
| Globale Reihenfolge | Architektur verlangt vollständige Reihenfolge aller Events. | Alle Anträge über eine Partition | Skalierungs- und Verfügbarkeitsproblem |
| DLQ ohne Prozess | Fehler landen irgendwo, niemand bearbeitet sie. | DLQ wächst wochenlang | Verdeckte Fachprozessausfälle |
| Schema ohne Governance | Producer ändern Payload nach Bedarf. | Feld `status` bekommt neue Bedeutung | Consumer brechen |
| Event Sourcing aus Prestige | Event Store wird eingeführt, obwohl CRUD genügt. | Kleines Stammdatenmodul mit Event Sourcing | Überengineering |
| Broker als Datenbank | Event Log wird als einzige Abfragequelle missbraucht. | UI liest direkt aus Topic | Instabile, schwer wartbare Architektur |
| Fachbereich nicht beteiligt | Events werden rein technisch modelliert. | `DocumentUploadedToS3` | Fehlende fachliche Aussage |
| Keine Schutzbedarfssicht | Events transportieren sensible Daten ohne Klassifikation. | Gesundheits-/Personendaten in breiten Topics | Sicherheits- und Compliance-Risiko |

## 17. Reviewfragen für EDA-Entwürfe

### Fachliche Fragen

Welche fachliche Tatsache beschreibt dieses Event genau? Wann gilt sie als eingetreten? Wer darf dieses Event erzeugen? Ist der Event-Name für Sachbearbeitung und Fachaufsicht verständlich? Welche fachliche Wirkung hat das Event bei jedem Consumer? Darf diese Wirkung verzögert eintreten? Was passiert, wenn das Event doppelt, verspätet oder gar nicht verarbeitet wird? Gibt es eine fachliche Korrektur oder Stornierung? Welche Events sind rechts-, zahlungs- oder bescheidrelevant? Welche Events sind nur technische Integrationssignale?

### Architekturfragen

Warum ist Asynchronität hier besser als ein synchroner Aufruf? Welche Systeme sind Producer, welche Consumer? Gibt es einen Event-Katalog? Gibt es klare Topic-Namen, Versionen und Owner? Ist Event Notification oder Event Carried State Transfer gewählt? Ist Event Sourcing wirklich notwendig oder genügt ein normales Datenmodell plus Integrationsevents? Gibt es CQRS, und falls ja: Wie werden Read Models aktualisiert? Wie wird eventual consistency in der Oberfläche erklärt? Gibt es ein Outbox- oder vergleichbares Konsistenzmuster? Wie werden neue Consumer angebunden, ohne bestehende Producer zu ändern?

### Sicherheits- und Schutzbedarfsfragen

Welche personenbezogenen Daten sind im Event enthalten? Ist Datenminimierung umgesetzt? Welcher Schutzbedarf gilt für Event, Topic, Broker, Consumer und Logs? Wer darf Events lesen, publizieren und erneut verarbeiten? Sind technische Konten und Service Accounts sauber berechtigt? Sind administrative Aktionen am Broker protokolliert? Werden Events verschlüsselt übertragen und gespeichert? Gibt es Mandantentrennung? Sind Aufbewahrung und Löschung definiert? Welche sicherheitsrelevanten Ereignisse werden zentral detektiert?

### Betriebsfragen

Welche SLOs gelten für Event-Verarbeitung? Welche maximale Verzögerung ist fachlich tolerierbar? Wie werden Consumer-Lag, DLQ, Retry-Fehler und Publish-Fehler überwacht? Wer ist zuständig, wenn ein Consumer ausfällt? Gibt es Runbooks? Gibt es Reprocessing-Verfahren? Wie wird verhindert, dass Reprocessing doppelte Fachwirkungen auslöst? Gibt es Lasttests für Broker und Consumer? Wie wird Schema-Kompatibilität vor Deployment geprüft? Wie sieht der Betriebsübergang aus?

### Governancefragen

Wer besitzt den Event-Katalog? Wer genehmigt neue Eventtypen? Wer entscheidet über Breaking Changes? Welche Dokumentationsform ist verbindlich: AsyncAPI, Markdown, Architekturdiagramm, ADR? Gibt es Consumer-driven Contract Tests? Werden Events in Architekturreviews geprüft? Gibt es ein Ausnahmeverfahren für direkte synchrone Kopplung? Wird EDA als Plattformfähigkeit betrieben oder pro Projekt individuell improvisiert?

## 18. Beispiel-Zielbild für Behörden-EDA

Ein belastbares Zielbild würde ich so formulieren:

Das Fachverfahren veröffentlicht fachliche Integrationsevents ausschließlich nach erfolgreicher fachlicher Transaktion. Event-Erzeugung und fachliche Persistenz werden über ein Outbox-Pattern oder ein gleichwertiges Konsistenzmuster abgesichert. Events werden in einem zentralen Event-Katalog beschrieben, versioniert und einem fachlichen Owner zugeordnet. Event-Verträge werden maschinenlesbar dokumentiert, vorzugsweise mit AsyncAPI für Channels, Messages, Operationen und Bindings. AsyncAPI ist dafür geeignet, message-driven APIs protocol-agnostisch zu beschreiben. ([asyncapi.com](https://www.asyncapi.com/docs/reference/specification/latest))

Alle Events enthalten eine eindeutige Event-ID, Event-Typ, Version, Erzeuger, Zeitpunkt, fachlichen Bezug, Correlation ID, Schema-Referenz und klassifizierte Nutzdaten. Wo Interoperabilität über Plattform- und Herstellergrenzen hinweg relevant ist, wird ein standardisierter Umschlag wie CloudEvents geprüft, weil CloudEvents Eventdaten in gemeinsamen Formaten für Interoperabilität beschreibt. ([github.com](https://github.com/cloudevents/spec))

Consumer müssen idempotent arbeiten, definierte Retry-Regeln verwenden und fehlerhafte Nachrichten in eine überwachte Dead Letter Queue überführen. Jede DLQ besitzt Verantwortliche, Bearbeitungsfristen, Runbooks und Reprocessing-Regeln. Event-Verarbeitung wird über Metriken, Logs und Traces überwacht. Correlation IDs ermöglichen eine Ende-zu-Ende-Nachverfolgung über Portal, Fachanwendung, Broker, Consumer und nachgelagerte Systeme.

Für personenbezogene oder schutzbedürftige Daten gilt Datenminimierung. Events transportieren nur die Daten, die für berechtigte Consumer erforderlich sind. Event-Zugriffe werden berechtigt, protokolliert und überwacht. Der Schutzbedarf wird entlang der Grundwerte Vertraulichkeit, Integrität und Verfügbarkeit bewertet. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com))

## 19. Deine Bewertungslogik als Enterprise Architekt

Du bewertest einen EDA-Entwurf nicht zuerst anhand der Broker-Technologie. Ob Kafka, RabbitMQ, Azure Service Bus oder ein anderes Produkt verwendet wird, ist zweitrangig. Zuerst prüfst du fünf Ebenen.

Erstens prüfst du die **fachliche Semantik**: Sind Events echte fachliche Tatsachen oder technische Statusmeldungen? Zweitens prüfst du die **Kopplung**: Welche Systeme müssen voneinander wissen, und welche Abhängigkeiten entstehen trotzdem? Drittens prüfst du die **Konsistenz**: Was passiert bei Verzögerung, Fehler, Duplikat und Reihenfolgeproblem? Viertens prüfst du die **Betriebsfähigkeit**: Gibt es Monitoring, DLQ-Prozesse, Reprocessing, Runbooks und Verantwortliche? Fünftens prüfst du **Governance und Schutzbedarf**: Sind Events klassifiziert, versioniert, dokumentiert, berechtigt und auditierbar?

Die zentrale Korrektur lautet: **EDA ist nicht automatisch modernere Architektur. EDA ist nur dann bessere Architektur, wenn die zusätzliche Komplexität durch fachliche Entkopplung, Skalierbarkeit, Erweiterbarkeit oder Nachvollziehbarkeit gerechtfertigt ist.**

## 20. Praktische Übung

Du bekommst folgenden Mini-Entwurf eines Dienstleisters:

„Nach Eingang eines Online-Antrags sendet das Portal ein Event `ApplicationUpdated` an Kafka. Das DMS, das Reporting und das Zahlungsmodul konsumieren dieses Event. Das Event enthält alle Antragsdaten, alle Nachweise als Base64 und den aktuellen Status. Falls ein Consumer fehlschlägt, wird dreimal retryt. Danach landet das Event in einer DLQ. Event-Versionierung ist nicht vorgesehen, weil JSON flexibel ist. Monitoring wird später ergänzt.“

Deine Aufgabe ist, diesen Entwurf als Enterprise Architekt zu bewerten.

Musterlösung:

Der Event-Name `ApplicationUpdated` ist fachlich unzureichend, weil er nicht beschreibt, welche fachliche Tatsache eingetreten ist. Für den Behördenkontext wäre mindestens zu trennen zwischen *AntragEingegangen*, *AntragGeändert*, *NachweisEingereicht*, *NachweisGeprüft* und *BescheidErstellt*. Der Producer ist vermutlich falsch gewählt: Nicht das Portal sollte das fachliche Event erzeugen, sondern die Fachanwendung nach erfolgreicher Validierung und Speicherung. Sonst können Events entstehen, obwohl der Antrag fachlich nicht angenommen wurde.

Die Payload ist überfrachtet. Alle Antragsdaten und Nachweise als Base64 in einem breit konsumierten Event erhöhen Schutzbedarfs-, Datenschutz-, Speicher- und Versionierungsrisiken. Besser wäre ein minimales Event mit fachlichen Referenzen und nur den Daten, die Consumer wirklich brauchen. Das DMS kann gegebenenfalls über eine berechtigte Schnittstelle Dokumente beziehen. Das Reporting benötigt meist keine vollständigen Nachweise. Das Zahlungsmodul darf erst reagieren, wenn ein zahlungsrelevantes Ereignis wie *ZahlungFreigegeben* oder *ZahlungAusgelöst* vorliegt, nicht schon bei einer allgemeinen Antragsaktualisierung.

Retry und DLQ sind zu vage. Es fehlt die Unterscheidung zwischen temporären und permanenten Fehlern. Es fehlen Backoff-Regeln, maximale Verarbeitungsdauer, Alarmierung, DLQ-Owner, Runbook, Reprocessing-Konzept und fachliche Auswirkungsanalyse. Eine DLQ ohne Prozess ist kein Sicherheitsnetz, sondern ein verdeckter Fehlerstapel.

„JSON ist flexibel“ ist keine Versionierungsstrategie. Gerade weil JSON flexibel ist, können Producer Consumer unbeabsichtigt brechen. Es braucht Schema-Verträge, Kompatibilitätsregeln und Versionierung. Für eine formale Beschreibung der message-driven API eignet sich AsyncAPI; für interoperable Event-Metadaten kann CloudEvents geprüft werden. ([asyncapi.com](https://www.asyncapi.com/docs/reference/specification/latest))

Monitoring „später“ ist ein harter Architekturfehler. In EDA ist Observability kein Zusatz, sondern Teil der Mindestbetriebsfähigkeit. Ohne Consumer-Lag, DLQ-Monitoring, Correlation IDs und fachliche Prozessmetriken kann niemand sicher sagen, ob Anträge vollständig verarbeitet wurden. Im Behördenkontext ist zusätzlich die BSI-Perspektive auf Protokollierung und Detektion zu berücksichtigen. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Mindeststandards/PDCA/PDCA_node.html?utm_source=chatgpt.com))

## 21. Dein prüfbares Ergebnis nach dieser Lektion

Nach dieser Lektion solltest du einen EDA-Entwurf mit folgender Architektenfrage öffnen können: **Welche fachliche Tatsache wird hier entkoppelt, und welche Betriebs-, Konsistenz- und Nachweisanforderungen entstehen dadurch?**

Wenn du diese Frage sauber stellst, rutschst du nicht in Tool-Diskussionen ab. Du bewertest dann nicht „Kafka ja oder nein“, sondern ob die Architektur fachlich trägt. Genau das ist Enterprise-Architecture-Arbeit: Muster nicht bewundern, sondern ihren Nutzen, ihre Kosten, ihre Risiken und ihre Passung zum Behördenprozess sichtbar machen.

Die wichtigste Faustregel lautet: **Events sind Verträge über fachliche Tatsachen. Wer Events schlecht benennt, schlecht versioniert oder schlecht betreibt, verteilt keine Architektur — er verteilt Unsicherheit.**

<>