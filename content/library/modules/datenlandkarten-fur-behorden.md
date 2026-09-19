## Checkliste: Datenlandkarte für Behörden-Fachverfahren

1. Prüfe zuerst den **fachlichen Prozess**, nicht die Datenbanktabellen.  
2. Identifiziere die zentralen **Datenobjekte**: Person, Vorgang, Nachweis, Bescheid, Zahlung, Kommunikation.  
3. Kläre je Datenobjekt das **führende System**: Wo entsteht die verbindliche Wahrheit?  
4. Unterscheide **Erzeugen, Ändern, Lesen, Weitergeben, Archivieren und Löschen**.  
5. Zeichne Datenflüsse immer mit **Quelle, Ziel, Zweck, Auslöser und Schnittstelle**.  
6. Benenne pro Datenobjekt einen **Data Owner** und mindestens einen fachlichen Steward.  
7. Prüfe **Schutzbedarf** nach Vertraulichkeit, Integrität und Verfügbarkeit.  
8. Prüfe **Datenqualität**: Vollständigkeit, Aktualität, Eindeutigkeit, Plausibilität, Konsistenz.  
9. Kläre **Registerbezug** und Once-Only-Fähigkeit: Welche Daten dürfen oder sollen aus Registern kommen?  
10. Dokumentiere **Aufbewahrung, Archivierung, Löschung und Nachweisfähigkeit**.  
11. Trenne operative Daten, Berichtsdaten, Metadaten und Auditdaten sauber voneinander.  
12. Markiere Datenrisiken sichtbar: doppelte Pflege, unklare Verantwortlichkeit, fehlende Löschlogik, Schattenkopien, unklare Schnittstellenverträge.  

<>

## 1. Was eine Datenlandkarte wirklich ist

Eine Datenlandkarte ist eine fachlich-architektonische Übersicht darüber, **welche Datenobjekte in einer Organisation existieren, wo sie entstehen, wo sie verändert werden, welche Systeme sie nutzen, wohin sie fließen, wer verantwortlich ist, welchen Schutzbedarf sie haben und wie ihr Lebenszyklus endet**. Sie ist damit kein reines Datenbankmodell, kein ER-Diagramm und keine technische Schnittstellenliste. Sie ist ein Architekturwerkzeug, um Fachlichkeit, Anwendungen, Schnittstellen, Informationssicherheit, Datenschutz, Betrieb und Governance zusammenzuführen.

In der Enterprise Architecture gehört eine Datenlandkarte in den Bereich **Data Architecture**. TOGAF beschreibt Datenarchitektur als Teil der Informationssystemarchitektur; klassische Artefakte sind unter anderem Datenentitäten, Anwendungs-/Daten-Beziehungen, Datenverteilung, Datensicherheit, Datenmigration und Datenlebenszyklus. Genau hier liegt der Nutzen für dich als Enterprise Architekt: Du machst sichtbar, welche Daten für die Verwaltung handlungsfähig, prüffähig und steuerbar machen. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7599909799/toc.pdf?utm_source=chatgpt.com))

DAMA-DMBOK ist dafür eine wichtige fachliche Referenz, weil es Data Management als standardisiertes Wissensgebiet beschreibt und Themen wie Data Governance, Data Architecture, Data Quality, Data Security und Data Lifecycle Management zusammenführt. Für Behörden ist das besonders relevant, weil Daten nicht nur „IT-Rohstoff“ sind, sondern Grundlage für Verwaltungsentscheidungen, Bescheide, Nachweise, Fristen, Zahlungen, Berichtspflichten und Aktenführung. ([dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/?utm_source=chatgpt.com))

## 2. Der wichtigste Perspektivwechsel

Der häufigste Fehler besteht darin, eine Datenlandkarte aus Sicht der Systeme zu zeichnen: „System A sendet an System B.“ Das ist zu technisch und zu kurz. Du musst aus Sicht der **Datenobjekte und Verwaltungswirklichkeit** denken: „Welche Information wird für welche behördliche Entscheidung benötigt, wer darf sie erzeugen, wer darf sie verändern, wer muss sie nachvollziehen können und wann darf oder muss sie entfernt werden?“

Ein Fachverfahren verarbeitet nicht einfach „Daten“. Es verarbeitet zum Beispiel eine Person, einen Antrag, einen Nachweis, eine fachliche Prüfung, einen Bescheid, eine Zahlung, eine Frist, eine Kommunikation und einen Aktenvorgang. Diese Objekte haben unterschiedliche Verantwortlichkeiten, unterschiedliche Schutzbedarfe und unterschiedliche Lebenszyklen. Genau diese Differenzierung macht dich als Architekt stark.

## 3. Grundbegriffe sauber erklärt

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Datenobjekt | Fachlich bedeutsames Informationsobjekt, über das die Organisation sprechen, entscheiden und nachweisen muss. Es ist nicht zwingend identisch mit einer Datenbanktabelle. | Person, Vorgang, Nachweis, Bescheid, Zahlung, Kommunikation. | TOGAF ordnet Datenentitäten und Datenarchitektur als Architekturartefakte ein. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7599909799/toc.pdf?utm_source=chatgpt.com)) |
| Datenattribut | Einzelnes Merkmal eines Datenobjekts. | Name, Geburtsdatum, Vorgangsstatus, Bescheiddatum, Zahlungsbetrag. | DAMA-DMBOK ist Referenz für standardisiertes Datenmanagement. ([dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/?utm_source=chatgpt.com)) |
| Datenfluss | Bewegung oder Übergabe von Daten zwischen Systemen, Organisationseinheiten oder Prozessschritten. | Portal übergibt Antrag an Fachverfahren; Fachverfahren übergibt Bescheid an DMS. | TOGAF nennt Data Dissemination/Data Flow-nahe Artefakte als Teil der Datenarchitektur. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7699949799/toc.pdf?utm_source=chatgpt.com)) |
| Führendes System | System, in dem die verbindliche fachliche Wahrheit eines Datenobjekts oder Attributs gepflegt wird. | Personenstammdaten kommen aus Register; Vorgangsstatus wird im Fachverfahren geführt. | Begriff ist Architekturpraxis; fachlich anschlussfähig an Data Governance und Data Architecture nach DAMA/TOGAF. ([dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/?utm_source=chatgpt.com)) |
| Datenquelle | System oder Stelle, aus der Daten stammen. | Register, Onlineportal, Sachbearbeitung, DMS, Zahlungsplattform. | Registermodernisierung zielt auf interoperable Register und vereinfachten Austausch von Nachweisdaten. ([it-planungsrat.de](https://www.it-planungsrat.de/projekte/registermodernisierung?utm_source=chatgpt.com)) |
| Datensenke | System, das Daten aufnimmt, nutzt oder speichert, ohne zwingend führend zu sein. | Reporting-System, Archiv, Monitoring, DMS-Kopie. | Architekturpraxis; relevant für Datenlebenszyklus und Datenschutzgrundsätze. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Data Owner | Fachlich verantwortliche Rolle für Bedeutung, Qualität, Regeln und Nutzung eines Datenobjekts. | Fachbereich „Leistungsgewährung“ verantwortet Vorgangsdaten. | DAMA-DMBOK stellt Data Governance als zentralen Bereich des Data Management heraus. ([snowflake.com](https://www.snowflake.com/en/fundamentals/data-governance/framework/dama-dmbok/?utm_source=chatgpt.com)) |
| Data Steward | Operative Rolle, die Datenregeln, Qualitätsprüfungen und Klärungen im Alltag unterstützt. | Sachgebietskoordination prüft Dubletten, Statuswerte, Pflichtfelder. | DAMA-DMBOK/Data-Governance-Praxis. ([dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/?utm_source=chatgpt.com)) |
| Metadaten | Daten über Daten: Definition, Herkunft, Aktualität, Schutzbedarf, Format, Eigentümer, Aufbewahrungsfrist. | „Bescheiddatum: Datum der Bekanntgabe; Format ISO-8601; führend im Fachverfahren.“ | DAMA-DMBOK behandelt Metadaten als Kernbereich des Datenmanagements. ([dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/?utm_source=chatgpt.com)) |
| Berichtsdaten | Für Auswertung, Steuerung und Statistik aufbereitete Daten; oft abgeleitet und nicht operativ führend. | Monatsbericht: Anzahl abgeschlossener Vorgänge je Standort. | Analytische Architektur muss operative und analytische Nutzung trennen; DMBOK wird als methodische Grundlage genutzt. ([arxiv.org](https://arxiv.org/abs/2212.03612?utm_source=chatgpt.com)) |
| Schutzbedarf | Einschätzung möglicher Schäden bei Verletzung von Vertraulichkeit, Integrität oder Verfügbarkeit. | Falscher Bescheid wegen manipulierter Nachweisdaten: hoher Integritätsschaden. | BSI beschreibt Schutzbedarfsfeststellung entlang Vertraulichkeit, Integrität und Verfügbarkeit. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Aufbewahrung und Löschung | Regelung, wie lange Daten benötigt, archiviert, gesperrt oder gelöscht werden. | Kommunikationsdaten nach Verfahrensabschluss gemäß Akten-/Aufbewahrungsregel. | DSGVO Art. 5 enthält unter anderem Datenminimierung, Richtigkeit, Speicherbegrenzung sowie Integrität und Vertraulichkeit. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |

## 4. Das Behördenbeispiel: Personen-, Vorgangs-, Nachweis-, Bescheid-, Zahlungs- und Kommunikationsdaten

Nehmen wir ein typisches Fachverfahren: Eine Person stellt über ein Portal einen Antrag. Das Portal übergibt die Antragsdaten an ein Fachverfahren. Das Fachverfahren ruft Registerdaten ab, prüft Nachweise, erzeugt einen Bescheid, löst gegebenenfalls eine Zahlung aus, schreibt Dokumente in DMS/eAkte, erzeugt Kommunikationsereignisse und liefert aggregierte Daten an ein Berichtssystem.

Die Datenlandkarte muss jetzt nicht nur zeigen, **dass** Systeme verbunden sind, sondern **welches Datenobjekt an welcher Stelle welchen Status hat**. Eine Person kann im Portal als Antragsteller auftreten, im Register als Stammdatensatz existieren, im Fachverfahren als Beteiligter geführt werden, in der eAkte als Aktenbezug erscheinen und im Reporting nur aggregiert oder pseudonymisiert ausgewertet werden. Wenn du das nicht trennst, entsteht später Chaos: widersprüchliche Namen, falsche Adressen, doppelte Pflege, unklare Berichte und schwer prüfbare Entscheidungen.

## 5. Beispiel-Datenlandkarte als fachliche Matrix

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Personendaten | Beschreiben natürliche Personen oder Organisationen, die am Verfahren beteiligt sind. Kritisch sind Eindeutigkeit, Aktualität, Identifikation und Zweckbindung. | Name, Geburtsdatum, Adresse, Identifikationsmerkmal, Rolle im Verfahren. | DSGVO Art. 5 verlangt unter anderem Datenminimierung, Richtigkeit, Speicherbegrenzung sowie Integrität und Vertraulichkeit. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Vorgangsdaten | Beschreiben den Verwaltungsfall selbst. Sie sind meist im Fachverfahren führend, weil dort Bearbeitung, Status, Fristen und Entscheidungen entstehen. | Vorgangsnummer, Antragseingang, Bearbeitungsstatus, Frist, zuständige Organisationseinheit. | Data Architecture betrachtet Datenobjekte und deren Beziehung zu Anwendungen/Prozessen als Architekturgegenstand. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7699949799/toc.pdf?utm_source=chatgpt.com)) |
| Nachweisdaten | Belegen eine Anspruchsvoraussetzung oder Sachlage. Sie können vom Antragsteller kommen oder über Register/Nachweisabruf bereitgestellt werden. | Einkommensnachweis, Meldebestätigung, Aufenthaltstitel, Studienbescheinigung. | Registermodernisierung und NOOTS sollen Nachweisdatenabrufe vereinfachen und das Once-Only-Prinzip unterstützen. ([it-planungsrat.de](https://www.it-planungsrat.de/projekte/registermodernisierung?utm_source=chatgpt.com)) |
| Bescheiddaten | Dokumentieren die rechtsverbindliche Entscheidung der Behörde. Kritisch sind Version, Bekanntgabe, Begründung, Zustellung und Aktennachweis. | Bewilligungsbescheid, Ablehnungsbescheid, Änderungsbescheid. | Datenschutz- und Nachweisfähigkeit ergeben sich aus Verarbeitungsgrundsätzen und Akten-/Fachverfahrenspflichten; DSGVO Art. 5 ist Grundrahmen für personenbezogene Verarbeitung. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Zahlungsdaten | Betreffen finanzielle Anordnungen, Auszahlungen, Rückforderungen oder Gebühren. Kritisch sind Integrität, Vier-Augen-Prüfung, Buchungsstatus und Schnittstelle zur Kasse. | Zahlungsanordnung, Betrag, IBAN, Kassenzeichen, Auszahlungsstatus. | BSI-Schutzbedarf ist besonders bei Integrität und Verfügbarkeit relevant, wenn falsche oder ausfallende Daten erhebliche Schäden erzeugen können. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Kommunikationsdaten | Dokumentieren Schreiben, Benachrichtigungen, E-Mails, Portalnachrichten, Zustellinformationen und Gesprächsnotizen. | Eingangsbestätigung, Rückfrage, Fristsetzung, Zustellnachweis. | DSGVO-Grundsätze und Speicherbegrenzung sind bei Kommunikationshistorien besonders relevant. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Metadaten | Beschreiben Struktur, Bedeutung, Herkunft und Status der Daten. Ohne Metadaten ist die Datenlandkarte später nicht wartbar. | Datenowner, Schutzbedarf, Quelle, Aktualität, Löschregel, Qualitätsregel. | DAMA-DMBOK positioniert Data Management als standardisiertes Rahmenwerk für Governance, Qualität, Architektur und Lebenszyklus. ([dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/?utm_source=chatgpt.com)) |
| Berichtsdaten | Verdichtete, oft abgeleitete Daten für Steuerung, Controlling, Statistik und Leitung. Sie dürfen nicht unbemerkt operativ zurückwirken. | Anzahl Anträge je Monat, durchschnittliche Bearbeitungszeit, offene Vorgänge je Standort. | Analytische Architekturen trennen operative und auswertende Datenverwendung systematisch. ([arxiv.org](https://arxiv.org/abs/2212.03612?utm_source=chatgpt.com)) |

## 6. Welche Systeme erzeugen, ändern, lesen, weitergeben und archivieren?

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Onlineportal | Erzeugt Antragsdaten aus Nutzereingaben, liest teilweise Register- oder Profildaten, übergibt den Antrag an das Fachverfahren. Es ist oft System of Engagement, aber selten führendes System für den gesamten Vorgang. | Bürger füllt Antrag aus; Portal sendet Antragsdatensatz und Anlagen an Fachverfahren. | Once-Only-Verwaltungsleistungen sollen Daten/Nachweise nicht mehrfach erheben, sondern über Register nutzbar machen. ([bva.bund.de](https://www.bva.bund.de/DE/Services/Behoerden/Verwaltungsdienstleistungen/Registermodernisierung/Ueberblick/ueberblick_node.html?utm_source=chatgpt.com)) |
| Fachverfahren | Führt Vorgangsdaten, Bearbeitungsstatus, fachliche Prüfung, Entscheidungsvorbereitung und Bescheiderzeugung. Es ist häufig führend für Vorgang, Status und Bescheidentwurf. | Sachbearbeitung prüft Antrag; Status wechselt von „eingegangen“ zu „in Prüfung“ zu „entschieden“. | TOGAF ordnet Anwendungs-/Daten-Beziehungen der Datenarchitektur zu. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7699949799/toc.pdf?utm_source=chatgpt.com)) |
| Register | Führt bestimmte Stammdaten oder Nachweisdaten. Das Fachverfahren sollte diese Daten nicht ungeprüft dauerhaft duplizieren, sondern Quelle, Abrufzeitpunkt und Zweck dokumentieren. | Melderegister liefert aktuelle Adresse; Register liefert Nachweisstatus. | Registermodernisierung zielt darauf, Register interoperabel nutzbar zu machen und Nachweisdatenaustausch zu vereinfachen. ([it-planungsrat.de](https://www.it-planungsrat.de/projekte/registermodernisierung?utm_source=chatgpt.com)) |
| DMS/eAkte | Archiviert Dokumente, Aktenmetadaten, Bescheide, Nachweise und Kommunikationsdokumente. Es ist meist führend für Aktenstruktur und Dokumentnachweis, aber nicht für operative Vorgangslogik. | Finaler Bescheid wird revisionssicher in der eAkte abgelegt. | Speicherbegrenzung und Nachvollziehbarkeit müssen mit Aufbewahrungsregeln in Einklang gebracht werden. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Zahlungs-/Kassenverfahren | Führt Zahlungsanordnung, Buchungsstatus, Auszahlung, Rückforderung oder Gebühreneinzug. Es ist meist führend für buchhalterischen Zahlungsstatus. | Fachverfahren löst Auszahlung aus; Kasse bestätigt Buchung. | Integrität ist bei Zahlungsdaten besonders schutzbedürftig; BSI betrachtet Schutzbedarf entlang der drei Grundwerte. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Kommunikationsdienst | Versendet Benachrichtigungen oder Schreiben, führt aber nicht zwingend die fachliche Wahrheit. Wichtig sind Zustellstatus, Inhalt, Zeitpunkt und Bezug zum Vorgang. | Portalnachricht „Bitte reichen Sie Nachweis X nach“. | DSGVO-Grundsätze gelten auch für Kommunikationsdaten, wenn personenbezogene Daten verarbeitet werden. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Reporting/BI | Liest operative Daten oder replizierte Auszüge, bereitet sie für Auswertungen auf und erzeugt Kennzahlen. Es darf nicht stillschweigend zum Schatten-Fachverfahren werden. | Dashboard zeigt Bearbeitungszeiten und Rückstände. | Analytische Datenarchitekturen müssen Zweck, Ableitung und Nutzungsgrenzen transparent machen. ([arxiv.org](https://arxiv.org/abs/2212.03612?utm_source=chatgpt.com)) |
| Archiv | Bewahrt Daten/Dokumente gemäß Aufbewahrungs- oder Archivierungsregeln. Es ist nicht gleichbedeutend mit produktiver Bearbeitung. | Abgeschlossene Akte wird nach Frist ins Archiv überführt. | Speicherbegrenzung nach DSGVO verlangt eine definierte Dauer oder Kriterien für die Dauer personenbezogener Speicherung. ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/ALL/?uri=celex%3A32016R0679&utm_source=chatgpt.com)) |
| IAM/Audit-Logging | Erzeugt Nachweise darüber, wer wann worauf zugegriffen oder etwas geändert hat. Diese Daten sind eigene Datenobjekte, nicht nur technische Nebenprodukte. | „Sachbearbeiter X änderte Zahlungsstatus am Datum Y.“ | BSI-Schutzbedarf umfasst Integrität und Verfügbarkeit; Auditdaten dienen der Nachvollziehbarkeit und Sicherheitsprüfung. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |

## 7. Die eigentliche Modellierung: So gehst du Schritt für Schritt vor

### Schritt 1: Fachlichen Prozess grob schneiden

Beginne mit dem Verwaltungsprozess, nicht mit der Systemliste. Ein einfacher Ablauf reicht: Antrag eingeht, Identität wird geprüft, Nachweise werden erhoben oder abgerufen, Fall wird bearbeitet, Entscheidung wird erstellt, Bescheid wird zugestellt, Zahlung wird ausgelöst, Akte wird abgelegt, Berichtsdaten werden erzeugt.

Der Zweck ist nicht Prozessperfektion, sondern Datenverständnis. Du willst erkennen, an welchen fachlichen Stellen Daten entstehen, ihren Status ändern oder beweisrelevant werden.

### Schritt 2: Datenobjekte sammeln

Du fragst: „Über welche Dinge spricht der Fachbereich, wenn er den Fall bearbeitet?“ Daraus entstehen Datenobjekte. In unserem Beispiel sind das Person, Vorgang, Antrag, Nachweis, Prüfung, Bescheid, Zahlung, Kommunikation, Akte, Frist, Status, Auditereignis und Berichtseintrag.

Wichtig: Du modellierst zuerst grob. Ein Datenobjekt ist auf dieser Ebene keine Tabelle. „Person“ ist ein fachliches Objekt. Später kannst du unterscheiden zwischen Personendaten, Beteiligtenrolle, Identitätsmerkmal, Adresse und Kontaktkanal.

### Schritt 3: CRUD+AL je Datenobjekt erfassen

CRUD allein reicht im Behördenkontext nicht. Du brauchst mindestens **Create, Read, Update, Delete plus Archive und Legal Hold/Aufbewahrung**. Praktisch nutze ich dafür „ERLWA“: **Erzeugen, Lesen, Weitergeben, Ändern, Archivieren/Löschen**.

Für jedes Datenobjekt dokumentierst du: Wer erzeugt es? Wer darf es ändern? Wer liest es? Wer gibt es weiter? Wer archiviert es? Wer löscht es? Wer darf Löschung sperren, weil Aufbewahrung oder Nachweisführung entgegensteht?

### Schritt 4: Führendes System bestimmen

Jetzt kommt die zentrale Architekturfrage: „Wo ist die Wahrheit?“ Nicht jede Kopie ist Wahrheit. Nicht jedes lesende System darf ändern. Nicht jede technische Datenhaltung ist fachlich führend.

Beispiel: Die aktuelle Meldeadresse kann aus einem Register kommen. Das Fachverfahren speichert vielleicht eine zum Zeitpunkt der Entscheidung verwendete Adresse. Diese Adresse ist dann nicht zwingend die führende aktuelle Adresse, aber sie ist entscheidungsrelevanter Nachweisstand. Diese Unterscheidung ist Gold wert.

### Schritt 5: Datenflüsse zeichnen

Ein Datenfluss ist nur dann sauber beschrieben, wenn er mindestens diese Informationen enthält: Quelle, Ziel, Datenobjekt, Zweck, Auslöser, Frequenz, Schnittstelle, Transport, Schutzbedarf, Protokollierung und Fehlerverhalten.

„Fachverfahren sendet an DMS“ ist zu dünn. Besser: „Fachverfahren übergibt finalen Bescheid als PDF/A mit Aktenmetadaten, Vorgangs-ID, Dokumenttyp und Bekanntgabedatum an DMS/eAkte nach fachlicher Freigabe; Fehler werden an Sachbearbeitung und Betriebsmonitoring gemeldet.“

### Schritt 6: Data Owner und Verantwortlichkeit klären

Der Systembetreiber ist nicht automatisch Data Owner. Der Data Owner ist fachlich verantwortlich für Bedeutung, Qualität, Regeln und Nutzung eines Datenobjekts. IT kann Custodian sein, also technischer Verwahrer. Datenschutz, Informationssicherheit und Fachbereich müssen beteiligt werden, aber sie ersetzen nicht die fachliche Datenverantwortung.

### Schritt 7: Schutzbedarf und Risiken markieren

Der BSI-Ansatz fragt, welcher Schaden entstehen kann, wenn Vertraulichkeit, Integrität oder Verfügbarkeit verletzt werden. Für eine Datenlandkarte bedeutet das: Du bewertest nicht nur Systeme, sondern auch Datenobjekte und Datenflüsse. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com))

Ein Zahlungsbetrag hat hohen Integritätsbedarf. Ein Nachweis kann hohen Vertraulichkeitsbedarf haben. Ein Vorgangsstatus kann für Fristen und Rechtsschutz relevant sein. Ein Registerabruf kann besonders protokollierungspflichtig sein. Eine falsche Berichtszahl ist vielleicht nicht unmittelbar fallentscheidend, kann aber Leitung, Ressourcensteuerung und parlamentarische Auskunft verfälschen.

### Schritt 8: Lebenszyklus festlegen

Am Ende jedes Datenobjekts stehen Aufbewahrung, Archivierung, Sperrung, Löschung oder dauerhafte Nachweisführung. DSGVO Art. 5 nennt unter anderem Datenminimierung, Richtigkeit, Speicherbegrenzung sowie Integrität und Vertraulichkeit als Grundsätze personenbezogener Verarbeitung. Für Behörden heißt das: Jede Datenlandkarte muss sichtbar machen, warum Daten gespeichert werden, wie lange sie benötigt werden und welche Lösch- oder Aufbewahrungslogik gilt. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com))

## 8. Beispiel: Datenlandkarte im kompakten Zielbild

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Person | Führend für aktuelle Stammdaten ist ein Register oder Identitätsdienst; das Fachverfahren speichert nur verfahrensrelevante Personenbezüge und Entscheidungsstand. | Register liefert Adresse; Fachverfahren speichert verwendete Adresse zum Bescheidzeitpunkt. | Registermodernisierung/NOOTS unterstützt Nachweis- und Datenaustausch nach Once-Only-Logik. ([noots.gov.de](https://noots.gov.de/startseite?utm_source=chatgpt.com)) |
| Vorgang | Führend ist das Fachverfahren. Es erzeugt Vorgangsnummer, Status, Fristen, Bearbeitungsschritte und Entscheidungskontext. | Vorgangsstatus „Nachweis fehlt“ entsteht im Fachverfahren. | TOGAF: Datenarchitektur beschreibt logische/physische Datenassets und Datenmanagementressourcen. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7699949799/toc.pdf?utm_source=chatgpt.com)) |
| Nachweis | Quelle kann Antragsteller, Register oder Drittsystem sein. Führend ist abhängig vom Nachweistyp; im Fachverfahren wird der verwendete Nachweisstand dokumentiert. | Studienbescheinigung wird hochgeladen; Meldeinformation wird aus Register abgerufen. | Once-Only-Prinzip: Nachweise sollen künftig nicht immer wieder übermittelt werden müssen. ([bva.bund.de](https://www.bva.bund.de/DE/Services/Behoerden/Verwaltungsdienstleistungen/Registermodernisierung/Ueberblick/ueberblick_node.html?utm_source=chatgpt.com)) |
| Bescheid | Führend für fachliche Entscheidung ist das Fachverfahren; führend für Dokumentablage und Aktennachweis ist DMS/eAkte. | Fachverfahren erzeugt Bescheid; DMS archiviert finale Fassung. | Datenschutzgrundsätze und Nachweisfähigkeit müssen zusammengeführt werden. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Zahlung | Fachverfahren erzeugt Zahlungsanspruch oder Zahlungsanordnung; Kassenverfahren ist führend für Buchung und Zahlungsstatus. | Auszahlung angewiesen; Kasse bestätigt „bezahlt“. | BSI-Grundwerte sind für Zahlungsintegrität und Verfügbarkeit relevant. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Kommunikation | Kommunikationsdienst versendet; Fachverfahren oder DMS führt fachlichen Kommunikationsnachweis. | Fristsetzung per Portalnachricht; Zustellnachweis in eAkte. | Speicherbegrenzung und Zweckbindung sind bei Kommunikationsdaten zu prüfen. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Bericht | BI-System ist führend für Kennzahlendarstellung, aber nicht für operative Fallentscheidung. Herkunft und Berechnungslogik müssen dokumentiert sein. | KPI „durchschnittliche Bearbeitungsdauer“ aus Vorgangsstatushistorie. | Analytische Datenarchitekturen benötigen klare Ableitungs- und Nutzungsmodelle. ([arxiv.org](https://arxiv.org/abs/2212.03612?utm_source=chatgpt.com)) |
| Audit | IAM, Fachverfahren, DMS und Schnittstellen erzeugen Auditereignisse. Auditdaten sind eigene schutzbedürftige Datenobjekte. | Zugriff auf Registerdaten wird protokolliert. | BSI-Schutzbedarf ist für Integrität und Nachvollziehbarkeit relevant. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |

## 9. Vorlage für eine Datenlandkarte

Diese Vorlage kannst du direkt in Workshops, Architekturunterlagen oder Ausschreibungen verwenden.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Datenobjekt | Fachlicher Name des Datenobjekts. Keine technischen Tabellennamen als Primärsicht verwenden. | Person, Vorgang, Nachweis, Bescheid, Zahlung. | TOGAF/DAMA als Referenz für Datenarchitektur und Datenmanagement. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7699949799/toc.pdf?utm_source=chatgpt.com)) |
| Fachliche Definition | Kurze, verbindliche Beschreibung, was das Datenobjekt bedeutet und was nicht dazugehört. | „Vorgang = fachlicher Verwaltungsfall von Antragseingang bis Abschluss.“ | Data Governance nach DAMA erfordert gemeinsame Begriffe und Standards. ([dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/?utm_source=chatgpt.com)) |
| Zweck der Verarbeitung | Warum wird das Datenobjekt benötigt? | Entscheidung vorbereiten, Nachweis prüfen, Zahlung auslösen. | DSGVO Art. 5 verlangt zweckbezogene und minimierte Verarbeitung personenbezogener Daten. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Erzeugendes System | Wo entsteht das Datenobjekt initial? | Portal erzeugt Antrag; Fachverfahren erzeugt Vorgang. | Architekturpraxis auf Basis Application/Data-Beziehung. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7699949799/toc.pdf?utm_source=chatgpt.com)) |
| Führendes System | Wo liegt die verbindliche fachliche Wahrheit? | Fachverfahren für Vorgangsstatus; Register für aktuelle Stammdaten. | Registermodernisierung stärkt interoperable Register als Datenquellen. ([it-planungsrat.de](https://www.it-planungsrat.de/projekte/registermodernisierung?utm_source=chatgpt.com)) |
| Ändernde Systeme/Rollen | Wer darf Daten ändern? | Sachbearbeitung ändert Status; Kasse ändert Zahlungsstatus. | BSI-Schutzbedarf: Integrität muss je Zielobjekt betrachtet werden. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/Lektion_4_05/Lektion_4_05_node.html?utm_source=chatgpt.com)) |
| Lesende Systeme/Rollen | Wer nutzt Daten ohne Änderungsrecht? | Reporting liest Status; DMS liest Bescheiddaten. | Data Governance trennt Verantwortlichkeit und Nutzung. ([snowflake.com](https://www.snowflake.com/en/fundamentals/data-governance/framework/dama-dmbok/?utm_source=chatgpt.com)) |
| Datensenken/Kopien | Wo landen Kopien, Replikate oder Auszüge? | BI, Archiv, Suchindex, Monitoring, Exportdatei. | DSGVO-Speicherbegrenzung macht Kopien architekturrelevant. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Schnittstellen/Datenflüsse | Über welche Schnittstellen fließen Daten? | REST-API, Event, Datei, Fachstandard, DMS-Schnittstelle. | TOGAF kennt Datenverteilung und Datenflüsse als Architekturartefakte. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7699949799/toc.pdf?utm_source=chatgpt.com)) |
| Registerbezug | Stammt das Objekt oder ein Attribut aus einem Register? | Meldeadresse, Unternehmensdaten, Nachweisstatus. | NOOTS soll sicheren digitalen Datenaustausch zwischen Behörden ermöglichen. ([noots.gov.de](https://noots.gov.de/startseite?utm_source=chatgpt.com)) |
| Datenqualität | Welche Qualitätsregeln gelten? | Pflichtfelder, Dublettenprüfung, Plausibilität, Aktualitätsprüfung. | DAMA-DMBOK umfasst Data Quality als Wissensbereich. ([dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/?utm_source=chatgpt.com)) |
| Schutzbedarf | Bewertung von Vertraulichkeit, Integrität, Verfügbarkeit. | Zahlungsbetrag: Integrität hoch; Nachweis: Vertraulichkeit hoch. | BSI-Grundschutz nutzt die Grundwerte Vertraulichkeit, Integrität und Verfügbarkeit. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Data Owner | Fachliche Verantwortlichkeit für Bedeutung, Regeln und Qualität. | Referat Leistungsrecht, Fachbereich Auszahlung. | Data Governance ist zentraler Bezugspunkt im DAMA-DMBOK. ([snowflake.com](https://www.snowflake.com/en/fundamentals/data-governance/framework/dama-dmbok/?utm_source=chatgpt.com)) |
| Technischer Custodian | Technische Betriebs-/Verwahrungsverantwortung. | Plattformteam, Datenbankbetrieb, DMS-Betrieb. | Architekturpraxis; Governance trennt fachliche und technische Verantwortung. ([dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/?utm_source=chatgpt.com)) |
| Aufbewahrung/Löschung | Fristen, Archivierung, Sperrung, Löschereignis. | Löschung nach Ablauf der Aufbewahrungsfrist; Archivierung nach Vorgangsabschluss. | DSGVO Art. 5 enthält Speicherbegrenzung als Grundsatz. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Risiken/Entscheidungsbedarf | Offene Fragen und Architekturentscheidungen. | „Unklar, ob BI personenbezogene Rohdaten benötigt.“ | BSI und DSGVO machen Risikosichtbarkeit im Datenumgang erforderlich. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |

## 10. Interviewfragen für Workshops

### Fragen an den Fachbereich

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Datenobjekte | „Über welche fachlichen Objekte sprechen Sie im Verfahren?“ | Antrag, Vorgang, Person, Nachweis, Bescheid, Zahlung. | Datenarchitektur beginnt bei fachlichen Datenentitäten. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7699949799/toc.pdf?utm_source=chatgpt.com)) |
| Fachliche Wahrheit | „Wenn zwei Systeme unterschiedliche Werte zeigen: Welcher Wert gilt?“ | Adresse im Portal vs. Adresse im Register. | Registermodernisierung stärkt Register als interoperable Datenquellen. ([it-planungsrat.de](https://www.it-planungsrat.de/projekte/registermodernisierung?utm_source=chatgpt.com)) |
| Entscheidungsrelevanz | „Welche Daten sind für den Bescheid entscheidend?“ | Nachweisdatum, Prüfungsergebnis, Frist, Rechtsgrundlage. | DSGVO-Richtigkeit und Integrität sind für personenbezogene Verarbeitung relevant. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Statuslogik | „Welche Status gibt es, wer darf sie ändern, und was lösen sie aus?“ | „in Prüfung“, „Nachweis fehlt“, „bewilligt“, „abgelehnt“. | Integrität des Status kann fachliche Schäden erzeugen; BSI-Schutzbedarf prüfen. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Nachweise | „Welche Nachweise werden erhoben, abgerufen, geprüft oder ersetzt?“ | Upload durch Antragsteller oder Registerabruf. | Once-Only-Prinzip soll erneute Nachweisübermittlung vermeiden. ([noots.gov.de](https://noots.gov.de/startseite?utm_source=chatgpt.com)) |
| Qualität | „Woran erkennen Sie falsche, unvollständige oder veraltete Daten?“ | Dublette, falscher Status, abgelaufener Nachweis. | DAMA-DMBOK umfasst Data Quality als Kernbereich. ([dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/?utm_source=chatgpt.com)) |
| Verantwortung | „Wer entscheidet über Datenregeln, Pflichtfelder und Korrekturen?“ | Referatsleitung, Fachadministration, Datensteward. | Data Governance steht im Zentrum des DMBOK-Frameworks. ([snowflake.com](https://www.snowflake.com/en/fundamentals/data-governance/framework/dama-dmbok/?utm_source=chatgpt.com)) |
| Aufbewahrung | „Wann endet der fachliche Bedarf, und welche Aufbewahrungspflichten gelten?“ | Vorgang abgeschlossen, Widerspruchsfrist abgelaufen, Archivfrist läuft. | DSGVO verlangt Speicherbegrenzung und Zweckbindung. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Berichtsnutzung | „Welche Kennzahlen werden aus den Daten gebildet?“ | Fallzahlen, Bearbeitungszeit, Rückstände, Zahlungsvolumen. | Analytische Datenarchitekturen müssen Herkunft und Ableitung klären. ([arxiv.org](https://arxiv.org/abs/2212.03612?utm_source=chatgpt.com)) |
| Risiko | „Was wäre fachlich schlimm, wenn diese Daten falsch, weg oder unbefugt sichtbar wären?“ | Falscher Bescheid, falsche Zahlung, Datenschutzvorfall, Fristversäumnis. | BSI bewertet Schutzbedarf anhand möglicher Schäden bei verletzten Grundwerten. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |

### Fragen an IT, Betrieb und Security

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Schnittstellen | „Welche Systeme tauschen welche Daten über welchen Mechanismus aus?“ | REST, Messaging, Datei, DMS-Connector, Registerabruf. | TOGAF: Datenverteilung und Datenflüsse sind Datenarchitekturartefakte. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7699949799/toc.pdf?utm_source=chatgpt.com)) |
| Protokollierung | „Welche Datenzugriffe und Änderungen werden protokolliert?“ | Registerabruf, Statusänderung, Bescheidfreigabe. | BSI-Grundwerte Integrität und Nachvollziehbarkeit sind für Schutzbedarf relevant. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Kopien | „Wo entstehen technische Kopien, Caches, Exporte, Suchindizes oder BI-Replikate?“ | Elasticsearch-Index, Data Warehouse, CSV-Export. | DSGVO-Speicherbegrenzung betrifft auch Kopien und Replikate. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Löschung | „Wie wird Löschung technisch in Fachverfahren, DMS, BI, Logs und Backups umgesetzt?“ | Löschjob, Sperrkennzeichen, Archivregel, Backup-Retention. | DSGVO Art. 5 enthält Speicherbegrenzung als Grundsatz. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Berechtigungen | „Welche Rollen dürfen Daten lesen, ändern, exportieren oder administrieren?“ | Sachbearbeitung, Fachaufsicht, Admin, Dienstleister. | Schutzbedarf nach BSI ist auch Grundlage für Zugriffsschutz. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/Lektion_4_05/Lektion_4_05_node.html?utm_source=chatgpt.com)) |
| Datenqualität technisch | „Welche Validierungen und Plausibilitätsprüfungen sind automatisiert?“ | Pflichtfelder, Formatprüfung, Dublettenprüfung, Statusübergänge. | DAMA-DMBOK umfasst Data Quality. ([dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/?utm_source=chatgpt.com)) |
| Betriebsrisiko | „Was passiert, wenn Register, DMS, Kasse oder BI nicht verfügbar sind?“ | Antrag kann nicht abgeschlossen werden; Bescheid kann nicht archiviert werden. | Verfügbarkeit ist einer der BSI-Grundwerte. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |

## 11. Modellierungsregeln für gute Datenlandkarten

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Fachlich vor technisch | Beginne mit Datenobjekten und Verwaltungszwecken, nicht mit Tabellen, APIs oder Produkten. | „Bescheid“ vor „BESCHEID_TBL“. | TOGAF trennt Architekturartefakte von physischer Implementierung. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7699949799/toc.pdf?utm_source=chatgpt.com)) |
| Ein Datenobjekt, eine Definition | Jedes Datenobjekt braucht eine kurze, eindeutige Definition. | „Nachweis = Information oder Dokument, das eine Anspruchsvoraussetzung belegt.“ | DAMA-DMBOK unterstützt standardisiertes Datenmanagement. ([dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/?utm_source=chatgpt.com)) |
| Führendes System explizit markieren | Markiere pro Datenobjekt oder Attribut, welches System verbindlich ist. | Register für aktuelle Adresse; Fachverfahren für Vorgangsstatus. | Registermodernisierung zielt auf vernetzte, interoperable Register. ([it-planungsrat.de](https://www.it-planungsrat.de/projekte/registermodernisierung?utm_source=chatgpt.com)) |
| Kopien als Kopien kennzeichnen | Jede Replikation, jeder Export und jeder Cache muss sichtbar sein. | BI-Auszug ist nicht führend für operative Entscheidung. | Speicherbegrenzung und Datenminimierung machen Kopien risikorelevant. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Datenflüsse mit Zweck modellieren | Kein Pfeil ohne fachlichen Zweck. | „Abruf Meldeadresse zur Identitätsprüfung“. | DSGVO verlangt zweckbezogene Verarbeitung personenbezogener Daten. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Schutzbedarf je Objekt und Fluss | Vertraulichkeit, Integrität und Verfügbarkeit nicht nur auf Systemebene betrachten. | Zahlungsdaten: Integrität hoch; Registerabruf: Vertraulichkeit hoch. | BSI-Schutzbedarf erfolgt entlang der Grundwerte. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Verantwortlichkeit trennen | Data Owner, System Owner, Betreiber und Datenschutzrolle nicht vermischen. | Fachbereich verantwortet Statuslogik; IT betreibt Datenbank. | Data Governance ist zentraler Bestandteil von Data Management. ([snowflake.com](https://www.snowflake.com/en/fundamentals/data-governance/framework/dama-dmbok/?utm_source=chatgpt.com)) |
| Lebenszyklus modellieren | Erhebung, Nutzung, Archivierung, Löschung und Sperrung gehören in die Landkarte. | Vorgang abgeschlossen, Aufbewahrungsfrist beginnt. | DSGVO Art. 5: Speicherbegrenzung. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Reporting separieren | Berichtsdaten sind abgeleitet und brauchen Herkunft, Berechnungslogik und Nutzungsgrenzen. | KPI „Bearbeitungsdauer“ aus Statushistorie. | Analytische Datenarchitektur trennt operative und auswertende Nutzung. ([arxiv.org](https://arxiv.org/abs/2212.03612?utm_source=chatgpt.com)) |
| Offene Entscheidungen sichtbar lassen | Unklarheiten nicht glätten, sondern als Entscheidungsbedarf markieren. | „Führendes System für Kommunikationsstatus offen.“ | Architekturarbeit nach TOGAF ist iterativ und entscheidungsorientiert. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7698999699/toc.pdf?utm_source=chatgpt.com)) |

## 12. Typische Fehler und fachliche Korrektur

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Fehler: Systemliste statt Datenlandkarte | Es werden Anwendungen aufgelistet, aber keine Datenobjekte, Verantwortungen oder Lebenszyklen beschrieben. | „Portal → Fachverfahren → DMS“ ohne Aussage zu Person, Nachweis, Bescheid. | TOGAF betrachtet Datenarchitektur als eigene Domäne, nicht nur als Applikationsübersicht. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/9698999899/toc.pdf?utm_source=chatgpt.com)) |
| Korrektur | Datenobjekte zuerst erfassen, dann Systeme je Datenobjekt zuordnen. | Person, Vorgang, Nachweis, Bescheid, Zahlung. | TOGAF Data Architecture. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7699949799/toc.pdf?utm_source=chatgpt.com)) |
| Fehler: Führendes System bleibt unklar | Mehrere Systeme ändern dieselben Attribute; niemand weiß, welcher Wert gilt. | Adresse wird im Portal, Fachverfahren und DMS geändert. | Registermodernisierung adressiert interoperable Register und Datenaustausch. ([it-planungsrat.de](https://www.it-planungsrat.de/projekte/registermodernisierung?utm_source=chatgpt.com)) |
| Korrektur | Attributgenau klären: aktuelle Adresse im Register, Zustelladresse im Fachverfahren, Dokumentadresse im Bescheid. | Drei Bedeutungen, drei Regeln. | Data Governance/DAMA. ([dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/?utm_source=chatgpt.com)) |
| Fehler: Berichtssystem wird Schattenquelle | BI korrigiert Daten manuell und liefert später „bessere“ Zahlen als das Fachverfahren. | Excel-Korrektur für Leitungsbericht. | Analytische Datenarchitektur muss Herkunft und Ableitung klären. ([arxiv.org](https://arxiv.org/abs/2212.03612?utm_source=chatgpt.com)) |
| Korrektur | BI als abgeleitete Sicht markieren; Korrekturen zurück in fachlichen Klärprozess. | Fehlerliste an Data Steward. | DAMA Data Quality/Data Governance. ([dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/?utm_source=chatgpt.com)) |
| Fehler: Löschung nur im Fachverfahren betrachtet | Daten bleiben in DMS, Exporten, Suchindex, Logs oder Backups erhalten. | Vorgang gelöscht, aber PDF liegt weiter im Exportverzeichnis. | DSGVO-Speicherbegrenzung gilt für personenbezogene Datenverarbeitung. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Korrektur | Löschkette modellieren: Fachverfahren, DMS, BI, Logs, Archiv, Backup-Retention. | Lösch-/Sperrkonzept je Datenobjekt. | DSGVO Art. 5. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Fehler: Schutzbedarf nur auf Anwendungsebene | Die Anwendung wird „hoch“ bewertet, aber einzelne Datenflüsse und Objekte bleiben unbewertet. | Registerabruf unverschlüsselt oder unzureichend protokolliert. | BSI bewertet Schutzbedarf entlang Vertraulichkeit, Integrität, Verfügbarkeit. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Korrektur | Schutzbedarf je Datenobjekt und Datenfluss erfassen. | Nachweis, Zahlung, Bescheid, Auditlog separat bewerten. | BSI-Grundschutz. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/Lektion_4_05/Lektion_4_05_node.html?utm_source=chatgpt.com)) |
| Fehler: Data Owner wird mit System Owner verwechselt | IT wird für fachliche Bedeutung und Qualität verantwortlich gemacht. | Betriebsteam soll entscheiden, welche Status fachlich zulässig sind. | Data Governance ist zentraler Bestandteil von Data Management. ([snowflake.com](https://www.snowflake.com/en/fundamentals/data-governance/framework/dama-dmbok/?utm_source=chatgpt.com)) |
| Korrektur | Fachlicher Data Owner entscheidet Bedeutung und Regeln; IT verantwortet technische Umsetzung. | Fachbereich definiert Statusmodell, IT implementiert. | DAMA-DMBOK. ([dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/?utm_source=chatgpt.com)) |

## 13. Konkretes Visualisierungsmodell

Eine gute Datenlandkarte besteht aus drei Ebenen.

Die erste Ebene ist die **fachliche Datenobjektkarte**. Sie zeigt die großen Datenobjekte und ihre Beziehungen: Person stellt Antrag, Antrag erzeugt Vorgang, Vorgang nutzt Nachweise, Prüfung erzeugt Entscheidung, Entscheidung erzeugt Bescheid, Bescheid kann Zahlung auslösen, alles wird in der Akte dokumentiert.

Die zweite Ebene ist die **System-/Datenflusskarte**. Sie zeigt Portal, Fachverfahren, Register, DMS/eAkte, Zahlungsplattform, Kommunikationsdienst, Reporting, Archiv und IAM/Audit. Die Pfeile sind nach Datenobjekt beschriftet, nicht nur technisch.

Die dritte Ebene ist die **Governance- und Risikokarte**. Sie ergänzt je Datenobjekt führendes System, Data Owner, Schutzbedarf, Qualitätsregeln, Löschlogik und offene Entscheidungen.

Für Behörden empfehle ich diese Reihenfolge: erst Datenobjektkarte, dann Systemflusskarte, dann Governance-Matrix. Wer direkt mit Systempfeilen beginnt, landet fast immer in einem Integrationsdiagramm und verfehlt die Architekturfrage.

## 14. Mini-Beispiel als textuelle Datenflusskarte

Das Onlineportal erzeugt einen Antrag mit Personendaten, Kontaktdaten und hochgeladenen Nachweisen. Das Fachverfahren übernimmt den Antrag und erzeugt daraus einen Vorgang mit Vorgangsnummer, Status und Fristen. Für bestimmte Stammdaten oder Nachweise ruft das Fachverfahren Registerdaten ab. Der Registerabruf wird protokolliert und mit Zweck, Zeitpunkt und Ergebnis dokumentiert. Die Sachbearbeitung prüft Nachweise und erzeugt eine Entscheidung. Aus der Entscheidung entsteht ein Bescheid, der im Fachverfahren fachlich erzeugt und anschließend im DMS/eAkte abgelegt wird. Wenn eine Zahlung erforderlich ist, sendet das Fachverfahren eine Zahlungsanordnung an das Kassenverfahren. Das Kassenverfahren bestätigt den Zahlungsstatus. Das Reporting liest ausgewählte Status- und Laufzeitdaten, bildet Kennzahlen und darf keine operative Fallentscheidung verändern. Nach Abschluss wird der Vorgang gemäß Aufbewahrungsregel archiviert oder später gelöscht beziehungsweise gesperrt.

Das ist noch kein Bild, aber bereits eine vollständige Architektur-Erzählung. Aus ihr kannst du ein Diagramm, eine Matrix und ein Zielbild ableiten.

## 15. Reviewfragen, mit denen du professionell wirkst

Du wirkst als Enterprise Architekt stark, wenn du ruhige, präzise Fragen stellst. Nicht: „Welche Datenbank nutzt ihr?“ Sondern: „Welches System ist führend für den fachlichen Status, und wie verhindern wir widersprüchliche Statuswerte in Fachverfahren, DMS und Reporting?“

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Führende Systeme | „Für welches Datenobjekt ist welches System verbindlich?“ | Register für Stammdatum, Fachverfahren für Vorgang, DMS für Aktennachweis. | Registermodernisierung/TOGAF. ([it-planungsrat.de](https://www.it-planungsrat.de/projekte/registermodernisierung?utm_source=chatgpt.com)) |
| Datenqualität | „Welche Qualitätsregel verhindert falsche Bescheide?“ | Nachweis darf bei Entscheidung nicht abgelaufen sein. | DAMA-DMBOK Data Quality. ([dama.org](https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/?utm_source=chatgpt.com)) |
| Schutzbedarf | „Was passiert, wenn dieses Datenobjekt falsch, unbefugt sichtbar oder nicht verfügbar ist?“ | Falsche Auszahlung, Datenschutzvorfall, Fristversäumnis. | BSI-Schutzbedarf. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Löschung | „Wo liegen Kopien, und wie werden sie nach Fristende behandelt?“ | Fachverfahren, DMS, BI, Export, Suchindex, Logs. | DSGVO Art. 5 Speicherbegrenzung. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Registerbezug | „Welche Daten sollen künftig nicht mehr vom Antragsteller erhoben, sondern aus Registern abgerufen werden?“ | Meldeadresse, Nachweisstatus. | Once-Only/NOOTS. ([noots.gov.de](https://noots.gov.de/startseite?utm_source=chatgpt.com)) |
| Berichtsdaten | „Welche Kennzahl basiert auf welchem operativen Ereignis?“ | Bearbeitungsdauer = Zeit zwischen Antragseingang und Bescheidfreigabe. | Analytische Datenarchitektur. ([arxiv.org](https://arxiv.org/abs/2212.03612?utm_source=chatgpt.com)) |
| Aktennachweis | „Was muss später beweisbar sein?“ | Bescheidversion, Zustellung, Nachweisstand, Prüfergebnis. | DSGVO und Verwaltungspraxis; personenbezogene Verarbeitung muss nachvollziehbar und begrenzt sein. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Schnittstellen | „Welche Datenobjekte werden übertragen, nicht nur welche Systeme sind verbunden?“ | Bescheid-PDF plus Aktenmetadaten an DMS. | TOGAF Data Architecture. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7699949799/toc.pdf?utm_source=chatgpt.com)) |

## 16. Executive-Formulierungen

Eine Datenlandkarte ist gegenüber Leitung und Auftraggebern kein Selbstzweck. Du formulierst ihren Nutzen so:

„Die Datenlandkarte schafft Transparenz darüber, welche Datenobjekte für Verwaltungsentscheidungen relevant sind, welche Systeme dafür führend sind und wo Risiken durch doppelte Pflege, unklare Verantwortung, fehlende Löschlogik oder nicht abgesicherte Datenflüsse entstehen.“

Oder kürzer:

„Wir reduzieren fachliche Widersprüche, technische Nacharbeit und Prüfungsrisiken, indem wir pro Datenobjekt Quelle, Verantwortung, Nutzung, Schutzbedarf und Lebenszyklus verbindlich klären.“

Oder für Ausschreibungen:

„Der Auftragnehmer liefert eine abgestimmte Datenlandkarte für alle verfahrensrelevanten Datenobjekte inklusive führender Systeme, Datenflüsse, Data Owner, Schutzbedarf, Qualitätsregeln, Registerbezug, Aufbewahrung und Löschung. Die Datenlandkarte ist vor Detailimplementierung mit Fachbereich, Datenschutz, Informationssicherheit, Betrieb und Architektur abzustimmen.“

## 17. Deine Übung

Nimm ein fiktives Fachverfahren „Leistungsantrag Bildungshilfe“. Modelliert werden sollen Person, Antrag, Vorgang, Nachweis, Bescheid, Zahlung, Kommunikation, Akte, Bericht und Auditlog.

Arbeite in fünf Schritten. Erstens: Schreibe je Datenobjekt eine fachliche Definition in einem Satz. Zweitens: Bestimme erzeugendes System, führendes System, lesende Systeme und archivierende Systeme. Drittens: Zeichne mindestens sechs Datenflüsse: Portal zu Fachverfahren, Fachverfahren zu Register, Fachverfahren zu DMS, Fachverfahren zu Kasse, Fachverfahren zu Kommunikationsdienst, Fachverfahren zu Reporting. Viertens: Bewerte je Datenobjekt Vertraulichkeit, Integrität und Verfügbarkeit mit normal, hoch oder sehr hoch. Fünftens: Markiere mindestens fünf offene Architekturentscheidungen.

Ein gutes Ergebnis enthält zum Beispiel folgende Entscheidungspunkte: Ist das Register führend für aktuelle Personendaten oder nur Quelle zum Abrufzeitpunkt? Wird der Bescheid im Fachverfahren oder im DMS versioniert? Darf Reporting personenbezogene Rohdaten sehen oder nur aggregierte Daten? Wie wird ein abgelaufener Nachweis erkannt? Wie wird eine Löschanforderung über Fachverfahren, DMS, BI und Protokolle hinweg behandelt?

## 18. Musterlösung in Kurzform

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Person | Register ist führend für aktuelle Stammdaten; Fachverfahren speichert verwendeten Entscheidungsstand. | Adresse aus Register am 13.06.2026 verwendet. | Once-Only und Registermodernisierung. ([noots.gov.de](https://noots.gov.de/startseite?utm_source=chatgpt.com)) |
| Antrag | Portal erzeugt Antrag; Fachverfahren übernimmt und wird nach Eingang führend für Bearbeitung. | Antragseingang mit Zeitstempel. | TOGAF Data/Application-Bezug. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7699949799/toc.pdf?utm_source=chatgpt.com)) |
| Vorgang | Fachverfahren ist führend für Vorgangsnummer, Status, Fristen und Bearbeitung. | Status „in Prüfung“. | Data Architecture nach TOGAF. ([pubs.opengroup.org](https://pubs.opengroup.org/onlinepubs/7699949799/toc.pdf?utm_source=chatgpt.com)) |
| Nachweis | Quelle variiert; Fachverfahren dokumentiert verwendeten Nachweisstand. | Upload oder Registerabruf. | NOOTS/Once-Only. ([noots.gov.de](https://noots.gov.de/startseite?utm_source=chatgpt.com)) |
| Bescheid | Fachverfahren erzeugt; DMS/eAkte archiviert finale Fassung. | Bewilligungsbescheid als PDF/A. | DSGVO-Grundsätze und Nachweisfähigkeit. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Zahlung | Fachverfahren löst an; Kassenverfahren ist führend für Buchungsstatus. | Auszahlung bestätigt. | BSI Integrität/Verfügbarkeit. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Kommunikation | Kommunikationsdienst versendet; Fachverfahren oder DMS führt Nachweis. | Fristsetzung zugestellt. | DSGVO Speicherbegrenzung/Zweckbindung. ([eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de&utm_source=chatgpt.com)) |
| Bericht | BI erzeugt Kennzahlen aus replizierten oder aggregierten Daten. | Durchschnittliche Bearbeitungszeit. | Analytische Datenarchitektur. ([arxiv.org](https://arxiv.org/abs/2212.03612?utm_source=chatgpt.com)) |
| Auditlog | Systeme erzeugen Auditereignisse; Zugriff und Änderung müssen nachvollziehbar sein. | Registerabruf durch Sachbearbeiter. | BSI-Schutzbedarf und Integrität. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |

## 19. Merksatz für deine Praxis

Eine Datenlandkarte beantwortet nicht die Frage: „Welche Systeme haben wir?“ Sie beantwortet die viel wichtigere Frage: **„Welche fachlichen Daten brauchen wir, wo entsteht ihre Wahrheit, wer trägt Verantwortung, wohin fließen sie, wie schützen wir sie, und wann endet ihre berechtigte Nutzung?“**

Wenn du diese Frage sauber beantworten kannst, erkennst du als Enterprise Architekt sehr früh die kritischen Bruchstellen einer Behördenlandschaft: doppelte Pflege, falsche Verantwortlichkeiten, ungeklärte Registerbezüge, schwache Schnittstellenverträge, riskante Kopien, fehlende Löschketten und Berichtszahlen ohne belastbare Herkunft.

<>