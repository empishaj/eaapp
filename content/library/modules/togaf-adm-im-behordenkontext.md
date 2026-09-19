## Checkliste: TOGAF/ADM im Behördenmandat praktisch anwenden

1. Kläre zuerst das *Architekturmandat*, nicht die Methode.  
2. Übersetze TOGAF-Begriffe konsequent in Entscheidungssprache.  
3. Nutze ADM als *Phasenlogik*, nicht als Dokumentenmaschine.  
4. Beginne mit Stakeholdern, Problemen, Risiken und Entscheidungsbedarf.  
5. Trenne Business-, Daten-, Applikations- und Technologiearchitektur sauber.  
6. Verbinde die Domänen anschließend über Fähigkeiten, Datenflüsse, Schnittstellen und Roadmaps.  
7. Baue Security, Datenschutz, Betrieb und Dienstleistersteuerung von Anfang an ein.  
8. Erstelle nur Artefakte, die eine konkrete Entscheidung vorbereiten.  
9. Arbeite iterativ: erst grobes Zielbild, dann vertiefen.  
10. Nutze TOGAF leichtgewichtig: Vision, Ist/Soll, Gaps, Maßnahmen, Governance.  
11. Vermeide Framework-Jargon gegenüber Leitung und Fachseite.  
12. Mache am Ende jeder Phase sichtbar: *Welche Entscheidung ist jetzt möglich?*  

<>

## 1. Grundidee: TOGAF ist kein Zertifikatsstoff, sondern ein Denkgerüst für Entscheidungsfähigkeit

TOGAF ist in der Praxis dann wertvoll, wenn du es nicht als starres Framework verkaufst, sondern als geordneten Weg von Unsicherheit zu belastbaren Entscheidungen. Die Open Group beschreibt TOGAF als Enterprise-Architecture-Methodik und Framework; der Kern ist die Architecture Development Method, also ein iteratives Vorgehensmodell zur Entwicklung und Steuerung von Unternehmensarchitekturen. Die aktuelle TOGAF-10-Struktur ist modularer aufgebaut und enthält unter anderem Dokumente zu ADM, ADM-Techniken, Anwendung der ADM, Architekturinhalt sowie EA Capability & Governance. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com))

Für deinen Behördenkontext heißt das: Du nutzt TOGAF nicht, um zu zeigen, dass du TOGAF kennst. Du nutzt TOGAF, um einen unklaren Auftrag wie „Wir brauchen eine Zielarchitektur für unsere Fachverfahren“ in beherrschbare Arbeitsabschnitte zu zerlegen. Aus einem diffusen Problemraum werden konkrete Fragen: Welche Fachfähigkeiten sind betroffen? Welche Datenobjekte sind kritisch? Welche Systeme sind führend? Welche Schnittstellen sind instabil? Welche Schutzbedarfe gelten? Welche Plattformvorgaben existieren? Welche Entscheidungen muss ein Gremium treffen? Genau dort wird TOGAF praktisch.

Die ADM solltest du dir als Architektur-Wertstrom merken: *Mandat klären → Zielrichtung formulieren → Facharchitektur verstehen → Datenarchitektur klären → Applikationslandschaft ordnen → Technologie- und Plattformfragen bewerten → Optionen entwickeln → Migration planen → Umsetzung begleiten → Änderungen kontrolliert aufnehmen*. Requirements Management läuft dabei nicht als einzelne Phase, sondern quer durch alles. Es sammelt Anforderungen, Randbedingungen, Risiken, offene Fragen und Entscheidungen fortlaufend ein.

## 2. Die wichtigste Übersetzung: Von TOGAF-Sprache zu Behördensprache

Im Bundesministerium oder in einer Bundesbehörde solltest du TOGAF selten namentlich in den Vordergrund stellen. Leitung, Fachreferate, Datenschutz, Informationssicherheit, Betrieb, Vergabe und Projektleitungen interessieren sich nicht für die Schönheit des Frameworks. Sie interessieren sich für bessere Entscheidungsgrundlagen, geringere Risiken, weniger Reibung zwischen Fachverfahren, belastbare Roadmaps und sauber steuerbare Dienstleister.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Preliminary Phase | Nicht: „Wir etablieren eine EA Capability.“ Sondern: „Wir klären Mandat, Rollen, Entscheidungswege und Spielregeln.“ | Wer darf Architekturprinzipien festlegen? Wer entscheidet Ausnahmen? | TOGAF ADM und Governance-Struktur nach Open Group; BSI-Mindeststandards für verbindliches Mindestniveau in Bundesverwaltung. ([opengroup.org](https://www.opengroup.org/public/arch/p2/p2_intro.htm?utm_source=chatgpt.com)) |
| Architecture Vision | Nicht: „Wir erstellen eine Vision.“ Sondern: „Wir formulieren, wofür die Architekturarbeit Nutzen stiftet.“ | „Registeranbindung wird standardisiert, damit Fachverfahren Daten nicht mehrfach pflegen.“ | TOGAF beschreibt die ADM als Methode zur Entwicklung organisationsspezifischer Architektur. ([opengroup.org](https://www.opengroup.org/public/arch/p2/p2_intro.htm?utm_source=chatgpt.com)) |
| Business Architecture | Nicht: „Business Layer.“ Sondern: „Welche Verwaltungsfähigkeiten, Prozesse und Verantwortlichkeiten sind betroffen?“ | Antrag annehmen, Identität prüfen, Nachweise verwalten, Bescheid erstellen. | TOGAF trennt Architekturdomänen; diese Trennung ist für saubere Analyse wesentlich. ([en.wikipedia.org](https://en.wikipedia.org/wiki/TOGAF?utm_source=chatgpt.com)) |
| Data Architecture | Nicht: „Datenmodellierung.“ Sondern: „Welche Daten sind führend, schutzbedürftig, redundant oder widersprüchlich?“ | Personendaten im Fachverfahren vs. Registerdaten vs. Aktenmetadaten. | BSI-Schutzbedarf fragt nach Schäden bei Verlust von Vertraulichkeit, Integrität und Verfügbarkeit. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Application Architecture | Nicht: „Anwendungsarchitektur.“ Sondern: „Welche Fachverfahren, Portale, DMS, Registeradapter und Schnittstellen leisten was?“ | Legacy-Fachverfahren bleibt System of Record, Portal wird System of Engagement. | TOGAF arbeitet typischerweise mit Business-, Daten-, Applikations- und Technologiearchitektur. ([en.wikipedia.org](https://en.wikipedia.org/wiki/TOGAF?utm_source=chatgpt.com)) |
| Technology Architecture | Nicht: „Technikbild.“ Sondern: „Welche Plattform-, Betriebs-, IAM-, Netzwerk-, Monitoring- und Sicherheitsbedingungen tragen die Lösung?“ | Kubernetes-Plattform, API-Gateway, IAM, Logging, SIEM, Backup. | BSI-Mindeststandards definieren ein verbindliches Mindestniveau für Informationssicherheit in der Bundesverwaltung. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Mindeststandards/Mindeststandards_node.html?utm_source=chatgpt.com)) |
| Opportunities & Solutions | Nicht: „Lösungsbausteine.“ Sondern: „Welche realistischen Umsetzungsoptionen haben wir?“ | API-Gateway zuerst, Registeradapter danach, DMS-Integration parallel. | TOGAF ADM ist iterativ und soll organisationsspezifisch angepasst werden. ([opengroup.org](https://www.opengroup.org/public/arch/p2/p2_intro.htm?utm_source=chatgpt.com)) |
| Migration Planning | Nicht: „Migration.“ Sondern: „Welche Reihenfolge reduziert Risiko und schafft früh Nutzen?“ | Erst Schnittstelleninventar, dann Standardvertrag, dann Pilotintegration. | TOGAF umfasst Planung, Implementierung, Steuerung und Pflege von Architektur. ([palladio-consulting.de](https://www.palladio-consulting.de/togaf/?utm_source=chatgpt.com)) |
| Implementation Governance | Nicht: „Architekturkontrolle.“ Sondern: „Wir sichern, dass Umsetzung und Zielbild nicht auseinanderlaufen.“ | Architektur-Reviews, ADRs, Ausnahmeentscheidungen, Lieferantennachweise. | TOGAF enthält Governance-Aspekte; BSI-Vorgaben ergänzen Sicherheitssteuerung. ([opengroup.org](https://www.opengroup.org/togaf/fundamental-content?utm_source=chatgpt.com)) |
| Architecture Change Management | Nicht: „Änderungsmanagement.“ Sondern: „Neue Anforderungen werden bewertet, ohne die Zielarchitektur zu zerstören.“ | Neue Registerschnittstelle, neue Plattformvorgabe, geänderte Schutzbedarfseinstufung. | ADM ist ein Lebenszyklusansatz für Architekturentwicklung. ([opengroup.org](https://www.opengroup.org/public/arch/p2/p2_intro.htm?utm_source=chatgpt.com)) |

Die harte Korrektur lautet: TOGAF wird in Behörden oft falsch angewendet, wenn Architekten mit Framework-Begriffen beginnen. Das erzeugt Distanz. Beginne stattdessen mit Entlastung: „Wir schaffen ein klares Entscheidungsbild über Fachverfahren, Daten, Schnittstellen, Sicherheit, Betrieb und Migration.“ Erst intern benutzt du die ADM-Struktur, um nichts zu vergessen.

## 3. Die ADM-Phasen als leichtgewichtige Mandatslogik

### 3.1 Requirements Management: Der rote Faden in der Mitte

Requirements Management ist kein Backlog wie in Scrum, sondern die laufende Architektur-Registratur. Dort sammelst du fachliche Anforderungen, nicht-funktionale Anforderungen, rechtliche Randbedingungen, Schutzbedarfe, Betriebsanforderungen, Schnittstellenanforderungen, Vergabevorgaben, Architekturprinzipien, Risiken, Annahmen und offene Entscheidungen.

Im Behördenmandat führst du daraus ein *Architecture Requirements & Decisions Log*. Dieses Dokument ist klein, aber zentral. Es enthält pro Eintrag: ID, Quelle, Beschreibung, Domäne, Priorität, Risiko, betroffene Stakeholder, Status, Entscheidung oder nächster Klärungsschritt. Damit verhinderst du, dass Anforderungen in Protokollen, E-Mails oder Dienstleisterfolien verschwinden.

### 3.2 Preliminary Phase: Mandat, Spielregeln und Architekturfähigkeit klären

Die Preliminary Phase beantwortet nicht die Frage „Wie sieht die Zielarchitektur aus?“, sondern „Wie dürfen wir überhaupt Architekturarbeit leisten?“ Im Behördenkontext ist das entscheidend, weil Zuständigkeiten verteilt sind: Fachreferat, IT-Referat, Informationssicherheit, Datenschutz, Betrieb, zentrale IT-Dienstleister, Vergabe, Projektleitung und externe Lieferanten haben jeweils eigene Perspektiven.

Deine Kernfragen lauten: Wer ist Auftraggeber? Welche Entscheidungen sollen vorbereitet werden? Welche Architekturdomänen sind im Scope? Gibt es verbindliche Standards? Welche Gremien entscheiden? Welche Rolle hat der externe Dienstleister? Welche Artefakte gelten als verbindlich? Wie werden Ausnahmen entschieden? Welche Sicherheits- und Datenschutzinstanzen müssen beteiligt werden? Welche vorhandenen Dokumente sind maßgeblich?

Das Ergebnis ist kein 80-seitiges Papier, sondern ein *Architecture Working Agreement*. Darin stehen Scope, Rollen, Entscheidungswege, Review-Takt, Artefaktliste, Qualitätskriterien und Eskalationsweg. Genau dieses Dokument schützt dich später vor der typischen Falle: Alle wollen Architektur, aber niemand will entscheiden.

### 3.3 Phase A – Architecture Vision: Zielrichtung und Nutzenversprechen formulieren

Die Architecture Vision ist der erste sichtbare Führungsartefakt. Sie muss so kurz sein, dass eine Abteilungsleitung sie versteht, und so präzise, dass Projektleitungen daraus Handlungsrichtung ableiten können.

Für unser Beispiel einer Bundesbehörde könnte die Vision lauten: „Die Fachverfahrenslandschaft wird so weiterentwickelt, dass zentrale Verwaltungsfähigkeiten über stabile, dokumentierte und sicher betriebene Schnittstellen unterstützt werden. Registerdaten werden nachvollziehbar angebunden, Datenverantwortung wird geklärt, IAM wird vereinheitlicht, Integrationen werden über standardisierte Schnittstellenverträge gesteuert, und Modernisierung erfolgt schrittweise entlang fachlicher Prioritäten und betrieblicher Risiken.“

Diese Vision leistet drei Dinge. Sie benennt den Nutzen: weniger Wildwuchs, klarere Datenverantwortung, frühere Risikosichtbarkeit. Sie begrenzt den Scope: Fachverfahren, Register, Schnittstellen, IAM, Plattform, Betrieb. Und sie bereitet Entscheidungen vor: Welche Zielprinzipien gelten? Welche Vorhaben werden priorisiert? Welche Altlasten werden akzeptiert, welche nicht?

### 3.4 Phase B – Business Architecture: Fachfähigkeiten, Prozesse und Verantwortlichkeiten verstehen

In der Business Architecture schaust du nicht zuerst auf Systeme, sondern auf Verwaltungsfähigkeiten. Das ist wichtig, weil Systemnamen historisch gewachsen sind und oft den falschen Fokus setzen. Eine Behörde braucht nicht „System X modernisieren“, sondern Fähigkeiten wie Antrag entgegennehmen, Identität prüfen, Nachweise verwalten, Vorgang bearbeiten, Fachentscheidung treffen, Bescheid erstellen, Kommunikation führen, Akte führen, Zahlung auslösen und Berichtspflichten erfüllen.

Der praktische Output ist eine Capability Map mit Verantwortlichkeiten und Pain Points. Dazu kommen Prozesslandkarten oder ausgewählte BPMN-Sichten für kritische Abläufe. Du musst nicht jeden Prozess modellieren. Du modellierst dort, wo Medienbrüche, Wartezeiten, unklare Zuständigkeiten, manuelle Übergaben oder Sicherheitsrisiken sichtbar werden müssen.

Typische Interviewfrage: „Welche fachliche Fähigkeit wäre morgen nicht mehr arbeitsfähig, wenn dieses Fachverfahren ausfällt?“ Diese Frage zwingt Fachseite und IT weg vom Systemnamen hin zur Wirkung.

### 3.5 Phase C1 – Data Architecture: Datenobjekte, Verantwortung und führende Systeme klären

Data Architecture ist im Behördenkontext oft der unterschätzte Hebel. Viele Modernisierungsvorhaben scheitern nicht an Technik, sondern an ungeklärter Datenverantwortung. Personendaten, Vorgangsdaten, Nachweisdaten, Bescheiddaten, Zahlungsdaten, Aktenmetadaten und Kommunikationsdaten liegen häufig in mehreren Systemen. Wenn nicht klar ist, welches System führend ist, entstehen Doppelpflege, widersprüchliche Auskünfte, Schnittstellenkonflikte und riskante manuelle Korrekturen.

Dein Artefakt ist eine Datenlandkarte. Sie zeigt je Datenobjekt: fachliche Definition, Datenowner, führendes System, lesende Systeme, schreibende Systeme, Schnittstellen, Schutzbedarf, Aufbewahrung, Löschung, Datenqualität und offene Entscheidungen. Die BSI-Schutzbedarfslogik ist dabei anschlussfähig, weil sie Vertraulichkeit, Integrität und Verfügbarkeit als Grundwerte betrachtet und nach möglichen Schäden fragt, wenn diese verletzt werden. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com))

Leitfrage: „Wer darf dieses Datum fachlich verbindlich ändern?“ Wenn darauf keine klare Antwort kommt, hast du keinen technischen Fehler gefunden, sondern einen Architekturentscheidungsbedarf.

### 3.6 Phase C2 – Application Architecture: Applikationslandschaft und Integrationen ordnen

Application Architecture beantwortet: Welche Anwendungen unterstützen welche Fähigkeiten? Welche Anwendung ist System of Record? Welche Anwendung ist nur Oberfläche? Welche Schnittstellen sind kritisch? Welche Fachverfahren sind strategisch, welche nur Übergangslösungen? Welche Anwendungen haben hohe fachliche Kritikalität, aber schlechten technischen Zustand?

Das zentrale Artefakt ist eine Applikationslandkarte mit Capability-Zuordnung. Ergänzend nutzt du Schnittstelleninventar, Systemsteckbriefe, Abhängigkeitsdiagramme und ADRs. Für das Beispiel würdest du Portal, Fachverfahren, Registeradapter, DMS/eAkte, IAM, API-Gateway, Reporting, Monitoring und Betriebsplattform sichtbar verbinden.

Praktischer Satz für ein Gremium: „Wir bewerten Anwendungen nicht nach Alter, sondern nach fachlichem Wert, Risiko, Anschlussfähigkeit und strategischer Passung.“

### 3.7 Phase D – Technology Architecture: Plattform, Betrieb, Security und Betriebsfähigkeit konkretisieren

Technology Architecture ist nicht nur Infrastruktur. Im Behördenkontext gehören dazu Plattformstrategie, Netzwerkzonen, IAM, Verschlüsselung, Protokollierung, Monitoring, Backup, Wiederanlauf, Mandantentrennung, Betriebsmodell, Patchprozesse, technische Konten, Secret Management, Deployment-Prozesse und Lieferkettenkontrolle.

Hier musst du besonders eng mit Informationssicherheit und Betrieb arbeiten. Die BSI-Mindeststandards definieren nach § 44 BSIG ein verbindliches Mindestniveau für Informationssicherheit in Einrichtungen der Bundesverwaltung; daher darf Security in der Zielarchitektur nicht als nachträglicher Prüfpunkt erscheinen, sondern muss als Architekturbedingung formuliert werden. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Mindeststandards/Mindeststandards_node.html?utm_source=chatgpt.com))

Der Fehler vieler Architekturteams besteht darin, Plattformen als Zielbild zu zeichnen, ohne Betriebsverantwortung, Schutzbedarf, Logging, Backup, Notfallfähigkeit und Dienstleisterzugriffe zu klären. Das ist keine Zielarchitektur, sondern eine technische Wunschgrafik.

### 3.8 Phase E – Opportunities & Solutions: Optionen statt Wunschlösung

In dieser Phase entwickelst du umsetzbare Optionen. Nicht: „Wir machen Microservices.“ Sondern: „Welche Lösungspfade haben wir, mit welchen Kosten, Risiken, Abhängigkeiten und Entscheidungspunkten?“

Für das Beispiel könnten drei Optionen entstehen. Option 1: Minimalmodernisierung mit Schnittstellenstandardisierung und stabilisierendem API-Gateway. Option 2: Schrittweise Entkopplung über Registeradapter, DMS-Integration und IAM-Zentralisierung. Option 3: strategischer Plattformumbau mit stärkerer Modularisierung, Event-Flüssen und langfristiger Legacy-Ablösung. Jede Option bekommt Nutzen, Risiken, Voraussetzungen, Zeithorizont, betroffene Stakeholder und No-Regret-Maßnahmen.

Der wichtigste Satz lautet: „Eine Architekturentscheidung ist erst dann reif, wenn mindestens zwei realistische Alternativen sichtbar sind.“

### 3.9 Phase F – Migration Planning: Roadmap, Übergangsarchitektur und Priorisierung

Migration Planning übersetzt das Zielbild in Reihenfolge. In Behörden ist das selten ein Big Bang. Realistisch ist eine Abfolge aus Stabilisierung, Transparenz, Standardisierung, Pilotierung und schrittweiser Ablösung.

Eine gute Roadmap enthält Arbeitspakete, Abhängigkeiten, Nutzenbeitrag, Risiken, Entscheidungsbedarf, grobe Kostenklasse, Verantwortlichkeit und Zielquartal. Noch wichtiger: Sie zeigt Übergangsarchitekturen. Eine Übergangsarchitektur ist kein Scheitern, sondern professionelle Realität. Sie sagt: „Für 12 bis 18 Monate leben wir mit diesem Legacy-System weiter, aber nur unter diesen Bedingungen: dokumentierte Schnittstellen, Monitoring, Betriebsverantwortung, Datenowner, Ablösepfad.“

### 3.10 Phase G – Implementation Governance: Umsetzung an Zielbild koppeln

Implementation Governance ist in Behörden besonders wichtig, weil viel Umsetzung über Projekte, Programme und Dienstleister läuft. Deine Aufgabe ist nicht, jedes Ticket zu kontrollieren. Deine Aufgabe ist, Architekturentscheidungen prüfbar zu machen.

Dazu gehören Architektur-Reviews, ADRs, Schnittstellenverträge, Security-by-Architecture-Reviews, Definition-of-Ready für Architekturentscheidungen, Definition-of-Done für Architekturartefakte und ein Ausnahmeprozess. Ein Dienstleister darf nicht nur „technisch liefern“, sondern muss gegen Zielbild, Standards, Schutzbedarf, Betriebsmodell und Schnittstellenvertrag liefern.

Gute Governance klingt nicht wie Kontrolle. Sie klingt so: „Wir reduzieren spätere Nacharbeit, weil zentrale Architekturfragen vor Umsetzung geklärt werden.“

### 3.11 Phase H – Architecture Change Management: Zielbild lernfähig halten

Architecture Change Management verhindert, dass die Zielarchitektur nach drei Monaten veraltet. Neue gesetzliche Anforderungen, neue Registervorgaben, Plattformentscheidungen, Sicherheitsbefunde, Haushaltsentscheidungen oder Dienstleisterwechsel können die Architektur verändern. Das Ziel ist nicht Starrheit, sondern kontrollierte Anpassung.

Dein leichtgewichtiges Change-Verfahren enthält: Änderungsauslöser, betroffene Architekturdomäne, Risiko, Dringlichkeit, Architekturprinzipien, Entscheidungsoptionen, Auswirkung auf Roadmap und betroffene Stakeholder. Damit vermeidest du, dass jede Änderung als Einzelfall behandelt wird und die Landschaft wieder auseinanderläuft.

## 4. TOGAF im Behördenkontext: das praktische Zielbild

Ein Behördenauftrag beginnt oft ungefähr so: „Wir haben mehrere Fachverfahren, Legacy-Systeme, unterschiedliche Dienstleister, uneinheitliche Schnittstellen, unklare Datenverantwortung und möchten perspektivisch eine Plattformstrategie aufbauen.“ Das ist noch kein Architekturauftrag. Das ist eine Problemlage.

Du machst daraus folgende Architekturfrage: „Wie müssen Fachfähigkeiten, Daten, Anwendungen, Schnittstellen, IAM, Plattform, Betrieb und Governance geordnet werden, damit die Behörde ihre Fachverfahren schrittweise modernisieren, Risiken reduzieren und Dienstleister besser steuern kann?“

Diese Umformulierung ist wesentlich. Sie verhindert, dass du zu früh in eine Lösung springst. Du bist nicht derjenige, der sofort „Kubernetes“, „Microservices“, „API Gateway“ oder „Event-Driven Architecture“ ruft. Du bist derjenige, der Entscheidungsfähigkeit herstellt.

## 5. Das 30/60/90-Tage-Vorgehensmodell auf TOGAF-Basis

### Tage 1–30: Mandat, Lagebild und Architecture Vision

In den ersten 30 Tagen musst du Vertrauen, Übersicht und Entscheidungsstruktur herstellen. Du führst Interviews, sichtest Dokumente, identifizierst Stakeholder, klärst Gremienwege und formulierst ein erstes Architekturmandat. Ziel ist nicht Vollständigkeit. Ziel ist ein belastbares Anfangsbild.

| Aspekt | Details/Erklärung | Beispiel | Artefakt | Entscheidung |
|---|---|---|---|---|
| Auftrag klären | Was soll Architekturarbeit konkret leisten? | Zielarchitektur für Fachverfahrensmodernisierung | Architecture Working Agreement | Mandat bestätigt oder geschärft |
| Stakeholder erfassen | Wer ist betroffen, wer entscheidet, wer blockiert unbeabsichtigt? | Fachreferat, IT, ISB, DSB, Betrieb, Vergabe, Dienstleister | Stakeholder Map | Beteiligungsmodell |
| Dokumente sichten | Vorhandene Konzepte, Verträge, Sicherheitskonzepte, Betriebsdokumente prüfen | Fachkonzepte, Schnittstellenlisten, AVV, Betriebshandbuch | Dokumentenradar | Lücken sichtbar |
| Problemraum strukturieren | Pain Points clustern | Schnittstellen, Datenqualität, IAM, Betrieb, Legacy | Problem- und Risikolandkarte | Prioritäten für Vertiefung |
| Vision formulieren | Nutzenversprechen und Zielrichtung | „Weniger Wildwuchs, bessere Anschlussfähigkeit“ | Architecture Vision 1.0 | Freigabe zur Vertiefung |
| Arbeitsmodus etablieren | Review-Takt, Entscheidungslog, Artefaktformat | 14-tägiger Architektur-Jour-fixe | Governance Light | Arbeitsfähigkeit |

Die wichtigsten Fragen in den ersten 30 Tagen lauten: „Welche Entscheidung soll in drei Monaten besser möglich sein als heute?“, „Welche Systeme sind fachlich kritisch?“, „Welche Schnittstellen verursachen den größten Schmerz?“, „Welche Datenobjekte sind unklar verantwortet?“, „Welche Sicherheits- oder Betriebsrisiken sind bereits bekannt?“, „Welche Dienstleister liefern welche Teile?“ und „Welche Architekturentscheidungen wurden bereits faktisch getroffen, aber nie dokumentiert?“

### Tage 31–60: Domänenarchitekturen trennen und verbinden

In den Tagen 31 bis 60 gehst du in die Domänen. Jetzt entstehen Capability Map, Datenlandkarte, Applikationslandkarte, Schnittstelleninventar, Technologie-/Plattformbild und erste Gap-Analyse. Wichtig ist: Du trennst die Sichten analytisch, aber verbindest sie über konkrete Abhängigkeiten.

| Aspekt | Details/Erklärung | Beispiel | Artefakt | Entscheidung |
|---|---|---|---|---|
| Business Architecture | Fähigkeiten und kritische Prozesse erfassen | Antrag, Prüfung, Bescheid, Akte, Zahlung | Capability Map | Welche Fähigkeiten priorisiert werden |
| Data Architecture | Datenobjekte, führende Systeme, Schutzbedarf klären | Person, Vorgang, Nachweis, Bescheid | Datenlandkarte | Data-Owner- und SoT-Entscheidungen |
| Application Architecture | Systeme, Verantwortlichkeiten, Abhängigkeiten ordnen | Portal, Fachverfahren, DMS, Registeradapter | Applikationslandkarte | Modernisierungscluster |
| Technology Architecture | Plattform, IAM, Logging, Betrieb, Backup bewerten | API-Gateway, IAM, Kubernetes, SIEM | Technologiezielbild grob | Plattform- und Betriebsleitplanken |
| Integration | Schnittstellen fachlich und technisch beschreiben | Registerabfrage, DMS-Übergabe | Schnittstelleninventar | Schnittstellenstandard |
| Gaps | Ist/Soll-Abweichungen erfassen | Keine zentrale Authentifizierung, unklare Datenowner | Gap-Liste | Maßnahmenbedarf |

Die wichtigste Denkleistung in dieser Phase ist das Verbinden: Eine Fähigkeit braucht Daten. Daten liegen in Systemen. Systeme kommunizieren über Schnittstellen. Schnittstellen laufen auf Technologie. Technologie unterliegt Security, Betrieb und Vergabe. Genau diese Kette macht dich als Enterprise Architekt wirksam.

### Tage 61–90: Optionen, Roadmap, Governance und Entscheidungsvorlage

In den Tagen 61 bis 90 erzeugst du aus Analyse Entscheidungsfähigkeit. Du formulierst Zielprinzipien, Lösungsoptionen, Übergangsarchitekturen, Roadmap und Governance-Modell. Am Ende sollte ein Gremium nicht nur informiert sein, sondern entscheiden können.

| Aspekt | Details/Erklärung | Beispiel | Artefakt | Entscheidung |
|---|---|---|---|---|
| Zielprinzipien | Leitplanken für weitere Vorhaben | API-first dort, wo fachlich sinnvoll; IAM zentral; Datenowner benennen | Architekturprinzipien | Prinzipien freigegeben |
| Optionen | Realistische Lösungspfade vergleichen | Stabilisieren, schrittweise entkoppeln, strategisch ablösen | Optionsvergleich | Zielpfad auswählen |
| Roadmap | Maßnahmen in Reihenfolge bringen | Q1 Schnittstelleninventar, Q2 Registerpilot, Q3 IAM-Integration | Transformationsroadmap | Priorisierung |
| Übergangsarchitektur | Zwischenzustände explizit machen | Legacy bleibt, aber mit API-Fassade und Monitoring | Plateau-/Transition View | Akzeptierte Übergangslösung |
| Governance | Umsetzung an Zielbild koppeln | ADRs, Reviews, Ausnahmeprozess | Architecture Governance Light | Verbindlicher Steuerungsmodus |
| Entscheidungsvorlage | Leitungstaugliche Zusammenfassung | Nutzen, Risiken, Kostenklasse, Abhängigkeiten | Executive Decision Paper | Beschlussfähigkeit |

Der Schlüsselsatz für Tag 90 lautet: „Wir haben nicht alle Details endgültig gelöst, aber wir wissen jetzt, welche Entscheidungen in welcher Reihenfolge nötig sind, welche Risiken wir tragen, welche Maßnahmen zuerst Nutzen bringen und wie Umsetzung gesteuert wird.“

## 6. Musterartefakte für dein Behördenmandat

### 6.1 Architecture Vision – Einseiter

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Ausgangslage | Kurz beschreiben, warum Architekturarbeit nötig ist | Mehrere Fachverfahren, uneinheitliche Schnittstellen, unklare Datenverantwortung | TOGAF nutzt ADM zur Entwicklung organisationsspezifischer Architektur. ([opengroup.org](https://www.opengroup.org/public/arch/p2/p2_intro.htm?utm_source=chatgpt.com)) |
| Zielbild | Zielzustand in Behördensprache | Standardisierte Registeranbindung, klare Datenowner, nachvollziehbare Roadmap | TOGAF Standard als EA-Methodik. ([opengroup.org](https://www.opengroup.org/togaf?utm_source=chatgpt.com)) |
| Nutzen | Entlastung formulieren | Weniger Wildwuchs, bessere Dienstleistersteuerung, frühere Risikosichtbarkeit | Fachliche Ableitung aus EA-Praxis |
| Scope | Was ist enthalten, was nicht? | Fachverfahren A/B/C, Register, DMS, IAM, API-Gateway; keine Detailimplementierung | ADM-Anpassung an praktischen Kontext. ([opengroup.org](https://www.opengroup.org/togaf/fundamental-content?utm_source=chatgpt.com)) |
| Prinzipien | 5 bis 7 Leitplanken | Führende Systeme klären, Schnittstellen vertraglich beschreiben, Security by Architecture | BSI-Mindestniveau Informationssicherheit. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Oeffentliche-Verwaltung/Mindeststandards/Mindeststandards_node.html?utm_source=chatgpt.com)) |
| Entscheidungen | Was soll entschieden werden? | Zielpfad, Pilot, Governance, Roadmap | TOGAF Governance- und ADM-Logik |

### 6.2 Architecture Working Agreement – Minimalstruktur

Das Architecture Working Agreement enthält erstens Mandat und Auftraggeber, zweitens Scope und Nicht-Scope, drittens Stakeholder und Rollen, viertens Entscheidungswege, fünftens Artefakte, sechstens Review-Takt, siebtens Qualitätskriterien, achtens Sicherheits- und Datenschutzbeteiligung, neuntens Dienstleistereinbindung und zehntens Ausnahmeprozess. Dieses Dokument sollte auf drei bis fünf Seiten passen. Alles darüber wird am Anfang meist zu schwer.

### 6.3 Architecture Requirements & Decisions Log

| Aspekt | Details/Erklärung | Beispiel | Entscheidung/Risiko |
|---|---|---|---|
| ID | Eindeutige Nummer | AR-017 | Nachverfolgung |
| Quelle | Wer hat es eingebracht? | ISB, Fachreferat, Betrieb | Relevanz klären |
| Beschreibung | Was wird gefordert oder beobachtet? | Registerabfragen müssen protokolliert werden | Security-/Betriebsanforderung |
| Domäne | Business, Data, Application, Technology, Security, Betrieb | Technology/Security | Zuständigkeit |
| Priorität | Muss, Soll, Kann | Muss | Architekturleitplanke |
| Status | Offen, in Prüfung, entschieden, verworfen | Offen | Nächster Schritt |
| Entscheidung | Beschluss oder ADR-Link | ADR-004 Logging-Standard | Nachvollziehbarkeit |

### 6.4 Gap-Analyse

Die Gap-Analyse beantwortet drei Fragen: Was ist heute? Was soll künftig gelten? Was fehlt dazwischen? Für eine Behörde ist das besonders wirksam, weil es Streit entpersonalisiert. Nicht „System X ist schlecht“, sondern „Für die Fähigkeit Nachweisverwaltung fehlt ein führendes System, ein Datenowner, eine dokumentierte Schnittstelle und ein abgestimmtes Löschkonzept.“

### 6.5 Roadmap-Artefakt

Eine gute Roadmap besteht nicht nur aus Balken. Sie enthält Maßnahmencluster: Transparenz schaffen, Risiken reduzieren, Standards festlegen, Pilot umsetzen, Skalierung vorbereiten, Legacy ablösen. Für jedes Cluster benennst du Nutzen, Abhängigkeiten, Risiken, Entscheidungspunkte und verantwortliche Rollen.

## 7. Typische Fehler – und die fachliche Korrektur

| Aspekt | Details/Erklärung | Beispiel | Korrektur |
|---|---|---|---|
| Framework vor Problem | TOGAF wird erklärt, bevor der Nutzen klar ist | „Wir machen Phase B/C/D“ | „Wir klären Fachfähigkeiten, Daten, Systeme und Plattformrisiken.“ |
| Zu viele Artefakte | Dokumente entstehen ohne Entscheidung | 120-seitiges Zielbild ohne Beschluss | Pro Artefakt eine Entscheidungsfrage definieren |
| System statt Fähigkeit | Architektur beginnt bei Anwendungen | „Fachverfahren X modernisieren“ | Erst Fähigkeit, dann Daten, dann Anwendung |
| Daten zu spät betrachtet | Datenowner und führende Systeme bleiben offen | Widersprüchliche Personendaten | Datenlandkarte früh erstellen |
| Security als Prüfung am Ende | ISB wird erst vor Go-live eingebunden | Nachträgliche Nacharbeit | Security in Vision, Prinzipien und Reviews einbauen |
| Betrieb vergessen | Zielbild ignoriert Monitoring, Backup, Support | Plattform nicht abnahmefähig | Betriebsmodell als Architekturdomäne behandeln |
| Dienstleister nicht steuerbar | Lieferanten liefern Folien, aber keine prüfbaren Artefakte | Schnittstelle ohne Vertrag | Artefakte und Akzeptanzkriterien vertraglich verankern |
| Big-Bang-Roadmap | Zielarchitektur wirkt unrealistisch | Komplettablösung in einem Schritt | Übergangsarchitekturen definieren |
| Keine Entscheidungen | Alles bleibt „in Abstimmung“ | Offene SoT-Frage über Monate | Decision Log und ADRs einführen |
| Keine Change-Logik | Zielbild veraltet sofort | Neue Vorgabe sprengt Roadmap | Architecture Change Board light etablieren |

## 8. Wann TOGAF zu schwergewichtig wird – und wie du es reduzierst

TOGAF wird zu schwergewichtig, wenn du jede Phase vollständig dokumentieren willst, obwohl das Mandat nur eine begrenzte Entscheidung braucht. Es wird ebenfalls schwergewichtig, wenn du alle Stakeholder in alle Details zwingst, wenn du Modellierung wichtiger nimmst als Klärung, oder wenn du Architektur als Parallelbürokratie neben Projektmanagement, Informationssicherheit und Betrieb aufbaust.

Die pragmatische Reduktion lautet: Nutze nur fünf Kernartefakte. Erstens Architecture Vision. Zweitens Capability-/Prozesssicht. Drittens Daten- und Applikationslandkarte. Viertens Gap-/Risikoliste. Fünftens Roadmap mit Governance. Alles Weitere entsteht nur bei konkretem Bedarf: ADRs für Entscheidungen, Schnittstellenverträge für Integrationen, Security Reviews für kritische Systeme, Plattformzielbild für Infrastrukturentscheidungen.

Eine gute Faustregel: Wenn ein Artefakt keine Entscheidung vorbereitet, kein Risiko sichtbar macht, keine Verantwortlichkeit klärt und keine Umsetzung steuert, ist es aktuell überflüssig.

## 9. Executive-Formulierungen für Gremien und Leitung

„Wir nutzen Architekturarbeit, um aus vielen Einzelvorhaben ein steuerbares Gesamtbild zu machen.“

„Das Ziel ist nicht mehr Dokumentation, sondern bessere Entscheidungen: Welche Systeme bleiben, welche werden entkoppelt, welche Schnittstellen werden standardisiert, welche Risiken müssen vor Umsetzung geklärt werden?“

„Die vorgeschlagene Vorgehensweise reduziert Wildwuchs, weil Fachfähigkeiten, Datenverantwortung, Anwendungen, Schnittstellen und Plattformentscheidungen gemeinsam betrachtet werden.“

„Wir schaffen keine zusätzliche Bürokratie, sondern einen verbindlichen Klärungsweg für Fragen, die sonst spät, teuer und konfliktträchtig in Projekten auftauchen.“

„Die Roadmap trennt Sofortmaßnahmen, Übergangslösungen und strategische Zielarchitektur. Dadurch müssen wir nicht alles gleichzeitig entscheiden.“

„Security, Datenschutz und Betrieb werden nicht nachgelagert geprüft, sondern als Architekturbedingungen von Beginn an eingebaut.“

„Dienstleistersteuerung wird verbessert, weil Liefergegenstände nicht nur funktional, sondern auch architektonisch, betrieblich und sicherheitsbezogen prüfbar werden.“

## 10. Konkrete Übungen

### Übung 1: Architecture Vision formulieren

Nimm folgende Ausgangslage: Eine Behörde betreibt drei Fachverfahren, zwei davon Legacy. Registerdaten werden manuell abgeglichen. DMS-Anbindung ist uneinheitlich. IAM erfolgt pro Fachverfahren separat. Betrieb und Monitoring sind je Dienstleister unterschiedlich geregelt.

Deine Aufgabe: Formuliere eine Architecture Vision mit maximal 180 Wörtern. Sie muss Ausgangslage, Zielbild, Nutzen, Scope und erste Architekturprinzipien enthalten.

Bewertungskriterien: Ist der Nutzen klar? Sind Fachfähigkeit, Daten, Anwendungen, Technologie und Governance erkennbar? Ist die Sprache leitungstauglich? Wird keine Lösung vorschnell gesetzt?

### Übung 2: ADM-Phasen zuordnen

Ordne die folgenden Aktivitäten ADM-Phasen zu: Stakeholder Map erstellen, führende Systeme klären, API-Gateway-Optionen vergleichen, Roadmap priorisieren, Architekturprinzipien festlegen, Betriebsmonitoring prüfen, Schnittstellenvertrag erstellen, Ausnahmeentscheidung dokumentieren, Schutzbedarf für Datenobjekte erfassen, Zielbildänderung wegen neuer Registervorgabe bewerten.

Ziel: Du sollst erkennen, dass ADM keine lineare Schablone ist. Manche Aktivitäten gehören primär in eine Phase, wirken aber in andere Phasen hinein.

### Übung 3: Gap-Analyse bauen

Erstelle für die Fähigkeit „Nachweise verwalten“ eine Gap-Analyse. Betrachte Ist-Zustand, Soll-Zustand, Lücke, Risiko, Maßnahme, Owner und Entscheidung. Typische Gaps könnten sein: kein führendes System, unklare Aufbewahrung, manuelle Übergabe an DMS, fehlende Protokollierung, keine einheitliche Schnittstelle.

### Übung 4: Roadmap ableiten

Leite aus drei Gaps eine 6-Monats-Roadmap ab. Die Roadmap muss mindestens ein Transparenz-Arbeitspaket, ein Standardisierungs-Arbeitspaket, einen Pilot und eine Governance-Maßnahme enthalten.

## 11. Kleine Prüfung zur Selbstbewertung

| Aspekt | Prüfungsfrage | Erwartung an eine starke Antwort | Punkte |
|---|---|---|---|
| ADM-Verständnis | Warum beginnt gute Architekturarbeit nicht mit Technology Architecture? | Weil zuerst Mandat, Nutzen, Fähigkeiten, Daten und Anwendungszusammenhänge geklärt werden müssen; Technologie trägt diese Ziele. | 0–5 |
| Behördenübersetzung | Wie erklärst du Architecture Vision ohne TOGAF-Jargon? | Als kurzes Ziel- und Nutzenbild, das Entscheidungsrichtung, Scope und Leitplanken festlegt. | 0–5 |
| Domänentrennung | Unterschied zwischen Business, Data, Application und Technology Architecture? | Fähigkeit/Prozess; Datenobjekte/Verantwortung; Systeme/Schnittstellen; Plattform/Betrieb/Security. | 0–5 |
| Datenarchitektur | Warum sind führende Systeme architekturrelevant? | Sie verhindern widersprüchliche Daten, Doppelpflege, Schnittstellenkonflikte und unklare Verantwortung. | 0–5 |
| Governance | Was leistet Implementation Governance praktisch? | Sie koppelt Umsetzung, Dienstleisterlieferung und Projektentscheidungen an Zielbild, Standards und Reviews. | 0–5 |
| Pragmatik | Wann reduzierst du TOGAF? | Wenn vollständige Framework-Artefakte keinen zusätzlichen Entscheidungsnutzen liefern. | 0–5 |
| Roadmap | Was ist eine Übergangsarchitektur? | Ein bewusst gestalteter Zwischenzustand mit klaren Bedingungen, Risiken und Ablösepfad. | 0–5 |
| Security | Warum gehört BSI-/Security-Sicht früh in die ADM? | Schutzbedarf, Logging, IAM, Betrieb und Notfallfähigkeit beeinflussen Architekturentscheidungen grundlegend. | 0–5 |

Ab 32 Punkten sitzt das Grundverständnis. Ab 36 Punkten argumentierst du bereits mandatsfähig. Unter 28 Punkten solltest du vor allem an Domänentrennung, Datenarchitektur und Governance arbeiten.

## 12. Dein mentales Modell für reale Mandate

Merke dir diesen Satz als Arbeitskompass: *TOGAF liefert die Reihenfolge der Klärung, nicht die Sprache des Mandats.*

In einem deutschen Behördenkontext wirkst du stark, wenn du nicht „ADM Phase B/C/D“ sagst, sondern: „Wir klären zuerst, welche fachlichen Fähigkeiten betroffen sind. Dann bestimmen wir die kritischen Daten und Verantwortlichkeiten. Danach ordnen wir Anwendungen und Schnittstellen. Anschließend bewerten wir Plattform, Security und Betrieb. Daraus leiten wir Optionen, Roadmap und Governance ab.“

Genau so wird aus TOGAF ein praktisches Arbeitsmodell. Nicht schwer, nicht akademisch, nicht folienverliebt. Sondern ein strukturierter Weg, um Behörden aus gewachsener Komplexität in entscheidbare Architekturarbeit zu führen. <>