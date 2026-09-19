## Checkliste für deine Applikationsportfolio-Bewertung

1. **Applikationsbegriff klären:** Bewerte nicht Server, Datenbanken oder einzelne Schnittstellen isoliert, sondern fachlich erkennbare Anwendungen mit Zweck, Nutzern, Daten und Verantwortlichkeit.  
2. **Portfolio-Ziel festlegen:** Entscheide vorher, ob du Transparenz, Kostensenkung, Modernisierung, Sicherheitsbewertung, Roadmap-Planung oder Ausschreibungsvorbereitung erreichen willst.  
3. **Fachlichen Wert erfassen:** Frage, welche Verwaltungsleistung, welches Fachverfahren oder welcher Prozess ohne die Anwendung nicht oder nur schlechter funktioniert.  
4. **Kritikalität bestimmen:** Prüfe Auswirkungen auf Bürger, Sachbearbeitung, Fristen, Zahlungen, Bescheide, Berichtspflichten und Behördenleitung.  
5. **Schutzbedarf berücksichtigen:** Bewerte Vertraulichkeit, Integrität und Verfügbarkeit der verarbeiteten Informationen und Systeme.  
6. **Technischen Zustand getrennt bewerten:** Eine alte Anwendung kann stabil und geschäftskritisch sein; eine moderne Anwendung kann schlecht wartbar, teuer oder riskant sein.  
7. **Datenqualität prüfen:** Kläre, ob die Anwendung führende Daten hält, Dubletten erzeugt, manuelle Korrekturen benötigt oder widersprüchliche Datenstände verursacht.  
8. **Schnittstellenabhängigkeit sichtbar machen:** Dokumentiere Provider, Consumer, Register, DMS/eAkte, IAM, Zahlungsdienste, Berichtssysteme und Batch-Strecken.  
9. **Betriebs- und Kostenlage erfassen:** Erhebe Lizenzkosten, Betriebskosten, Dienstleisterkosten, Know-how-Risiken, Release-Aufwand, Störungen und Wartungsfenster.  
10. **Hersteller- und Technologieabhängigkeit bewerten:** Prüfe Support-Ende, proprietäre Komponenten, fehlende Dokumentation, Einzelpersonenwissen und Vertragsbindung.  
11. **Modernisierungsfähigkeit einschätzen:** Unterscheide Stabilisieren, Kapseln, Migrieren, Ersetzen, Refaktorieren und Abschalten.  
12. **Entscheidung ableiten:** Jede Anwendung braucht am Ende eine nachvollziehbare Portfolioentscheidung: investieren, tolerieren, migrieren, ablösen, stilllegen oder beobachten.  

## Grundidee: Applikationsportfolio ist Architektursteuerung, nicht Inventur

Ein Applikationsportfolio ist die strukturierte Gesamtsicht auf Anwendungen einer Organisation. Im Behördenkontext ist es besonders wichtig, weil Anwendungen nicht nur technische Systeme sind, sondern Verwaltungsleistungen ermöglichen: Anträge entgegennehmen, Vorgänge bearbeiten, Registerdaten abrufen, Bescheide erzeugen, Zahlungen auslösen, Akten führen, Fristen überwachen und Berichtspflichten erfüllen. Enterprise Architecture liefert dafür den Ordnungsrahmen, weil sie Geschäftsprozesse, Daten, Anwendungen und Technologie miteinander verbindet; TOGAF beschreibt Enterprise Architecture als bewährte Methode und Rahmenwerk zur Verbesserung organisatorischer Wirksamkeit. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com))

Der häufigste Fehler ist die Gleichsetzung von „alt“ mit „schlecht“ und „neu“ mit „gut“. Das ist fachlich falsch. Eine 18 Jahre alte Anwendung kann stabil, revisionssicher, gut verstanden und für eine Kernleistung unverzichtbar sein. Eine neue Anwendung kann dagegen strategisch unklar, schlecht integriert, teuer im Betrieb und datenfachlich problematisch sein. Bewertet wird deshalb nicht das Baujahr, sondern die Kombination aus **Nutzen, Risiko, Kosten, technischer Zukunftsfähigkeit und strategischer Passung**.

Im Application Portfolio Management arbeitet man typischerweise mit einem Applikationsregister, Portfolio-Darstellungen und Bewertungsdimensionen wie Wert, Kosten, Risiko, Lebenszyklus und Zielzustand. Solche Sichten dienen nicht der Dokumentation um der Dokumentation willen, sondern der Entscheidungsunterstützung für Transformation, Modernisierung und Steuerung. ([palladio-consulting.de](https://www.palladio-consulting.de/application-portfolio-management/?utm_source=chatgpt.com))

## Das Bewertungsmodell: Fünf Fragen statt Bauchgefühl

Eine professionelle Portfoliobewertung beantwortet fünf Kernfragen. Erstens: **Wofür wird die Anwendung fachlich benötigt?** Zweitens: **Was passiert, wenn sie ausfällt, falsche Daten liefert oder nicht mehr gepflegt werden kann?** Drittens: **Wie gesund ist sie technisch, betrieblich und organisatorisch?** Viertens: **Wie gut passt sie zur Zielarchitektur der Behörde?** Fünftens: **Welche Entscheidung ist daraus abzuleiten?**

Diese Denkweise passt gut zum bekannten TIME-Modell aus dem Application Portfolio Management: Anwendungen werden nicht pauschal bewertet, sondern in Entscheidungsrichtungen wie **Tolerate, Invest, Migrate, Eliminate** eingeordnet. Gartner beschreibt Portfolio-Health-Checks unter anderem entlang fachlicher Passung, technischer Passung und Kosten; SAP LeanIX beschreibt TIME ebenfalls als Einordnung nach strategischem Wert und Managementaufwand. ([gartner.com](https://www.gartner.com/en/information-technology/topics/enterprise-apps?utm_source=chatgpt.com))

Für Behörden musst du dieses Modell erweitern. In einem privatwirtschaftlichen Kontext steht oft Kosten-/Nutzenoptimierung im Vordergrund. In einer Bundesbehörde kommen weitere harte Bewertungsdimensionen hinzu: Rechtssicherheit, Nachvollziehbarkeit, Schutzbedarf, Aktenrelevanz, Registerbezug, Nachweisfähigkeit, Barrierefreiheit, Vergabefähigkeit, Dienstleistersteuerung, Betriebssicherheit und Abhängigkeit von hoheitlichen Prozessen.

## Bewertungsdimensionen für Bundesbehörden

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Fachlicher Wert | Misst, wie stark die Anwendung eine Verwaltungsleistung, einen Fachprozess oder eine gesetzliche Aufgabe unterstützt. Hoher Wert bedeutet: Ohne diese Anwendung entsteht fachlicher Stillstand oder erhebliche manuelle Ersatzarbeit. | Fachverfahren für Antragsbearbeitung, Bescheiderstellung oder Registerabgleich. | TOGAF als EA-Rahmen für Verbindung von Geschäft und IT; APM als Entscheidungsinstrument. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com)) |
| Kritikalität | Bewertet die Auswirkung von Ausfall, Fehlern oder Verzögerung auf Bürger, Sachbearbeitung, Fristen, Zahlungen, Berichtspflichten und Behördenleitung. | Zahlungslauf fällt aus; Bescheide werden verspätet erstellt; Fristen können nicht eingehalten werden. | BSI-Schutzbedarfslogik für Auswirkungen auf Zielobjekte. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Nutzerzahl | Erfasst interne und externe Nutzung, aber nicht nur quantitativ. Wenige Nutzer können trotzdem hohe Kritikalität bedeuten, wenn sie zentrale Entscheider oder Spezialrollen sind. | 30 Fachaufsichten nutzen ein Berichtssystem, das die Leitungsvorlage erzeugt. | Portfolio-Health-Check-Logik. ([gartner.com](https://www.gartner.com/en/information-technology/topics/enterprise-apps?utm_source=chatgpt.com)) |
| Schutzbedarf | Bewertet Vertraulichkeit, Integrität und Verfügbarkeit. Das BSI fragt bei der Schutzbedarfsfeststellung, welcher Schaden bei Verletzung dieser Grundwerte entstehen kann; für IT-Systeme soll der Schutzbedarf je Grundwert festgelegt werden. | Personenbezogene Vorgangsdaten, Registerdaten, Bescheide, Zahlungsdaten. | BSI IT-Grundschutz. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Technischer Zustand | Bewertet Architektur, Codequalität, Plattformstand, Patchfähigkeit, Testabdeckung, Dokumentation, Releasefähigkeit und technische Schulden. | Java-EE-Altsystem ohne automatisierte Tests; aktuelles Spring-System ohne saubere Schnittstellenverträge. | EA-/APM-Bewertung über technische Passung. ([gartner.com](https://www.gartner.com/en/information-technology/topics/enterprise-apps?utm_source=chatgpt.com)) |
| Wartbarkeit | Misst, wie gut Änderungen verstanden, getestet, umgesetzt und produktiv gebracht werden können. Entscheidend sind Know-how, Modularität, Testbarkeit, Build-Prozess und Dokumentation. | Jede Gesetzesänderung dauert drei Monate, weil nur ein externer Entwickler das System kennt. | APM-Logik Wert/Kosten/Risiko/Lebenszyklus. ([palladio-consulting.de](https://www.palladio-consulting.de/application-portfolio-management/?utm_source=chatgpt.com)) |
| Betriebskosten | Umfasst Lizenzkosten, Hosting, Betrieb, Support, Dienstleister, Störungen, Rufbereitschaft, manuelle Betriebsarbeiten und Sonderaufwände. | Geringe Lizenzkosten, aber hohe manuelle Aufwände durch nächtliche Batch-Fehler. | Gartner betont Portfolio-Health-Checks inklusive Kostenperspektive. ([gartner.com](https://www.gartner.com/en/information-technology/topics/enterprise-apps?utm_source=chatgpt.com)) |
| Schnittstellenabhängigkeit | Bewertet Anzahl, Kritikalität und Qualität der Schnittstellen. Viele Schnittstellen sind nicht automatisch schlecht; schlecht sind unklare Verträge, instabile Datenflüsse und unbekannte Abhängigkeiten. | Fachverfahren ↔ Register ↔ DMS/eAkte ↔ Zahlungsplattform ↔ Data Warehouse. | APM-Portfoliosichten und Architekturabhängigkeiten. ([palladio-consulting.de](https://www.palladio-consulting.de/application-portfolio-management/?utm_source=chatgpt.com)) |
| Datenqualität | Bewertet Vollständigkeit, Aktualität, Korrektheit, Dubletten, führende Systeme, manuelle Korrekturen und Berichtstauglichkeit. | Personendaten werden im Portal, Fachverfahren und Berichtssystem unterschiedlich gepflegt. | EA-Verknüpfung von Business-, Daten-, Applikations- und Technologieperspektive. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com)) |
| Herstellerabhängigkeit | Bewertet Vendor Lock-in, proprietäre Schnittstellen, auslaufenden Support, Lizenzbindung, Dienstleistermonopol und fehlende Exit-Fähigkeit. | Standardsoftware mit teuren Sonderanpassungen und unklarem Datenexport. | APM betrachtet Risiko, Kosten und Lebenszyklus. ([palladio-consulting.de](https://www.palladio-consulting.de/application-portfolio-management/?utm_source=chatgpt.com)) |
| Lebenszyklus | Bewertet, ob Anwendung, Technologie, Plattform, Datenbank, Betriebssystem, Framework oder Vertrag am Anfang, in Reife, im Extended Support oder am Ende steht. | Datenbankversion läuft in 18 Monaten aus dem Support. | Portfolio-Health-Check und technische Passung. ([gartner.com](https://www.gartner.com/en/information-technology/topics/enterprise-apps?utm_source=chatgpt.com)) |
| Modernisierungsbedarf | Bewertet, ob die Anwendung stabilisiert, gekapselt, refaktoriert, ersetzt, migriert oder abgeschaltet werden sollte. AWS beschreibt typische Migrationsstrategien wie Rehost, Replatform, Relocate und Retire; solche Strategien lassen sich als technische Entscheidungsoptionen in Roadmaps verwenden. ([docs.aws.amazon.com](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html?utm_source=chatgpt.com)) | Legacy-Fachverfahren wird zunächst per API gekapselt, später durch neues Fachverfahren ersetzt. | AWS Prescriptive Guidance; TIME-Modell. ([docs.aws.amazon.com](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html?utm_source=chatgpt.com)) |

## Applikationssteckbrief: Vorlage für die Erfassung

Ein guter Steckbrief ist so kurz wie möglich und so vollständig wie nötig. Er darf nicht zu einem Roman werden, muss aber genug Information liefern, damit Architektur, Fachbereich, Betrieb, Informationssicherheit, Datenschutz, Einkauf und Leitung dieselbe Anwendung gleich verstehen.

| Aspekt | Details/Erklärung | Beispiel |
|---|---|---|
| Applikationsname | Offizieller Name, Kurzname, technische Namen, bekannte Aliasnamen. | „FAVIS“, „Antragsportal“, „Altverfahren X“ |
| Fachlicher Zweck | Welche Verwaltungsleistung oder welcher Prozess wird unterstützt? | Aufnahme und Bearbeitung von Online-Anträgen |
| Fachdomäne | Zuordnung zu Fachbereich, Referat, Prozessgruppe oder Capability. | Antrag, Vorgang, Bescheid, Zahlung, Bericht |
| Applikationstyp | Eigenentwicklung, Standardsoftware, SaaS, Individualanpassung, Plattformkomponente, Reporting, Schnittstellenkomponente. | Standardsoftware mit behördenspezifischer Anpassung |
| Business Owner | Fachlich verantwortliche Stelle für Nutzen, Priorität und fachliche Anforderungen. | Referat A1, Produktverantwortliche Fachseite |
| Application Owner | Verantwortlich für Anwendungspflege, Roadmap, Lifecycle und technische Koordination. | IT-Produktverantwortlicher |
| Technical Owner | Verantwortlich für Architektur, Code, Plattform, Schnittstellen und technische Qualität. | Architekturteam oder Dienstleister |
| Data Owner | Verantwortlich für zentrale Datenobjekte und Datenqualität. | Fachbereich Personenstammdaten |
| Nutzergruppen | Interne Nutzer, externe Nutzer, Admins, Dienstleister, Maschinenkonten. | Antragsteller, Sachbearbeiter, Fachaufsicht |
| Nutzerzahl | Aktive Nutzer pro Monat, Spitzenlast, externe Zugriffe. | 2.500 interne Nutzer, 80.000 externe Anträge/Jahr |
| Fachliche Kritikalität | Auswirkungen bei Ausfall, Fehler oder Verzögerung. | Keine fristgerechte Bescheiderstellung möglich |
| Schutzbedarf | Bewertung für Vertraulichkeit, Integrität und Verfügbarkeit. | V: hoch, I: hoch, A: normal/hoch |
| Datenobjekte | Zentrale Datenobjekte, führende Daten, Kopien, Berichtsdaten. | Person, Vorgang, Nachweis, Bescheid, Zahlung |
| Führendes System | Für welche Daten ist die Anwendung System of Record? | Führend für Vorgangsstatus, nicht für Personendaten |
| Schnittstellen | Provider, Consumer, Protokolle, Kritikalität, SLAs, Datenobjekte. | Registerabruf, DMS-Ablage, Zahlungsfreigabe |
| Technologie | Programmiersprache, Framework, Datenbank, Middleware, Betriebssystem, Plattform. | Java 8, Oracle DB, SOAP, WebLogic |
| Betriebsmodell | On-Prem, Private Cloud, Bundescloud, SaaS, Dienstleisterbetrieb, Eigenbetrieb. | Dienstleisterbetrieb im Rechenzentrum |
| Releasefähigkeit | Deploymenthäufigkeit, Automatisierung, Testgrad, Rollback-Fähigkeit. | Quartalsweise Releases, manuelle CAB-Freigabe |
| Observability | Logging, Monitoring, Tracing, Alerting, Dashboards, Incident-Daten. | Logs vorhanden, keine End-to-End-Traces |
| Kosten | Lizenz, Betrieb, Wartung, Dienstleister, Infrastruktur, Änderungsbudget. | 480.000 €/Jahr Betrieb und Pflege |
| Vertragslage | Laufzeit, Kündigungsfristen, Support-Level, Exit-Regelung, Quellcodezugriff. | Support bis 2028, Exit unklar |
| Lebenszyklusstatus | Neu, aktiv, stabil, kritisch, auslaufend, abgekündigt. | Kritisch: Framework EOL, DB bald EOL |
| Risiken | Fachlich, technisch, betrieblich, sicherheitsbezogen, datenbezogen, organisatorisch. | Einzelpersonenwissen, keine Testautomatisierung |
| Zielbild-Entscheidung | Investieren, stabilisieren, kapseln, migrieren, ersetzen, stilllegen. | Kapseln 2026, Ersatz 2027–2028 |
| Nächster Entscheidungspunkt | Datum und Gremium für nächste Entscheidung. | Architekturboard Q3/2026 |

## Bewertungsmatrix: Von Kriterien zu Entscheidungen

Für den Anfang empfehle ich eine 5er-Skala. Sie ist fein genug für Differenzierung und einfach genug für Workshops. Wichtig: Jede Zahl braucht eine Bedeutung. Ohne Bewertungslogik wird die Matrix politisch verhandelbar und fachlich schwach.

| Aspekt | Details/Erklärung | Skala 1 | Skala 3 | Skala 5 |
|---|---|---:|---:|---:|
| Fachlicher Wert | Beitrag zur Verwaltungsleistung und Fachstrategie. | kaum relevant | wichtig für Teilprozess | unverzichtbar für Kernleistung |
| Kritikalität | Schaden bei Ausfall oder Fehler. | geringe Auswirkung | spürbare Einschränkung | erheblicher Schaden/Stillstand |
| Nutzerzahl/Reichweite | Anzahl und Bedeutung der Nutzergruppen. | wenige Randnutzer | relevante interne Nutzung | breite interne/externe Nutzung |
| Schutzbedarf | Bedarf an Schutz für Vertraulichkeit, Integrität, Verfügbarkeit. | normal | erhöht | hoch/sehr hoch |
| Technisches Risiko | Alter, EOL, Architekturprobleme, Patchfähigkeit, technische Schulden. | gering | beherrschbar | kritisch |
| Wartbarkeit | Änderbarkeit, Testbarkeit, Know-how, Dokumentation. | sehr gut | akzeptabel | schlecht |
| Betriebskosten | Direkte und indirekte Kosten. | niedrig | mittel | hoch/unklar |
| Schnittstellenabhängigkeit | Anzahl, Kritikalität und Instabilität von Schnittstellen. | isoliert | mehrere Abhängigkeiten | viele kritische Abhängigkeiten |
| Datenqualitätsrisiko | Fehler, Dubletten, manuelle Korrektur, unklare Führerschaft. | gering | punktuelle Probleme | strukturelles Risiko |
| Herstellerabhängigkeit | Vendor Lock-in, Support, Exit, Vertragsabhängigkeit. | gering | mittel | hoch |
| Lebenszyklusdruck | Support-Ende, Plattformalter, Vertragsende, Technologieauslauf. | kein Druck | mittelfristiger Druck | akuter Druck |
| Ablösefähigkeit | Realistische Möglichkeit zur Migration oder Stilllegung. Achtung: Hier ist 5 positiv. | kaum ablösbar | mit Aufwand ablösbar | gut ablösbar |

## Gewichtung: Behördengeeigneter Startvorschlag

Nicht jede Dimension zählt gleich stark. In Bundesbehörden sollten fachlicher Wert, Kritikalität, Schutzbedarf, Datenrisiken und Betriebsfähigkeit stärker gewichtet werden als reine Modernitätsästhetik. Die folgende Gewichtung ist ein Startmodell, das du im Architekturboard oder Portfolio-Workshop anpassen kannst.

| Aspekt | Details/Erklärung | Gewicht | Warum dieses Gewicht sinnvoll ist |
|---|---|---:|---|
| Fachlicher Wert | Beitrag zur Verwaltungsleistung. | 15 % | Eine Anwendung mit niedrigem Wert sollte nicht dauerhaft hohe Kosten binden. |
| Kritikalität | Auswirkung bei Ausfall oder Fehler. | 15 % | Kritische Anwendungen benötigen Stabilität, Resilienz und priorisierte Maßnahmen. |
| Schutzbedarf | Vertraulichkeit, Integrität, Verfügbarkeit. | 10 % | Schutzbedarf beeinflusst Architektur, IAM, Betrieb, Logging, Backup und Dienstleisterzugriff. |
| Technisches Risiko | EOL, Architektur, Patchfähigkeit, technische Schulden. | 12 % | Technische Risiken werden sonst zu verdeckten Transformationshindernissen. |
| Wartbarkeit | Änderbarkeit, Testbarkeit, Know-how. | 10 % | Gesetzesänderungen und Verfahrensanpassungen müssen lieferfähig bleiben. |
| Betriebskosten | Laufende Kosten und versteckte Aufwände. | 8 % | Kosten sind wichtig, aber nicht allein entscheidend. |
| Schnittstellenabhängigkeit | Abhängigkeit von Registern, DMS, IAM, Zahlungsverkehr, Reporting. | 8 % | Schnittstellen bestimmen Migrationsreihenfolge und Risiko. |
| Datenqualitätsrisiko | Qualität, Dubletten, führende Systeme, Korrekturaufwand. | 8 % | Schlechte Datenqualität erzeugt falsche Entscheidungen, Bescheide und Berichte. |
| Herstellerabhängigkeit | Vendor Lock-in, Exit-Fähigkeit, Support. | 6 % | Hohe Abhängigkeit begrenzt Verhandlungsmacht und Roadmap-Freiheit. |
| Lebenszyklusdruck | Support-Ende, Vertragsende, Plattformende. | 5 % | Dringlichkeit muss sichtbar werden. |
| Ablösefähigkeit | Realistische Modernisierungs- oder Stilllegungsoption. | 3 % | Wichtig für Roadmap, aber nicht alleiniger Treiber. |

## Konkrete Score-Logik

Du arbeitest mit zwei getrennten Achsen. Das ist entscheidend, weil sonst fachlicher Wert und technisches Risiko in einem Mischwert verschwinden. Für Portfolioentscheidungen brauchst du mindestens diese zwei Scores:

Der **Nutzen-Score** misst fachliche Bedeutung und strategische Relevanz. Eine einfache Formel lautet: `Nutzen = 0,45 × fachlicher Wert + 0,35 × Kritikalität + 0,20 × Nutzer-/Reichweitenrelevanz`.

Der **Risiko-/Modernisierungsdruck-Score** misst Handlungsdruck. Eine einfache Formel lautet: `Druck = 0,20 × Schutzbedarf + 0,20 × technisches Risiko + 0,15 × Wartbarkeitsproblem + 0,10 × Betriebskosten + 0,10 × Schnittstellenabhängigkeit + 0,10 × Datenqualitätsrisiko + 0,08 × Herstellerabhängigkeit + 0,07 × Lebenszyklusdruck`.

Die **Ablösefähigkeit** behandelst du separat. Eine Anwendung kann hohen Modernisierungsdruck haben, aber kurzfristig kaum ablösbar sein. Genau dort entstehen Übergangsarchitekturen: stabilisieren, kapseln, beobachten, Know-how sichern, Schnittstellenvertrag herstellen, Datenbereinigung starten, Zielsystem vorbereiten.

## Portfolio-Matrix: Nutzen gegen Risiko

| Aspekt | Details/Erklärung | Entscheidung | Beispiel |
|---|---|---|---|
| Hoher Nutzen, niedriger Druck | Strategisch relevante und technisch/betrieblich gesunde Anwendung. | Investieren und ausbauen. | Modernes Antragsportal mit guter Architektur und hoher Nutzung. |
| Hoher Nutzen, hoher Druck | Kernanwendung mit erheblichem Risiko. | Priorisiert stabilisieren, modernisieren oder ersetzen. | Zentrales Legacy-Fachverfahren mit EOL-Technologie. |
| Niedriger Nutzen, niedriger Druck | Randanwendung ohne akuten Schmerz. | Tolerieren, konsolidieren oder später prüfen. | Kleine Hilfsanwendung mit wenigen Nutzern und stabiler Technik. |
| Niedriger Nutzen, hoher Druck | Teure oder riskante Anwendung ohne ausreichenden Wert. | Stilllegen, ersetzen oder Funktion in Zielsystem überführen. | Alte Access-Lösung mit personenbezogenen Daten und unklarer Verantwortung. |
| Mittlerer Nutzen, hoher Druck, gute Ablösefähigkeit | Gute Kandidaten für Migration oder Standardisierung. | Migrieren, repurchasen oder konsolidieren. | Altes Reporting-Tool, dessen Funktionen in BI-Plattform überführt werden können. |
| Hoher Nutzen, hoher Druck, schlechte Ablösefähigkeit | Gefährliche Kernabhängigkeit. | Erst stabilisieren und kapseln, dann schrittweise transformieren. | Monolithisches Fachverfahren mit vielen Register- und DMS-Abhängigkeiten. |

## Text-Heatmap für ein Beispielportfolio

Die folgende Heatmap nutzt eine 1–5-Skala. Bei Risiko- und Druckkriterien bedeutet 5: kritisch oder hoch. Bei Wertkriterien bedeutet 5: sehr hoher fachlicher Wert. Das ist wichtig, weil du in Workshops sonst Äpfel und Birnen vergleichst.

| Aspekt | Fachlicher Wert | Kritikalität | Schutzbedarf | Technisches Risiko | Wartbarkeitsproblem | Schnittstellenabhängigkeit | Datenqualitätsrisiko | Herstellerabhängigkeit | Lebenszyklusdruck | Ablösefähigkeit | Portfolioentscheidung |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| A1 Online-Antragsportal | 5 | 4 | 4 | 2 | 2 | 4 | 2 | 2 | 2 | 3 | Investieren und härten |
| A2 Legacy-Fachverfahren Vorgang | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 5 | 2 | Stabilisieren, kapseln, Zielablösung planen |
| A3 Nachweisprüfung Access/Excel | 3 | 3 | 4 | 5 | 5 | 2 | 5 | 1 | 5 | 4 | Schnell ablösen oder in Fachverfahren integrieren |
| A4 DMS/eAkte Standardprodukt | 5 | 5 | 5 | 3 | 3 | 5 | 3 | 5 | 3 | 2 | Strategisch steuern, Exit und Schnittstellen absichern |
| A5 Berichtsdatenmart Leitung | 4 | 3 | 3 | 3 | 3 | 4 | 5 | 2 | 3 | 3 | Datenqualität verbessern, Ziel-BI anbinden |

## Beispielportfolio im Detail

| Aspekt | Details/Erklärung | Beispiel | Entscheidung |
|---|---|---|---|
| A1 Online-Antragsportal | Das Portal nimmt externe Anträge entgegen, führt Nutzer durch Formulare, prüft Eingaben vor und übergibt Antragsdaten an das Fachverfahren. Es hat hohen fachlichen Wert und hohe Außenwirkung, ist technisch aber vergleichsweise gesund. | Hohe Nutzerzahl, hoher Schutzbedarf, mehrere Schnittstellen zu IAM, Fachverfahren und Dokumentupload. | **Investieren.** Barrierefreiheit, Security, Lastfähigkeit, API-Stabilität und Observability stärken. |
| A2 Legacy-Fachverfahren Vorgang | Zentrales System für Vorgangsbearbeitung, Statusführung, Bescheiderstellung und Fachentscheidungen. Technisch stark gealtert, viele Schnittstellen, hohe Kritikalität. | Java-Altversion, Oracle-DB, SOAP-Schnittstellen, wenig Testautomatisierung, hohes Einzelpersonenwissen. | **Stabilisieren und kapseln.** Keine Big-Bang-Ablösung. Erst Schnittstellenverträge, Testharness, Datenlandkarte, Zieldomänen schneiden. |
| A3 Nachweisprüfung Access/Excel | Kleine Schattenanwendung für Nachweisprüfung, entstanden aus fachlicher Not. Fachlich nützlich, aber hochriskant wegen Datenqualität, Datenschutz, fehlender Nachvollziehbarkeit und fehlender Betriebseinbettung. | Lokale Dateiablagen, manuelle Exporte, personenbezogene Nachweisdaten. | **Ablösen.** Funktion kurzfristig in Fachverfahren oder Workflow-Komponente überführen. |
| A4 DMS/eAkte Standardprodukt | Zentrale Komponente für Dokumentablage, Aktenführung, Aufbewahrung und Nachvollziehbarkeit. Hoher fachlicher und regulatorischer Wert, aber starke Hersteller- und Schnittstellenabhängigkeit. | DMS/eAkte als Senke für Bescheide, Nachweise und Kommunikation. | **Strategisch steuern.** Keine übereilte Ablösung; stattdessen Exit-Fähigkeit, Metadatenmodell, Schnittstellenvertrag und Betriebs-SLOs sichern. |
| A5 Berichtsdatenmart Leitung | Liefert Auswertungen für Steuerung, Controlling und Berichtspflichten. Der Nutzen ist hoch, aber Datenqualität und Herkunft sind teilweise unklar. | Daten aus Fachverfahren, Portal, DMS und manuellen Excel-Zulieferungen. | **Datenqualität priorisieren.** Data Lineage, Definitionen, führende Systeme und Qualitätsregeln klären. |

## Roadmap-Entscheidungen aus dem Portfolio ableiten

Die Matrix allein ist noch keine Roadmap. Sie zeigt nur, wo Handlungsdruck liegt. Eine Roadmap entsteht erst, wenn du Abhängigkeiten, Entscheidungsfenster, Budgets, Vergaben, Schutzbedarf, Betriebsfähigkeit und Migrationsfähigkeit einbeziehst.

Für A2, das zentrale Legacy-Fachverfahren, wäre die schlechteste Entscheidung: „Wir ersetzen das System vollständig in einem Großprojekt.“ Fachlich realistischer ist eine Transformationskette: zuerst technische Stabilisierung, dann Schnittstellenkapselung, dann Datenbereinigung, dann fachliche Domänenaufteilung, dann schrittweise Verlagerung einzelner Funktionen. AWS nennt bei Migrationen Strategien wie Rehost, Replatform, Relocate und Retire; für Behördenportfolios solltest du diese technischen Optionen aber immer mit fachlicher Kritikalität, Schutzbedarf und Vergaberealität verbinden. ([docs.aws.amazon.com](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html?utm_source=chatgpt.com))

Eine pragmatische Roadmap könnte so aussehen: In den ersten drei Monaten wird das Portfolio erfasst und validiert. In den Monaten vier bis sechs werden rote Risiken stabilisiert: EOL-Technologien, fehlende Backups, unklare Verantwortlichkeiten, kritische Schnittstellen ohne Vertrag, Schattenanwendungen mit personenbezogenen Daten. In den Monaten sieben bis zwölf werden Zielarchitekturentscheidungen getroffen: welche Funktionen bleiben, welche werden gekapselt, welche werden in Standardprodukte überführt, welche Anwendungen werden abgelöst. Ab dem zweiten Jahr beginnt die Umsetzung in Migrationswellen.

## Entscheidungslogik: Nicht jede rote Anwendung wird sofort abgelöst

| Aspekt | Details/Erklärung | Richtige Entscheidung | Typischer Denkfehler |
|---|---|---|---|
| Hoher Wert und hohes Risiko | Anwendung ist fachlich unverzichtbar, aber technisch gefährdet. | Stabilisieren, absichern, kapseln, Zielablösung vorbereiten. | „Sofort neu bauen.“ |
| Niedriger Wert und hohes Risiko | Anwendung erzeugt mehr Risiko als Nutzen. | Abschalten, konsolidieren oder Funktion migrieren. | „Die läuft doch noch.“ |
| Hoher Wert und niedriger Risiko | Anwendung ist strategischer Baustein. | Investieren, standardisieren, als Zielplattform nutzen. | „Keine Aufmerksamkeit nötig, weil nichts brennt.“ |
| Niedriger Wert und niedriger Risiko | Anwendung ist unauffällig, aber möglicherweise redundant. | Tolerieren, später konsolidieren. | „Alles muss modernisiert werden.“ |
| Hohe Herstellerabhängigkeit | Anwendung ist fachlich wichtig, aber Exit-Fähigkeit fehlt. | Vertrags-, Daten- und Schnittstellenstrategie entwickeln. | „Standardsoftware löst Architekturarbeit automatisch.“ |
| Schlechte Datenqualität | Anwendung liefert widersprüchliche oder unvollständige Daten. | Data Owner, führende Systeme und Qualitätsregeln klären. | „Das ist ein Reportingproblem.“ |

## Typische Fehler bei Applikationsportfolio-Bewertungen

| Aspekt | Details/Erklärung | Beispiel | Korrektur |
|---|---|---|---|
| Alter mit Qualität verwechseln | Das Baujahr sagt wenig über fachlichen Wert, Stabilität oder Risiko. | „Das System ist alt, also muss es weg.“ | Nach Wert, Risiko, Kosten, Schutzbedarf und Zielpassung bewerten. |
| Fachbereich zu spät einbinden | IT bewertet technische Risiken, aber versteht fachlichen Schaden oft nicht vollständig. | Anwendung wird als unkritisch eingestuft, obwohl sie Fristen steuert. | Business Owner, Sachbearbeitung und Fachaufsicht früh einbeziehen. |
| Schatten-IT ignorieren | Excel-, Access- und lokale Tools enthalten oft kritische Datenflüsse. | Nachweise werden außerhalb des Fachverfahrens gepflegt. | Schattenanwendungen explizit erfassen und bewerten. |
| Schnittstellen unterschätzen | Die Anwendung selbst wirkt klein, ist aber Integrationsdrehscheibe. | Kleines Statussystem versorgt Portal, DMS und Reporting. | Schnittstellenabhängigkeit separat bewerten. |
| Datenverantwortung nicht klären | Ohne Data Owner bleibt Datenqualität ein Niemandsthema. | Personendaten weichen zwischen Portal und Fachverfahren ab. | Führende Systeme, Data Owner und Qualitätsregeln festlegen. |
| Kosten zu eng betrachten | Lizenzkosten sind nur ein Teil der Realität. | Billiges System verursacht hohe manuelle Betriebsaufwände. | Total Cost of Ownership erfassen: Betrieb, Störungen, Dienstleister, Change-Aufwand. |
| Herstellerabhängigkeit verharmlosen | Standardsoftware kann strategisch sinnvoll sein, aber Exit-Fähigkeit fehlt häufig. | Kein vollständiger Datenexport, proprietäre Workflows. | Exit-Szenario, Datenmodell, Schnittstellen und Vertragsklauseln prüfen. |
| Schutzbedarf erst am Ende betrachten | Sicherheitsanforderungen verändern Architekturentscheidungen. | Nachträgliche Verschlüsselung, Logging und IAM-Anpassung. | Schutzbedarf früh je Anwendung und Datenobjekt bewerten. |
| Keine Entscheidungsfähigkeit erzeugen | Portfolio wird dokumentiert, aber nicht priorisiert. | 120 Anwendungen im Katalog, keine Roadmap. | Matrix, Heatmap und Entscheidungskategorien erzwingen. |
| Big-Bang-Ablösung planen | Besonders bei Kernverfahren ist vollständiger Ersatz riskant. | Dreijähriges Ablöseprogramm ohne Übergangsarchitektur. | Übergangsarchitekturen, Kapselung, Migrationswellen und Pilotdomänen planen. |

## Interviewfragen für deine Portfolioerhebung

| Aspekt | Details/Erklärung | Beispiel-Fragen |
|---|---|---|
| Fachlicher Zweck | Klärt, warum die Anwendung existiert. | Welche Verwaltungsleistung unterstützt die Anwendung? Welche Aufgabe wäre ohne sie nicht erfüllbar? |
| Kritikalität | Klärt Schaden und Priorität. | Was passiert nach 4 Stunden, 1 Tag, 1 Woche Ausfall? Welche Fristen, Zahlungen oder Bescheide wären betroffen? |
| Nutzer | Klärt Reichweite und Nutzungsmuster. | Wer nutzt die Anwendung? Wie viele aktive Nutzer gibt es? Gibt es externe Nutzer oder technische Konten? |
| Daten | Klärt Datenobjekte und Verantwortlichkeit. | Welche Daten entstehen hier? Welche Daten werden nur gelesen? Für welche Daten ist die Anwendung führend? |
| Schnittstellen | Klärt Abhängigkeiten. | Welche Systeme liefern Daten? Welche Systeme erhalten Daten? Gibt es Schnittstellenverträge? |
| Schutzbedarf | Klärt Sicherheitsarchitektur. | Welche Schäden entstehen bei Offenlegung, Manipulation oder Nichtverfügbarkeit? |
| Betrieb | Klärt Stabilität und Verantwortlichkeiten. | Wer betreibt die Anwendung? Wie wird überwacht? Gibt es Runbooks, SLAs, Notfallverfahren? |
| Wartbarkeit | Klärt Änderungsfähigkeit. | Wie lange dauert eine typische Fachänderung? Gibt es automatisierte Tests? Wer versteht den Code? |
| Kosten | Klärt echte Belastung. | Welche Lizenz-, Betriebs-, Dienstleister- und Change-Kosten entstehen jährlich? |
| Lebenszyklus | Klärt Zeitdruck. | Welche Komponenten laufen aus dem Support? Wann endet der Vertrag? Gibt es Hersteller-Roadmaps? |
| Zielbild | Klärt strategische Passung. | Passt die Anwendung zur Zielarchitektur? Soll sie bleiben, ersetzt, gekapselt oder stillgelegt werden? |

## Praktische Übung mit fünf fiktiven Anwendungen

Du bekommst fünf Anwendungen einer fiktiven Bundesbehörde. Deine Aufgabe ist, für jede Anwendung den Steckbrief grob auszufüllen, die Matrixwerte 1–5 zu vergeben und eine Portfolioentscheidung abzuleiten.

| Aspekt | Details/Erklärung | Fiktive Anwendung |
|---|---|---|
| Anwendung 1 | Zentrales Fachverfahren für Vorgangsbearbeitung, Bescheide und Statusführung. 20 Jahre alt, hohe Nutzung, viele Schnittstellen, kaum Tests, stabiler Betrieb, aber Framework und Datenbank laufen bald aus dem Support. | **VORGANG-Classic** |
| Anwendung 2 | Neues Online-Portal für externe Antragsteller. Gute UX, moderne Technologie, hohe Außenwirkung, aber Monitoring und Fehleranalyse sind noch schwach. | **AntragOnline** |
| Anwendung 3 | Kleine Access-Datenbank in einem Referat zur Nachweisprüfung. Enthält personenbezogene Daten, wird täglich genutzt, ist nicht offiziell betrieben. | **NachweisDesk** |
| Anwendung 4 | Standardprodukt für eAkte/DMS. Zentraler Dokumentenspeicher, teuer, herstellerabhängig, aber fachlich unverzichtbar. | **AktePlus** |
| Anwendung 5 | Berichtssystem für Leitung und Controlling. Nutzt Daten aus mehreren Quellen, aber Kennzahlen sind nicht einheitlich definiert. | **LeitungsBI** |

### Musterlösung

| Aspekt | Fachlicher Wert | Kritikalität | Schutzbedarf | Technisches Risiko | Datenqualitätsrisiko | Ablösefähigkeit | Entscheidung |
|---|---:|---:|---:|---:|---:|---:|---|
| VORGANG-Classic | 5 | 5 | 5 | 5 | 4 | 2 | Nicht sofort ersetzen. Erst stabilisieren, kapseln, Schnittstellen dokumentieren, Testbasis schaffen, Zielablösung in Wellen planen. |
| AntragOnline | 5 | 4 | 4 | 2 | 2 | 3 | Investieren. Observability, Security-Gates, Lasttests, Fehleranalyse und API-Verträge verbessern. |
| NachweisDesk | 3 | 3 | 4 | 5 | 5 | 4 | Kurzfristig ablösen. Daten sichern, Verantwortlichkeit klären, Funktion in offizielles Fachverfahren oder Workflow-Modul überführen. |
| AktePlus | 5 | 5 | 5 | 3 | 3 | 2 | Strategisch behalten, aber Herstellerabhängigkeit, Exit, Metadatenmodell, Schnittstellen und Betriebs-SLOs aktiv steuern. |
| LeitungsBI | 4 | 3 | 3 | 3 | 5 | 3 | Nicht primär technisch modernisieren. Zuerst Kennzahlen, Data Owner, Datenherkunft und Qualitätsregeln klären. |

## Deine Arbeitsmethode in der Praxis

Du gehst in fünf Schritten vor. Im ersten Schritt definierst du den Scope: Welche Organisationseinheit, welche Fachdomänen, welche Anwendungen, welche Plattformdienste, welche Schattenanwendungen werden betrachtet? Im zweiten Schritt erfasst du den Applikationssteckbrief und validierst ihn mit Fachseite, IT-Betrieb, Security, Datenschutz, Architektur und Dienstleister. Im dritten Schritt bewertest du jede Anwendung mit der Matrix. Im vierten Schritt erzeugst du Portfolio-Sichten: Heatmap, Quadrantenmatrix, Kosten-/Risikoblick, Schnittstellenkarte, Lebenszyklusübersicht. Im fünften Schritt leitest du Entscheidungen und Roadmap-Arbeitspakete ab.

Der wichtigste Punkt: Du präsentierst nicht nur Zahlen. Du formulierst entscheidungsreife Aussagen. Nicht: „VORGANG-Classic hat 4,6 Punkte Risiko.“ Sondern: „VORGANG-Classic ist ein fachlich unverzichtbares Kernverfahren mit akutem technischem Lebenszyklusdruck. Eine direkte Ablösung wäre riskant. Empfohlen wird eine zweistufige Transition: 2026 Stabilisierung und Kapselung, 2027 Domänenschnitt und Zielsystementscheidung, ab 2028 Migration in Wellen.“

## Executive-taugliche Formulierungen

| Aspekt | Details/Erklärung | Beispiel |
|---|---|---|
| Risiko ohne Alarmismus | Zeigt Handlungsbedarf, ohne Panik zu erzeugen. | „Das Risiko liegt nicht darin, dass die Anwendung alt ist, sondern darin, dass fachliche Kritikalität, auslaufende Technologie und geringe Änderbarkeit zusammentreffen.“ |
| Wert anerkennen | Verhindert, dass Fachbereiche sich angegriffen fühlen. | „Das Verfahren hat über Jahre zuverlässig Kernleistungen getragen. Genau deshalb müssen wir seine Zukunft jetzt aktiv sichern.“ |
| Roadmap statt Schuldzuweisung | Führt in Umsetzung. | „Wir schlagen keine Sofortablösung vor, sondern eine kontrollierte Übergangsarchitektur mit Stabilisierung, Kapselung und schrittweiser Funktionsmigration.“ |
| Datenqualität sichtbar machen | Hebt Datenrisiken auf Leitungsebene. | „Die Berichtsunsicherheit entsteht nicht im Dashboard, sondern in uneinheitlichen Datenführungen der Quellsysteme.“ |
| Herstellerabhängigkeit sachlich adressieren | Macht Abhängigkeiten steuerbar. | „Das Standardprodukt bleibt strategisch relevant; parallel müssen Exit-Fähigkeit, Datenexport und Schnittstellenhoheit verbessert werden.“ |

## Merksatz für dich als Enterprise Architekt

Eine professionelle Applikationsportfolio-Bewertung beantwortet nicht die Frage, welche Anwendung „modern“ aussieht. Sie beantwortet, welche Anwendung welchen Verwaltungswert liefert, welches Risiko sie trägt, welche Daten sie verantwortet, welche Abhängigkeiten sie erzeugt und welche Zukunftsentscheidung daraus folgt.

Dein Ziel ist nicht, Anwendungen zu verurteilen. Dein Ziel ist, Entscheidungsfähigkeit herzustellen. Genau darin liegt der Unterschied zwischen technischer Bestandsaufnahme und Enterprise Architecture. <>