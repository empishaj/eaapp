## Checkliste: BPMN für Verwaltungsverfahren sicher anwenden

1. **Kläre zuerst den Modellzweck:** Willst du verstehen, optimieren, abstimmen, automatisieren oder auditierbar dokumentieren?

2. **Trenne Prozesslandkarte, Fachprozessmodell, technisches Ablaufmodell und ausführbares Workflowmodell.**

3. **Modelliere immer einen klaren Auslöser:** Ein Verwaltungsprozess beginnt selten „einfach so“, sondern durch Antrag, Frist, Nachricht, Ereignis oder internen Prüfauftrag.

4. **Verwende Pools für eigenständige Beteiligte:** Behörde, Antragsteller, andere Behörde, Register, DMS oder externer Dienstleister.

5. **Verwende Lanes für Verantwortlichkeiten innerhalb eines Pools:** Eingangsstelle, Sachbearbeitung, Fachprüfung, Entscheidungsstelle, Rechtsbehelf, Systemunterstützung.

6. **Nutze Sequenzflüsse nur innerhalb eines Pools und Nachrichtenflüsse zwischen Pools.**

7. **Benutze Gateways nur für echte Verzweigungen, Parallelitäten oder ereignisabhängige Pfade.**

8. **Mache Wartezeiten sichtbar:** Fristen, Rückmeldungen, Nachforderungen, Wiedervorlagen und Eskalationen sind in Behörden oft der eigentliche Prozesskern.

9. **Mache Medienbrüche sichtbar:** Papier, E-Mail, Fachverfahren, Excel-Liste, DMS/eAkte, Registerabfrage, manuelle Übertragung.

10. **Unterscheide fachliche Entscheidung von technischem Routing:** Die Frage „Ist der Antrag bewilligungsfähig?“ gehört fachlich in Entscheidungstabellen oder Fachregeln; die Frage „Welcher Pfad läuft danach?“ gehört ins Prozessmodell.

11. **Halte BPMN fachlich lesbar:** Ein Modell, das nur ein Tool oder ein Entwickler versteht, ist für Architekturkommunikation ungeeignet.

12. **Übersetze Prozessbefunde immer in Architekturentscheidungen:** Medienbruch wird Integrationsanforderung, Wartezeit wird SLA-/SLO-Frage, Rollenunklarheit wird IAM-Thema, Aktenablage wird DMS-/eAkte-Anforderung.

<>

## 1. Grundhaltung: BPMN ist kein Malprogramm, sondern eine Präzisionssprache für Verantwortung, Ablauf und Übergabe

BPMN steht für **Business Process Model and Notation**. Die Object Management Group beschreibt BPMN 2.0.2 als formalen Standard für Geschäftsprozessdiagramme, der von fachlichen Beteiligten verstanden werden soll und zugleich präzise genug ist, um in softwarebezogene Prozesskomponenten überführt werden zu können. Genau diese Doppelrolle macht BPMN für Bundesbehörden wertvoll: Es verbindet Fachseite, Organisation, IT, Betrieb, Dienstleister und Architektur in einer gemeinsamen Prozesssprache. ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN))

Für dich als Enterprise Architekt ist BPMN nicht primär interessant, weil du schöne Prozessbilder erzeugst. Der eigentliche Wert liegt darin, **Unklarheiten sichtbar zu machen**: Wer entscheidet? Wer wartet? Wer trägt Daten um? Wo wird doppelt geprüft? Wo liegt der Vorgang? Wo endet fachliche Verantwortung und wo beginnt Systemautomatisierung? Wo entstehen Frist-, Datenschutz-, IAM-, DMS-, Register-, Schnittstellen- oder Betriebsanforderungen?

Gerade in der Verwaltung sind Prozesse oft nicht linear. Sie bestehen aus Eingang, Vorprüfung, Rückfrage, Fristen, Zuständigkeiten, Fachprüfung, Dokumentation, Aktenführung, Bescheidung, Versand, Widerspruch und ggf. Rückkopplung in Fachverfahren. Eine einfache Pfeilgrafik reicht dafür oft nicht aus, weil sie Ereignisse, Rollen, Zuständigkeiten, Fristen und Nachrichtenflüsse nicht sauber unterscheidet. Das Organisationshandbuch des Bundes beziehungsweise die Prozessmanagement-Angebote des Bundesverwaltungsamts behandeln Prozessmanagement als systematisches Managementthema für Behörden, nicht als isolierte Modellierungsübung. ([orghandbuch.de](https://www.orghandbuch.de/Webs/OHB/DE/OrganisationshandbuchNEU/3_managementansaetze_u_instrumente/3_3_Prozessmanagement/prozessmanagement-node.html?utm_source=chatgpt.com))

## 2. Die wichtigste Korrektur: BPMN ist nicht automatisch Prozessautomation

Ein häufiger Fehler lautet: „Wir modellieren BPMN, also automatisieren wir den Prozess.“ Das ist falsch. BPMN kann auf mehreren Ebenen verwendet werden. Ein fachliches BPMN-Modell zeigt, **was fachlich passiert**. Ein technisches Ablaufmodell zeigt, **wie Systeme, Schnittstellen und technische Komponenten zusammenspielen**. Ein ausführbares BPMN-Modell zeigt, **was eine Workflow-Engine tatsächlich steuern kann**. Die OMG weist BPMN zwar auch eine Brückenfunktion in Richtung Softwarekomponenten zu, aber daraus folgt nicht, dass jedes fachliche Behördenmodell direkt ausführbar sein sollte. ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN))

In der Bundesbehördenpraxis solltest du deshalb immer zuerst den Zweck klären. Willst du einen Ist-Prozess verstehen, ist ein fachliches Modell mit Rollen, Wartezeiten, Medienbrüchen und Systemunterstützung richtig. Willst du später Workflow-Automation betreiben, brauchst du zusätzlich technische Präzision: eindeutige Ereignisse, ausführbare Tasks, Datenobjekte, Fehlerpfade, Service-Tasks, User-Tasks, Schnittstellenverträge, Berechtigungen, Audit-Logging, Wiederanlaufverhalten und Betriebsmodell.

## 3. Die drei Sichtweisen: Fachprozess, technisches Ablaufmodell, ausführbare Prozessautomation

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| **Fachliche Prozesssicht** | Beschreibt den Ablauf aus Sicht der Verwaltung: Rollen, Zuständigkeiten, fachliche Entscheidungen, Dokumente, Fristen, Übergaben und Ausnahmen. Sie muss von Fachbereich, Organisation, Projektleitung und Architektur verstanden werden. | „Antrag wird angenommen, auf Vollständigkeit geprüft, bei fehlenden Nachweisen nachgefordert, fachlich bewertet, entschieden, beschieden und abgelegt.“ | BPMN ist als stakeholderverständliche Notation angelegt. ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN)) |
| **Technische Ablaufmodellierung** | Beschreibt, welche Systeme, Schnittstellen, Nachrichten, Datenobjekte und technischen Komponenten beteiligt sind. Diese Sicht ist präziser, aber nicht zwingend direkt ausführbar. | „Portal sendet Antrag an API-Gateway, Fachverfahren legt Vorgang an, Registerschnittstelle prüft Stammdaten, DMS speichert Bescheid.“ | BPMN kann fachliche und softwarebezogene Sichten verbinden. ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN)) |
| **Ausführbare Prozessautomation** | Beschreibt einen Prozess so exakt, dass eine Workflow- oder Process-Engine Aufgaben, Ereignisse, Service-Aufrufe, Timer, Fehlerpfade und Zustände steuern kann. | „Nach 14 Tagen ohne Rückmeldung erzeugt die Engine automatisch eine Wiedervorlage oder Eskalation.“ | BPMN 2.0.2 enthält neben der grafischen Spezifikation auch maschinenlesbare Artefakte wie XML-Schemata. ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN)) |
| **Prozesslandkarte** | Zeigt nur die grobe Prozessfamilie und deren Zusammenhang. Sie ist keine Ablaufmodellierung. | „Antragsbearbeitung“, „Widerspruchsbearbeitung“, „Bescheidversand“, „Aktenführung“, „Statistikmeldung“. | Prozessmanagement in Behörden wird als systematische Identifikation, Dokumentation und Analyse verstanden. ([bva.bund.de](https://www.bva.bund.de/SharedDocs/Downloads/DE/Behoerden/Beratung/Prozessmanagement/Leitfaeden/Kurzleitfaden_GPM.pdf?__blob=publicationFile&v=1&utm_source=chatgpt.com)) |

Merksatz: **Die Prozesslandkarte sagt, welche Prozesse es gibt. BPMN sagt, wie ein konkreter Prozess abläuft. Das technische Modell sagt, welche Systeme daran beteiligt sind. Das ausführbare Modell sagt, was eine Engine steuern darf.**

## 4. BPMN-Grundelemente für Behördenprozesse

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| **Pool** | Ein Pool repräsentiert einen eigenständigen Prozessbeteiligten oder Verantwortungsraum. Zwischen Pools fließen Nachrichten, nicht Sequenzflüsse. | Pool „Antragsteller“, Pool „Bundesbehörde“, Pool „Registerbehörde“, Pool „Postdienstleister“. | BPMN nutzt Pools und Lanes zur Darstellung von Beteiligten und Verantwortlichkeiten. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Lane** | Eine Lane unterteilt einen Pool nach Rollen, Organisationseinheiten oder Verantwortlichkeiten. | Lane „Eingangsstelle“, „Sachbearbeitung“, „Fachprüfung“, „Entscheidungsstelle“, „Rechtsbehelf“. | Pools und Schwimmbahnen helfen, organisatorische Strukturen und Zuständigkeiten abzubilden. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Start Event** | Markiert den Auslöser eines Prozesses. In Behörden meist Antrag, Nachricht, Frist, interner Auftrag oder externer Trigger. | „Antrag eingegangen“, „Widerspruch eingegangen“, „Frist abgelaufen“. | BPMN-Ereignisse kennzeichnen Beginn, Ende oder Zwischenzustände. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Intermediate Event** | Markiert ein Ereignis während des Prozesses, z. B. Nachricht, Timer, Fehler oder Eskalation. | „Nachweise eingegangen“, „14-Tage-Frist abgelaufen“, „Register nicht erreichbar“. | Ereignisse können durch Zeitvorgaben, Nachrichten oder externe Auslöser ausgelöst werden. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **End Event** | Markiert das fachliche oder technische Ende eines Prozesspfads. | „Bescheid versandt“, „Antrag abgelehnt“, „Vorgang abgelegt“, „Widerspruch abgeschlossen“. | BPMN unterscheidet Start-, Zwischen- und Endereignisse. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Task** | Eine atomare Tätigkeit. Sie sollte aktiv formuliert werden: Verb + Objekt. | „Antrag erfassen“, „Nachweise prüfen“, „Bescheid erstellen“, „Vorgang archivieren“. | Aktivitäten und Gateways steuern Prozesslogik und Ablauf. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **User Task** | Eine Tätigkeit, die ein Mensch mit Systemunterstützung ausführt. | Sachbearbeiter prüft im Fachverfahren die Vollständigkeit. | BPMN kann fachliche Arbeit und technische Ausführung unterscheidbar machen. ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN)) |
| **Manual Task** | Eine manuelle Tätigkeit ohne direkte Systemsteuerung. | Papierakte aus Archiv holen, Unterschriftenmappe weitergeben, Poststück öffnen. | Für Verwaltungsanalyse wichtig, weil manuelle Tätigkeiten Medienbrüche sichtbar machen. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Service Task** | Automatisierter Systemaufruf. | Registerdaten abrufen, Aktenmetadaten im DMS speichern, Versandstatus abfragen. | BPMN kann in softwarebezogene Komponenten überführt werden. ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN)) |
| **Business Rule Task** | Auswertung von Regeln oder Entscheidungstabellen, häufig besser mit DMN kombiniert. | „Bewilligungsfähigkeit anhand Fachregeln prüfen“. | BPMN eignet sich für Ablauf; Entscheidungslogik sollte nicht unkontrolliert im Ablauf versteckt werden. |
| **Exclusive Gateway XOR** | Genau ein Pfad wird gewählt. | „Antrag vollständig?“ Ja oder Nein. | Gateways modellieren Bedingungen und Verzweigungen. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Parallel Gateway AND** | Mehrere Pfade laufen gleichzeitig und müssen ggf. wieder zusammengeführt werden. | Fachprüfung und Registerabfrage laufen parallel. | Gateways steuern Prozesspfade und Parallelitäten. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Event-based Gateway** | Der nächste Pfad hängt davon ab, welches Ereignis zuerst eintritt. | „Nachweise gehen ein“ oder „Frist läuft ab“. | Ereignisbasierte Gateways routen nach eintretenden Ereignissen, nicht nach Datenbedingungen. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Sequence Flow** | Pfeil für die Reihenfolge innerhalb eines Pools. | Von „Antrag erfassen“ zu „Vollständigkeit prüfen“. | Sequenzflüsse dürfen nicht mit Nachrichtenflüssen verwechselt werden. ([omg.org](https://www.omg.org/bpmn/Documents/Introduction_to_BPMN.pdf?utm_source=chatgpt.com)) |
| **Message Flow** | Kommunikation zwischen Pools. | Antragsteller sendet Unterlagen an Behörde; Behörde sendet Bescheid an Antragsteller. | Nachrichtenflüsse werden zwischen Beteiligten verwendet, nicht als normaler Ablaufpfeil innerhalb eines Pools. ([omg.org](https://www.omg.org/bpmn/Documents/Introduction_to_BPMN.pdf?utm_source=chatgpt.com)) |
| **Subprozess** | Kapselt einen detaillierten Teilprozess. | „Fachprüfung durchführen“, „Bescheid erstellen“, „Widerspruch bearbeiten“. | BPMN erlaubt strukturierte Detaillierung, ohne Hauptmodelle zu überladen. |
| **Boundary Event** | Ereignis, das an einer Aktivität hängt und während ihrer Ausführung eintreten kann. | Während „Nachweise anfordern“ läuft die Frist ab. | Angehängte Zwischenereignisse können Aufgaben unterbrechen oder zusätzliche Pfade auslösen. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Error Event** | Technischer oder fachlicher Fehlerpfad. | Registerabfrage fehlgeschlagen, Signaturdienst nicht verfügbar, Versanddienst meldet Fehler. | Fehlerpfade sind für ausführbare oder technische Prozessmodelle besonders relevant. |
| **Escalation Event** | Eskalation ohne zwingenden technischen Fehler. | Fristüberschreitung, Fachprüfung überfällig, Entscheidungsvorlage nicht bearbeitet. | Timer und Ereignisse machen Wartezeiten und Eskalationen modellierbar. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |

## 5. Behördenbeispiel: Antrag, Vorprüfung, Nachforderung, Fachprüfung, Entscheidung, Bescheid, Akte, Widerspruch

Wir nehmen als Annahme ein generisches Verwaltungsverfahren. Es geht nicht um ein konkretes Gesetz, keine echte Fristnorm und keine verbindliche Verfahrensvorgabe. Das Beispiel dient als Architektur- und Modellierungsübung.

Der Prozess beginnt mit dem **Antragseingang**. Der Antrag kann über ein Portal, per Post oder per E-Mail eingehen. Die Eingangsstelle erfasst den Eingang, legt einen Vorgang an und prüft formal, ob Mindestangaben vorhanden sind. Danach prüft die Sachbearbeitung die Vollständigkeit. Fehlen Nachweise, wird eine Nachforderung erstellt. Der Antragsteller erhält eine Nachricht und eine Frist. Treffen Unterlagen ein, wird erneut geprüft. Läuft die Frist ab, wird je nach Verfahrensregel erinnert, abgelehnt oder zur Entscheidung vorgelegt. Ist der Antrag vollständig, folgt die Fachprüfung. Dort können Registerdaten abgefragt, Nachweise bewertet, Risikoklassen ermittelt oder Fachregeln angewandt werden. Danach wird entschieden, ein Bescheid erstellt, versandt und in der eAkte abgelegt. Geht ein Widerspruch ein, startet ein eigener Rechtsbehelfsprozess oder ein angebundener Subprozess.

## 6. Textuelles BPMN-Beispielmodell

### 6.1 Beteiligte Pools und Lanes

**Pool 1: Antragsteller/in**

Dieser Pool enthält die Aktionen des externen Beteiligten: Antrag stellen, Nachweise nachreichen, Bescheid empfangen, ggf. Widerspruch einlegen. Der Antragsteller ist nicht Teil des behördeninternen Sequenzflusses. Zwischen Antragsteller und Behörde werden Nachrichtenflüsse modelliert.

**Pool 2: Bundesbehörde**

Dieser Pool enthält die interne Bearbeitung. Geeignete Lanes sind „Eingangsstelle“, „Sachbearbeitung“, „Fachprüfung“, „Entscheidungsbefugte Stelle“, „Bescheiderstellung/Versand“, „DMS/eAkte/Fachverfahren“ und „Rechtsbehelf“. Ob Systeme als eigene Lane oder als eigener Pool modelliert werden, hängt vom Modellzweck ab. Für fachliche Ist-Analyse reicht oft eine System-Lane; für technische Integration ist ein eigener Pool pro System sauberer.

**Pool 3: Registerbehörde oder Registersystem**

Dieser Pool wird verwendet, wenn Registerabfragen fachlich oder technisch relevant sind. Dadurch wird sichtbar, dass die Behörde auf externe Antwortzeiten, Schnittstellenverfügbarkeit und Datenqualität angewiesen ist.

**Pool 4: Post-/Versanddienst oder Zustelldienst**

Dieser Pool ist sinnvoll, wenn Versand, Zustellung, Rückläufer oder Nachweis der Bekanntgabe relevant sind.

### 6.2 Hauptprozess in textueller BPMN-Form

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| **1. Start im Antragsteller-Pool** | Der Prozess beginnt außerhalb der Behörde. | Start Event: „Bedarf an Verwaltungsleistung entsteht“ → Task: „Antrag ausfüllen“ → Send Task: „Antrag an Behörde senden“. | BPMN modelliert Beteiligte und Nachrichtenbeziehungen über Pools und Message Flows. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **2. Nachricht an Behörde** | Zwischen Antragsteller und Behörde wird ein Nachrichtenfluss verwendet. | Message Flow: „Antrag übermittelt“ an Message Start Event „Antrag eingegangen“. | Nachrichtenflüsse gehören zwischen Beteiligte, Sequenzflüsse innerhalb eines Pools. ([omg.org](https://www.omg.org/bpmn/Documents/Introduction_to_BPMN.pdf?utm_source=chatgpt.com)) |
| **3. Eingang erfassen** | Eingangsstelle dokumentiert den Eingang. | User Task: „Antragseingang registrieren“; Data Object: „Antrag“. | BPMN unterstützt Aufgaben, Datenobjekte und Verantwortlichkeiten. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **4. Vorgang anlegen** | Fachverfahren oder DMS erzeugt Vorgangsnummer. | Service Task: „Vorgang im Fachverfahren anlegen“; Service Task: „Aktenstruktur in eAkte erzeugen“. | BPMN kann fachliche und technische Komponenten verbinden. ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN)) |
| **5. Formale Vorprüfung** | Sachbearbeitung prüft Mindestangaben. | User Task: „Mindestangaben prüfen“. | Aktivitäten beschreiben konkrete Arbeitsschritte. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **6. Gateway Vollständigkeit** | Exklusiver Entscheidungspunkt. | XOR Gateway: „Antrag vollständig?“ Pfade: Ja / Nein. | XOR-Gateways modellieren alternative Pfade. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **7. Nachforderung** | Bei fehlenden Unterlagen wird eine Nachricht erzeugt. | Task: „Nachforderung erstellen“ → Send Task: „Nachforderung versenden“ → Message Flow an Antragsteller. | Nachrichtenereignisse und Timer sind zentrale BPMN-Ereignistypen. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **8. Warten auf Nachweise oder Fristablauf** | Hier ist ein event-based Gateway fachlich sauber. | Event-based Gateway: entweder Message Intermediate Event „Nachweise eingegangen“ oder Timer Intermediate Event „Frist abgelaufen“. | Ereignisbasierte Gateways reagieren auf das zuerst eintretende Ereignis. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **9. Rücklauf prüfen** | Nachweise werden wieder in den Prüfpfad geführt. | Task: „Nachgereichte Unterlagen prüfen“ → zurück zu Gateway „vollständig?“. | Schleifen sind zulässig, müssen aber lesbar und begrenzt modelliert werden. |
| **10. Frist abgelaufen** | Fachlicher Ausnahme- oder Eskalationspfad. | Timer Event „Frist abgelaufen“ → Task „Folgeentscheidung vorbereiten“. | Timer-Ereignisse machen Wartezeiten und Fristen sichtbar. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **11. Fachprüfung** | Fachliche Bewertung, ggf. mit Regeln und Registerdaten. | Subprozess „Fachprüfung durchführen“ mit Registerabfrage, Nachweisbewertung und Risikoklasse. | BPMN eignet sich für Prozesslogik; detaillierte Entscheidungslogik sollte separat strukturiert werden. |
| **12. Registerabfrage** | Externer Informationsaustausch. | Send Task „Registeranfrage senden“ → Message Flow an Registersystem → Receive Task „Registerantwort empfangen“. | Pools und Nachrichtenflüsse zeigen organisationsübergreifende Zusammenarbeit. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **13. Entscheidung** | Ergebnis der Fachprüfung führt zur Entscheidung. | Business Rule Task „Entscheidungsvorschlag ermitteln“ → User Task „Entscheidung prüfen und freigeben“. | Gateways und Tasks bilden Bedingungen und Tätigkeiten ab. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **14. Gateway Ergebnis** | Bewilligung, Ablehnung oder Rückfrage. | XOR Gateway: „Entscheidungsergebnis?“ Pfade: Bewilligen / Ablehnen / Rückfrage. | Gateways sollten echte Alternativen ausdrücken. |
| **15. Bescheiderstellung** | Dokumenterzeugung und Prüfung. | Service Task „Bescheidentwurf erzeugen“ → User Task „Bescheid fachlich prüfen“ → ggf. Task „Freigabe einholen“. | Technische und menschliche Arbeit sollten unterscheidbar bleiben. |
| **16. Versand** | Versand über Portal, Post oder besonderes elektronisches Postfach. | Send Task „Bescheid versenden“ → Message Flow an Antragsteller. | Nachrichtenflüsse zeigen Kommunikation zwischen Beteiligten. ([omg.org](https://www.omg.org/bpmn/Documents/Introduction_to_BPMN.pdf?utm_source=chatgpt.com)) |
| **17. Aktenablage** | Ablage ist kein Nachgedanke, sondern Prozessbestandteil. | Service Task „Bescheid und Nachweise in eAkte ablegen“. | Prozessmanagement vermeidet Inkonsistenzen durch abgestimmte Prozessdokumentation. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **18. End Event** | Der Prozess endet fachlich sauber. | End Event „Bescheid bekanntgegeben und Vorgang abgelegt“. | Endereignisse markieren abgeschlossene Prozesspfade. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **19. Widerspruch** | Widerspruch ist meist eigener Prozess, nicht nur ein Rückpfeil. | Message Start Event „Widerspruch eingegangen“ → Subprozess „Widerspruch bearbeiten“. | Prozesse können durch Nachrichtenereignisse neu gestartet oder fortgesetzt werden. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |

## 7. So sieht das Beispiel als kompakter Prozessfluss aus

**Antragsteller/in:** „Antrag erstellen“ → „Antrag senden“ → Nachricht an Behörde.

**Bundesbehörde / Eingangsstelle:** Message Start Event „Antrag eingegangen“ → „Eingang registrieren“ → „Vorgang im Fachverfahren anlegen“ → „Aktenstruktur in eAkte erzeugen“.

**Bundesbehörde / Sachbearbeitung:** „Mindestangaben prüfen“ → XOR „Antrag vollständig?“.

**Pfad Nein:** „Nachforderung erstellen“ → „Nachforderung versenden“ → Event-based Gateway „Was passiert zuerst?“ → Nachricht „Nachweise eingegangen“ oder Timer „Frist abgelaufen“. Bei Nachweiseingang: „Nachweise erfassen“ → zurück zu „Antrag vollständig?“. Bei Fristablauf: „Folgeentscheidung vorbereiten“ → „Ablehnung wegen fehlender Mitwirkung prüfen“ oder „Erinnerung versenden“, je nach Fachregel.

**Pfad Ja:** Subprozess „Fachprüfung durchführen“. Darin: „Registerabfrage vorbereiten“ → Nachricht an Register → „Registerantwort empfangen“ → „Nachweise bewerten“ → „Risikoklasse bestimmen“ → „Entscheidungsvorschlag erstellen“.

**Entscheidungsstelle:** „Entscheidung prüfen“ → XOR „Bewilligungsfähig?“ → Pfad Bewilligung oder Ablehnung.

**Bescheiderstellung/Versand:** „Bescheidentwurf erzeugen“ → „Bescheid prüfen“ → ggf. „Freigabe einholen“ → „Bescheid versenden“ → Nachricht an Antragsteller.

**DMS/eAkte:** „Bescheid, Antrag, Nachweise und Entscheidungsvermerk ablegen“ → End Event „Vorgang abgeschlossen“.

**Rechtsbehelf:** Message Start Event „Widerspruch eingegangen“ → eigener Subprozess „Widerspruch bearbeiten“.

## 8. Wie du Rollen, Zuständigkeiten und Medienbrüche sichtbar machst

Ein BPMN-Modell wird in der Verwaltung erst dann wertvoll, wenn es nicht nur „Ablauf“ zeigt, sondern **Arbeitswirklichkeit**. Dazu gehören Rollen, Bearbeitungswechsel, Systemwechsel, Papier, E-Mail, Excel, Fachverfahren, DMS, manuelle Kontrollen, Wartezeiten, Fristen und Rückfragen.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| **Rollen** | Jede fachliche Tätigkeit gehört in die Lane der zuständigen Rolle. Dadurch sieht man Verantwortungswechsel. | Eingangsstelle erfasst; Sachbearbeitung prüft; Fachreferat bewertet; Entscheidungsstelle gibt frei. | Pools und Lanes fördern Verständnis für Verantwortlichkeiten. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Zuständigkeiten** | Unklare Zuständigkeit zeigt sich oft durch Aufgaben ohne passende Lane oder durch Rückpfeile zwischen Organisationseinheiten. | „Wer entscheidet bei unvollständigen Unterlagen?“ bleibt offen. | Prozessmanagement soll Transparenz über Abläufe schaffen. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Medienbruch** | Ein Medienbruch liegt vor, wenn Informationen manuell zwischen Kanälen oder Systemen übertragen werden. | Antrag kommt per PDF-Mail, Daten werden manuell ins Fachverfahren übernommen. | Verwaltungsprozessmodelle sollten Dokumentation und Analyse ermöglichen. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Wartezeit** | Wartezeit ist ein Ereignis- oder Timer-Thema, kein unsichtbarer Zwischenraum. | „Warten auf Nachweise“, „Warten auf Registerantwort“, „Wiedervorlage nach 14 Tagen“. | BPMN unterstützt Zeit- und Nachrichtenauslöser. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Manuelle Übergabe** | Manuelle Übergaben verursachen Verlust-, Verzögerungs- und Nachverfolgungsrisiken. | Papierakte wandert zur Fachaufsicht; Excel-Liste wird per E-Mail verteilt. | Fachschalen wie PICTURE-BPMN reduzieren BPMN auf verwaltungsnahe Analyseelemente. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Systemunterstützung** | Systeme sollten sichtbar sein, aber nicht jeden fachlichen Prozess überladen. | Fachverfahren, Register, DMS, Versanddienst, IAM, Portal. | BPMN kann Prozesslogik und IT-nahe Umsetzung verbinden. ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN)) |

Praktische Regel: **Wenn eine Information abgeschrieben, kopiert, per E-Mail verschoben, in Excel nachgehalten oder ausgedruckt wird, zeichne es sichtbar ein.** Genau dort entstehen Architekturthemen.

## 9. Wann BPMN sinnvoll ist und wann eine Prozesslandkarte reicht

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| **BPMN ist sinnvoll, wenn mehrere Rollen beteiligt sind** | Je mehr Übergaben, desto größer der Nutzen von Lanes, Gateways und Ereignissen. | Antragsteller, Eingangsstelle, Sachbearbeitung, Fachprüfung, Register, DMS, Versand. | BPMN unterstützt die Darstellung von Beteiligten und Abläufen. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **BPMN ist sinnvoll bei Fristen und Wartezeiten** | Timer und Ereignisse zeigen, was sonst in Texten verschwindet. | Nachforderung mit 14-Tage-Frist. | BPMN kennt Zeitereignisse und externe Auslöser. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **BPMN ist sinnvoll bei Ausnahmen** | Fehler-, Eskalations- und Abbruchpfade werden sichtbar. | Register nicht erreichbar, Unterlagen fehlen, Widerspruch geht ein. | Ereignisse können Prozesspfade beeinflussen. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **BPMN ist sinnvoll bei Digitalisierungsvorhaben** | Medienbrüche und Systemgrenzen werden Grundlage für Zielarchitektur. | Portal-zu-Fachverfahren-Integration statt manueller Erfassung. | Prozessmanagement ist in öffentlicher Verwaltung für Digitalisierung und Integration relevant. ([ceur-ws.org](https://ceur-ws.org/Vol-933/pap1.pdf?utm_source=chatgpt.com)) |
| **Prozesslandkarte reicht bei grober Orientierung** | Wenn nur Prozessfamilien, Verantwortungsbereiche oder Prioritäten dargestellt werden sollen, ist BPMN zu detailliert. | „Antragsbearbeitung“, „Rechtsbehelf“, „Berichtswesen“, „Aktenführung“. | Prozessmanagement beginnt mit Identifikation und Strukturierung von Prozessen. ([bva.bund.de](https://www.bva.bund.de/SharedDocs/Downloads/DE/Behoerden/Beratung/Prozessmanagement/Leitfaeden/Kurzleitfaden_GPM.pdf?__blob=publicationFile&v=1&utm_source=chatgpt.com)) |
| **Prozesssteckbrief reicht bei stabilen Standardprozessen** | Wenn Ablauf kaum variiert und keine Automations- oder Architekturentscheidung ansteht, genügt oft ein Steckbrief. | „Interne Freigabe einer Standardvorlage“. | Einheitlicher Detailgrad ist in Verwaltungsmodellierung wichtig. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **BPMN ist zu viel bei reiner Aufbauorganisation** | Organigramme, Verantwortungsmatrizen und Rollenmodelle sind keine Prozessmodelle. | „Welche Abteilung ist für welche Leistung zuständig?“ | Pools und Lanes ergänzen, ersetzen aber keine Organisationsmodellierung. |

Merksatz: **Nutze BPMN, wenn Ablauf, Entscheidung, Verantwortung, Ereignis oder Übergabe relevant ist. Nutze eine Prozesslandkarte, wenn du nur Orientierung, Portfolio oder Priorisierung brauchst.**

## 10. Prozessinterview führen: Vorgehen für den Ist-Prozess

Ein gutes BPMN-Modell beginnt nicht im Modellierungstool, sondern im Gespräch. Dein Ziel ist nicht, den Fachbereich mit Symbolen zu beeindrucken. Dein Ziel ist, den tatsächlichen Ablauf so zu verstehen, dass Fachseite, IT und Architektur danach dasselbe Bild vor Augen haben.

### 10.1 Interviewstruktur

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| **1. Prozesszweck klären** | Warum existiert der Prozess? Welche Verwaltungsleistung oder interne Pflicht erfüllt er? | „Bearbeitung eines Antrags auf Leistung X“. | Prozessmanagement ist auf systematische Identifikation und Dokumentation ausgerichtet. ([bva.bund.de](https://www.bva.bund.de/SharedDocs/Downloads/DE/Behoerden/Beratung/Prozessmanagement/Leitfaeden/Kurzleitfaden_GPM.pdf?__blob=publicationFile&v=1&utm_source=chatgpt.com)) |
| **2. Auslöser bestimmen** | Was startet den Prozess wirklich? | Antragseingang, Fristablauf, Registermeldung, Widerspruch. | BPMN-Ereignisse bilden Auslöser ab. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **3. Ergebnis bestimmen** | Wann ist der Prozess fachlich beendet? | Bescheid versandt und Vorgang abgelegt. | Endereignisse markieren Prozessabschluss. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **4. Beteiligte erfassen** | Wer ist beteiligt, intern und extern? | Antragsteller, Behörde, Register, DMS, Versanddienst. | Pools und Lanes modellieren Beteiligte und Verantwortlichkeiten. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **5. Tätigkeiten sammeln** | Welche Arbeitsschritte passieren tatsächlich? | Erfassen, prüfen, nachfordern, entscheiden, bescheiden, ablegen. | Aktivitäten bilden Arbeitsschritte ab. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **6. Entscheidungen identifizieren** | Wo verzweigt der Prozess? | Vollständig? Zuständig? Bewilligungsfähig? Widerspruch zulässig? | Gateways steuern Prozesspfade. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **7. Daten und Dokumente erfassen** | Welche Informationen entstehen, ändern sich oder werden verwendet? | Antrag, Nachweise, Registerdaten, Bescheid, Aktenmetadaten. | BPMN kann mit Datenobjekten und Datenspeichern arbeiten. ([medium.com](https://medium.com/nerd-for-tech/quick-start-to-camunda-and-bpmn-2-0-413310ab7630?utm_source=chatgpt.com)) |
| **8. Systeme erfassen** | Welche Anwendungen unterstützen den Prozess? | Portal, Fachverfahren, DMS/eAkte, Registerschnittstelle. | BPMN kann Prozessmodelle und Softwarekomponenten verbinden. ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN)) |
| **9. Ausnahmen erfassen** | Was passiert, wenn etwas nicht klappt? | Fristablauf, fehlende Unterlagen, Registerfehler, Rückläufer. | Ereignisse beeinflussen Prozesspfade. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **10. Zeiten erfassen** | Wo wird gewartet, wie lange, mit welcher Frist? | Nachforderung 14 Tage, Fachprüfung 5 Arbeitstage, Versandlaufzeit. | Timer sind in BPMN explizit modellierbar. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **11. Medienbrüche erfassen** | Wo werden Informationen manuell übertragen? | PDF in Fachverfahren abtippen, Excel-Liste, Papierakte. | Verwaltungsnahe BPMN-Fachschalen betonen Analyse und Optimierung. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **12. Schmerzpunkte priorisieren** | Welche Probleme sind fachlich, technisch oder organisatorisch relevant? | Lange Liegezeiten, unklare Zuständigkeit, doppelte Datenerfassung. | Prozessmanagement dient Analyse und Optimierung. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |

### 10.2 Konkrete Interviewfragen

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| **Start** | „Woran erkennen Sie, dass ein neuer Vorgang beginnt?“ | „Wenn ein Antrag im Portal eingeht oder ein Brief in der Poststelle landet.“ | Ereignisse starten Prozesse. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Eingangskanäle** | „Über welche Kanäle kommt der Antrag?“ | Portal, Post, E-Mail, Fachportal, andere Behörde. | Pools und Nachrichtenflüsse helfen, externe Kommunikation zu zeigen. ([omg.org](https://www.omg.org/bpmn/Documents/Introduction_to_BPMN.pdf?utm_source=chatgpt.com)) |
| **Verantwortung** | „Wer ist für den nächsten Schritt verantwortlich?“ | Eingangsstelle registriert, Sachbearbeitung prüft. | Lanes zeigen Verantwortlichkeiten. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Entscheidung** | „Nach welchen Kriterien entscheiden Sie hier?“ | Vollständigkeit, Zuständigkeit, Anspruch, Frist, Risikoklasse. | Gateways zeigen Pfade; Regeln sollten fachlich strukturiert werden. |
| **Ausnahmen** | „Was passiert, wenn etwas fehlt oder falsch ist?“ | Nachforderung, Rückfrage, Ablehnung, Eskalation. | Zwischenereignisse und Fehlerpfade machen Ausnahmen sichtbar. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Fristen** | „Wo warten Sie auf jemanden oder etwas?“ | Rückmeldung des Antragstellers, Registerantwort, Fachfreigabe. | Timer-Ereignisse bilden Wartezeiten ab. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Systeme** | „In welchem System wird dieser Schritt dokumentiert?“ | Fachverfahren, DMS, Excel, E-Mail-Postfach. | BPMN kann menschliche und technische Arbeit verbinden. ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN)) |
| **Daten** | „Welche Daten entstehen, werden geändert oder übernommen?“ | Personendaten, Vorgangsdaten, Nachweisdaten, Bescheiddaten. | Prozessmodelle können Datenobjekte und Artefakte ergänzen. ([medium.com](https://medium.com/nerd-for-tech/quick-start-to-camunda-and-bpmn-2-0-413310ab7630?utm_source=chatgpt.com)) |
| **Medienbruch** | „Wo schreiben Sie Daten aus einem System in ein anderes?“ | PDF-Antrag wird manuell ins Fachverfahren übertragen. | In Verwaltungsprozessen ist Analyse von Medienbrüchen zentral. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Kontrolle** | „Wer prüft, ob der Schritt korrekt war?“ | Vier-Augen-Prüfung, Fachaufsicht, Systemvalidierung. | BPMN macht Kontrollpunkte und Zuständigkeiten sichtbar. |
| **Ende** | „Wann ist der Vorgang wirklich abgeschlossen?“ | Bescheid versandt, Zustellung dokumentiert, Akte vollständig. | Endereignisse markieren Abschluss. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Verbesserung** | „Wenn Sie eine Sache ändern könnten, welche wäre das?“ | Weniger manuelle Datenerfassung, bessere Registerintegration. | Prozessmanagement dient Optimierung und Transparenz. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |

## 11. Modellierungsregeln für saubere Behörden-BPMN

### 11.1 Benennung

Tasks formulierst du immer als **Verb + Objekt**. Nicht „Prüfung“, sondern „Antrag prüfen“. Nicht „Bescheid“, sondern „Bescheid erstellen“. Nicht „DMS“, sondern „Dokument in eAkte ablegen“. Dadurch wird klar, was getan wird.

Gateways formulierst du als Frage. Nicht „Vollständigkeit“, sondern „Antrag vollständig?“. Die ausgehenden Pfade heißen dann „ja“ und „nein“ oder fachlich präziser „vollständig“ und „unvollständig“.

Ereignisse formulierst du als Zustand oder Ereignis. Nicht „Antrag prüfen“, sondern „Antrag eingegangen“. Nicht „Frist prüfen“, sondern „Frist abgelaufen“.

### 11.2 Detaillierungsgrad

Ein Modell sollte genau so detailliert sein, dass sein Zweck erfüllt wird. Für ein Executive-Gremium brauchst du keine 80 Elemente. Für eine Fachbereichsabstimmung brauchst du Rollen, Entscheidungen, Dokumente und Ausnahmen. Für technische Automation brauchst du zusätzlich technische Ereignisse, Service-Tasks, Datenobjekte, Fehlerpfade und Zustandsübergänge.

Die Prozessplattform Sachsen beschreibt BPMN 2.0 als leistungsfähige, etablierte Methode zur Dokumentation und Visualisierung von Geschäftsprozessen und verweist darauf, dass verwaltungsnahe Fachschalen wie PICTURE-BPMN BPMN gezielt reduzieren, damit fachliche Dokumentation, Analyse und Optimierung beherrschbar bleiben. Das ist für dich wichtig: In Behörden ist nicht maximale Symbolfülle professionell, sondern passende Symbolauswahl. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf))

### 11.3 Sequenzfluss und Nachrichtenfluss

Innerhalb eines Behördenpools verwendest du Sequenzflüsse. Zwischen Behörde und Antragsteller, Register, DMS als externem System oder Versanddienst verwendest du Nachrichtenflüsse. Diese Unterscheidung ist nicht akademisch. Sie zeigt, ob die Behörde den nächsten Schritt selbst steuert oder auf einen externen Beteiligten wartet. Die BPMN-Einführung der OMG stellt klar, dass Sequence Flow Lanes innerhalb eines Pools überqueren kann, während Message Flow nicht für Flow Objects innerhalb derselben Pool-Lanes verwendet wird. ([omg.org](https://www.omg.org/bpmn/Documents/Introduction_to_BPMN.pdf?utm_source=chatgpt.com))

Praktische Übersetzung: Wenn Sachbearbeitung an Fachprüfung übergibt, ist das meist Sequenzfluss innerhalb der Behörde. Wenn die Behörde eine Nachforderung an den Antragsteller sendet, ist das Nachrichtenfluss. Wenn die Behörde auf Registerantwort wartet, ist das ebenfalls Kommunikation zwischen Beteiligten.

## 12. BPMN-Spickzettel für dich als Enterprise Architekt

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| **Start Event** | Prozessauslöser. | „Antrag eingegangen“. | ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Message Start Event** | Prozess startet durch empfangene Nachricht. | Antrag trifft über Portal ein. | ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Timer Start Event** | Prozess startet zu einem Zeitpunkt oder Rhythmus. | Monatliche Prüfliste erzeugen. | ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Task** | Einzelne Tätigkeit. | „Antrag erfassen“. | ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **User Task** | Mensch arbeitet mit System. | Sachbearbeiter prüft im Fachverfahren. | ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN)) |
| **Manual Task** | Menschliche Tätigkeit ohne Systemsteuerung. | Papierpost öffnen. | ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Service Task** | Automatisierter Systemschritt. | Registerdaten abrufen. | ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN)) |
| **Business Rule Task** | Fachregel oder Entscheidung wird angewendet. | Anspruchskriterien prüfen. | |
| **XOR Gateway** | Genau ein Pfad. | Vollständig: ja/nein. | ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **AND Gateway** | Parallele Pfade. | Registerabfrage und Fachprüfung parallel. | ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Event-based Gateway** | Pfad hängt vom nächsten Ereignis ab. | Nachweise kommen oder Frist läuft ab. | ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Intermediate Message Event** | Nachricht während des Prozesses. | Nachweise eingegangen. | ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Intermediate Timer Event** | Wartezeit oder Frist. | 14 Tage warten. | ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Boundary Timer Event** | Frist hängt an laufender Aktivität. | Während „Nachweise anfordern“ läuft Frist ab. | ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Boundary Error Event** | Fehler an einer Aktivität. | Registerabfrage fehlgeschlagen. | ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Subprozess** | Detaillierter Teilprozess. | Fachprüfung durchführen. | |
| **Call Activity** | Wiederverwendbarer Prozess. | Standardprozess „Bescheid versenden“. | |
| **Data Object** | Dokument oder Datenobjekt im Prozess. | Antrag, Nachweis, Bescheid. | ([medium.com](https://medium.com/nerd-for-tech/quick-start-to-camunda-and-bpmn-2-0-413310ab7630?utm_source=chatgpt.com)) |
| **Data Store** | Persistenter Speicher. | Fachverfahren, eAkte, Register. | ([medium.com](https://medium.com/nerd-for-tech/quick-start-to-camunda-and-bpmn-2-0-413310ab7630?utm_source=chatgpt.com)) |
| **Annotation** | Erläuterung ohne Prozesslogik. | „Frist nach Fachvorgabe prüfen“. | |
| **Message Flow** | Kommunikation zwischen Pools. | Behörde sendet Nachforderung. | ([omg.org](https://www.omg.org/bpmn/Documents/Introduction_to_BPMN.pdf?utm_source=chatgpt.com)) |
| **Sequence Flow** | Ablauf innerhalb eines Pools. | Vorprüfung → Fachprüfung. | ([omg.org](https://www.omg.org/bpmn/Documents/Introduction_to_BPMN.pdf?utm_source=chatgpt.com)) |

## 13. Typische Fehler und direkte Korrektur

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| **Fehler: Alles in einen Pool werfen** | Externe Beteiligte und interne Rollen werden vermischt. Dadurch ist nicht sichtbar, wer wirklich steuert und wer nur kommuniziert. | Antragsteller als Lane innerhalb der Behörde. | Pools und Lanes trennen Beteiligte und Verantwortlichkeiten. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Korrektur** | Antragsteller, Behörde, Register und Versanddienst als eigene Pools modellieren. | Message Flow zwischen Antragsteller und Behörde. | ([omg.org](https://www.omg.org/bpmn/Documents/Introduction_to_BPMN.pdf?utm_source=chatgpt.com)) |
| **Fehler: Nachrichtenfluss innerhalb einer Behörde** | Message Flow wird als normaler Pfeil zwischen Lanes missbraucht. | Sachbearbeitung → Fachprüfung als Message Flow. | Sequence Flow kann Lanes innerhalb eines Pools überschreiten; Message Flow gehört nicht zwischen Flow Objects derselben Pool-Lanes. ([omg.org](https://www.omg.org/bpmn/Documents/Introduction_to_BPMN.pdf?utm_source=chatgpt.com)) |
| **Korrektur** | Innerhalb der Behörde Sequenzfluss nutzen; externe Kommunikation als Message Flow. | Sachbearbeitung → Fachprüfung = Sequence Flow. | ([omg.org](https://www.omg.org/bpmn/Documents/Introduction_to_BPMN.pdf?utm_source=chatgpt.com)) |
| **Fehler: Gateways ohne Frage** | Niemand versteht, nach welchem Kriterium verzweigt wird. | Gateway „Prüfung“. | Gateways modellieren Bedingungen. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Korrektur** | Gateway als konkrete Frage benennen. | „Antrag vollständig?“ | |
| **Fehler: Entscheidungen im Task verstecken** | Fachregeln verschwinden in einer Aktivität und sind später nicht prüfbar. | Task „Antrag bearbeiten“ enthält Vollständigkeit, Anspruch, Risiko und Fristprüfung. | BPMN modelliert Ablauf; detaillierte Regelwerke sollten separat strukturiert werden. |
| **Korrektur** | Entscheidungspunkte explizit modellieren und komplexe Regeln in DMN oder Regelkatalog auslagern. | Gateway „bewilligungsfähig?“ plus Entscheidungstabelle. | |
| **Fehler: Keine Ausnahmen modellieren** | Das Modell zeigt nur den Idealfall. Behördenrealität besteht aber oft aus Rückfragen, Fristen, Fehlern und Sonderfällen. | Kein Pfad für fehlende Nachweise. | Ereignisse beeinflussen Prozessverlauf und können Aufgaben unterbrechen. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Korrektur** | Timer, Message Events, Error Events und Eskalationen ergänzen. | Nachweise eingegangen oder Frist abgelaufen. | ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Fehler: Systeme als Menschen modellieren** | Ein System wird wie eine Organisationseinheit behandelt, obwohl es nur eine technische Komponente ist. | Lane „DMS entscheidet“. | BPMN sollte Verantwortlichkeit und Systemverhalten sauber unterscheiden. |
| **Korrektur** | Systemschritte als Service Tasks oder eigene technische Pools modellieren. | „Dokument in DMS ablegen“. | ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN)) |
| **Fehler: Zu viel Symbolik** | Das Modell wird korrekt, aber unlesbar. | 40 Spezialereignisse in einem Fachbereichsmodell. | Fachschalen wie PICTURE-BPMN reduzieren BPMN bewusst für Verwaltungsanalyse. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Korrektur** | Für Fachmodelle wenige, klare Symbole verwenden; technische Details in separater Sicht modellieren. | Fachsicht auf Seite 1, technische Sicht separat. | |
| **Fehler: Ende unklar** | Der Prozess endet mit „Bescheid erstellen“, obwohl Versand und Aktenablage fehlen. | End Event nach Dokumenterzeugung. | Endereignisse markieren den Abschluss des Prozesspfads. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Korrektur** | Fachliches Ende sauber definieren. | „Bescheid bekanntgegeben und Vorgang abgelegt“. | |

## 14. Vom Prozessmodell zur Architekturentscheidung

Das ist der Teil, der dich als Enterprise Architekt sichtbar stärker macht. Du modellierst BPMN nicht, um BPMN zu besitzen. Du modellierst, um Architekturentscheidungen belastbar herzuleiten.

| Aspekt | Details/Erklärung | Beispiel | Architekturentscheidung |
|---|---|---|---|
| **Medienbruch** | Daten werden manuell übertragen. | PDF-Antrag wird ins Fachverfahren abgetippt. | Portal-Fachverfahren-Integration, strukturierte Formulardaten, OpenAPI-Schnittstelle. |
| **Unklare führende Datenquelle** | Mehrere Systeme halten denselben Status. | Status in Excel und Fachverfahren unterschiedlich. | Führendes System für Vorgangsstatus festlegen. |
| **Lange Wartezeit** | Prozess hängt an externer Antwort. | Registerantwort dauert unplanbar. | SLO für Registerschnittstelle, Retry-Konzept, Monitoring, Ersatzverfahren. |
| **Viele Rückfragen** | Eingaben sind unvollständig. | Nachweise fehlen häufig. | Formularvalidierung, Vorabprüfung, Pflichtfeldlogik, Dokumentencheckliste. |
| **Unklare Rolle** | Entscheidung wird informell getroffen. | Fachprüfung und Entscheidungsfreigabe in derselben Rolle. | Rollenmodell, Vier-Augen-Prinzip, IAM-Berechtigungsstruktur. |
| **Manuelle Aktenablage** | Dokumente werden spät oder uneinheitlich abgelegt. | Bescheid wird lokal gespeichert und später hochgeladen. | DMS/eAkte-Integration, automatische Ablage, Metadatenstandard. |
| **Fehlerpfad fehlt** | Technische Fehler sind nicht fachlich geregelt. | Register nicht erreichbar. | Fallback-Prozess, Incident-Prozess, Fehlercodes, Wiederanlaufkonzept. |
| **Widerspruch als Rückpfeil** | Rechtsbehelf wird nicht als eigener Prozess verstanden. | Widerspruch geht zurück in Antragsprozess. | Eigener Rechtsbehelfsprozess, Aktenbezug, Statusmodell, Fristenmodell. |
| **Viele Sonderfälle** | Prozessmodell wird durch Fachlogik überladen. | Anspruchsprüfung mit vielen Kriterien. | DMN-Entscheidungsmodell statt Gateway-Kaskade. |
| **Keine Betriebsdaten** | Prozess ist nicht steuerbar. | Niemand sieht, wo Vorgänge hängen. | Observability, Prozesskennzahlen, Dashboard, Durchlaufzeitmessung. |

## 15. Vorgehensmodell: So setzt du BPMN im Behördenprojekt real um

### Phase 1: Auftrag klären

Du beginnst mit drei Fragen: **Wofür modellieren wir? Wer nutzt das Modell? Welche Entscheidung soll danach möglich sein?** Wenn die Antwort nur lautet „Wir brauchen Prozessdoku“, ist das zu schwach. Besser ist: „Wir modellieren den Ist-Prozess, um Medienbrüche, Rollenunklarheiten und Integrationsbedarfe für die Zielarchitektur sichtbar zu machen.“

Ergebnis dieser Phase ist ein kurzer Modellierungsauftrag: Prozessname, Scope, Nicht-Scope, Beteiligte, Zielgruppe, Detaillierungsgrad, Notationsumfang, Qualitätskriterien.

### Phase 2: Ist-Prozess erheben

Du führst Interviews mit Eingangsstelle, Sachbearbeitung, Fachprüfung, IT-Betrieb, DMS-/Fachverfahrensverantwortlichen und ggf. Datenschutz, Informationssicherheit und Rechtsbereich. Du fragst nicht abstrakt „Wie läuft der Prozess?“, sondern lässt dir einen echten Vorgang erzählen: „Nehmen wir den letzten normalen Antrag. Was passierte zuerst? Was danach? Wo warteten Sie? Wer hatte den Vorgang? Welches System war offen?“

Ergebnis dieser Phase ist ein Rohmodell mit Hauptpfad, Ausnahmefällen, offenen Fragen und Schmerzpunkten.

### Phase 3: Modell validieren

Du legst das Modell dem Fachbereich vor und gehst Schritt für Schritt durch: „Ist das wirklich die Reihenfolge? Wer macht das? Was passiert, wenn die Unterlagen fehlen? Wann gilt der Vorgang als abgeschlossen?“ Ein BPMN-Modell ist erst dann gut, wenn die Fachseite sagt: „Ja, so arbeiten wir tatsächlich.“ Nicht: „So sollte es eigentlich sein.“

Ergebnis dieser Phase ist ein validierter Ist-Prozess mit markierten Medienbrüchen, Wartezeiten, Systemen, Datenobjekten und Verantwortlichkeiten.

### Phase 4: Soll-Prozess strukturieren

Jetzt trennst du Verbesserungsideen sauber: Was kann organisatorisch verbessert werden? Was braucht IT-Integration? Was braucht Datenklärung? Was braucht IAM? Was braucht DMS/eAkte? Was braucht Regelmodellierung? Was braucht Betriebsfähigkeit?

Ergebnis dieser Phase ist ein Soll-Prozess mit Zielprinzipien: digitale Eingangsdaten, klare Zuständigkeit, minimierte manuelle Übertragung, automatisierte Ablage, nachvollziehbare Entscheidung, messbare Durchlaufzeit.

### Phase 5: Architekturentscheidungen ableiten

Aus dem Soll-Prozess entstehen Architekturartefakte: Schnittstellenvertrag, Datenlandkarte, Rollenmodell, ADR, Zielarchitekturbaustein, DMS-Konzept, IAM-Anforderung, Observability-Anforderung, Betriebsanforderung, Migrationspfad.

Ergebnis dieser Phase ist kein „BPMN-Bild“, sondern ein entscheidungsfähiges Architekturpaket.

## 16. Qualitätskriterien für dein BPMN-Modell

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| **Lesbarkeit** | Fachbereich kann den Prozess ohne Symbolschulung grob erklären. | Hauptpfad passt auf eine Seite. | BPMN soll von Stakeholdern genutzt werden können. ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN)) |
| **Eindeutiger Start** | Der Auslöser ist sichtbar. | „Antrag eingegangen“. | Ereignisse kennzeichnen Prozessbeginn. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Eindeutiges Ende** | Der fachliche Abschluss ist sichtbar. | „Bescheid bekanntgegeben und Akte vollständig“. | BPMN unterscheidet Endereignisse. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Verantwortlichkeit** | Jede menschliche Tätigkeit liegt in einer passenden Lane. | Sachbearbeitung prüft, Fachprüfung bewertet. | Pools und Lanes zeigen Verantwortlichkeiten. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Saubere Flüsse** | Sequence Flow innerhalb, Message Flow zwischen Pools. | Behörde sendet Bescheid per Message Flow. | ([omg.org](https://www.omg.org/bpmn/Documents/Introduction_to_BPMN.pdf?utm_source=chatgpt.com)) |
| **Explizite Entscheidungen** | Gateways haben klare Fragen und benannte Pfade. | „Antrag vollständig?“ Ja/Nein. | Gateways steuern Bedingungen. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Ausnahmen sichtbar** | Nicht nur Schönwetterprozess modellieren. | Fristablauf, Registerfehler, Widerspruch. | Ereignisse beeinflussen Prozesspfade. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Daten sichtbar** | Relevante Dokumente und Datenobjekte sind erkennbar. | Antrag, Nachweis, Bescheid, Registerauskunft. | BPMN kann Datenobjekte ergänzen. ([medium.com](https://medium.com/nerd-for-tech/quick-start-to-camunda-and-bpmn-2-0-413310ab7630?utm_source=chatgpt.com)) |
| **Systeme sichtbar** | Fachverfahren, DMS, Register, Portal erscheinen dort, wo sie prozessrelevant sind. | Service Task „Vorgang anlegen“. | BPMN kann softwarebezogene Prozesskomponenten adressieren. ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN)) |
| **Architekturfähigkeit** | Aus dem Modell lassen sich Anforderungen und Entscheidungen ableiten. | Medienbruch → Schnittstellenbedarf. | Prozessmanagement dient Analyse und Optimierung. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |

## 17. Mini-Methode: Vom Interview zur BPMN in 90 Minuten

Du kannst in Workshops sehr pragmatisch arbeiten. Starte mit dem **Happy Path**: Antrag kommt rein, wird geprüft, entschieden, beschieden, abgelegt. Danach ergänzt du drei Dinge: **Ausnahmen**, **Wartezeiten**, **Systeme**. Zum Schluss ergänzt du **Datenobjekte** und **Verantwortlichkeiten**.

Die Reihenfolge lautet: zuerst Ereignisse und Tasks, dann Rollen, dann Gateways, dann Nachrichten, dann Timer, dann Daten, dann Systeme, dann Fehlerpfade. Dadurch verhinderst du, dass du dich zu früh in technischen Details verlierst.

Ein guter Workshop-Satz lautet: „Wir zeichnen nicht, wie es im Handbuch stehen sollte. Wir zeichnen, wie der Vorgang tatsächlich durch die Organisation läuft.“

## 18. Übung: Modelliere einen Verwaltungsprozess

### Aufgabe

Modelliere den Prozess „Bearbeitung eines Antrags auf Leistung X“ als BPMN-Fachmodell. Verwende mindestens drei Pools: Antragsteller, Bundesbehörde, Registersystem. Verwende in der Bundesbehörde mindestens fünf Lanes: Eingangsstelle, Sachbearbeitung, Fachprüfung, Entscheidungsstelle, DMS/eAkte. Ergänze mindestens einen Timer, eine Nachforderung, eine Registerabfrage, eine Entscheidung, einen Bescheidversand und eine Aktenablage.

### Mindestumfang

Dein Modell muss folgende Elemente enthalten: Message Start Event „Antrag eingegangen“, Task „Antrag erfassen“, Task „Vorgang anlegen“, XOR Gateway „Antrag vollständig?“, Send Task „Nachforderung versenden“, Event-based Gateway „Nachweise eingegangen oder Frist abgelaufen?“, Timer Intermediate Event „Frist abgelaufen“, Subprozess „Fachprüfung durchführen“, Message Flow zur Registerabfrage, XOR Gateway „Bewilligungsfähig?“, Task „Bescheid erstellen“, Send Task „Bescheid versenden“, Service Task „Dokumente in eAkte ablegen“, End Event „Vorgang abgeschlossen“.

### Zusatzaufgabe für Enterprise-Architecture-Niveau

Leite aus deinem Modell mindestens zehn Architekturanforderungen ab. Beispiele: strukturierte Antragserfassung, Fachverfahren-API, DMS-Ablagevertrag, Registerschnittstelle, IAM-Rollenmodell, Audit-Logging, Fristenmonitoring, Wiedervorlagen, Fehlerbehandlung bei Registerausfall, Statusmodell, Bescheidtemplate-Service, Versandnachweis, Prozesskennzahlen.

### Bewertung deiner Lösung

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| **Fachliche Vollständigkeit** | Hauptpfad, Nachforderung, Fachprüfung, Entscheidung, Bescheid, Akte und Widerspruch sind berücksichtigt. | Widerspruch als eigener Start oder Subprozess. | BPMN unterstützt verschiedene Ereignisse und Prozesspfade. ([camunda.com](https://camunda.com/bpmn/reference/)) |
| **Notationsdisziplin** | Pools, Lanes, Sequenz- und Nachrichtenflüsse sind sauber getrennt. | Message Flow nur zwischen Antragsteller und Behörde. | ([omg.org](https://www.omg.org/bpmn/Documents/Introduction_to_BPMN.pdf?utm_source=chatgpt.com)) |
| **Verwaltungstauglichkeit** | Fristen, Nachweise, Aktenablage und manuelle Tätigkeiten sind sichtbar. | Timer „Frist abgelaufen“. | PICTURE-BPMN reduziert BPMN gezielt für verwaltungsnahe Analyse. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Architekturwert** | Aus dem Modell entstehen konkrete Anforderungen. | Medienbruch wird API-Anforderung. | Prozessmanagement unterstützt Analyse und Optimierung. ([prozessplattform.sachsen.de](https://www.prozessplattform.sachsen.de/download/HandbuchProzessmanagementAuflage5.pdf)) |
| **Lesbarkeit** | Das Modell ist für Fachbereich und IT gemeinsam diskutierbar. | Hauptmodell maximal eine Seite, Details in Subprozessen. | BPMN soll Stakeholder und technische Umsetzung verbinden. ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN)) |

## 19. Executive-Formulierungen für Gremien

„Das Prozessmodell zeigt nicht nur den Ablauf der Antragsbearbeitung, sondern die entscheidenden Steuerungspunkte: Eingangskanäle, Vollständigkeitsprüfung, Nachforderung, Fristbehandlung, Fachprüfung, Entscheidung, Bescheidung, Versand und Aktenablage.“

„Die wesentlichen Risiken liegen nicht im einzelnen Bearbeitungsschritt, sondern an den Übergängen: Medienbrüche, unklare Zuständigkeiten, Wartezeiten auf Rückmeldungen, manuelle Datenübernahme und fehlende Transparenz über den Vorgangsstatus.“

„Aus dem Ist-Prozess ergeben sich klare Architekturthemen: ein führendes Fachverfahren für den Vorgangsstatus, standardisierte Schnittstellen zum Portal und zum Register, eine verbindliche DMS-/eAkte-Ablage, ein Rollen- und Berechtigungskonzept sowie messbare Betriebs- und Durchlaufzeitkennzahlen.“

„BPMN dient hier nicht der Dokumentation um der Dokumentation willen. Das Modell ist die Grundlage, um Fachlichkeit, Organisation, IT, Security, Betrieb und Dienstleistersteuerung auf ein gemeinsames Zielbild auszurichten.“

„Für die Zielarchitektur empfehlen wir, die Prozesssicht mit Datenlandkarte, Schnittstellenverträgen, IAM-Rollenmodell, DMS-Konzept, Observability-Anforderungen und Architecture Decision Records zu verbinden.“

## 20. Deine persönliche Arbeitsformel

Wenn du einen Behördenprozess modellierst, gehst du immer in dieser Reihenfolge vor:

**Auslöser klären. Ergebnis klären. Beteiligte klären. Hauptpfad aufnehmen. Entscheidungen sichtbar machen. Ausnahmen ergänzen. Wartezeiten modellieren. Medienbrüche markieren. Systeme und Datenobjekte ergänzen. Modell validieren. Soll-Prozess ableiten. Architekturentscheidungen formulieren.**

Das ist die professionelle Linie. Nicht Symbolwissen macht dich stark, sondern die Fähigkeit, aus Prozesswirklichkeit belastbare Architekturentscheidungen zu gewinnen. BPMN ist dabei dein Vergrößerungsglas: Es zeigt, wo Organisation, Fachlichkeit, Daten, Systeme, Sicherheit, Betrieb und Verantwortung tatsächlich aufeinandertreffen.

<>