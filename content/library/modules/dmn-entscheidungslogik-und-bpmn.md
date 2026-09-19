## Checkliste: Was du bei DMN sofort erkennen und beherrschen musst

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| 1. Prozesslogik trennen | BPMN beschreibt den Ablauf; DMN beschreibt die fachliche Entscheidung innerhalb oder neben diesem Ablauf. | „Antrag prüfen“ ist BPMN; „Ist der Antrag zulässig?“ ist DMN. | OMG beschreibt DMN ausdrücklich als Standard für Geschäftsentscheidungen und Fachregeln sowie als Ergänzung zu BPMN. ([omg.org](https://www.omg.org/dmn/)) |
| 2. Entscheidung identifizieren | Eine DMN-Entscheidung beantwortet eine fachliche Frage mit einem Ergebnis. | „Welche Nachweise sind erforderlich?“ | DMN soll fachliche Entscheidungsmodelle für Fachseite, Analysten und technische Umsetzung verständlich machen. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| 3. Eingabedaten bestimmen | Jede Entscheidung braucht klar benannte Daten. | Alter, Wohnsitz, Fristdatum, Nachweisstatus, Registertreffer. | DMN arbeitet mit Entscheidungen, Eingabedaten, Wissensmodellen und Entscheidungstabellen. ([omg.org](https://www.omg.org/dmn/)) |
| 4. Fachregeln explizit machen | Regeln dürfen nicht nur in Code, Excel oder Einzelwissen existieren. | „Wenn Frist überschritten und keine Wiedereinsetzung, dann unzulässig.“ | DMN reduziert Umsetzungsrisiken durch grafische Zerlegung und eindeutige Entscheidungstabellen. ([omg.org](https://www.omg.org/dmn/)) |
| 5. Entscheidungstabellen korrekt lesen | Zeilen sind Regeln, Spalten sind Eingaben und Ausgaben. | Eingabe: Friststatus; Ausgabe: Zulässigkeit. | Hit Policies bestimmen, was passiert, wenn mehrere Regeln zutreffen. ([docs.drools.org](https://docs.drools.org/latest/drools-docs/drools/DMN/index.html?utm_source=chatgpt.com)) |
| 6. Hit Policy festlegen | Die Hit Policy ist kein Detail, sondern definiert die Auswertungslogik. | U = genau eine Regel darf treffen; C = mehrere Ergebnisse sammeln. | Camunda beschreibt die DMN-Hit-Policies U, A, P, F, C, O und R. ([docs.camunda.io](https://docs.camunda.io/docs/components/best-practices/modeling/choosing-the-dmn-hit-policy/?utm_source=chatgpt.com)) |
| 7. Wissensquellen dokumentieren | Regeln brauchen Herkunft und Nachvollziehbarkeit. | Gesetz, Verwaltungsvorschrift, Dienstanweisung, Fachkonzept, Gremienentscheidung. | DMN schafft eine Brücke zwischen fachlichem Entscheidungsdesign und technischer Implementierung. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| 8. Abhängige Entscheidungen modellieren | Komplexe Logik wird in mehrere kleine Entscheidungen zerlegt. | „Fristlage“ beeinflusst „Zulässigkeit“, diese beeinflusst „Prüfungspfad“. | OMG nennt die grafische Zerlegung komplexer Entscheidungsanforderungen als Nutzen von DMN. ([omg.org](https://www.omg.org/dmn/)) |
| 9. BPMN sauber koppeln | BPMN ruft DMN an genau den Stellen auf, an denen fachliche Entscheidung erforderlich ist. | Business-Rule-Task „Zulässigkeit prüfen“. | BPMN soll Prozesse für Fach- und Technikbeteiligte verständlich und zugleich präzise modellieren. ([omg.org](https://www.omg.org/bpmn/)) |
| 10. Regeln testbar machen | Jede Regel braucht Testfälle, Grenzfälle und Negativfälle. | Antrag am letzten Tag, fehlender Nachweis, widersprüchliche Registerdaten. | Forschung zu DMN betont Analyseaufgaben wie Erkennung überlappender und fehlender Regeln. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |
| 11. Governance einbauen | Regeln brauchen Owner, Version, Änderungsweg und Abnahme. | Fachregel ändert sich durch neue Verwaltungsvorschrift. | DMN ist für Fachanwender, Analysten und technische Entwickler gleichermaßen gedacht. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| 12. Architekturwert erkennen | DMN ist nicht nur Modellierung, sondern Facharchitektur: Es macht Entscheidungswissen steuerbar. | Ablöseprojekt: Regeln werden aus Legacy-Code extrahiert und fachlich bestätigt. | DMN unterstützt eine wiederverwendbare Bibliothek von Entscheidungsbausteinen. ([omg.org](https://www.omg.org/dmn/)) |

## 1. Grundverständnis: Was DMN eigentlich leistet

DMN steht für *Decision Model and Notation*. Es ist eine standardisierte Modellierungssprache, um fachliche Entscheidungen und Fachregeln präzise zu beschreiben. Der entscheidende Punkt ist: DMN modelliert nicht primär, wie Menschen oder Systeme durch einen Prozess laufen, sondern nach welchen fachlichen Kriterien ein Ergebnis ermittelt wird. Die OMG beschreibt DMN als Sprache zur präzisen Spezifikation von Geschäftsentscheidungen und Geschäftsregeln; außerdem ist DMN so angelegt, dass es zusammen mit BPMN genutzt werden kann. ([omg.org](https://www.omg.org/dmn/))

Für dich als Enterprise Architekt im Behördenkontext ist DMN besonders wertvoll, weil Behördenprozesse häufig regelintensiv sind: Zulässigkeit, Zuständigkeit, Anspruchsprüfung, Nachweispflichten, Fristen, Priorisierung, Risikoklassifikation, Eskalation, Statuswechsel und Prüftiefe hängen oft von klaren, aber verteilten Regeln ab. Diese Regeln stecken in Gesetzen, Verwaltungsvorschriften, Fachkonzepten, Dienstanweisungen, Excel-Dateien, historisch gewachsenem Code, Sachbearbeiterwissen oder Schnittstellenlogik. DMN zwingt dich, diese Entscheidungslogik sichtbar, prüfbar und diskutierbar zu machen.

Ein sauberer Satz lautet: BPMN beantwortet „Was passiert wann und durch wen?“, DMN beantwortet „Welche fachliche Entscheidung wird aus welchen Eingaben nach welchen Regeln getroffen?“ Genau diese Trennung ist professionell. Wenn du sie nicht machst, entstehen Prozessmodelle voller verschachtelter Gateways, technische Systeme voller schwer auffindbarer Regelverzweigungen und Fachbereiche, die ihre eigene Entscheidungslogik nicht mehr vollständig erklären können.

## 2. Prozesslogik versus Entscheidungslogik

Prozesslogik beschreibt Reihenfolge, Zuständigkeit, Übergaben, Wartezustände, Ereignisse, Aufgaben, Eskalationen und Systeminteraktionen. Entscheidungslogik beschreibt Kriterien, Schwellenwerte, Kombinationen, Klassifikationen und fachliche Ableitungen. BPMN ist daher die Sprache des Ablaufs; DMN ist die Sprache der fachlichen Regelentscheidung. BPMN ist laut OMG ein Standard für grafische Prozessnotation, der für Fachbeteiligte verständlich und zugleich präzise genug für technische Umsetzung sein soll. ([omg.org](https://www.omg.org/bpmn/))

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Prozesslogik | Beschreibt den Ablauf: Start, Aufgaben, Rollen, Ereignisse, Gateways, Nachrichten, Ende. | Antrag erfassen → Unterlagen prüfen → Entscheidung vorbereiten → Bescheid erstellen. | BPMN ist laut OMG eine grafische Notation für Geschäftsprozessdiagramme. ([omg.org](https://www.omg.org/bpmn/)) |
| Entscheidungslogik | Beschreibt fachliche Ableitungen aus Eingabedaten und Regeln. | Wenn Antrag fristgerecht, zuständig und vollständig ist, dann formell zulässig. | DMN spezifiziert Geschäftsentscheidungen und Fachregeln. ([omg.org](https://www.omg.org/dmn/)) |
| Typische BPMN-Frage | Wer macht was, wann, mit welchem Ergebnis und welcher Übergabe? | Sachbearbeitung fordert Nachweis nach. | BPMN ist auf Prozessverständnis und Prozesskommunikation ausgelegt. ([omg.org](https://www.omg.org/bpmn/)) |
| Typische DMN-Frage | Welches Ergebnis ergibt sich aus welchen fachlichen Bedingungen? | Welche Nachweise sind aufgrund Antragstyp und Risikoklasse erforderlich? | DMN soll für Fachseite, Analysten und technische Umsetzung gleichermaßen lesbar sein. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| Fehlerhafte Vermischung | Entscheidungsregeln werden als BPMN-Gateway-Kaskaden modelliert. | 17 Gateways prüfen Alter, Frist, Wohnsitz, Nachweise und Risiko. | DMN und BPMN wurden laut OMG komplementär entworfen. ([omg.org](https://www.omg.org/dmn/)) |
| Gute Trennung | BPMN enthält eine Aufgabe „Zulässigkeit prüfen“; DMN beschreibt die konkrete Entscheidung. | BPMN-Business-Rule-Task ruft DMN-Tabelle auf. | DMN ist für Entscheidungslogik neben BPMN vorgesehen. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |

Der wichtigste Architekturfehler ist, eine Entscheidung als Prozessverzweigung zu behandeln. Ein Gateway in BPMN ist kein guter Ort für komplexe Fachregeln. Ein Gateway darf sagen: „Wenn Entscheidung = zulässig, dann weiter zur Sachprüfung; wenn Entscheidung = unzulässig, dann Ablehnungsbescheid vorbereiten.“ Die fachliche Herleitung dieser Entscheidung gehört aber in DMN.

## 3. Warum Fachregeln nicht in Code, Excel oder Einzelwissen verschwinden dürfen

Fachregeln sind Steuerungswissen der Organisation. Wenn sie unkontrolliert in Code, Excel-Dateien, lokalen Checklisten oder Kopfmonopolen einzelner Experten verschwinden, verliert die Behörde Transparenz, Änderbarkeit und Nachweisfähigkeit. Das ist nicht nur ein technisches Problem, sondern ein Architekturproblem.

In Code versteckte Regeln sind schwer fachlich zu prüfen. Excel-Regeln werden häufig kopiert, lokal verändert und ohne Versionierung weitergenutzt. Einzelwissen ist riskant, weil es bei Krankheit, Fluktuation oder Dienstleisterwechsel verschwindet. Aus Architekturperspektive ist das besonders kritisch, weil Entscheidungslogik dann nicht mehr eindeutig einer Quelle, einem Owner, einer Version und einem Prozessschritt zugeordnet werden kann.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Code-Versteck | Fachregeln werden als `if/else`, SQL-Filter oder Mappinglogik implementiert. | `if applicant.age < 18 && missingConsent then reject`. | DMN will eine standardisierte Brücke zwischen Fachentscheidung und Implementierung schaffen. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| Excel-Wildwuchs | Tabellen werden lokal angepasst, ohne zentrale Freigabe. | „Prüfliste_final_v7_neu_wirklich.xlsx“. | DMN unterstützt eindeutige Entscheidungstabellen und reduzierte Automatisierungsrisiken. ([omg.org](https://www.omg.org/dmn/)) |
| Einzelwissen | Nur erfahrene Sachbearbeitung kennt Sonderfälle. | „Bei Fallgruppe C machen wir das immer anders.“ | DMN soll Diskussion und Einigung über Umfang und Art der Entscheidungslogik unterstützen. ([omg.org](https://www.omg.org/dmn/)) |
| Dienstleisterabhängigkeit | Regeln liegen im Customizing oder Quellcode des Dienstleisters. | Änderung nur über Change Request mit langer Laufzeit. | DMN ist für Fachseite, Analysten und technische Entwickler verständlich angelegt. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| Testproblem | Ohne explizite Regeln fehlen systematische Testfälle. | Grenzfälle werden erst im Betrieb entdeckt. | Analyse von DMN-Tabellen umfasst unter anderem fehlende und überlappende Regeln. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |
| Revisionsproblem | Niemand kann später erklären, warum ein bestimmter Entscheidungspfad genommen wurde. | Widerspruchsfall: Entscheidungsgrundlage unklar. | DMN zielt auf klare, unzweideutige Entscheidungstabellen. ([omg.org](https://www.omg.org/dmn/)) |

Dein Ziel als Architekt ist nicht, jeden Fachparagraphen selbst auszulegen. Dein Ziel ist, Entscheidungslogik so zu strukturieren, dass Fachseite, IT, Security, Betrieb, Test und Dienstleister dieselbe fachliche Landkarte sehen. Genau hier wird DMN zur Architekturkommunikation.

## 4. Die wichtigsten DMN-Bausteine

DMN besteht aus zwei Ebenen: Erstens modellierst du, welche Entscheidungen voneinander abhängen. Das geschieht im *Decision Requirements Diagram*, kurz DRD. Zweitens modellierst du, wie eine konkrete Entscheidung berechnet oder bestimmt wird. Das geschieht häufig mit Entscheidungstabellen, kann aber auch über andere sogenannte Boxed Expressions erfolgen.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Decision | Eine fachliche Entscheidung mit klarer Entscheidungsfrage und Ergebnis. | „Ist der Antrag formell zulässig?“ | DMN modelliert Geschäftsentscheidungen und Fachregeln. ([omg.org](https://www.omg.org/dmn/)) |
| Input Data | Daten, die für Entscheidungen benötigt werden. | Antragseingang, Fristdatum, Antragstyp, Wohnsitz, Nachweisstatus. | DMN nutzt Eingaben als Grundlage für Entscheidungslogik. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Business Knowledge Model | Wiederverwendbare fachliche Berechnungs- oder Regelkomponente. | „Berechne Friststatus“, „ermittle Risikopunkte“. | DMN unterstützt wiederverwendbare Entscheidungsbausteine. ([omg.org](https://www.omg.org/dmn/)) |
| Knowledge Source | Herkunft oder Autorität einer Regel. | Gesetz, Verwaltungsvorschrift, Fachkonzept, Gremienbeschluss. | DMN soll Entscheidungswissen verständlich und nachvollziehbar machen. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| Decision Table | Tabellarische Darstellung von Eingaben, Bedingungen und Ergebnissen. | Wenn Friststatus = überschritten und Ausnahme = nein, dann unzulässig. | Entscheidungstabellen enthalten Hit Policy, Eingaben und Ausgaben. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Hit Policy | Regel, wie mehrere passende Tabellenzeilen interpretiert werden. | Unique, First, Collect. | Hit Policies bestimmen das Ergebnis bei mehreren passenden Regeln. ([docs.drools.org](https://docs.drools.org/latest/drools-docs/drools/DMN/index.html?utm_source=chatgpt.com)) |
| FEEL | Ausdruckssprache für Bedingungen und Werte in DMN. | `date("2026-06-13")`, `[1..10]`, `not("unvollständig")`. | FEEL wird für Bedingungen in Entscheidungstabellen verwendet. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Decision Service | Technisch oder fachlich abgrenzbarer Entscheidungsdienst. | „Eligibility Decision Service“. | DMN kann als Grundlage für ausführbare Entscheidungsservices dienen. ([omg.org](https://www.omg.org/dmn/)) |

Für den Behördenkontext solltest du DMN zunächst fachlich nutzen, nicht sofort technisch überladen. Das erste Ziel ist Verständlichkeit und Prüfbarkeit. Ausführbarkeit ist wertvoll, aber erst der zweite Schritt. Ein fachlich falsches, aber ausführbares DMN-Modell ist schlechter als eine saubere, fachlich geprüfte Entscheidungstabelle, die später technisch umgesetzt wird.

## 5. Behördenbeispiel: Antrag mit Nachweispflichten, Fristen, Statuswechseln und Risikoklassen

Wir nehmen ein bewusst generisches Verwaltungsbeispiel, damit die Methode übertragbar bleibt. Ein Bürger oder eine Organisation stellt einen Antrag auf eine behördliche Leistung. Der Antrag wird formal geprüft, fehlende Nachweise werden nachgefordert, Fristen werden bewertet, Registerdaten können abgefragt werden, eine Risikoklasse wird ermittelt, und danach wird entschieden, ob der Antrag in die Standardprüfung, vertiefte Prüfung, Nachforderung oder Ablehnung läuft.

Die fachliche Entscheidungslandschaft könnte so aussehen: Zunächst wird geprüft, ob die Behörde zuständig ist. Danach wird geprüft, ob der Antrag fristgerecht eingegangen ist. Parallel wird geprüft, welche Nachweise erforderlich sind. Anschließend wird bewertet, ob die vorliegenden Nachweise vollständig und plausibel sind. Zusätzlich wird eine Risikoklasse ermittelt, beispielsweise auf Basis von Widersprüchen, fehlenden Registertreffern, ungewöhnlichen Angaben oder früheren Auffälligkeiten. Aus diesen Teilentscheidungen ergibt sich der nächste Prüfungspfad und der Statuswechsel im Fachverfahren.

### 5.1 Decision Requirements Diagram als textuelle Architekturansicht

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Eingabedaten | Rohdaten aus Antrag, Fachverfahren, Registerschnittstelle oder DMS. | Antragstyp, Eingangsdatum, Wohnsitz, Nachweise, Registertreffer. | DMN nutzt Input Data als Grundlage für Entscheidungen. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Entscheidung 1 | Zuständigkeit ermitteln. | „Behörde zuständig: ja/nein/unklar.“ | DMN modelliert fachliche Entscheidungen. ([omg.org](https://www.omg.org/dmn/)) |
| Entscheidung 2 | Fristlage bestimmen. | „fristgerecht“, „nachfristfähig“, „verfristet“. | Entscheidungstabellen eignen sich für solche Klassifikationen. ([docs.camunda.io](https://docs.camunda.io/docs/components/best-practices/modeling/choosing-the-dmn-hit-policy/?utm_source=chatgpt.com)) |
| Entscheidung 3 | Nachweispflichten bestimmen. | Liste erforderlicher Nachweise je Antragstyp und Fallgruppe. | Collect-Hit-Policies können mehrere Ergebnisse liefern. ([docs.drools.org](https://docs.drools.org/latest/drools-docs/drools/DMN/index.html?utm_source=chatgpt.com)) |
| Entscheidung 4 | Vollständigkeit prüfen. | „vollständig“, „unvollständig“, „widersprüchlich“. | Hit Policies regeln die Auswertung mehrerer passender Regeln. ([docs.drools.org](https://docs.drools.org/latest/drools-docs/drools/DMN/index.html?utm_source=chatgpt.com)) |
| Entscheidung 5 | Risikoklasse ermitteln. | „niedrig“, „mittel“, „hoch“. | DMN unterstützt komplexe, mehrkriterielle Fachregeln. ([omg.org](https://www.omg.org/dmn/)) |
| Entscheidung 6 | Prüfungspfad bestimmen. | Standardprüfung, Nachforderung, vertiefte Prüfung, Ablehnungsvorbereitung. | DMN und BPMN sind komplementär nutzbar. ([omg.org](https://www.omg.org/dmn/)) |
| Entscheidung 7 | Zielstatus bestimmen. | „in Prüfung“, „Nachforderung offen“, „unzulässig“, „entscheidungsreif“. | BPMN nutzt das Ergebnis für den weiteren Ablauf. ([omg.org](https://www.omg.org/bpmn/)) |
| Wissensquellen | Herkunft der Regeln. | Fachgesetz, Verwaltungsvorschrift, Fachkonzept, Architekturentscheidung. | DMN schafft eine standardisierte Brücke zwischen Fachdesign und Implementierung. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |

Textuell sieht das DRD so aus: Die Entscheidung „Prüfungspfad bestimmen“ hängt ab von „Zuständigkeit ermitteln“, „Fristlage bestimmen“, „Nachweispflichten bestimmen“, „Nachweisvollständigkeit prüfen“ und „Risikoklasse ermitteln“. Diese Entscheidungen hängen wiederum von Eingabedaten ab: Antrag, Eingangsdatum, Antragstyp, Stammdaten, Registerdaten, DMS-Nachweise und Vorgangshistorie. Die Wissensquellen sind Fachgesetz, Verwaltungsvorschrift, fachliche Auslegung, Sicherheitsanforderungen und Betriebsregeln.

## 6. Beispielhafte DMN-Entscheidungstabellen

### 6.1 Entscheidungstabelle: „Fristlage bestimmen“

Diese Tabelle hat die Hit Policy *Unique*, weil genau ein Friststatus herauskommen soll. Wenn mehrere Regeln gleichzeitig zutreffen könnten, wäre die Tabelle fachlich unsauber oder müsste mit Priorität modelliert werden.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Entscheidungsname | Fristlage bestimmen | Ergebnis ist ein Friststatus. | Unique bedeutet, dass nur eine Regel zutreffen darf. ([docs.camunda.io](https://docs.camunda.io/docs/components/best-practices/modeling/choosing-the-dmn-hit-policy/?utm_source=chatgpt.com)) |
| Hit Policy | U — Unique | Genau eine Regel darf passen. | Hit Policies bestimmen die Auswertung passender Regeln. ([docs.drools.org](https://docs.drools.org/latest/drools-docs/drools/DMN/index.html?utm_source=chatgpt.com)) |
| Eingabe 1 | Eingangsdatum relativ zur Antragsfrist | vor Fristende, am Fristende, nach Fristende | DMN-Tabellen enthalten Eingaben, Regeln und Ausgaben. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Eingabe 2 | Ausnahmegrund vorhanden | ja/nein | FEEL kann Bedingungen in Tabellen ausdrücken. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Ausgabe | Friststatus | fristgerecht, nachfristfähig, verfristet | DMN eignet sich für fachliche Klassifikationen. ([omg.org](https://www.omg.org/dmn/)) |

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Regel 1 | Wenn Eingangsdatum vor oder am Fristende liegt, ist der Antrag fristgerecht. | Eingangsdatum ≤ Fristende → fristgerecht | DMN-Entscheidungstabellen bilden Bedingungen und Ergebnisse ab. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Regel 2 | Wenn Eingangsdatum nach Fristende liegt und ein fachlich zulässiger Ausnahmegrund vorliegt, ist der Antrag nachfristfähig. | Eingangsdatum > Fristende und Ausnahmegrund = ja → nachfristfähig | Unique verlangt nicht überlappende Regeln. ([docs.camunda.io](https://docs.camunda.io/docs/components/best-practices/modeling/choosing-the-dmn-hit-policy/?utm_source=chatgpt.com)) |
| Regel 3 | Wenn Eingangsdatum nach Fristende liegt und kein Ausnahmegrund vorliegt, ist der Antrag verfristet. | Eingangsdatum > Fristende und Ausnahmegrund = nein → verfristet | Überlappungen oder Lücken müssen fachlich geprüft werden. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |

### 6.2 Entscheidungstabelle: „Nachweispflichten bestimmen“

Diese Entscheidung kann mehrere Nachweise zurückgeben. Deshalb ist *Collect* plausibel. Wenn ein Antrag mehrere Fallgruppen erfüllt, sollen mehrere Nachweise gesammelt werden. Collect kann mehrere Treffer zurückgeben; je nach Engine und Zielbild muss geklärt werden, ob Reihenfolge, Duplikate und Aggregation fachlich relevant sind. ([docs.drools.org](https://docs.drools.org/latest/drools-docs/drools/DMN/index.html?utm_source=chatgpt.com))

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Entscheidungsname | Nachweispflichten bestimmen | Ergebnis ist eine Liste erforderlicher Nachweise. | Collect kann mehrere passende Ergebnisse liefern. ([docs.drools.org](https://docs.drools.org/latest/drools-docs/drools/DMN/index.html?utm_source=chatgpt.com)) |
| Hit Policy | C — Collect | Mehrere Regeln dürfen zutreffen. | Camunda beschreibt Collect als Hit Policy für mehrere Treffer. ([docs.camunda.io](https://docs.camunda.io/docs/components/best-practices/modeling/choosing-the-dmn-hit-policy/?utm_source=chatgpt.com)) |
| Eingabe 1 | Antragstyp | Erst Antrag, Verlängerung, Änderung | DMN-Tabellen kombinieren Eingabebedingungen und Ausgaben. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Eingabe 2 | Personengruppe oder Fallgruppe | Standardfall, Sonderfall A, Sonderfall B | DMN unterstützt mehrkriterielle Regeln. ([omg.org](https://www.omg.org/dmn/)) |
| Eingabe 3 | Registertreffer | vorhanden, nicht vorhanden, widersprüchlich | Eingabedaten können aus Fachsystemen oder Schnittstellen stammen. ([omg.org](https://www.omg.org/dmn/)) |
| Ausgabe | Erforderlicher Nachweis | Identitätsnachweis, Wohnsitznachweis, Einkommensnachweis, Zusatznachweis | DMN schafft explizite Fachregelartefakte. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Regel 1 | Für jeden Erstantrag ist ein Identitätsnachweis erforderlich. | Antragstyp = Erstantrag → Identitätsnachweis | Entscheidungstabellen bilden Regeln zeilenweise ab. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Regel 2 | Wenn kein belastbarer Registertreffer vorliegt, ist ein Wohnsitznachweis erforderlich. | Registertreffer = nicht vorhanden → Wohnsitznachweis | Collect erlaubt mehrere passende Regeln. ([docs.drools.org](https://docs.drools.org/latest/drools-docs/drools/DMN/index.html?utm_source=chatgpt.com)) |
| Regel 3 | Bei Sonderfall A ist ein Zusatznachweis erforderlich. | Fallgruppe = Sonderfall A → Zusatznachweis A | Mehrkriterielle Regeln sind ein typisches DMN-Einsatzfeld. ([omg.org](https://www.omg.org/dmn/)) |
| Regel 4 | Bei widersprüchlichem Registertreffer ist eine Klärungsunterlage erforderlich. | Registertreffer = widersprüchlich → Klärungsnachweis | DMN hilft, Fachregeln explizit und diskutierbar zu machen. ([omg.org](https://www.omg.org/dmn/)) |

### 6.3 Entscheidungstabelle: „Risikoklasse ermitteln“

Hier kannst du zwei Modellierungsarten wählen. Entweder du berechnest Punkte und leitest daraus eine Risikoklasse ab, oder du definierst direkte Klassifikationsregeln. Für Behördenarchitektur ist die Punktevariante oft transparenter, weil Einzelindikatoren nachvollziehbar bleiben.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Entscheidungsname | Risikopunkte ermitteln | Mehrere Risikoindikatoren werden gesammelt oder summiert. | Collect kann mit Aggregation genutzt werden. ([docs.camunda.io](https://docs.camunda.io/docs/components/best-practices/modeling/choosing-the-dmn-hit-policy/?utm_source=chatgpt.com)) |
| Hit Policy | C+ — Collect Sum | Mehrere passende Regeln werden addiert. | Camunda beschreibt Collect mit Aggregatoren wie Sum, Min, Max und Count. ([docs.camunda.io](https://docs.camunda.io/docs/components/best-practices/modeling/choosing-the-dmn-hit-policy/?utm_source=chatgpt.com)) |
| Eingabe | Risikoindikatoren | widersprüchliche Angaben, fehlender Registertreffer, frühere Korrekturen | DMN unterstützt mehrkriterielle Geschäftsregeln. ([omg.org](https://www.omg.org/dmn/)) |
| Ausgabe | Risikopunkte | 0, 10, 20, 40 | Hit Policy bestimmt Ergebnisbildung bei mehreren Treffern. ([docs.drools.org](https://docs.drools.org/latest/drools-docs/drools/DMN/index.html?utm_source=chatgpt.com)) |

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Regel 1 | Keine Auffälligkeit ergibt keine Zusatzpunkte. | Keine Auffälligkeit → 0 Punkte | DMN macht Regelbeiträge explizit. ([omg.org](https://www.omg.org/dmn/)) |
| Regel 2 | Widerspruch zwischen Antrag und Register erhöht Risiko. | Registerwiderspruch = ja → 40 Punkte | Collect Sum aggregiert mehrere Regelbeiträge. ([docs.camunda.io](https://docs.camunda.io/docs/components/best-practices/modeling/choosing-the-dmn-hit-policy/?utm_source=chatgpt.com)) |
| Regel 3 | Fehlender Pflichtnachweis erhöht Risiko moderat. | Pflichtnachweis fehlt → 20 Punkte | Hit Policy regelt mehrere Treffer. ([docs.drools.org](https://docs.drools.org/latest/drools-docs/drools/DMN/index.html?utm_source=chatgpt.com)) |
| Regel 4 | Frühere manuelle Korrektur erhöht Risiko leicht. | Vorgangshistorie = Korrekturfall → 10 Punkte | Analyse sollte Überlappungen und Lücken prüfen. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |

Danach folgt eine zweite Entscheidung „Risikoklasse bestimmen“ mit Unique:

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Regel 1 | 0 bis 19 Punkte ergeben niedrige Risikoklasse. | Punkte 0..19 → niedrig | Unique verlangt eindeutige Regelzuordnung. ([docs.camunda.io](https://docs.camunda.io/docs/components/best-practices/modeling/choosing-the-dmn-hit-policy/?utm_source=chatgpt.com)) |
| Regel 2 | 20 bis 49 Punkte ergeben mittlere Risikoklasse. | Punkte 20..49 → mittel | Lücken und Überschneidungen müssen geprüft werden. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |
| Regel 3 | Ab 50 Punkten ergibt sich hohe Risikoklasse. | Punkte ≥ 50 → hoch | DMN-Tabellen sollten vollständig und widerspruchsfrei sein. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |

### 6.4 Entscheidungstabelle: „Prüfungspfad bestimmen“

Diese Entscheidung ist die Brücke zurück in BPMN. Das Ergebnis steuert den Prozess.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Entscheidungsname | Prüfungspfad bestimmen | Liefert den nächsten fachlichen Bearbeitungspfad. | DMN arbeitet neben BPMN und ergänzt Prozessmodelle um Entscheidungslogik. ([omg.org](https://www.omg.org/dmn/)) |
| Hit Policy | F oder U | U bei disjunkten Regeln; F nur, wenn Regelreihenfolge fachlich gewollt ist. | First nutzt die erste passende Regel; Unique erlaubt nur einen Treffer. ([docs.drools.org](https://docs.drools.org/latest/drools-docs/drools/DMN/index.html?utm_source=chatgpt.com)) |
| Eingaben | Zuständigkeit, Friststatus, Vollständigkeit, Risikoklasse | zuständig = nein; Friststatus = verfristet; Risiko = hoch | DMN modelliert mehrkriterielle Entscheidungen. ([omg.org](https://www.omg.org/dmn/)) |
| Ausgabe | Prüfungspfad | Standardprüfung, Nachforderung, vertiefte Prüfung, Ablehnungsvorbereitung | BPMN nutzt das Ergebnis für den Ablauf. ([omg.org](https://www.omg.org/bpmn/)) |

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Regel 1 | Wenn die Behörde nicht zuständig ist, wird an den Zuständigkeitsklärungspfad übergeben. | zuständig = nein → Zuständigkeitsklärung | DMN-Entscheidungen können Prozesspfade bestimmen. ([omg.org](https://www.omg.org/dmn/)) |
| Regel 2 | Wenn Antrag verfristet ist, wird Ablehnungsvorbereitung gestartet. | Friststatus = verfristet → Ablehnungsvorbereitung | DMN und BPMN sind komplementär. ([omg.org](https://www.omg.org/dmn/)) |
| Regel 3 | Wenn Nachweise fehlen, wird Nachforderung gestartet. | Vollständigkeit = unvollständig → Nachforderung | BPMN bildet anschließend die Nachforderung als Aufgabe ab. ([omg.org](https://www.omg.org/bpmn/)) |
| Regel 4 | Wenn Risiko hoch ist, wird vertiefte Prüfung gestartet. | Risikoklasse = hoch → vertiefte Prüfung | DMN eignet sich für mehrkriterielle Regelentscheidungen. ([omg.org](https://www.omg.org/dmn/)) |
| Regel 5 | Wenn alles formal sauber und Risiko niedrig oder mittel ist, läuft Standardprüfung. | zulässig, vollständig, Risiko niedrig/mittel → Standardprüfung | Entscheidungstabellen sollten eindeutige und vollständige Regeln enthalten. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |

## 7. Zusammenspiel von BPMN und DMN

Das Zusammenspiel ist einfach, aber in der Praxis oft falsch umgesetzt. BPMN enthält eine Aktivität, zum Beispiel „Formale Zulässigkeit prüfen“. Diese Aktivität ruft ein DMN-Entscheidungsmodell auf. Das DMN-Modell liefert ein Ergebnis, beispielsweise `zulässig`, `unzulässig`, `Nachforderung erforderlich` oder `manuelle Klärung`. Danach entscheidet BPMN anhand dieses Ergebnisses, welcher Prozesspfad folgt.

Ein gutes BPMN-DMN-Zusammenspiel sieht so aus: Das BPMN-Modell bleibt lesbar und zeigt die Bearbeitungslogik. Das DMN-Modell enthält die fachliche Regelmatrix. Das Fachverfahren oder eine Rule Engine kann später die DMN-Logik ausführen, aber die fachliche Verantwortung bleibt sichtbar. Die OMG betont, dass BPMN und DMN unabhängig nutzbar, aber komplementär entworfen sind. ([omg.org](https://www.omg.org/dmn/))

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| BPMN-Start | Prozess beginnt mit Antragseingang. | Start Event „Antrag eingegangen“. | BPMN ist Standard für Geschäftsprozessdiagramme. ([omg.org](https://www.omg.org/spec/BPMN/2.0.2/About-BPMN)) |
| BPMN-Aktivität | Prozess ruft Entscheidung auf. | Business-Rule-Task „Prüfungspfad bestimmen“. | BPMN soll fachlich verständlich und technisch präzise sein. ([omg.org](https://www.omg.org/bpmn/)) |
| DMN-Entscheidung | Entscheidung wird anhand von Regeln getroffen. | DMN liefert `Nachforderung`. | DMN spezifiziert Entscheidungslogik. ([omg.org](https://www.omg.org/dmn/)) |
| BPMN-Gateway | Gateway wertet nur das Ergebnis aus, nicht die ganze Regelmatrix. | Wenn Prüfungspfad = Nachforderung, dann Nachweis anfordern. | DMN und BPMN sind komplementär. ([omg.org](https://www.omg.org/dmn/)) |
| BPMN-Folge | Prozess setzt Bearbeitung fort. | Nachforderung versenden, Frist setzen, Wiedervorlage planen. | BPMN beschreibt Ablauf und Übergaben. ([omg.org](https://www.omg.org/bpmn/)) |

Die Regel lautet: Je mehr fachliche Bedingungen in BPMN-Gateways auftauchen, desto wahrscheinlicher ist das Modell falsch geschnitten. BPMN soll nicht zur Ersatz-Entscheidungstabelle werden.

## 8. DMN-Vorlage für Behörden-Facharchitektur

Diese Vorlage kannst du in Architekturpaketen, Fachkonzepten, Ausschreibungen, Reviews oder Modernisierungsprojekten verwenden.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Modellname | Eindeutiger Name des Entscheidungsmodells. | DMN-FV-001 Formale Antragsprüfung | DMN schafft standardisierte Entscheidungsmodelle. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| Zweck | Fachlicher Zweck der Entscheidung. | Ermittlung des nächsten Prüfungspfads nach Antragseingang. | DMN soll Business- und IT-Verständnis verbinden. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| Geltungsbereich | Verfahren, Organisationseinheit, Antragstypen, Kanäle. | Gilt für Online- und Papier-Erstanträge. | DMN unterstützt organisationsweite Entscheidungsbausteine. ([omg.org](https://www.omg.org/dmn/)) |
| Nicht-Geltungsbereich | Bewusst ausgeschlossene Fälle. | Sonderverfahren X wird separat geregelt. | Klare Scope-Abgrenzung reduziert Modellrisiken. ([omg.org](https://www.omg.org/dmn/)) |
| Owner | Fachlich verantwortliche Stelle. | Referat Fachverfahren, Fachverantwortliche Person. | DMN ist für Fachseite und technische Umsetzung lesbar. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| Wissensquellen | Herkunft der Regeln. | Gesetz, Verwaltungsvorschrift, Fachkonzept, ADR. | DMN dokumentiert Entscheidungswissen nachvollziehbar. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| Eingabedaten | Datenobjekte, Quellen, Qualität, Schutzbedarf. | Antrag, Registerauskunft, DMS-Nachweise. | DMN-Tabellen nutzen Eingabedaten. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Entscheidungen | Einzelentscheidungen und Abhängigkeiten. | Fristlage, Nachweispflicht, Risikoklasse, Prüfungspfad. | DMN unterstützt Zerlegung komplexer Entscheidungssysteme. ([omg.org](https://www.omg.org/dmn/)) |
| Entscheidungstabellen | Regeln, Hit Policy, Eingabe- und Ausgabespalten. | Unique-Tabelle „Fristlage bestimmen“. | Hit Policy ist Bestandteil der Entscheidungstabelle. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Testfälle | Positiv-, Negativ-, Grenz- und Konfliktfälle. | Frist genau am Stichtag; fehlender Nachweis; widersprüchlicher Registertreffer. | Forschung betont Prüfung auf Lücken und Überlappungen. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |
| Versionierung | Version, Datum, Änderungsgrund, Freigabe. | v1.2 wegen neuer Verwaltungsvorschrift. | DMN unterstützt wiederverwendbare und verwaltbare Entscheidungsbausteine. ([omg.org](https://www.omg.org/dmn/)) |
| BPMN-Kopplung | Prozessschritt, der die Entscheidung nutzt. | Business-Rule-Task „Prüfungspfad bestimmen“. | BPMN und DMN wurden komplementär entworfen. ([omg.org](https://www.omg.org/dmn/)) |
| Architekturwirkung | Auswirkungen auf Fachverfahren, Schnittstellen, IAM, Logging, Test, Betrieb. | Regelentscheidung muss im Audit Log nachvollziehbar sein. | DMN reduziert Aufwand und Risiko bei Entscheidungsautomatisierung. ([omg.org](https://www.omg.org/dmn/)) |

## 9. Interviewtechnik: So extrahierst du Fachregeln sauber

Fachbereiche sprechen selten direkt in DMN. Sie sagen nicht: „Wir brauchen eine Unique-Hit-Policy mit disjunkten Regeln.“ Sie sagen: „Normalerweise reicht der Nachweis, außer bei Sonderfall A; wenn die Frist überschritten ist, kommt es darauf an; bei bestimmten Fällen geht das zur manuellen Prüfung.“ Deine Aufgabe ist, aus diesen Aussagen prüfbare Regeln zu machen.

Du interviewst nicht nur nach dem Normalfall, sondern gezielt nach Varianten, Ausnahmen, Grenzfällen, Widersprüchen und Quellen. Gute Regelinterviews sind handwerklich präzise. Du fragst nicht: „Wie läuft der Prozess?“ Du fragst zusätzlich: „Woran erkennen Sie, dass dieser Fall anders behandelt werden muss? Welche Daten brauchen Sie dafür? Wer darf diese Regel ändern? Wo steht diese Regel? Was passiert, wenn zwei Regeln gleichzeitig zutreffen?“

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Entscheidungsfrage | Welche fachliche Frage soll beantwortet werden? | „Ist der Antrag formell zulässig?“ | DMN modelliert Entscheidungen. ([omg.org](https://www.omg.org/dmn/)) |
| Ergebnisraum | Welche möglichen Ergebnisse gibt es? | zulässig, unzulässig, Nachforderung, manuelle Klärung. | DMN-Tabellen enthalten Ausgaben. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Eingabedaten | Welche Informationen braucht die Entscheidung? | Antragstyp, Frist, Nachweise, Registertreffer. | DMN nutzt Input Data. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Datenquelle | Woher kommen die Eingaben? | Fachverfahren, Portal, Registerschnittstelle, DMS. | DMN kann mit Prozess- und Systemmodellen verbunden werden. ([omg.org](https://www.omg.org/dmn/)) |
| Regelquelle | Wo ist die Regel begründet? | Gesetz, Verwaltungsvorschrift, Fachkonzept, gelebte Praxis. | DMN schafft Nachvollziehbarkeit zwischen Fachdesign und Umsetzung. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| Normalfall | Welche Regel gilt im Standardfall? | Vollständig und fristgerecht → Standardprüfung. | Entscheidungstabellen strukturieren fachliche Regeln. ([omg.org](https://www.omg.org/dmn/)) |
| Ausnahme | Wann gilt der Normalfall nicht? | Frist überschritten, aber Ausnahmegrund vorhanden. | DMN hilft bei komplexen mehrkriteriellen Regeln. ([omg.org](https://www.omg.org/dmn/)) |
| Grenzfall | Was passiert am Rand einer Regel? | Eingang genau am Fristende. | DMN-Analyse prüft Lücken und Überschneidungen. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |
| Konfliktfall | Was passiert, wenn mehrere Regeln passen? | Nachforderung und hohe Risikoklasse zugleich. | Hit Policies bestimmen die Auswertung mehrerer Treffer. ([docs.drools.org](https://docs.drools.org/latest/drools-docs/drools/DMN/index.html?utm_source=chatgpt.com)) |
| Änderbarkeit | Wer darf die Regel ändern und wie wird sie freigegeben? | Fachreferat gibt Regeländerung frei; IT setzt um. | DMN ist für Fachseite und technische Umsetzung lesbar. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| Testbarkeit | Welche Beispiele beweisen, dass die Regel korrekt verstanden wurde? | Je Regel mindestens ein Positiv- und ein Negativfall. | Forschung betont formale Analyse von Entscheidungstabellen. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |

Ein sehr wirksamer Satz im Interview lautet: „Bitte geben Sie mir drei echte Falltypen: einen einfachen Standardfall, einen schwierigen Sonderfall und einen Fall, bei dem erfahrene Sachbearbeitung diskutieren würde.“ Aus diesen drei Fällen entstehen meist die ersten tragfähigen DMN-Regeln.

## 10. Typische Fehler bei DMN in Behördenprojekten

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Prozess und Entscheidung vermischt | Fachregeln werden als BPMN-Gateway-Labyrinth modelliert. | Zwölf Gateways statt einer DMN-Tabelle. | BPMN und DMN sind komplementär und sollten passend eingesetzt werden. ([omg.org](https://www.omg.org/dmn/)) |
| Entscheidungsfrage fehlt | Tabelle hat keinen klaren Zweck. | „Prüfung“ statt „Welche Nachweise sind erforderlich?“ | DMN modelliert konkrete Entscheidungen. ([omg.org](https://www.omg.org/dmn/)) |
| Ergebnisraum unklar | Ausgaben sind unscharf oder vermischt. | „ok“, „prüfen“, „vielleicht“, „Sonderfall“. | DMN soll eindeutige Entscheidungsmodelle ermöglichen. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| Falsche Hit Policy | Mehrere Regeln können treffen, aber Tabelle steht auf Unique. | Antrag ist Erstantrag und Sonderfall; zwei Zeilen passen. | Unique erlaubt nur eine passende Regel. ([docs.camunda.io](https://docs.camunda.io/docs/components/best-practices/modeling/choosing-the-dmn-hit-policy/?utm_source=chatgpt.com)) |
| Keine Regelquelle | Niemand weiß, warum eine Regel gilt. | „Das machen wir schon immer so.“ | DMN soll Diskussion und Einigung über Entscheidungslogik unterstützen. ([omg.org](https://www.omg.org/dmn/)) |
| Unvollständige Tabellen | Bestimmte Eingabekombinationen sind nicht abgedeckt. | Registertreffer = unklar fehlt. | Analyse von DMN-Tabellen betrachtet fehlende Regeln. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |
| Überlappende Regeln | Mehrere Regeln liefern unterschiedliche Ergebnisse. | Eine Regel sagt Standardprüfung, andere vertiefte Prüfung. | Analyse von DMN-Tabellen betrachtet überlappende Regeln. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |
| Fachbegriffe nicht definiert | Begriffe werden unterschiedlich verstanden. | „vollständig“ bedeutet je Referat etwas anderes. | DMN soll Fach- und Technikverständnis verbinden. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| Technische Felder statt fachlicher Sprache | Tabelle übernimmt Datenbanknamen. | `IS_REG_HIT_FLG = 0` statt „Registertreffer vorhanden = nein“. | DMN ist für Business User verständlich angelegt. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| Keine Testfälle | Modell sieht gut aus, ist aber fachlich nicht geprüft. | Sonderfall wird erst in Produktion erkannt. | DMN-Tabellen sollten auf Lücken und Überschneidungen geprüft werden. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |
| Keine Versionierung | Regeländerungen sind nicht nachvollziehbar. | Fachregel wurde geändert, aber alte Bescheide sind nicht erklärbar. | DMN unterstützt verwaltbare Entscheidungsbausteine. ([omg.org](https://www.omg.org/dmn/)) |
| Zu große Tabellen | Eine Tabelle versucht alles zugleich zu entscheiden. | 80 Regeln mit Frist, Risiko, Zuständigkeit, Nachweisen und Status. | DMN unterstützt grafische Zerlegung komplexer Anforderungen. ([omg.org](https://www.omg.org/dmn/)) |

Der wichtigste Korrekturimpuls lautet: Schneide große Entscheidungen in kleine, fachlich benannte Entscheidungen. Eine gute DMN-Landschaft ist nicht eine gigantische Tabelle, sondern ein Netz verständlicher Teilentscheidungen.

## 11. Qualitätskriterien für gute DMN-Modelle

Ein gutes DMN-Modell ist fachlich verständlich, regeltechnisch eindeutig, testbar, versionierbar und mit BPMN, Datenarchitektur und Systemarchitektur verbunden. Für Behörden kommt zusätzlich hinzu: Die Regelherkunft muss nachvollziehbar sein, die fachliche Verantwortung muss klar sein, und die Auswirkungen auf Bescheidung, Nachweisführung, Betrieb und Dienstleistersteuerung müssen erkennbar werden.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Fachliche Klarheit | Jede Entscheidung hat eine klare Frage. | „Welche Nachweise sind erforderlich?“ | DMN modelliert konkrete Geschäftsentscheidungen. ([omg.org](https://www.omg.org/dmn/)) |
| Eindeutiger Ergebnisraum | Ausgaben sind definiert und begrenzt. | `standard`, `nachforderung`, `vertieft`, `ablehnungsvorbereitung`. | Entscheidungstabellen enthalten definierte Ausgaben. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Passende Hit Policy | Auswertungslogik entspricht der Fachlogik. | Collect für mehrere Nachweise, Unique für Friststatus. | Hit Policies bestimmen Ergebnisbildung. ([docs.drools.org](https://docs.drools.org/latest/drools-docs/drools/DMN/index.html?utm_source=chatgpt.com)) |
| Vollständigkeit | Alle relevanten Eingabekombinationen sind abgedeckt. | Auch `Registertreffer = unklar` ist geregelt. | DMN-Analyse prüft fehlende Regeln. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |
| Widerspruchsfreiheit | Regeln überlappen nicht unbeabsichtigt. | Keine Kombination führt gleichzeitig zu Standard- und Ablehnungspfad. | DMN-Analyse prüft überlappende Regeln. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |
| Quellenbezug | Jede relevante Regel verweist auf eine Quelle. | Regelquelle: Verwaltungsvorschrift Abschnitt X. | DMN verbindet Fachdesign und technische Umsetzung. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| Testbarkeit | Jede Regel hat Beispiele. | Testfall: Frist exakt am Stichtag. | Analyse und Tests sind zentrale Qualitätssicherung für DMN. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |
| BPMN-Kopplung | Prozess nutzt Entscheidungsergebnis, modelliert aber nicht die ganze Regelmatrix. | Gateway nach DMN-Ergebnis. | BPMN und DMN sind komplementär. ([omg.org](https://www.omg.org/dmn/)) |
| Datenbezug | Eingaben sind mit Datenobjekten und führenden Systemen verbunden. | Registertreffer kommt aus Registerschnittstelle, Nachweisstatus aus DMS. | DMN nutzt Eingabedaten für Entscheidungen. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Governance | Owner, Version, Freigabe und Änderungsweg sind definiert. | Fachreferat verantwortet Regelversion 1.2. | DMN unterstützt verwaltbare Entscheidungsbausteine. ([omg.org](https://www.omg.org/dmn/)) |

## 12. Konkrete Umsetzung im Projekt

In einem echten Behördenprojekt gehst du in sieben Schritten vor. Erstens identifizierst du im BPMN-Prozess alle Stellen, an denen fachlich entschieden wird. Zweitens formulierst du jede Entscheidung als Frage. Drittens bestimmst du Ergebnisraum und Eingabedaten. Viertens klärst du Regelquellen und Verantwortlichkeiten. Fünftens modellierst du ein DRD, damit Abhängigkeiten sichtbar werden. Sechstens erstellst du Entscheidungstabellen mit passender Hit Policy. Siebtens validierst du die Tabellen mit Fachbereich, Test, IT und Betrieb.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Schritt 1 | Entscheidungsstellen im Prozess markieren. | Gateway „vollständig?“ wird Kandidat für DMN. | BPMN beschreibt Prozesslogik. ([omg.org](https://www.omg.org/bpmn/)) |
| Schritt 2 | Entscheidungsfrage formulieren. | „Ist der Antrag vollständig?“ | DMN modelliert Entscheidungen. ([omg.org](https://www.omg.org/dmn/)) |
| Schritt 3 | Ergebnisraum definieren. | vollständig, unvollständig, widersprüchlich. | DMN-Tabellen haben Ausgaben. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Schritt 4 | Eingabedaten bestimmen. | Liste eingereichter Nachweise, erforderliche Nachweise. | DMN-Tabellen haben Eingaben. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Schritt 5 | Wissensquellen zuordnen. | Fachkonzept, Verwaltungsvorschrift, Gremienentscheidung. | DMN soll Fachdesign und Umsetzung verbinden. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN)) |
| Schritt 6 | Entscheidungstabelle bauen. | Regeln mit Hit Policy Unique oder Collect. | Hit Policies bestimmen die Auswertung. ([docs.drools.org](https://docs.drools.org/latest/drools-docs/drools/DMN/index.html?utm_source=chatgpt.com)) |
| Schritt 7 | Testfälle und Review durchführen. | Jede Regel mit Positiv-, Negativ- und Grenzfall. | DMN-Analyse prüft Lücken und Überlappungen. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |

Als Enterprise Architekt solltest du dabei nicht in Tooldetails abtauchen. Deine Kernleistung ist die Strukturierung: Welche Entscheidungen gibt es? Welche Regeln gehören zusammen? Welche Daten werden benötigt? Welche Systeme liefern diese Daten? Welche Regelquelle gilt? Welche Prozessschritte verwenden das Ergebnis? Welche Risiken entstehen bei Änderung, Migration oder Automatisierung?

## 13. Übung mit Musterlösung

### Übungsfall

Eine Behörde nimmt Anträge entgegen. Ein Antrag kann nur weiter in die Sachprüfung gehen, wenn die Behörde zuständig ist, der Antrag fristgerecht oder nachfristfähig ist und alle erforderlichen Nachweise vorliegen. Wenn Nachweise fehlen, wird eine Nachforderung erstellt. Wenn die Behörde nicht zuständig ist, geht der Fall in die Zuständigkeitsklärung. Wenn der Antrag verfristet und nicht nachfristfähig ist, wird eine Ablehnungsvorbereitung gestartet. Zusätzlich soll bei hoher Risikoklasse eine vertiefte Prüfung erfolgen, sofern der Antrag nicht bereits wegen Zuständigkeit oder Frist ausscheidet.

Deine Aufgabe ist: Identifiziere die DMN-Entscheidungen, Eingabedaten, Wissensquellen und Entscheidungstabellen. Lege außerdem fest, wo BPMN und DMN gekoppelt werden.

### Musterlösung: Entscheidungen

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Entscheidung 1 | Zuständigkeit ermitteln | Ergebnis: zuständig, nicht zuständig, unklar | DMN modelliert Geschäftsentscheidungen. ([omg.org](https://www.omg.org/dmn/)) |
| Entscheidung 2 | Fristlage bestimmen | Ergebnis: fristgerecht, nachfristfähig, verfristet | Entscheidungstabellen eignen sich für Klassifikation. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Entscheidung 3 | Erforderliche Nachweise bestimmen | Ergebnis: Liste erforderlicher Nachweise | Collect kann mehrere Ergebnisse liefern. ([docs.drools.org](https://docs.drools.org/latest/drools-docs/drools/DMN/index.html?utm_source=chatgpt.com)) |
| Entscheidung 4 | Nachweisvollständigkeit prüfen | Ergebnis: vollständig, unvollständig, widersprüchlich | DMN-Tabellen kombinieren Eingaben und Ausgaben. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Entscheidung 5 | Risikoklasse bestimmen | Ergebnis: niedrig, mittel, hoch | DMN unterstützt mehrkriterielle Regeln. ([omg.org](https://www.omg.org/dmn/)) |
| Entscheidung 6 | Prüfungspfad bestimmen | Ergebnis: Zuständigkeitsklärung, Ablehnungsvorbereitung, Nachforderung, vertiefte Prüfung, Standardprüfung | DMN kann BPMN-Prozesspfade steuern. ([omg.org](https://www.omg.org/dmn/)) |

### Musterlösung: Eingabedaten

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Antrag | Enthält Antragstyp, Eingangsdatum, Erklärungen und Metadaten. | Antragstyp = Erstantrag | DMN-Tabellen nutzen Eingabedaten. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Personendaten | Fachlich relevante Stammdaten. | Wohnsitz, Identitätsstatus | Input Data ist Grundlage von Entscheidungen. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Fristdaten | Stichtag, Eingangsdatum, Ausnahmegrund. | Eingangsdatum > Fristende | DMN kann Datumsbedingungen verwenden. ([ibm.com](https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=started-decision-service-in-15-minutes&utm_source=chatgpt.com)) |
| Nachweisdaten | Eingereichte und erforderliche Nachweise. | Einkommensnachweis fehlt | Entscheidungstabellen bilden Regeln ab. ([omg.org](https://www.omg.org/dmn/)) |
| Registerdaten | Treffer, Nichttreffer oder Widerspruch. | Registertreffer = widersprüchlich | DMN kann Eingaben aus Systemen und Schnittstellen verwenden. ([omg.org](https://www.omg.org/dmn/)) |
| Vorgangshistorie | Frühere Fälle, Korrekturen oder Klärungen. | frühere manuelle Korrektur | DMN unterstützt mehrkriterielle Entscheidung. ([omg.org](https://www.omg.org/dmn/)) |

### Musterlösung: zentrale Entscheidungstabelle „Prüfungspfad bestimmen“

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Hit Policy | First oder Unique; fachlich empfehlenswert ist Unique mit disjunkten Bedingungen. | Keine Regel darf widersprüchlich mehrere Pfade liefern. | Unique erlaubt nur eine passende Regel; First nimmt die erste passende Regel. ([docs.drools.org](https://docs.drools.org/latest/drools-docs/drools/DMN/index.html?utm_source=chatgpt.com)) |
| Regel 1 | Nicht zuständig hat Vorrang. | Zuständigkeit = nicht zuständig → Zuständigkeitsklärung | DMN kann fachliche Pfade bestimmen. ([omg.org](https://www.omg.org/dmn/)) |
| Regel 2 | Verfristet ohne Nachfristfähigkeit führt zur Ablehnungsvorbereitung. | Friststatus = verfristet → Ablehnungsvorbereitung | DMN modelliert Entscheidungslogik. ([omg.org](https://www.omg.org/dmn/)) |
| Regel 3 | Fehlende Nachweise führen zur Nachforderung. | Nachweisvollständigkeit = unvollständig → Nachforderung | BPMN bildet danach den Nachforderungsprozess ab. ([omg.org](https://www.omg.org/bpmn/)) |
| Regel 4 | Hohe Risikoklasse führt zur vertieften Prüfung. | Risiko = hoch → vertiefte Prüfung | DMN unterstützt mehrkriterielle Fachregeln. ([omg.org](https://www.omg.org/dmn/)) |
| Regel 5 | Alle Bedingungen erfüllt und Risiko nicht hoch führt zur Standardprüfung. | zuständig, fristgerecht/nachfristfähig, vollständig, Risiko niedrig/mittel → Standardprüfung | DMN-Tabellen sollten vollständig und widerspruchsfrei sein. ([arxiv.org](https://arxiv.org/abs/1603.07466?utm_source=chatgpt.com)) |

Eine robuste Unique-Variante würde die Vorranglogik nicht nur über Zeilenreihenfolge ausdrücken, sondern die Bedingungen disjunkt formulieren. Beispiel: Die Regel „Nachforderung“ gilt nur, wenn Zuständigkeit nicht negativ ist, Frist nicht verfristet ist und Nachweise unvollständig sind. Die Regel „vertiefte Prüfung“ gilt nur, wenn Zuständigkeit positiv, Fristlage akzeptabel und Nachweise vollständig sind. So vermeidest du, dass die fachliche Priorität nur implizit in der Tabellenreihenfolge steckt.

## 14. Was du am Ende können solltest

Du solltest eine Fachregel nicht mehr als „kleine Bedingung“ behandeln, sondern als Architekturbaustein. Du erkennst künftig, ob eine Aussage Prozesslogik oder Entscheidungslogik ist. Du kannst Entscheidungsfragen formulieren, Eingabedaten bestimmen, Ergebnisräume definieren, Fachregeln in Tabellen überführen, Hit Policies begründen, Wissensquellen dokumentieren, DMN mit BPMN verbinden und aus dem Ganzen ein transparentes Architekturartefakt machen.

Die wichtigste professionelle Haltung lautet: Nicht sofort automatisieren. Erst verstehen, schneiden, benennen, prüfen und versionieren. Danach kann automatisiert werden. DMN ist dann nicht nur ein Diagrammstandard, sondern ein Mittel, um Verwaltungsentscheidungen nachvollziehbar, änderbar, testbar und übergabefähig zu machen.

## 15. Wissensgrenzen und Annahmen

Ich habe das Beispiel bewusst generisch gehalten, weil konkrete Verwaltungsentscheidungen immer an die jeweilige Rechtsgrundlage, Verwaltungsvorschrift, Zuständigkeitsordnung und behördliche Praxis gebunden sind. Für ein echtes BAMF-, Bundes- oder Landesverfahren müsste jede Regel mit der konkreten Rechts- und Fachquelle abgeglichen werden. Stand der geprüften Quellen: Die OMG-Hauptseite beschreibt DMN als Standard für Entscheidungen und Fachregeln; DMN 1.5 ist als formale Version mit Veröffentlichungsdatum August 2024 ausgewiesen, während das OMG-DMN-Taskforce-Repository eine DMN-1.6-Release-Markierung vom 17. Februar 2026 zeigt. Für Ausschreibungen oder Toolkonformität solltest du daher immer die konkret geforderte DMN-Version und Engine-Unterstützung festlegen. ([omg.org](https://www.omg.org/spec/DMN/1.5/About-DMN))

<>