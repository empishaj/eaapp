## Checkliste: Architektur-Governance in Bundesbehörden sauber aufsetzen

* Prüfe zuerst, welche bestehenden Gremien, Projektprozesse, Sicherheitsprozesse und Beschaffungswege bereits existieren.
* Definiere Architektur-Governance nicht als Zusatzbürokratie, sondern als Entscheidungs- und Entlastungssystem.
* Lege wenige, verbindliche Architekturprinzipien fest, nicht dreißig unverbindliche Leitsätze.
* Übersetze Prinzipien in prüfbare Standards, Review-Fragen und Quality Gates.
* Trenne Beratung, Review, Entscheidung und Eskalation sauber voneinander.
* Verankere ADRs dort, wo Architekturentscheidungen tatsächlich entstehen: im Projekt, nicht nur im Architekturteam.
* Baue Ausnahmeprozesse ein, damit Governance realistisch bleibt und nicht durch Schattenentscheidungen umgangen wird.
* Dokumentiere Entscheidungen mit Kontext, Alternativen, Konsequenzen, Gültigkeit und Wiedervorlage.
* Nutze Architecture Boards nur für risikoreiche, bereichsübergreifende oder standardabweichende Themen.
* Verfolge Maßnahmen sichtbar mit Verantwortlichen, Fristen und Status.
* Miss Governance über Wirkung: weniger Nacharbeit, weniger Sonderlösungen, frühere Risikosichtbarkeit, bessere Wiederverwendung.
* Starte leichtgewichtig und skaliere erst, wenn Komplexität, Risiko oder Schnittstellenzahl steigen.

<>

## 1. Grundverständnis: Architektur-Governance ist kein Kontrollapparat, sondern ein Entscheidungssystem

Architektur-Governance bedeutet im Behördenkontext nicht, dass ein zentrales Architekturteam jedes Diagramm freigibt und jedes Projekt ausbremst. Richtig verstanden ist Governance ein System aus Prinzipien, Standards, Entscheidungswegen, Rollen, Reviews und Nachverfolgung, das Vorhaben früher klärt, vergleichbarer macht und riskante Architekturentscheidungen sichtbar macht, bevor sie teuer werden. Die IT-Architekturrichtlinie Bund beschreibt Architekturvorgaben als Instrument, um IT- und Digitalvorhaben des Bundes grundlegend zu strukturieren und zu steuern; die Nationale IT-Architekturrichtlinie betont systematische, nachvollziehbare und transparente Architekturentscheidungen. Genau das ist der Kern guter Governance: Entscheidungen werden nicht zufällig, personenabhängig oder nachträglich getroffen, sondern nachvollziehbar, wiederverwendbar und prüfbar. ([bmi.bund.de](https://www.bmi.bund.de/SharedDocs/downloads/DE/publikationen/themen/it-digitalpolitik/BMI23033.html?utm_source=chatgpt.com))

Der wichtigste Denkfehler wäre: „Governance = Genehmigung.“ Besser ist: „Governance = klare Spielregeln plus frühe Unterstützung plus dokumentierte Abweichungen.“ In einer Bundesbehörde mit Fachverfahren, Dienstleistern, Datenschutz, Informationssicherheit, Vergabe, Betrieb, Plattformteams und föderalen Schnittstellen braucht Architektur-Governance vor allem drei Dinge: gemeinsame Sprache, belastbare Entscheidungspunkte und eine niedrige Reibung für Projekte.

<>

## 2. Die Bausteine der Architektur-Governance

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Architekturprinzipien | Grundsätzliche Leitlinien, die gewünschtes Architekturverhalten beschreiben. Sie sind absichtlich stabiler als einzelne Technologien. | „Wiederverwendung vor Neubau“, „API-first“, „Security by Design“, „Cloud-/Plattformfähigkeit vor Sonderbetrieb“. | TOGAF beschreibt Enterprise Architecture als Methode und Rahmen zur Entwicklung und Steuerung von Unternehmensarchitekturen. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com)) |
| Standards | Konkrete, prüfbare Festlegungen, die Prinzipien operationalisieren. | „REST APIs werden per OpenAPI spezifiziert“, „IAM-Anbindung erfolgt über zentralen Identity Provider“, „Schnittstellen müssen Monitoring-Metriken liefern“. | XÖV stellt für den Datenaustausch zwischen öffentlichen Verwaltungen Methoden und Produkte bereit. ([it-planungsrat.de](https://www.it-planungsrat.de/produkte-standards/standards?utm_source=chatgpt.com)) |
| Review-Prozesse | Geregelte Architekturprüfungen mit klarer Fragelogik, Vorlagen und Entscheidungspfaden. | Vorstudien-Review, Lösungsdesign-Review, Pre-Go-live-Review. | TOGAF behandelt Architecture Governance und Architecture Compliance als Teil der Architektursteuerung; Compliance Reviews prüfen Vorhaben gegen Architekturvorgaben. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com)) |
| Architekturboard | Entscheidungs- und Eskalationsgremium für relevante Architekturthemen. Nicht jedes Detail gehört dorthin. | Entscheidung über Abweichung vom API-Standard oder über Einführung eines neuen IAM-Patterns. | COBIT trennt Governance und Management über Ziele, Prozesse, Rollen und Informationsflüsse; das ist für Board-Design nützlich. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |
| Entscheidungslog | Übersicht über Architekturentscheidungen, Status, Verantwortliche, Datum, Gültigkeit und Folgen. | „Zentraler API-Gateway wird für externe Schnittstellen verpflichtend.“ | ADR-Praktiken zielen darauf, wichtige Architekturentscheidungen mit Kontext und Konsequenzen festzuhalten. ([adr.github.io](https://adr.github.io/?utm_source=chatgpt.com)) |
| ADRs | Kurze Entscheidungsdokumente für einzelne signifikante Architekturentscheidungen. | „ADR-014: Nutzung von Keycloak-kompatibler OIDC-Anbindung für Fachverfahren X.“ | Michael Nygard popularisierte ADRs 2011 als leichtgewichtige Dokumentation wichtiger Architekturentscheidungen. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Ausnahmeprozesse | Geregelter Umgang mit begründeten Abweichungen von Standards. | Ein Legacy-System darf für zwölf Monate eine abweichende Authentifizierung nutzen, muss aber einen Migrationsplan liefern. | BSI-Grundschutz arbeitet maßnahmen- und risikoorientiert; Abweichungen müssen begründet, bewertet und nachverfolgt werden. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html?utm_source=chatgpt.com)) |
| Quality Gates | Prüfpunkte im Lebenszyklus eines Vorhabens, an denen Mindestanforderungen nachgewiesen werden. | Kein Go-live ohne Betriebsmodell, Logging-Konzept, IAM-Konzept, Datenschutzklärung und Sicherheitsfreigabe. | NIST SSDF empfiehlt u. a. Design-/Architekturreviews zur Prüfung gegen Sicherheitsanforderungen und Risiken. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com)) |
| Rollen und Verantwortlichkeiten | Klare Zuständigkeiten für Erstellung, Review, Entscheidung, Umsetzung und Kontrolle. | Solution Architect erstellt Lösungsarchitektur; Enterprise Architect prüft Passfähigkeit; ISB bewertet Sicherheitsrisiken. | V-Modell XT Bund unterscheidet Projekt- und Organisationsrollen und integriert Informationssicherheitsaspekte in Projektabläufe. ([itzbund.de](https://www.itzbund.de/static/download/Produkte/VMXT/V-Modell-XT-Bund-2.3.pdf?utm_source=chatgpt.com)) |
| Maßnahmenverfolgung | Verbindliche Nachhaltung offener Architekturmaßnahmen. | „OpenAPI-Spezifikation bis 15.07. ergänzen; Owner: Dienstleister; Prüfer: API-Architekt.“ | COBIT betont Governance-/Managementziele, Informationsflüsse und Verantwortlichkeiten als Steuerungsbestandteile. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |

<>

## 3. Das Zielbild: Minimal Viable Architecture Governance

Eine gute Behörden-Governance beginnt nicht mit einem hundertseitigen Handbuch. Sie beginnt mit einem kleinen, verbindlichen Kern. Dieser Kern besteht aus fünf Elementen: erstens einem Satz von acht bis zwölf Architekturprinzipien, zweitens einer Standardlandkarte, drittens einem einfachen Review-Ablauf, viertens einem Architecture Decision Log mit ADRs und fünftens einem geregelten Ausnahmeprozess. Alles Weitere wird erst ergänzt, wenn die Organisation reif genug ist oder die Vorhabenkomplexität es verlangt.

Der zentrale Satz lautet: Jedes Vorhaben muss wissen, welche Architekturentscheidungen es selbst treffen darf, welche es dokumentieren muss, welche es reviewen lassen muss und welche durch ein Board entschieden werden müssen. Damit entlastest du Projekte, weil sie nicht ständig informell fragen müssen: „Dürfen wir das so machen?“ Gleichzeitig entlastest du die Behörde, weil Sonderwege, Sicherheitslücken, Betriebsprobleme und Integrationsrisiken früher sichtbar werden.

<>

## 4. Governance-Operating-Model für eine Bundesbehörde

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Zweck | Architekturentscheidungen sollen nachvollziehbar, wiederverwendbar, sicher, betreibbar und strategiekonform sein. | Fachverfahren werden nicht isoliert modernisiert, sondern entlang gemeinsamer Plattform-, IAM-, Daten- und Schnittstellenstandards. | Die Nationale IT-Architekturrichtlinie betont systematische, nachvollziehbare und transparente Architekturentscheidungen. ([nationale-it-architekturrichtlinie.gov.de](https://nationale-it-architekturrichtlinie.gov.de/?utm_source=chatgpt.com)) |
| Geltungsbereich | Gilt für neue IT-Vorhaben, wesentliche Änderungen, Ausschreibungen, Schnittstellen, Plattformmigrationen und sicherheitsrelevante Änderungen. | Neue Online-Antragsstrecke, Modernisierung eines Legacy-Fachverfahrens, neue Registerschnittstelle. | Die IT-Architekturrichtlinie Bund ist zur Nachnutzung bei Neuentwicklung und Fortschreibung von Architekturvorgaben empfohlen. ([digital.bund.de](https://digital.bund.de/?utm_source=chatgpt.com)) |
| Governance-Ebenen | Strategisch, Portfolio, Solution, Delivery, Betrieb. Jede Ebene hat eigene Entscheidungen und Artefakte. | Strategisch: Plattformstrategie. Solution: Zielbild Fachverfahren. Delivery: konkrete ADRs. Betrieb: Runbook und Observability. | TOGAF strukturiert Architekturarbeit über Architekturdomänen und Governance-/ADM-Logik. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com)) |
| Entscheidungslogik | Entscheidungen werden dort getroffen, wo Kompetenz und Auswirkung zusammenpassen. | Team entscheidet über internes Framework; Board entscheidet über neuen Integrationsstandard. | COBIT beschreibt Governance- und Managementziele inklusive Rollen, Prozesse und Informationsflüsse. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |
| Artefakte | Architektursteckbrief, Kontextdiagramm, Schnittstellenübersicht, Datenklassifikation, IAM-Konzept, Betriebsmodell, ADRs, Ausnahmen, Maßnahmenliste. | Ein Vorhaben liefert vor Review einen 6-seitigen Architektursteckbrief statt 80 Folien. | V-Modell XT Bund arbeitet mit Rollen, Produkten und qualitätssichernden Projektabläufen. ([itzbund.de](https://www.itzbund.de/static/download/Produkte/VMXT/V-Modell-XT-Bund-2.3.pdf?utm_source=chatgpt.com)) |
| Board-Kadenz | Regelmäßig, kurz, entscheidungsorientiert. Empfehlenswert: alle zwei Wochen 60 bis 90 Minuten. | Zwei Entscheidungen, ein Risiko, eine Ausnahme, Maßnahmenkontrolle. | Diese Kadenz ist eine praxiserprobte Ausgestaltung; die Quellen geben Rahmen, nicht diese konkrete Taktung vor. |
| Review-Tiefe | Risikobasiert: kleine Änderungen Self-Check, mittlere Vorhaben Review, hohe Risiken Board. | Nur ein neues internes Batch-Job-Feature braucht keinen Boardtermin; neue Bürgerdaten-Schnittstelle schon. | NIST SSDF fordert risikoorientierte Sicherheits- und Designprüfungen im Entwicklungsprozess. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com)) |
| Erfolgsmessung | Governance wird über Wirkung gemessen, nicht über Anzahl Sitzungen. | Weniger technische Ausnahmen, kürzere Betriebsübergaben, weniger Nacharbeit nach Security Review. | COBIT legt Wert auf Governance-/Managementziele und Zielerreichung. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |

<>

## 5. Die fünf Governance-Ebenen konkret

### 5.1 Strategische Architektur-Governance

Auf strategischer Ebene geht es nicht um einzelne Microservices, sondern um Richtungsentscheidungen: Welche Plattformen werden genutzt? Welche IAM-Zielarchitektur gilt? Welche Integrationsmuster sind verbindlich? Welche Datenräume, Standards und Betriebsmodelle werden bevorzugt? Welche Legacy-Technologien werden abgekündigt? Diese Ebene braucht Anschluss an Behördenleitung, IT-Leitung, Informationssicherheit, Datenschutz, Vergabe und Portfolio-Steuerung.

Typische Entscheidungen sind: „Alle neuen Fachverfahren nutzen zentrale IAM-Föderation“, „Schnittstellen zu anderen Behörden orientieren sich an etablierten Verwaltungsstandards“, „Observability ist Bestandteil der Betriebsfähigkeit“, „Neue Individuallösungen benötigen eine Wiederverwendungsprüfung“. Für föderale und zwischenbehördliche Datenübermittlung sind XÖV, FIM und KoSIT-relevante Standards wichtige Bezugspunkte; XÖV dient der Schaffung einheitlicher Schnittstellen für Datenübermittlung zwischen Behörden und ihren Kundinnen/Kunden beziehungsweise zwischen Behörden. ([it-planungsrat.de](https://www.it-planungsrat.de/produkte-standards/standards?utm_source=chatgpt.com))

### 5.2 Portfolio-Governance

Portfolio-Governance prüft, ob Vorhaben zusammenpassen. Eine Behörde hat oft viele parallele Modernisierungsinitiativen: Fachverfahren A migriert auf eine Plattform, Fachverfahren B baut eine eigene Schnittstellenlogik, Fachverfahren C führt ein separates Benutzerkonto ein, Fachverfahren D kauft eine SaaS-Lösung. Ohne Portfolio-Governance entstehen Mehrfachlösungen. Mit Portfolio-Governance werden Abhängigkeiten, Wiederverwendung, Standardkonformität, Ressourcenengpässe und Entscheidungsfenster sichtbar.

Ein einfacher Portfolio-Check fragt: Nutzt das Vorhaben bestehende Plattformdienste? Erzeugt es neue technische Standards? Berührt es zentrale Datenobjekte? Führt es neue Betriebsanforderungen ein? Verändert es IAM, Schnittstellen, Registerzugriffe, Logging, Archivierung oder Datenschutz? Wenn ja, braucht es frühzeitig Architekturberatung.

### 5.3 Solution-Governance

Solution-Governance prüft das konkrete Lösungskonzept. Hier entstehen Architektursteckbrief, Kontextdiagramm, Schnittstellenliste, Datenmodell, Sicherheitsannahmen, IAM-Konzept, Betriebsmodell, Deployment-Modell und ADRs. Wichtig ist: Solution-Governance muss vor Ausschreibung und vor Implementierungsstart wirken. Wird Architektur erst kurz vor Go-live geprüft, ist sie meist nur noch Schadensbegrenzung.

Eine gute Regel lautet: Kein größeres IT-Vorhaben startet Umsetzung oder Ausschreibung ohne Architektursteckbrief und dokumentierte Kernentscheidungen. Gerade bei Dienstleistern ist das entscheidend, weil Architekturqualität sonst in schöne Präsentationen ausweicht, aber nicht in Liefergegenstände, Standards und Abnahmekriterien übersetzt wird.

### 5.4 Delivery-Governance

Delivery-Governance lebt im Projektalltag. Hier werden ADRs geschrieben, technische Schulden markiert, Standards in Pipelines geprüft, Schnittstellen spezifiziert, Security-Checks integriert und Maßnahmen nachgehalten. Diese Ebene darf nicht vollständig vom zentralen Board abhängig sein, sonst wird sie langsam. Teams müssen viele Entscheidungen selbst treffen dürfen, solange sie innerhalb der Leitplanken bleiben und ihre Entscheidungen dokumentieren.

NIST SSDF ist hier besonders nützlich, weil es sichere Softwareentwicklung als Reihe grundlegender Praktiken beschreibt, darunter Design- und Architekturprüfungen gegen Sicherheitsanforderungen und Risiken. Das passt gut zu Quality Gates, die nicht erst am Ende prüfen, sondern in Analyse, Design, Build und Release integriert werden. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com))

### 5.5 Betriebs-Governance

Betriebs-Governance stellt sicher, dass eine Lösung nicht nur gebaut, sondern auch verantwortbar betrieben werden kann. Sie prüft Monitoring, Logging, Alarmierung, Betriebsdokumentation, Patchbarkeit, Backup/Restore, Berechtigungskonzepte, Notfallverfahren, SLAs/OLAs, Kapazitätsplanung und Übergabe an den Betrieb. Der größte Praxisfehler ist, Betrieb als Nachsatz zu behandeln. In Behörden führt das zu teuren Übergabeproblemen, unklaren Verantwortlichkeiten und langen Stabilisierungsphasen.

<>

## 6. Architekturprinzipien: wenige, scharf formulierte Leitplanken

Architekturprinzipien müssen entscheidungsfähig sein. Ein Prinzip wie „Wir bauen moderne IT“ ist wertlos. Ein gutes Prinzip hat Name, Aussage, Begründung, Konsequenzen und Prüffragen. TOGAF empfiehlt Architekturprinzipien als Teil der Governance- und Architekturarbeit; in der Praxis sollten Behörden lieber wenige starke Prinzipien nutzen als viele dekorative. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com))

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Prinzip 1: Wiederverwendung vor Neubau | Neue Lösungen prüfen zuerst vorhandene Plattformdienste, Standards und Komponenten. | Vor eigenem Dokumentenversand wird geprüft, ob ein zentraler Versanddienst existiert. | IT-Architekturrichtlinien dienen der Abstimmung und Entwicklung von IT-Projekten, Produkten und Organisationen. ([bmds.bund.de](https://bmds.bund.de/themen/digitaler-staat/it-architektur?utm_source=chatgpt.com)) |
| Prinzip 2: API-first | Schnittstellen werden vor Implementierung fachlich und technisch spezifiziert. | OpenAPI-Spezifikation vor Entwicklung; Fehlercodes, Authentifizierung, Versionierung und Monitoring enthalten. | XÖV/FIM unterstützen Standardisierung von Prozessen und Fachdatenstrukturen für automatisierte Datenübermittlung. ([docs.fitko.de](https://docs.fitko.de/fim-xoev/docs/?utm_source=chatgpt.com)) |
| Prinzip 3: IAM zentral vor lokal | Authentifizierung und Autorisierung sollen an zentrale IAM-Vorgaben anschließen. | OIDC/SAML-Anbindung statt lokaler Benutzerverwaltung im Fachverfahren. | BSI-Grundschutz und BSI-Standards bilden eine Basis für Informationssicherheit. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html?utm_source=chatgpt.com)) |
| Prinzip 4: Security by Design | Sicherheitsanforderungen werden im Design berücksichtigt, nicht erst durch Nachprüfung ergänzt. | Threat Modeling und Security Review vor Umsetzung kritischer Schnittstellen. | NIST SSDF empfiehlt Design-/Architekturreviews gegen Sicherheitsanforderungen und Risiken. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com)) |
| Prinzip 5: Observability ist Betriebsfähigkeit | Jede produktive Lösung liefert technische und fachliche Beobachtbarkeit. | Metriken, Logs, Traces, fachliche Events, Alarmregeln und Dashboards. | Diese Ausgestaltung ist eine praktische Ableitung aus Betriebs- und Sicherheitsgovernance; konkrete Tools sind behördenspezifisch. |
| Prinzip 6: Daten sind beherrscht | Datenobjekte, Datenklassifikation, Datenflüsse und Verantwortlichkeiten werden dokumentiert. | Bürgerdaten, Verfahrensdaten, Protokolldaten und Löschfristen werden getrennt betrachtet. | FIM und XÖV fokussieren Prozess- und Fachdatenstrukturen für Verwaltungsverfahren. ([docs.fitko.de](https://docs.fitko.de/fim-xoev/docs/Method_Handlung/?utm_source=chatgpt.com)) |
| Prinzip 7: Plattform vor Sonderbetrieb | Neue Lösungen verwenden bevorzugt standardisierte Plattformdienste. | Containerplattform, zentrale Secrets-Verwaltung, CI/CD, Logging und Monitoring statt individueller Betriebsinseln. | IT-Konsolidierung Bund zielt unter anderem auf Konsolidierung von IT-Lösungen der unmittelbaren Bundesverwaltung. ([itzbund.de](https://www.itzbund.de/DE/digitalemission/itkonsolidierungbund/itkonsolidierungbund.html?utm_source=chatgpt.com)) |
| Prinzip 8: Entscheidungen werden dokumentiert | Signifikante Architekturentscheidungen werden als ADR festgehalten. | „Warum nutzen wir Messaging statt synchroner REST-Kopplung?“ wird dokumentiert. | ADRs dokumentieren wichtige Architekturentscheidungen mit Kontext und Konsequenzen. ([adr.github.io](https://adr.github.io/?utm_source=chatgpt.com)) |

<>

## 7. Standards: Aus Prinzipien werden prüfbare Regeln

Ein Prinzip ist nur der Anfang. Governance wirkt erst, wenn daraus Standards werden. Beispiel: „API-first“ klingt gut, ist aber noch nicht prüfbar. Prüffähig wird es so: „Vor Implementierungsbeginn liegt eine abgestimmte Schnittstellenspezifikation vor. Sie enthält fachliche Ressourcen, Datenobjekte, Authentifizierung, Autorisierung, Fehlercodes, Versionierung, Rate Limits, Protokollierungsanforderungen, Monitoring-Metriken, Testfälle und Deprecation-Regeln.“ Jetzt kann ein Dienstleister liefern, ein Architekt prüfen, ein Projektleiter planen und ein Betriebsteam Anforderungen ableiten.

Für Bundesbehörden solltest du Standards in sechs Domänen strukturieren: Facharchitektur, Datenarchitektur, Anwendungsarchitektur, Integrationsarchitektur, Technologie-/Plattformarchitektur und Sicherheits-/Betriebsarchitektur. Diese Domänensicht ist anschlussfähig an gängige Enterprise-Architecture-Methoden wie TOGAF und zugleich konkret genug für Projektarbeit. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com))

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Fachstandard | Beschreibt Prozesse, Leistungen, fachliche Begriffe, Rollen und Regelwerke. | Einheitliche Fachbegriffe für Antrag, Bescheid, Akte, Vorgang, Nachweis. | FIM stellt standardisierte Informationen zu Verwaltungsleistungen bereit. ([digitale-verwaltung.de](https://www.digitale-verwaltung.de/Webs/DV/DE/aktuelles-service/faq-lexikon/glossar/functions/ozg-lexikon.html?lv2=20339784&lv3=20337916&utm_source=chatgpt.com)) |
| Datenstandard | Beschreibt Datenmodelle, Datenqualität, Klassifikation, Austauschformate, Löschung und Archivierung. | Nutzung eines XÖV-kompatiblen Datenschemas für behördenübergreifenden Austausch. | XÖV liefert Rahmenwerk und Qualitätskriterien für öffentliche IT-Standards. ([it-planungsrat.de](https://www.it-planungsrat.de/produkte-standards/standards?utm_source=chatgpt.com)) |
| Schnittstellenstandard | Beschreibt Protokolle, API-Design, Versionierung, Fehlerbehandlung, Authentifizierung und Monitoring. | REST/OpenAPI für synchrone APIs; Messaging-Pattern für Ereignisse; Standardfehlerformat. | XÖV konzentriert sich auf Datenformate und Schnittstellen der Verwaltung. ([docs.fitko.de](https://docs.fitko.de/kompass/docs/it-landschaft/basisdienste/datenuebermittlung/datenstandards/xoev/?utm_source=chatgpt.com)) |
| IAM-Standard | Beschreibt Identitäten, Rollen, Authentifizierung, Autorisierung, Föderation, technische Nutzer und Rezertifizierung. | Kein lokales Passwortmanagement in neuen Fachverfahren. | BSI-Grundschutz ist zentrale Referenz für Informationssicherheit. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html?utm_source=chatgpt.com)) |
| Plattformstandard | Beschreibt Zielplattformen, Deployment, Secrets, Netzwerkzonen, Laufzeitumgebung und Betriebsübergabe. | Containerisierung nur über freigegebene Plattform-Templates. | IT-Architekturrichtlinien geben Rahmen für Abstimmung und Entwicklung von IT-Lösungen. ([bmds.bund.de](https://bmds.bund.de/themen/digitaler-staat/it-architektur?utm_source=chatgpt.com)) |
| Securitystandard | Beschreibt Schutzbedarf, Threat Modeling, sichere Entwicklung, Schwachstellenmanagement und Freigaben. | Kein Go-live bei offenen kritischen Schwachstellen ohne akzeptierte Ausnahme. | NIST SSDF beschreibt Praktiken zur Reduktion von Software-Schwachstellenrisiken. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com)) |
| Observabilitystandard | Beschreibt Logs, Metriken, Traces, fachliche Ereignisse, Dashboards und Alarmierung. | Jede kritische Schnittstelle liefert Erfolgsrate, Latenz, Fehlerrate und Korrelations-ID. | Diese Standardisierung ist eine praktische Ableitung aus Betriebsfähigkeit; konkrete Vorgaben sind organisationsspezifisch. |

<>

## 8. Review-Ablauf: leichtgewichtig, risikobasiert, entscheidungsorientiert

Der Review-Prozess sollte nicht wie eine Prüfung am Ende wirken. Er muss früh, kurz und hilfreich sein. Das beste Modell ist ein dreistufiger Ansatz: Self-Check für kleine Änderungen, Architekturreview für relevante Vorhaben und Architecture Board für Entscheidungen mit großer Tragweite. Dadurch verhinderst du, dass jedes Thema ins Board gezerrt wird, und stellst gleichzeitig sicher, dass kritische Risiken nicht im Projekt versteckt bleiben.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Schritt 1: Intake | Das Vorhaben meldet sich mit Kurzsteckbrief an. | Name, Ziel, Systeme, Daten, Schnittstellen, Dienstleister, Zeitplan, Risiken. | V-Modell XT Bund nutzt definierte Produkte/Rollen als Projektstrukturierungslogik. ([itzbund.de](https://www.itzbund.de/static/download/Produkte/VMXT/V-Modell-XT-Bund-2.3.pdf?utm_source=chatgpt.com)) |
| Schritt 2: Triage | Architekturteam bewertet Risiko und Review-Tiefe. | Niedrig: Self-Check; Mittel: Review; Hoch: Board. | Risikobasierte Ausgestaltung ist Praxisableitung; NIST SSDF stützt frühe Design-/Sicherheitsreviews. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com)) |
| Schritt 3: Self-Assessment | Projekt beantwortet Standardfragen. | Gibt es personenbezogene Daten? Neue Schnittstellen? Abweichungen von IAM? Neue Plattformkomponenten? | BSI-Grundschutz legt informationssicherheitsbezogene Anforderungen und Maßnahmen nahe. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html?utm_source=chatgpt.com)) |
| Schritt 4: Architekturreview | 60-minütige Prüfung mit Architekt, Security, Betrieb, Datenschutz bei Bedarf. | Architektursteckbrief wird geprüft; Maßnahmen werden festgelegt. | TOGAF Architecture Compliance Reviews prüfen Vorhaben gegen Architekturvorgaben. ([coe.qualiware.com](https://coe.qualiware.com/resources/togaf/9-1/part7-capabilityframework/architecture-compliance/?utm_source=chatgpt.com)) |
| Schritt 5: Entscheidung | Ergebnis: freigegeben, freigegeben mit Auflagen, Wiedervorlage, Board-Entscheidung, abgelehnt. | „Freigabe mit Auflage: IAM-Migrationsplan bis Sprint 5.“ | COBIT unterstützt Governance über Ziele, Prozesse und Verantwortlichkeiten. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |
| Schritt 6: ADR/Decision Log | Relevante Entscheidungen werden dokumentiert. | ADR zu API-Gateway-Nutzung, Datenreplikation oder Plattformausnahme. | ADRs halten Kontext und Konsequenzen signifikanter Entscheidungen fest. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Schritt 7: Maßnahmenverfolgung | Offene Punkte werden nachverfolgt. | Ampelstatus, Owner, Fälligkeitsdatum, Nachweis. | COBIT betont Informationsflüsse, Verantwortlichkeiten und Governance-/Managementziele. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |
| Schritt 8: Gate-Prüfung | Vor Umsetzung, Ausschreibung oder Go-live werden Mindestnachweise geprüft. | Kein Go-live ohne Betriebsmodell, Monitoring, Security-Freigabe und offene Risiken. | NIST SSDF empfiehlt Reviews zur Sicherstellung, dass Design und Architektur Sicherheitsanforderungen erfüllen. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com)) |

<>

## 9. Konkreter Review-Ablauf als Vorlage

### 9.1 Vor dem Review

Das Projekt füllt einen Architektursteckbrief aus. Dieser darf maximal sechs bis acht Seiten haben. Enthalten sein müssen Ziel, Kontext, betroffene Systeme, Daten, Schnittstellen, Nutzergruppen, Betriebsmodell, Sicherheitsannahmen, Plattformbezug, Abhängigkeiten, offene Entscheidungen und bekannte Abweichungen. Wichtig: Der Steckbrief ist kein Folienfriedhof. Er ist das Arbeitsstück für Architekturklärung.

### 9.2 Während des Reviews

Der Review beginnt nicht mit Technologie, sondern mit Zweck und Kontext: Welches fachliche Problem wird gelöst? Welche Systeme werden berührt? Welche Daten fließen? Welche Schnittstellen entstehen? Danach werden Architekturprinzipien und Standards geprüft. Anschließend werden Risiken, Abweichungen und Entscheidungen identifiziert. Das Review endet immer mit einem Ergebnis: Entscheidung, Auflagen, offene Fragen, ADRs und Maßnahmen.

### 9.3 Nach dem Review

Das Projekt erhält ein kurzes Review-Protokoll. Es enthält keine Romanform, sondern fünf Dinge: Entscheidung, Auflagen, offene Risiken, erforderliche ADRs und Maßnahmenliste. Offene Maßnahmen werden nicht in E-Mails begraben, sondern in einem sichtbaren Maßnahmenregister geführt. Bei kritischen Punkten erfolgt eine Wiedervorlage im Board.

<>

## 10. Quality Gates: Wo Governance verbindlich wird

Quality Gates sind die Stellen, an denen aus Empfehlung Verbindlichkeit wird. In Behörden sollten Gates nicht zu spät liegen. Ein Gate kurz vor Produktivsetzung ist wichtig, aber allein zu schwach. Dann sind Architekturfehler bereits teuer. Sinnvoll sind mindestens vier Gates: Vorhabenstart, Ausschreibung/Beauftragung, Umsetzungsstart und Go-live.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Gate 0: Vorhabenidee | Prüft, ob Architekturberatung notwendig ist. | Berührt das Vorhaben zentrale Plattformen, IAM, Daten, Schnittstellen oder Schutzbedarf? | IT-Architekturrichtlinien strukturieren und steuern IT- und Digitalvorhaben. ([bmi.bund.de](https://www.bmi.bund.de/SharedDocs/downloads/DE/publikationen/themen/it-digitalpolitik/BMI23033.html?utm_source=chatgpt.com)) |
| Gate 1: Vor Ausschreibung/Beauftragung | Prüft, ob Architekturvorgaben in Leistungsbeschreibung und Liefergegenstände übersetzt wurden. | OpenAPI, Betriebsmodell, ADRs, Security-Nachweise und Dokumentation als Liefergegenstände. | V-Modell XT Bund ist für strukturierte Projektarbeit mit Produkten und Rollen anschlussfähig. ([itzbund.de](https://www.itzbund.de/static/download/Produkte/VMXT/V-Modell-XT-Bund-2.3.pdf?utm_source=chatgpt.com)) |
| Gate 2: Vor Umsetzungsstart | Prüft, ob Lösungsarchitektur tragfähig ist. | Kontextdiagramm, Datenflüsse, IAM, Schnittstellen, Plattform, Risiken, offene ADRs. | TOGAF Compliance Reviews prüfen Projekte gegen Architekturkriterien und Ziele. ([coe.qualiware.com](https://coe.qualiware.com/resources/togaf/9-1/part7-capabilityframework/architecture-compliance/?utm_source=chatgpt.com)) |
| Gate 3: Vor Integrationstest | Prüft, ob Architekturentscheidungen umgesetzt und testbar sind. | API-Verträge, Auth-Flows, Logging, Fehlerszenarien, Lastannahmen. | NIST SSDF empfiehlt Design-/Architekturreviews gegen Sicherheitsanforderungen und Risiko. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com)) |
| Gate 4: Vor Go-live | Prüft Betriebsfähigkeit, Sicherheit, Datenschutz, Monitoring und Restausnahmen. | Runbook, Dashboards, Alarmierung, Notfallverfahren, offene Risiken akzeptiert. | BSI-Grundschutz und BSI-Standards bilden Referenz für Informationssicherheit. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html?utm_source=chatgpt.com)) |
| Gate 5: Nach Go-live | Prüft Stabilisierung und Lessons Learned. | Architekturmaßnahmen abgeschlossen? Technische Schulden dokumentiert? Betriebskennzahlen stabil? | Diese Nachprüfung ist Praxisableitung aus kontinuierlicher Governance und Maßnahmenverfolgung. |

<>

## 11. Rollenmodell mit Verantwortlichkeiten

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Behörden-/IT-Leitung | Setzt Mandat, Prioritäten und Eskalationsrahmen. | Bestätigt, dass Architekturstandards für neue Vorhaben verbindlich sind. | COBIT trennt Governance und Management und legt Wert auf Zielorientierung. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |
| Chief/Lead Enterprise Architect | Verantwortet Governance-Modell, Architekturprinzipien, Board, Standards und Architektur-Repository. | Führt Architecture Board und entscheidet Triage-Logik. | TOGAF ist ein EA-Framework für Entwicklung und Steuerung von Architekturen. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com)) |
| Enterprise Architect | Bewertet Passfähigkeit zur Zielarchitektur, Roadmap, Standards und Portfolio. | Erkennt, dass drei Vorhaben dieselbe IAM-Funktion bauen wollen. | IT-Architekturrichtlinien fördern passfähige Weiterentwicklung der IT. ([nationale-it-architekturrichtlinie.gov.de](https://nationale-it-architekturrichtlinie.gov.de/?utm_source=chatgpt.com)) |
| Solution Architect | Entwirft konkrete Lösungsarchitektur und erstellt Architektursteckbrief. | Beschreibt Fachverfahren, Schnittstellen, Datenflüsse und Betriebsmodell. | V-Modell XT Bund unterscheidet Projektrollen und Organisationsrollen. ([digitale-verwaltung.de](https://www.digitale-verwaltung.de/Webs/DV/DE/aktuelles-service/V_modell_xt/V_modell_xt_ueberblick/v_modell_xt_ueberblick_node.html?utm_source=chatgpt.com)) |
| Security Architect / ISB | Bewertet Schutzbedarf, Sicherheitsarchitektur, Risiken und Mindestmaßnahmen. | Fordert Threat Modeling für sensible Registerschnittstelle. | BSI-Grundschutz-Kompendium und BSI-Standards sind Basis für Informationssicherheit. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html?utm_source=chatgpt.com)) |
| Datenschutz | Prüft personenbezogene Daten, Zweckbindung, Löschung, Protokollierung und Rechtsgrundlagen. | Bewertet neue Datenübermittlung zwischen Fachverfahren. | Datenschutzprüfung ist behördenspezifisch und muss mit geltendem Datenschutzrecht verzahnt werden; konkrete Rechtsberatung ist separat erforderlich. |
| Data Architect | Prüft Datenmodell, Datenflüsse, Stammdaten, Schnittstellenobjekte und Datenqualität. | Stellt sicher, dass „Person“, „Antrag“ und „Bescheid“ einheitlich modelliert werden. | FIM/XÖV fokussieren Fachdatenstrukturen und Prozesse für Verwaltungsverfahren. ([docs.fitko.de](https://docs.fitko.de/fim-xoev/docs/?utm_source=chatgpt.com)) |
| Platform Architect | Prüft Plattformfähigkeit, Deployment, Laufzeitumgebung, Skalierung, Secrets, Netzwerk und Betriebsintegration. | Bewertet, ob eine Anwendung auf Zielplattform lauffähig und betreibbar ist. | IT-Konsolidierung Bund zielt auf konsolidierte IT-Lösungen in der Bundesverwaltung. ([itzbund.de](https://www.itzbund.de/DE/digitalemission/itkonsolidierungbund/itkonsolidierungbund.html?utm_source=chatgpt.com)) |
| Betriebsverantwortlicher | Prüft Runbook, Monitoring, SLAs/OLAs, Incident-Prozesse, Backup/Restore und Übergabe. | Verhindert Go-live ohne Alarmierung und Supportmodell. | Betriebsfähigkeit ist praktische Governance-Ableitung; konkrete Betriebsprozesse sind organisationsspezifisch. |
| Projekt-/Programmleitung | Plant Reviews, Maßnahmen, Liefergegenstände und Entscheidungsfenster. | Sorgt dafür, dass Architekturauflagen in Sprint-/Meilensteinplanung landen. | V-Modell XT Bund ist auf strukturierte Projektabwicklung mit Rollen und Produkten ausgelegt. ([itzbund.de](https://www.itzbund.de/static/download/Produkte/VMXT/V-Modell-XT-Bund-2.3.pdf?utm_source=chatgpt.com)) |
| Fachseite/Product Owner | Liefert fachlichen Kontext, Prioritäten, Nutzungsfälle und Akzeptanzkriterien. | Klärt, welche fachlichen Daten tatsächlich benötigt werden. | FIM liefert standardisierte Informationen für Verwaltungsleistungen. ([digitale-verwaltung.de](https://www.digitale-verwaltung.de/Webs/DV/DE/aktuelles-service/faq-lexikon/glossar/functions/ozg-lexikon.html?lv2=20339784&lv3=20337916&utm_source=chatgpt.com)) |
| Dienstleister | Liefert Architekturartefakte, Nachweise und Umsetzung gemäß Standards. | Erstellt OpenAPI, ADRs, Betriebsdokumentation, Testnachweise und Security-Fixes. | Governance-Anforderung ist aus Projekt-/Beschaffungssteuerung abzuleiten; Standards müssen vertraglich prüfbar sein. |

<>

## 12. RACI-Matrix für Architektur-Governance

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Architekturprinzipien definieren | Accountable: Lead EA; Responsible: EA-Team; Consulted: Security, Betrieb, Datenschutz, Fachbereiche; Informed: Projekte. | Prinzipienkatalog wird jährlich geprüft. | TOGAF stützt Prinzipien- und Governance-Arbeit. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com)) |
| Architektursteckbrief erstellen | Accountable: Projektleitung; Responsible: Solution Architect; Consulted: EA, Security, Betrieb; Informed: Board bei hoher Relevanz. | Steckbrief vor Gate 1. | V-Modell XT Bund nutzt Rollen-/Produktorientierung. ([itzbund.de](https://www.itzbund.de/static/download/Produkte/VMXT/V-Modell-XT-Bund-2.3.pdf?utm_source=chatgpt.com)) |
| Architekturreview durchführen | Accountable: Lead EA; Responsible: zuständiger EA; Consulted: Security/Data/Platform/Betrieb; Informed: Projekt. | 60-min-Review mit Ergebnisprotokoll. | TOGAF Compliance Review als Referenzlogik. ([coe.qualiware.com](https://coe.qualiware.com/resources/togaf/9-1/part7-capabilityframework/architecture-compliance/?utm_source=chatgpt.com)) |
| ADR erstellen | Accountable: Solution Architect; Responsible: Team/Dienstleister; Consulted: EA; Informed: Board bei Grundsatzentscheidung. | ADR zur Datenreplikation. | ADRs dokumentieren signifikante Architekturentscheidungen. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Ausnahme genehmigen | Accountable: Architecture Board oder delegierter Lead EA; Responsible: Antragsteller; Consulted: Security/Betrieb/Datenschutz; Informed: Portfolio. | 12-monatige Ausnahme für Legacy-Auth. | BSI-/Risikologik stützt begründete, nachverfolgte Abweichungen. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html?utm_source=chatgpt.com)) |
| Maßnahmen schließen | Accountable: Projektleitung; Responsible: jeweiliger Owner; Consulted: EA/Security/Betrieb; Informed: Board. | Nachweis im Maßnahmenregister. | COBIT betont Verantwortlichkeiten und Informationsflüsse. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |

<>

## 13. Architecture Board: Wann es gebraucht wird und wann nicht

Ein Architecture Board ist kein wöchentliches Statusmeeting. Es ist ein Entscheidungs-, Klärungs- und Eskalationsgremium. Es sollte nur Themen behandeln, die eine übergreifende Architekturwirkung haben. Dazu gehören neue Standards, Abweichungen von Standards, kritische Risiken, konkurrierende Zielbilder, Plattformentscheidungen, IAM-Grundsatzfragen, Integrationsmuster, Datenhoheit, technische Schulden mit strategischer Wirkung und Architekturkonflikte zwischen Projekten.

Nicht ins Board gehören reine Implementierungsdetails, lokale Framework-Fragen ohne Außenwirkung, normale Code-Qualitätsfragen, Sprint-Probleme, reine Budgetberichte oder Vorhabenstatus ohne Architekturentscheidung. Wenn ein Board zu viele operative Themen behandelt, verliert es Autorität und Geschwindigkeit.

<>

## 14. Board-Agenda als konkrete Vorlage

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| 1. Eröffnung und Entscheidungsfähigkeit | 5 Minuten: Teilnehmer, Quorum, Ziel der Sitzung. | „Heute zwei Entscheidungen, eine Ausnahme, drei Maßnahmen.“ | Governance-Gremienlogik ist praktische Ausgestaltung auf Basis von COBIT/TOGAF. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com)) |
| 2. Maßnahmenkontrolle | 10 Minuten: offene Maßnahmen, überfällige Punkte, Blocker. | „IAM-Migrationsplan Vorhaben X überfällig.“ | COBIT betont Management- und Informationsflüsse. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |
| 3. Entscheidungsanträge | 30 Minuten: maximal zwei bis drei Entscheidungen. | „Freigabe neuer Integrationspattern für Ereignisverarbeitung.“ | ADR/Decision-Log-Logik stützt nachvollziehbare Entscheidungen. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| 4. Ausnahmeentscheidungen | 15 Minuten: Abweichungen mit Risiko, Dauer, Kompensation, Rückbauplan. | „Temporäre Ausnahme von zentralem IAM bis Q2/2027.“ | BSI-Grundschutz stützt risikoorientierte Bewertung. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html?utm_source=chatgpt.com)) |
| 5. Architektur-Risiken | 10 Minuten: neue rote Risiken aus Reviews. | „Schnittstelle ohne fachliches Datenmodell gefährdet Integrationszeitplan.“ | NIST SSDF unterstützt frühe Risiko-/Designprüfung. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com)) |
| 6. Standards/Prinzipien | 10 Minuten: neue oder geänderte Standards. | „Neuer Mindeststandard für API-Fehlercodes.“ | IT-Architekturrichtlinie und XÖV/FIM stützen Standardisierungslogik. ([it-planungsrat.de](https://www.it-planungsrat.de/produkte-standards/standards?utm_source=chatgpt.com)) |
| 7. Zusammenfassung | 5 Minuten: Entscheidungen, ADRs, Maßnahmen, Wiedervorlagen. | „ADR-022 bis Freitag final; Ausnahme läuft bis 31.12.; Review in 3 Monaten.“ | ADRs schaffen transparente Entscheidungshistorie. ([adr.github.io](https://adr.github.io/?utm_source=chatgpt.com)) |

<>

## 15. Entscheidungslog: Das Gedächtnis der Architektur

Ein Entscheidungslog ist die Übersicht über alle relevanten Architekturentscheidungen. Es ersetzt keine ADRs, sondern referenziert sie. Der Zweck ist einfach: Nach sechs Monaten soll niemand mehr fragen müssen, warum ein bestimmter Weg gewählt wurde, wer entschieden hat, welche Alternativen verworfen wurden und welche Konsequenzen akzeptiert wurden.

### Vorlage: Architecture Decision Log

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Entscheidungs-ID | Eindeutige ID für Nachvollziehbarkeit. | DEC-2026-014 | ADR-Logik: Entscheidungen einzeln referenzierbar machen. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Titel | Kurzer Name der Entscheidung. | „Zentraler API-Gateway für externe Schnittstellen“ | ADRs dokumentieren signifikante Entscheidungen. ([adr.github.io](https://adr.github.io/?utm_source=chatgpt.com)) |
| Status | Vorgeschlagen, entschieden, ersetzt, abgelaufen, widerrufen. | entschieden | ADR-Status ist Kernbestandteil gängiger ADR-Vorlagen. ([adr.github.io](https://adr.github.io/?utm_source=chatgpt.com)) |
| Kontext | Warum ist die Entscheidung nötig? | Mehrere Vorhaben planen eigene externe API-Zugänge. | ADRs halten Kontext und Konsequenzen fest. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Entscheidung | Was wurde beschlossen? | Externe APIs laufen über freigegebenen Gateway-Pattern. | Architecture Governance fordert nachvollziehbare Steuerung. ([nationale-it-architekturrichtlinie.gov.de](https://nationale-it-architekturrichtlinie.gov.de/?utm_source=chatgpt.com)) |
| Alternativen | Welche Optionen wurden geprüft? | Direkte Exposition, projektspezifischer Gateway, zentraler Gateway. | ADRs verbessern Vergleichbarkeit von Entscheidungen. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Konsequenzen | Positive und negative Folgen. | Einheitliche Security; zusätzlicher Onboarding-Aufwand. | ADRs erfassen Konsequenzen explizit. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Owner | Wer verantwortet Entscheidung/Nachpflege? | Lead EA Integration | COBIT betont Verantwortlichkeiten. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |
| Gültigkeit/Wiedervorlage | Wann wird geprüft? | Review nach 12 Monaten | Praktische Governance-Ergänzung. |
| Verknüpfte Artefakte | ADR, Standard, Review, Ausnahme, Maßnahme. | ADR-014, API-Standard v1.2 | Architekturentscheidungen sollen auffindbar und nutzbar sein. |

<>

## 16. ADR-Vorlage für Behördenvorhaben

Ein ADR sollte kurz sein. Zwei Seiten reichen in den meisten Fällen. Der Fehler vieler Organisationen besteht darin, ADRs zu schwer zu machen. Dann schreibt sie niemand. Ein ADR ist kein Gutachten, sondern eine nachvollziehbare Architekturentscheidung.

### Vorlage: Architecture Decision Record

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Titel | Eine Entscheidung, nicht ein Thema. | „ADR-017: Nutzung zentraler IAM-Föderation für Fachverfahren AntragOnline“ | Nygard beschreibt ADRs für einzelne signifikante Entscheidungen. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Status | Vorgeschlagen, akzeptiert, ersetzt, verworfen. | akzeptiert | ADR-Grundstruktur. ([adr.github.io](https://adr.github.io/?utm_source=chatgpt.com)) |
| Datum | Entscheidungsdatum. | 13.06.2026 | Praktische Nachvollziehbarkeit. |
| Kontext | Ausgangslage, Problem, Rahmenbedingungen. | Das Fachverfahren benötigt Authentifizierung für interne Nutzer und externe Dienstleister. | ADRs dokumentieren Kontext. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Entscheidungsbedarf | Welche Frage wird entschieden? | Soll lokale Benutzerverwaltung oder zentrale IAM-Anbindung genutzt werden? | ADRs fokussieren auf Entscheidung. |
| Optionen | Realistische Alternativen. | Lokale Nutzerverwaltung, zentrale IAM-Föderation, temporäre Hybridlösung. | ADRs machen Alternativen sichtbar. |
| Entscheidung | Klare Auswahl. | Zentrale IAM-Föderation wird genutzt. | ADR-Kern. |
| Begründung | Warum diese Option? | Einheitliche Zugriffskontrolle, weniger Betriebsrisiko, bessere Rezertifizierung. | BSI-/Security-Governance stützt kontrollierte Zugriffskonzepte. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html?utm_source=chatgpt.com)) |
| Konsequenzen | Folgen, Risiken, Kosten, Einschränkungen. | Onboarding-Aufwand; Abhängigkeit vom zentralen IAM-Team; lokale Sonderrollen müssen migriert werden. | ADRs erfassen Konsequenzen. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Maßnahmen | Was ist umzusetzen? | Rollenmodell bis Sprint 3, Testnutzer bis Sprint 4, Security Review vor Integrationstest. | Maßnahmenverfolgung als Governance-Praxis. |
| Wiedervorlage | Wann wird geprüft? | Nach Pilotbetrieb oder bei IAM-Standardänderung. | Praktische Governance-Ergänzung. |

<>

## 17. Ausnahmeprozess: Abweichungen erlauben, aber beherrscht

Ohne Ausnahmeprozess wird Governance entweder unrealistisch oder unehrlich. In Behörden gibt es Legacy-Systeme, Haushaltsjahre, Vergabegrenzen, laufende Verträge, politische Termine, Datenschutzauflagen, Betriebsrestriktionen und technische Abhängigkeiten. Deshalb darf eine Abweichung möglich sein. Aber sie muss sichtbar, begründet, befristet, kompensiert und rückführbar sein.

Eine Ausnahme ist keine stille Erlaubnis, Standards zu ignorieren. Sie ist eine bewusst akzeptierte Abweichung mit Risikoakzeptanz und Rückbauplan.

### Ausnahmeformular als Vorlage

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Antragsteller | Wer beantragt die Ausnahme? | Projektleitung Fachverfahren X | COBIT betont Verantwortlichkeiten. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |
| Betroffener Standard | Gegen welche Vorgabe wird abgewichen? | IAM-Standard v2.1: zentrale Authentifizierung verpflichtend. | Architekturvorgaben sollen eigenverantwortlich eingehalten werden. ([nationale-it-architekturrichtlinie.gov.de](https://nationale-it-architekturrichtlinie.gov.de/?utm_source=chatgpt.com)) |
| Beschreibung der Abweichung | Was wird anders gemacht? | Für externe Nutzer wird für sechs Monate lokale Authentifizierung genutzt. | Governance braucht explizite Abweichungstransparenz. |
| Begründung | Warum ist Standardkonformität aktuell nicht möglich? | Bestehender Dienstleistervertrag, fehlende Schnittstelle im Altsystem, gesetzter Pilottermin. | Praktische Behördenrealität; rechtliche/vertragliche Details separat prüfen. |
| Risiko | Welche Risiken entstehen? | Uneinheitliche Zugriffskontrolle, erhöhter Rezertifizierungsaufwand, zusätzlicher Betriebsprozess. | BSI-Grundschutz unterstützt risikoorientierte Sicherheitsbewertung. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html?utm_source=chatgpt.com)) |
| Kompensationsmaßnahmen | Wie wird Risiko reduziert? | Starke Passwortregeln, Protokollierung, manuelle Rezertifizierung, eingeschränkter Nutzerkreis. | NIST SSDF unterstützt risikomindernde Sicherheitspraktiken im SDLC. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com)) |
| Laufzeit | Bis wann gilt die Ausnahme? | Bis 31.12.2026 | Befristung verhindert dauerhafte Schattenstandards. |
| Rückbau-/Migrationsplan | Wie wird Standardkonformität hergestellt? | IAM-Migration in Release 2; Schnittstellenbereitstellung bis 15.11.2026. | Maßnahmenverfolgung ist Governance-Kern. |
| Entscheider | Wer akzeptiert die Ausnahme? | Architecture Board plus ISB bei Sicherheitsrelevanz. | Board-/Governance-Ausgestaltung aus TOGAF/COBIT ableitbar. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com)) |
| Wiedervorlage | Wann wird geprüft? | Monatlich im Maßnahmenregister, Board nach drei Monaten. | Praktische Governance-Ergänzung. |
| Ergebnis | Genehmigt, genehmigt mit Auflagen, abgelehnt. | Genehmigt mit Auflagen. | Entscheidungslogik. |

<>

## 18. Maßnahmenverfolgung: Der unterschätzte Kern der Governance

Viele Governance-Modelle scheitern nicht an schlechten Prinzipien, sondern an fehlender Nachverfolgung. Ein Review ohne Maßnahmenregister ist oft nur ein Gespräch. Ein Board ohne offene Punkte ist oft nur eine Bühne. Wirkliche Steuerung entsteht erst, wenn jede Auflage einen Owner, ein Fälligkeitsdatum, einen Nachweis und einen Status hat.

### Maßnahmenregister als Vorlage

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Maßnahme-ID | Eindeutige Nummer. | ARCH-ACT-2026-031 | COBIT betont steuerbare Informationsflüsse. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |
| Ursprung | Review, Board, Ausnahme, Gate, Audit. | Architekturreview Gate 2 | Governance-Nachvollziehbarkeit. |
| Beschreibung | Konkrete Aufgabe. | OpenAPI-Spezifikation um Fehlercodes und Auth-Flows ergänzen. | API-first operationalisieren. |
| Owner | Verantwortliche Person oder Rolle. | Solution Architect Dienstleister | Verantwortlichkeit verhindert Diffusion. |
| Prüfer | Wer nimmt ab? | API Architect Behörde | Trennung von Umsetzung und Prüfung. |
| Fälligkeit | Klares Datum. | 30.06.2026 | Steuerbarkeit. |
| Status | Offen, in Arbeit, blockiert, erledigt, akzeptierte Ausnahme. | in Arbeit | Transparenz. |
| Nachweis | Konkretes Artefakt. | Link zur OpenAPI v1.1 und Review-Kommentar. | Prüfbarkeit. |
| Risiko bei Nichtumsetzung | Konsequenz. | Integrationsrisiko im Systemtest. | Risikosichtbarkeit. |

<>

## 19. Wie Governance als Entlastung wirkt

Governance wirkt entlastend, wenn sie Projekte vor späten Überraschungen schützt. Ohne Governance baut ein Dienstleister vielleicht eine Lösung, die technisch funktioniert, aber nicht zum IAM passt, keine brauchbaren Betriebsmetriken liefert, Datenmodelle uneinheitlich interpretiert oder Schnittstellen ohne Versionierung bereitstellt. Das wird dann in Security Review, Betriebseinführung, Datenschutzprüfung oder Integrationstest teuer. Mit Governance werden diese Punkte früh sichtbar.

Die Entlastungslogik kannst du so kommunizieren: „Wir prüfen nicht, um euch aufzuhalten. Wir prüfen, damit ihr nicht drei Monate später umbauen müsst.“ Das ist ein entscheidender Satz. Er verändert die Wahrnehmung. Architektur-Governance ist dann keine Instanz, die Nein sagt, sondern ein System, das teure Nacharbeit verhindert.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Weniger Nacharbeit | Standards und Reviews klären Anforderungen vor Implementierung. | IAM-Anbindung wird vor Entwicklung festgelegt, nicht nach Abnahmetest. | NIST SSDF stützt frühe Design-/Architekturreviews. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com)) |
| Bessere Vergleichbarkeit | Vorhaben nutzen gleiche Steckbriefe, Prinzipien und Reviewfragen. | Zwei Fachverfahren können bezüglich Daten, Schnittstellen und Betrieb verglichen werden. | IT-Architekturrichtlinie fördert transparente Architekturentscheidungen. ([nationale-it-architekturrichtlinie.gov.de](https://nationale-it-architekturrichtlinie.gov.de/?utm_source=chatgpt.com)) |
| Frühere Risikosichtbarkeit | Risiken werden in Intake, Review und Gate sichtbar. | Datenschutzrisiko bei Protokolldaten wird vor Ausschreibung erkannt. | BSI-Grundschutz unterstützt risikoorientierte Informationssicherheit. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html?utm_source=chatgpt.com)) |
| Nachvollziehbare Entscheidungen | ADRs und Decision Logs verhindern Wissensverlust. | Nach Personalwechsel ist klar, warum Messaging gewählt wurde. | ADRs halten Kontext und Konsequenzen fest. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Bessere Dienstleistersteuerung | Architekturqualität wird Liefergegenstand und Abnahmekriterium. | Dienstleister liefert OpenAPI, ADRs, Runbook und Security-Nachweise. | V-Modell XT Bund stützt produkt- und rollenorientierte Projektsteuerung. ([itzbund.de](https://www.itzbund.de/static/download/Produkte/VMXT/V-Modell-XT-Bund-2.3.pdf?utm_source=chatgpt.com)) |
| Reduzierte Sonderlösungen | Ausnahmeprozess macht Abweichungen sichtbar und befristet. | Legacy-Ausnahme läuft nicht unbemerkt in Dauerbetrieb. | Governance-/Risikologik aus COBIT/BSI ableitbar. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |

<>

## 20. Typische Fehler beim Aufbau von Architektur-Governance

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Zu viel Governance am Anfang | Ein schweres Modell wird eingeführt, bevor die Organisation die Grundartefakte beherrscht. | 40-seitige Review-Vorlage, die niemand ausfüllt. | Leichtgewichtige ADRs sind als Gegenmodell hilfreich. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Board als Statusmeeting | Das Board hört Projektberichte, trifft aber keine Architekturentscheidungen. | 90 Minuten Folien, null Entscheidungen. | TOGAF/COBIT stützen entscheidungs- und steuerungsorientierte Governance. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com)) |
| Prinzipien ohne Prüfbarkeit | Leitlinien klingen gut, erzeugen aber keine Review-Fragen. | „Modularität ist wichtig“ ohne Kriterien. | Architekturprinzipien müssen operationalisiert werden; TOGAF liefert Rahmen. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com)) |
| Reviews zu spät | Architektur wird erst kurz vor Go-live geprüft. | Security findet fehlendes IAM-Konzept nach fast fertiger Umsetzung. | NIST SSDF empfiehlt Design-/Architekturprüfung im Entwicklungsprozess. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com)) |
| Keine Ausnahmeprozesse | Projekte umgehen Standards informell. | „Das machen wir nur dieses eine Mal“ wird Dauerlösung. | BSI-/Risikologik verlangt transparente Risikobehandlung. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html?utm_source=chatgpt.com)) |
| Keine Maßnahmenverfolgung | Review-Ergebnisse verschwinden in Protokollen. | Offene Logging-Anforderung wird erst im Betrieb wiederentdeckt. | COBIT betont Verantwortlichkeiten und Informationsflüsse. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |
| Architektur isoliert von Vergabe | Vorgaben stehen nicht in Leistungsbeschreibung und Vertrag. | Dienstleister liefert Code, aber keine ADRs, keine Betriebskonzepte, keine API-Nachweise. | V-Modell XT Bund ist mit Lieferprodukten und Rollen anschlussfähig. ([itzbund.de](https://www.itzbund.de/static/download/Produkte/VMXT/V-Modell-XT-Bund-2.3.pdf?utm_source=chatgpt.com)) |
| Zu technische Governance | Fachliche Begriffe, Daten, Prozesse und Rechtskontext werden ignoriert. | Technisch saubere API, aber falsches fachliches Datenmodell. | FIM/XÖV adressieren Prozess- und Fachdatenstrukturen. ([docs.fitko.de](https://docs.fitko.de/fim-xoev/docs/?utm_source=chatgpt.com)) |
| Keine Management-Rückendeckung | Architekturteam empfiehlt, aber niemand muss folgen. | Standards sind „nice to have“. | COBIT macht Governance-Ziele und Verantwortlichkeit explizit. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |
| Governance als Personenmacht | Entscheidungen hängen an einzelnen starken Architekten statt an nachvollziehbaren Regeln. | „Weil Herr X das so will“ statt ADR und Standard. | Nationale IT-Architekturrichtlinie betont nachvollziehbare und transparente Entscheidungen. ([nationale-it-architekturrichtlinie.gov.de](https://nationale-it-architekturrichtlinie.gov.de/?utm_source=chatgpt.com)) |

<>

## 21. Konkretes leichtgewichtiges Governance-Modell für deinen Start

Für deinen Einstieg als Enterprise Architekt in einem Bundesbehördenumfeld würde ich mit einem 90-Tage-Modell arbeiten. Ziel ist nicht, sofort die perfekte Governance zu bauen. Ziel ist, innerhalb von drei Monaten eine nutzbare Architektursteuerung zu etablieren, die bestehende Gremien ergänzt und nicht ersetzt.

### Phase 1: Verstehen und Andocken

In den ersten drei bis vier Wochen klärst du bestehende Prozesse: Welche Projektgremien gibt es? Wo werden IT-Entscheidungen getroffen? Wer ist für Informationssicherheit zuständig? Wer verantwortet Datenschutz? Wie laufen Ausschreibungen? Wer entscheidet über Plattformen? Wo liegen Architekturartefakte? Welche Standards sind bereits verbindlich? Welche Vorhaben sind kritisch? Welche Reviews existieren schon?

Das Ergebnis dieser Phase ist eine Governance-Landkarte: Gremien, Rollen, Artefakte, Entscheidungspunkte, Schmerzpunkte. Du vermeidest damit den klassischen Fehler, ein neues Governance-Modell neben die Organisation zu stellen. Stattdessen integrierst du dich in bestehende Entscheidungswege.

### Phase 2: Minimalstandard definieren

In Woche fünf bis acht definierst du den Governance-Kern: acht bis zwölf Architekturprinzipien, einen Architektursteckbrief, einen Review-Ablauf, ein ADR-Template, ein Ausnahmeformular und ein Maßnahmenregister. Außerdem definierst du Triage-Kriterien: Wann reicht Self-Check? Wann braucht es Review? Wann braucht es Board?

Das Ergebnis dieser Phase ist ein „Architecture Governance Starter Kit“. Es sollte so schlank sein, dass Projektleitungen es akzeptieren, aber so verbindlich, dass Architekturentscheidungen steuerbar werden.

### Phase 3: Pilotieren und schärfen

In Woche neun bis zwölf wendest du das Modell auf zwei bis drei echte Vorhaben an. Idealerweise wählst du unterschiedliche Fälle: ein Legacy-Modernisierungsvorhaben, eine neue Schnittstelle und eine Plattform-/IAM-relevante Änderung. Danach passt du Vorlagen, Fragen und Board-Logik an. Governance muss aus echter Anwendung lernen.

Das Ergebnis dieser Phase ist ein validiertes Operating Model mit belastbaren Beispielen, nicht nur ein Konzeptpapier.

<>

## 22. Dein Governance-Operating-Model als kompakte Zielstruktur

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Name | Lightweight Architecture Governance | „LAG-Bund v1.0“ | Eigene Modellierung auf Basis TOGAF/COBIT/BSI/V-Modell. |
| Ziel | Frühere Architekturklärung, weniger Nacharbeit, nachvollziehbare Entscheidungen. | Reviews vor Ausschreibung und Umsetzung. | IT-Architekturrichtlinie: systematische und transparente Entscheidungen. ([nationale-it-architekturrichtlinie.gov.de](https://nationale-it-architekturrichtlinie.gov.de/?utm_source=chatgpt.com)) |
| Scope | Neue Vorhaben, wesentliche Änderungen, Schnittstellen, Plattform, IAM, Daten, Security, Betrieb. | Modernisierung eines Fachverfahrens. | IT-Architekturrichtlinie Bund für Neuentwicklung/Fortschreibung. ([digital.bund.de](https://digital.bund.de/?utm_source=chatgpt.com)) |
| Prinzipien | 8–12 verbindliche Leitplanken. | API-first, IAM zentral, Plattform vor Sonderbetrieb. | TOGAF als EA- und Governance-Rahmen. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com)) |
| Standards | Prüffähige Mindestanforderungen je Domäne. | API-, IAM-, Daten-, Security-, Observability-Standard. | XÖV/FIM/BSI als wichtige Referenzpunkte. ([it-planungsrat.de](https://www.it-planungsrat.de/produkte-standards/standards?utm_source=chatgpt.com)) |
| Review | Risikobasierter Ablauf mit Self-Check, Review und Board. | Kritische Bürgerdaten-Schnittstelle geht ins Board. | NIST SSDF und TOGAF stützen frühe Reviews/Compliance. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com)) |
| Board | Entscheidet Standards, Ausnahmen, Konflikte und hohe Risiken. | Ausnahme von IAM-Standard. | COBIT/TOGAF stützen Governance-Gremienlogik. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |
| ADRs | Dokumentieren signifikante Architekturentscheidungen. | ADR zu Datenreplikation. | Nygard ADR. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Ausnahmen | Befristet, begründet, risikobewertet, kompensiert. | Legacy-Ausnahme mit Rückbauplan. | BSI-/Risikologik. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html?utm_source=chatgpt.com)) |
| Gates | Vorhabenstart, Ausschreibung, Umsetzung, Integration, Go-live. | Kein Go-live ohne Betriebs- und Security-Nachweise. | V-Modell XT Bund und NIST SSDF als Anschlusslogik. ([itzbund.de](https://www.itzbund.de/static/download/Produkte/VMXT/V-Modell-XT-Bund-2.3.pdf?utm_source=chatgpt.com)) |
| Metriken | Durchlaufzeit, offene Risiken, Ausnahmen, Nacharbeit, Wiederverwendung, Gate-Failures. | Anzahl überfälliger Architekturmaßnahmen sinkt pro Quartal. | COBIT unterstützt Ziel-/Steuerungslogik. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |

<>

## 23. Metriken: Woran du erkennst, ob Governance funktioniert

Miss nicht, wie viele Reviews du durchgeführt hast. Das ist Aktivität, nicht Wirkung. Gute Governance misst, ob die Organisation bessere Architekturentscheidungen trifft und weniger Reibung erzeugt.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Frühindikator: Review-Zeitpunkt | Anteil der Vorhaben, die vor Ausschreibung/Umsetzungsstart reviewt wurden. | Ziel: 80 % der relevanten Vorhaben vor Gate 1. | Frühe Designprüfung entspricht NIST-SSDF-Logik. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com)) |
| Nacharbeitsquote | Architekturauflagen nach Go-live oder kurz vor Go-live. | Ziel: sinkende Anzahl später Architekturauflagen. | Praktische Wirkungsmessung. |
| Ausnahmen | Anzahl, Dauer und Überfälligkeit von Ausnahmen. | Ziel: keine unbefristeten Ausnahmen. | Risikoorientierte Governance aus BSI/COBIT ableitbar. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html?utm_source=chatgpt.com)) |
| Standardnutzung | Anteil neuer Vorhaben mit Standard-IAM, Standard-API, Standard-Plattform. | Ziel: 90 % IAM-Standardkonformität bei neuen Vorhaben. | IT-Architekturrichtlinie/XÖV stützen Standardisierung. ([nationale-it-architekturrichtlinie.gov.de](https://nationale-it-architekturrichtlinie.gov.de/?utm_source=chatgpt.com)) |
| ADR-Abdeckung | Anteil signifikanter Entscheidungen mit ADR. | Ziel: jede Board-Entscheidung hat ADR oder Decision-Log-Eintrag. | ADRs dokumentieren signifikante Entscheidungen. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Maßnahmenalter | Durchschnittliches Alter offener Architekturmaßnahmen. | Ziel: keine roten Maßnahmen älter als 30 Tage ohne Eskalation. | COBIT-Zielsteuerung als Referenz. ([isaca.org](https://www.isaca.org/resources/cobit?utm_source=chatgpt.com)) |
| Betriebsübergabequalität | Anzahl fehlender Betriebsartefakte bei Go-live. | Ziel: Runbook, Monitoring und Alarmierung vollständig. | Praktische Betriebs-Governance. |

<>

## 24. Beispiel: Governance für Modernisierung eines Fachverfahrens

Nehmen wir eine Bundesbehörde, die ein altes Fachverfahren modernisiert. Das Verfahren soll auf eine Plattform migrieren, zentrale IAM-Anbindung nutzen, Schnittstellen standardisieren und Observability verbessern.

Im Intake erkennt die Architektur-Triage: Das Vorhaben ist hoch relevant, weil personenbezogene Daten verarbeitet werden, mehrere Schnittstellen betroffen sind, IAM geändert wird und Betrieb auf einer neuen Plattform geplant ist. Es braucht also kein Self-Check-only, sondern ein vollständiges Architekturreview plus Board-Entscheidungen für zwei Punkte: IAM-Übergangsarchitektur und Integrationsstandard.

Im ersten Review stellt sich heraus: Das Altsystem kann den zentralen IAM-Standard noch nicht vollständig unterstützen. Die Governance blockiert jetzt nicht pauschal. Stattdessen wird eine Ausnahme beantragt. Die Ausnahme gilt befristet für neun Monate, enthält Kompensationsmaßnahmen, eine manuelle Rezertifizierung, Protokollierung und einen Migrationsplan. Parallel wird ein ADR geschrieben: „ADR-021: Temporäre Hybrid-IAM-Architektur für Fachverfahren X“. Das Board akzeptiert die Ausnahme mit Auflagen.

Für Schnittstellen wird eine andere Entscheidung getroffen: Neue Schnittstellen müssen sofort nach API-Standard spezifiziert werden. Legacy-Schnittstellen dürfen im Übergang bestehen, müssen aber im Schnittstellenregister markiert und in die Roadmap aufgenommen werden. Damit entsteht kein Big Bang, aber auch keine unsichtbare Daueraltlast.

Für Observability wird ein Gate gesetzt: Kein Go-live ohne technische Metriken, strukturierte Logs, Korrelations-ID, fachliche Erfolgskennzahlen und Alarmierung für kritische Fehler. Das ist keine Zusatzbürokratie, sondern verhindert den typischen Zustand: „Das System ist live, aber niemand sieht, warum Vorgänge fehlschlagen.“

<>

## 25. Übung: Baue dein eigenes leichtgewichtiges Governance-Modell

### Ausgangslage

Eine Bundesbehörde betreibt fünf Legacy-Fachverfahren. Zwei davon sollen modernisiert werden. Ein neues Online-Verfahren wird ausgeschrieben. Es gibt bereits ein IT-Sicherheitsgremium, eine Projektlenkung, ein Datenschutzreview und ein Betriebsübergabeformular. Es gibt aber kein Architekturboard, keine verbindlichen ADRs, keine einheitlichen Review-Fragen und keine saubere Nachverfolgung von Architekturauflagen.

### Aufgabe 1: Governance-Landkarte erstellen

Beschreibe auf einer Seite, welche bestehenden Gremien und Prozesse du nutzt. Markiere, wo Architekturentscheidungen heute vermutlich entstehen: Projektstart, Ausschreibung, Dienstleisterdesign, Security Review, Betriebseinführung, Lenkungskreis. Dein Ziel ist, keine neue Parallelbürokratie zu bauen, sondern Architektur an vorhandene Punkte anzudocken.

### Aufgabe 2: Triage-Regeln formulieren

Definiere fünf Kriterien, die ein Vorhaben reviewpflichtig machen. Gute Kriterien wären: neue oder geänderte Schnittstellen, personenbezogene oder besonders schutzwürdige Daten, Abweichung von IAM-/Plattformstandard, neuer externer Dienstleister, neue Betriebsanforderungen, hohe Verfügbarkeit, behördenübergreifender Datenaustausch.

### Aufgabe 3: Drei Architekturprinzipien operationalisieren

Nimm drei Prinzipien: „API-first“, „IAM zentral“, „Observability ist Betriebsfähigkeit“. Formuliere je Prinzip drei prüfbare Review-Fragen. Beispiel für API-first: Liegt eine Schnittstellenspezifikation vor? Sind Authentifizierung, Fehlercodes und Versionierung beschrieben? Gibt es Testfälle und Monitoring-Anforderungen?

### Aufgabe 4: Board-Agenda bauen

Erstelle eine 60-minütige Agenda für das erste Architecture Board. Begrenze dich auf drei Themen: eine Standardentscheidung, eine Ausnahme und eine rote Architekturmaßnahme. Schreibe zu jedem Thema, welche Entscheidung erwartet wird.

### Aufgabe 5: Einen ADR schreiben

Schreibe einen ADR zur Frage: „Soll das neue Online-Verfahren eine lokale Benutzerverwaltung nutzen oder an das zentrale IAM angebunden werden?“ Nutze die Felder Status, Kontext, Optionen, Entscheidung, Konsequenzen und Maßnahmen.

### Aufgabe 6: Ausnahmeformular ausfüllen

Formuliere eine befristete Ausnahme für ein Legacy-Fachverfahren, das den zentralen IAM-Standard erst in neun Monaten erfüllen kann. Beschreibe Risiko, Kompensation, Laufzeit, Rückbauplan, Owner und Wiedervorlage.

### Musterlösung in Kurzform

Ein gutes Ergebnis wäre: Das bestehende IT-Sicherheitsgremium bleibt für Sicherheitsfreigaben zuständig, der Lenkungskreis bleibt für Budget und Prioritäten zuständig, das neue Architecture Board entscheidet nur Architekturstandards, Ausnahmen und bereichsübergreifende Konflikte. Reviews werden vor Ausschreibung und vor Umsetzungsstart durchgeführt. ADRs werden durch Solution Architects erstellt und durch Enterprise Architects geprüft. Ausnahmen werden befristet und im Maßnahmenregister verfolgt. Damit passt Governance in bestehende Prozesse und erzeugt trotzdem neue Klarheit.

<>

## 26. Dein praktischer Merksatz für Executive-Kommunikation

Architektur-Governance in einer Bundesbehörde verkaufst du nicht mit „Wir brauchen ein Board“. Du sagst besser:

„Wir schaffen einen leichten Entscheidungsrahmen, damit Vorhaben früher wissen, welche Standards gelten, welche Abweichungen zulässig sind, welche Risiken sichtbar werden und welche Entscheidungen später noch nachvollziehbar sein müssen. Dadurch reduzieren wir Nacharbeit, Betriebsrisiken und Sonderlösungen.“

Das ist die richtige Tonlage. Nicht Kontrollanspruch. Nicht Framework-Eitelkeit. Sondern Entlastung, Transparenz, Risikoreduktion und Lieferfähigkeit.

<>