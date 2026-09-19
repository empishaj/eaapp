## Observability-Checkliste für Enterprise Architecture

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Zweck geklärt | Observability dient nicht der Tool-Einführung, sondern der Betriebsfähigkeit eines Fachprozesses. | „Kann eine Registerauskunft fachlich und technisch nachvollzogen werden?“ | OpenTelemetry beschreibt Observability als Fähigkeit, den internen Systemzustand über Telemetriedaten zu verstehen. ([opentelemetry.io](https://opentelemetry.io/docs/what-is-opentelemetry/)) |
| Fachprozess sichtbar | Nicht nur Server überwachen, sondern den Ende-zu-Ende-Vorgang. | Portal → API-Gateway → Fachverfahren → Register → DMS → Datenbank. | OpenTelemetry nennt Traces, Metrics und Logs als zentrale Telemetriedaten. ([opentelemetry.io](https://opentelemetry.io/docs/what-is-opentelemetry/)) |
| Logs strukturiert | Logs müssen maschinenlesbar, korrelierbar und datenschutzgerecht sein. | JSON-Log mit `trace_id`, `case_id_hash`, `service`, `error_code`. | OpenTelemetry beschreibt die Korrelation von Logs mit Trace- und Span-IDs. ([opentelemetry.io](https://opentelemetry.io/docs/concepts/context-propagation/)) |
| Metriken definiert | Metriken messen Verhalten über Zeit: Rate, Fehler, Dauer, Sättigung. | Latenz p95, Fehlerrate, Queue-Länge, DB-Connection-Auslastung. | OpenTelemetry umfasst Erzeugung, Export und Sammlung von Metriken. ([opentelemetry.io](https://opentelemetry.io/docs/what-is-opentelemetry/)) |
| Traces durchgängig | Jeder Request muss über Systemgrenzen hinweg verfolgbar sein. | Eine Anfrage erhält dieselbe Trace-ID vom Portal bis zur Datenbank. | Context Propagation ermöglicht Korrelation über Prozess- und Netzwerkgrenzen hinweg. ([opentelemetry.io](https://opentelemetry.io/docs/concepts/context-propagation/)) |
| Events fachlich nutzbar | Fachliche Ereignisse werden sichtbar, ohne sensible Inhalte offenzulegen. | „Antrag eingereicht“, „Registerabfrage gestartet“, „DMS-Ablage fehlgeschlagen“. | Architekturableitung aus Observability-Grundprinzipien. |
| SLI/SLO/SLA getrennt | Messwert, Zielwert und Zusage dürfen nicht vermischt werden. | SLI: Erfolgsrate. SLO: 99,5 %. SLA: vertragliche Zusage mit Berichtspflicht. | Google SRE betont, dass SLO-Ziele fachliche und produktbezogene Auswirkungen haben. ([sre.google](https://sre.google/sre-book/service-level-objectives/)) |
| Alerting wirkungsorientiert | Alerts müssen handlungsfähig sein, nicht bloß laut. | „Registerschnittstelle p95 > 2 s für 10 Minuten und Fehlerrate > 2 %“. | Incident Management zielt auf schnelle Reaktion und Wiederherstellung. ([atlassian.com](https://www.atlassian.com/incident-management)) |
| Dashboards rollenbasiert | Betrieb, Entwicklung, Service Owner und Leitung brauchen unterschiedliche Sichten. | Executive-Dashboard zeigt Fachprozessverfügbarkeit, nicht JVM-Heap. | SLOs sollten auch Management-Bewertung ermöglichen. ([sre.google](https://sre.google/sre-book/service-level-objectives/)) |
| Runbooks vorhanden | Jeder relevante Alarm braucht Diagnose- und Handlungsanleitung. | „Bei DMS-Timeout zuerst Queue prüfen, dann Provider-Status, dann Notbetrieb.“ | NIST SP 800-61 Rev. 3 betont vorbereitete Incident-Response-Fähigkeiten zur Reduktion von Auswirkungen. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/61/r3/final)) |
| Datenschutz eingeplant | Observability darf keine unnötigen personenbezogenen Daten sammeln. | Aktenzeichen gehasht, keine Namen, keine Dokumentinhalte im Log. | Architektur- und Datenschutzanforderung, insbesondere im Behördenkontext. |
| Abnahme prüfbar | Observability muss als Liefergegenstand und Abnahmekriterium formuliert werden. | „Ein Trace muss Portal, Gateway, Fachverfahren und DMS-Spans enthalten.“ | OpenTelemetry ist kein Backend, sondern Framework/Toolkit; Backend und Visualisierung sind gesondert zu liefern. ([opentelemetry.io](https://opentelemetry.io/docs/what-is-opentelemetry/)) |

## 1. Die Kernidee: Observability ist Betriebsarchitektur, nicht Monitoring-Kosmetik

Observability bedeutet: Ein System ist so gebaut, dass du aus seinen äußeren Signalen zuverlässig ableiten kannst, was intern passiert. Das ist ein entscheidender Unterschied zu klassischem Monitoring. Monitoring fragt oft: „Ist der Server grün?“ Observability fragt: „Warum ist der Fachprozess für den Nutzer langsam, fehlerhaft oder unvollständig?“ Genau deshalb ist Observability ein Architekturthema. Sie muss in Zielarchitektur, Schnittstellenverträge, Datenmodell, Security, Betriebskonzept, Abnahme und Dienstleistersteuerung eingebaut werden.

Der typische Fehler ist, Observability erst am Ende in Form eines Tools zu bestellen: „Wir nehmen dann Grafana, Prometheus, ELK, Splunk, Dynatrace, New Relic oder irgendetwas Ähnliches.“ Das ist zu spät und zu flach gedacht. Ein Tool kann nur anzeigen, was das System vorher sauber erzeugt. Wenn keine Trace-IDs übergeben werden, wenn Logs unstrukturiert sind, wenn fachliche Fehler nicht von technischen Fehlern unterschieden werden, wenn Registeraufrufe keine eindeutigen Fehlerklassen liefern und wenn das DMS nur „500 Internal Server Error“ zurückgibt, dann kann auch das beste Dashboard keine Betriebsfähigkeit herbeizaubern.

Für dich als Enterprise Architekt heißt das: Du definierst nicht nur Zielsysteme und Schnittstellen, sondern auch die Beobachtbarkeit der Zielarchitektur. Ein System, das fachlich kritisch ist, aber im Fehlerfall nicht nachvollziehbar reagiert, ist architektonisch unfertig. Es ist nicht wirklich abnahmebereit, selbst wenn die Oberfläche funktioniert.

## 2. Die wichtigsten Begriffe sauber getrennt

| Aspekt | Details/Erklärung | Beispiel | Architekturentscheidung |
|---|---|---|---|
| Logs | Logs sind einzelne, zeitpunktbezogene Aufzeichnungen über Ereignisse. Gute Logs sind strukturiert, korrelierbar, klassifiziert und sparsam mit sensiblen Daten. | „Registerabfrage fehlgeschlagen, Fehlerklasse TIMEOUT, Trace-ID 123, Fachprozess AntragPruefen.“ | Logging-Standard, Pflichtfelder, Retention, Schutzbedarf, Maskierung. |
| Metriken | Metriken sind aggregierte Messwerte über Zeit. Sie zeigen Trends, Last, Latenz, Fehlerquoten und Ressourcenverbrauch. | p95-Latenz der Registerabfrage, Anzahl Requests pro Minute, Fehlerrate. | Metrikkatalog, SLI-Definition, Aggregationsfenster, Grenzwerte. |
| Traces | Traces zeigen den Weg einer Anfrage durch mehrere Systeme. Ein Trace besteht aus Spans, also Teilabschnitten des Weges. | Portal-Request → Gateway-Span → Fachverfahren-Span → Register-Span → DMS-Span → DB-Span. | Durchgängige Trace-Kontext-Weitergabe über HTTP, Messaging und Batch. |
| Events | Events beschreiben fachliche oder technische Zustandsänderungen. Sie können operational, fachlich oder sicherheitsrelevant sein. | „Dokument abgelegt“, „Registerantwort erhalten“, „Retry gestartet“. | Event-Namenskonvention, Event-Schema, Audit-Abgrenzung. |
| Dashboard | Ein Dashboard verdichtet Telemetrie für eine Zielgruppe. Es ist keine Datensammlung, sondern eine Betriebsansicht. | Fachprozess-Dashboard: Erfolgsquote, Latenz, Fehler nach Schnittstelle. | Rollenbasierte Dashboard-Standards. |
| Alerting | Alerting informiert nur dann, wenn Handeln erforderlich ist. Ein guter Alert hat Schweregrad, Ursache, Auswirkung und Runbook-Link. | „DMS-Ablagefehler > 1 % für 15 Minuten, Auswirkung: Dokumente warten in Queue.“ | Alert-Regeln, Eskalationsmodell, Bereitschaftsprozess. |
| SLI | Service Level Indicator: der konkrete Messwert. | „Anteil erfolgreicher Antragsübermittlungen innerhalb von 3 Sekunden.“ | Welche Messung repräsentiert Nutzer- oder Fachwert? |
| SLO | Service Level Objective: der Zielwert für einen SLI. | „99,5 % der Antragsübermittlungen pro Kalendermonat erfolgreich < 3 Sekunden.“ | Zielwert, Messfenster, Ausschlüsse, Fehlerbudget. |
| SLA | Service Level Agreement: formale Zusage gegenüber Kunde, Auftraggeber oder Fachbereich. | „Portal ist monatlich zu 99,0 % verfügbar, Störungsbericht monatlich.“ | Vertragliche, organisatorische und Berichtspflichten. |
| Error Budget | Erlaubter Anteil an Zielverfehlung innerhalb eines Zeitfensters. | Bei 99,5 % SLO sind 0,5 % Fehlerbudget pro Monat vorhanden. | Release-Steuerung, Stabilisierungspflicht, Risikomanagement. |
| Runbook | Konkrete Handlungsanleitung für Störungen, Diagnosen und Wiederanlauf. | „Wenn Register-Timeout: Statusseite prüfen, Retry-Queue prüfen, Fachbereich informieren.“ | Liefergegenstand, Review, Test im Betriebsübergang. |
| Incident Management | Prozess zur Erkennung, Priorisierung, Bearbeitung, Kommunikation und Nachbereitung von Störungen. | Major Incident bei Ausfall der Registerabfrage während Kernzeit. | Rollen, Eskalation, Kommunikationswege, Post-Incident-Review. |

OpenTelemetry ist dabei besonders relevant, weil es als offenes, herstellerneutrales Framework und Toolkit für Erzeugung, Export und Sammlung von Telemetriedaten wie Traces, Metriken und Logs beschrieben wird; es ist selbst kein Observability-Backend, sondern die Instrumentierungs- und Austauschschicht. ([opentelemetry.io](https://opentelemetry.io/docs/what-is-opentelemetry/)) Für Architekturarbeit ist diese Unterscheidung sehr wichtig: Du forderst nicht „OpenTelemetry statt Monitoring-Tool“, sondern „standardisierte Telemetrieerzeugung und -weitergabe, damit unterschiedliche Backends nutzbar bleiben“.

## 3. Das Behördenbeispiel: Portal → API-Gateway → Fachverfahren → Register → DMS → Datenbank

Nehmen wir einen typischen Behördenvorgang. Ein Nutzer meldet sich im Portal an, ruft einen Vorgang auf, das Portal sendet eine Anfrage an ein API-Gateway, das Gateway leitet an ein Fachverfahren weiter, das Fachverfahren fragt ein externes oder internes Register ab, legt Dokumente im DMS ab und schreibt den Vorgangsstatus in eine Datenbank. Aus Nutzersicht ist das ein einziger Vorgang. Aus technischer Sicht ist es eine Kette abhängiger Systeme. Aus Architektursicht ist genau diese Kette der Gegenstand der Observability.

Wenn der Nutzer eine Fehlermeldung sieht, reicht es nicht zu wissen, dass „irgendwo ein Fehler“ auftrat. Du musst erkennen können, ob der Fehler im Portal, im Gateway, im Fachverfahren, bei der Registerschnittstelle, beim DMS, in der Datenbank, in einem Timeout, in einer Berechtigungsprüfung, in einem Schemafehler oder in einer fachlichen Ablehnung entstanden ist.

| Kettenglied | Was beobachtbar sein muss | Beispielmetriken | Beispiel-Logs/Events | Typische Architekturforderung |
|---|---|---|---|---|
| Portal | Nutzernahe Verfügbarkeit, Ladezeiten, Frontend-Fehler, API-Fehler aus Nutzersicht. | Page Load Time, API Error Rate, Login-Erfolgsquote, Client-Fehler. | `portal.request.started`, `portal.api_call.failed`, Browser-Fehlerklasse. | Portal muss Trace-Kontext erzeugen oder übernehmen und an Gateway weitergeben. |
| API-Gateway | Routing, Authentifizierung, Autorisierung, Quotas, Rate Limits, Antwortzeiten je Route. | Requests pro Route, 4xx/5xx, p95/p99 Latenz, Rejections. | `gateway.auth.failed`, `gateway.route.timeout`, `gateway.rate_limited`. | Gateway muss Trace-ID erhalten, weitergeben und eigene Spans erzeugen. |
| Fachverfahren | Fachliche Verarbeitung, Validierung, Regelprüfung, Orchestrierung abhängiger Systeme. | Business Success Rate, Processing Time, Validation Error Rate, Retry Count. | `case.validation.failed`, `register.call.started`, `dms.store.requested`. | Fachverfahren muss technische und fachliche Fehlerklassen sauber trennen. |
| Registerschnittstelle | Verfügbarkeit, Antwortzeit, fachliche Treffer, technische Fehler, Timeouts, Schemafehler. | Register p95 Latenz, Timeout Rate, Trefferquote, Fehler nach Fehlercode. | `register.timeout`, `register.schema_mismatch`, `register.no_match`. | Schnittstellenvertrag muss technische Fehlercodes, fachliche Antwortcodes und Monitoringdaten enthalten. |
| DMS | Dokumentablage, Abruf, Metadaten, Versionierung, Ablagefehler, Queue-Rückstau. | Store Success Rate, Retrieval Latency, Queue Length, DMS Error Rate. | `dms.document.stored`, `dms.metadata.invalid`, `dms.queue.retry`. | DMS-Integration muss idempotent, retryfähig und beobachtbar sein. |
| Datenbank | Query-Latenz, Connection Pool, Locks, Deadlocks, Fehler, Speicher, Replikationslag. | Query p95, Connection Pool Saturation, Lock Wait Time, Deadlocks. | `db.query.slow`, `db.connection.exhausted`, `db.deadlock`. | Datenbankzugriffe müssen technisch messbar sein, ohne Fachinhalte offenzulegen. |
| Gesamtkette | Ende-zu-Ende-Erfolg, Ende-zu-Ende-Latenz, Fehlerursache, betroffener Fachprozess. | E2E Success Rate, E2E p95, Error Budget Burn Rate, Anzahl betroffener Vorgänge. | `case.submission.completed`, `case.submission.failed`. | Ein fachlicher Vorgang muss über Trace-ID und fachliche Korrelationskennung nachvollziehbar sein. |

Die wichtigste technische Grundlage ist Context Propagation: OpenTelemetry beschreibt, dass Trace-ID und Span-ID zwischen Services weitergegeben werden, damit Signale wie Traces, Logs und Metriken über Prozess- und Netzwerkgrenzen hinweg korreliert werden können. ([opentelemetry.io](https://opentelemetry.io/docs/concepts/context-propagation/)) Für dein Behördenbeispiel heißt das: Jede Anfrage braucht eine durchgängige technische Korrelation. Zusätzlich brauchst du häufig eine fachliche Korrelationskennung, etwa eine gehashte Vorgangs-ID oder eine nicht sprechende Prozessinstanz-ID. Diese darf keine unnötigen personenbezogenen Daten enthalten.

## 4. Logs: Was du als Architekt fordern solltest

Logs sind nicht einfach Textausgaben. In professionellen Behördenarchitekturen sind Logs ein geregelter Datenbestand mit Schutzbedarf, Zweckbindung, Aufbewahrung, Suchbarkeit und klarer operativer Funktion. Schlechte Logs lauten: „Fehler beim Speichern.“ Gute Logs lauten sinngemäß: „DMS-Ablage fehlgeschlagen, Fehlerklasse TIMEOUT, technischer Fehlercode DMS-504, Trace-ID vorhanden, Vorgangsreferenz pseudonymisiert, Retry geplant, nächste Wiederholung in 60 Sekunden.“

| Aspekt | Details/Erklärung | Beispiel | Abnahmekriterium |
|---|---|---|---|
| Struktur | Logs müssen maschinenlesbar sein, vorzugsweise JSON oder vergleichbar strukturiert. | `timestamp`, `level`, `service`, `trace_id`, `span_id`, `error_code`. | Stichprobe zeigt mindestens 95 % strukturierte Logs für definierte Komponenten. |
| Korrelation | Jeder relevante Logeintrag muss Trace-ID und, wo sinnvoll, Span-ID enthalten. | Portal- und DMS-Fehler sind über dieselbe Trace-ID auffindbar. | Für einen Testvorgang sind alle Logeinträge Ende-zu-Ende auffindbar. |
| Fehlerklassen | Fehler müssen technisch und fachlich klassifiziert werden. | `VALIDATION_ERROR`, `AUTHORIZATION_DENIED`, `TIMEOUT`, `DEPENDENCY_UNAVAILABLE`. | Fehlercodes sind dokumentiert und werden in Dashboards gruppierbar dargestellt. |
| Datenschutz | Keine Namen, Dokumentinhalte, vollständigen Aktenzeichen oder Registerinhalte in operativen Logs. | `case_id_hash` statt Klarnamen oder Akteninhalt. | Log-Stichprobe enthält keine unzulässigen Inhaltsdaten. |
| Betriebsnutzen | Logs müssen Diagnose ermöglichen, nicht nur Debugging für Entwickler. | „Welche Schnittstelle, welcher Fehler, welche Auswirkung, welche nächste Aktion?“ | Runbook verweist auf konkrete Suchabfragen im Logsystem. |

Eine starke Architekturvorgabe lautet: „Alle zentralen Services liefern strukturierte, korrelierbare und klassifizierte Logs. Logeinträge enthalten mindestens Zeitstempel, Service, Umgebung, Version, Severity, Trace-ID, Span-ID, Fehlerklasse, technischen Fehlercode und, sofern erforderlich, eine pseudonymisierte fachliche Korrelationskennung. Personenbezogene Inhalte, Dokumentinhalte und vollständige fachliche Identifikatoren dürfen nicht in operativen Logs gespeichert werden.“

## 5. Metriken: Die Betriebsphysik des Systems

Metriken sind die Zahlen, an denen du erkennst, ob ein System gesund ist. Für Architekturarbeit sind vier Familien besonders hilfreich: Traffic, Errors, Duration und Saturation. In der Praxis wird häufig auch mit RED gearbeitet: Rate, Errors, Duration. Für Infrastruktur ergänzt man USE: Utilization, Saturation, Errors.

| Kategorie | Details/Erklärung | Beispielmetriken | Warum relevant |
|---|---|---|---|
| Traffic/Rate | Wie viel passiert? | Requests pro Minute je API-Route, Registerabfragen pro Stunde, Dokumentablagen pro Minute. | Zeigt Last, Nutzung und ungewöhnliche Muster. |
| Errors | Was schlägt fehl? | 5xx-Rate, fachliche Ablehnungen, Timeout Rate, DMS Store Failure Rate. | Trennt technische Störung von fachlicher Ablehnung. |
| Duration | Wie lange dauert es? | p50/p95/p99 Antwortzeit, Ende-zu-Ende-Dauer, DB-Query-Latenz. | Nutzerwirkung zeigt sich oft zuerst in Latenz. |
| Saturation | Wo wird es eng? | Queue-Länge, Connection Pool Usage, Thread Pool Saturation, CPU, Speicher, I/O. | Früherkennung vor Ausfall. |
| Freshness | Wie aktuell sind Daten? | Alter letzter Registersync, Replikationslag, letztes erfolgreiches Batchfenster. | Kritisch bei Registern, Berichten und Datenplattformen. |
| Correctness | Ist das Ergebnis fachlich plausibel? | Anteil unvollständiger Vorgänge, Anzahl DMS-Metadatenfehler, Validierungsfehler je Regel. | Behördenprozesse scheitern nicht nur technisch, sondern oft fachlich-operativ. |

Beispielhafte Architekturforderung: „Für jede synchrone Schnittstelle sind mindestens Request Rate, Erfolgsrate, technische Fehlerrate, fachliche Ablehnungsrate, p50/p95/p99-Latenz und Timeout Rate zu erfassen. Für jede asynchrone Verarbeitung sind Queue-Länge, Verarbeitungsrate, Retry-Anzahl, Dead-Letter-Anzahl und Alter des ältesten unbearbeiteten Elements zu erfassen.“

## 6. Traces: Der Röntgenblick durch die Behördenkette

Traces sind für verteilte Architekturen unverzichtbar. Ohne Tracing siehst du vielleicht, dass das Portal langsam ist. Mit Tracing siehst du, dass die Portalantwort langsam ist, weil das Fachverfahren 200 ms braucht, die Registerschnittstelle 2,7 Sekunden wartet, das DMS zweimal retryt und die Datenbank am Ende 80 ms benötigt.

| Trace-Span | Erwartete Attribute | Beispiel | Nutzen |
|---|---|---|---|
| Portal-Span | Route, Nutzerkanal, Session-Typ, Trace-ID. | `POST /antrag/einreichen` | Nutzernahe Sicht auf Vorgang. |
| Gateway-Span | Route, Auth-Ergebnis, Mandant, Downstream-Service. | `gateway.route=fv-case-api` | Erkennt Routing-, Auth- und Quota-Probleme. |
| Fachverfahren-Span | Fachprozess, Regelprüfung, externer Aufruf, Version. | `process=caseSubmission` | Zeigt Orchestrierungslogik. |
| Register-Span | Registername, Operation, Timeout, Ergebniscode. | `register.operation=lookupPersonStatus` | Erkennt externe Abhängigkeiten. |
| DMS-Span | Operation, Dokumenttyp, Metadatenvalidierung, Retry. | `dms.operation=storeDocument` | Erkennt Ablage- und Metadatenprobleme. |
| DB-Span | Query-Typ, Tabelle/Repository, Dauer, Fehlerklasse. | `repository.saveCaseStatus` | Erkennt Persistenzengpässe. |

Wichtig ist: Tracing darf nicht bedeuten, dass Fachinhalte massenhaft in Telemetriedaten landen. Trace-Attribute müssen bewusst modelliert werden. Du brauchst genug Kontext für Diagnose, aber nicht mehr. Besonders im Behördenumfeld ist das eine Architekturentscheidung, keine Entwickler-Laune.

## 7. Events: Fachliche Beobachtbarkeit ohne Fachinhalt preiszugeben

Events sind sinnvoll, wenn du fachliche Zustandsübergänge sichtbar machen möchtest. Ein Event sagt nicht nur „HTTP 200“, sondern „Dokument wurde erfolgreich abgelegt“ oder „Registerabfrage ergab fachlich keinen Treffer“. Das ist für Fachbereiche, Betrieb und Management deutlich verständlicher.

| Event | Bedeutung | Sinnvolle Attribute | Nicht hinein gehört |
|---|---|---|---|
| `case.submission.started` | Vorgang wurde gestartet. | Prozessname, Kanal, Trace-ID, Vorgangstyp. | Name, Adresse, Dokumentinhalt. |
| `register.lookup.completed` | Registerabfrage beendet. | Registername, Ergebnisklasse, Dauer, Trace-ID. | Registerantwort im Klartext. |
| `dms.document.stored` | Dokument wurde abgelegt. | Dokumenttyp, DMS-Operation, Dauer, Metadatenstatus. | Dokumentinhalt, vollständiger Dateiname mit Personendaten. |
| `case.submission.failed` | Vorgang konnte nicht abgeschlossen werden. | Fehlerklasse, betroffene Komponente, Retry-Status. | Freitext mit sensiblen Daten. |
| `case.submission.completed` | Ende-zu-Ende-Prozess erfolgreich. | Gesamtdauer, beteiligte Systeme, Versionen. | Personenbezogene Inhalte. |

Der Architekturtrick ist: Events müssen fachlich genug sein, um Betriebswirkung zu erkennen, aber abstrakt genug, um Datenschutz und Informationssicherheit einzuhalten.

## 8. SLI, SLO, SLA und Error Budget verständlich erklärt

Ein SLI ist der Messwert. Ein SLO ist das Ziel. Ein SLA ist die formale Zusage. Das Error Budget ist der erlaubte Spielraum für Zielverfehlungen. Google SRE weist ausdrücklich darauf hin, dass 100-Prozent-Ziele meist unrealistisch und unerwünscht sind, weil sie Innovation verlangsamen oder zu überkonservativen Lösungen führen können; stattdessen sollte man einen erlaubten Zielverfehlungsanteil, also ein Error Budget, definieren und regelmäßig verfolgen. ([sre.google](https://sre.google/sre-book/service-level-objectives/))

| Begriff | Details/Erklärung | Behördenbeispiel | Architekturwirkung |
|---|---|---|---|
| SLI | Messbarer Indikator für Servicequalität. | „Anteil erfolgreicher Registerabfragen innerhalb von 2 Sekunden.“ | Muss technisch messbar und fachlich relevant sein. |
| SLO | Zielwert für den SLI. | „99 % der Registerabfragen innerhalb der Kernzeit < 2 Sekunden.“ | Beeinflusst Architektur, Kapazität, Caching, Timeout, Retry. |
| SLA | Formale Servicevereinbarung. | „Monatliche Verfügbarkeit 99,0 %, Störungsbericht, Reaktionszeiten.“ | Beeinflusst Vertrag, Dienstleistersteuerung, Reporting. |
| Error Budget | Zulässige Abweichung vom SLO. | Bei 99 % SLO sind 1 % Zielverfehlung im Messfenster erlaubt. | Steuert Release-Risiko und Stabilisierung. |
| Burn Rate | Geschwindigkeit, mit der das Error Budget verbraucht wird. | Fehlerrate steigt stark, Monatsbudget wäre in zwei Tagen verbraucht. | Frühwarnung für Incident oder Change Freeze. |

Ein Executive-tauglicher Satz lautet: „Wir definieren nicht 100 Prozent Verfügbarkeit als Wunschbild, sondern messbare Serviceziele mit klarer Nutzerwirkung. Das Error Budget zeigt, ob wir Stabilitätsspielraum haben oder ob wir Änderungen stoppen und Ursachen beseitigen müssen.“

## 9. Beispiel-SLOs für das Behördenportal

| Aspekt | Details/Erklärung | Beispiel-SLO | Messung |
|---|---|---|---|
| Portalverfügbarkeit | Nutzer kann Fachvorgang starten. | 99,5 % Verfügbarkeit während Kernzeit pro Monat. | Synthetischer Check plus echte Nutzeranfragen. |
| Ende-zu-Ende-Erfolg | Vorgang wird vollständig verarbeitet. | 99,0 % der Einreichungen werden technisch erfolgreich abgeschlossen. | E2E-Event `case.submission.completed` gegen `started`. |
| Registerlatenz | Registerabfrage ist für Gesamtprozess kritisch. | 95 % der Registerabfragen < 2 Sekunden, 99 % < 5 Sekunden. | Trace-Span und Metrik je Registeroperation. |
| DMS-Ablage | Dokument muss zuverlässig abgelegt werden. | 99,7 % erfolgreiche Ablagen ohne manuelle Nacharbeit. | DMS Store Success Rate, Dead-Letter Queue. |
| Datenbank | Persistenz darf nicht Engpass werden. | 95 % der Statusspeicherungen < 150 ms. | DB-Span und Repository-Metrik. |
| Incident-Erkennung | Kritische Störungen werden schnell erkannt. | Kritische Störung innerhalb von 5 Minuten detektiert. | Alert-Zeitpunkt gegen Störungsbeginn. |
| Wiederherstellung | Betrieb reagiert innerhalb definierter Zeit. | Kritische Service-Degradation innerhalb von 30 Minuten mitigiert. | Incident-Zeitlinie, Runbook-Nutzung. |

Wichtig: SLOs sollten nie rein technisch ausgedacht werden. Google SRE betont, dass die Auswahl von SLO-Zielen keine rein technische Aktivität ist, weil Produkt-, Nutzer- und Organisationsauswirkungen einfließen müssen. ([sre.google](https://sre.google/sre-book/service-level-objectives/)) Im Behördenkontext übersetzt du das in Fachkritikalität: Ein Registerabruf für eine gesetzlich fristgebundene Entscheidung ist anders zu bewerten als ein internes Berichtssystem mit nächtlicher Aktualisierung.

## 10. Alerting: Weniger Lärm, mehr Handlungsfähigkeit

Ein Alert ist nur gut, wenn jemand weiß, was zu tun ist. Schlechte Alerts melden Symptome ohne Kontext: „CPU > 80 %“. Gute Alerts melden Wirkung, Komponente, Schweregrad und nächsten Schritt: „Registerabfragen im Fachprozess AntragPruefen haben p95 > 5 Sekunden und Timeout Rate > 3 % seit 10 Minuten; betroffene Vorgänge: 137; Runbook: RB-REG-002.“

| Alert-Typ | Guter Auslöser | Schlechtes Muster | Runbook-Frage |
|---|---|---|---|
| Verfügbarkeit | E2E-Check schlägt mehrfach fehl. | Einzelner Ping fehlgeschlagen. | Ist der Fachprozess wirklich betroffen? |
| Latenz | p95/p99 überschreitet SLO über definiertes Fenster. | Einzelner langsamer Request. | Welche Komponente dominiert die Trace-Dauer? |
| Fehlerquote | Technische Fehlerrate steigt über Schwelle. | Jeder 404 erzeugt Alarm. | Handelt es sich um Nutzerfehler, Fachablehnung oder Systemstörung? |
| Queue-Rückstau | Alter ältester Nachricht überschreitet Grenzwert. | Queue enthält überhaupt Nachrichten. | Wird noch verarbeitet oder steht die Verarbeitung? |
| Error Budget | Burn Rate gefährdet Monatsziel. | Monatsbericht erst nach Ablauf. | Müssen Releases pausiert oder Kapazitäten erhöht werden? |
| Security-relevantes Ereignis | Ungewöhnliche Auth-Fehler oder Zugriffsmuster. | Jeder einzelne Loginfehler. | Muss Incident Response aktiviert werden? |

Incident Management ist der Prozess, mit dem Teams auf ungeplante Ereignisse oder Serviceunterbrechungen reagieren und den Service wieder in den vorgesehenen Betriebszustand bringen. ([atlassian.com](https://www.atlassian.com/incident-management)) Für Behördenarchitekturen bedeutet das: Alerting, Runbooks, Rufbereitschaft, Fachbereichskommunikation und Provider-Eskalation gehören zusammen. Ein Alert ohne Prozess ist nur ein lautes Geräusch.

## 11. Dashboard-Ideen für unterschiedliche Zielgruppen

| Zielgruppe | Dashboard-Zweck | Inhalte | Gute Leitfrage |
|---|---|---|---|
| Executive / Leitung | Betriebsfähigkeit und Wirkung verstehen. | Fachprozessverfügbarkeit, SLO-Status, Error Budget, Major Incidents, Trend. | „Können Bürger, Mitarbeitende oder Partner den Prozess zuverlässig nutzen?“ |
| Service Owner | Servicequalität steuern. | SLI/SLO je Service, Incidents, Change-Korrelation, Provider-Status. | „Welcher Service gefährdet die Fachleistung?“ |
| Betrieb / NOC | Störungen erkennen und priorisieren. | Alerts, Systemstatus, Queue-Rückstau, Abhängigkeiten, Runbook-Links. | „Was muss jetzt bearbeitet werden?“ |
| Entwicklung | Ursachen analysieren. | Traces, Fehlerklassen, Deployment-Versionen, Logs, DB-Latenzen. | „Welche Änderung oder Komponente verursacht das Verhalten?“ |
| Schnittstellenmanagement | Externe und interne Abhängigkeiten überwachen. | Register-SLO, DMS-SLO, API-Fehlercodes, Provider-Latenzen. | „Welche Schnittstelle bricht die Prozesskette?“ |
| Informationssicherheit | Sicherheitsrelevante Ereignisse erkennen. | Auth-Fehler, ungewöhnliche Zugriffsmuster, Policy-Verletzungen. | „Gibt es Hinweise auf Missbrauch, Fehlkonfiguration oder Angriff?“ |

Ein gutes Executive-Dashboard zeigt keine technische Tapete. Es zeigt die Betriebsfähigkeit fachlicher Fähigkeiten. Für dein Beispiel wären gute Executive-Kacheln: „Portal nutzbar“, „Antragseinreichung erfolgreich“, „Registerabfrage stabil“, „DMS-Ablage stabil“, „Fehlerbudget im grünen Bereich“, „offene kritische Incidents“, „Top-3-Risiken der letzten 30 Tage“.

## 12. Konkrete Observability-Anforderungen für Ausschreibung und Zielarchitektur

| Aspekt | Details/Erklärung | Beispielhafte Anforderung | Abnahmekriterium |
|---|---|---|---|
| Ende-zu-Ende-Tracing | Jeder fachliche Vorgang ist über Systemgrenzen nachvollziehbar. | „Der Auftragnehmer implementiert verteiltes Tracing für Portal, API-Gateway, Fachverfahren, Registeradapter, DMS-Adapter und Datenbankzugriffe.“ | Testvorgang erzeugt einen vollständigen Trace mit allen definierten Spans. |
| OpenTelemetry | Telemetrie soll standardisiert und toolneutral erzeugt werden. | „Telemetriedaten sind über OpenTelemetry-kompatible Instrumentierung bereitzustellen.“ | Export über OTLP oder abgestimmtes gleichwertiges Format funktioniert in Testumgebung. |
| Trace-Kontext | Korrelation über Dienste hinweg. | „Trace-Kontext ist bei synchronen HTTP-Aufrufen und asynchronen Nachrichten weiterzugeben.“ | Trace-ID bleibt über Portal, Gateway, Fachverfahren und DMS erhalten. |
| Strukturierte Logs | Maschinelle Analyse und Korrelation. | „Alle zentralen Services erzeugen strukturierte Logs mit Pflichtfeldern.“ | Logprüfung zeigt Pflichtfelder, Severity, Fehlerklasse und Trace-ID. |
| Metrikkatalog | Messbarkeit der Betriebsziele. | „Für jede Schnittstelle sind Rate, Error, Duration und Saturation-Metriken zu liefern.“ | Metriken sind im Observability-Backend sichtbar und dokumentiert. |
| Fachliche Events | Fachprozessstatus sichtbar machen. | „Für zentrale Zustandsübergänge sind fachliche Events ohne sensible Inhaltsdaten zu erzeugen.“ | Ereignisse für Start, Registerantwort, DMS-Ablage und Abschluss nachweisbar. |
| Dashboards | Betriebs- und Managementsicht. | „Der Auftragnehmer liefert rollenbasierte Dashboards für Betrieb, Service Owner und Leitung.“ | Dashboards zeigen definierte SLIs/SLOs und Drilldown. |
| Alerting | Handlungsfähige Alarmierung. | „Alerts müssen Schweregrad, Auswirkung, betroffene Komponente und Runbook-Link enthalten.“ | Testalarm erzeugt korrekte Benachrichtigung mit Runbook. |
| Runbooks | Operative Handlungsfähigkeit. | „Für alle kritischen Alerts sind Runbooks mit Diagnose, Eskalation und Kommunikationsschritten zu liefern.“ | Runbook wird in Betriebsübergabe praktisch geprüft. |
| Betriebsübergabe | Wissenstransfer und Verantwortlichkeit. | „Observability-Artefakte sind Teil der Betriebsübergabe und werden versioniert dokumentiert.“ | Betrieb bestätigt Nutzbarkeit anhand eines simulierten Incidents. |
| Datenschutz | Schutz sensibler Daten. | „Operative Telemetrie darf keine Dokumentinhalte, Klarnamen oder vollständigen Registerdaten enthalten.“ | Stichprobenprüfung und Logging-Konzept sind abgenommen. |
| Providersteuerung | Externe Abhängigkeiten messbar machen. | „Für DMS und Register sind Provider-SLOs, Fehlercodes und Statusinformationen in das Monitoring einzubinden.“ | Schnittstellen-Dashboard zeigt Provider-Latenzen und Fehlerklassen. |

## 13. Beispielbewertung der Behördenkette

| Aspekt | Beobachtung | Bewertung | Architekturmaßnahme |
|---|---|---|---|
| Portal | Frontend misst Ladezeit, aber keine Korrelation zum Backend. | Teilweise beobachtbar. | Trace-Kontext im Frontend/Gateway etablieren. |
| API-Gateway | Technische Metriken vorhanden, aber keine fachliche Route-Zuordnung. | Operativ nutzbar, fachlich schwach. | Routen nach Fachprozess taggen. |
| Fachverfahren | Logs als Freitext, keine Fehlerklassifikation. | Kritische Lücke. | Strukturierte Logs und Fehlerkatalog einführen. |
| Register | Nur Gesamtverfügbarkeit bekannt, keine Operation-spezifische Latenz. | Nicht ausreichend steuerbar. | Operationen einzeln messen: Lookup, Validate, Update. |
| DMS | Fehler landen in Retry-Queue, aber ohne Alter des ältesten Elements. | Rückstau wird zu spät erkannt. | Queue-Age, Retry-Count und Dead-Letter-Metriken ergänzen. |
| Datenbank | Technische DB-Metriken vorhanden, aber nicht mit Fachprozess verknüpft. | Diagnose begrenzt. | DB-Spans mit Repository-Operationen ergänzen. |
| Gesamtprozess | Kein SLO für „Antrag erfolgreich eingereicht“. | Architektur fachlich nicht steuerbar. | E2E-SLI/SLO definieren und Dashboard aufbauen. |

Das ist genau der Punkt, den du auf Executive-Level erklären musst: Einzelne grüne Komponenten beweisen nicht, dass der Fachprozess funktioniert. Betriebsfähigkeit entsteht erst, wenn die Kette als Kette sichtbar ist.

## 14. Typische Fehler, die du klar vermeiden solltest

| Fehler | Warum problematisch | Korrektur |
|---|---|---|
| Tool vor Konzept | Man kauft ein Dashboard, aber erzeugt keine brauchbaren Signale. | Erst Observability-Anforderungen, dann Toolauswahl. |
| Nur Infrastruktur überwachen | CPU und RAM sagen wenig über Fachprozess-Erfolg. | Fachprozess-SLIs definieren. |
| Logs als Freitext | Freitext ist schwer suchbar, kaum aggregierbar und oft uneinheitlich. | Strukturierte Logs mit Pflichtschema. |
| Keine Trace-Weitergabe | Fehlerursachen verschwinden an Systemgrenzen. | Trace-Kontext über HTTP, Messaging und Jobs propagieren. |
| Fachliche und technische Fehler vermischen | Eine fachliche Ablehnung ist kein Systemfehler. | Fehlerklassenmodell definieren. |
| Zu viele Alerts | Teams werden alarmmüde und übersehen echte Störungen. | Alerts an Nutzerwirkung und Runbooks koppeln. |
| Keine Runbooks | Alarm wird erkannt, aber niemand weiß, was zu tun ist. | Runbooks als Pflichtliefergegenstand. |
| Keine SLOs | Betrieb wird subjektiv: „gefühlt langsam“, „gefühlt instabil“. | SLI/SLO je kritischem Fachprozess. |
| 100-Prozent-Ziele | Führt zu unrealistischen Erwartungen oder unverhältnismäßigen Kosten. | Zielwerte mit Error Budget definieren. |
| Datenschutz vergessen | Logs werden selbst zum Risiko. | Datensparsamkeit, Maskierung, Hashing, Retention. |
| Keine Provider-Sicht | Externe Register oder DMS werden Black Boxes. | Schnittstellen-SLOs, Fehlercodes, Statusintegration fordern. |
| Keine Abnahme | Observability bleibt Absichtserklärung. | Testbare Abnahmekriterien in Vertrag und Definition of Done. |

## 15. Executive-Erklärung: Warum Observability ein Architekturthema ist

Eine starke Formulierung für Leitung und Gremien lautet:

„Observability ist die Fähigkeit, die Betriebsfähigkeit eines digitalen Fachprozesses nachweisbar zu machen. In einer modernen Behördenarchitektur reicht es nicht, einzelne Systeme technisch zu überwachen. Entscheidend ist, ob ein Bürger-, Partner- oder Mitarbeiterprozess Ende-zu-Ende funktioniert. Dafür müssen Logs, Metriken, Traces, Events, Dashboards, Alerts und Runbooks bereits in der Zielarchitektur vorgesehen werden. Ohne diese Fähigkeit erkennen wir Störungen zu spät, können Dienstleister schlechter steuern, verlieren Zeit in der Ursachenanalyse und haben keine belastbare Grundlage für Servicequalität, Abnahme und kontinuierliche Verbesserung.“

Noch kürzer für ein Architekturboard:

„Ein System ohne Beobachtbarkeit ist nicht betriebssicher nachweisbar. Es kann funktionieren, aber wir können nicht zuverlässig erklären, warum es funktioniert, wann es kippt und wo wir im Störungsfall eingreifen müssen.“

## 16. Praktische Übung für dich

| Schritt | Aufgabe | Erwartetes Ergebnis |
|---|---|---|
| 1 | Wähle einen Fachprozess: „Antrag über Portal einreichen“. | Prozessname und fachliche Kritikalität sind beschrieben. |
| 2 | Zeichne die Kette: Portal → Gateway → Fachverfahren → Register → DMS → DB. | Ein einfaches Sequenzbild oder eine tabellarische Kette. |
| 3 | Definiere je Kettenglied drei Metriken. | Mindestens Rate, Errors, Duration je Schnittstelle. |
| 4 | Definiere einen Ende-zu-Ende-SLI. | Zum Beispiel: „Anteil erfolgreich abgeschlossener Einreichungen“. |
| 5 | Lege ein SLO fest. | Zum Beispiel: „99 % pro Monat innerhalb der Kernzeit“. |
| 6 | Beschreibe Trace-Anforderungen. | Welche Spans und Attribute sind erforderlich? |
| 7 | Entwerfe ein Executive-Dashboard. | Maximal acht Kacheln mit Fachprozesswirkung. |
| 8 | Formuliere drei Alerts. | Jeder Alert hat Schwelle, Auswirkung und Runbook-Verweis. |
| 9 | Schreibe ein Mini-Runbook für DMS-Ausfall. | Diagnose, Sofortmaßnahme, Eskalation, Kommunikation. |
| 10 | Formuliere Abnahmekriterien. | Ein Testvorgang beweist Logs, Metriken, Trace, Alert und Dashboard. |

Als Musterlösung für einen SLI kannst du formulieren: „Der SLI `case_submission_success_rate` misst den Anteil aller gestarteten Antragseinreichungen, die innerhalb von 60 Sekunden technisch erfolgreich abgeschlossen werden, einschließlich Registerabfrage, DMS-Ablage und Statusspeicherung. Fachliche Ablehnungen aufgrund valider Regeln werden separat gemessen und nicht als technische Fehler gezählt.“

Als Muster-SLO: „Mindestens 99,0 % aller technisch zulässigen Antragseinreichungen werden während der Kernbetriebszeit pro Kalendermonat innerhalb von 60 Sekunden erfolgreich abgeschlossen. Ausgenommen sind angekündigte Wartungsfenster und nachweislich außerhalb der eigenen Betriebsverantwortung liegende Provider-Störungen, sofern diese separat ausgewiesen werden.“

Als Muster-Abnahmekriterium: „Für einen definierten Testvorgang ist nachzuweisen, dass Portal, API-Gateway, Fachverfahren, Registeradapter, DMS-Adapter und Datenbankzugriff in einem gemeinsamen Trace sichtbar sind; alle relevanten Logs enthalten dieselbe Trace-ID; die Metriken für Erfolgsrate, Latenz und Fehlerklasse erscheinen im Dashboard; ein simulierter DMS-Timeout erzeugt einen Alert mit Link auf ein getestetes Runbook.“

## 17. Dein mentales Modell als Enterprise Architekt

Denke Observability künftig in vier Ebenen. Erstens: Fachprozess. Was muss aus Sicht der Behörde funktionieren? Zweitens: Servicekette. Welche Systeme tragen diesen Prozess? Drittens: Telemetrie. Welche Logs, Metriken, Traces und Events beweisen Zustand und Ursache? Viertens: Betriebsreaktion. Welche Dashboards, Alerts, Runbooks und Incident-Prozesse sorgen dafür, dass Menschen richtig handeln können?

Wenn du nur Ebene drei betrachtest, wirst du Tool-Spezialist. Wenn du alle vier Ebenen zusammenführst, wirst du Betriebsarchitekt. Genau das ist im Behördenkontext der Unterschied zwischen „wir haben Monitoring“ und „wir können digitale Verwaltungsleistungen zuverlässig betreiben, erklären und steuern“. <>