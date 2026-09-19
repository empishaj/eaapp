## Checkliste für gute Capability Maps in Bundesbehörden

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| 1. Fähigkeit zuerst, System später | Beginne nicht mit „Was macht System X?“, sondern mit „Welche fachliche Fähigkeit muss die Behörde dauerhaft beherrschen?“ | Nicht „DMS“, sondern „Akte führen“ | TOGAF ist ein etabliertes EA-Framework zur strukturierten Entwicklung von Enterprise Architecture. ([opengroup.org](https://www.opengroup.org/togaf)) |
| 2. Stabile Sprache wählen | Fähigkeiten werden in dauerhaften, fachlichen Begriffen beschrieben, nicht in Projekt- oder Produktnamen. | „Identität prüfen“ statt „Projekt eID-Modernisierung“ | Eigene EA-Praxis, angelehnt an Capability-Based Planning |
| 3. Klare Hierarchie bauen | Eine Capability Map braucht Ebenen: Domäne, Capability, Sub-Capability. | „Antragsmanagement → Antrag entgegennehmen → Eingangskanal validieren“ | ArchiMate unterstützt die Modellierung und Analyse von Beziehungen zwischen Business-Domänen. ([opengroup.org](https://www.opengroup.org/archimate-forum/archimate-overview)) |
| 4. Prozesse nicht mit Fähigkeiten verwechseln | Eine Fähigkeit beschreibt, was die Organisation können muss; ein Prozess beschreibt, wie es abläuft. | Fähigkeit: „Bescheid erstellen“; Prozess: „Bescheid prüfen, freigeben, versenden“ | Eigene EA-Praxis |
| 5. Organisationseinheiten nicht als Fähigkeiten modellieren | Referate, Abteilungen oder Teams sind Verantwortungsstrukturen, keine fachlichen Fähigkeiten. | „Referat 42“ ist keine Capability; „Fachentscheidung treffen“ ist eine Capability | Eigene EA-Praxis |
| 6. Anwendungen nur zuordnen, nicht als Ausgangspunkt nehmen | Anwendungen unterstützen Fähigkeiten, sie sind nicht die Fähigkeiten selbst. | Fachverfahren A unterstützt „Vorgang bearbeiten“ | ArchiMate erlaubt die Visualisierung von Beziehungen zwischen Business-, Application- und Technology-Domänen. ([opengroup.org](https://www.opengroup.org/archimate-forum/archimate-overview)) |
| 7. Datenobjekte sichtbar machen | Jede wichtige Fähigkeit verarbeitet, erzeugt oder nutzt Daten. | „Nachweise verwalten“ nutzt Nachweisdaten, Dokumentmetadaten, Prüfstatus | Eigene EA-Praxis |
| 8. Schutzbedarf verknüpfen | Fähigkeiten mit personenbezogenen Daten, Bescheiden oder Zahlungen brauchen Sicherheitsbewertung. | „Identität prüfen“ hat hohen Bedarf an Vertraulichkeit und Integrität | Das BSI bewertet Schutzbedarf anhand möglicher Schäden für Vertraulichkeit, Integrität und Verfügbarkeit. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html)) |
| 9. Risiken pro Fähigkeit erfassen | Modernisierungsbedarf entsteht dort, wo wichtige Fähigkeiten schwach unterstützt werden. | Manuelle Nachweispflege, Medienbrüche, unklare Datenhoheit | Eigene EA-Praxis |
| 10. Roadmap aus Fähigkeiten ableiten | Maßnahmen werden nicht als lose IT-Projekte geplant, sondern als Verbesserung konkreter Fähigkeiten. | „Nachweismanagement modernisieren“ statt „Tool X einführen“ | TOGAF nutzt Enterprise Architecture zur Verbesserung geschäftlicher Wirksamkeit. ([opengroup.org](https://www.opengroup.org/togaf)) |
| 11. Leitungssprache nutzen | Für Führungskräfte zählt: Handlungsfähigkeit, Risiko, Priorität, Wirkung, Abhängigkeit. | „Diese Fähigkeit ist kritisch für Bearbeitungszeit und Rechtskonformität.“ | Eigene EA-Praxis |
| 12. Karte aktuell halten | Capability Maps sind Steuerungsinstrumente, keine einmaligen Workshopbilder. | Quartalsweise Aktualisierung im Architekturboard | Eigene EA-Praxis |

## Grundidee: Was ist eine Capability Map?

Eine Capability Map ist eine fachliche Landkarte der Fähigkeiten einer Organisation. Sie beantwortet nicht zuerst die Frage, welche Anwendungen existieren, welche Projekte laufen oder welche Referate zuständig sind. Sie beantwortet zuerst die deutlich wichtigere Architekturfrage: „Was muss diese Behörde dauerhaft können, um ihren gesetzlichen Auftrag zuverlässig zu erfüllen?“ Genau deshalb ist Capability Mapping für Enterprise Architecture so mächtig. Es trennt das stabile fachliche Können von den oft wechselnden Prozessen, Systemen, Projekten, Organisationseinheiten und Dienstleisterstrukturen.

Eine Fähigkeit ist dabei kein einzelner Arbeitsschritt. Sie ist eine organisatorische Befähigung. Eine Bundesbehörde muss zum Beispiel Anträge entgegennehmen, Identitäten prüfen, Nachweise verwalten, Vorgänge bearbeiten, Fachentscheidungen treffen, Bescheide erstellen, Akten führen, Zahlungen auslösen und Berichtspflichten erfüllen können. Diese Fähigkeiten bleiben fachlich erkennbar, auch wenn morgen ein neues Portal, ein anderes Fachverfahren, eine neue DMS-Lösung, ein zentraler IAM-Dienst oder eine andere Betriebsplattform eingeführt wird.

Genau hier liegt der Architekturwert. Wenn du bei Systemnamen beginnst, beschreibst du den aktuellen Maschinenraum. Wenn du bei Fähigkeiten beginnst, beschreibst du die fachliche Leistungsfähigkeit der Behörde. Das ist der Unterschied zwischen Inventur und Steuerung.

## Der zentrale Unterschied: Fähigkeit, Prozess, Organisation, Anwendung und Projekt

| Aspekt | Details/Erklärung | Beispiel | Typischer Fehler | Literatur/Quelle |
|---|---|---|---|---|
| Fähigkeit / Capability | Beschreibt, was die Behörde dauerhaft können muss. Sie ist relativ stabil und fachlich formuliert. | „Identität prüfen“, „Bescheid erstellen“, „Akte führen“ | Fähigkeiten als Systeme benennen: „DMS nutzen“, „SAP bedienen“ | Capability-Based Planning ist ein etablierter EA-Ansatz; TOGAF ist als EA-Framework breit eingesetzt. ([opengroup.org](https://www.opengroup.org/togaf)) |
| Prozess | Beschreibt, wie eine Fähigkeit in einem konkreten Ablauf ausgeführt wird. Prozesse haben Reihenfolge, Rollen, Ereignisse und Entscheidungen. | Antrag eingeht, Vorprüfung erfolgt, Nachforderung wird erstellt, Fachprüfung wird durchgeführt | Prozessschritte als Capabilities modellieren: „Formular öffnen“, „E-Mail schreiben“ | Prozessarchitektur ergänzt Capability Mapping |
| Organisationseinheit | Beschreibt, wer formal zuständig ist. Organisationseinheiten können sich ändern, ohne dass die Fähigkeit verschwindet. | Referat A, Sachgebiet B, Außenstelle C | Referatsnamen als Capabilities übernehmen | Organisationsmodell ist eine eigene Sicht |
| Anwendung | Beschreibt, womit eine Fähigkeit technisch unterstützt wird. Eine Anwendung kann mehrere Fähigkeiten unterstützen. | Portal, Fachverfahren, DMS/eAkte, IAM, Zahlungsmodul | Anwendung als Ausgangspunkt der Zielarchitektur nehmen | ArchiMate unterstützt Beziehungen zwischen Business-, Application- und Technology-Domänen. ([opengroup.org](https://www.opengroup.org/archimate-forum/archimate-overview)) |
| Projekt / Maßnahme | Beschreibt eine zeitlich begrenzte Veränderungsinitiative. Projekte verbessern, ersetzen oder schaffen Fähigkeiten. | „Modernisierung Nachweismanagement 2027“ | Projektname als dauerhafte Fähigkeit modellieren | In ArchiMate werden Umsetzungsaktivitäten über Implementation-&-Migration-Elemente wie Work Package, Plateau und Gap modelliert. ([opengroup.org](https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf)) |

Die saubere Denkregel lautet: Eine Fähigkeit ist ein dauerhaftes Können. Ein Prozess ist der Ablauf dieses Könnens. Eine Organisationseinheit ist die Zuständigkeit dafür. Eine Anwendung ist ein technisches Mittel. Ein Projekt ist eine zeitlich begrenzte Veränderung. Sobald diese fünf Dinge vermischt werden, wird die Architektur unklar.

## Warum Enterprise Architecture bei Fähigkeiten beginnen sollte

Enterprise Architecture beginnt bei Fähigkeiten, weil Fähigkeiten die Brücke zwischen Auftrag, Organisation, Daten, Anwendungen, Infrastruktur, Risiken und Investitionen bilden. Ein Systemname sagt wenig darüber aus, warum dieses System wichtig ist. Eine Fähigkeit sagt dagegen sehr viel: Sie zeigt, welcher Teil des behördlichen Auftrags betroffen ist, welche Fachprozesse davon abhängen, welche Daten verarbeitet werden, welche Anwendungen unterstützen, welche Risiken bestehen und welche Modernisierungsmaßnahmen Priorität haben.

Nehmen wir ein Fachverfahren namens „FV-Alpha“. Der Name sagt fast nichts. Unterstützt es die Antragsannahme? Die Fachentscheidung? Die Bescheiderstellung? Die Aktenführung? Die Zahlung? Ohne Capability Map bleibt unklar, ob FV-Alpha fachlich kritisch, technisch ersetzbar, organisatorisch zentral oder nur historisch gewachsen ist. Erst wenn du FV-Alpha auf Fähigkeiten legst, erkennst du seinen Architekturwert.

Das ist besonders in Bundesbehörden wichtig, weil dort Fachlichkeit, Recht, Organisation, IT-Betrieb, Datenschutz, Informationssicherheit, Haushaltslogik, Dienstleistersteuerung und politische Erwartung miteinander verbunden sind. Eine Capability Map hilft, diese Komplexität nicht über Systemlisten, sondern über fachliche Leistungsfähigkeit zu ordnen.

## Beispiel: Capability Map für ein Verwaltungsverfahren

Für dein Beispiel bauen wir eine Capability Map in drei Ebenen. Ebene 1 beschreibt große fachliche Domänen. Ebene 2 beschreibt zentrale Fähigkeiten. Ebene 3 beschreibt konkrete Sub-Fähigkeiten, die später mit Prozessen, Anwendungen, Daten und Maßnahmen verbunden werden können.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Ebene 1: Capability Domain | Grober fachlicher Fähigkeitsbereich. Diese Ebene ist für Leitung, Strategie und Portfolio geeignet. | Antragsmanagement, Identitäts- und Nachweismanagement, Vorgangsmanagement | Eigene EA-Praxis |
| Ebene 2: Business Capability | Konkrete Fähigkeit, die die Behörde dauerhaft beherrschen muss. | Antrag entgegennehmen, Identität prüfen, Bescheid erstellen | Eigene EA-Praxis |
| Ebene 3: Sub-Capability | Feiner zerlegte Fähigkeit, die für Analyse, Bewertung und Modernisierung geeignet ist. | Eingangskanal validieren, Nachweisstatus prüfen, Bescheidversion erzeugen | Eigene EA-Praxis |

### Capability Map – Ebene 1 bis 3

| Aspekt | Details/Erklärung | Beispiel | Relevanz für Modernisierung |
|---|---|---|---|
| 1. Antragsmanagement | Fähigkeit, Anträge rechtsverbindlich, vollständig und kanalübergreifend entgegenzunehmen. | Antrag entgegennehmen; Eingang bestätigen; Fristbeginn feststellen; Eingangskanal validieren | Hoch, wenn Anträge per Papier, E-Mail, Portal und Fachverfahren parallel eingehen |
| 2. Identitäts- und Nachweismanagement | Fähigkeit, Identität, Vertretungsberechtigung und Nachweise korrekt zu prüfen und zu verwalten. | Identität prüfen; Nachweise verwalten; Nachforderungen auslösen; Nachweisstatus pflegen | Sehr hoch, wenn Nachweise mehrfach abgelegt, manuell geprüft oder nicht eindeutig zuordenbar sind |
| 3. Vorgangsmanagement | Fähigkeit, einen Verwaltungsfall strukturiert, nachvollziehbar und statusgeführt zu bearbeiten. | Vorgang anlegen; Vorgang bearbeiten; Fristen überwachen; Status steuern; Wiedervorlage verwalten | Sehr hoch, wenn Bearbeitungsstände unklar sind oder manuelle Listen genutzt werden |
| 4. Entscheidungsmanagement | Fähigkeit, fachliche Prüfungen, Regelanwendung und Entscheidungen nachvollziehbar durchzuführen. | Fachentscheidung treffen; Prüfkriterien anwenden; Vier-Augen-Prüfung durchführen; Entscheidung dokumentieren | Hoch, wenn Entscheidungslogik in Excel, E-Mails oder Erfahrungswissen liegt |
| 5. Bescheidmanagement | Fähigkeit, Bescheide korrekt, nachvollziehbar, versioniert und zustellfähig zu erstellen. | Bescheid erstellen; Textbausteine nutzen; Rechtsbehelfsbelehrung einfügen; Freigabe durchführen | Hoch, wenn Bescheide manuell zusammengesetzt oder uneinheitlich erzeugt werden |
| 6. Kommunikationsmanagement | Fähigkeit, Kommunikation mit Antragstellern, Behörden, Dienstleistern und internen Stellen zu führen. | Kommunikation führen; Nachricht versenden; Nachforderung kommunizieren; Rückfragen dokumentieren | Hoch, wenn Kommunikation außerhalb der Akte oder ohne Statusbezug stattfindet |
| 7. Akten- und Dokumentenmanagement | Fähigkeit, aktenrelevante Informationen vollständig, revisionssicher und auffindbar zu führen. | Akte führen; Dokument ablegen; Metadaten pflegen; Aufbewahrung steuern; Löschung vorbereiten | Sehr hoch, wenn DMS/eAkte nicht sauber integriert ist |
| 8. Zahlungs- und Leistungsmanagement | Fähigkeit, Zahlungen, Erstattungen oder Gebühren fachlich korrekt auszulösen und nachzuverfolgen. | Zahlung auslösen; Zahlungsstatus prüfen; Rückforderung vorbereiten; Buchungsdaten übergeben | Hoch, wenn finanzwirksame Entscheidungen betroffen sind |
| 9. Berichts- und Steuerungsmanagement | Fähigkeit, Berichtspflichten, Kennzahlen, Controlling und Nachweise gegenüber Leitung oder Aufsicht zu erfüllen. | Berichtspflichten erfüllen; Fallzahlen melden; Bearbeitungszeiten auswerten; Qualitätsindikatoren liefern | Hoch, wenn Reporting aus manuellen Abfragen entsteht |
| 10. Querschnittliche Steuerungsfähigkeit | Fähigkeit, Sicherheit, Datenschutz, Rollen, Qualität und Betrieb fachlich-technisch beherrschbar zu halten. | Rollenmodell steuern; Schutzbedarf bewerten; Audit Logs auswerten; Dienstleisterleistung überwachen | Sehr hoch, wenn Verantwortlichkeiten unklar sind |

Eine solche Map ist noch kein Prozessmodell und keine Applikationslandkarte. Sie ist die fachliche Ordnungsschicht darüber. Aus ihr kannst du später BPMN-Prozesse, Datenlandkarten, Schnittstellenverträge, Applikationsportfolio-Bewertungen, Schutzbedarfsanalysen, Zielarchitekturen und Roadmaps ableiten.

## Wie du aus dem Verwaltungsbeispiel eine saubere Hierarchie baust

Die von dir genannten Begriffe sind bereits ein guter Start, aber fachlich noch gemischt. „Antrag entgegennehmen“, „Identität prüfen“, „Nachweise verwalten“, „Vorgang bearbeiten“, „Fachentscheidung treffen“, „Bescheid erstellen“, „Kommunikation führen“, „Akte führen“, „Zahlung auslösen“ und „Berichtspflichten erfüllen“ sind gute Ebene-2-Fähigkeiten. Für eine belastbare Capability Map musst du sie clustern, normalisieren und hierarchisieren.

| Aspekt | Details/Erklärung | Beispiel | Entscheidung |
|---|---|---|---|
| Normalisierung | Formuliere Fähigkeiten als fachliche Verb-Nomen-Kombination. | „Antrag entgegennehmen“, „Nachweis verwalten“, „Bescheid erstellen“ | Gut |
| Clusterung | Ordne verwandte Fähigkeiten in Domänen. | „Antrag entgegennehmen“ gehört zu Antragsmanagement | Notwendig |
| Granularität | Zerlege nur so tief, wie Entscheidungen daraus entstehen. | „Nachweisstatus pflegen“ ist sinnvoll; „Button Speichern klicken“ nicht | Entscheidungsebene beachten |
| Stabilität | Vermeide temporäre Projekt- oder Systembegriffe. | „Akte führen“ statt „eAkte-Rollout nutzen“ | Pflicht |
| Verantwortbarkeit | Jede Fähigkeit braucht perspektivisch einen fachlichen Owner. | „Nachweismanagement“ hat Data Owner und Prozessverantwortung | Pflicht |
| Bewertbarkeit | Jede Fähigkeit muss hinsichtlich Reife, Risiko und Zielbild bewertbar sein. | Reifegrad 2 von 5, hoher Medienbruch, Zielbild API-integriert | Pflicht |

Eine gute Capability Map hat meistens drei Ebenen. Mehr Ebenen führen in frühen Phasen oft zu Scheingenauigkeit. Weniger Ebenen sind für Modernisierungsentscheidungen oft zu grob. Die praktische Regel lautet: Ebene 1 ist für Leitung, Ebene 2 für Architektur- und Portfolioentscheidungen, Ebene 3 für Analyse, Interviews und Maßnahmenplanung.

## Beispielmodell: Capability Map als textuelles Architekturmodell

### Ebene 1: Fachliche Domänen

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Antragsmanagement | Eingang, Annahme, Plausibilität, Friststart und Eingangsbestätigung | Antrag entgegennehmen | Eigene EA-Praxis |
| Identitäts- und Nachweismanagement | Identität, Berechtigung, Nachweise, Nachforderung, Nachweisstatus | Identität prüfen, Nachweise verwalten | Eigene EA-Praxis |
| Vorgangs- und Entscheidungsmanagement | Fallanlage, Bearbeitung, Prüfung, Entscheidung, Qualitätssicherung | Vorgang bearbeiten, Fachentscheidung treffen | Eigene EA-Praxis |
| Bescheid- und Kommunikationsmanagement | Bescheiderstellung, Versand, Kommunikation, Zustellung, Rückfragen | Bescheid erstellen, Kommunikation führen | Eigene EA-Praxis |
| Akten- und Dokumentenmanagement | Aktenführung, Dokumentablage, Metadaten, Aufbewahrung, Löschung | Akte führen | Eigene EA-Praxis |
| Zahlungs- und Berichtswesen | Zahlung, Abrechnung, Berichte, Kennzahlen, Meldepflichten | Zahlung auslösen, Berichtspflichten erfüllen | Eigene EA-Praxis |

### Ebene 2 und 3: Konkrete Fähigkeiten

| Aspekt | Details/Erklärung | Beispiel | Risiken |
|---|---|---|---|
| Antrag entgegennehmen | Fähigkeit, einen Antrag über zulässige Kanäle vollständig und nachvollziehbar zu erfassen. | Online-Antrag, Papierformular, E-Mail-Eingang, persönliche Vorsprache | Medienbruch, Doppeleingabe, unklarer Fristbeginn |
| Eingang validieren | Fähigkeit, Mindestangaben, Signatur/Authentisierung, Zuständigkeit und Vollständigkeit zu prüfen. | Prüfung auf Pflichtfelder, Mandant, Aktenzeichen | Unvollständige Vorgänge, manuelle Rückfragen |
| Identität prüfen | Fähigkeit, natürliche oder juristische Personen verlässlich zu identifizieren. | eID, Ausweisdokument, Registerabgleich, Vertretungsnachweis | Identitätsfehler, unberechtigter Zugriff |
| Nachweise verwalten | Fähigkeit, Nachweise anzufordern, entgegenzunehmen, zuzuordnen, zu prüfen und aufzubewahren. | Einkommensnachweis, Aufenthaltsnachweis, Bescheinigung | Verlust, Mehrfachablage, unklare Gültigkeit |
| Vorgang bearbeiten | Fähigkeit, Fallstatus, Zuständigkeit, Bearbeitungsschritte und Fristen zu steuern. | Vorgangsakte, Wiedervorlage, Aufgabenliste | Liegezeiten, unklare Verantwortung, Schattenlisten |
| Fachentscheidung treffen | Fähigkeit, fachliche Regeln auf den Fall anzuwenden und das Ergebnis nachvollziehbar zu begründen. | Bewilligung, Ablehnung, Teilbewilligung | Intransparente Entscheidungslogik |
| Bescheid erstellen | Fähigkeit, aus Entscheidung, Rechtsgrundlage und Textbausteinen einen korrekten Bescheid zu erzeugen. | PDF-Bescheid, digitale Zustellung, Postversand | Fehlerhafte Texte, uneinheitliche Bescheide |
| Kommunikation führen | Fähigkeit, fallbezogene Kommunikation vollständig, nachvollziehbar und adressatengerecht zu führen. | Nachforderung, Rückfrage, Anhörung, Statusinformation | Kommunikation außerhalb der Akte |
| Akte führen | Fähigkeit, alle aktenrelevanten Informationen strukturiert, auffindbar und aufbewahrungsgerecht zu führen. | DMS/eAkte, Dokumentmetadaten, Aktenplan | Aktenunvollständigkeit, Suchprobleme |
| Zahlung auslösen | Fähigkeit, finanzwirksame Vorgänge korrekt an Haushalts-, Kassen- oder Zahlungssysteme zu übergeben. | Auszahlung, Gebühr, Rückforderung | Zahlungsfehler, Abstimmungsaufwand |
| Berichtspflichten erfüllen | Fähigkeit, steuerungs- und meldepflichtige Informationen korrekt bereitzustellen. | Fallzahlen, Bearbeitungszeit, Statusstatistik | Manuelle Auswertung, uneinheitliche Zahlen |

## Wie du Fähigkeiten mit Anwendungen, Daten, Schnittstellen, Schutzbedarf, Verantwortung, Risiken und Roadmap verbindest

Eine Capability Map wird erst dann wirklich wertvoll, wenn du sie nicht als reine Fachlandkarte stehen lässt, sondern mit Architekturinformationen anreicherst. Der wichtigste Schritt ist die Verknüpfung: Jede Fähigkeit bekommt Anwendungen, Datenobjekte, Schnittstellen, Verantwortlichkeiten, Schutzbedarf, Risiken und Maßnahmen. Dadurch wird aus einer schönen Übersicht ein Steuerungsinstrument.

| Aspekt | Details/Erklärung | Beispiel | Architekturentscheidung |
|---|---|---|---|
| Fähigkeit | Was muss die Behörde dauerhaft können? | Nachweise verwalten | Capability bleibt fachlich stabil |
| Unterstützende Anwendungen | Welche Systeme unterstützen diese Fähigkeit heute? | Portal, Fachverfahren, DMS/eAkte | Erkennen von Überlappung und Redundanz |
| Datenobjekte | Welche fachlichen Daten werden erzeugt, gelesen, verändert oder archiviert? | Nachweisdokument, Nachweisstatus, Gültigkeitsdatum, Dokumentmetadaten | Data Ownership und führendes System klären |
| Schnittstellen | Welche Systeme tauschen Daten aus? | Portal → Fachverfahren; Fachverfahren → DMS; Fachverfahren → Register | Schnittstellenvertrag erforderlich |
| Schutzbedarf | Welche Anforderungen bestehen an Vertraulichkeit, Integrität und Verfügbarkeit? | Personenbezogene Nachweise: Vertraulichkeit hoch; Prüfstatus: Integrität hoch | Sicherheitsanforderungen ableiten |
| Verantwortung | Wer trägt fachliche, technische und betriebliche Verantwortung? | Fachbereich als Capability Owner, IT als Application Owner, Betrieb als Service Owner | Governance klären |
| Risiken | Wo entstehen fachliche, technische oder betriebliche Schwachstellen? | Manuelle Zuordnung, doppelte Ablage, fehlende Statussynchronisation | Modernisierungsbedarf begründen |
| Roadmap-Maßnahme | Welche Veränderung verbessert die Fähigkeit? | Zentrales Nachweismanagement mit DMS-Integration und Status-API | Maßnahme priorisieren |

Beim Schutzbedarf solltest du dich in Bundesbehörden eng an die Grundlogik des BSI halten: Es geht nicht abstrakt um „sicher“ oder „unsicher“, sondern um mögliche Schäden, wenn Vertraulichkeit, Integrität oder Verfügbarkeit eines Zielobjekts beeinträchtigt werden. Der BSI-Standard 200-2 beschreibt die Schutzbedarfsbetrachtung für IT-Systeme bezogen auf diese Grundwerte; der Schutzbedarf eines IT-Systems leitet sich in der Praxis aus den unterstützten Anwendungen, Daten und Prozessen ab. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_2.pdf?__blob=publicationFile&v=2))

## Beispiel: Capability-to-Application-to-Data-Mapping

| Aspekt | Details/Erklärung | Beispiel | Risiken | Roadmap-Impuls |
|---|---|---|---|---|
| Antrag entgegennehmen | Portal und Poststelle erfassen Anträge, Fachverfahren legt Vorgang an. | Portal, Eingangsbuch, Fachverfahren; Datenobjekte: Antrag, Antragsteller, Eingangsdatum | Papier- und Onlinekanal nicht synchron; Fristbeginn unklar | Einheitlicher Eingangsdienst mit eindeutiger Vorgangs-ID |
| Identität prüfen | Identitätsdaten werden geprüft und mit Antrag verknüpft. | IAM/eID, Fachverfahren, Registerschnittstelle; Datenobjekte: Identität, Vertretung, Prüfstatus | Manuelle Prüfung, keine eindeutige Prüfhistorie | Standardisierte Identitätsprüfung mit Audit-Trail |
| Nachweise verwalten | Nachweise werden angefordert, empfangen, geprüft und abgelegt. | Portal, Fachverfahren, DMS/eAkte; Datenobjekte: Nachweis, Dokument, Gültigkeit | Doppelte Ablage, fehlende Metadaten, unklare Version | Zentrales Nachweisobjekt und DMS-Integration |
| Vorgang bearbeiten | Fall wird statusgeführt bearbeitet. | Fachverfahren, Workflow-Komponente; Datenobjekte: Vorgang, Status, Aufgabe, Frist | Schattenlisten, unklare Bearbeitungsstände | Vorgangsstatusmodell harmonisieren |
| Fachentscheidung treffen | Fachregeln werden angewendet und Ergebnis dokumentiert. | Fachverfahren, Regelwerk/DMN, Wissensdatenbank; Datenobjekte: Prüfergebnis, Entscheidungsgrundlage | Regelwissen in Köpfen oder Excel | Entscheidungslogik externalisieren und versionieren |
| Bescheid erstellen | Entscheidung wird in rechtssicheren Bescheid überführt. | Fachverfahren, Vorlagenservice, DMS/eAkte, Versanddienst | Manuelle Textbausteine, fehlende Versionierung | Zentraler Bescheidservice mit Vorlagen-Governance |
| Akte führen | Dokumente und relevante Ereignisse werden aktenkonform abgelegt. | DMS/eAkte, Fachverfahren; Datenobjekte: Akte, Dokument, Metadaten | Akte nicht vollständig, Kommunikation fehlt | Aktenintegrationsstandard definieren |
| Zahlung auslösen | Finanzwirksame Entscheidung wird an Zahlungssystem übergeben. | Fachverfahren, Haushalts-/Kassensystem; Datenobjekte: Zahlungsauftrag, Betrag, Empfänger | Medienbruch, manuelle Übertragung | Sichere Zahlungsübergabe mit Rückmeldestatus |
| Berichtspflichten erfüllen | Steuerungsdaten werden aggregiert und berichtet. | BI/Reporting, Fachverfahren; Datenobjekte: Fallzahl, Status, Bearbeitungsdauer | Uneinheitliche Kennzahlen, Excel-Reporting | Fachliches Kennzahlenmodell etablieren |

## Die wichtigste Modellierungsregel: Capability Maps sind keine Organigramme

Ein häufiger Fehler in Behörden besteht darin, die Capability Map entlang der bestehenden Aufbauorganisation zu zeichnen. Das wirkt zunächst naheliegend, ist aber architektonisch schwach. Ein Organigramm sagt, wer heute zuständig ist. Eine Capability Map sagt, was dauerhaft beherrscht werden muss. Diese Unterscheidung ist entscheidend, weil Modernisierung oft gerade dann nötig wird, wenn Fähigkeiten über mehrere Referate, Dienstleister, Systeme und Datenquellen verteilt sind.

Beispiel: „Nachweise verwalten“ kann fachlich im Fachbereich liegen, technisch im Fachverfahren umgesetzt sein, dokumentarisch im DMS stattfinden, organisatorisch von einer Poststelle unterstützt werden und sicherheitlich vom IAM abhängen. Wenn du nur das Organigramm anschaust, siehst du Zuständigkeiten. Wenn du die Fähigkeit anschaust, siehst du die tatsächliche Leistungsfähigkeit und ihre Abhängigkeiten.

## Schritt-für-Schritt-Methode zum Erstellen einer Capability Map

| Aspekt | Details/Erklärung | Ergebnis | Qualitätssignal |
|---|---|---|---|
| Schritt 1: Auftrag und Scope klären | Kläre, welches Verwaltungsverfahren, welche Behörde, welche Abteilung oder welches Leistungsbündel betrachtet wird. | Scope-Statement | Es ist klar, was innerhalb und außerhalb der Betrachtung liegt |
| Schritt 2: Fachlichen Wertstrom verstehen | Beschreibe grob, wie aus einem Auslöser ein Ergebnis entsteht. | Value-Stream-Skizze | Du kannst erklären, wie Antrag, Prüfung, Entscheidung und Bescheid zusammenhängen |
| Schritt 3: Fähigkeiten sammeln | Sammle stabile fachliche Fähigkeiten, ohne Systeme, Referate oder Projekte zu verwenden. | Roh-Capability-Liste | Begriffe sind fachlich, dauerhaft und verständlich |
| Schritt 4: Fähigkeiten normalisieren | Formuliere einheitlich mit Verb + Objekt. | Bereinigte Capability-Liste | Keine Dubletten, keine Systemnamen, keine Prozessmikroschritte |
| Schritt 5: Fähigkeiten clustern | Ordne Fähigkeiten in Domänen. | Ebene-1-Map | Leitung kann die Karte in fünf Minuten verstehen |
| Schritt 6: Hierarchie bilden | Zerlege wichtige Fähigkeiten in Sub-Capabilities. | Ebene-2-/Ebene-3-Map | Detailgrad unterstützt Entscheidungen |
| Schritt 7: Anwendungen zuordnen | Lege je Fähigkeit unterstützende Anwendungen, Services und manuelle Hilfsmittel darunter. | Capability-to-Application-Matrix | Redundanzen und Lücken werden sichtbar |
| Schritt 8: Datenobjekte zuordnen | Erfasse zentrale Datenobjekte je Fähigkeit. | Capability-to-Data-Matrix | Führende Systeme und Datenrisiken werden diskutierbar |
| Schritt 9: Schnittstellen erfassen | Ordne relevante Datenflüsse und Integrationen zu. | Schnittstellenübersicht | Medienbrüche und Integrationsrisiken werden sichtbar |
| Schritt 10: Schutzbedarf und Kritikalität bewerten | Bewerte fachliche Kritikalität, Schutzbedarf, Nutzerwirkung und Betriebsrelevanz. | Bewertete Capability Map | Priorisierung wird begründbar |
| Schritt 11: Reife und Zielbild bewerten | Bewerte Ist-Reife und Soll-Reife je Fähigkeit. | Heatmap | Modernisierungsbedarf wird sichtbar |
| Schritt 12: Maßnahmen ableiten | Leite Roadmap-Maßnahmen aus Gaps ab. | Capability-basierte Roadmap | Projekte sind mit fachlicher Wirkung verbunden |

## Reifegradmodell für Capability Maps

Ein einfacher Reifegrad reicht häufig aus. Wichtig ist, dass du ihn konsequent anwendest und nicht zu fein wirst.

| Aspekt | Details/Erklärung | Beispiel | Bewertung |
|---|---|---|---|
| Reifegrad 1: Ad hoc | Fähigkeit existiert, ist aber stark personenabhängig, manuell oder uneinheitlich. | Nachweise werden per E-Mail empfangen und lokal abgelegt. | Kritisch |
| Reifegrad 2: Teilweise strukturiert | Es gibt Systeme oder Regeln, aber keine durchgängige Integration. | Nachweise liegen im DMS, Status wird im Fachverfahren manuell gepflegt. | Schwach |
| Reifegrad 3: Standardisiert | Fähigkeit ist prozessual und systemisch geordnet. | Nachweise werden standardisiert zugeordnet und statusgeführt geprüft. | Solide |
| Reifegrad 4: Integriert | Anwendungen, Daten, Schnittstellen und Rollenmodell sind gut verbunden. | Portal, Fachverfahren und DMS teilen Status und Metadaten. | Gut |
| Reifegrad 5: Steuerbar und optimierbar | Fähigkeit ist messbar, automatisierbar, überwacht und kontinuierlich verbesserbar. | Durchlaufzeiten, Fehlerquoten und Nachforderungsgründe sind auswertbar. | Sehr gut |

Für Bundesbehörden ist Reifegrad 5 nicht immer notwendig. Nicht jede Fähigkeit muss maximal automatisiert sein. Die Zielreife hängt von Fallzahl, Risiko, Schutzbedarf, gesetzlicher Bedeutung, Nutzerwirkung, Betriebsaufwand und strategischem Zielbild ab.

## Priorisierung: Welche Fähigkeiten zuerst modernisieren?

Du solltest Modernisierung nicht nach Lautstärke, Systemalter oder Projektverfügbarkeit priorisieren. Besser ist eine Matrix aus fachlicher Kritikalität, Risiko, Reife, Schutzbedarf, Nutzerwirkung und strategischer Bedeutung.

| Aspekt | Details/Erklärung | Beispiel | Bewertungslogik |
|---|---|---|---|
| Fachliche Kritikalität | Wie stark hängt der gesetzliche Auftrag von dieser Fähigkeit ab? | Fachentscheidung treffen | Hoch, wenn ohne Fähigkeit keine Bescheide möglich sind |
| Fallzahl / Volumen | Wie häufig wird die Fähigkeit genutzt? | Antrag entgegennehmen | Hoch, wenn Massengeschäft betroffen ist |
| Schutzbedarf | Welche Schäden entstehen bei Verlust von Vertraulichkeit, Integrität oder Verfügbarkeit? | Identität prüfen | Hoch bei personenbezogenen Daten oder rechtsverbindlichen Entscheidungen |
| Ist-Reife | Wie stabil, integriert und steuerbar ist die Fähigkeit heute? | Nachweise verwalten | Niedrige Reife erhöht Modernisierungsdruck |
| Technische Schuld | Wie stark behindert die aktuelle IT-Unterstützung Veränderung oder Betrieb? | Legacy-Fachverfahren | Hoch bei veralteter Technologie, fehlenden Schnittstellen |
| Datenrisiko | Gibt es doppelte Datenhaltung, unklare Datenhoheit oder schlechte Qualität? | Vorgangsstatus | Hoch bei widersprüchlichen Statusinformationen |
| Nutzerwirkung | Wie stark betrifft die Fähigkeit Antragsteller, Sachbearbeitung oder Leitung? | Kommunikation führen | Hoch bei vielen Rückfragen und Beschwerden |
| Roadmap-Relevanz | Ist die Fähigkeit Voraussetzung für weitere Modernisierung? | Identitätsmanagement | Hoch, wenn andere Zielbilder davon abhängen |

Eine praktische Formel lautet: Priorität = fachliche Kritikalität × Risiko × Veränderungsnutzen. Eine Fähigkeit mit hohem Risiko und hoher fachlicher Bedeutung bekommt Vorrang, selbst wenn das zugrunde liegende System nicht das älteste ist.

## Capability Map in Leitungssprache erklären

Für Leitung und Gremien solltest du keine Modellierungssprache in den Vordergrund stellen. Du erklärst nicht „Wir haben Capabilities gemappt“, sondern: „Wir haben die fachliche Leistungsfähigkeit der Organisation strukturiert und mit Risiken, Anwendungen, Daten und Modernisierungsmaßnahmen verbunden.“ Das ist verständlicher und anschlussfähiger.

Eine gute Executive-Formulierung wäre:

„Diese Capability Map zeigt, welche Fähigkeiten die Behörde zur Bearbeitung des Verwaltungsverfahrens dauerhaft benötigt. Sie trennt fachlichen Auftrag von aktuellen Systemnamen und macht sichtbar, welche Fähigkeiten kritisch, schwach unterstützt, mehrfach systemisch abgebildet oder besonders risikobehaftet sind. Dadurch können wir Modernisierungsmaßnahmen nicht mehr nur als IT-Projekte diskutieren, sondern als gezielte Verbesserung der behördlichen Handlungsfähigkeit.“

Eine weitere Formulierung für ein Architekturboard:

„Die Karte zeigt nicht, wie die Organisation formal aufgebaut ist, sondern welche fachlichen Fähigkeiten sie erbringen muss. Für jede Fähigkeit sehen wir unterstützende Anwendungen, zentrale Datenobjekte, Schnittstellen, Schutzbedarf, Verantwortlichkeiten, Risiken und geplante Maßnahmen. Damit entsteht eine gemeinsame Entscheidungsgrundlage für Zielarchitektur, Portfolio, Security, Datenverantwortung und Roadmap.“

## Interviewmethode: Wie du Capabilities erhebst

Capability Mapping entsteht nicht am Schreibtisch. Du brauchst Interviews mit Fachbereich, IT, Betrieb, Datenschutz, Informationssicherheit, Architektur, Dienstleistern und Leitung. Dabei musst du verhindern, dass alle sofort über Systeme reden. Dein Job ist, immer wieder auf die fachliche Fähigkeit zurückzuführen.

| Aspekt | Details/Erklärung | Beispielhafte Frage | Worauf du achtest |
|---|---|---|---|
| Auftrag verstehen | Welche gesetzliche oder fachliche Leistung wird erbracht? | „Welche Ergebnisse muss das Verfahren am Ende liefern?“ | Auftrag, Ergebnis, Leistungsversprechen |
| Auslöser erfassen | Was startet den Vorgang? | „Wodurch beginnt ein Fall?“ | Antrag, Registerereignis, Meldung, Frist |
| Ergebnis erfassen | Was ist der fachliche Output? | „Was gilt als abgeschlossener Vorgang?“ | Bescheid, Zahlung, Ablehnung, Aktenabschluss |
| Fähigkeiten sammeln | Was muss die Organisation dafür können? | „Welche fachlichen Fähigkeiten brauchen Sie dafür dauerhaft?“ | Keine Systemnamen akzeptieren |
| Prozesse unterscheiden | Wie läuft die Fähigkeit konkret ab? | „Welche Schritte gehören dazu?“ | BPMN-Kandidat, nicht Capability selbst |
| Daten ermitteln | Welche Informationen werden benötigt oder erzeugt? | „Welche Daten müssen korrekt sein, damit die Fähigkeit funktioniert?“ | Datenobjekte, Qualität, führende Systeme |
| Anwendungen erfassen | Welche Systeme unterstützen die Fähigkeit? | „Welche Anwendungen nutzen Sie dafür heute?“ | Anwendungen später zuordnen, nicht zuerst modellieren |
| Schnittstellen verstehen | Wo werden Daten übergeben? | „Wo verlassen Informationen Ihr System oder kommen aus anderen Systemen?“ | Integrationen, Medienbrüche |
| Risiken erfassen | Wo entstehen Fehler, Verzögerungen oder Nacharbeit? | „Wo müssen Sie heute manuell korrigieren?“ | Modernisierungsbedarf |
| Schutzbedarf erkennen | Was wäre ein relevanter Schaden? | „Was passiert, wenn diese Information falsch, öffentlich oder nicht verfügbar ist?“ | Vertraulichkeit, Integrität, Verfügbarkeit |
| Verantwortung klären | Wer entscheidet fachlich über diese Fähigkeit? | „Wer darf fachliche Regeln ändern?“ | Capability Owner, Data Owner |
| Zielbild erheben | Wie sollte die Fähigkeit in drei Jahren aussehen? | „Was wäre hier eine robuste Zielarbeitsweise?“ | Roadmap, Soll-Reife |

## Gute Interviewfragen nach Zielgruppe

| Aspekt | Details/Erklärung | Beispiel | Zielgruppe |
|---|---|---|---|
| Leitung | Fokus auf Auftrag, Risiko, Wirkung, Priorisierung. | „Welche Fähigkeiten sind für die Erfüllung des gesetzlichen Auftrags unverzichtbar?“ | Abteilungsleitung, Referatsleitung |
| Fachbereich | Fokus auf fachliche Arbeit, Regeln, Daten, Engpässe. | „Welche fachlichen Entscheidungen treffen Sie, und welche Informationen brauchen Sie dafür?“ | Sachbearbeitung, Fachaufsicht |
| IT-Anwendungsbetreuung | Fokus auf Anwendungen, Schnittstellen, Datenhaltung, technische Grenzen. | „Welche Fähigkeiten unterstützt das Fachverfahren tatsächlich, und wo weichen Anwender aus?“ | Application Owner |
| Betrieb | Fokus auf Verfügbarkeit, Monitoring, Wiederanlauf, Abhängigkeiten. | „Welche Komponenten müssen verfügbar sein, damit die Fähigkeit erbracht werden kann?“ | Betrieb, Plattformteam |
| Informationssicherheit | Fokus auf Schutzbedarf, Rollen, Protokollierung, Dienstleisterzugriffe. | „Welche Fähigkeiten verarbeiten besonders schützenswerte oder entscheidungskritische Informationen?“ | ISB, Security Architect |
| Datenschutz | Fokus auf personenbezogene Daten, Zweckbindung, Aufbewahrung, Löschung. | „Welche Datenobjekte werden für welchen Zweck verarbeitet?“ | Datenschutzkoordination |
| Dienstleister | Fokus auf tatsächliche Implementierung, Grenzen, Lieferobjekte. | „Welche Fähigkeiten sind im System hart kodiert, konfigurierbar oder nur manuell lösbar?“ | Externe Auftragnehmer |

## Typische Fehler beim Capability Mapping

| Aspekt | Details/Erklärung | Beispiel | Korrektur |
|---|---|---|---|
| Systemnamen statt Fähigkeiten | Die Karte wird zur Applikationsliste. | „MARIS“, „DMS“, „SAP“, „Portal“ als Capabilities | Erst fachliche Fähigkeit benennen, Systeme darunter legen |
| Organigramm kopieren | Referate werden als Fähigkeitsdomänen modelliert. | „Referat 31“, „Sachgebiet A“ | Fähigkeiten organisationsneutral formulieren |
| Prozessschritte zu fein modellieren | Die Map wird zu einem Ablaufdiagramm. | „Dokument öffnen“, „Feld prüfen“, „E-Mail senden“ | Prozessdetails in BPMN auslagern |
| Projekte als Fähigkeiten modellieren | Temporäre Veränderung wird als dauerhaftes Können dargestellt. | „eAkte-Rollout“, „Registermodernisierung“ | Projekt als Maßnahme an Fähigkeit hängen |
| Zu abstrakte Fähigkeiten | Die Map bleibt wolkig und nicht entscheidungsfähig. | „Verwaltung durchführen“ | Auf konkrete fachliche Fähigkeiten herunterbrechen |
| Zu viele Ebenen | Die Map wird unlesbar und verliert Steuerungswert. | Fünf bis sieben Hierarchieebenen | Für EA meist drei Ebenen nutzen |
| Keine Owner | Niemand fühlt sich verantwortlich. | Fähigkeit „Nachweise verwalten“ ohne fachliche Zuständigkeit | Capability Owner benennen |
| Keine Datenverknüpfung | Datenrisiken bleiben unsichtbar. | Antrag, Nachweis und Bescheid werden nicht als Datenobjekte modelliert | Capability-to-Data-Matrix ergänzen |
| Keine Schutzbedarfslogik | Security wird später als Zusatzthema behandelt. | Identitätsprüfung ohne Schutzbedarfsbezug | Schutzbedarf früh je Fähigkeit/Datenobjekt erfassen |
| Keine Roadmap-Ableitung | Die Map bleibt ein Workshop-Artefakt. | Keine Maßnahmen, keine Priorisierung | Gaps und Work Packages ableiten |

## Capability Mapping und ArchiMate

Wenn du Capability Maps später formal modellieren willst, ist ArchiMate sehr geeignet. ArchiMate ist eine offene Modellierungssprache für Enterprise Architecture, mit der Beziehungen zwischen Business-, Application- und Technology-Domänen beschrieben, analysiert und visualisiert werden können. ([opengroup.org](https://www.opengroup.org/archimate-forum/archimate-overview))

In ArchiMate würdest du „Nachweise verwalten“ als Capability modellieren. Der Geschäftsprozess „Nachweis prüfen“ realisiert oder nutzt diese Fähigkeit. Eine Application Component wie „Fachverfahren“ oder „DMS/eAkte“ unterstützt über Application Services die Fähigkeit. Datenobjekte wie „Nachweis“, „Dokumentmetadaten“ oder „Prüfstatus“ werden von Anwendungen verarbeitet. Eine Roadmap-Maßnahme wird als Work Package modelliert. Der Zielzustand kann als Plateau beschrieben werden, die Differenz zwischen Ist und Ziel als Gap. Die Open-Group-Referenzkarten zu ArchiMate enthalten unter anderem Beziehungen wie Serving und Realization sowie Implementation-&-Migration-Elemente wie Work Package, Plateau und Gap. ([opengroup.org](https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf))

| Aspekt | Details/Erklärung | Beispiel | ArchiMate-Logik |
|---|---|---|---|
| Capability | Fachliche Fähigkeit | Nachweise verwalten | Strategy Layer |
| Business Process | Ablauf, der Fähigkeit ausführt | Nachweis prüfen | Business Layer |
| Business Role | Fachliche Rolle | Sachbearbeitung, Fachaufsicht | Business Layer |
| Application Component | Anwendungskomponente | Fachverfahren, DMS/eAkte | Application Layer |
| Application Service | Nutzbare Anwendungsleistung | Dokument ablegen, Status synchronisieren | Application Layer |
| Data Object | Fachliches Datenobjekt in Anwendungskontext | Nachweis, Prüfstatus, Aktenmetadaten | Application Layer |
| Technology Node | Infrastruktur-/Plattformknoten | Kubernetes-Cluster, Datenbankserver | Technology Layer |
| Work Package | Umsetzungsmaßnahme | Einführung Nachweisservice | Implementation & Migration |
| Plateau | stabiler Ist- oder Zielzustand | Zielarchitektur 2028 | Implementation & Migration |
| Gap | Differenz zwischen Ist und Ziel | Keine zentrale Nachweis-ID | Implementation & Migration |

## Konkrete Umsetzung: Von der Capability Map zur Modernisierungsroadmap

Du gehst praktisch so vor: Zuerst erstellst du die Map. Dann bewertest du jede Fähigkeit. Danach leitest du Gaps ab. Aus den Gaps entstehen Maßnahmen. Diese Maßnahmen gruppierst du zu Roadmap-Paketen.

| Aspekt | Details/Erklärung | Beispiel | Ergebnis |
|---|---|---|---|
| Ist-Fähigkeit bewerten | Wie gut funktioniert die Fähigkeit heute? | Nachweise verwalten: Reifegrad 2 | Ist-Reife |
| Ziel-Fähigkeit definieren | Wie soll die Fähigkeit künftig funktionieren? | Zentrale Nachweis-ID, DMS-Integration, Statusmodell | Soll-Reife |
| Gap formulieren | Was fehlt zwischen Ist und Ziel? | Keine eindeutige Nachweiszuordnung; manuelle Statuspflege | Gap |
| Maßnahme ableiten | Was muss verändert werden? | Nachweisservice einführen; Schnittstelle zum DMS standardisieren | Work Package |
| Abhängigkeiten prüfen | Welche anderen Fähigkeiten müssen vorher verbessert werden? | Identität prüfen und Vorgang bearbeiten liefern Stammdaten | Roadmap-Abhängigkeit |
| Nutzen beschreiben | Welche Wirkung entsteht? | Weniger Nachforderungen, bessere Aktenvollständigkeit, weniger Doppelablage | Business Case |
| Risiko beschreiben | Was passiert ohne Maßnahme? | Weiterhin Medienbrüche, falsche Zuordnungen, lange Bearbeitung | Entscheidungsgrundlage |

Eine gute Maßnahme heißt nicht „DMS-Projekt“. Eine gute Maßnahme heißt zum Beispiel: „Nachweismanagement standardisieren und medienbruchfrei in Fachverfahren und DMS/eAkte integrieren.“ Diese Formulierung sagt sofort, welche Fähigkeit verbessert wird, welche Systeme betroffen sind und welche fachliche Wirkung erwartet wird.

## Mini-Beispiel einer Capability-basierten Roadmap

| Aspekt | Details/Erklärung | Beispiel | Priorität |
|---|---|---|---|
| Q1–Q2: Transparenz herstellen | Fähigkeiten, Anwendungen, Datenobjekte, Schnittstellen und Risiken erfassen. | Capability Map und Capability-to-Application-Matrix erstellen | Hoch |
| Q2–Q3: Kritische Daten klären | Führende Systeme, Datenqualität und Datenverantwortung bestimmen. | Antrag, Vorgang, Nachweis, Bescheid, Zahlungsauftrag | Hoch |
| Q3–Q4: Nachweismanagement verbessern | Größten Medienbruch reduzieren. | Nachweis-ID, DMS-Metadaten, Statusmodell | Sehr hoch |
| Q4–Q1: Bescheidservice standardisieren | Bescheiderstellung vereinheitlichen. | Vorlagen-Governance, Versionierung, Freigabeprozess | Mittel bis hoch |
| Q1–Q2: Reporting stabilisieren | Steuerungsfähigkeit verbessern. | Einheitliches Kennzahlenmodell, Datenqualitätsregeln | Mittel |
| Q2–Q4: Plattform- und Integrationszielbild umsetzen | Schnittstellen, IAM, Monitoring und Betrieb professionalisieren. | API-Gateway, IAM-Anbindung, Observability | Hoch |

## Übung: Capability Map für ein fiktives Bundesverfahren erstellen

Du bekommst ein fiktives Verfahren: Eine Bundesbehörde bearbeitet Anträge auf eine bestimmte Leistung. Anträge kommen über ein Online-Portal, per Post und über andere Behörden. Die Sachbearbeitung prüft Identität, Zuständigkeit, Nachweise und fachliche Voraussetzungen. Danach wird ein Bescheid erstellt, in der eAkte abgelegt, versendet und bei Bewilligung eine Zahlung ausgelöst. Die Leitung benötigt monatliche Berichte zu Fallzahlen, Bearbeitungszeiten, Ablehnungsgründen und offenen Vorgängen.

Deine Aufgabe besteht darin, eine Capability Map mit drei Ebenen zu erstellen. Ebene 1 enthält maximal sechs Domänen. Ebene 2 enthält zehn bis fünfzehn Fähigkeiten. Ebene 3 enthält für fünf besonders wichtige Fähigkeiten jeweils drei bis fünf Sub-Fähigkeiten. Danach ordnest du zu jeder Ebene-2-Fähigkeit mindestens eine Anwendung, ein Datenobjekt, eine Schnittstelle oder einen manuellen Medienbruch, einen Schutzbedarfsaspekt, einen Owner, ein Risiko und eine mögliche Roadmap-Maßnahme zu.

### Bewertungskriterien für deine Lösung

| Aspekt | Details/Erklärung | Sehr gute Lösung | Schwache Lösung |
|---|---|---|---|
| Fachliche Stabilität | Fähigkeiten sind unabhängig von Systemen, Projekten und Organisationseinheiten formuliert. | „Nachweise verwalten“ | „DMS nutzen“ |
| Hierarchiequalität | Drei Ebenen sind logisch, verständlich und nicht überladen. | Domäne → Capability → Sub-Capability | Zufällige Liste ohne Struktur |
| Begriffsqualität | Fähigkeiten sind als Verb-Nomen-Kombination formuliert. | „Identität prüfen“ | „Identitätsprüfung Sachgebiet 2“ |
| Abgrenzung zu Prozessen | Prozesse werden nicht mit Fähigkeiten verwechselt. | Prozessdetails separat notiert | Einzelne Klicks als Capability |
| IT-Verknüpfung | Anwendungen werden Fähigkeiten zugeordnet. | Fachverfahren unterstützt „Vorgang bearbeiten“ | Anwendungsliste ohne fachlichen Bezug |
| Datenverknüpfung | Zentrale Datenobjekte sind sichtbar. | Antrag, Vorgang, Nachweis, Bescheid | Daten fehlen komplett |
| Schnittstellenblick | Datenflüsse und Medienbrüche werden benannt. | Portal → Fachverfahren → DMS | Schnittstellen bleiben unsichtbar |
| Schutzbedarf | Vertraulichkeit, Integrität und Verfügbarkeit werden fachlich begründet. | Bescheid: Integrität hoch | Pauschal „alles hoch“ |
| Verantwortlichkeit | Fachliche und technische Owner sind unterscheidbar. | Capability Owner, Application Owner, Data Owner | „IT ist zuständig“ |
| Roadmap-Fähigkeit | Aus Schwächen werden Maßnahmen abgeleitet. | Nachweisservice einführen | „System verbessern“ |
| Leitungstauglichkeit | Die Map ist auch ohne technische Detailkenntnis erklärbar. | Klare fachliche Sprache | Tool- und Architekturjargon dominiert |
| Entscheidungsnutzen | Die Map zeigt Prioritäten, Risiken und Abhängigkeiten. | Heatmap mit Maßnahmen | Nur Dokumentation ohne Steuerungswirkung |

## Dein konkreter Arbeitsauftrag für die erste eigene Capability Map

Erstelle zuerst eine Tabelle mit vier Spalten: „Domäne“, „Fähigkeit“, „Sub-Fähigkeit“ und „Begründung“. Trage die zehn Fähigkeiten aus deinem Beispiel ein: Antrag entgegennehmen, Identität prüfen, Nachweise verwalten, Vorgang bearbeiten, Fachentscheidung treffen, Bescheid erstellen, Kommunikation führen, Akte führen, Zahlung auslösen und Berichtspflichten erfüllen. Danach gruppierst du sie in fünf bis sechs Domänen. Anschließend ergänzt du für jede Fähigkeit die Anwendungen, Datenobjekte, Risiken und Maßnahmen.

Die erste Version muss nicht perfekt sein. Sie muss nur eines leisten: Sie muss das Gespräch weg von Systemnamen und hin zur fachlichen Leistungsfähigkeit bringen. Genau das ist der Kern guter Enterprise Architecture in einer Bundesbehörde.

<>