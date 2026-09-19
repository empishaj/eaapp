## Checkliste: RTO/RPO und Betriebsfähigkeit als Architekturthema prüfen

1. Ist der fachliche Geschäftsprozess klar benannt, nicht nur das IT-System?  
2. Ist die fachliche Kritikalität dokumentiert: Bürgerwirkung, Rechtsfristen, Zahlungen, Sicherheit, Reputation, Steuerungsfähigkeit?  
3. Ist die maximale Ausfallzeit fachlich begründet, bevor über Technik gesprochen wird?  
4. Ist das RTO als Zielzeit für Wiederanlauf definiert?  
5. Ist das RPO als maximal tolerierbarer Datenverlust definiert?  
6. Ist geklärt, ob Notbetrieb, Teilbetrieb oder vollständiger Normalbetrieb gefordert ist?  
7. Sind Abhängigkeiten zu IAM, Netzwerk, Datenbanken, Registerdiensten, Dokumentenablage, Schnittstellen und Betriebsteams sichtbar?  
8. Ist nachgewiesen, dass Backup nicht nur erstellt, sondern regelmäßig wiederhergestellt getestet wird?  
9. Gibt es einen dokumentierten Wiederanlaufplan inklusive Rollen, Reihenfolge, Kommunikationswegen und Entscheidungsbefugnissen?  
10. Sind Wartungsfenster, Change-Prozesse und Incident-Prozesse mit den Betriebsanforderungen vereinbar?  
11. Sind Hochverfügbarkeitsmaßnahmen von Disaster-Recovery-Maßnahmen getrennt bewertet?  
12. Sind Betriebsübergabe, Monitoring, Runbooks, SLAs, OLAs und Abnahmekriterien prüfbar formuliert?  

<>

## 1. Grundsatz: Betriebsfähigkeit ist kein Betriebsdetail, sondern Architekturqualität

Betriebsfähigkeit ist die Fähigkeit eines Fachverfahrens, unter realistischen Betriebsbedingungen verlässlich, überwachbar, wiederherstellbar, sicher betreibbar und organisatorisch beherrschbar zu funktionieren. Als Enterprise Architekt darfst du RTO, RPO, Backup, Restore, Disaster Recovery, Hochverfügbarkeit, Notbetrieb und Betriebsübergabe deshalb nicht erst am Projektende betrachten. Sie gehören in Zielarchitektur, Lösungsdesign, Ausschreibung, Architekturreview, Teststrategie und Abnahme.

Der wichtigste Denkfehler lautet: „Das macht später der Betrieb.“ Nein. Der Betrieb kann nur das betreiben, was Architektur, Entwicklung, Beschaffung und Fachseite vorher als wiederherstellbares, beobachtbares und dokumentiertes System entworfen haben. BSI-Standard 200-4 beschreibt Business Continuity Management als praxisnahe Anleitung für Institutionen; ISO 22301 spezifiziert Anforderungen an ein Business-Continuity-Management-System, während ISO 22313 Anwendungshinweise dazu liefert. NIST SP 800-34 adressiert Contingency Planning für föderale Informationssysteme und betont die Bewertung von Systemen und Operationen zur Ableitung von Notfallplanungsanforderungen. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_4.html?utm_source=chatgpt.com))

## 2. Die Kernbegriffe sauber getrennt

Der erste professionelle Schritt ist begriffliche Hygiene. Viele Projekte vermischen Verfügbarkeit, RTO, RPO, Kritikalität, Backup und Hochverfügbarkeit. Dadurch entstehen scheinbar starke Anforderungen, die in Wahrheit nicht prüfbar sind.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Fachliche Kritikalität | Bewertet die Auswirkung eines Ausfalls auf Aufgabe, Frist, Bürgerleistung, Zahlung, Nachweisfähigkeit, Sicherheit, Steuerung oder gesetzlichen Auftrag. Sie ist der Ausgangspunkt. | „Ausfall verhindert fristgerechte Leistungsbewilligung“ ist kritischer als „Ausfall verzögert Monatsreporting“. | BSI 200-4 und ISO 22301/22313 betrachten Kontinuität aus Sicht kritischer Tätigkeiten und Organisationserfordernisse. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_4.html?utm_source=chatgpt.com)) |
| Verfügbarkeit | Anteil der Zeit, in der ein Dienst nutzbar ist. Typisch als Prozentwert pro Zeitraum formuliert, etwa 99,5 % im Monatsmittel. | Ein Registerdienst ist werktags 7–19 Uhr mit 99,5 % verfügbar. | Verfügbarkeit ist keine Wiederherstellungszusage; sie ersetzt kein RTO/RPO. |
| RTO, Recovery Time Objective | Zielzeit, innerhalb der ein Prozess, Dienst oder System nach einer Störung wieder in einem definierten Zustand verfügbar sein muss. Entscheidend ist: Welcher Zustand? Notbetrieb, Teilbetrieb oder Normalbetrieb? | „RTO 4 Stunden bis lesender Zugriff im Notbetrieb; RTO 24 Stunden bis vollständige Sachbearbeitung.“ | NIST SP 800-34 behandelt Wiederanlaufanforderungen und Priorisierung im Rahmen von Contingency Planning. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final?utm_source=chatgpt.com)) |
| RPO, Recovery Point Objective | Maximal tolerierbarer Datenverlust, gemessen rückwärts vom Störungszeitpunkt bis zum letzten konsistent wiederherstellbaren Datenstand. | „RPO 15 Minuten“ bedeutet: Im Ausfallfall dürfen höchstens 15 Minuten Daten verloren gehen. | BSI CON.3 stellt Datensicherung als Grundlage dar, damit IT-Betrieb durch redundante Datenbestände wiederaufgenommen werden kann. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/03_CON_Konzepte_und_Vorgehensweisen/CON_3_Datensicherungskonzept_Edition_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Backup | Kopie von Daten oder Systemzuständen zur Wiederherstellung. Backup ist kein Erfolg, solange Restore nicht getestet wurde. | Tägliches Datenbankbackup, stündliche Transaktionslogs, immutable Backup für Ransomware-Szenarien. | BSI CON.3 behandelt Anforderungen an Datensicherungskonzepte. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/03_CON_Konzepte_und_Vorgehensweisen/CON_3_Datensicherungskonzept_Edition_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Restore | Praktische Wiederherstellung aus Backup oder Replikat. Restore ist der Moment der Wahrheit. | Wiederherstellung einer Fachverfahrensdatenbank in einer isolierten Umgebung mit fachlicher Plausibilitätsprüfung. | BSI CON.3 fokussiert nicht nur Sicherung, sondern Wiederaufnahmefähigkeit durch redundante Datenbestände. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/03_CON_Konzepte_und_Vorgehensweisen/CON_3_Datensicherungskonzept_Edition_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Hochverfügbarkeit | Architektur zur Reduzierung ungeplanter Ausfälle durch Redundanz, Failover, Clustering, Replikation, Lastverteilung und Fehlerisolation. | Zwei Applikationsknoten hinter Load Balancer; Datenbank-Cluster mit automatischem Failover. | Hochverfügbarkeit mindert Ausfälle, ersetzt aber kein Disaster Recovery. |
| Disaster Recovery | Fähigkeit, nach schwerwiegendem Ausfall eines Standorts, Providers, Rechenzentrums, Clusters oder Datenbestands wieder arbeitsfähig zu werden. | Wiederanlauf in zweitem Rechenzentrum oder souveräner Cloud-Zone nach Totalausfall des Primärstandorts. | NIST SP 800-34 ist eine zentrale Referenz für Contingency Planning und Wiederherstellungsplanung. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final?utm_source=chatgpt.com)) |
| Notbetrieb | Minimaler fachlicher Betriebsmodus zur Aufrechterhaltung unverzichtbarer Funktionen. | Manuelle Fallannahme, Lesemodus, priorisierte Bearbeitung, Papierformular, Offline-Erfassung mit späterer Nachverarbeitung. | ISO 22313 betont vordefinierte akzeptable Kapazität während Störungen. ([iso.org](https://www.iso.org/standard/75107.html?utm_source=chatgpt.com)) |
| Betriebsübergabe | Geordnete Übergabe von System, Wissen, Dokumentation, Monitoring, Runbooks, Supportwegen und Verantwortlichkeiten in den Regelbetrieb. | Betriebsdokumentation, Alarmierungsregeln, Berechtigungsmodell, Backup-Nachweise, Wiederanlauftest, Schulung. | BSI-Grundschutz-Bausteine zu Betrieb, Datensicherung und Sicherheitsvorfällen liefern hierfür belastbare Bezugspunkte. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/03_CON_Konzepte_und_Vorgehensweisen/CON_3_Datensicherungskonzept_Edition_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |

## 3. Der entscheidende Unterschied: Verfügbarkeit, RTO, RPO und Kritikalität

Verfügbarkeit beantwortet die Frage: „Wie oft ist der Dienst im definierten Zeitraum nutzbar?“ RTO beantwortet: „Wie schnell müssen wir nach einem Ausfall wieder arbeitsfähig sein?“ RPO beantwortet: „Wie viele Daten dürfen wir verlieren?“ Fachliche Kritikalität beantwortet: „Wie schlimm ist der Ausfall für Auftrag, Menschen, Fristen, Geld, Recht, Sicherheit und Steuerung?“

Diese vier Größen dürfen niemals gegeneinander ausgetauscht werden. Ein System kann 99,9 % verfügbar sein und trotzdem ein schlechtes RTO haben, wenn ein Totalausfall nur nach drei Tagen wiederherstellbar ist. Ein System kann ein gutes RTO haben und trotzdem ein schlechtes RPO, wenn es schnell startet, aber acht Stunden Datenverlust verursacht. Ein System kann technisch unkritisch wirken, aber fachlich hochkritisch sein, weil es eine gesetzliche Frist, eine Zahlung oder eine Sicherheitsentscheidung blockiert.

## 4. Die fachliche Ableitung: Nicht „Was kann die Technik?“, sondern „Was trägt der Prozess?“

Als Enterprise Architekt beginnst du nicht mit Backup-Software, Clustern oder Cloud-Regionen. Du beginnst mit der fachlichen Schadenskurve. Du fragst: Was passiert nach 15 Minuten Ausfall, nach 1 Stunde, nach 4 Stunden, nach 1 Tag, nach 3 Tagen? Ab wann wird aus Unbequemlichkeit ein Rückstand, aus Rückstand ein Fristbruch, aus Fristbruch ein Rechtsproblem, aus Rechtsproblem ein Vertrauens- oder Steuerungsproblem?

Danach leitest du RTO und RPO ab. Nicht jedes System braucht RTO 15 Minuten und RPO 0. Das wäre teuer, komplex und oft unnötig. Aber jedes System braucht eine begründete Entscheidung. Gute Architektur bedeutet nicht maximale Ausfallsicherheit überall, sondern angemessene Resilienz an den richtigen Stellen.

## 5. Beispiele aus Behörden- und Fachverfahrenskontexten

| Aspekt | Details/Erklärung | Beispiel | Mögliche RTO/RPO-Ableitung | Literatur/Quelle |
|---|---|---|---|---|
| Fachverfahren für Antragsbearbeitung | Kernsystem für Fallanlage, Sachbearbeitung, Bescheidung, Fristen, Statusänderungen. | Asyl-, Leistungs-, Förder- oder Genehmigungsverfahren. | RTO häufig Stunden bis 1 Arbeitstag; RPO je nach Transaktionskritik 15 Minuten bis 4 Stunden. Notbetrieb über Falllisten, Lesemodus oder manuelle Erfassung denkbar. | Ableitung aus Business Impact und Kontinuitätsanforderungen; BSI 200-4 und ISO 22301/22313 geben hierfür den BCM-Rahmen. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_4.html?utm_source=chatgpt.com)) |
| Registerabfragen | Abhängigkeit von externen oder zentralen Registern. Häufig lesend, aber fachlich entscheidend. | Melderegister, Ausländerzentralregister, Unternehmensregister, Identitätsprüfung. | RTO abhängig davon, ob Bearbeitung ohne Registerauskunft fortgesetzt werden darf. RPO oft nicht primär relevant, wenn Datenquelle extern führend ist; wichtiger sind Fallback, Caching, Queueing und Nachprüfung. | NIST betont die Bewertung von Systemen und Operationen zur Priorisierung von Contingency-Anforderungen. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final?utm_source=chatgpt.com)) |
| Dokumentenablage | Ablage, Recherche, Aktenbestand, Nachweisführung, Bescheide, Eingangspost, Scans. | eAkte, DMS, Vorgangsdokumentation. | RTO oft kritisch für Lesefähigkeit; RPO streng, wenn neue Dokumente rechtsrelevant sind. Notbetrieb kann Scan-Stopp, manuelle Aktenliste oder temporäre Ablage sein. | BSI CON.3 ist relevant, weil Wiederaufnahmefähigkeit über belastbare Datensicherung abgesichert werden muss. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/03_CON_Konzepte_und_Vorgehensweisen/CON_3_Datensicherungskonzept_Edition_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Zahlungsprozesse | Auszahlung, Rückforderung, Buchung, Zahlungsfreigabe, Kassenintegration. | Sozialleistung, Gebührenrückzahlung, Fördermittelzahlung. | RTO und RPO meistens streng. RPO nahe 0 oder transaktionslogbasiert, weil Doppelzahlung, Nichtzahlung oder Buchungsinkonsistenz erheblich sind. | ISO 22301 verlangt systematisches Vorbereiten, Reagieren und Wiederherstellen bei Störungen. ([iso.org](https://www.iso.org/publication/PUB200223.html?utm_source=chatgpt.com)) |
| Berichtssysteme | Steuerungsberichte, Statistik, Management-Reporting, Lagebilder. | Monatsbericht, Controlling, operative Dashboards. | RTO häufig weniger streng bei Monatsreporting, aber sehr streng bei Lage- oder Krisenreporting. RPO abhängig von Aktualitätsanforderung. | Kritikalität entsteht aus Nutzungszweck, nicht aus Systemklasse. |

## 6. Architekturperspektive: Was du konkret prüfst

Du prüfst nicht nur, ob es „ein Backup gibt“. Du prüfst, ob die technische, fachliche und organisatorische Kette hält. Diese Kette lautet: Kritikalität erkennen, Zielzustand definieren, Architekturmaßnahmen auswählen, Betrieb vorbereiten, Wiederherstellung testen, Abnahme nachweisen.

Ein robustes Architekturreview enthält deshalb mindestens diese Fragen: Ist der fachliche Prozess mit Kritikalität beschrieben? Gibt es eine Business-Impact-Ableitung? Sind RTO und RPO pro Capability, nicht nur pro Server, definiert? Sind führende Datenquellen bekannt? Sind Schnittstellenabhängigkeiten sichtbar? Ist der Notbetrieb beschrieben? Ist klar, welche Reihenfolge der Wiederanlauf hat? Sind IAM, Netzwerk, DNS, Zertifikate, Secrets, Monitoring, Logging, Messaging, Datenbank, Storage, DMS und externe Register in der Wiederherstellung berücksichtigt? Ist die Wiederherstellung regelmäßig getestet? Sind Incident- und Krisenprozesse gekoppelt? ENISA nennt die Integration von Business-Continuity- und Disaster-Recovery-Plänen mit Incident-Response- und Krisenmanagement-Prozessen als technische Implementierungsanforderung im NIS2-Kontext. ([enisa.europa.eu](https://www.enisa.europa.eu/sites/default/files/2025-06/ENISA_Technical_implementation_guidance_on_cybersecurity_risk_management_measures_version_1.0.pdf?utm_source=chatgpt.com))

## 7. Betriebsfähigkeitsraster für Architekturreviews

Dieses Raster kannst du in Architekturboards, Ausschreibungen, Lösungsdesigns und Betriebsübergaben verwenden. Es ist bewusst leichtgewichtig, aber prüfbar.

| Aspekt | Details/Erklärung | Prüffrage | Nachweis/Artefakt | Beispiel | Literatur/Quelle |
|---|---|---|---|---|---|
| Fachprozess | Nicht das System, sondern die fachliche Leistung wird bewertet. | Welche Leistung fällt aus, wenn das System nicht verfügbar ist? | Prozessbeschreibung, Capability Map, Facharchitektur. | „Antrag kann nicht weiterbearbeitet werden.“ | BSI 200-4, ISO 22301/22313. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_4.html?utm_source=chatgpt.com)) |
| Kritikalität | Auswirkung nach Zeitfenstern bewerten. | Was passiert nach 1 h, 4 h, 1 Tag, 3 Tagen? | Business-Impact-Analyse, Risikobewertung. | Fristversäumnis nach 24 h. | BSI 200-4. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_4.html?utm_source=chatgpt.com)) |
| Betriebszeit | Definiert, wann der Dienst benötigt wird. | 24/7, werktags, Geschäftszeiten, Kampagnenzeiten? | Serviceprofil, SLA, Betriebsvereinbarung. | Registerabfrage werktags 6–22 Uhr. | Betriebsanforderung aus Fachbedarf. |
| RTO | Zielzeit bis definierter Wiederanlaufzustand. | Bis wann muss welcher Zustand wiederhergestellt sein? | RTO-Tabelle, Wiederanlaufkonzept. | 4 h bis Lesemodus, 24 h bis Vollbetrieb. | NIST SP 800-34. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final?utm_source=chatgpt.com)) |
| RPO | Maximal tolerierter Datenverlust. | Wie viele Daten dürfen verloren gehen? | Backup-Konzept, Replikationskonzept, Transaktionslog-Konzept. | RPO 15 min für Zahlungsvorgänge. | BSI CON.3. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/03_CON_Konzepte_und_Vorgehensweisen/CON_3_Datensicherungskonzept_Edition_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Notbetrieb | Fachlich akzeptabler Minimalbetrieb. | Welche Minimalleistung muss weiterlaufen? | Notbetriebskonzept, manuelle Verfahren, Fallback-Prozess. | Manuelle Fallannahme mit späterer Nacherfassung. | ISO 22313. ([iso.org](https://www.iso.org/standard/75107.html?utm_source=chatgpt.com)) |
| Backup | Sicherung von Daten, Konfigurationen, Artefakten und Metadaten. | Was wird gesichert, wie oft, wie lange, wie geschützt? | Backup-Policy, Backup-Protokolle, Retention-Konzept. | Datenbank, DMS, Konfiguration, Secrets-Referenzen. | BSI CON.3. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/03_CON_Konzepte_und_Vorgehensweisen/CON_3_Datensicherungskonzept_Edition_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Restore-Test | Wiederherstellung muss praktisch geprüft werden. | Wurde ein Restore unter realistischen Bedingungen getestet? | Restore-Protokoll, Testbericht, fachliche Abnahme. | Quartalsweiser Restore in isolierter Umgebung. | BSI CON.3. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/03_CON_Konzepte_und_Vorgehensweisen/CON_3_Datensicherungskonzept_Edition_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Hochverfügbarkeit | Fehler einzelner Komponenten dürfen nicht sofort zum Dienstausfall führen. | Welche Single Points of Failure bleiben? | Architekturdiagramm, HA-Konzept, Failover-Test. | Zwei App-Knoten, redundanter Load Balancer. | Architektur- und Betriebsnachweis. |
| Disaster Recovery | Wiederanlauf bei Standort-, Plattform- oder Großausfall. | Wo läuft das System, wenn Standort A ausfällt? | DR-Konzept, Runbook, Übungsprotokoll. | Wiederanlauf in zweitem RZ. | NIST SP 800-34. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final?utm_source=chatgpt.com)) |
| Incident-Prozess | Störungen müssen erkannt, klassifiziert, eskaliert und bearbeitet werden. | Wer entscheidet was bei Major Incident? | Incident-Prozess, RACI, Meldewege. | Major Incident Bridge, Lagebericht, Post-Incident Review. | BSI DER.2.1 fordert schnelle und effiziente Bearbeitung erkannter Sicherheitsvorfälle. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/05_DER_Detektion_und_Reaktion/DER_2_1_Behandlung_von_Sicherheitsvorfaellen_Edition_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Monitoring/Observability | Ohne Erkennung keine Wiederherstellung. | Welche fachlichen und technischen Signale zeigen Störung? | Dashboard, Alert-Regeln, SLOs, Logkonzept. | Queue-Stau, Fehlerrate, Antwortzeit, Zahlungsabbruchquote. | Betriebs- und Security-Anforderungen. |
| Wartungsfenster | Geplante Nichtverfügbarkeit muss fachlich tragbar sein. | Wann darf abgeschaltet werden? | Wartungskalender, Change-Prozess, Kommunikationsplan. | Sonntag 6–10 Uhr nur bei nichtkritischen Verfahren. | Betriebsanforderung aus Serviceprofil. |
| Betriebsübergabe | Betrieb muss die Lösung wirklich übernehmen können. | Sind Runbooks, Zugänge, Schulung, SLAs und Supportwege vollständig? | Operational Readiness Review, Übergabeprotokoll. | Go-live nur nach Betriebsfreigabe. | BSI-Grundschutz-Betriebsbausteine. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/04_OPS_Betrieb/OPS_1_1_2_Ordnungsgemaesse_IT_Administration_Edition_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |

## 8. Interviewfragen zur Erhebung von Betriebsanforderungen

Die Qualität deiner RTO/RPO-Erhebung hängt direkt von deinen Fragen ab. Frage niemals: „Welches RTO wollen Sie?“ Fachbereiche antworten dann oft „sofort“, weil sie die Kostenfolgen nicht sehen. Frage stattdessen nach Auswirkungen, Fristen, Mengen, Arbeitsfähigkeit und Alternativen.

| Aspekt | Details/Erklärung | Beispielhafte Interviewfragen | Ziel der Frage | Literatur/Quelle |
|---|---|---|---|---|
| Fachliche Leistung | Erst die Leistung verstehen, dann Systeme bewerten. | Welche konkrete Leistung gegenüber Bürgern, Behörden, Gerichten, Trägern oder internen Stellen hängt an diesem Verfahren? | Capability statt Technik erfassen. | BSI 200-4, ISO 22301/22313. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_4.html?utm_source=chatgpt.com)) |
| Zeitkritik | Ausfallauswirkung zeitlich staffeln. | Was passiert nach 30 Minuten, 2 Stunden, 1 Tag, 3 Tagen? | Schadenskurve ableiten. | BCM-Logik aus BSI/ISO. |
| Fristen | Rechtliche und organisatorische Deadlines sichtbar machen. | Welche gesetzlichen, vertraglichen oder internen Fristen werden durch Ausfall gefährdet? | Kritikalität begründen. | Behördenpraxis, Fachanforderung. |
| Datenverlust | RPO fachlich erklären lassen. | Welche Daten dürften wir im schlimmsten Fall neu erfassen? Welche keinesfalls? | RPO ableiten. | BSI CON.3. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/03_CON_Konzepte_und_Vorgehensweisen/CON_3_Datensicherungskonzept_Edition_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Datenkonsistenz | Kritisch bei Zahlungen, Bescheiden, Statuswechseln. | Was ist schlimmer: 30 Minuten Datenverlust oder inkonsistente Daten? | Konsistenzanforderung klären. | Architektur- und Datenmanagementpraxis. |
| Notbetrieb | Minimalleistung definieren. | Was muss unbedingt weitergehen, auch wenn das Zielsystem ausfällt? | Minimum Viable Operation bestimmen. | ISO 22313. ([iso.org](https://www.iso.org/standard/75107.html?utm_source=chatgpt.com)) |
| Manuelle Verfahren | Realistische Fallbacks prüfen. | Gibt es Papier-, Excel-, Postkorb-, Telefon- oder E-Mail-Verfahren? Sind sie zulässig? | Notbetrieb konkretisieren. | BCM-Praxis. |
| Abhängigkeiten | Wiederanlauf hängt an Ketten, nicht an Einzelsystemen. | Welche anderen Systeme, Register, Schnittstellen, Identitätsdienste, Netzwerke oder Teams werden benötigt? | Dependency Map erstellen. | NIST SP 800-34. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final?utm_source=chatgpt.com)) |
| Betriebszeiten | Nicht jedes System braucht 24/7. | Wann wird das Verfahren tatsächlich gebraucht? Gibt es Spitzen, Kampagnen, Stichtage? | Servicezeiten definieren. | Fachanforderung. |
| Mengen und Rückstau | Nach Wiederanlauf muss Rückstand abgearbeitet werden. | Wie viele Fälle entstehen pro Stunde/Tag? Wie schnell muss Rückstau abgebaut werden? | Kapazitätsanforderung ableiten. | Betriebsplanung. |
| Kommunikation | Störung ist auch Kommunikationsereignis. | Wer muss wann informiert werden? Fachbereich, Leitung, Bürger, externe Partner? | Incident-Kommunikation festlegen. | BSI DER.2.1. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/05_DER_Detektion_und_Reaktion/DER_2_1_Behandlung_von_Sicherheitsvorfaellen_Edition_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Abnahme | Anforderungen müssen testbar werden. | Woran erkennen Sie, dass der Wiederanlauf erfolgreich war? | Abnahmekriterien formulieren. | Architektur-Governance. |

## 9. Beispielbewertung: fünf typische Systemklassen

Die folgenden Werte sind keine allgemeingültigen Vorgaben, sondern plausible Startwerte für Diskussionen. In echten Behördenprojekten müssen sie fachlich, rechtlich, betrieblich und wirtschaftlich validiert werden.

| Aspekt | Details/Erklärung | Beispiel | RTO | RPO | Technische Maßnahmen | Abnahmekriterium |
|---|---|---|---:|---:|---|---|
| Fachverfahren hochkritisch | Kernbearbeitung mit Fristen, Bescheiden, Statusentscheidungen. | Fallbearbeitung im zentralen Fachverfahren. | 4–8 h Teilbetrieb, 24 h Vollbetrieb | 15–60 min | HA für Applikation, Datenbankreplikation, Transaktionslogs, regelmäßige Restore-Tests, Notbetrieb für Fallannahme. | In DR-Übung wird Lesemodus innerhalb 4 h und Vollbetrieb innerhalb 24 h nachweisbar hergestellt. |
| Registerabfrage kritisch | Externe Datenquelle für Entscheidungsfähigkeit. | Identitäts- oder Statusabfrage. | 2–4 h oder Fallback sofort | Abhängig von führendem Register; oft nicht lokal maßgeblich | Timeout-Strategie, Circuit Breaker, Caching, Queueing, Fallback-Meldung, Nachprüfprozess. | Bei Registerausfall kann Vorgang markiert, zwischengespeichert und nach Wiederverfügbarkeit kontrolliert nachbearbeitet werden. |
| Dokumentenablage kritisch | Nachweis, Recherche, Bescheid- und Aktenzugriff. | eAkte/DMS. | 4 h Lesebetrieb, 24 h Schreibbetrieb | 15 min–4 h | Storage-Replikation, DMS-Backup, Index-Rebuild-Konzept, getrennte Sicherung von Metadaten und Binärdaten. | Stichproben aus Aktenbestand sind nach Restore vollständig, lesbar, korrekt versioniert und recherchierbar. |
| Zahlungsprozess sehr kritisch | Finanzielle Wirkung, Buchung, Freigabe, Schnittstelle zur Kasse. | Auszahlung/Rückforderung. | 1–4 h für Stop/Statusklärung, 8–24 h für Verarbeitung | 0–15 min | Transaktionssichere Verarbeitung, Idempotenz, Journal, Vier-Augen-Freigabe, Replay-Konzept, Abgleich mit Kasse. | Nach simuliertem Ausfall gibt es keine Doppelzahlung, keine verlorene Buchung und eine vollständige Abstimmungsliste. |
| Berichtssystem mittel bis kritisch | Steuerung, Statistik, Lagebild. | Monatsreporting oder operatives Dashboard. | 1–3 Tage bei Monatsbericht; 1–4 h bei Lagebild | 1 Tag bis 15 min | Data-Warehouse-Backups, Rebuild aus Quellsystemen, Datenqualitätschecks, Snapshot-Konzept. | Bericht kann aus wiederhergestellten Daten reproduziert werden; Abweichungen sind dokumentiert und fachlich akzeptiert. |

## 10. Wie du RTO/RPO konkret ableitest

Du gehst in fünf Schritten vor. Erstens beschreibst du die fachliche Capability, zum Beispiel „Antrag entgegennehmen“, „Fall entscheiden“, „Dokument nachweisen“, „Zahlung auslösen“ oder „Lage berichten“. Zweitens bewertest du den Ausfall entlang von Zeitfenstern. Drittens definierst du den minimal akzeptablen Wiederanlaufzustand. Viertens leitest du daraus RTO und RPO ab. Fünftens prüfst du, ob Architektur, Betrieb und Dienstleister diese Werte nachweislich erfüllen können.

Ein professioneller Satz lautet nicht: „Das System braucht RTO 4 Stunden.“ Ein professioneller Satz lautet: „Für die Capability ‚Zahlungsfreigabe‘ ist spätestens nach 4 Stunden ein fachlich kontrollierter Teilbetrieb erforderlich, in dem offene Zahlungen identifizierbar, neue Freigaben gestoppt oder priorisiert verarbeitet und Buchungsinkonsistenzen ausgeschlossen werden. Der maximal tolerierbare Datenverlust beträgt 15 Minuten, wobei Transaktionsjournal und Kassenabgleich sicherstellen müssen, dass keine Doppelzahlung und keine unerkannte Nichtzahlung entsteht.“

Das ist Architektur. Es verbindet Fachlichkeit, Zeit, Daten, Betrieb, Risiko und Prüfbarkeit.

## 11. Technische Maßnahmen richtig bewerten

Nicht jede Maßnahme löst jedes Problem. Backup senkt Datenverlustrisiko, aber nicht automatisch Ausfallzeit. Hochverfügbarkeit senkt Ausfallwahrscheinlichkeit, aber schützt nicht zwingend vor logischer Datenkorruption, Ransomware oder Bedienfehlern. Replikation kann RPO verbessern, aber sie repliziert unter Umständen auch fehlerhafte oder verschlüsselte Daten. Disaster Recovery kann Standortausfälle adressieren, aber nur, wenn IAM, Netzwerk, DNS, Zertifikate, Secrets, Images, Konfiguration und Daten konsistent wiederherstellbar sind.

| Aspekt | Details/Erklärung | Gut geeignet für | Nicht ausreichend für | Beispiel |
|---|---|---|---|---|
| Tägliches Backup | Einmal tägliche Sicherung. | Unkritische Daten, niedrige Änderungsrate. | RPO unter 24 h, schnelle Wiederherstellung. | Berichtsdatenbank mit Tagesstand. |
| Stündliches Backup/Log Backup | Häufigere Sicherung oder Transaktionslogs. | RPO im Stunden- oder Minutenbereich. | Sofortige Verfügbarkeit. | Fachverfahren mit laufender Sachbearbeitung. |
| Immutable Backup | Unveränderbare Sicherung gegen Manipulation. | Ransomware- und Insider-Szenarien. | Hochverfügbarkeit im laufenden Betrieb. | Unveränderbare Backup-Snapshots. |
| Datenbankreplikation | Laufende Replikation in zweite Instanz. | Kurzes RPO, schneller Failover. | Schutz vor logischen Fehlern, wenn repliziert wird. | Primär-/Standby-Datenbank. |
| Applikationscluster | Mehrere App-Instanzen. | Ausfall einzelner Knoten. | Datenverlust, Datenbankausfall, fehlerhafte Releases. | Kubernetes-Deployment mit mehreren Pods. |
| Multi-Zone-Betrieb | Verteilung über Ausfallzonen. | Infrastrukturfehler in Zone. | Standortweiter Ausfall, fehlerhafte Daten, IAM-Ausfall. | Betrieb in zwei Availability Zones. |
| Zweitstandort/DR-Umgebung | Wiederanlauf bei Standortausfall. | Katastrophenfall, Rechenzentrumsausfall. | Ungetestete Abhängigkeiten. | Warm Standby im zweiten RZ. |
| Notbetrieb | Manuelle oder reduzierte Fortführung. | Fachliche Mindestarbeitsfähigkeit. | Hohe Mengen, lange Dauer ohne Nacharbeit. | Manuelle Fallannahme mit späterem Import. |
| Observability | Erkennung, Diagnose, Steuerung. | Schnelle Incident-Erkennung und Ursachenanalyse. | Verhindert Ausfall nicht allein. | SLO-Dashboard, Alerting, Trace-Korrelation. |
| Runbooks | Schrittweise Betriebsanweisung. | Wiederholbare Reaktion und Wiederanlauf. | Unklare Zuständigkeiten oder fehlende Berechtigungen. | „Datenbank-Failover durchführen“. |

## 12. Incident-Prozesse als Architekturthema

Incident-Prozesse sind nicht nur Tickets. Sie sind der operative Nerv der Architektur. Eine Architektur, die keinen klaren Störungspfad hat, ist nicht vollständig. Du brauchst Klassifikation, Alarmierung, Eskalation, Kommunikationsregeln, Entscheidungsbefugnis, technische Diagnose, fachliche Lagebewertung, Wiederanlaufentscheidung und Nachbereitung.

Bei Behörden ist zusätzlich wichtig: Es gibt häufig mehrere beteiligte Organisationseinheiten, Dienstleister, Rechenzentren, Fachreferate, Datenschutz, Informationssicherheit, Leitungsbereiche und externe Partner. Darum muss vor dem Ernstfall klar sein, wer bei einem Major Incident entscheidet, wer informiert, wer technische Maßnahmen freigibt, wer fachlich priorisiert und wer nach außen kommuniziert. BSI DER.2.1 betont, dass erkannte Sicherheitsvorfälle schnell und effizient bearbeitet werden müssen; ENISA verweist im NIS2-Kontext auf die Verzahnung von Business Continuity, Disaster Recovery, Incident Response und Krisenmanagement. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/05_DER_Detektion_und_Reaktion/DER_2_1_Behandlung_von_Sicherheitsvorfaellen_Edition_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com))

## 13. Betriebsübergabe: Was vor Go-live vorliegen muss

Ein System ist nicht produktionsreif, nur weil es fachlich funktioniert. Es ist produktionsreif, wenn es betrieben, überwacht, gesichert, wiederhergestellt, aktualisiert, skaliert, supportet und verantwortet werden kann.

| Aspekt | Details/Erklärung | Mindestnachweis | Beispiel für Abnahmekriterium |
|---|---|---|---|
| Betriebsdokumentation | Systemübersicht, Komponenten, Schnittstellen, Datenflüsse, Verantwortlichkeiten. | Aktuelles Betriebsdokument. | „Alle produktiven Komponenten sind mit Zweck, Betreiber, Ansprechpartner, SLA und Abhängigkeiten dokumentiert.“ |
| Runbooks | Handlungsanweisungen für Standardstörungen und Wiederanlauf. | Runbook-Sammlung. | „Für Datenbankausfall, Queue-Stau, Zertifikatsablauf, Registerausfall und Deployment-Rollback liegen getestete Runbooks vor.“ |
| Monitoring | Technische und fachliche Signale. | Dashboards, Alerts, Alarmwege. | „Fehlerrate, Antwortzeit, Queue-Länge, Jobabbrüche und fachliche Durchsatzkennzahlen sind überwacht.“ |
| Backup/Restore | Sicherung plus Wiederherstellungsnachweis. | Backup-Konzept, Restore-Testbericht. | „Ein vollständiger Restore wurde innerhalb des geforderten RTO erfolgreich durchgeführt und fachlich geprüft.“ |
| Berechtigungen | Betrieb braucht handlungsfähige, kontrollierte Rechte. | Rollenmodell, Break-Glass-Verfahren. | „Betriebsrollen sind definiert; Notfallzugriff ist protokolliert, befristet und freigabepflichtig.“ |
| Incident-Prozess | Störungspfad muss bekannt sein. | RACI, Eskalationsmatrix, Kontaktliste. | „Major-Incident-Prozess wurde mit Fachseite, Betrieb und Dienstleister durchgespielt.“ |
| Wartungsfenster | Geplante Eingriffe brauchen fachliche Akzeptanz. | Wartungsregelung, Kommunikationsplan. | „Regelwartung ist auf fachlich akzeptierte Zeitfenster beschränkt und mindestens x Tage vorher anzukündigen.“ |
| Dienstleistersteuerung | Externe Leistung muss messbar sein. | SLA/OLA, Liefergegenstände, Reporting. | „Dienstleister berichtet monatlich Backup-Erfolg, Restore-Teststatus, Incidents, Problem Records und offene Betriebsrisiken.“ |
| Sicherheitsbetrieb | Security-Ereignisse müssen detektiert und behandelt werden. | Logging, SIEM-Anbindung, Meldeweg. | „Sicherheitsrelevante Ereignisse werden zentral protokolliert und nach definiertem Prozess eskaliert.“ |
| Wissensübergabe | Betrieb darf nicht vom Projektteam abhängig bleiben. | Schulung, Übergabeprotokoll. | „Betriebsteam kann Standardstörungen anhand Runbook ohne Projektunterstützung bearbeiten.“ |

## 14. Prüffähige Abnahmekriterien formulieren

Schwache Formulierung: „Der Auftragnehmer stellt Backup und Restore sicher.“ Diese Aussage ist zu weich. Sie sagt nicht, was gesichert wird, wie oft, wie lange, wie geschützt, wie wiederhergestellt, wie getestet und wie abgenommen wird.

Starke Formulierung: „Der Auftragnehmer liefert ein abgestimmtes Backup- und Restore-Konzept für Datenbank, Dokumentenspeicher, Konfigurationen, Schnittstellendefinitionen und betriebsrelevante Metadaten. Das Konzept weist je Datenklasse Sicherungsfrequenz, Aufbewahrungsdauer, Verschlüsselung, Zugriffsschutz, RPO, Restore-Verfahren und Testintervall aus. Vor Produktivsetzung ist ein Restore-Test in einer isolierten Umgebung durchzuführen. Der Test gilt nur als bestanden, wenn die Anwendung innerhalb des vereinbarten RTO startet, die fachlichen Stichproben erfolgreich geprüft sind und ein Restore-Protokoll mit Abweichungen, Zeiten und Verantwortlichen vorliegt.“

Noch stärker wird es, wenn du den Wiederanlaufzustand definierst: „RTO 4 Stunden bis fachlicher Lesebetrieb“ ist prüfbarer als „RTO 4 Stunden“. „RPO 15 Minuten für zahlungsrelevante Transaktionen“ ist prüfbarer als „regelmäßige Backups“.

## 15. Typische Fehler und klare Korrektur

| Aspekt | Details/Erklärung | Risiko | Korrektur |
|---|---|---|---|
| RTO/RPO werden technisch geschätzt | Betrieb oder Dienstleister nennt Werte ohne Fachvalidierung. | Teure Über- oder gefährliche Unterdimensionierung. | RTO/RPO aus Business Impact ableiten und fachlich freigeben lassen. |
| Verfügbarkeit ersetzt Wiederherstellung | 99,9 % klingt gut, sagt aber wenig über Totalausfall. | Nach schwerem Ausfall dauert Wiederanlauf Tage. | Verfügbarkeit, RTO, RPO und DR getrennt spezifizieren. |
| Backup wird mit Restore verwechselt | „Backup erfolgreich“ heißt nicht „wiederherstellbar“. | Im Ernstfall sind Daten unbrauchbar, inkonsistent oder zu langsam wiederherstellbar. | Regelmäßige Restore-Tests mit fachlicher Prüfung verlangen. |
| Notbetrieb fehlt | Alles hängt am Zielsystem. | Bei Ausfall steht der Fachprozess vollständig still. | Minimalbetrieb definieren: was, wer, wie lange, mit welchen Daten. |
| Abhängigkeiten fehlen | IAM, DNS, Netzwerk, Zertifikate, Register, DMS oder Queue werden vergessen. | System ist technisch restored, aber fachlich nicht nutzbar. | Dependency Map und Wiederanlaufreihenfolge erstellen. |
| RPO ignoriert Datenkonsistenz | Datenverlust wird isoliert betrachtet. | Doppelte Zahlungen, falsche Bescheide, Statusbrüche. | Konsistenz, Idempotenz, Journalisierung und Abgleich definieren. |
| DR wird nie geübt | Plan existiert nur als Dokument. | Ernstfall scheitert an Rollen, Rechten, Zeit oder Details. | Tabletop-Übungen und technische DR-Tests fest einplanen. |
| Wartungsfenster passen nicht zum Fachprozess | Technik plant Wartung während fachlicher Spitzen. | Geplante Ausfälle wirken wie Störungen. | Fachliche Kalender, Stichtage und Kampagnen berücksichtigen. |
| Betriebsübergabe zu spät | Betrieb bekommt System kurz vor Go-live. | Wissenslücken, unklare Verantwortung, instabile Produktion. | Operational Readiness Review vor Produktionsfreigabe. |
| Dienstleister liefert Dokumente ohne Nachweis | Konzepte sind schön, aber nicht bewiesen. | Papier-Compliance statt Betriebsfähigkeit. | Abnahme über Testprotokolle, Übungen, Metriken und Stichproben. |

## 16. Kompaktes Vorgehensmodell für dich als Enterprise Architekt

Du kannst dieses Vorgehen in jedem Behördenprojekt einsetzen.

| Aspekt | Details/Erklärung | Ergebnis |
|---|---|---|
| Schritt 1: Capability identifizieren | Beschreibe die fachliche Fähigkeit, nicht nur Applikationen. | Liste kritischer Capabilities. |
| Schritt 2: Ausfallschaden staffeln | Bewerte Auswirkungen nach Zeitfenstern. | Schadenskurve je Capability. |
| Schritt 3: Kritikalitätsklasse vergeben | Klassifiziere nach Bürgerwirkung, Fristen, Geld, Recht, Sicherheit, Steuerung. | Kritikalitätsprofil. |
| Schritt 4: Notbetrieb definieren | Lege Minimalleistung und zulässige Einschränkungen fest. | Notbetriebskonzept. |
| Schritt 5: RTO/RPO ableiten | Formuliere Zielzeiten und maximalen Datenverlust je Capability. | RTO/RPO-Matrix. |
| Schritt 6: Abhängigkeiten modellieren | Identifiziere technische und organisatorische Ketten. | Dependency Map. |
| Schritt 7: Maßnahmen bewerten | Ordne HA, Backup, Restore, DR, Monitoring, Runbooks und Incident-Prozess zu. | Maßnahmenkatalog. |
| Schritt 8: Nachweise verlangen | Übersetze Anforderungen in prüfbare Liefergegenstände. | Abnahmekriterien. |
| Schritt 9: Testen lassen | Restore, Failover, Notbetrieb und Incident-Ablauf üben. | Testprotokolle. |
| Schritt 10: Governance etablieren | Regelmäßige Reviews, Risikolog, Maßnahmenverfolgung. | Betriebsfähigkeits-Governance. |

## 17. Übung: Betriebsfähigkeit für ein Behördenverfahren ableiten

Nimm folgendes Szenario: Eine Behörde betreibt ein Fachverfahren zur Antragsbearbeitung. Das Verfahren nutzt ein zentrales IAM, fragt ein Register ab, speichert Bescheide im DMS, löst bei positiven Entscheidungen Zahlungen aus und liefert tägliche Berichte an die Leitung.

Deine Aufgabe besteht aus fünf Arbeitsschritten. Erstens zerlegst du das Verfahren in Capabilities: Antrag anlegen, Identität prüfen, Registerauskunft abrufen, Fall entscheiden, Dokument erzeugen, Bescheid ablegen, Zahlung auslösen, Status berichten. Zweitens bewertest du jede Capability entlang der Zeitfenster 1 Stunde, 4 Stunden, 1 Arbeitstag und 3 Arbeitstage. Drittens leitest du je Capability RTO, RPO und Notbetriebsfähigkeit ab. Viertens formulierst du technische Maßnahmen. Fünftens formulierst du Abnahmekriterien.

Eine mögliche Musterlösung sähe so aus: Für „Zahlung auslösen“ setzt du RTO 4 Stunden für kontrollierten Teilbetrieb, RPO 15 Minuten, zwingende Journalisierung, Idempotenz, Kassenabgleich und Wiederanlaufprotokoll. Für „Bericht erstellen“ setzt du RTO 24 Stunden und RPO 1 Tag, außer es handelt sich um ein Lagebild; dann wird RTO 2 Stunden und RPO 15 Minuten plausibel. Für „Dokument ablegen“ setzt du RTO 4 Stunden Lesebetrieb und 24 Stunden Schreibbetrieb, RPO 1 Stunde, DMS-Restore-Test mit Stichproben. Für „Registerauskunft abrufen“ definierst du Fallback: Vorgänge dürfen markiert und später geprüft werden, aber finale Entscheidung ohne Registertreffer ist nur zulässig, wenn die Fachregel das erlaubt.

## 18. Deine Zielkompetenz als Enterprise Architekt

Wenn du dieses Thema professionell beherrschst, wirst du in Architekturreviews nicht mehr fragen: „Habt ihr Backup?“ Du wirst fragen: „Welche fachliche Fähigkeit muss in welchem Zustand nach welcher Zeit mit welchem maximalen Datenverlust wieder verfügbar sein, welche Abhängigkeiten müssen dafür funktionieren, wie wurde das getestet, wer entscheidet im Störungsfall und welcher Nachweis liegt für die Abnahme vor?“

Genau an dieser Stelle wird Betriebsfähigkeit zur Architekturdisziplin. Du schützt nicht nur Systeme. Du schützt Handlungsfähigkeit. Und in Behörden ist Handlungsfähigkeit ein Kernmerkmal guter Architektur: nachvollziehbar, prüfbar, wiederanlauffähig und für den Regelbetrieb tragfähig.

## 19. Quellenbasis zur fachlichen Vertiefung

Die wichtigsten Quellen für dein weiteres Lernen sind BSI-Standard 200-4 für Business Continuity Management, BSI IT-Grundschutz CON.3 für Datensicherungskonzepte, BSI DER.2.1 für die Behandlung von Sicherheitsvorfällen, NIST SP 800-34 Rev. 1 für Contingency Planning föderaler Informationssysteme sowie ISO 22301/22313 für Business-Continuity-Management-Systeme und deren Anwendung. Diese Quellen passen gut zu deinem Zielkontext Bundesbehörde, weil sie Organisation, Betrieb, Wiederherstellung, Notfallvorsorge und prüfbare Managementsystematik verbinden. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_4.html?utm_source=chatgpt.com))

<>