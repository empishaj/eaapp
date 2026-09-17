## Checkliste: Woran du einen belastbaren Schnittstellenvertrag erkennst

| Aspekt | Details/Erklärung | Beispiel |
|---|---|---|
| Fachlicher Zweck | Die Schnittstelle beschreibt zuerst den Verwaltungsprozess, nicht zuerst den Endpunkt. | „Registerdaten zur Plausibilisierung eines Antrags abrufen.“ |
| Provider und Consumer | Verantwortliche Systeme, Organisationseinheiten und fachliche Eigentümer sind benannt. | Registerdienst als Provider, Fachverfahren als Consumer. |
| Datenobjekte | Fachobjekte, Pflichtfelder, Formate, Codelisten, Semantik und Datenherkunft sind definiert. | Person, Antrag, Dokument, Vorgang, Aktenzeichen. |
| Authentifizierung | Es ist geklärt, wie Systeme oder Benutzer eindeutig identifiziert werden. | mTLS, OAuth2/OIDC, technisches Konto, Zertifikat. |
| Autorisierung | Es ist geklärt, wer welche Operation unter welchen Bedingungen ausführen darf. | Fachverfahren darf nur für berechtigte Fallbearbeitung abrufen. |
| Fehlerbehandlung | Fachliche und technische Fehler sind maschinenlesbar, stabil und nachvollziehbar beschrieben. | `404 REGISTER_ENTRY_NOT_FOUND`, `409 CASE_STATE_INVALID`. |
| Versionierung | Es ist klar, was kompatibel ist, was brechend ist und wie Migration erfolgt. | `/v1/register/persons`, Deprecation-Frist 12 Monate. |
| Betrieb | Verfügbarkeit, Wartungsfenster, Supportzeiten, Eskalation und SLOs sind geregelt. | 99,5 % Monatsverfügbarkeit, Wartung Sonntag 02:00–04:00. |
| Monitoring | Metriken, Logs, Correlation IDs und Alarme sind vertraglich festgelegt. | Latenz p95, Fehlerrate, Timeoutquote, DMS-Übergabestatus. |
| Datenschutz | Zweckbindung, Datenminimierung, Löschfristen, Protokollierung und Zugriffsschutz sind beschrieben. | Nur erforderliche Registerattribute werden übertragen. |
| Änderungsprozess | Änderungen laufen über definierte Prüfung, Freigabe, Test und Kommunikation. | Change Request mit Auswirkungsanalyse und Abnahmetest. |
| Abnahmefähigkeit | Der Vertrag enthält prüfbare Kriterien, nicht nur Absichtserklärungen. | „OpenAPI muss gegen Spectral-Regeln validieren.“ |

## 1. Grundidee: Ein Schnittstellenvertrag ist kein Swagger-File

Ein häufiger Fehler ist die Gleichsetzung von „Schnittstellenvertrag“ mit „OpenAPI-Datei“. Das ist fachlich zu klein gedacht. Eine OpenAPI-Spezifikation beschreibt eine HTTP-API formal und maschinenlesbar; die OpenAPI Specification definiert dafür eine standardisierte, programmiersprachenunabhängige Beschreibung, sodass Menschen und Systeme Fähigkeiten eines Dienstes ohne Quellcodeinsicht verstehen können. ([spec.openapis.org](https://spec.openapis.org/oas/v3.1.1.html?utm_source=chatgpt.com)) Ein Schnittstellenvertrag geht darüber hinaus: Er regelt fachlichen Zweck, Verantwortlichkeiten, Datenbedeutung, Sicherheitsanforderungen, Betriebsregeln, Änderungsprozesse, Datenschutz, Support, Versionierung und Abnahme.

Für Behördenlandschaften ist das entscheidend, weil Schnittstellen selten nur „technische Verbindungen“ sind. Sie verbinden Zuständigkeiten, Rechtsgrundlagen, Fachverfahren, Aktenführung, Registerdaten, Fachprozesse, Sicherheitszonen und Betriebsorganisationen. Genau deshalb muss ein guter Schnittstellenvertrag vier Ebenen abdecken: die fachliche Ebene, die technische Ebene, die Sicherheits- und Datenschutzebene sowie die betriebliche und organisatorische Ebene.

Im deutschen Verwaltungskontext solltest du außerdem prüfen, ob vorhandene Standards genutzt werden müssen oder sinnvoll sind. XÖV-Standards sind Spezifikationen für den Datenaustausch in der öffentlichen Verwaltung beziehungsweise zwischen Verwaltung und ihren Kunden; die KoSIT koordiniert IT-Standards für den Datenaustausch in der öffentlichen Verwaltung. ([xoev.de](https://www.xoev.de/xoev-4987?utm_source=chatgpt.com)) FIT-Connect ist ein Beispiel für standardisierte, sichere Anbindung zwischen Online-Verwaltungsdiensten und IT-Systemen zur Antragsbearbeitung auf Basis einheitlicher Schnittstellen und Standards. ([fitko.de](https://www.fitko.de/produktmanagement/fit-connect?utm_source=chatgpt.com)) Für DMS/eAkte-Kontexte ist zusätzlich relevant, dass xdomea als Standard für den Austausch von Akten, Vorgängen und Dokumenten beschrieben wird. ([xrepository.de](https://www.xrepository.de/api/xrepository/urn%3Axoev-de%3Axdomea%3Akosit%3Astandard%3Axdomea_3.0.0%3Adokument%3ASpezifikation_xdomea_3.0.0%3Adatei%3Axdomea_3-0-0_Spezifikation.pdf?utm_source=chatgpt.com))

## 2. Das mentale Modell: Der Vertrag beantwortet nicht „Wie rufe ich die API auf?“, sondern „Darf, soll und kann dieser Austausch zuverlässig stattfinden?“

Ein Schnittstellenvertrag beginnt mit der Frage: Welches fachliche Ergebnis soll durch den Datenaustausch entstehen? Erst danach kommen Ressourcen, Methoden, Payloads, Statuscodes und technische Protokolle. Bei deinem Beispiel lautet der fachliche Ablauf: Ein Fachverfahren bearbeitet einen Antrag, ruft zur Plausibilisierung Registerdaten ab, erzeugt oder empfängt Dokumente, übergibt diese an ein DMS beziehungsweise eine eAkte und erhält anschließend eine technische oder fachliche Rückmeldung zum Übergabestatus.

Daraus entstehen mindestens zwei Verträge oder ein Vertrag mit zwei Schnittstellenanlagen: Erstens der Vertrag „Registerdatenabruf“ zwischen Fachverfahren und Registerdienst. Zweitens der Vertrag „Dokumentübergabe an DMS/eAkte“ zwischen Fachverfahren und DMS. Wenn die Dokumentübergabe asynchron nachverarbeitet wird, kommt zusätzlich ein Ereignis- oder Statuskanal hinzu, etwa „Dokument übernommen“, „Dokument abgelehnt“, „Vorgang angelegt“ oder „Nachverarbeitung fehlgeschlagen“. Für solche nachrichten- oder eventgetriebenen Schnittstellen ist AsyncAPI relevant, weil die Spezifikation message-driven APIs maschinenlesbar und protokollagnostisch beschreibt. ([asyncapi.com](https://www.asyncapi.com/docs/reference/specification/latest?utm_source=chatgpt.com))

## 3. Die Rollen im Schnittstellenvertrag

| Aspekt | Details/Erklärung | Beispiel |
|---|---|---|
| Fachlicher Owner | Verantwortet Zweck, fachliche Regeln, Datenbedeutung und fachliche Abnahme. | Referat Fachverfahren / Registerfachlichkeit |
| Technischer Provider | Betreibt oder liefert die Schnittstelle. | Registerplattform, DMS-Betreiber |
| Consumer | Nutzt die Schnittstelle und hält Consumer-Pflichten ein. | Fachverfahren Antrag |
| Betrieb | Verantwortet Monitoring, Incident, Wartung, Wiederanlauf und Support. | Plattformbetrieb / Rechenzentrum |
| Informationssicherheit | Prüft Schutzbedarf, Authentifizierung, Autorisierung, Logging und Netzfreigaben. | ISB / Security Architect |
| Datenschutz | Prüft Zweck, Datenumfang, Rechtsgrundlage, Protokollierung und Löschung. | Datenschutzkoordination |
| Architektur | Prüft Zielbildkonformität, Standards, Kopplung, Versionierung und Wiederverwendbarkeit. | Enterprise Architecture / Solution Architecture |
| Lieferant/Dienstleister | Implementiert nach Vorgaben und liefert Nachweise. | Softwarehaus, Integrator, DMS-Hersteller |

Die wichtigste Korrektur: Provider und Consumer sind nicht nur Systeme. In einem belastbaren Vertrag müssen auch Organisationseinheiten, Ansprechpartner, Eskalationswege und Entscheidungsbefugnisse benannt sein. Wenn nur „System A ruft System B“ dokumentiert ist, ist der Vertrag im Störungs- oder Änderungsfall praktisch wertlos.

## 4. Vorlage für einen Schnittstellenvertrag

### 4.1 Dokumentkopf

| Aspekt | Details/Erklärung | Beispiel |
|---|---|---|
| Vertragsname | Eindeutiger Name der Schnittstelle oder Schnittstellenbeziehung. | `Registerdatenabruf und DMS-Übergabe für Antragsverfahren X` |
| Version des Vertrags | Version des Vertragsdokuments, nicht der API. | `1.0.0` |
| Status | Entwurf, in Prüfung, freigegeben, in Betrieb, abgekündigt. | `Freigegeben` |
| Gültigkeitsbereich | Systeme, Organisationen, Umgebungen und Prozesse. | Produktion, Test, Abnahme |
| Ansprechpartner | Fachlich, technisch, Betrieb, Security, Datenschutz. | Owner-Liste mit Rollenpostfächern |
| Anlagen | OpenAPI, AsyncAPI, Datenmodell, Fehlerkatalog, Betriebshandbuch. | `Anlage A: OpenAPI register-v1.yaml` |

### 4.2 Fachlicher Zweck und Prozesskontext

| Aspekt | Details/Erklärung | Beispiel |
|---|---|---|
| Fachlicher Zweck | Warum existiert die Schnittstelle? | Plausibilisierung von Antragsdaten durch Registerabruf. |
| Prozessschritt | Wo im Prozess wird sie genutzt? | Nach Antragseingang, vor fachlicher Entscheidung. |
| Auslöser | Was startet den Austausch? | Sachbearbeitung öffnet Vorgang oder automatischer Regelcheck startet. |
| Ergebnis | Was ist nach erfolgreichem Austausch fachlich erreicht? | Registerdaten liegen als Prüfnachweis im Vorgang vor. |
| Nicht-Ziele | Was leistet die Schnittstelle ausdrücklich nicht? | Keine Massendatenabfrage, keine Datenkorrektur im Register. |

Hier musst du als Architekt besonders sauber sein. „Registerdaten abrufen“ ist noch kein Zweck. Besser ist: „Das Fachverfahren ruft definierte Registerattribute ab, um eine im Antrag angegebene Identität und Anschrift im Rahmen der Vorgangsbearbeitung zu plausibilisieren und den Prüfnachweis revisionssicher im Vorgang abzulegen.“ Damit sind Zweck, Datenumfang, Prozessbezug und Nachweisfunktion deutlich klarer.

### 4.3 Fachliche Datenobjekte

| Aspekt | Details/Erklärung | Beispiel |
|---|---|---|
| Fachobjekt | Fachlich benanntes Objekt, nicht nur technische Klasse. | Antragsteller, Registerauskunft, Dokument, Vorgang |
| Eindeutige Kennung | Stabile ID oder fachlicher Schlüssel. | `caseId`, `registerRequestId`, `documentId` |
| Pflichtfelder | Felder, ohne die die Operation nicht gültig ist. | Aktenzeichen, Dokumenttyp, MIME-Type |
| Codelisten | Verbindliche Wertebereiche. | Dokumenttyp: Antrag, Nachweis, Bescheid |
| Datenherkunft | Quelle der Daten. | Antrag, Register, DMS, Fachverfahren |
| Datenqualität | Validierungsregeln und Toleranzen. | Geburtsdatum ISO-Format, PLZ fünfstellig |
| Schutzbedarf | Fachliche Einordnung nach Vertraulichkeit, Integrität, Verfügbarkeit. | Personenbezogene Registerdaten: hoch zu prüfen |

Datenschutz und Informationssicherheit müssen hier konkret werden. Die DSGVO verlangt bei personenbezogenen Daten unter anderem Zweckbindung, Datenminimierung, Integrität und Vertraulichkeit; Art. 32 verlangt geeignete technische und organisatorische Maßnahmen passend zum Risiko, einschließlich Vertraulichkeit, Integrität, Verfügbarkeit und Belastbarkeit der Systeme. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng?utm_source=chatgpt.com)) Daraus folgt praktisch: Du darfst im Vertrag nicht nur Payload-Felder auflisten, sondern musst erklären, warum diese Felder benötigt werden, wer sie sehen darf, wie sie protokolliert werden und wann sie gelöscht oder archiviert werden.

### 4.4 Technischer Schnittstellentyp

| Aspekt | Details/Erklärung | Beispiel |
|---|---|---|
| Schnittstellenart | REST, SOAP, Message Queue, Event, Datei, Fachstandard. | REST für Register, REST oder xdomea-nahe Übergabe für DMS |
| Protokoll | Transport- und Anwendungsprotokoll. | HTTPS/TLS, AMQP, Kafka, SFTP |
| Spezifikation | Maschinenlesbare Beschreibung. | OpenAPI, AsyncAPI, XML Schema, JSON Schema |
| Umgebung | DEV, TEST, QS, PROD. | Getrennte URLs und Zertifikate |
| Netzwerk | Zonen, Firewalls, Gateway, Mandanten. | API-Gateway in Integrationszone |
| Payload-Format | JSON, XML, PDF/A, Binärdaten, Multipart. | JSON-Metadaten plus PDF/A-Dokument |
| Größenlimits | Maximalgröße, Timeout, Chunking. | Dokument maximal 50 MB |

Bei OpenAPI ist wichtig: Die Datei ist Anlage und Prüfgegenstand, aber der Vertrag ist das übergeordnete Dokument. OpenAPI kann Endpunkte, Schemas, Security Schemes, Responses und Beispiele beschreiben; Sicherheitsanforderungen werden in OpenAPI über Security Schemes und Security Requirements modelliert. ([spec.openapis.org](https://spec.openapis.org/oas/v3.1.1.html?utm_source=chatgpt.com)) Der Vertrag muss zusätzlich regeln, wer Zertifikate ausstellt, wie Schlüssel rotiert werden, wie Consumer freigeschaltet werden und wie ein kompromittiertes technisches Konto gesperrt wird.

### 4.5 Sicherheit: Authentifizierung, Autorisierung, Transport, Nachvollziehbarkeit

| Aspekt | Details/Erklärung | Beispiel |
|---|---|---|
| Authentifizierung | Nachweis der Identität von System, Benutzer oder technischer Komponente. | mTLS für System-zu-System, OIDC für Benutzerkontext |
| Autorisierung | Prüfung der Berechtigung für konkrete Operation und Daten. | Rolle `REGISTER_READ_CASE_CONTEXT` |
| Least Privilege | Nur erforderliche Rechte, keine pauschalen Vollzugriffe. | Consumer darf lesen, nicht ändern |
| Mandantentrennung | Trennung nach Behörde, Organisation, Fachbereich oder Mandant. | Behördenkennung im Token-Claim |
| Transportverschlüsselung | Schutz auf Transportweg. | TLS, Zertifikatsprüfung, keine Klartextkanäle |
| Datenverschlüsselung | Schutz ruhender oder transportierter Dokumente. | Verschlüsselte DMS-Ablage |
| Auditierbarkeit | Nachvollziehbarkeit von Zugriffen und Änderungen. | Audit-Log mit Fallbezug und Zweck |
| Missbrauchserkennung | Erkennung ungewöhnlicher Nutzung. | Rate Limits, Abrufmuster, Alarm bei Massenabruf |

Das BSI formuliert für Identitäts- und Berechtigungsmanagement den Grundsatz, dass der Zugang zu schützenswerten Ressourcen auf berechtigte Benutzende und berechtigte IT-Komponenten einzuschränken ist. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/02_ORP_Organisation_und_Personal/ORP_4_Identitaets_und_Berechtigungsmanagement_Editon_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) Für Schnittstellen heißt das: Nicht nur Menschen, sondern auch Fachverfahren, Batch-Jobs, API-Gateways, DMS-Adapter und technische Konten sind Identitäten. Ein Vertrag ohne technische Identitäten ist unvollständig.

### 4.6 Fehlercodes und Fehlerobjekte

Ein Schnittstellenvertrag braucht einen stabilen Fehlerkatalog. Für HTTP-APIs sollte ein maschinenlesbares Fehlerobjekt verwendet werden. RFC 9457 definiert „Problem Details“ als Format, um maschinenlesbare Fehlerdetails in HTTP-Antworten zu transportieren; RFC 9457 ersetzt dabei RFC 7807. ([rfc-editor.org](https://www.rfc-editor.org/info/rfc9457/?utm_source=chatgpt.com))

| Aspekt | Details/Erklärung | Beispiel |
|---|---|---|
| HTTP-Status | Technische Fehlerklasse. | `400`, `401`, `403`, `404`, `409`, `422`, `429`, `500`, `503` |
| Fachlicher Fehlercode | Stabiler maschinenlesbarer Code. | `REGISTER_ENTRY_NOT_FOUND` |
| Fehlertitel | Kurze menschenlesbare Beschreibung. | „Registereintrag nicht gefunden“ |
| Detail | Konkrete Fehlerbeschreibung ohne sensible Zusatzdaten. | „Zur Anfrage konnte kein eindeutiger Eintrag ermittelt werden.“ |
| Correlation ID | Nachverfolgung über Systeme. | `X-Correlation-ID` |
| Retry-Fähigkeit | Darf der Consumer erneut versuchen? | Ja bei `503`, nein bei `422` |
| Verantwortlichkeit | Wer muss reagieren? | Consumer, Provider, Fachbereich, Betrieb |

Beispiel für ein Fehlerobjekt:

```json id="sa3egf"
{
  "type": "https://api.beispiel.de/problems/register-entry-not-found",
  "title": "Registereintrag nicht gefunden",
  "status": 404,
  "detail": "Zur übermittelten Suchanfrage konnte kein eindeutiger Registereintrag ermittelt werden.",
  "instance": "/register-requests/REQ-2026-000123",
  "code": "REGISTER_ENTRY_NOT_FOUND",
  "correlationId": "9f2e7c4a-6d1e-4f31-9a44-1a88f14c8890",
  "retryable": false
}
```

Wichtig ist die Trennung: HTTP-Statuscodes beschreiben die technische Antwortklasse; fachliche Fehlercodes beschreiben die fachliche Bedeutung. `404` allein reicht nicht, weil unklar bleibt, ob der Endpunkt unbekannt ist, der Registereintrag nicht existiert oder die Behörde keine Leseberechtigung auf diesen Eintrag hat.

### 4.7 Versionierung, Änderung und Deprecation

| Aspekt | Details/Erklärung | Beispiel |
|---|---|---|
| API-Version | Version der technischen Schnittstelle. | `/v1`, Header oder Media Type |
| Vertragsversion | Version des Vertragsdokuments. | `Schnittstellenvertrag 1.2.0` |
| Schemaversion | Version des Datenmodells. | `RegisterResponseSchema 1.1.0` |
| Kompatible Änderung | Consumer müssen nicht angepasst werden. | Optionales neues Feld |
| Brechende Änderung | Consumer müssen angepasst werden. | Pflichtfeld entfernt, Semantik geändert |
| Deprecation | Geregelte Abkündigung. | 12 Monate Parallelbetrieb |
| Migration | Vorgehen für Consumer. | Testfenster, Migrationsleitfaden, Cutover |
| Kommunikationspflicht | Wer wird wann informiert? | 90/60/30-Tage-Regel |

Für dich als Enterprise Architekt ist Versionierung ein Governance-Thema. Eine neue API-Version ist nicht nur eine URL-Frage, sondern eine Abhängigkeitsentscheidung. Wenn zehn Fachverfahren dieselbe Registerschnittstelle nutzen, erzeugt jede brechende Änderung Aufwand in zehn Lieferketten. Deshalb muss ein Vertrag festlegen, welche Änderungen erlaubt sind, wie lange alte Versionen betrieben werden und wer die Kosten und Risiken der Migration trägt.

### 4.8 Betrieb, SLA, SLO, Support und Wartungsfenster

| Aspekt | Details/Erklärung | Beispiel |
|---|---|---|
| Betriebszeit | Wann ist die Schnittstelle regulär verfügbar? | 24/7 oder Mo–Fr 06:00–20:00 |
| Service Level | Vertragliche Zielwerte. | 99,5 % Monatsverfügbarkeit |
| SLO | Internes oder operationalisiertes Qualitätsziel. | p95 Antwortzeit < 800 ms |
| Wartungsfenster | Geplante Nichtverfügbarkeit. | Sonntag 02:00–04:00 |
| Incident-Klassen | Kritikalität und Reaktionszeiten. | P1: kompletter Ausfall, Reaktion 30 Minuten |
| Eskalation | Rollen und Wege. | Betrieb → Provider-Lead → Fachlicher Owner |
| Kapazität | Lastannahmen und Limits. | 20 Requests/Sekunde, 100.000 Abrufe/Tag |
| Rate Limiting | Schutz vor Überlast oder Missbrauch. | `429 TOO_MANY_REQUESTS` |
| Wiederanlauf | Verhalten nach Ausfall. | Consumer wiederholt mit Exponential Backoff |

Ein Fehler, den ich in vielen Organisationen sehe: Es werden SLA-Werte vereinbart, aber keine Messmethode. „99,5 % Verfügbarkeit“ ist ohne Messpunkt, Messintervall, Ausschlüsse, Wartungsfenster und Verantwortlichkeit nicht prüfbar. Besser ist: „Die Verfügbarkeit wird monatlich an der Providerkante des API-Gateways gemessen; geplante Wartungsfenster sind ausgenommen; Fehler `5xx` und Timeouts zählen als Nichtverfügbarkeit; Consumer-Netzwerkfehler außerhalb der Providerzone zählen nicht.“

### 4.9 Logging, Monitoring und Observability

| Aspekt | Details/Erklärung | Beispiel |
|---|---|---|
| Technische Logs | Betriebsrelevante Ereignisse. | Request-ID, Statuscode, Latenz, Consumer-ID |
| Audit-Logs | Nachvollziehbare Zugriffe auf schützenswerte Daten. | Wer/was hat wann welchen Fall abgefragt? |
| Fachliche Ereignisse | Prozesszustände. | Registerauskunft erhalten, Dokument übergeben |
| Correlation | Verbindung über Systemgrenzen. | Gemeinsame Correlation ID über Fachverfahren, Register, DMS |
| Metriken | Messbare Betriebsdaten. | Fehlerrate, p95 Latenz, Queue-Lag |
| Alarme | Schwellenwerte mit Reaktion. | 5xx-Rate > 2 % über 5 Minuten |
| Aufbewahrung | Fristen für Logs und Audits. | Technische Logs 30–90 Tage, Audit nach Vorgabe |
| Zugriffsschutz | Wer darf Logs sehen? | Betrieb sieht Technikdaten, Fachbereich keine Tokens |

Das BSI behandelt Protokollierung als übergreifenden IT-Grundschutz-Baustein und beschreibt Anforderungen, damit sicherheitsrelevante Ereignisse angemessen protokolliert werden können. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/04_OPS_Betrieb/OPS_1_1_5_Protokollierung_Edition_2023.html?utm_source=chatgpt.com)) Für Schnittstellenverträge heißt das: Logs dürfen nicht „irgendwie im System“ entstehen, sondern müssen Zweck, Inhalt, Zugriff, Schutz, Aufbewahrung, Auswertung und Alarmierung geregelt haben. Besonders wichtig: Keine Tokens, Passwörter, vollständigen Personendaten oder Dokumentinhalte unkontrolliert in technischen Logs.

## 5. Beispielvertrag: Registerdatenabruf und Dokumentübergabe an DMS/eAkte

### 5.1 Dokumentkopf

| Aspekt | Details/Erklärung | Beispielvertrag |
|---|---|---|
| Name | Offizieller Name des Vertrags. | Schnittstellenvertrag „Antragsverfahren X – Registerdatenabruf und DMS-Übergabe“ |
| Vertragsversion | Version dieses Dokuments. | 1.0.0 |
| Status | Freigabestand. | Entwurf zur Architekturprüfung |
| Gültig ab | Geplanter Nutzungsbeginn. | 01.10.2026 |
| Provider 1 | Registerschnittstelle. | Zentrales Registersystem R |
| Provider 2 | DMS/eAkte. | DMS-Plattform D |
| Consumer | Aufrufendes Fachverfahren. | Fachverfahren Antrag X |
| Anlagen | Technische Spezifikationen. | OpenAPI Register v1, OpenAPI DMS v1, Fehlerkatalog, Betriebsmodell, Datenfeldkatalog |

### 5.2 Fachlicher Prozess

Das Fachverfahren Antrag X nimmt einen Antrag entgegen. Zur Prüfung der angegebenen Personen- und Anschriftsdaten ruft es definierte Registerattribute beim Registersystem R ab. Die Registerauskunft wird nicht zur unbeschränkten Datenanreicherung genutzt, sondern ausschließlich zur Plausibilisierung des konkreten Vorgangs. Nach fachlicher Prüfung erzeugt das Fachverfahren Dokumente wie Antrag, Nachweis, Prüfvermerk oder Bescheid und übergibt diese mit Metadaten an das DMS/eAkte-System D. Das DMS legt Akte, Vorgang oder Dokument ab und meldet den Übernahmestatus zurück.

### 5.3 Schnittstelle A: Registerdatenabruf

| Aspekt | Details/Erklärung | Beispielvertrag |
|---|---|---|
| Zweck | Plausibilisierung von Antragsdaten. | Abruf definierter Registerattribute für konkreten Vorgang. |
| Operation | Technische Operation. | `POST /v1/register/person-search` |
| Consumer | Aufrufendes System. | Fachverfahren Antrag X |
| Provider | Antwortendes System. | Registersystem R |
| Aufrufart | Synchron oder asynchron. | Synchroner REST-Aufruf |
| Authentifizierung | Systemidentität. | mTLS plus OAuth2 Client Credentials |
| Autorisierung | Zugriffskontrolle. | Scope `register.person.read` und Behördenkennung |
| Request | Suchdaten. | Name, Geburtsdatum, optional Anschrift |
| Response | Registerauskunft. | Eindeutiger Treffer, Mehrfachtreffer, kein Treffer |
| Datenminimierung | Nur erforderliche Attribute. | Keine Rückgabe nicht benötigter Registerattribute |
| Idempotenz | Wiederholbarkeit. | Suchanfrage verändert keine Registerdaten |
| Rate Limit | Schutz vor Überlast. | 20 Requests/Sekunde pro Consumer |
| Timeout | Technische Grenze. | 3 Sekunden Provider-Timeout |
| Fehler | Maschinenlesbare Fehler. | Problem Details nach RFC 9457 |
| Logging | Nachvollziehbarkeit. | Consumer-ID, Fall-ID, Zweck, Ergebnisstatus, keine vollständigen Payloads |

Mini-OpenAPI-Ausschnitt:

```yaml id="1uuj6q"
openapi: 3.1.1
info:
  title: Registerdatenabruf API
  version: 1.0.0
paths:
  /v1/register/person-search:
    post:
      summary: Sucht Registerdaten für einen konkreten Vorgang
      operationId: searchRegisterPerson
      security:
        - oauth2ClientCredentials:
            - register.person.read
      parameters:
        - name: X-Correlation-ID
          in: header
          required: true
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/RegisterPersonSearchRequest"
      responses:
        "200":
          description: Registerauskunft erfolgreich ermittelt
        "400":
          description: Anfrage syntaktisch fehlerhaft
        "403":
          description: Consumer ist für diese Operation nicht berechtigt
        "404":
          description: Kein eindeutiger Registereintrag gefunden
        "429":
          description: Rate Limit überschritten
        "503":
          description: Registerdienst temporär nicht verfügbar
components:
  securitySchemes:
    oauth2ClientCredentials:
      type: oauth2
      flows:
        clientCredentials:
          tokenUrl: https://auth.beispiel.de/oauth2/token
          scopes:
            register.person.read: Lesen definierter Registerattribute
```

Dieser Ausschnitt zeigt nur die technische Anlage. Im Vertrag muss zusätzlich stehen, wer den Scope vergibt, welche Behörde welche Daten abrufen darf, wie lange Audit-Logs aufbewahrt werden, wie Testdaten bereitgestellt werden und wie Missbrauchsmuster erkannt werden.

### 5.4 Schnittstelle B: Dokumentübergabe an DMS/eAkte

| Aspekt | Details/Erklärung | Beispielvertrag |
|---|---|---|
| Zweck | Revisionssichere Übergabe von Dokumenten und Metadaten. | Fachverfahren übergibt Antrag, Nachweise, Bescheid an DMS/eAkte. |
| Operation | Technische Operation. | `POST /v1/dms/cases/{caseId}/documents` |
| Consumer | Aufrufendes Fachverfahren. | Fachverfahren Antrag X |
| Provider | DMS/eAkte. | DMS-Plattform D |
| Dokumentformate | Zulässige Inhalte. | PDF/A, XML-Metadaten, optional Hashwert |
| Metadaten | Akten- und Vorgangsbezug. | Aktenzeichen, Vorgangs-ID, Dokumenttyp, Erstellzeitpunkt |
| Größenlimit | Maximalgröße. | 50 MB pro Dokument |
| Integrität | Nachweis unveränderter Übertragung. | SHA-256-Hash im Metadatensatz |
| Rückmeldung | Übernahmestatus. | `ACCEPTED`, `STORED`, `REJECTED` |
| Fehler | Fachliche Ablehnung. | Dokumenttyp unbekannt, Aktenzeichen ungültig |
| Nachverarbeitung | Asynchron möglich. | Virenprüfung, Formatvalidierung, Ablageindexierung |
| Standardbezug | Prüfen, ob xdomea einschlägig ist. | Austausch von Akten, Vorgängen und Dokumenten |

Mini-Request:

```json id="y69sg2"
{
  "caseId": "CASE-2026-0004711",
  "fileReference": "AZ-2026-12345",
  "documentType": "BESCHEID",
  "createdAt": "2026-10-01T10:15:30Z",
  "mimeType": "application/pdf",
  "contentHash": {
    "algorithm": "SHA-256",
    "value": "f2a1c4..."
  },
  "metadata": {
    "applicantId": "APP-99881",
    "classification": "INTERNAL",
    "retentionCategory": "STANDARD_CASE_FILE"
  }
}
```

Mini-Response bei Annahme:

```json id="o5mt7a"
{
  "transferId": "DMS-TR-2026-000001",
  "caseId": "CASE-2026-0004711",
  "status": "ACCEPTED",
  "correlationId": "9f2e7c4a-6d1e-4f31-9a44-1a88f14c8890",
  "nextStatusExpectedWithinSeconds": 300
}
```

Die saubere fachliche Unterscheidung ist hier: `ACCEPTED` bedeutet nur, dass das DMS die Übergabe angenommen hat. Es bedeutet noch nicht zwingend, dass das Dokument vollständig geprüft, indexiert, virengeprüft und revisionssicher abgelegt wurde. Wenn Nachverarbeitung stattfindet, brauchst du einen Statusabruf oder ein Statusereignis.

### 5.5 Schnittstelle C: Asynchrone DMS-Statusrückmeldung

| Aspekt | Details/Erklärung | Beispielvertrag |
|---|---|---|
| Zweck | Rückmeldung der DMS-Nachverarbeitung. | Dokument wurde abgelegt oder abgelehnt. |
| Art | Event oder Callback. | Event `DocumentStorageCompleted` |
| Producer | Sendendes System. | DMS-Plattform D |
| Consumer | Empfangendes System. | Fachverfahren Antrag X |
| Kanal | Topic, Queue oder Callback-Endpunkt. | `dms.document-status.v1` |
| Schlüssel | Ordnung und Korrelation. | `transferId`, `caseId`, `correlationId` |
| Semantik | Bedeutung des Ereignisses. | Statusänderung, kein Command |
| Fehler | Ablehnungsgrund. | `INVALID_DOCUMENT_TYPE`, `VIRUS_CHECK_FAILED` |
| Wiederholung | Zustellung bei Fehlern. | Retry 5-mal, danach Dead Letter Queue |
| Idempotenz | Doppelte Events zulässig behandeln. | Consumer speichert letzte `eventId` |

Mini-Event:

```json id="2nunil"
{
  "eventId": "evt-2026-00000091",
  "eventType": "DocumentStorageCompleted",
  "eventVersion": "1.0.0",
  "occurredAt": "2026-10-01T10:17:12Z",
  "transferId": "DMS-TR-2026-000001",
  "caseId": "CASE-2026-0004711",
  "status": "STORED",
  "dmsDocumentId": "DMS-DOC-558812",
  "correlationId": "9f2e7c4a-6d1e-4f31-9a44-1a88f14c8890"
}
```

## 6. Mindeststandards für Behörden-Schnittstellenverträge

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Maschinenlesbare Spezifikation | REST-Schnittstellen brauchen eine vollständige OpenAPI-Anlage. | OpenAPI mit Schemas, Responses, Security, Beispielen. | OpenAPI beschreibt HTTP-APIs formal und maschinenlesbar. ([spec.openapis.org](https://spec.openapis.org/oas/v3.1.1.html?utm_source=chatgpt.com)) |
| Event-Spezifikation | Ereignis- oder Messaging-Schnittstellen brauchen AsyncAPI oder gleichwertige Beschreibung. | Channels, Messages, Payloads, Operationen. | AsyncAPI beschreibt message-driven APIs protokollagnostisch. ([asyncapi.com](https://www.asyncapi.com/docs/reference/specification/latest?utm_source=chatgpt.com)) |
| Öffentliche Verwaltungsstandards | XÖV, FIT-Connect oder xdomea sind zu prüfen, wenn der Kontext passt. | DMS/eAkte, Fachverfahrensaustausch, OZG-Anbindung. | XÖV und FIT-Connect dienen standardisiertem Austausch in der Verwaltung. ([xoev.de](https://www.xoev.de/xoev-4987?utm_source=chatgpt.com)) |
| Fehlerstandard | Fehlerobjekte müssen maschinenlesbar und stabil sein. | Problem Details mit `code`, `correlationId`, `retryable`. | RFC 9457 definiert Problem Details und ersetzt RFC 7807. ([rfc-editor.org](https://www.rfc-editor.org/info/rfc9457/?utm_source=chatgpt.com)) |
| Sicherheitsmodell | Technische Identitäten, Benutzerkontext, Rechte und Mandanten müssen geregelt sein. | mTLS, OAuth2, Behördenkennung, Scopes. | BSI: Zugriff auf schützenswerte Ressourcen nur für berechtigte Nutzende und IT-Komponenten. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/02_ORP_Organisation_und_Personal/ORP_4_Identitaets_und_Berechtigungsmanagement_Editon_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Datenschutz | Zweck, Datenumfang, Rechtsgrundlage, Löschung und Protokollzugriff müssen beschrieben sein. | Registerdaten nur zur Vorgangsprüfung. | DSGVO Art. 5 und Art. 32. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng?utm_source=chatgpt.com)) |
| Observability | Correlation, Logs, Metriken, Alarme und Supportwege müssen festgelegt sein. | `X-Correlation-ID`, p95-Latenz, 5xx-Rate. | BSI-Protokollierung und Detektion. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/04_OPS_Betrieb/OPS_1_1_5_Protokollierung_Edition_2023.html?utm_source=chatgpt.com)) |
| Betriebsfähigkeit | SLA/SLO, Wartungsfenster, Eskalation und Wiederanlauf müssen prüfbar sein. | 99,5 % Verfügbarkeit, Wartungsfenster, P1-Reaktion. | Betriebsstandard ist organisationsspezifisch abzunehmen. |
| Änderbarkeit | Versionierung, Deprecation, Migration und Consumer-Kommunikation müssen geregelt sein. | 12 Monate Parallelbetrieb bei brechenden Änderungen. | Architektur-Governance / API-Lifecycle. |
| Abnahme | Vertrag muss prüfbare Liefergegenstände enthalten. | OpenAPI validiert, Testfälle bestanden, Security Review abgeschlossen. | Projekt- und Behördenvorgaben. |

## 7. Review-Checkliste für dich als Enterprise Architekt

| Aspekt | Details/Erklärung | Prüffrage |
|---|---|---|
| Fachlicher Zweck | Ist die fachliche Begründung eindeutig? | Kann ich erklären, warum diese Daten genau jetzt gebraucht werden? |
| Prozessbezug | Ist der Prozessschritt klar? | Vor, während oder nach welcher Fallbearbeitung wird die Schnittstelle genutzt? |
| Provider/Consumer | Sind System- und Organisationsverantwortung getrennt benannt? | Wer entscheidet, wer betreibt, wer reagiert im Incident? |
| Datenmodell | Sind Semantik, Pflichtfelder und Codelisten definiert? | Weiß ein Consumer wirklich, was jedes Feld bedeutet? |
| Datenminimierung | Werden nur notwendige Daten übertragen? | Gibt es Felder „nur zur Sicherheit“? |
| Authentifizierung | Sind Systemidentitäten eindeutig? | Gibt es technische Konten, Zertifikate, Token und Rotationsregeln? |
| Autorisierung | Ist Zugriff fall-, rollen- oder mandantenbezogen begrenzt? | Kann ein Consumer mehr lesen, als er fachlich benötigt? |
| Fehler | Sind Fehler maschinenlesbar und handlungsleitend? | Weiß der Consumer, ob Retry sinnvoll ist? |
| Idempotenz | Sind Wiederholungen sicher? | Was passiert bei Timeout und erneutem Dokumentupload? |
| Versionierung | Sind kompatible und brechende Änderungen definiert? | Was passiert mit alten Consumern? |
| Monitoring | Gibt es Messpunkte und Schwellwerte? | Wo wird Latenz gemessen: Consumer, Gateway oder Provider? |
| Logging | Sind sensible Inhalte aus Logs ausgeschlossen? | Werden Tokens, Dokumentinhalte oder vollständige Registerdaten geloggt? |
| SLA/SLO | Sind Werte messbar und realistisch? | Gibt es Messmethode, Ausschlüsse und Reporting? |
| Datenschutz | Sind Zweck, Rechtsgrundlage, Aufbewahrung und Zugriffsschutz beschrieben? | Kann Datenschutz den Vertrag prüfen, ohne Annahmen zu erraten? |
| Betrieb | Sind Support, Wartung, Eskalation und Notfallverfahren beschrieben? | Wer wird nachts angerufen, wenn die DMS-Übergabe steht? |
| Abnahme | Gibt es überprüfbare Kriterien? | Kann ich objektiv sagen: Vertrag erfüllt oder nicht erfüllt? |

## 8. Typische Fehler und klare Korrektur

| Aspekt | Details/Erklärung | Korrektur |
|---|---|---|
| Swagger statt Vertrag | Es gibt nur eine OpenAPI-Datei, aber keine fachlichen oder betrieblichen Regeln. | OpenAPI als Anlage führen, Vertrag um Zweck, Rollen, Betrieb, Datenschutz und Change erweitern. |
| Unklare Datenbedeutung | Feldnamen sind technisch, aber fachlich nicht erklärt. | Datenfeldkatalog mit Semantik, Herkunft, Pflichtstatus, Codeliste und Beispiel ergänzen. |
| Keine Consumer-Pflichten | Provider-Anforderungen sind beschrieben, Consumer-Verhalten fehlt. | Timeouts, Retries, Idempotenz, Rate Limits und Fehlerverarbeitung verpflichtend regeln. |
| Fehler nur als Text | Fehlerantworten sind freie Texte. | Stabilen Fehlerkatalog mit maschinenlesbaren Codes einführen. |
| Keine fachlichen Fehler | Nur `500`, `400`, `404`; fachliche Bedeutung bleibt unklar. | Fachliche Codes wie `CASE_NOT_ELIGIBLE`, `DOCUMENT_TYPE_UNKNOWN` ergänzen. |
| Keine Correlation ID | Störungen können systemübergreifend nicht verfolgt werden. | Durchgängige `X-Correlation-ID` vertraglich festlegen. |
| Zu breite Berechtigungen | Ein technisches Konto darf zu viel. | Scopes, Rollen, Mandanten und Zweckbindung konkretisieren. |
| Ungeklärte Deprecation | Alte Versionen laufen endlos oder werden plötzlich abgeschaltet. | Parallelbetrieb, Fristen, Migrationsplan und Kommunikationspflicht definieren. |
| SLA ohne Messpunkt | Verfügbarkeit ist vereinbart, aber nicht messbar. | Messpunkt, Intervall, Ausschlüsse und Reporting festlegen. |
| Logging mit sensiblen Inhalten | Payloads oder Tokens landen in Logs. | Log-Policy definieren: technische Metadaten ja, sensible Inhalte nein. |
| DMS-Annahme wird mit Ablage verwechselt | `202 Accepted` wird als endgültig erfolgreiche Ablage interpretiert. | Statusmodell mit `ACCEPTED`, `STORED`, `REJECTED` und Rückmeldung einführen. |
| Idempotenz fehlt | Wiederholte Requests erzeugen Duplikate. | Idempotency-Key oder fachlichen Schlüssel für Dokumentübergaben definieren. |
| Testdaten fehlen | Schnittstelle ist spezifiziert, aber nicht realistisch testbar. | Testdatenkatalog, Negativfälle und Abnahmeszenarien ergänzen. |
| Keine Verantwortlichkeiten | Im Fehlerfall fühlt sich niemand zuständig. | RACI, Eskalationskette und Betriebsübergabe verbindlich machen. |

## 9. Praktisches Vorgehen: So erstellst du einen Schnittstellenvertrag real

### Schritt 1: Fachlichen Prozess schneiden

Du startest nicht mit Endpunkten, sondern mit dem Prozessbild. Zeichne den Ablauf in fünf bis sieben Stationen: Antrag eingegangen, Registerdaten prüfen, Ergebnis bewerten, Dokument erzeugen, Dokument an DMS übergeben, DMS-Nachverarbeitung abwarten, Vorgang fortsetzen. An jede Station schreibst du: Welches System? Welche Daten? Welche Verantwortung? Welcher Fehlerfall?

### Schritt 2: Schnittstellen identifizieren

Danach trennst du bewusst zwischen synchronem Abruf und asynchroner Verarbeitung. Der Registerabruf ist wahrscheinlich synchron, weil die Fachlogik sofort eine Antwort benötigt. Die DMS-Übergabe kann synchron angenommen, aber asynchron verarbeitet werden. Genau diese Unterscheidung verhindert später falsche Zusagen wie „Dokument ist gespeichert“, obwohl nur „Dokument wurde angenommen“ gilt.

### Schritt 3: Fachobjekte definieren

Erstelle einen Datenfeldkatalog. Für jedes Feld brauchst du Name, Bedeutung, Typ, Pflichtstatus, Quelle, Beispiel, Schutzbedarf, Validierungsregel und Lösch-/Aufbewahrungsbezug. Bei Behörden ist das nicht Formalismus, sondern Risikoreduktion. Ein Feld wie `status` ist ohne Codeliste gefährlich, weil jedes System etwas anderes darunter verstehen kann.

### Schritt 4: Sicherheitsmodell beschreiben

Lege fest, ob die Schnittstelle systembezogen, benutzerbezogen oder gemischt autorisiert wird. Bei System-zu-System-Schnittstellen reicht es oft nicht, nur das Fachverfahren zu authentifizieren. Du musst klären, ob zusätzlich Fallkontext, Behördenkennung, Mandant, Rolle oder Zweck im Token beziehungsweise im Audit-Log sichtbar sein müssen.

### Schritt 5: Fehler- und Statusmodell entwerfen

Schreibe zuerst fachliche Fehler auf, nicht technische: kein Treffer, Mehrfachtreffer, Register temporär nicht verfügbar, Dokumenttyp unbekannt, Aktenzeichen ungültig, Virenprüfung fehlgeschlagen, Datei zu groß, Vorgang geschlossen. Danach ordnest du HTTP-Statuscodes und Retry-Regeln zu.

### Schritt 6: Betriebsmodell konkretisieren

Definiere Verfügbarkeit, Latenz, Durchsatz, Wartungsfenster, Supportzeiten, Incident-Klassen, Eskalation, Monitoring und Reporting. Prüfe außerdem, ob die vereinbarten Ziele zum fachlichen Prozess passen. Eine Registerschnittstelle, die während Kernarbeitszeiten ausfällt, kann den gesamten Fachprozess blockieren. Eine DMS-Nachverarbeitung darf eventuell verzögert sein, muss aber zuverlässig nachholbar sein.

### Schritt 7: Versionierung und Änderung regeln

Lege fest, was eine brechende Änderung ist. Beispiele: Pflichtfeld wird neu eingeführt, Feldbedeutung ändert sich, Fehlercode verschwindet, Statussemantik ändert sich, zulässige Dokumenttypen werden eingeschränkt. Danach definierst du Migrationsfristen und Abnahmeschritte.

### Schritt 8: Abnahme formulieren

Eine gute Abnahme ist messbar. Beispiele: OpenAPI validiert ohne Fehler; alle Pflichtbeispiele sind vorhanden; Security Review ist abgeschlossen; Negativtests für `400`, `401`, `403`, `404`, `409`, `422`, `429`, `503` sind bestanden; Monitoring-Dashboard ist vorhanden; Correlation ID ist in allen beteiligten Systemen nachweisbar; DMS-Statusrückmeldung ist mit Duplikat-Event getestet.

## 10. Übung für dich

Du bekommst folgenden Fall: Ein Fachverfahren `AntragOnline` soll vor der Entscheidung eine Registerauskunft abrufen und danach drei Dokumente an die eAkte übergeben: Antrag, Nachweis, Bescheid. Die Registerauskunft darf nur im konkreten Vorgang genutzt werden. Das DMS prüft Dokumente asynchron auf Format, Virusfreiheit und Metadatenvollständigkeit. Bei Fehlern muss das Fachverfahren die Sachbearbeitung informieren.

Deine Aufgabe: Erstelle einen Mini-Schnittstellenvertrag mit genau diesen zehn Abschnitten: Zweck, Provider/Consumer, Prozessschritt, Datenobjekte, Authentifizierung, Autorisierung, Fehlerkatalog, Betriebsanforderungen, Monitoring/Logging, Änderungsprozess. Danach prüfst du deinen Vertrag gegen drei Fragen: Erstens, kann ein Entwickler daraus implementieren? Zweitens, kann der Betrieb daraus überwachen und reagieren? Drittens, kann ein Datenschutz- oder Security-Prüfer daraus Risiken bewerten?

Als Zielantwort sollte bei dir ungefähr Folgendes entstehen: Der Registerabruf ist synchron, lesend, idempotent, fallbezogen autorisiert und mit Problem-Details-Fehlern beschrieben. Die DMS-Übergabe ist zweistufig: Annahme der Übergabe und spätere Statusrückmeldung. Dokumente haben Typ, Aktenzeichen, Hash, MIME-Type und Größenlimit. Das Fachverfahren muss Timeouts, Retry, Idempotency-Key und Statusduplikate beherrschen. Logs enthalten Correlation ID, Consumer-ID, Fallreferenz und Status, aber keine vollständigen Registerdaten und keine Dokumentinhalte.

## 11. Dein Merksatz als Architekt

Ein guter Schnittstellenvertrag macht aus einer technischen Verbindung eine belastbare Vereinbarung zwischen Fachlichkeit, Technik, Sicherheit, Datenschutz und Betrieb. Die entscheidende Architekturleistung liegt nicht darin, einen Endpunkt zu benennen, sondern Verantwortung, Bedeutung, Grenzen, Fehler, Betrieb und Veränderbarkeit so zu beschreiben, dass die Schnittstelle auch unter Last, im Fehlerfall, bei Audits und bei späteren Änderungen tragfähig bleibt. <>