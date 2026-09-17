## Checkliste: OpenAPI und AsyncAPI für Enterprise Integration sicher bewerten

* Prüfe zuerst, ob die Schnittstelle synchron per HTTP oder asynchron per Nachricht/Event gedacht ist.  
* Unterscheide fachlich sauber zwischen Ressource, Aktion, Command, Event und technischer Message.  
* Bewerte, ob REST-Ressourcen als fachliche Substantive modelliert sind, nicht als versteckte RPC-Funktionsnamen.  
* Prüfe HTTP-Methoden auf korrekte Semantik: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.  
* Prüfe Statuscodes auf fachliche Aussagekraft, Fehlerbehandlung und Konsistenz.  
* Verlange ein standardisiertes Fehlerobjekt, idealerweise angelehnt an RFC 9457 Problem Details.  
* Prüfe Authentifizierung und Autorisierung getrennt: „Wer bist du?“ ist nicht „Was darfst du?“.  
* Prüfe Schemas auf Pflichtfelder, Datentypen, fachliche Constraints, Beispiele und Änderbarkeit.  
* Prüfe Versionierung nicht nur technisch, sondern als Kompatibilitätsstrategie.  
* Prüfe Pagination, Filterung, Sortierung und Limits bei Listen- und Suchschnittstellen.  
* Prüfe Idempotenz bei Wiederholungen, Timeouts, Retries und doppelten Nachrichten.  
* Prüfe AsyncAPI auf Channels, Messages, Payloads, Producer, Consumer und Betriebsverhalten.  
* Prüfe Schema-Evolution: Welche Änderungen brechen Consumer, welche sind kompatibel?  
* Prüfe Dokumentationsqualität: Kann ein fremdes Team die API korrekt konsumieren, testen und betreiben?  
* Prüfe Behördenkontext: Schutzbedarf, Nachvollziehbarkeit, Auditierbarkeit, Datenschutz, Betrieb und Dienstleistersteuerung.  

## 1. Grundidee: OpenAPI beschreibt HTTP-Schnittstellen, AsyncAPI beschreibt nachrichtengetriebene Schnittstellen

OpenAPI ist der Standard zur formalen Beschreibung von HTTP APIs. Die aktuelle offizielle OpenAPI-Spezifikation 3.2.0 beschreibt eine sprachunabhängige Schnittstellenbeschreibung, mit der Menschen und Maschinen eine HTTP API verstehen können, ohne Quellcode, Zusatzdokumentation oder Netzwerkanalyse zu benötigen. ([spec.openapis.org](https://spec.openapis.org/oas/v3.2.0.html?utm_source=chatgpt.com)) AsyncAPI ist das entsprechende Modell für message-driven APIs; die aktuelle AsyncAPI-Spezifikation 3.1.0 beschreibt nachrichtengetriebene APIs maschinenlesbar und protokollunabhängig, etwa für Kafka, AMQP, MQTT, WebSockets oder HTTP-basierte Messaging-Szenarien. ([asyncapi.com](https://www.asyncapi.com/docs/reference/specification/latest?utm_source=chatgpt.com))

Für dich als Enterprise Architekt ist entscheidend: OpenAPI und AsyncAPI sind nicht einfach „Dokumentationsformate“. Sie sind Architekturverträge. Sie beschreiben, wie Systeme miteinander sprechen, welche Daten ausgetauscht werden, welche Fehler auftreten können, welche Sicherheitsmechanismen gelten und welche Betriebsannahmen ein Consumer treffen darf.

Im Behördenkontext wird diese Unterscheidung besonders wichtig. Eine Registerabfrage ist typischerweise synchron: Ein Fachverfahren fragt ein Register an und erwartet eine Antwort. Ein Statusereignis wie „Nachweis geprüft“ ist typischerweise asynchron: Ein System teilt mit, dass etwas passiert ist, und andere Systeme können darauf reagieren. Eine Dokumentübergabe an ein DMS kann synchron, asynchron oder hybrid sein: Das Fachverfahren übergibt Metadaten und Datei, erhält eine technische Annahmebestätigung und bekommt die spätere Verarbeitungsrückmeldung als Event.

Der erste Denkfehler wäre, jede Integration als REST API zu entwerfen. Der zweite Denkfehler wäre, alles eventgetrieben zu bauen. Gute Architektur entscheidet nicht nach Mode, sondern nach Kopplung, Zeitverhalten, Fehlerbild, fachlicher Verantwortung und Betriebsfähigkeit.

## 2. Das mentale Modell: Anfrage, Befehl, Ereignis, Nachricht

Eine Anfrage fragt Informationen ab. Beispiel: „Gib mir die Meldedaten zu dieser Person.“ Sie passt zu `GET /register/personen/{personId}`. Ein Befehl fordert eine Zustandsänderung an. Beispiel: „Lege dieses Dokument in der Akte ab.“ Er passt häufig zu `POST /akten/{aktenId}/dokumente`. Ein Ereignis berichtet eine fachliche Tatsache aus der Vergangenheit. Beispiel: „Nachweis wurde geprüft.“ Es passt zu einem Event wie `NachweisGeprueft`. Eine Nachricht ist der technische Transportbehälter, in dem ein Command oder Event übermittelt wird.

Das ist eine wichtige Trennung: Ein Event ist fachlich vergangenheitsbezogen. Es sagt nicht „prüfe den Nachweis“, sondern „Nachweis wurde geprüft“. Ein Command ist auffordernd. Es sagt „prüfe den Nachweis“. Eine Query ist lesend. Sie sagt „gib mir den aktuellen Prüfstatus“. Genau diese Unterscheidung brauchst du, um OpenAPI- und AsyncAPI-Entwürfe fachlich zu bewerten.

## 3. OpenAPI verstehen: REST-Ressourcen sauber modellieren

REST-Ressourcen sind fachliche Dinge, über die ein System eine stabile Schnittstelle anbietet. Im Behördenbeispiel sind typische Ressourcen `Antrag`, `Akte`, `Dokument`, `Nachweis`, `Bescheid`, `Zahlung`, `Person`, `Statushistorie` oder `Registerauskunft`.

Eine gute REST-Schnittstelle modelliert nicht technische Funktionen, sondern fachliche Ressourcen. Deshalb ist `GET /personen/{personId}` besser als `GET /holePerson`. `POST /akten/{aktenId}/dokumente` ist besser als `POST /uploadDocumentToDmsAndStartProcessing`. Der Pfad beschreibt die Ressource, die HTTP-Methode beschreibt die Operation.

Die HTTP-Semantik selbst ist standardisiert. RFC 9110 definiert unter anderem Statuscodes als dreistellige Antwortcodes, die das Ergebnis einer HTTP-Anfrage und die Bedeutung der Antwort beschreiben; gültige Statuscodes liegen im Bereich 100 bis 599. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) Daraus folgt für Architekturreviews: Eine API, die immer `200 OK` zurückgibt und Fehler im Body versteckt, verletzt die Erwartung vieler Clients, Gateways, Monitoring-Systeme und Testwerkzeuge.

### OpenAPI-Grundstruktur im Kopf

Eine OpenAPI-Spezifikation enthält im Kern: allgemeine API-Informationen, Server, Pfade, Operationen, Parameter, Request Bodies, Responses, Schemas, Security Schemes und wiederverwendbare Komponenten. Seit OpenAPI 3.1 orientiert sich das Schema Object an JSON Schema Draft 2020-12; JSON Schema selbst ist die zentrale Sprache zur Beschreibung und Validierung von JSON-Strukturen. ([swagger.io](https://swagger.io/specification/?utm_source=chatgpt.com))

Für dich heißt das praktisch: Du prüfst nicht nur, ob eine YAML-Datei syntaktisch valide ist. Du prüfst, ob die Spezifikation einen belastbaren Vertrag darstellt. Ein Vertrag ist belastbar, wenn ein Consumer daraus ableiten kann, wie er authentifiziert, welche Felder er senden darf, welche Antworten kommen können, welche Fehlerformate gelten, welche Limits bestehen und wie Änderungen behandelt werden.

## 4. HTTP-Methoden fachlich richtig verwenden

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| `GET` | Dient zum Lesen einer Ressource oder Sammlung. Ein `GET` darf keinen fachlichen Zustand verändern. | `GET /register/personen/{personId}` liest Registerdaten. | RFC 9110 beschreibt HTTP-Methoden und Semantik. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) |
| `POST` | Dient häufig zum Erzeugen einer untergeordneten Ressource oder zum Auslösen eines Prozesses, dessen Ergebnis nicht vollständig durch eine Ressourcen-ID vorgegeben ist. | `POST /akten/{aktenId}/dokumente` übergibt ein neues Dokument. | RFC 9110; OpenAPI beschreibt HTTP APIs maschinenlesbar. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) |
| `PUT` | Ersetzt eine bekannte Ressource vollständig oder legt sie unter einer bekannten ID an. Wichtig: Der Client kennt die Ziel-URI. | `PUT /antraege/{antragId}/kontaktdaten` ersetzt die Kontaktdaten. | RFC 9110. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) |
| `PATCH` | Ändert Teile einer Ressource. Muss sauber dokumentieren, welches Patch-Format gilt. | `PATCH /antraege/{antragId}` ändert einzelne Felder. | RFC 9110. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) |
| `DELETE` | Entfernt eine Ressource oder markiert sie als gelöscht, je nach Fachdomäne. In Behörden oft heikel wegen Aktenführung und Nachweisbarkeit. | `DELETE /dokumente/{dokumentId}` ist fachlich oft eher eine Stornierung oder Aussonderung als echtes Löschen. | RFC 9110 plus fachliche Aufbewahrungsregeln; konkrete Rechtsgrundlage muss projektspezifisch geprüft werden. |

Als Architekt solltest du besonders wachsam sein, wenn Pfade Verben enthalten: `/createApplication`, `/checkDocument`, `/sendBescheid`, `/updateAkte`. Das ist nicht automatisch falsch, aber es ist ein Signal, dass jemand eine technische Funktion statt einer fachlichen Ressource modelliert hat. Bei Fachverfahren führt das schnell zu unklaren Verantwortlichkeiten und schwer testbaren Schnittstellen.

## 5. Statuscodes: nicht dekorativ, sondern Teil des Vertrags

Statuscodes sind ein Betriebs- und Integrationssignal. Sie helfen Clients, Gateways, Monitoring, Retry-Mechanismen und Menschen. Ein sauberer Entwurf unterscheidet technische Fehler, fachliche Validierungsfehler, Berechtigungsprobleme, nicht gefundene Ressourcen und Konflikte.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| `200 OK` | Erfolgreiche synchrone Antwort mit Inhalt. | Registerauskunft wurde gefunden und zurückgegeben. | RFC 9110. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) |
| `201 Created` | Neue Ressource wurde erzeugt. Der `Location`-Header sollte auf die neue Ressource zeigen. | Dokumentmetadaten wurden angelegt. | RFC 9110. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) |
| `202 Accepted` | Anfrage wurde angenommen, Verarbeitung läuft aber asynchron weiter. | Dokument wurde zur Virenprüfung und DMS-Ablage angenommen. | RFC 9110. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) |
| `400 Bad Request` | Syntaktisch oder strukturell ungültige Anfrage. | Pflichtfeld `aktenId` fehlt oder JSON ist ungültig. | RFC 9110; RFC 9457 für strukturierte Fehlerdetails. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) |
| `401 Unauthorized` | Authentifizierung fehlt oder ist ungültig. Der Begriff ist historisch unscharf, praktisch meint er: nicht gültig authentifiziert. | Kein gültiges Token. | RFC 9110. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) |
| `403 Forbidden` | Identität ist bekannt, aber Berechtigung reicht nicht. | Sachbearbeitung darf diese Akte nicht sehen. | RFC 9110. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) |
| `404 Not Found` | Ressource existiert nicht oder darf absichtlich nicht sichtbar gemacht werden. | Antrag nicht gefunden. | RFC 9110. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) |
| `409 Conflict` | Anfrage widerspricht aktuellem Zustand. | Bescheid soll erstellt werden, obwohl Nachweisprüfung noch offen ist. | RFC 9110. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) |
| `422 Unprocessable Content` | Inhalt ist syntaktisch korrekt, aber fachlich nicht verarbeitbar. | Geburtsdatum liegt in der Zukunft. | RFC 9110 enthält die Statuscode-Systematik; genaue Verwendung muss API-Standard festlegen. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) |
| `429 Too Many Requests` | Rate Limit überschritten. | Register schützt sich vor Überlastung. | RFC 9110 und API-Gateway-Policy. |
| `500/502/503/504` | Server-, Gateway-, Wartungs- oder Timeout-Probleme. | Registerschnittstelle ist nicht erreichbar. | RFC 9110. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) |

Ein typischer Behördenfehler ist die Vermischung von fachlicher Ablehnung und technischem Fehler. „Antrag abgelehnt“ ist kein `500`. „Nachweis ungültig“ ist meist kein technischer Fehler, sondern ein fachliches Ergebnis. „Register nicht erreichbar“ ist dagegen kein fachlicher Status, sondern ein Integrations- oder Betriebsproblem.

## 6. Fehlerobjekte: RFC 9457 als sauberer Standardanker

Für Fehlerantworten solltest du ein konsistentes Fehlerformat verlangen. RFC 9457 definiert „Problem Details for HTTP APIs“ als maschinenlesbares Fehlerformat für HTTP-Antworten und löst RFC 7807 ab. ([rfc-editor.org](https://www.rfc-editor.org/info/rfc9457/?utm_source=chatgpt.com)) Typische Felder sind `type`, `title`, `status`, `detail` und `instance`. Erweiterungen sind möglich, zum Beispiel `correlationId`, `errorCode`, `violations` oder `timestamp`, solange sie sauber dokumentiert werden.

Ein gutes Behörden-Fehlerobjekt sollte fachliche Fehlercodes enthalten, aber keine schutzwürdigen Interna preisgeben. Es sollte einem Client ermöglichen, fachlich zu reagieren: Eingabefehler anzeigen, Retry starten, Eskalation auslösen, Vorgang zurückstellen oder Support mit Correlation ID informieren.

```json id="y001yw"
{
  "type": "https://api.behoerde.example/problems/validation-error",
  "title": "Validierungsfehler",
  "status": 400,
  "detail": "Die Anfrage enthält ungültige Felder.",
  "instance": "/antraege/ANT-2026-000123",
  "correlationId": "7f6d9f0c-8e2a-4c0b-9a18-1b45c1e9a111",
  "violations": [
    {
      "field": "antragsteller.geburtsdatum",
      "code": "DATE_IN_FUTURE",
      "message": "Das Geburtsdatum darf nicht in der Zukunft liegen."
    }
  ]
}
```

Dieses Format ist reviewfähig, weil es technische Diagnose und fachliche Reaktion trennt. Der Client muss keine Freitextmeldung parsen. Monitoring kann Fehlerklassen aggregieren. Support kann über `correlationId` nachverfolgen, was passiert ist.

## 7. Authentifizierung und Autorisierung in OpenAPI

Authentifizierung beantwortet: „Wer oder was ruft auf?“ Autorisierung beantwortet: „Darf diese Identität diese Operation auf diese Ressource ausführen?“ In OpenAPI werden Sicherheitsmechanismen über `securitySchemes` und `security` beschrieben. OpenAPI ist dabei die Beschreibung des Vertrags; die konkrete Durchsetzung erfolgt in IAM, API-Gateway, Anwendung und gegebenenfalls Policy Engine.

Im Behördenkontext musst du mindestens folgende Fälle prüfen: interne Nutzer, externe Antragstellende, Fachaufsicht, Sachbearbeitung, Administratoren, technische Konten, Dienstleister und System-zu-System-Kommunikation. Gerade technische Konten sind kritisch, weil sie oft zu breit berechtigt sind und später niemand mehr weiß, welches System mit welcher Verantwortung aufruft.

Ein guter OpenAPI-Entwurf dokumentiert deshalb nicht nur „Bearer Token erforderlich“, sondern auch Scopes, Rollen, Claims, Mandantenbezug und fachliche Zugriffsvoraussetzungen. Beispiel: `register:person:read` reicht nicht, wenn zusätzlich geprüft werden muss, ob die Sachbearbeitung für genau diesen Vorgang zuständig ist.

## 8. Schemas: Der eigentliche Vertrag liegt in den Daten

Schemas beschreiben die Form der Daten: Felder, Typen, Pflichtfelder, Formate, Enums, Beispiele, Grenzen und Verschachtelungen. JSON Schema Draft 2020-12 ist die aktuelle JSON-Schema-Version und beschreibt Struktur und Validierung von JSON-Daten; OpenAPI 3.1 übernimmt die Parsing-Anforderungen von JSON Schema Draft 2020-12 mit OpenAPI-spezifischen Anpassungen. ([swagger.io](https://swagger.io/specification/?utm_source=chatgpt.com))

Ein schlechtes Schema sieht so aus: überall `string`, kaum Pflichtfelder, keine Beispiele, keine fachlichen Constraints, keine Beschreibung der Codes. Ein gutes Schema sagt: `geburtsdatum` ist ein Datum, `status` hat definierte Werte, `aktenzeichen` folgt einem Muster, `dokumentTyp` kommt aus einem kontrollierten Katalog, `erstelltAm` ist ein Zeitstempel, `personId` ist ein stabiler Identifier und nicht zufällig ein Anzeigename.

Ein wichtiger Punkt: Jedes Schema ist auch ein Governance-Objekt. Wenn ein Feld veröffentlicht ist, kann ein Consumer es verwenden. Wenn du es später entfernst, umbenennst oder semantisch anders befüllst, brichst du Consumer. Deshalb ist Schema-Design Architekturarbeit, nicht nur Implementierungsdetail.

## 9. Versionierung: Nicht Versionsnummern zählen, sondern Kompatibilität verstehen

Versionierung ist keine Kosmetik. Sie beantwortet: Welche Änderung darf ich vornehmen, ohne Consumer zu brechen? Eine kompatible Änderung ist zum Beispiel ein neues optionales Antwortfeld, sofern Consumer unbekannte Felder ignorieren. Eine potenziell brechende Änderung ist das Entfernen eines Feldes, die Änderung eines Datentyps, die Umbenennung eines Enum-Werts, die Verschärfung eines Pflichtfeldes oder die Änderung der fachlichen Bedeutung.

Für Behördenintegration empfehle ich folgende Regel: Major-Versionen nur bei brechenden Vertragsänderungen; Minor- oder Patch-Änderungen für kompatible Erweiterungen; Deprecation-Fristen verbindlich dokumentieren; alte Versionen nicht „heimlich“ abschalten; Consumer aktiv inventarisieren.

Bei REST APIs ist eine Version im Pfad wie `/v1/antraege` einfach zu verstehen, aber nicht immer elegant. Alternativen sind Header- oder Media-Type-Versionierung. Für Behördenumgebungen ist Verständlichkeit oft wichtiger als technische Eleganz. Entscheidend ist, dass Versionierung, Lebenszyklus, Abkündigung und Migrationspflicht dokumentiert sind.

## 10. Pagination, Filterung und Suche

Jede Listen-API braucht eine Antwort auf die Frage: Was passiert bei vielen Treffern? Ohne Pagination entstehen Performance-Probleme, Timeouts, instabile UIs und unkontrollierte Last auf Registern oder Fachverfahren.

Für einfache Fälle reicht `limit` und `offset`. Für große, veränderliche Datenbestände ist Cursor-basierte Pagination meist robuster, weil sich während der Abfrage Daten ändern können. Behördenbeispiel: Eine Suche über Vorgänge, Akten oder Dokumente sollte niemals unbegrenzt alle Treffer liefern.

```yaml id="f89ew5"
parameters:
  - name: limit
    in: query
    schema:
      type: integer
      minimum: 1
      maximum: 100
      default: 25
  - name: cursor
    in: query
    schema:
      type: string
responses:
  '200':
    description: Trefferliste mit Cursor für Folgeseite
```

Wichtig ist auch: Filter und Sortierung müssen fachlich erlaubt sein. Nicht jede Suchmöglichkeit ist zulässig oder sinnvoll. Eine API, die beliebige Wildcard-Suchen über personenbezogene Registerdaten erlaubt, erzeugt Sicherheits-, Datenschutz- und Performance-Risiken.

## 11. Idempotenz: Der Schutz gegen doppelte Ausführung

Idempotenz bedeutet: Eine Operation kann mehrfach ausgeführt werden, ohne dass sich der fachliche Effekt mehrfach wiederholt. Bei `GET` ist das trivialer, bei `POST` nicht. Gerade bei Dokumentübergaben, Zahlungen, Bescheiderstellung und asynchronen Verarbeitungen ist Idempotenz entscheidend.

Beispiel: Ein Client sendet `POST /akten/{aktenId}/dokumente`. Die Verbindung bricht ab. Der Client weiß nicht, ob das Dokument angekommen ist. Ohne Idempotenz sendet er erneut. Plötzlich liegt das Dokument doppelt in der Akte. Mit einem `Idempotency-Key` kann der Server erkennen: Diese fachliche Operation wurde bereits angenommen.

```http id="jrsgpu"
POST /akten/AKT-2026-00042/dokumente
Idempotency-Key: 9c4a2fd8-cc73-4c4e-b3f7-86c9cb1d9e30
Content-Type: application/json
```

Für Enterprise-Reviews ist die Kernfrage: Welche Operationen dürfen bei Retry nicht doppelt wirken? Genau dort brauchst du Idempotenzschlüssel, fachliche Eindeutigkeitsregeln, deduplizierende Verarbeitung oder eindeutig korrelierbare Prozess-IDs.

## 12. Mini-Beispiel OpenAPI: Registerabfrage über REST

Dieses Beispiel zeigt eine synchrone Registerabfrage. Es ist absichtlich klein, aber architektonisch sauber: fachliche Ressource, klare Operation, Security, Statuscodes, Schemas und Fehlerobjekt.

```yaml id="kwxps4"
openapi: 3.1.0
info:
  title: Registerauskunft API
  version: 1.0.0
servers:
  - url: https://api.behoerde.example/register/v1

paths:
  /personen/{personId}:
    get:
      summary: Personendaten aus dem Register abrufen
      operationId: getPersonById
      security:
        - oauth2:
            - register.person.read
      parameters:
        - name: personId
          in: path
          required: true
          schema:
            type: string
          description: Stabiler Identifier der Person im Register
      responses:
        "200":
          description: Person wurde gefunden
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/PersonAuskunft"
        "400":
          description: Ungültige Anfrage
          content:
            application/problem+json:
              schema:
                $ref: "#/components/schemas/Problem"
        "401":
          description: Authentifizierung fehlt oder ist ungültig
        "403":
          description: Keine Berechtigung für diese Registerauskunft
        "404":
          description: Person wurde nicht gefunden
        "429":
          description: Rate Limit überschritten
        "500":
          description: Unerwarteter Serverfehler

components:
  schemas:
    PersonAuskunft:
      type: object
      required:
        - personId
        - familienname
        - vorname
        - geburtsdatum
      properties:
        personId:
          type: string
          example: "PERS-123456789"
        familienname:
          type: string
          example: "Muster"
        vorname:
          type: string
          example: "Mina"
        geburtsdatum:
          type: string
          format: date
          example: "1990-05-17"
        aktualisiertAm:
          type: string
          format: date-time
          example: "2026-06-13T09:30:00Z"

    Problem:
      type: object
      required:
        - type
        - title
        - status
      properties:
        type:
          type: string
          format: uri
        title:
          type: string
        status:
          type: integer
        detail:
          type: string
        instance:
          type: string
        correlationId:
          type: string
          format: uuid

  securitySchemes:
    oauth2:
      type: oauth2
      flows:
        clientCredentials:
          tokenUrl: https://auth.behoerde.example/oauth2/token
          scopes:
            register.person.read: Personendaten aus dem Register lesen
```

Was du daran prüfen solltest: Ist `personId` fachlich stabil? Gibt es Mandanten- oder Zuständigkeitsprüfung? Sind Antwortdaten minimal oder zu breit? Ist `404` zulässig oder muss aus Sicherheitsgründen unscharf geantwortet werden? Gibt es Rate Limits? Gibt es Audit Logging? Werden Correlation IDs durchgereicht?

## 13. Mini-Beispiel OpenAPI: Dokumentübergabe an ein DMS

Dokumentübergabe ist ein gutes Beispiel, weil sie häufig falsch modelliert wird. Der Fehler besteht darin, Upload, Virenprüfung, Metadatenvalidierung, DMS-Ablage, Aktenaktualisierung und Rückmeldung in einen einzigen synchronen Aufruf zu pressen. Besser ist oft: Annahme synchron, Verarbeitung asynchron.

```yaml id="5nkfep"
paths:
  /akten/{aktenId}/dokumente:
    post:
      summary: Dokument zur Ablage in einer Akte übergeben
      operationId: submitDocumentForAkte
      parameters:
        - name: aktenId
          in: path
          required: true
          schema:
            type: string
        - name: Idempotency-Key
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
              type: object
              required:
                - dokumentTyp
                - dateiname
                - inhaltBase64
              properties:
                dokumentTyp:
                  type: string
                  enum: [NACHWEIS, BESCHEID, ANLAGE, SCHREIBEN]
                dateiname:
                  type: string
                  example: "nachweis_wohnort.pdf"
                mimeType:
                  type: string
                  example: "application/pdf"
                inhaltBase64:
                  type: string
                  contentEncoding: base64
      responses:
        "202":
          description: Dokument wurde angenommen und wird asynchron verarbeitet
          content:
            application/json:
              schema:
                type: object
                required:
                  - verarbeitungsId
                  - status
                properties:
                  verarbeitungsId:
                    type: string
                    example: "DOCJOB-2026-000099"
                  status:
                    type: string
                    enum: [ANGENOMMEN]
        "400":
          description: Ungültige Metadaten oder ungültiger Inhalt
        "409":
          description: Akte ist für Dokumentübergabe gesperrt
        "413":
          description: Dokument überschreitet erlaubte Größe
        "415":
          description: Dateityp wird nicht unterstützt
```

Der wichtigste Punkt ist `202 Accepted`: Die API verspricht nicht, dass das Dokument bereits endgültig im DMS liegt. Sie verspricht nur, dass der Verarbeitungsauftrag angenommen wurde. Die endgültige Rückmeldung kann über eine Statusabfrage oder ein Event erfolgen.

## 14. AsyncAPI verstehen: Events, Channels, Messages und Payloads

AsyncAPI beschreibt die asynchrone Kommunikation. Ein Channel ist der logische Kommunikationskanal, etwa ein Kafka Topic oder eine Queue. Eine Message ist die konkrete Nachricht, die über diesen Channel läuft. Der Payload ist der fachliche Inhalt. Eine Operation beschreibt, ob ein System sendet oder empfängt. Die AsyncAPI-Dokumentstruktur enthält unter anderem Root-Elemente wie `info`, `servers`, `channels`, `operations` und `components`. ([asyncapi.com](https://www.asyncapi.com/docs/concepts/asyncapi-document/structure?utm_source=chatgpt.com))

Ein wichtiger Unterschied zu OpenAPI: Bei REST ist der Consumer meist aktiv und fragt an. Bei Events ist der Producer aktiv und veröffentlicht eine Tatsache. Consumer reagieren, ohne dass der Producer sie direkt kennen muss. Das reduziert direkte Kopplung, erhöht aber Anforderungen an Betrieb, Schema-Evolution, Monitoring, Replay, Ordering und Fehlerbehandlung.

AsyncAPI ist protokollunabhängig. Das ist stark, aber auch gefährlich: Die Spezifikation sagt nicht automatisch, ob Kafka, RabbitMQ, AMQP, MQTT oder ein anderes System fachlich richtig ist. Du musst zusätzlich Betriebssemantik prüfen: Gibt es Ordering? Gibt es Retention? Gibt es Dead Letter Queues? Gibt es Consumer Groups? Gibt es Replay? Gibt es garantierte Zustellung oder nur Best Effort?

## 15. Event-Namen im Behördenkontext

Ein gutes Event benennt eine fachliche Tatsache in der Vergangenheit. Es ist kein technischer Logeintrag und kein versteckter Befehl.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Vergangenheitsform | Events beschreiben, was passiert ist. | `AntragEingegangen`, `NachweisGeprueft`, `BescheidErstellt` | AsyncAPI beschreibt message-driven APIs; fachliche Namenskonvention ist Architekturstandard. ([asyncapi.com](https://www.asyncapi.com/docs/reference/specification/latest?utm_source=chatgpt.com)) |
| Fachsprache | Namen kommen aus der Domäne, nicht aus der Implementierung. | Gut: `AkteAktualisiert`; schlecht: `DmsCallbackReceived` | Domänenmodellierung und API-Governance. |
| Keine Commands als Events | Ein Event fordert nicht auf, sondern informiert. | Gut: `ZahlungAusgeloest`; schlecht: `LoeseZahlungAus` | Architekturprinzip Command/Event-Trennung. |
| Stabilität | Event-Namen dürfen nicht bei jeder Implementierungsänderung wechseln. | `NachweisGeprueft` bleibt stabil, auch wenn Prüfservice ersetzt wird. | API-Lifecycle-Management. |
| Versionierbarkeit | Brechende Payload-Änderungen brauchen Versionierungsstrategie. | `antrag.status.v1` oder Message-Version im Schema. | AsyncAPI unterstützt API-Beschreibung und Versionierung über Dokument-/Info-Strukturen; konkrete Versionierungsstrategie muss festgelegt werden. ([asyncapi.com](https://www.asyncapi.com/docs/concepts/asyncapi-document/structure?utm_source=chatgpt.com)) |

Gute Event-Namen wären: `AntragEingegangen`, `NachweisPruefungAbgeschlossen`, `NachweisAbgelehnt`, `BescheidErstellt`, `BescheidVersandt`, `ZahlungAusgeloest`, `AkteAktualisiert`, `DokumentAblageFehlgeschlagen`.

Schlechte Event-Namen wären: `UpdateStatus`, `ProcessData`, `SendToDms`, `Callback`, `DmsResponse`, `DoPayment`, `KafkaMessage1`, `AntragEvent`.

## 16. Mini-Beispiel AsyncAPI: Statusereignis über Event

Dieses Beispiel zeigt ein fachliches Statusereignis. Ein Fachverfahren veröffentlicht, dass sich der Status eines Antrags geändert hat. Andere Systeme können reagieren, etwa Portal, DMS, Reporting oder Benachrichtigungsdienst.

```yaml id="ts1o8f"
asyncapi: 3.1.0
info:
  title: Antrag Status Events
  version: 1.0.0

servers:
  production:
    host: kafka.behoerde.example:9092
    protocol: kafka

channels:
  antragStatus:
    address: fachverfahren.antrag.status.v1
    messages:
      AntragStatusGeaendert:
        $ref: "#/components/messages/AntragStatusGeaendert"

operations:
  publishAntragStatusGeaendert:
    action: send
    channel:
      $ref: "#/channels/antragStatus"
    messages:
      - $ref: "#/channels/antragStatus/messages/AntragStatusGeaendert"

components:
  messages:
    AntragStatusGeaendert:
      name: AntragStatusGeaendert
      title: Antragstatus wurde geändert
      summary: Ereignis, das eine fachliche Statusänderung eines Antrags meldet
      contentType: application/json
      headers:
        type: object
        required:
          - eventId
          - occurredAt
          - correlationId
        properties:
          eventId:
            type: string
            format: uuid
          occurredAt:
            type: string
            format: date-time
          correlationId:
            type: string
            format: uuid
          causationId:
            type: string
            format: uuid
      payload:
        $ref: "#/components/schemas/AntragStatusGeaendertPayload"

  schemas:
    AntragStatusGeaendertPayload:
      type: object
      required:
        - antragId
        - neuerStatus
        - statusGeaendertAm
      properties:
        antragId:
          type: string
          example: "ANT-2026-000123"
        alterStatus:
          type: string
          enum: [EINGEGANGEN, IN_PRUEFUNG, NACHWEIS_ERFORDERLICH, BESCHIED_ERSTELLT]
        neuerStatus:
          type: string
          enum: [EINGEGANGEN, IN_PRUEFUNG, NACHWEIS_ERFORDERLICH, BESCHIED_ERSTELLT]
        statusGeaendertAm:
          type: string
          format: date-time
        quelle:
          type: string
          example: "FACHVERFAHREN-ANTRAG"
```

In einem Review fragst du jetzt: Ist `eventId` eindeutig? Ist `occurredAt` fachlich oder technisch? Gibt es eine `correlationId` entlang der Prozesskette? Sind Statuswerte stabil? Was passiert, wenn ein Consumer das Event zweimal erhält? Gibt es eine Retention? Kann ein neuer Consumer alte Events nachlesen? Gibt es eine Dead Letter Queue? Wer besitzt das Schema?

## 17. Mini-Beispiel AsyncAPI: Fehlerrückmeldung nach DMS-Verarbeitung

Asynchrone Fehlerrückmeldungen sind heikel, weil sie fachlich und technisch sauber getrennt werden müssen. Ein DMS-Fehler kann bedeuten: Datei zu groß, Virenprüfung fehlgeschlagen, Akte gesperrt, DMS temporär nicht verfügbar, Metadaten ungültig oder Berechtigung fehlt.

```yaml id="opuzif"
channels:
  dokumentVerarbeitung:
    address: dms.dokument.verarbeitung.v1
    messages:
      DokumentVerarbeitungAbgeschlossen:
        $ref: "#/components/messages/DokumentVerarbeitungAbgeschlossen"
      DokumentVerarbeitungFehlgeschlagen:
        $ref: "#/components/messages/DokumentVerarbeitungFehlgeschlagen"

components:
  messages:
    DokumentVerarbeitungFehlgeschlagen:
      name: DokumentVerarbeitungFehlgeschlagen
      contentType: application/json
      headers:
        type: object
        required: [eventId, occurredAt, correlationId]
        properties:
          eventId:
            type: string
            format: uuid
          occurredAt:
            type: string
            format: date-time
          correlationId:
            type: string
            format: uuid
      payload:
        type: object
        required:
          - verarbeitungsId
          - aktenId
          - fehlerKategorie
          - fehlerCode
        properties:
          verarbeitungsId:
            type: string
          aktenId:
            type: string
          dokumentId:
            type: string
          fehlerKategorie:
            type: string
            enum: [FACHLICH, TECHNISCH, SICHERHEIT, TEMPORAER]
          fehlerCode:
            type: string
            example: "DMS_TEMPORARY_UNAVAILABLE"
          wiederholbar:
            type: boolean
          beschreibung:
            type: string
```

Dieses Event ist besser als ein generisches `DmsError`, weil Consumer entscheiden können: Muss der Vorgang manuell geklärt werden? Soll später erneut versucht werden? Muss der Antragsteller etwas nachreichen? Muss Betrieb alarmiert werden?

## 18. Schema-Evolution bei Events

Schema-Evolution ist bei Events kritischer als bei synchronen APIs, weil Events gespeichert, erneut gelesen und von unbekannten oder später hinzukommenden Consumern verarbeitet werden können. AsyncAPI beschreibt Payload-Schemas, also Struktur, Datentypen und Eigenschaften einer Message. ([asyncapi.com](https://www.asyncapi.com/docs/concepts/asyncapi-document/define-payload?utm_source=chatgpt.com)) Aber AsyncAPI allein löst nicht deine Governance. Du brauchst Regeln.

Kompatible Änderungen sind meist: neues optionales Feld, neue Message mit neuem Namen, zusätzliche Header, zusätzliche Statuswerte nur dann, wenn Consumer unbekannte Werte robust behandeln. Brechende Änderungen sind: Pflichtfeld entfernen, Feldtyp ändern, Enum-Werte umbenennen, Feldbedeutung ändern, Zeitformat ändern, Identifier-Semantik ändern.

Für Behörden empfehle ich: Event-Schemas versionieren, Consumer-Kompatibilität testen, alte Event-Versionen für eine definierte Frist weiter unterstützen, Breaking Changes nur über neue Channel- oder Message-Version einführen und bei kritischen Fachverfahren eine Schema Registry oder vergleichbare Governance verwenden.

## 19. OpenAPI oder AsyncAPI: Entscheidungskriterien

| Aspekt | Details/Erklärung | Beispiel | Entscheidung |
|---|---|---|---|
| Zeitverhalten | Braucht der Aufrufer sofort eine Antwort? | Registerabfrage im Bearbeitungsdialog. | OpenAPI/REST. |
| Fachliche Tatsache | Soll nur mitgeteilt werden, dass etwas passiert ist? | `BescheidErstellt`. | AsyncAPI/Event. |
| Prozessauslösung | Soll ein anderer Service etwas tun? | „Dokument prüfen“. | Eher Command/Queue oder REST, nicht als Event tarnen. |
| Kopplung | Muss der Producer den Consumer kennen? | Fachverfahren informiert Portal und Reporting. | AsyncAPI reduziert direkte Kopplung. |
| Fehlerbehandlung | Muss der Aufrufer sofort fachlich reagieren? | Register sagt: Person nicht gefunden. | OpenAPI. |
| Lastspitzen | Muss Verarbeitung entkoppelt werden? | Massenhafte Dokumentnachverarbeitung nachts. | AsyncAPI/Queue/Event. |
| Nachvollziehbarkeit | Müssen Statusänderungen auditierbar verteilt werden? | Antragstatus ändert sich. | AsyncAPI plus Audit-Konzept. |
| Benutzerinteraktion | Wartet ein Mensch im UI? | Sachbearbeitung klickt „Register prüfen“. | Meist OpenAPI, ggf. mit Timeout und Retry-Strategie. |
| Langläufer | Dauert Verarbeitung länger als typische HTTP-Timeouts? | DMS-Ablage mit Virenscan. | `202 Accepted` plus AsyncAPI-Rückmeldung. |
| Konsistenzbedarf | Muss Zustand sofort konsistent sein? | Zahlung darf nicht doppelt ausgelöst werden. | Strenge Transaktions-/Idempotenzregeln; nicht blind Eventing. |

Die beste Architektur ist oft hybrid: REST für Commands und Queries, Events für fachliche Zustandsänderungen und Rückmeldungen. Ein Antrag wird per REST eingereicht, die Statusänderung wird als Event verteilt, die Dokumentverarbeitung läuft asynchron, Fehler werden als Event zurückgemeldet und der aktuelle Zustand bleibt per REST abfragbar.

## 20. Review-Raster für OpenAPI

| Aspekt | Details/Erklärung | Beispiel | Bewertungskriterium | Literatur/Quelle |
|---|---|---|---|---|
| Fachlicher Schnitt | Ressourcen spiegeln die Domäne wider. | `Antraege`, `Akten`, `Dokumente`. | Keine technischen Funktionsnamen als API-Oberfläche. | OpenAPI beschreibt HTTP APIs als formalen Vertrag. ([spec.openapis.org](https://spec.openapis.org/oas/v3.2.0.html?utm_source=chatgpt.com)) |
| HTTP-Semantik | Methoden und Statuscodes sind korrekt verwendet. | `GET` liest, `POST` erzeugt/übermittelt, `202` für asynchrone Annahme. | Kein pauschales `200` für alles. | RFC 9110. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) |
| Security | Authentifizierung, Scopes, Rollen und fachliche Zugriffsvoraussetzungen sind dokumentiert. | `register.person.read`. | Security nicht nur in Fließtext, sondern im Vertrag. | OpenAPI Security Schemes; projektspezifisches IAM. |
| Schemas | Datentypen, Pflichtfelder, Enums, Beispiele und Constraints sind präzise. | `format: date`, `enum`, `required`. | Keine „string-Wüste“. | JSON Schema 2020-12. ([json-schema.org](https://json-schema.org/specification?utm_source=chatgpt.com)) |
| Fehlerobjekte | Fehler sind maschinenlesbar und konsistent. | `application/problem+json`. | Einheitliches Fehlerformat mit Correlation ID. | RFC 9457. ([rfc-editor.org](https://www.rfc-editor.org/info/rfc9457/?utm_source=chatgpt.com)) |
| Versionierung | API-Lebenszyklus ist steuerbar. | `/v1`, Deprecation-Frist, Migrationshinweise. | Brechende Änderungen sind geregelt. | API-Governance. |
| Pagination | Listen sind begrenzt und stabil abrufbar. | `limit`, `cursor`. | Keine unbegrenzten Ergebnislisten. | API-Design-Governance. |
| Idempotenz | Wiederholungen erzeugen keine doppelten Fachwirkungen. | `Idempotency-Key`. | Kritische `POST`-Operationen sind retry-sicher. | Resilienz- und Integrationsdesign. |
| Observability | Correlation IDs, Fehlercodes und relevante Headers sind vorgesehen. | `X-Correlation-ID`. | API ist im Betrieb nachvollziehbar. | Betriebsarchitektur. |
| Dokumentation | Summary, Description, Beispiele und Fehlerfälle erklären tatsächliches Verhalten. | Beispielrequests und -responses. | Consumer kann ohne Rückfragen starten. | OpenAPI-Ziel: Verstehen ohne Quellcode. ([spec.openapis.org](https://spec.openapis.org/oas/v3.2.0.html?utm_source=chatgpt.com)) |

## 21. Review-Raster für AsyncAPI

| Aspekt | Details/Erklärung | Beispiel | Bewertungskriterium | Literatur/Quelle |
|---|---|---|---|---|
| Event-Fachlichkeit | Events beschreiben fachliche Tatsachen. | `NachweisGeprueft`. | Keine Commands als Events. | AsyncAPI beschreibt message-driven APIs. ([asyncapi.com](https://www.asyncapi.com/docs/reference/specification/latest?utm_source=chatgpt.com)) |
| Channel-Struktur | Topics/Queues sind fachlich und versionierbar benannt. | `fachverfahren.antrag.status.v1`. | Keine technischen Sammeltopics wie `events`. | AsyncAPI Channels. ([asyncapi.com](https://www.asyncapi.com/docs/concepts/asyncapi-document/structure?utm_source=chatgpt.com)) |
| Message-Struktur | Header und Payload sind getrennt. | Header: `eventId`, `correlationId`; Payload: fachliche Daten. | Technische Metadaten nicht im Fachpayload verstecken. | AsyncAPI Message/Payload-Konzepte. ([asyncapi.com](https://www.asyncapi.com/docs/concepts/asyncapi-document/define-payload?utm_source=chatgpt.com)) |
| Producer/Consumer | Verantwortlichkeiten sind klar. | Fachverfahren produziert, Portal konsumiert. | Niemand konsumiert „heimlich“ ohne Ownership. | Integrations-Governance. |
| Idempotenz | Consumer können doppelte Nachrichten erkennen. | `eventId` plus fachlicher Schlüssel. | Doppelte Events führen nicht zu doppelten Aktionen. | Resilienzdesign. |
| Ordering | Reihenfolge ist fachlich bewertet. | Statusänderungen eines Antrags müssen pro `antragId` geordnet sein. | Ordering-Anforderungen sind explizit. | Messaging-Betriebskonzept. |
| Retry/DLQ | Fehlerhafte Verarbeitung ist geregelt. | Retry bei temporären Fehlern, DLQ bei nicht verarbeitbaren Messages. | Keine stillen Nachrichtenverluste. | Betriebsarchitektur. |
| Schema-Evolution | Kompatibilitätsregeln sind dokumentiert. | Neue optionale Felder erlaubt, Feldentfernung nur mit neuer Version. | Consumer brechen nicht unerwartet. | AsyncAPI plus Schema-Governance. |
| Observability | Events sind korrelierbar und messbar. | Lag, Fehlerrate, Consumer-Status. | Betrieb sieht, ob Verarbeitung hängt. | Observability-Architektur. |
| Schutzbedarf | Payload enthält nur notwendige Daten. | Event enthält `antragId`, aber nicht unnötig vollständige personenbezogene Daten. | Datensparsamkeit und Zugriffskontrolle sind berücksichtigt. | Projektspezifische Sicherheits- und Datenschutzanforderungen. |

## 22. Qualitätskriterien als Mindeststandard

Ein Mindeststandard für OpenAPI sollte verbindlich festlegen, dass jede API eine valide OpenAPI-Spezifikation besitzt, alle Operationen eine eindeutige `operationId` haben, alle Request- und Response-Schemas vollständig beschrieben sind, Fehler im einheitlichen Problem-Format zurückgegeben werden, Security Schemes dokumentiert sind, Statuscodes fachlich korrekt genutzt werden, Beispiele für Erfolgs- und Fehlerfälle vorhanden sind, Pagination für Listen verpflichtend ist, Idempotenz für kritische Schreiboperationen geregelt ist und Versionierung samt Deprecation-Prozess beschrieben wird.

Ein Mindeststandard für AsyncAPI sollte verbindlich festlegen, dass jedes Event einen fachlichen Namen in Vergangenheitsform besitzt, jeder Channel versioniert und fachlich benannt ist, jede Message Header für `eventId`, `occurredAt`, `correlationId` und optional `causationId` besitzt, jedes Payload-Schema versioniert und validierbar ist, Producer und Consumer dokumentiert sind, Retry- und Dead-Letter-Verhalten beschrieben ist, Ordering-Anforderungen explizit bewertet sind, personenbezogene Daten minimiert werden und Schema-Evolution verbindlich geregelt ist.

Für Ausschreibung und Abnahme kannst du das so formulieren: „Der Auftragnehmer liefert vor Implementierung eine abgestimmte OpenAPI- beziehungsweise AsyncAPI-Spezifikation. Die Spezifikation ist Bestandteil des Liefergegenstands, wird automatisiert validiert, in Reviews geprüft und darf erst nach Freigabe als Implementierungsgrundlage verwendet werden. Abweichungen von den API-Standards sind als Architecture Decision Record zu dokumentieren und freigeben zu lassen.“

## 23. Typische Designfehler

| Aspekt | Details/Erklärung | Beispiel | Korrektur | Literatur/Quelle |
|---|---|---|---|---|
| RPC über REST | Pfade beschreiben Funktionen statt Ressourcen. | `/doRegisterCheck` | `GET /register/personen/{personId}` | REST-/HTTP-Design; OpenAPI beschreibt HTTP APIs. ([spec.openapis.org](https://spec.openapis.org/oas/v3.2.0.html?utm_source=chatgpt.com)) |
| Statuscode-Missbrauch | API gibt immer `200` zurück. | Fehler im Body mit `success=false`. | Passende 4xx/5xx-Codes plus Problem Details. | RFC 9110, RFC 9457. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc9110?utm_source=chatgpt.com)) |
| Unklare Fehler | Freitextfehler ohne Code. | „Es ist ein Fehler aufgetreten.“ | Fehlercode, Kategorie, Correlation ID, Feldverletzungen. | RFC 9457. ([rfc-editor.org](https://www.rfc-editor.org/info/rfc9457/?utm_source=chatgpt.com)) |
| Zu breite Payloads | Event enthält vollständige Personendaten, obwohl nur Statusänderung nötig ist. | `AntragStatusGeaendert` mit kompletter Akte. | Minimaler Payload oder Event Notification plus Nachlade-API. | Sicherheits- und Datenschutzarchitektur. |
| Commands als Events | Event fordert eine Aktion. | `PruefeNachweisEvent`. | Command separat modellieren oder REST nutzen. | Event-Design-Governance. |
| Keine Idempotenz | Retry erzeugt doppelte Dokumente/Zahlungen. | Timeout nach `POST`. | `Idempotency-Key`, fachliche Deduplizierung. | Resilienzdesign. |
| Keine Schema-Evolution | Feld wird entfernt, Consumer brechen. | `status` wird in `state` umbenannt. | Versionierung, Deprecation, Kompatibilitätstests. | JSON Schema/AsyncAPI Governance. |
| Sammel-Topic | Alle Events laufen über ein Topic. | `behoerde.events`. | Fachliche Channels nach Domäne und Version. | AsyncAPI Channels. ([asyncapi.com](https://www.asyncapi.com/docs/concepts/asyncapi-document/structure?utm_source=chatgpt.com)) |
| Fehlende Beispiele | Spezifikation ist formal, aber nicht verständlich. | Keine Beispielantworten. | Beispiele für Erfolg, Validierungsfehler, Berechtigungsfehler. | OpenAPI-Ziel: Verständlichkeit für Menschen und Maschinen. ([spec.openapis.org](https://spec.openapis.org/oas/v3.2.0.html?utm_source=chatgpt.com)) |
| Betrieb vergessen | Keine Metriken, keine DLQ, keine Correlation ID. | Consumer hängt unbemerkt. | Observability-Anforderungen in API-Vertrag und Betriebskonzept. | Betriebsarchitektur. |

## 24. Behörden-End-to-End-Beispiel: Antrag, Register, DMS, Event, Fehlerrückmeldung

Ein Antrag geht im Portal ein. Das Portal sendet den Antrag per REST an das Fachverfahren: `POST /antraege`. Das Fachverfahren antwortet mit `201 Created` und einer `antragId`. Danach veröffentlicht das Fachverfahren das Event `AntragEingegangen` auf `fachverfahren.antrag.lifecycle.v1`.

Die Sachbearbeitung oder ein automatisierter Prüfdienst ruft synchron Registerdaten ab: `GET /register/personen/{personId}`. Diese Abfrage ist OpenAPI-beschrieben, geschützt durch OAuth2/Scopes und fachliche Berechtigungsprüfung. Wenn das Register nicht verfügbar ist, bekommt das Fachverfahren einen technischen Fehler und entscheidet, ob der Vorgang zurückgestellt oder später erneut geprüft wird.

Ein Nachweis wird an das DMS übergeben: `POST /akten/{aktenId}/dokumente` mit `Idempotency-Key`. Das Fachverfahren erhält `202 Accepted` und eine `verarbeitungsId`. Das DMS verarbeitet asynchron. Bei Erfolg sendet es `DokumentAblageAbgeschlossen`; bei Fehler sendet es `DokumentVerarbeitungFehlgeschlagen`. Das Fachverfahren aktualisiert den Vorgang und veröffentlicht gegebenenfalls `AkteAktualisiert` oder `NachweisPruefungAusstehend`.

Am Ende wird der Bescheid erstellt. Das Fachverfahren veröffentlicht `BescheidErstellt`. Ein Versanddienst konsumiert dieses Event oder wird über einen expliziten Command beauftragt. Genau hier musst du sauber entscheiden: „Bescheid erstellt“ ist ein Event. „Versende Bescheid“ ist ein Command. Wer das verwechselt, baut unklare Prozessverantwortung.

## 25. Konkretes Vorgehen zur Erstellung einer guten Spezifikation

Beginne nicht mit YAML. Beginne mit dem fachlichen Integrationsvertrag. Schritt eins ist die fachliche Schnittstellenkarte: Wer braucht was von wem, zu welchem Zeitpunkt, mit welcher Verbindlichkeit? Schritt zwei ist die Kommunikationsart: Query, Command oder Event. Schritt drei ist das Ressourcen- oder Eventmodell. Schritt vier ist das Datenmodell mit Pflichtfeldern, IDs, Statuswerten und fachlichen Constraints. Schritt fünf ist Fehler- und Ausnahmeverhalten. Schritt sechs ist Security. Schritt sieben ist Betriebsverhalten: Timeouts, Retries, Limits, Monitoring, Logging. Schritt acht ist Versionierung und Lebenszyklus. Schritt neun ist die maschinenlesbare Spezifikation. Schritt zehn ist Review, Test und Abnahme.

In der Praxis kannst du das mit einem API-Design-Workshop beginnen. Teilnehmende sollten sein: Fachseite, Solution Architect, Security/IAM, Datenschutz, Betrieb, Entwickler, Test, DMS/Register-Verantwortliche und gegebenenfalls Dienstleister. Das Ergebnis ist kein „schönes YAML“, sondern ein geprüfter Vertrag.

## 26. Reviewfragen, die du in Architekturterminen stellen solltest

Frage bei OpenAPI: Welche fachliche Ressource wird hier angeboten? Warum ist diese Operation synchron? Welche Statuscodes kann der Consumer erwarten? Welche Fehler sind fachlich, welche technisch? Welche Felder sind Pflicht und warum? Wie ist die Berechtigung auf Datensatzebene geregelt? Was passiert bei Timeout? Ist die Operation idempotent? Wie wird die API versioniert? Welche Beispiele zeigen echte Fachfälle?

Frage bei AsyncAPI: Welches fachliche Ereignis ist tatsächlich passiert? Wer ist Producer und fachlicher Owner? Wer darf konsumieren? Enthält das Event zu viele Daten oder zu wenig? Gibt es eine stabile `eventId`? Muss Reihenfolge garantiert sein? Was passiert bei doppelter Nachricht? Wie lange werden Events aufbewahrt? Gibt es Replay? Was passiert bei nicht verarbeitbaren Nachrichten? Wie werden Schemas weiterentwickelt?

Frage an Dienstleister: Welche Spezifikation ist verbindlich? Wie wird sie validiert? Welche Breaking-Change-Regeln gelten? Welche Contract Tests werden geliefert? Welche Beispielpayloads sind Bestandteil der Abnahme? Wie werden Fehlerfälle getestet? Wie wird die Schnittstelle in Betrieb und Support übergeben?

## 27. Praktische Übungen

### Übung 1: REST-Ressource verbessern

Ausgangsentwurf: `POST /checkPersonData`

Bewerte den Entwurf. Das Problem: Der Pfad beschreibt eine technische Aktion, keine Ressource. Außerdem ist unklar, ob gelesen, geprüft oder gespeichert wird. Eine bessere Variante wäre je nach Fachfall: `GET /register/personen/{personId}` für eine reine Abfrage, `POST /registerauskuenfte` für eine protokollierte Auskunftserstellung oder `POST /antraege/{antragId}/registerpruefungen` für eine fachliche Prüfung im Kontext eines Antrags.

Deine Aufgabe: Formuliere drei mögliche Zielentwürfe und entscheide, welcher passt, wenn die Registerprüfung auditierbar im Antrag gespeichert werden muss.

Musterlösung: Für auditierbare Prüfung im Antragskontext ist `POST /antraege/{antragId}/registerpruefungen` plausibel. Die Antwort kann `201 Created` liefern, wenn eine Prüfressource erzeugt wurde, oder `202 Accepted`, wenn die Prüfung asynchron weiterläuft.

### Übung 2: Fehlerobjekt entwerfen

Ausgangssituation: Ein Dokument kann nicht in das DMS übernommen werden, weil der Dateityp nicht erlaubt ist.

Deine Aufgabe: Entwirf eine Fehlerantwort mit Statuscode und Problem-Details-Body.

Musterlösung: Statuscode `415 Unsupported Media Type`, Body mit `type`, `title`, `status`, `detail`, `correlationId`, `errorCode: UNSUPPORTED_DOCUMENT_TYPE` und optional erlaubten Dateitypen.

### Übung 3: Event fachlich benennen

Ausgangsentwurf: `DmsCallbackReceived`

Bewertung: Das ist technisch und beschreibt den Empfang eines Callbacks, nicht die fachliche Tatsache. Bessere Namen sind `DokumentAblageAbgeschlossen`, `DokumentAblageFehlgeschlagen` oder `AkteAktualisiert`, je nachdem, was fachlich wirklich passiert ist.

Deine Aufgabe: Entscheide, welches Event passt, wenn das DMS zwar die Datei gespeichert hat, aber die Aktenmetadaten noch nicht aktualisiert wurden.

Musterlösung: `DokumentAblageAbgeschlossen` passt. `AkteAktualisiert` wäre falsch, wenn die Akte noch nicht aktualisiert ist.

### Übung 4: Idempotenz bewerten

Ausgangssituation: `POST /zahlungen` löst eine Auszahlung aus. Bei Timeout sendet der Client erneut.

Deine Aufgabe: Benenne das Risiko und drei Gegenmaßnahmen.

Musterlösung: Risiko ist doppelte Auszahlung. Gegenmaßnahmen: verpflichtender `Idempotency-Key`, fachlicher eindeutiger Zahlungsauftrag mit `zahlungsauftragId`, serverseitige Deduplizierung und klare Antwort bei Wiederholung derselben Operation.

### Übung 5: Schema-Evolution prüfen

Ausgangssituation: Im Event `AntragStatusGeaendert` soll das Feld `neuerStatus` in `status` umbenannt werden.

Bewertung: Das ist brechend, weil bestehende Consumer `neuerStatus` erwarten.

Musterlösung: Entweder neues optionales Feld `status` ergänzen und `neuerStatus` für eine definierte Frist beibehalten, oder neue Message-/Channel-Version einführen. Zusätzlich müssen Consumer-Kompatibilitätstests und Deprecation-Kommunikation erfolgen.

## 28. Dein kompaktes Bewertungsmodell

Wenn du eine OpenAPI oder AsyncAPI vor dir hast, bewerte sie in dieser Reihenfolge: Erst fachlicher Sinn, dann Kommunikationsart, dann Vertragsklarheit, dann Security, dann Fehlerverhalten, dann Datenqualität, dann Versionierung, dann Betrieb, dann Testbarkeit, dann Abnahmefähigkeit.

Der wichtigste Satz für deine Rolle lautet: Eine Schnittstellenspezifikation ist gut, wenn ein fremdes, berechtigtes, fachlich kompetentes Team sie ohne implizites Insiderwissen korrekt implementieren, testen, betreiben und weiterentwickeln kann.

Genau damit hebst du dich als Enterprise Architekt ab. Du prüfst nicht nur, ob ein Endpoint existiert. Du prüfst, ob eine Organisation darüber verlässlich zusammenarbeiten kann. <>