## Checkliste: Woran du eine professionelle Transformationsroadmap erkennst

Eine belastbare Roadmap beantwortet mindestens diese Punkte: 1. Ist die Ist-Architektur als überprüfbarer Ausgangszustand beschrieben? 2. Ist die Zielarchitektur konkret genug, um daraus Arbeit abzuleiten? 3. Sind die Gaps nach Business, Anwendungen, Daten, Integration, Security, Betrieb und Plattform getrennt sichtbar? 4. Gibt es echte Übergangsarchitekturen statt nur Projektphasen? 5. Ist für jede Übergangsarchitektur klar, welcher stabile Zwischenzustand erreicht wird? 6. Sind Work Packages so geschnitten, dass sie Architekturwirkung erzeugen und nicht nur Tätigkeiten sammeln? 7. Sind Abhängigkeiten vor der Terminplanung modelliert? 8. Sind Risiken und technische Schulden ausdrücklich in der Roadmap enthalten? 9. Gibt es Migrationswellen mit klaren Eintritts- und Austrittskriterien? 10. Sind Quick Wins von Fundamentarbeiten unterschieden? 11. Sind Entscheidungsfenster sichtbar, also Zeitpunkte, an denen Architekturentscheidungen verbindlich getroffen werden müssen? 12. Hat die Roadmap Abnahmekriterien je Plateau, nicht nur Meilensteine? 13. Ist erkennbar, welche Altlasten bewusst temporär toleriert werden? 14. Gibt es Governance-Punkte, an denen Architekturkonformität geprüft wird? 15. Kann ein Dienstleister, Projektleiter oder Behördenreferat daraus erkennen, was wann, warum und mit welchem Risiko zu liefern ist?

## 1. Der Kern: Eine Transformationsroadmap ist kein Terminplan, sondern ein Architektursteuerungsinstrument

Eine normale Projektroadmap sagt: „Im Q1 machen wir IAM, im Q2 APIs, im Q3 Plattform.“ Eine Architekturroadmap sagt zusätzlich: „Ohne IAM-Basisfähigkeit können Fachverfahren nicht einheitlich abgesichert werden; ohne API-Standard entstehen neue Punkt-zu-Punkt-Schnittstellen; ohne Observability kann die Plattformmigration nicht betrieblich abgenommen werden; ohne Daten- und Schnittstellenklassifikation ist keine tragfähige Migrationswelle planbar.“

Das ist der Unterschied zwischen Planung und Architekturführung.

TOGAF beschreibt die Architecture Roadmap als zeitliche Abfolge von Work Packages, die die Zielarchitektur realisieren. Phase E dient dabei dazu, aus Gaps, Anforderungen, Abhängigkeiten und Umsetzungsoptionen eine erste Roadmap mit Work Packages und Transition Architectures zu bilden; Phase F konkretisiert daraus den Implementation and Migration Plan, inklusive Priorisierung, Business Value, Risiken, Abhängigkeiten und Portfolio-/Projektzuschnitt. ([coe.qualiware.com](https://coe.qualiware.com/resources/togaf/9-1/part2-adm/phase-e-opportunities-solutions/))

Der wichtigste fachliche Satz für dich lautet: Eine Roadmap ist gut, wenn sie nicht die Wunschreihenfolge zeigt, sondern die notwendige Reihenfolge begründet.

## 2. Begriffsklärung: Die Bausteine sauber auseinanderhalten

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Ist-Architektur / Baseline Architecture | Der gegenwärtige Zustand der Organisation, Anwendungen, Datenflüsse, Schnittstellen, Betriebsmodelle, Sicherheitsmechanismen und technischen Plattformen. Sie muss nicht perfekt vollständig sein, aber entscheidungsfähig. | Drei Legacy-Fachverfahren, direkte Datenbankkopplungen, lokale Benutzerverwaltung, manuelle Logauswertung, VM-basierter Betrieb. | TOGAF ADM Phasen B–D, Architecture Definition |
| Zielarchitektur / Target Architecture | Der angestrebte Zustand, der fachliche Fähigkeiten, technische Zielbilder, Standards, Governance und Betriebsanforderungen beschreibt. | Standardisierte APIs, zentrales IAM, zentrale Observability, Plattformbetrieb, klar definierte Schnittstellenverträge. | TOGAF Architecture Definition, Phase E/F |
| Gap | Die Differenz zwischen Ist und Ziel. Ein Gap ist kein Wunsch, sondern eine präzise Veränderungslücke. | „Fachverfahren A unterstützt keine zentrale Authentifizierung über das Ziel-IAM.“ | TOGAF Gap Analysis, ArchiMate Gap |
| Plateau | Ein zeitlich begrenzter, relativ stabiler Architekturzustand. Ein Plateau ist ein Zwischenstand, auf dem die Organisation arbeitsfähig bleibt. | „Alle neuen Schnittstellen laufen über API-Gateway; Alt-Schnittstellen bestehen noch kontrolliert weiter.“ | ArchiMate Implementation & Migration |
| Transition Architecture | Eine architekturrelevante Zwischenarchitektur zwischen Ist und Ziel. Sie beschreibt nicht nur Arbeit, sondern einen beherrschbaren Zielzustand auf dem Weg. | „IAM integriert Pilotverfahren; Legacy-Benutzerverwaltung existiert parallel, aber neue Rollenmodelle werden zentral gepflegt.“ | TOGAF Phase E/F |
| Work Package | Ein logisch zusammengehöriges Paket von Veränderungen, das einen Teil der Zielarchitektur realisiert. | „Einführung API-Gateway inklusive OpenAPI-Standard, AuthN/AuthZ-Muster, Fehlercodekonzept und Betriebsmetriken.“ | TOGAF Work Packages, ArchiMate Work Package |
| Abhängigkeit | Eine sachliche Reihenfolgebeziehung zwischen Fähigkeiten, Systemen, Entscheidungen oder Liefergegenständen. | „Plattformmigration setzt Container-Readiness, Secrets Management und Observability voraus.“ | TOGAF Phase E/F |
| Migrationswelle | Eine gebündelte Umsetzungssequenz, meist nach Fachverfahren, Domäne, Risiko, Schnittstellencluster oder Plattformfähigkeit. | „Welle 1: niedrigkritische Registerauskunft; Welle 2: Kernverfahren mit hohem Datenvolumen.“ | Migration Planning |
| Quick Win | Eine schnell realisierbare Verbesserung mit sichtbarem Nutzen, die aber nicht vom Fundament ablenken darf. | Zentrales Log-Dashboard für kritische Schnittstellen, noch bevor die volle Plattformmigration erfolgt. | TOGAF nennt Quick Win als möglichen Umsetzungsansatz |
| Entscheidungsfenster | Zeitraum, in dem eine Entscheidung getroffen werden muss, damit spätere Arbeit nicht blockiert wird. | „Bis Ende Q2 muss entschieden sein, ob Legacy-Fachverfahren B stranguliert oder ersetzt wird.“ | Architektur-Governance |
| Technische Schulden | Bewusst oder unbewusst entstandene Vereinfachungen, die spätere Änderungskosten erhöhen. Für Roadmaps wichtig: Schulden müssen sichtbar, priorisiert und abgebaut oder bewusst toleriert werden. | Temporärer Adapter für Altverfahren wird maximal 18 Monate betrieben; Rückbau ist eigenes Work Package. | Ward Cunningham / Martin Fowler |

ArchiMate beschreibt Plateau, Gap und Work Package als Implementation-and-Migration-Elemente; ein Plateau steht dabei für einen relativ stabilen Architekturzustand während einer begrenzten Zeit, ein Gap für den Unterschied zwischen Plateaus und ein Work Package für eine Serie von Handlungen zur Erreichung bestimmter Ergebnisse unter Zeit- und Ressourcenbedingungen. ([opengroup.org](https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf?utm_source=chatgpt.com)) Der Begriff technische Schulden geht auf Ward Cunningham zurück; Martin Fowler hat später mit seinem Technical-Debt-Quadrant geholfen, Schulden differenzierter nach Absicht und Umgang zu klassifizieren. ([martinfowler.com](https://martinfowler.com/bliki/TechnicalDebt.html?utm_source=chatgpt.com))

## 3. Die wichtigste Denkfigur: Von „Ist → Soll“ zu „Ist → Übergang 1 → Übergang 2 → Ziel“

Der typische Anfängerfehler ist, Ist und Soll nebeneinanderzustellen und daraus sofort Projekte abzuleiten. Das wirkt effizient, ist aber oft architektonisch blind. Zwischen Ist und Soll liegen Zustände, in denen alte und neue Welt gleichzeitig existieren. Genau dort entstehen die echten Risiken: doppelte Benutzerverwaltung, hybride Schnittstellenlandschaft, uneinheitliches Monitoring, parallele Betriebsmodelle, Dateninkonsistenzen, ungeklärte Verantwortlichkeiten und nicht zurückgebaute Übergangslösungen.

Die professionelle Denkfigur lautet daher:

`P0 Ist-Architektur → TA1 Stabilisieren & sichtbar machen → TA2 Standardisieren & zentralisieren → TA3 Migrieren & entkoppeln → PZ Zielarchitektur`

Dabei steht P0 für das Ausgangsplateau, TA1 bis TA3 für Transition Architectures und PZ für das Zielplateau. Jede Transition Architecture muss als eigener, überprüfbarer Architekturzustand beschrieben werden. Nicht „IAM-Projekt gestartet“, sondern: „Pilotverfahren nutzt zentrales IAM produktiv; Rollenmodell, Token-Validierung, Audit-Logging und Rückfallverfahren sind abgenommen.“

## 4. Vorgehensmodell: In zehn Schritten zur belastbaren Transformationsroadmap

### Schritt 1: Ist-Architektur entscheidungsfähig aufnehmen

Du brauchst keine monatelange Vollinventur. Du brauchst eine Baseline, mit der du Architekturentscheidungen treffen kannst. Erfasse vor allem Fachverfahren, Schnittstellen, Datenobjekte, Authentifizierung/Autorisierung, Betriebsmodell, Deployments, Laufzeitumgebungen, Monitoring, Dokumentation, Verträge, Verantwortlichkeiten und bekannte Störungen.

Für das Behördenbeispiel bedeutet das: Du erfasst nicht nur „Fachverfahren A läuft auf VM“. Du erfasst: Welche Bürger- oder Verwaltungsleistung unterstützt es? Welche Daten verarbeitet es? Welche Schnittstellen nutzt es? Wer betreibt es? Wie erfolgt Anmeldung? Gibt es Rollen? Wie wird geloggt? Wer bekommt Störungsmeldungen? Gibt es Herstellerbindung? Gibt es Fristen? Gibt es Datenschutz- oder Sicherheitsauflagen? Gibt es manuelle Workarounds?

### Schritt 2: Zielarchitektur als Fähigkeitsbild formulieren

Eine Zielarchitektur darf nicht nur aus Technologiebegriffen bestehen. „Wir migrieren auf Kubernetes“ ist keine Zielarchitektur. Eine Zielarchitektur beschreibt, welche Fähigkeiten künftig vorhanden sein müssen.

Für das Beispiel wären Ziel-Fähigkeiten: Legacy-Fachverfahren werden schrittweise modernisiert oder stranguliert; neue und modernisierte Systeme stellen fachlich dokumentierte APIs bereit; Zugriff erfolgt über zentrales IAM; technische und fachliche Betriebsereignisse sind beobachtbar; Deployment und Betrieb erfolgen über eine standardisierte Plattform; Architekturentscheidungen werden über ADRs nachvollziehbar gemacht; Übergangslösungen haben Rückbaukriterien.

### Schritt 3: Gaps präzise formulieren

Ein Gap muss immer drei Dinge enthalten: den Ist-Zustand, den Zielzustand und die Veränderungslücke. Falsch wäre: „IAM fehlt.“ Richtig wäre: „Fachverfahren A verwaltet Benutzer lokal; Ziel ist zentrale Authentifizierung und rollenbasierte Autorisierung über das Behörden-IAM; Gap ist fehlende Integration, fehlendes Rollenmapping, fehlende Tokenprüfung, fehlendes Audit-Logging und fehlendes Betriebsverfahren bei IAM-Störung.“

Diese Präzision ist wichtig, weil aus jedem guten Gap später ein Work Package, eine Entscheidung, ein Risiko oder ein Akzeptanzkriterium entstehen kann.

### Schritt 4: Gaps clustern

Nicht jeder Gap wird ein eigenes Projekt. Du gruppierst Gaps nach Architekturwirkung. Typische Cluster sind: Schnittstellenstandardisierung, Identitäts- und Berechtigungsmanagement, Datenmodell und Stammdaten, Plattformfähigkeit, Betriebsfähigkeit, Security, Testbarkeit, Dokumentation, Hersteller-/Vertragsabhängigkeiten und Rückbau technischer Schulden.

Der professionelle Blick ist hier: Ein Gap kann klein aussehen, aber eine hohe Enablement-Wirkung haben. Ein API-Gateway oder ein IAM-Adapter kann als Fundament viele spätere Migrationen ermöglichen, auch wenn der unmittelbare Fachnutzen auf dem Papier zunächst kleiner wirkt.

### Schritt 5: Transition Architectures definieren

Jetzt beschreibst du realistische Zwischenzustände. Eine Transition Architecture ist kein Sprintziel und kein Projektstatus, sondern ein Zustand der Unternehmensarchitektur. Sie muss fachlich nutzbar, technisch betreibbar, sicherbar, testbar und governancefähig sein.

Beispiel: TA1 könnte lauten: „Transparenz- und Stabilisierungsschicht“. In diesem Zustand bleiben die Legacy-Fachverfahren weitgehend unverändert, aber ihre Schnittstellen, Betriebsereignisse, Nutzergruppen, Datenflüsse und Risiken sind sichtbar. Kritische Schnittstellen werden überwacht. Neue Schnittstellen müssen nach API-Standard beschrieben werden. Erste technische Schulden sind im Architektur-Backlog erfasst.

### Schritt 6: Work Packages schneiden

Work Packages sollen nicht nach Organisationssilos geschnitten werden, sondern nach Architekturwirkung. Ein schlechtes Work Package lautet: „Team IAM arbeitet an Keycloak.“ Ein gutes Work Package lautet: „Zentrale IAM-Basisfähigkeit für Fachverfahrenintegration bereitstellen, inklusive Mandanten-/Realm-Konzept, Rollenmodell, Token-Validierung, Audit-Logging, Betriebsverfahren, Referenzintegration und Sicherheitsabnahme.“

Ein Work Package muss einen Ergebniszustand liefern, nicht nur Beschäftigung.

### Schritt 7: Abhängigkeiten modellieren

Erst modellierst du Abhängigkeiten, dann planst du Termine. Nicht umgekehrt.

Typische Abhängigkeiten im Beispiel: API-Standard vor API-Massenmigration; IAM-Zielbild vor Fachverfahrenintegration; Observability-Baseline vor Plattformmigration; Datenklassifikation vor Schnittstellenumbau; Betriebsmodell vor Produktivsetzung; Entscheidung „Replace vs. Strangle“ vor Ausschreibung; Secrets Management vor Containerisierung; Netzwerk- und Sicherheitszonen vor Plattformbetrieb.

### Schritt 8: Risiken und technische Schulden bewusst aufnehmen

Eine Roadmap ohne Risiken ist meistens politisch hübsch und fachlich schwach. Risiken gehören in die Roadmap, weil sie die Reihenfolge beeinflussen. Technische Schulden ebenfalls, weil sie sonst als unsichtbare Zusatzkosten später wieder auftauchen.

Du unterscheidest: Schulden, die toleriert werden; Schulden, die vor Migration abgebaut werden müssen; Schulden, die während der Migration entstehen dürfen; Schulden, deren Rückbau eigenes Work Package wird.

### Schritt 9: Migrationswellen bilden

Migrationswellen sollten nicht rein kalendarisch gebildet werden. Gute Kriterien sind Kritikalität, fachliche Domäne, Schnittstellenkomplexität, Datenvolumen, Sicherheitsanforderungen, Änderungsbereitschaft der Fachseite, Herstellerabhängigkeit, Betriebsrisiko und Wiederverwendbarkeit der gewonnenen Muster.

Eine gute erste Welle ist selten das kritischste Kernverfahren. Sie ist aber auch nicht beliebig. Sie sollte repräsentativ genug sein, um Muster zu testen, und ungefährlich genug, um Fehler beherrschbar zu halten.

### Schritt 10: Entscheidungsfenster und Governance einbauen

Eine Roadmap braucht Entscheidungspunkte. Ohne Entscheidungspunkte wird sie zu einer Wunschliste. Beispiele: „Bis Ende Q1 Entscheidung IAM-Zielprodukt“, „bis Mitte Q2 Entscheidung API-Gateway-Betriebsmodell“, „bis Ende Q2 Entscheidung Strangler Pattern vs. Ersatzbeschaffung für Fachverfahren B“, „bis Q3 Entscheidung Plattformbetriebsmodell intern/extern“, „vor jeder Migrationswelle Architecture Compliance Review“.

TOGAF Phase E betont ausdrücklich die Prüfung von Abhängigkeiten, Transformationsbereitschaft, Risiken, Umsetzungsstrategie, Work Packages und Transition Architectures; Phase F konkretisiert Priorisierung, Business Value, Kosten/Nutzen, Risiken, Projektzuschnitt, Ressourcen und den finalen Implementation and Migration Plan. ([coe.qualiware.com](https://coe.qualiware.com/resources/togaf/9-1/part2-adm/phase-e-opportunities-solutions/))

## 5. Roadmap-Vorlage: So strukturierst du sie professionell

| Aspekt | Details/Erklärung | Beispiel | Metrik/Artefakt | Literatur/Quelle |
|---|---|---|---|---|
| Roadmap-ID | Eindeutige Kennung der Roadmap oder Transformationslinie. | TRM-FV-2026-01 | Roadmap-Register | TOGAF Architecture Roadmap |
| Architekturdomäne | Einordnung nach Business, Application, Data, Technology, Security, Operations. | Application + Security + Operations | Domänenmapping | TOGAF ADM B–D |
| Ausgangsplateau | Stabil beschriebener Ist-Zustand. | P0: Legacy-Fachverfahren mit lokalen Benutzern und Punkt-zu-Punkt-Schnittstellen. | Baseline-Diagramm, Systemkatalog | ArchiMate Plateau |
| Zielplateau | Angestrebter Endzustand. | PZ: Standardisierte APIs, zentrales IAM, Plattformbetrieb, zentrale Observability. | Target Architecture View | TOGAF Target Architecture |
| Transition Architecture | Architekturrelevanter Zwischenzustand. | TA2: Neue APIs über Gateway, Pilotverfahren am IAM, zentrale Logs für kritische Verfahren. | Transition Architecture Description | TOGAF Phase E/F |
| Gap | Präzise Veränderungslücke zwischen Ist und Ziel. | Lokale Benutzerverwaltung muss an zentrales IAM angebunden oder abgelöst werden. | Gap-Matrix | TOGAF Gap Analysis, ArchiMate Gap |
| Work Package | Logische Veränderungseinheit mit Ergebnisverantwortung. | WP-IAM-01: IAM-Basisfähigkeit und Referenzintegration. | Work-Package-Steckbrief | TOGAF Work Package |
| Abhängigkeiten | Sachliche Vorbedingungen, Nachbedingungen und Kopplungen. | IAM-Rollenmodell vor Migration von Fachverfahren A. | Dependency Map, RAID-Log | TOGAF Phase E/F |
| Risiken | Eintrittswahrscheinlichkeit, Auswirkung, Gegenmaßnahme, Restrestrisiko. | Hersteller unterstützt moderne Authentifizierung nicht. | Risiko-Register | Migration Planning |
| Technische Schulden | Bewusste Altlasten, Übergangslösungen und Rückbaupflichten. | Temporärer IAM-Adapter darf maximal bis Q4/2027 betrieben werden. | Debt Register | Cunningham/Fowler |
| Entscheidungsfenster | Zeitpunkt, bis zu dem eine Architekturentscheidung getroffen werden muss. | Q2: Entscheidung Replace vs. Strangle für Legacy-Verfahren B. | ADR, Entscheidungsvorlage | Architektur-Governance |
| Akzeptanzkriterien | Prüfpunkte, wann ein Plateau oder Work Package wirklich erreicht ist. | 95 Prozent kritischer Schnittstellen mit Monitoring; Pilotverfahren produktiv am IAM. | Abnahmeprotokoll | Implementation Governance |
| Migrationswelle | Bündelung betroffener Systeme oder Fähigkeiten. | Welle 1: niedrigkritische Auskunftsverfahren; Welle 2: Kernverfahren. | Wave Plan | Migration Planning |
| Governance-Gate | Verbindlicher Prüftermin für Architekturkonformität. | Vor Produktivsetzung: Security-, Betrieb-, API- und IAM-Review. | Architecture Compliance Review | TOGAF Phase G |

Diese Vorlage zwingt dich, nicht in Kalenderlogik zu verfallen. Der Kalender kommt erst nach Architekturzuständen, Abhängigkeiten und Risiken. Genau darin liegt der Unterschied zwischen Projektmanagement und Enterprise Architecture.

## 6. Priorisierungsmethode: Erst Abhängigkeiten, dann Nutzen, dann Risiko

Eine häufige Fehlsteuerung entsteht, wenn Organisationen nach „Business Value“ priorisieren, ohne Abhängigkeiten zu beachten. Dann landet das sichtbarste Fachverfahren oben, obwohl Plattform, IAM, Schnittstellenstandard und Observability noch nicht tragfähig sind. Professionell ist ein zweistufiges Vorgehen.

Zuerst baust du eine Abhängigkeitslogik. Alles, was architektonisch zwingende Vorbedingung ist, wird nicht wegpriorisiert, nur weil es weniger glamourös klingt. Danach bewertest du die innerhalb dieser Abhängigkeitslogik möglichen Work Packages.

Ich empfehle dir für Behördenkontexte eine einfache, aber starke Methode: **BADER-Priorisierung**. BADER steht für Business Value, Architektur-Enabler, Dringlichkeit, Effort und Risikoabbau.

| Aspekt | Details/Erklärung | Beispiel | Bewertung | Literatur/Quelle |
|---|---|---|---|---|
| Business Value | Welcher fachliche, organisatorische oder servicebezogene Nutzen entsteht? | Schnellere Bearbeitung, weniger Medienbruch, bessere Verfügbarkeit. | 1 = gering, 5 = sehr hoch | TOGAF Business Value in Phase F |
| Architektur-Enabler | Wie stark ermöglicht das Paket spätere Zielarchitektur? | IAM-Basisfähigkeit ermöglicht mehrere Fachverfahrenmigrationen. | 1 = isoliert, 5 = stark ermöglichend | TOGAF Work Packages / Dependencies |
| Dringlichkeit | Gibt es Fristen, Sicherheitsdruck, Vertragsende, Herstellerabkündigung oder politische Terminvorgaben? | Wartungsende Legacy-Middleware in 12 Monaten. | 1 = flexibel, 5 = kritisch | Migration Planning |
| Effort | Aufwand, Komplexität, Beschaffung, Personalbedarf, Fachbereichsbelastung. | Plattformmigration mit Schulung, Betriebsmodell und Refactoring. | 1 = niedrig, 5 = sehr hoch | Projekt-/Portfolioplanung |
| Risikoabbau | Reduziert das Paket Betriebs-, Sicherheits-, Integrations- oder Lieferantenrisiken? | Observability senkt Blindflug im Betrieb. | 1 = kaum, 5 = stark | TOGAF Risiko-Validierung |
| Abhängigkeitssperre | Ist das Paket Vorbedingung für andere Pakete? | API-Standard vor API-Massenumbau. | Ja/Nein, zusätzlich Dependency-Rank | TOGAF Dependency Refinement |

Die einfache Bewertungsformel lautet:

`Priorität = (Business Value × 2) + (Architektur-Enabler × 3) + (Dringlichkeit × 2) + (Risikoabbau × 2) - (Effort × 1)`

Diese Formel ist kein Naturgesetz. Sie ist ein Moderationswerkzeug. Der Faktor „Architektur-Enabler × 3“ ist bewusst hoch, weil Behördenmodernisierung oft daran scheitert, dass sichtbare Fachfunktionen vor Fundamentfähigkeiten priorisiert werden. Genau dann entstehen neue Silos unter modernem Namen.

Ein Work Package mit niedrigem direktem Fachnutzen kann trotzdem höchste Priorität haben, wenn es viele spätere Lieferungen ermöglicht. TOGAF Phase F weist ausdrücklich darauf hin, dass ein Projekt hohe Priorität verdienen kann, wenn es einen kritischen Liefergegenstand auf dem Weg zu einem größeren Nutzen bereitstellt, selbst wenn der unmittelbare Nutzen des Projekts selbst gering ist. ([coe.qualiware.com](https://coe.qualiware.com/resources/togaf/9-1/part2-adm/phase-f-migration-planning/))

## 7. Behördenbeispiel: Modernisierung von Legacy-Fachverfahren

### Ausgangslage

Die Behörde betreibt mehrere Legacy-Fachverfahren. Einige sind Eigenentwicklungen, andere Herstellerprodukte. Schnittstellen sind historisch gewachsen, teilweise dateibasiert, teilweise direkte Datenbankzugriffe, teilweise SOAP oder proprietäre REST-Endpunkte ohne einheitliches Fehler- und Versionierungskonzept. Benutzer werden in mehreren Verfahren lokal gepflegt. Logging ist technisch vorhanden, aber nicht zentral auswertbar. Betriebswissen liegt bei wenigen Personen. Die Zielarchitektur sieht standardisierte Schnittstellen, zentrales IAM, bessere Observability und eine Migration auf eine Plattform vor.

### Zielbild

Das Zielbild ist nicht „alles neu“. Das Zielbild lautet: Fachverfahren werden schrittweise modernisiert, entkoppelt und betrieblich beherrschbar gemacht. Neue Schnittstellen werden API-first entworfen. Authentifizierung und Autorisierung werden zentralisiert. Betriebsereignisse werden zentral beobachtbar. Plattformfähige Anwendungen werden standardisiert betrieben. Legacy-Komponenten bleiben nur dort temporär bestehen, wo ihr Weiterbetrieb ausdrücklich begründet, überwacht und mit Rückbaukriterium versehen ist.

## 8. Beispielroadmap mit Übergangsarchitekturen

Annahme: Die folgende Roadmap ist ein generisches Behördenbeispiel über 24 Monate. Sie ist nicht als konkrete BAMF-, Ministeriums- oder Vergaberealität zu verstehen, sondern als methodisches Muster.

| Aspekt | Details/Erklärung | Beispiel | Risiken/Entscheidungen | Literatur/Quelle |
|---|---|---|---|---|
| P0 — Ist-Plateau, Monat 0 | Legacy-Landschaft wird entscheidungsfähig beschrieben. Keine große Modernisierung beginnt ohne Transparenz über Schnittstellen, Daten, IAM, Betrieb und Kritikalität. | Systemkatalog, Schnittstellenlandkarte, Datenflussübersicht, Benutzerverwaltungsinventar, Betriebsrisiken. | Risiko: Analyse wird zur Endlosschleife. Entscheidung: Minimal notwendige Baseline definieren. | TOGAF Baseline Architecture, ArchiMate Plateau |
| TA1 — Stabilisieren und sichtbar machen, Monat 1–6 | Die Altlandschaft bleibt funktional, wird aber beobachtbar, dokumentiert und governancefähig. Neue Änderungen unterliegen Mindeststandards. | Zentrales Logging für kritische Schnittstellen, API-Design-Guideline, ADR-Pflicht, Debt Register, Störungskategorien. | Entscheidung bis Monat 3: Observability-Stack und API-Mindeststandard. Risiko: Teams empfinden Standards als Zusatzbürokratie. | TOGAF Phase E Work Packages |
| Work Package TA1.1 | Baseline & Architektur-Inventar. | Fachverfahrensteckbriefe, Schnittstellenmatrix, Kritikalitätsmatrix. | Risiko: fehlendes Wissen bei Dienstleistern. Gegenmaßnahme: Architekturinterviews und Dokumentationsabnahme. | Architecture Repository |
| Work Package TA1.2 | Observability-Minimum. | Zentrale Logs, technische Metriken, Schnittstellenfehler, Betriebsdashboards für Top-10-kritische Flüsse. | Risiko: uneinheitliche Logformate. Entscheidung: Mindestformat und Korrelations-ID. | Operations / Migration Planning |
| Work Package TA1.3 | API- und ADR-Governance. | OpenAPI-Pflicht für neue REST-Schnittstellen, Versionierungsregeln, Fehlercodekonzept, ADR-Template. | Risiko: neue Standards werden umgangen. Gegenmaßnahme: Architecture Review Gate. | TOGAF Implementation Governance |
| TA2 — Standardisieren und zentralisieren, Monat 6–12 | Erste zentrale Architekturbausteine sind produktiv nutzbar. Neue oder modernisierte Fachverfahren integrieren IAM und API-Standards. | IAM-Pilot produktiv, API-Gateway eingeführt, Rollenmodell für Pilotdomäne, zentrale Audit-Logs. | Entscheidung bis Monat 8: IAM-Zielmodell und Betriebsverantwortung. Risiko: Rollenmodell wird fachlich unterschätzt. | TOGAF Transition Architecture |
| Work Package TA2.1 | IAM-Basisfähigkeit. | Mandanten-/Realm-Konzept, Rollen-/Rechte-Modell, Token-Validierung, Audit, Notfallverfahren. | Risiko: Altverfahren können moderne Protokolle nicht direkt nutzen. Entscheidung: Adapter vs. Anpassung vs. Ersatz. | Security Architecture / IAM |
| Work Package TA2.2 | API-Gateway und Schnittstellenstandard. | Gateway, Routing, Authentifizierung, Rate Limits, Versionierung, Deprecation-Konzept, API-Katalog. | Risiko: Gateway wird nur technischer Proxy statt Governance-Punkt. | API Architecture |
| Work Package TA2.3 | Referenzintegration Pilotverfahren. | Ein nicht maximal kritisches, aber repräsentatives Verfahren nutzt IAM, API-Standard und Observability. | Risiko: Pilot ist zu trivial. Entscheidung: Pilotkriterien verbindlich machen. | Migration Planning |
| TA3 — Migrieren und entkoppeln, Monat 12–18 | Erste Migrationswellen laufen nach wiederholbarem Muster. Legacy wird nicht nur angebunden, sondern gezielt reduziert. | Zwei Fachverfahren modernisiert oder stranguliert; kritische Datenflüsse entkoppelt; Plattform-Readiness geprüft. | Entscheidung bis Monat 14: Replace, Refactor, Rehost oder Strangle je Verfahren. Risiko: Übergangsadapter werden dauerhaft. | TOGAF Phase F |
| Work Package TA3.1 | Migrationswelle 1. | Niedrig- bis mittelriskantes Fachverfahren wird auf Zielmuster gebracht. | Risiko: Fachbereich testet zu spät. Gegenmaßnahme: frühe Abnahmeszenarien. | Implementation and Migration Plan |
| Work Package TA3.2 | Plattform-Basis und Betriebsmodell. | CI/CD, Container-Readiness, Secrets, Netzsegmentierung, Backup/Restore, Betriebsübergabe. | Risiko: Plattform wird eingeführt, ohne Betriebsreife. Entscheidung: Mindest-Betriebsabnahme vor Produktivmigration. | Technology Architecture |
| Work Package TA3.3 | Rückbau erster technischer Schulden. | Deaktivierung alter Punkt-zu-Punkt-Schnittstellen, Entfernung lokaler Schattenbenutzer, Abschaltung alter Jobs. | Risiko: Niemand fühlt sich für Rückbau verantwortlich. Gegenmaßnahme: Rückbau als eigenes Lieferobjekt. | Technical Debt Management |
| TA4 — Skalieren und konsolidieren, Monat 18–24 | Das Muster wird auf weitere Verfahren übertragen. Governance, Betrieb, Plattform und IAM sind keine Piloten mehr, sondern Standard. | Migrationswelle 2 und 3; API-Katalog verbindlich; Alt-Schnittstellen reduziert; Betriebskennzahlen stabil. | Entscheidung bis Monat 20: Restlegacy-Strategie und Vertrags-/Ausschreibungsbedarf. Risiko: Parallelwelten bleiben zu lange. | Architecture Roadmap |
| Zielplateau PZ, ab Monat 24 | Die Zielarchitektur ist nicht vollständig „fertig“, aber als Regelbetrieb etabliert. Abweichungen sind begründet, befristet und sichtbar. | Plattformbetrieb, zentrales IAM, Observability, API-Governance, dokumentierte Restlegacy, Rückbauplan. | Risiko: Zielbild wird nach Projektende nicht weitergeführt. Gegenmaßnahme: Architecture Change Management. | TOGAF Phase H / Governance |

## 9. Beispiel: Aus einem Gap wird ein Work Package

Nehmen wir das Gap: „Lokale Benutzerverwaltung in Legacy-Fachverfahren verhindert zentrales IAM.“

Schwach formuliert wäre daraus: „IAM integrieren.“

Professionell formulierst du daraus:

Das Work Package „IAM-Integration Legacy-Fachverfahren Welle 1“ liefert die technische und fachliche Anbindung ausgewählter Fachverfahren an das zentrale IAM. Der Auftrag umfasst Rollen- und Rechteanalyse, Mapping lokaler Benutzergruppen auf zentrale Rollen, technische Authentifizierungsintegration, Autorisierungsprüfung, Audit-Logging, Betriebs- und Störungsverfahren, Testfälle, Dokumentation, Schulung der Betriebsverantwortlichen und Rückbauplan für lokale Benutzerpflege. Das Work Package gilt als abgeschlossen, wenn mindestens ein repräsentatives Fachverfahren produktiv über das zentrale IAM authentifiziert, fachlich berechtigte Rollen korrekt autorisiert, sicherheitsrelevante Ereignisse zentral auditierbar sind, lokale Benutzerpflege für den produktiven Standardfall deaktiviert ist und ein genehmigtes Rückfallverfahren existiert.

So wird aus Architektur eine prüfbare Lieferung.

## 10. Wie du Quick Wins richtig einsetzt

Quick Wins sind nützlich, aber gefährlich, wenn sie Fundamentarbeit verdrängen. Ein Quick Win darf nicht nur sichtbar sein; er sollte idealerweise auch in Richtung Zielarchitektur zeigen.

Gute Quick Wins im Beispiel wären: zentrale Sicht auf kritische Schnittstellenfehler; ein API-Katalog für neue Schnittstellen; ein ADR-Template mit Review-Prozess; eine Schnittstellenampel nach Kritikalität; ein Pilotverfahren mit sauberer IAM-Anbindung; ein Dashboard für Verfügbarkeit und Fehlerquoten.

Schlechte Quick Wins wären: ein neues Frontend auf altem Chaos; eine weitere Sonder-Schnittstelle für einen politischen Termin; ein manueller Report, der Observability nur simuliert; eine Containerisierung ohne Betriebsmodell; ein API-Gateway als reiner Durchleitungsproxy ohne Standards.

Der Merksatz: Ein guter Quick Win macht den Zielpfad leichter. Ein schlechter Quick Win macht den Zielpfad nur kurzfristig hübscher.

## 11. Entscheidungsfenster: Der unterschätzte Teil der Roadmap

Entscheidungsfenster sind in der Behördenarchitektur besonders wichtig, weil Vergabe, Haushalt, Datenschutz, IT-Sicherheit, Fachseite, Betrieb, Dienstleister und Leitung oft unterschiedliche Takte haben. Wenn Architekturentscheidungen zu spät fallen, werden Projekte gezwungen, lokale Ersatzentscheidungen zu treffen. Daraus entstehen später neue Schulden.

| Aspekt | Details/Erklärung | Beispiel | Konsequenz bei verpasstem Fenster | Literatur/Quelle |
|---|---|---|---|---|
| Produkt-/Technologieentscheidung | Auswahl oder Bestätigung zentraler Zielkomponenten. | IAM-Zielsystem, API-Gateway, Observability-Stack. | Teams bauen Zwischenlösungen, die später abgelöst werden müssen. | TOGAF Architecture Governance |
| Architekturpattern | Verbindliches Modernisierungsmuster. | Strangler Pattern, Rehost, Refactor, Replace. | Jedes Fachverfahren entscheidet anders; Standardisierung scheitert. | Migration Planning |
| Betriebsmodell | Klärung von Verantwortung, SLAs, Rufbereitschaft, Incident-Prozess. | Plattformbetrieb intern, extern oder hybrid. | Produktivsetzung verzögert sich oder Betrieb bleibt unsicher. | IT Service Management |
| Sicherheitsentscheidung | Klärung von Zonen, Authentifizierung, Autorisierung, Audit, Secrets. | Token-Lebensdauer, Rollenmodell, Zertifikatsmanagement. | Sicherheitsreviews stoppen späte Releases. | Security Architecture |
| Rückbauentscheidung | Festlegung, wann temporäre Altlasten entfernt werden. | Abschaltung lokaler Benutzerpflege nach IAM-Migration. | Übergangsarchitektur wird Dauerarchitektur. | Technical Debt Management |

Für dich als Enterprise Architekt ist das ein Machtinstrument im besten fachlichen Sinne: Du zwingst die Organisation nicht zu vorschnellen Entscheidungen, aber du machst sichtbar, wann Nichtentscheiden selbst zur Entscheidung wird.

## 12. Technische Schulden in der Roadmap sichtbar machen

Technische Schulden gehören nicht in eine versteckte Entwicklerliste. Sie gehören in die Roadmap, sobald sie Architekturwirkung haben.

Du verwendest dafür vier Kategorien:

| Aspekt | Details/Erklärung | Beispiel | Umgang | Literatur/Quelle |
|---|---|---|---|---|
| Tolerierte Schuld | Bewusst akzeptierte Abweichung mit Ablaufdatum. | Temporärer Adapter zwischen Legacy-Auth und zentralem IAM. | Befristen, überwachen, Rückbau terminieren. | Cunningham/Fowler |
| Blockierende Schuld | Muss vor einem Zielzustand beseitigt werden. | Anwendung kann keine eindeutigen Benutzeridentitäten verarbeiten. | Vor Migrationswelle beheben. | Technical Debt Management |
| Entstehende Schuld | Wird durch Übergang bewusst erzeugt. | Doppelte Logik im Legacy-System und neuer Plattform. | Als Übergang dokumentieren, Rückbaupflicht definieren. | Technical Debt Quadrant |
| Unbekannte Schuld | Vermutete Altlast, deren Umfang noch unklar ist. | Alte Batch-Jobs mit unklarem Datenbesitz. | Discovery-Work-Package einplanen. | Architecture Discovery |

Der entscheidende Punkt: Technische Schulden sind nicht automatisch Versagen. Sie werden gefährlich, wenn sie unsichtbar, unbegrenzt und ohne Eigentümer bleiben.

## 13. Typische Fehler beim Bau von Transformationsroadmaps

| Aspekt | Details/Erklärung | Beispiel | Korrektur | Literatur/Quelle |
|---|---|---|---|---|
| Roadmap als Terminliste | Es werden Quartale gefüllt, aber keine Architekturzustände beschrieben. | „Q1 IAM, Q2 APIs, Q3 Plattform.“ | Plateaus und Transition Architectures definieren. | TOGAF Architecture Roadmap |
| Zielarchitektur zu abstrakt | Das Zielbild enthält Schlagwörter, aber keine prüfbaren Fähigkeiten. | „Cloud-ready, API-first, sicher.“ | Fähigkeiten, Standards und Akzeptanzkriterien formulieren. | TOGAF Target Architecture |
| Abhängigkeiten zu spät erkannt | Termine werden geplant, bevor sachliche Reihenfolgen verstanden sind. | Plattformmigration startet ohne Observability. | Dependency Map vor Roadmap erstellen. | TOGAF Phase E/F |
| Quick Wins verdrängen Fundament | Sichtbare kleine Erfolge erzeugen neue Altlasten. | Neues Portal vor Schnittstellenstandard. | Quick Wins nur zulassen, wenn sie Zielmuster stärken. | Migration Strategy |
| Transition Architecture fehlt | Zwischenzustände werden nicht beschrieben. | Alte und neue IAM-Welt laufen parallel ohne Zielbild. | Jede Übergangsphase als stabilen Architekturzustand beschreiben. | TOGAF Transition Architecture |
| Work Packages sind Tätigkeiten | Pakete beschreiben Arbeit, aber kein Ergebnis. | „APIs bauen.“ | Liefergegenstände und Abnahmekriterien definieren. | TOGAF Work Packages |
| Rückbau wird vergessen | Übergangslösungen bleiben dauerhaft. | Temporärer Adapter läuft drei Jahre produktiv. | Rückbau als eigenes Work Package planen. | Technical Debt |
| Betrieb wird nachgelagert | Projekt liefert Software, aber keine Betriebsfähigkeit. | Keine Dashboards, keine Runbooks, keine SLAs. | Betriebsabnahme als Gate einführen. | ITSM / Implementation Governance |
| Fachseite wird zu spät eingebunden | Rollen, Prozesse und Datenbedeutung werden technisch geraten. | IAM-Rollenmodell passt nicht zur Sachbearbeitung. | Fachliche Capability- und Rollenworkshops früh durchführen. | Business Architecture |
| Risiken werden beschönigt | Roadmap sieht glatt aus, ist aber nicht glaubwürdig. | Herstellerabhängigkeit wird nicht erwähnt. | Risiko, Gegenmaßnahme und Restrestrisiko sichtbar machen. | TOGAF Risk Validation |
| Architekturentscheidungen fehlen | Teams entscheiden lokal, weil zentrale Entscheidungen ausbleiben. | Drei unterschiedliche Auth-Patterns. | ADRs und Entscheidungsfenster verbindlich machen. | Architecture Governance |
| Alles wird gleichzeitig gestartet | Organisation überschätzt Veränderungskapazität. | IAM, Plattform, APIs, Datenmigration und Ausschreibung parallel. | Migrationswellen nach Absorptionsfähigkeit schneiden. | Business Transformation Readiness |

## 14. Die Roadmap als Architekturansicht: Was du zeigen solltest

Eine gute Roadmap hat mindestens vier Sichten.

Die erste Sicht ist die **Zeit- und Plateau-Sicht**. Sie zeigt P0, TA1, TA2, TA3 und PZ. Diese Sicht ist für Leitung, Portfolio und Programmsteuerung geeignet.

Die zweite Sicht ist die **Domänen-Sicht**. Sie zeigt je Plateau, was sich in Business, Application, Data, Integration, Security/IAM, Operations und Technology verändert. Diese Sicht ist für Architekten und technische Steuerung entscheidend.

Die dritte Sicht ist die **Dependency-Sicht**. Sie zeigt, welche Work Packages andere ermöglichen oder blockieren. Diese Sicht verhindert Wunschplanung.

Die vierte Sicht ist die **Risk-&-Decision-Sicht**. Sie zeigt Risiken, technische Schulden, Entscheidungsfenster und Governance-Gates. Diese Sicht macht die Roadmap steuerbar.

Als Enterprise Architekt musst du nicht alles in eine überladene Grafik pressen. Besser sind vier saubere Views mit gemeinsamer ID-Struktur.

## 15. Minimaler Artefaktsatz für deine Arbeit als Enterprise Architekt

Du solltest für eine professionelle Roadmap mindestens diese Artefakte liefern: Architecture Vision, Baseline Summary, Target Architecture Summary, Gap Matrix, Dependency Map, Work-Package-Katalog, Transition-Architecture-Beschreibungen, Roadmap View, Risiko- und Schuldenregister, Entscheidungslog mit ADRs, Migrationswellenplan, Governance-Gates und Abnahmekriterien.

Wichtig: Nicht jedes Artefakt muss ein 60-seitiges Dokument sein. In einer guten Behördenrealität reichen oft kurze, präzise, versionierte Arbeitsartefakte. Entscheidend ist nicht Papiermenge, sondern Entscheidungsfähigkeit.

## 16. Konkrete Mini-Vorlage: Work-Package-Steckbrief

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Work-Package-ID | Eindeutige Kennung. | WP-IAM-01 | TOGAF Work Package |
| Name | Ergebnisorientierter Name. | IAM-Basisfähigkeit für Fachverfahrenintegration. | TOGAF Phase E |
| Zielbeitrag | Welchen Teil der Zielarchitektur realisiert das Paket? | Zentrale Authentifizierung und Auditierbarkeit. | Target Architecture |
| Betroffene Gaps | Welche Lücken werden geschlossen? | Lokale Benutzerverwaltung, fehlendes Rollenmapping, fehlendes Audit. | Gap Analysis |
| Liefergegenstände | Konkrete Ergebnisse. | Rollenmodell, technische Integration, Runbook, Testfälle, ADRs. | Implementation Planning |
| Abhängigkeiten | Vorbedingungen und Nachbedingungen. | IAM-Zielentscheidung, Netzwerkfreigaben, Fachrollenklärung. | Dependency Matrix |
| Risiken | Relevante Unsicherheiten. | Legacy unterstützt moderne Protokolle nicht. | Risk Register |
| Technische Schulden | Entstehende oder abgebaute Schulden. | Temporärer Adapter, Rückbau bis Q4/2027. | Technical Debt |
| Akzeptanzkriterien | Prüfpunkte für Abnahme. | Pilotverfahren produktiv angebunden; Audit-Events zentral sichtbar. | Implementation Governance |
| Verantwortliche | Fachlich, technisch, betrieblich. | Fachbereich, IAM-Team, Plattformteam, Betrieb, Dienstleister. | Governance Model |
| Entscheidungsbedarf | Notwendige Architekturentscheidungen. | Adapter vs. Refactoring; Token-Lebensdauer; Rollengranularität. | ADR |
| Metriken | Messbare Wirkung. | Anzahl angebundener Verfahren, Login-Fehlerquote, Audit-Abdeckung. | Operations / Observability |

## 17. Deine Übung

Du bekommst folgende Ausgangslage: Eine Behörde hat fünf Fachverfahren. Verfahren A ist kritisch und monolithisch. Verfahren B ist mittelwichtig und hat bereits REST-Schnittstellen. Verfahren C ist ein Herstellerprodukt. Verfahren D ist ein altes Batch-Verfahren. Verfahren E ist neu geplant. Es gibt kein zentrales IAM, keine einheitliche API-Governance, keine zentrale Observability und keine Plattformstandardisierung.

Deine Aufgabe ist, daraus eine Roadmap mit drei Transition Architectures zu bauen.

Bearbeite die Übung in dieser Reihenfolge: Beschreibe zuerst P0 als Ist-Plateau. Formuliere dann das Zielplateau PZ. Schreibe mindestens acht Gaps. Gruppiere die Gaps in vier Cluster. Definiere drei Transition Architectures. Schneide mindestens sechs Work Packages. Zeichne die wichtigsten Abhängigkeiten. Definiere zwei Quick Wins, aber begründe, warum sie den Zielpfad stärken. Lege drei Entscheidungsfenster fest. Benenne fünf technische Schulden inklusive Rückbaupflicht. Formuliere je Transition Architecture mindestens drei Akzeptanzkriterien.

Eine mögliche Lösungsskizze wäre: TA1 schafft Transparenz, API-Mindeststandard und Observability-Minimum. TA2 liefert IAM-Basisfähigkeit, API-Gateway und Referenzintegration mit Verfahren B oder E. TA3 migriert Verfahren B/E auf Zielmuster, kapselt Verfahren A über Strangler-Ansatz, bewertet Verfahren C vertraglich und technisch und plant Verfahren D als kontrollierten Rückbau- oder Ersatzkandidaten.

## 18. Prüfungsfragen für dich selbst

Wenn du deine Roadmap fertig hast, prüfe sie mit diesen Fragen: Kann ich erklären, warum diese Reihenfolge notwendig ist? Kann ich zeigen, welcher Zwischenzustand nach sechs, zwölf und achtzehn Monaten stabil betreibbar ist? Gibt es Work Packages, die nur Tätigkeiten, aber keine Architekturwirkung beschreiben? Sind Übergangslösungen befristet? Sind Rückbauarbeiten eingeplant? Gibt es Entscheidungen, die rechtzeitig vor Ausschreibung, Umsetzung oder Migration fallen müssen? Ist Observability vor riskanter Migration vorhanden? Ist IAM fachlich mit Rollen und Verantwortlichkeiten geklärt oder nur technisch geplant? Sind Risiken sichtbar genug, um glaubwürdig zu sein? Kann ein Leitungsgremium erkennen, wo es entscheiden muss?

## 19. Merksätze für deinen Alltag als Enterprise Architekt

Eine Zielarchitektur ohne Roadmap ist eine Vision ohne Traktion. Eine Roadmap ohne Transition Architectures ist ein Terminplan ohne Architektur. Ein Work Package ohne Akzeptanzkriterien ist Beschäftigung, keine Lieferung. Ein Quick Win ohne Zielbezug ist eine neue Altlast mit freundlichem Namen. Eine Übergangsarchitektur ohne Rückbaukriterium wird fast immer Dauerarchitektur. Und eine Roadmap, die keine Risiken zeigt, zeigt meistens nicht die Realität.

## 20. Dein professionelles Zielbild

Am Ende sollst du als Enterprise Architekt nicht sagen: „Wir haben eine Roadmap bis 2028.“ Du sollst sagen können: „Wir führen die Organisation über drei beherrschbare Architekturzustände von einer gewachsenen Legacy-Landschaft zu einer standardisierten, beobachtbaren und zentral abgesicherten Plattformarchitektur. Die Reihenfolge ergibt sich aus Abhängigkeiten: Erst Transparenz und Mindeststandards, dann zentrale Enabler wie IAM, API-Governance und Observability, dann skalierte Migration. Risiken, technische Schulden, Entscheidungsfenster und Rückbaupflichten sind Bestandteil der Roadmap und werden über Governance-Gates geprüft.“

Das ist die Sprache eines Enterprise Architekten, der nicht nur beschreibt, sondern steuert. <>