# Kritische Vertiefung der technischen Leitsätze 1–3

# Leitsatz 1 – Jede technische Entscheidung braucht einen fachlichen Grund

## Kritische Hinterfragung

Wörtlich genommen wäre der Leitsatz zu absolut. Nicht jede Wahl einer internen Library, jedes Refactoring oder jede lokale Implementierungsentscheidung benötigt eine fachliche Nutzenargumentation gegenüber einem Architekturboard. Teams brauchen technische Autonomie, sonst wird Enterprise Architecture zum Engpass.

Architekturrelevant wird eine technische Entscheidung dort, wo sie fachliche Fähigkeiten, gemeinsame Daten, andere Systeme, Security, Datenschutz, Betrieb, Kosten, Lieferfähigkeit, Beschaffung oder spätere Änderbarkeit spürbar beeinflusst. Dann muss der Zusammenhang zwischen technischem Mittel und fachlichem/organisatorischem Ziel erklärbar sein.

## Was „fachlicher Grund“ wirklich bedeutet

Ein fachlicher Grund ist nicht zwangsläufig ein einzelnes Feature. Er kann auch aus Qualität und Risiko entstehen: gesetzliche Fristen einhalten, Nachvollziehbarkeit sicherstellen, Bearbeitungsrückstände vermeiden, Datenintegrität schützen, Wiederanlauf ermöglichen oder eine organisationsweite Fähigkeit standardisieren.

Beispiel: „Wir führen Messaging ein, weil es modern ist“ ist keine belastbare Begründung. „Die Fachbearbeitung darf nicht von der gleichzeitigen Verfügbarkeit des Zielsystems abhängen; Rückmeldungen müssen nachvollziehbar verarbeitet werden“ ist ein nachvollziehbarer Treiber. Daraus kann Messaging eine Option werden – nicht automatisch die Entscheidung.

## EA-Anwendung im Behördenmandat

Als externer EA fragst du nicht „Welche Technologie gefällt uns?“, sondern:

- Welche Fähigkeit oder welcher Verwaltungsprozess wird unterstützt?
- Welcher fachliche Schmerz oder welches Risiko wird adressiert?
- Welche Daten, Schnittstellen und Organisationseinheiten sind betroffen?
- Welche Sicherheits-/Datenschutz-/Betriebsbedingungen gelten?
- Welche Alternativen existieren?
- Welche Folgekosten und Abhängigkeiten entstehen?

Du darfst dennoch technische Verbesserungen zulassen, die primär Engineering-Ziele verfolgen, solange sie innerhalb bestehender Leitplanken bleiben und keine systemischen Auswirkungen erzeugen.

## Gegenbeispiele und Grenze

Ein Team wechselt intern eine kleine Utility-Library ohne Änderung am Vertrag, Betriebsmodell oder Sicherheitsprofil. Dafür ist kein Enterprise-ADR nötig.

Ein Team ersetzt dagegen eine lokale Datenbank durch einen verteilten Datenspeicher und verändert Konsistenz, Backup, Betrieb und Datenhaltung. Auch wenn die Fachfunktion gleich bleibt, ist die Entscheidung architekturrelevant, weil Qualitätsmerkmale und Risiken betroffen sind.

## Typische Fehlanwendungen

- „Fachbereich hat Technologie X verlangt“ wird ungeprüft als fachlicher Grund akzeptiert.
- Ein Architekturtrend wird nachträglich mit Nutzenargumenten versehen.
- Qualitätsanforderungen werden nicht als fachlich relevante Treiber verstanden.
- Lokale Detailentscheidungen werden unnötig zentralisiert.

## Prüfregel

Je größer Blast Radius, Kopplung, Irreversibilität, Datenwirkung, Security-/Datenschutzwirkung, Betriebswirkung oder Kostenbindung, desto stärker muss die Entscheidung fachlich und architektonisch begründet werden.

## Arbeitsformel

**Eine technische Entscheidung ist dann stark, wenn sie einen nachvollziehbaren Bedarf adressiert, Alternativen berücksichtigt und ihre Auswirkungen auf Fachlichkeit, Daten, Betrieb und Risiko sichtbar macht.**

---

# Leitsatz 2 – Eine Architekturentscheidung ist erst vollständig, wenn ihre Konsequenzen benannt sind

## Kritische Hinterfragung

Auch dieser Satz darf nicht in Vollständigkeitsillusion kippen. Niemand kann alle zukünftigen Konsequenzen kennen. Architektur wird unter Unsicherheit entschieden. Das Ziel ist nicht, Zukunft exakt vorherzusagen, sondern die **wesentlichen bekannten und plausiblen Folgepflichten** transparent zu machen.

Ein ADR, das nur „Entscheidung: Kafka“ enthält, dokumentiert keine Architekturentscheidung. Es fehlt, warum entschieden wurde, welche Alternativen betrachtet wurden, welche Annahmen gelten und welche Konsequenzen akzeptiert werden.

## Arten von Konsequenzen

Konsequenzen sind nicht nur Risiken. Sie können positiv, negativ, neutral oder offen sein.

**Fachlich:** neue Bearbeitungslogik, neue Fehler-/Klärfälle, neue Wartezeiten.  
**Daten:** Replikation, Konsistenzmodell, Ownership, Aufbewahrung.  
**Integration:** zusätzliche Verträge, Versionierung, Kopplung.  
**Security:** neue Trust Boundary, technische Identitäten, Secrets.  
**Datenschutz:** neue Verarbeitung, Datenkopien, Löschpflichten.  
**Betrieb:** Monitoring, Runbooks, Skillbedarf, Bereitschaft.  
**Migration:** Parallelbetrieb, Übergangsschnittstellen, Rückbau.  
**Organisation:** neue Owner, Produktverantwortung, Lieferantenabhängigkeit.  
**Kosten:** Plattform-, Lizenz-, Betriebs- und Schulungsaufwand.

## Behördenbeispiel

Entscheidung: Ein Fachverfahren nutzt künftig ein zentrales IAM. Positive Folge: weniger lokale Benutzerverwaltung und bessere Governance. Folgepflichten: Rollenmapping, Joiner/Mover/Leaver, technische Integration, Supportmodell, Audit-Events, Verfügbarkeit des IAM, Migrationsstrategie und Umgang mit Altrollen.

Die Entscheidung kann fachlich richtig sein, obwohl sie neue Abhängigkeiten erzeugt. Genau diese Abhängigkeiten müssen sichtbar sein.

## Reversibilität

Eine sehr reversible Entscheidung benötigt weniger Voranalyse als eine langfristige Plattformentscheidung oder Datenmigration. Deshalb sollte die Entscheidungstiefe proportional zu **Irreversibilität und Blast Radius** sein.

## Annahmen und offene Punkte

Nicht jede Konsequenz muss endgültig gelöst sein. Unbekanntes wird als Annahme oder offener Prüfpunkt dokumentiert. Das ist professioneller als scheinbare Vollständigkeit.

## Typische Fehlanwendungen

- Nur Vorteile werden dokumentiert.
- Risiken werden genannt, aber niemand besitzt Gegenmaßnahmen.
- Konsequenzen werden mit Implementierungsdetails verwechselt.
- Eine Entscheidung wird „vorläufig“ genannt, erzeugt aber faktisch langfristigen Lock-in.
- Folgeentscheidungen werden nicht als solche sichtbar gemacht.

## Reviewfragen

- Welche Folgepflichten entstehen?
- Welche weiteren Entscheidungen werden ausgelöst?
- Welche Teams/Systeme/Daten sind betroffen?
- Welche Abhängigkeit wird neu geschaffen oder verstärkt?
- Was wird schwerer oder teurer?
- Was muss migriert oder später zurückgebaut werden?
- Welche Annahmen müssen validiert werden?
- Wer trägt Umsetzung und Pflege?

## Arbeitsformel

**Eine Architekturentscheidung ist reif, wenn Nutzen, Folgepflichten, Risiken, Abhängigkeiten, Annahmen und offene Prüfpunkte so sichtbar sind, dass die entscheidende Stelle weiß, was sie mit der Entscheidung mitbeschließt.**

---

# Leitsatz 3 – Technische Eleganz ersetzt keine Betriebsfähigkeit

## Kritische Hinterfragung

Der Satz ist richtig, darf aber nicht so verstanden werden, dass der Enterprise Architect zum Betriebsleiter wird. Der EA betreibt das System nicht selbst. Er muss jedoch sicherstellen, dass Betriebsfähigkeit als Qualitätsanforderung früh in Zielbild, Lösungsdesign, Ausschreibung, Review und Abnahme berücksichtigt wird.

Auch „Betriebsfähigkeit“ ist nicht identisch mit „es startet in Produktion“. Zwischen Architekturreife, Umsetzungsreife, Produktionsreife, Abnahmereife und Betriebsübernahme bestehen Unterschiede.

## Was Betriebsfähigkeit umfasst

Eine produktionsfähige Lösung benötigt mindestens klare Ownership, beobachtbares Verhalten, beherrschte Abhängigkeiten, Fehlerbehandlung, Wiederanlauf, Security, Datenschutz, Support, Runbooks und definierte Betriebsübergabe.

Bei kritischen Services kommen fachlich abgeleitete Wiederanlaufziele, Backup/Restore, Notbetrieb, Kapazität, Deployment-/Rollback-Strategie und Incident-/Problem-Einbindung hinzu.

## Backup ist nicht Wiederherstellung

Ein vorhandenes Backup beweist noch nicht, dass ein Dienst wiederhergestellt werden kann. Erst getesteter Restore, dokumentierte Reihenfolge, geklärte Abhängigkeiten, Verantwortlichkeiten und fachliche Nachpflege bilden einen belastbaren Recovery-Nachweis.

## Observability

CPU, RAM und HTTP-Status reichen häufig nicht. Ein System kann technisch „grün“ sein, obwohl tausende Vorgänge fachlich auf eine Rückmeldung warten. Deshalb sollte Observability – soweit sinnvoll – technische und service-/prozessrelevante Signale verbinden.

## Eventbasierte Systeme

Eine eventbasierte Architektur braucht eine explizite Strategie für Zustellung, Wiederholung, Duplikate und Fehlerfälle. Idempotenz, Dead Letter Queue und Replay sind mögliche Mittel, aber nicht pauschal überall Pflicht. Die konkrete Strategie hängt von fachlicher Semantik, Broker, Retention, Fehlerklassen und Betriebsmodell ab.

## Microservices und Plattformen

Microservices sind nicht automatisch besser betreibbar. Sie erhöhen oft verteilte Abhängigkeiten, Observability- und Deployment-Anforderungen. Mindestverträge für Ownership, Security, Logging/Tracing, Deployment und Betrieb sind sinnvoll; die interne Implementierung muss dennoch nicht zentral standardisiert werden.

## RTO und RPO

RTO und RPO sind keine Zahlen, die die IT frei erfindet. Sie müssen aus fachlicher Wirkung und akzeptierbarem Schaden abgeleitet werden. Beim RTO muss zusätzlich klar sein, welcher Zielzustand gemeint ist: Notbetrieb, Teilbetrieb oder vollständiger Normalbetrieb.

## Typische Fehlanwendungen

- „Kubernetes macht die Lösung hochverfügbar.“
- „Wir haben Backups, also sind wir recoverbar.“
- „Prometheus ist installiert, also haben wir Observability.“
- „Es gibt eine DLQ, also ist Fehlerbehandlung gelöst.“
- „Das System wurde deployt, also ist die Betriebsübergabe abgeschlossen.“

## EA-Reviewfragen

- Wer besitzt Dienst und Plattform fachlich/technisch/betrieblich?
- Welche Abhängigkeiten sind kritisch?
- Wie werden Nutzer- und Systemfehler erkannt?
- Welche RTO/RPO gelten und wie wurden sie abgeleitet?
- Wurde Restore/Wiederanlauf getestet?
- Welche Runbooks und Eskalationswege existieren?
- Gibt es Kapazitäts-/Lastannahmen?
- Wie funktioniert Rollback?
- Welche Nachweise werden für Abnahme und Betriebsübergabe verlangt?

## Arbeitsformel

**Als Enterprise Architect betreibe ich das System nicht selbst. Ich stelle sicher, dass Betriebsfähigkeit als Architektur- und Qualitätsanforderung früh definiert, im Lösungsdesign berücksichtigt und vor Produktionsfreigabe prüfbar nachgewiesen wird.**
