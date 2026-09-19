## Checkliste: Welche Fragen du in welchem Architekturkontext stellen musst

1. Frage nie „wild“, sondern immer passend zur Phase: Mandat, Ist, Soll, Gap, Entscheidung, Umsetzung, Abnahme.  
2. Beginne in frühen Gesprächen offen, später immer konkreter und prüfbarer.  
3. Stelle zuerst Kontextfragen, bevor du Lösungsfragen stellst.  
4. Frage nach fachlicher Wirkung, bevor du technische Architektur bewertest.  
5. Frage nach Verantwortung, bevor du Schnittstellen und Betrieb bewertest.  
6. Frage nach Datenflüssen, bevor du Security, Datenschutz und IAM beurteilst.  
7. Frage nach Betriebsfähigkeit, bevor du ein System als „fertig“ akzeptierst.  
8. Frage nach Nachweisen, bevor du Aussagen von Dienstleistern als erfüllt betrachtest.  
9. Frage nach Abweichungen, bevor du Architekturkonformität annimmst.  
10. Frage nach Entscheidungen, Optionen und Konsequenzen, bevor du Empfehlungen gibst.  
11. Frage je Rolle unterschiedlich: Management braucht Entscheidungsfragen, Betrieb braucht Handlungsfragen, Dienstleister braucht Lieferfragen.  
12. Beende jedes Architekturgespräch mit offenen Punkten, Entscheidungsbedarf, Verantwortlichen und nächstem Artefakt.  

<>

## Der Grundsatz: Architekturfragen sind keine Neugierfragen, sondern Steuerungsinstrumente

Emil, die wichtigste Korrektur ist diese: Ein Enterprise Architekt stellt Fragen nicht, um „mehr zu wissen“. Er stellt Fragen, um Komplexität entscheidbar, lieferbar, prüfbar und steuerbar zu machen. Eine gute Frage verändert den Raum. Sie bringt eine Annahme ans Licht, macht eine Abhängigkeit sichtbar, deckt einen Zielkonflikt auf oder erzwingt einen Nachweis.

Schlechte Architekturfragen sind zu früh zu technisch. Zum Beispiel: „Welche Datenbank nutzt ihr?“ Das kann wichtig sein, aber oft ist es zu früh. Besser ist zuerst: „Welche fachlichen Datenobjekte entstehen, wer verantwortet sie, wie lange werden sie benötigt, wo werden sie weitergegeben, und welche Folgen hätte Datenverlust?“ Erst danach wird die Datenbankfrage sinnvoll.

Der Kontext entscheidet also über die Frage. In der Mandatsklärung fragst du nach Verantwortung. In der Fachanalyse fragst du nach Fähigkeiten und Prozessen. In der Ist-Analyse fragst du nach Systemen, Schnittstellen und Schmerzpunkten. In der Zielarchitektur fragst du nach Prinzipien und Zielzustand. In Security fragst du nach Schutzbedarf, Zugriffen und Nachweisen. In Betrieb fragst du nach Monitoring, Wiederanlauf und Runbooks. In Ausschreibung fragst du nach Liefergegenständen. In Abnahme fragst du nach Prüfkriterien.

## Die Architektur-Fragelogik: Vom Unklaren zum Prüfbaren

Du brauchst einen inneren Fragetrichter. Am Anfang ist der Raum unscharf. Dort stellst du offene Orientierungsfragen. Danach strukturierst du. Dann prüfst du Annahmen. Dann führst du zu Entscheidungen. Am Ende verlangst du Nachweise.

| Aspekt | Details/Erklärung | Beispiel | Ergebnis |
|---|---|---|---|
| Orientierungsfragen | Diese Fragen klären, worum es überhaupt geht. Sie sind offen und breit. | „Welches fachliche Problem soll gelöst werden?“ | Gemeinsames Problemverständnis. |
| Kontextfragen | Diese Fragen klären Systemgrenzen, Rollen, Abhängigkeiten und Umfeld. | „Welche Systeme, Organisationseinheiten und externen Stellen sind betroffen?“ | System- und Stakeholderkontext. |
| Strukturfragen | Diese Fragen zerlegen Komplexität in Fähigkeiten, Prozesse, Daten, Anwendungen und Schnittstellen. | „Welche fachlichen Fähigkeiten werden unterstützt?“ | Architekturstruktur. |
| Prüfungsfragen | Diese Fragen testen Qualität, Risiken, Annahmen und Lücken. | „Woran erkennen wir, dass die Schnittstelle vollständig spezifiziert ist?“ | Reviewfähigkeit. |
| Entscheidungsfragen | Diese Fragen führen zu Optionen, Trade-offs und Beschlüssen. | „Welche Option ist unter Betrieb, Sicherheit, Kosten und Zeit am tragfähigsten?“ | Entscheidungsgrundlage. |
| Nachweisfragen | Diese Fragen machen Aussagen prüfbar. | „Welches Artefakt belegt die Erfüllung?“ | Liefergegenstand und Abnahme. |

## Kontext 1: Mandatsklärung

In der Mandatsklärung geht es nicht um Technik. Es geht darum, ob du überhaupt wirksam handeln kannst. Hier fragst du nach Rolle, Verantwortung, Entscheidungsrechten, Reviewrechten, Eskalationswegen und Erwartungen. Wenn du diesen Kontext überspringst, arbeitest du später fachlich sauber, aber organisatorisch wirkungslos.

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Auftrag | Du klärst, wofür du konkret gebraucht wirst. | „Welches Ergebnis erwarten Sie von der Enterprise Architecture in diesem Vorhaben?“ „Geht es um Zielbild, Review, Roadmap, Dienstleistersteuerung, Abnahme oder alles davon?“ | Mandat sichtbar machen. |
| Entscheidungsrechte | Du klärst, was du entscheiden darfst und was du vorbereitest. | „Welche Architekturentscheidungen darf ich freigeben?“ „Welche Entscheidungen müssen ins Architekturboard oder in die Lenkung?“ | Rollenkonflikte vermeiden. |
| Reviewrechte | Du klärst, wann du eingebunden wirst. | „Bei welchen Liefergegenständen ist ein Architekturreview verpflichtend?“ „Darf Implementierung vor Review beginnen?“ | Späte Schadensbegrenzung verhindern. |
| Eskalation | Du klärst, was bei Abweichungen passiert. | „Wie gehen wir mit Abweichungen von Architekturvorgaben um?“ „Wer entscheidet über Ausnahmen?“ | Governance belastbar machen. |
| Erfolgskriterien | Du klärst, woran deine Arbeit gemessen wird. | „Woran erkennen wir nach drei Monaten, dass Architekturarbeit geholfen hat?“ | Wirkung statt Aktivität messen. |

Deine Leitfrage in diesem Kontext lautet: „Welches Mandat brauche ich, damit Architekturqualität nicht nur empfohlen, sondern im Vorhaben wirksam gesteuert werden kann?“

## Kontext 2: Management- und Zielklärung

Mit Management sprichst du nicht zuerst über Komponenten, Frameworks oder Schnittstellenformate. Du fragst nach Ziel, Risiko, Entscheidungsbedarf, Prioritäten und Erfolg. Managementfragen müssen knapp, entscheidungsorientiert und risikobewusst sein.

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Strategisches Ziel | Du klärst, warum das Vorhaben relevant ist. | „Welche fachliche oder organisatorische Fähigkeit soll durch das Vorhaben verbessert werden?“ | Zielrichtung verstehen. |
| Prioritäten | Du klärst Zielkonflikte. | „Was ist wichtiger: schnelle Umsetzung, Standardisierung, geringe Betriebskosten, Integrationsfähigkeit oder Risikoreduktion?“ | Trade-offs sichtbar machen. |
| Entscheidung | Du klärst, welche Entscheidung wirklich ansteht. | „Welche Entscheidung muss in diesem Gremium heute vorbereitet oder getroffen werden?“ | Meeting auf Entscheidung ausrichten. |
| Risiko | Du klärst Risikotoleranz. | „Welche Risiken dürfen wir bewusst eingehen, und welche sind nicht akzeptabel?“ | Architektur nicht im luftleeren Raum bewerten. |
| Erfolg | Du klärst messbare Wirkung. | „Woran erkennen Fachseite und Leitung nach Produktivsetzung, dass das Vorhaben erfolgreich war?“ | Erfolgskriterien definieren. |

Ein starker Managementsatz lautet: „Ich brauche von Ihnen keine technische Detailentscheidung, sondern eine Priorisierung der Zielkonflikte. Danach kann Architektur die tragfähigen Optionen ausarbeiten.“

## Kontext 3: Fachseite und Geschäftsarchitektur

Mit der Fachseite fragst du nicht: „Welche Software möchten Sie?“ Du fragst: „Welche fachliche Fähigkeit muss besser werden?“ Die Fachseite beschreibt häufig Symptome: langsam, unübersichtlich, Medienbruch, zu viele Rückfragen, schlechte Datenqualität. Deine Aufgabe ist, daraus Fähigkeiten, Prozesse, Fachobjekte und Regeln herauszuarbeiten.

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Fachlicher Zweck | Du klärst den Nutzen. | „Welches fachliche Problem soll gelöst werden?“ „Was funktioniert heute nicht ausreichend?“ | Problem statt Lösung verstehen. |
| Fähigkeiten | Du identifizierst organisatorische Capabilities. | „Welche Fähigkeiten braucht die Organisation dafür?“ „Welche davon sind heute schwach unterstützt?“ | Capability Map aufbauen. |
| Prozesse | Du klärst Ablauf, Entscheidungen und Ausnahmen. | „Welche Schritte durchläuft ein Antrag von Eingang bis Abschluss?“ „Wo entstehen Rückfragen, Wartezeiten oder Medienbrüche?“ | Prozesslandkarte erstellen. |
| Fachobjekte | Du identifizierst zentrale Informationsobjekte. | „Welche fachlichen Objekte sind zentral: Antrag, Person, Nachweis, Bescheid, Akte, Frist?“ | Datenarchitektur vorbereiten. |
| Regeln | Du klärst fachliche Logik. | „Welche Regeln entscheiden, ob ein Antrag vollständig, gültig oder entscheidungsreif ist?“ | Anforderungen und Datenmodell schärfen. |
| Ausnahmen | Du findest reale Komplexität. | „Welche Sonderfälle kommen häufig vor?“ „Welche Fälle sprengen den Standardprozess?“ | Architektur nicht nur für Idealfall bauen. |

Die wichtigste Korrektur hier lautet: Die Fachseite liefert nicht automatisch Anforderungen. Sie liefert fachliche Wirklichkeit. Anforderungen entstehen erst, wenn diese Wirklichkeit strukturiert, geprüft und übersetzt wurde.

## Kontext 4: Ist-Architektur

In der Ist-Analyse fragst du nach Realität, nicht nach Wunschbildern. Du willst verstehen, welche Systeme existieren, welche Schnittstellen wirklich genutzt werden, wo manuelle Workarounds bestehen, welche Daten wo liegen, welche Abhängigkeiten kritisch sind und welche technischen Schulden bereits bekannt sind.

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Systemlandschaft | Du identifizierst relevante Anwendungen. | „Welche Systeme sind am Prozess beteiligt?“ „Welche Systeme sind führend für welche Daten?“ | Anwendungslandkarte. |
| Schnittstellen | Du findest technische und organisatorische Kopplungen. | „Welche Schnittstellen existieren wirklich?“ „Sind sie dokumentiert, versioniert und überwacht?“ | Schnittstellenkatalog. |
| Datenhaltung | Du klärst Datenquellen und Redundanzen. | „Wo entstehen die Daten zuerst?“ „Wo werden sie kopiert, verändert oder archiviert?“ | Datenflussbild. |
| Betrieb | Du erkennst Betriebsrealität. | „Wer betreibt welches System?“ „Welche Störungen treten regelmäßig auf?“ | Betriebsfähigkeitsraster. |
| Schmerzpunkte | Du trennst Symptome von Ursachen. | „Wo entsteht die meiste Nacharbeit?“ „Was wird manuell korrigiert?“ | Verbesserungshebel. |
| Dokumentation | Du prüfst vorhandene Nachweise. | „Welche Architektur-, Betriebs- und Schnittstellendokumentation ist aktuell?“ | Dokumentationslücken. |

In diesem Kontext ist deine wichtigste Frage: „Was ist dokumentiert, was ist gelebte Realität, und wo weichen beide voneinander ab?“

## Kontext 5: Zielarchitektur

In der Zielarchitektur fragst du nach Richtung, Prinzipien, Zielzustand, Standards, bewusst akzeptierten Übergängen und Nicht-Zielen. Zielarchitektur ist kein Wunschkonzert. Sie ist ein begründeter Ordnungszustand.

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Zielzustand | Du klärst, wie die Landschaft künftig funktionieren soll. | „Wie soll der Zielzustand in zwei bis drei Jahren aussehen?“ | Zielbild. |
| Prinzipien | Du klärst Leitplanken. | „Welche Prinzipien gelten verbindlich: API-first, zentrales IAM, Plattform vor Sonderlösung, Observability by Design?“ | Architekturprinzipien. |
| Standards | Du klärst verbindliche Vorgaben. | „Welche Standards sind für Schnittstellen, Security, Dokumentation, Betrieb und Datenmodelle einzuhalten?“ | Standardkatalog. |
| Nicht-Ziele | Du begrenzt den Scope. | „Was soll ausdrücklich nicht Teil dieses Zielbildes sein?“ | Scope-Klarheit. |
| Übergang | Du verhinderst Big-Bang-Denken. | „Welche Zwischenzustände sind realistisch und akzeptabel?“ | Transition Architecture. |
| Abweichungen | Du machst Zielkonflikte sichtbar. | „Welche bestehenden Systeme können die Zielarchitektur noch nicht erfüllen?“ | Gap-Liste und ADRs. |

Die wichtigste Zielarchitekturfrage lautet: „Welcher Zielzustand ist fachlich sinnvoll, technisch tragfähig, sicher, betreibbar, beschaffbar und schrittweise erreichbar?“

## Kontext 6: Schnittstellen und Integration

Bei Schnittstellen musst du sehr genau fragen. Schlechte Schnittstellen sind eine der häufigsten Ursachen für spätere Integrationsprobleme. Du fragst nicht nur nach Protokoll und Format, sondern nach fachlichem Zweck, Datenvertrag, Konsumenten, Fehlerverhalten, Security, Versionierung, Monitoring und Betrieb.

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Zweck | Jede Schnittstelle braucht einen fachlichen Grund. | „Welchen fachlichen Vorgang unterstützt diese Schnittstelle?“ | Schnittstelle nicht als Selbstzweck. |
| Provider und Consumer | Du klärst Verantwortung. | „Wer stellt die Schnittstelle bereit?“ „Wer nutzt sie?“ „Wer wird bei Änderungen informiert?“ | Verantwortlichkeit. |
| Datenvertrag | Du klärst fachliche und technische Daten. | „Welche Fachobjekte werden übertragen?“ „Welche Pflichtfelder, Formate und Validierungsregeln gelten?“ | API-/Datenmodell. |
| Authentifizierung und Autorisierung | Du klärst Zugriff. | „Wie authentifiziert sich der Consumer?“ „Welche Berechtigungen werden geprüft?“ | Security-Anschluss. |
| Fehlerverhalten | Du vermeidest Integrationsblindheit. | „Welche fachlichen und technischen Fehlercodes gibt es?“ „Wie erkennt der Consumer temporäre Fehler?“ | Fehlervertrag. |
| Versionierung | Du klärst Änderbarkeit. | „Wie werden Breaking Changes behandelt?“ „Wie lange werden alte Versionen unterstützt?“ | Lebenszyklusfähigkeit. |
| Monitoring | Du klärst Betriebssicht. | „Welche Metriken, Logs und Korrelations-IDs sind erforderlich?“ | Observability. |
| Spezifikation | Du verlangst Nachweis. | „Liegt eine OpenAPI-Spezifikation vor?“ „Ist sie validiert, versioniert und abgestimmt?“ | Prüfbarkeit. |

Die zentrale Frage lautet: „Kann ein Konsument diese Schnittstelle ohne informelle Zusatzabsprachen korrekt nutzen, Fehler behandeln und betreiben?“

## Kontext 7: Datenarchitektur

Datenfragen sind Architekturfragen. In Behörden sind Daten oft fachlich, rechtlich, historisch und organisatorisch relevant. Du fragst deshalb nicht nur: „Welche Tabellen gibt es?“ Du fragst nach Fachobjekten, Datenverantwortung, Datenherkunft, Qualität, Lebenszyklus, Speicherung, Archivierung und Weitergabe.

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Fachobjekte | Du klärst zentrale Datenbegriffe. | „Welche fachlichen Objekte sind entscheidend?“ | Fachliches Datenmodell. |
| Datenquelle | Du findest führende Systeme. | „Wo entsteht dieses Datum erstmalig?“ „Welches System ist führend?“ | Mastership klären. |
| Datenqualität | Du erkennst Risiken. | „Welche Datenfehler treten häufig auf?“ „Welche Folgen haben falsche oder fehlende Daten?“ | Qualitätsanforderungen. |
| Lebenszyklus | Du klärst Zustände. | „Welche Zustände durchläuft ein Antrag?“ „Wann wird ein Vorgang abgeschlossen oder archiviert?“ | Lebenszyklusmodell. |
| Weitergabe | Du machst Datenflüsse sichtbar. | „An welche Systeme oder Stellen werden Daten weitergegeben?“ | Datenflussdiagramm. |
| Löschung und Archivierung | Du klärst Aufbewahrung. | „Wann werden Daten gelöscht, gesperrt oder archiviert?“ | Betriebs- und Compliance-Anschluss. |
| Semantik | Du vermeidest Begriffschaos. | „Bedeutet ‚Antragsteller‘ in allen Systemen dasselbe?“ | Datenverständnis harmonisieren. |

Die wichtigste Datenfrage lautet: „Wer verantwortet welches fachliche Datum über welchen Lebenszyklus hinweg?“

## Kontext 8: Security Architecture

Security-Fragen stellst du nicht erst am Ende. Du stellst sie, sobald Datenflüsse, Rollen, Schnittstellen und Betriebsmodell erkennbar sind. Entscheidend ist: Du fragst nicht nur nach Maßnahmen, sondern nach Schutzbedarf, Bedrohungen, Zugriffen, Nachweisen und RestRisiken.

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Schutzbedarf | Du klärst Kritikalität. | „Welche Informationen, Prozesse und Systeme sind besonders schutzbedürftig?“ | Risikobasis. |
| Bedrohungen | Du denkst in Angriffen und Fehlbedienung. | „Was wäre der schwerwiegendste realistische Missbrauchsfall?“ | Bedrohungsmodell. |
| Zugriff | Du prüfst Berechtigungen. | „Wer darf welche Daten lesen, ändern, exportieren oder löschen?“ | Rollen- und Rechtekonzept. |
| Technische Identitäten | Du prüfst Maschinenzugriffe. | „Welche Service-Accounts, Clients oder technischen Identitäten existieren?“ | IAM-Tiefe. |
| Protokollierung | Du klärst Nachvollziehbarkeit. | „Welche sicherheitsrelevanten Aktionen müssen protokolliert werden?“ | Auditfähigkeit. |
| Schwachstellen | Du prüfst Lieferprozess. | „Welche Security-Scans, Reviews und Befundprozesse gibt es?“ | Secure Delivery. |
| Freigabe | Du klärst Akzeptanz. | „Wer akzeptiert verbleibende Risiken und auf welcher Grundlage?“ | Entscheidung statt Schwebezustand. |

Die wichtigste Security-Frage lautet: „Welche Sicherheitsannahmen liegen der Architektur zugrunde, und wodurch werden sie nachweisbar erfüllt?“

## Kontext 9: IAM, Rollen und Rechte

IAM ist nicht nur Login. IAM ist die Architektur von Identität, Rollen, Rechten, technischen Clients, Token-Flows, Berechtigungsprüfung und Entzug. Hier musst du besonders präzise fragen, weil unklare Berechtigungen später zu Sicherheits- und Betriebsproblemen führen.

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Identitäten | Du klärst, wer oder was sich authentifiziert. | „Welche menschlichen Nutzer und technischen Clients gibt es?“ | Identitätsmodell. |
| Rollen | Du klärst fachliche Rollen. | „Welche Rollen gibt es fachlich und welche technisch?“ | Rollenmodell. |
| Rechte | Du klärst konkrete Berechtigungen. | „Welche Rolle darf welche Aktion auf welchem Objekt ausführen?“ | Berechtigungsmatrix. |
| Token-Flows | Du klärst technische Umsetzung. | „Welche Token werden genutzt, wer stellt sie aus, wer validiert sie?“ | IAM-Architektur. |
| Entzug | Du klärst Lebenszyklus. | „Wie werden Rechte entzogen, wenn jemand Rolle oder Organisationseinheit wechselt?“ | Governance. |
| Administration | Du klärst privilegierte Zugriffe. | „Wer darf Rollen vergeben und wie wird das protokolliert?“ | Kontrollfähigkeit. |
| Tests | Du prüfst Negativfälle. | „Welche unberechtigten Zugriffe werden explizit getestet?“ | Abnahmefähigkeit. |

Die zentrale IAM-Frage lautet: „Ist für jede Identität klar, welche Berechtigung sie warum hat, wie sie technisch durchgesetzt und wie sie überprüft wird?“

## Kontext 10: Observability und Betrieb

Betriebsfragen sind Architekturfragen. Wenn ein System im Fehlerfall nicht beobachtbar ist, ist es nicht reif. Du fragst hier nach Logs, Metriken, Traces, SLOs, Alerts, Runbooks, Eskalationen und Verantwortlichkeiten.

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Sichtbarkeit | Du klärst, ob Fehler erkennbar sind. | „Woran erkennt der Betrieb, dass ein Antrag in der Verarbeitungskette hängen bleibt?“ | Monitoringbedarf. |
| Logs | Du klärst Ereignisnachweise. | „Welche fachlichen und technischen Ereignisse werden protokolliert?“ | Diagnosefähigkeit. |
| Metriken | Du klärst Messpunkte. | „Welche Metriken zeigen Zustand, Last, Fehler und Latenz?“ | Betriebssteuerung. |
| Traces | Du klärst systemübergreifende Nachverfolgung. | „Gibt es eine durchgängige Korrelations-ID über Portal, API-Gateway, Fachverfahren, Register und DMS?“ | End-to-End-Sicht. |
| Alerts | Du vermeidest Dashboard-Illusion. | „Welche Zustände lösen aktiv einen Alarm aus?“ | Reaktionsfähigkeit. |
| Runbooks | Du prüfst Handlungsfähigkeit. | „Was macht der Betrieb konkret bei Registerausfall, Datenbankfehler oder Queue-Rückstau?“ | Betriebsübergabe. |
| Verantwortung | Du klärst Zuständigkeit. | „Wer reagiert auf welchen Alarm, in welcher Zeit, mit welcher Eskalation?“ | Betriebsklarheit. |

Die wichtigste Betriebsfrage lautet: „Kann der Betrieb einen Fehler erkennen, eingrenzen, bewerten und behandeln, ohne erst den Entwickler anzurufen?“

## Kontext 11: Resilienz, RTO/RPO und Notbetrieb

Hier fragst du nach Ausfall, Wiederanlauf, Datenverlust und fachlicher Kritikalität. Viele Teams sagen „hochverfügbar“, ohne zu wissen, welche fachliche Wiederherstellungszeit wirklich benötigt wird. Deine Aufgabe ist, Fachlichkeit und Technik zusammenzubringen.

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Kritikalität | Du klärst fachliche Bedeutung. | „Welche Prozesse dürfen wie lange ausfallen?“ | Kritikalitätsmatrix. |
| RTO | Du klärst Wiederherstellungszeit. | „Nach welcher Zeit muss die Funktion wieder verfügbar sein?“ | Wiederanlaufziel. |
| RPO | Du klärst tolerierbaren Datenverlust. | „Wie viele Daten dürfen maximal verloren gehen?“ | Backup-/Restore-Anforderung. |
| Notbetrieb | Du prüfst Alternativen. | „Wie arbeitet die Fachseite weiter, wenn das System ausfällt?“ | Fallback-Konzept. |
| Restore | Du prüfst echte Wiederherstellung. | „Wann wurde Restore zuletzt getestet?“ | Nachweis statt Annahme. |
| Abhängigkeiten | Du erkennst Kettenrisiken. | „Welche Systeme müssen gleichzeitig verfügbar sein, damit der Prozess funktioniert?“ | Resilienzbild. |
| Wartung | Du klärst geplante Nichtverfügbarkeit. | „Welche Wartungsfenster sind fachlich akzeptabel?“ | Betriebsplanung. |

Die zentrale Resilienzfrage lautet: „Welche fachliche Wirkung hat ein technischer Ausfall, und welche Wiederherstellung ist deshalb wirklich erforderlich?“

## Kontext 12: Roadmap und Transformation

In der Roadmap fragst du nach Reihenfolge, Abhängigkeiten, Zwischenzuständen, Risiken und Entscheidungsfenstern. Eine Architekturroadmap ist kein Terminplan. Sie ist ein Veränderungspfad mit Architekturabhängigkeiten.

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Zielzustand | Du klärst Richtung. | „Welche Zielarchitektur soll erreicht werden?“ | Zielbildanker. |
| Ist-Zustand | Du klärst Ausgangslage. | „Welche Legacy-Abhängigkeiten begrenzen uns?“ | Realitätsbasis. |
| Gaps | Du identifizierst Lücken. | „Was fehlt zwischen Ist und Soll?“ | Gap-Liste. |
| Abhängigkeiten | Du erkennst Reihenfolgezwänge. | „Was muss vor API-Standardisierung, IAM-Anbindung oder Plattformmigration passieren?“ | Roadmaplogik. |
| Transition | Du definierst Zwischenzustände. | „Welche Übergangsarchitektur ist für sechs bis zwölf Monate akzeptabel?“ | Realistische Migration. |
| Quick Wins | Du findest frühe Wirkung. | „Welche Maßnahme reduziert Risiko früh, ohne das Zielbild zu verletzen?“ | Momentum. |
| Risiken | Du machst Roadmap-Risiken sichtbar. | „Welche Entscheidung blockiert mehrere Arbeitspakete?“ | Risikosteuerung. |

Die wichtigste Roadmapfrage lautet: „Welche Reihenfolge reduziert Risiko, schafft Nutzen und bringt uns trotzdem sichtbar näher an die Zielarchitektur?“

## Kontext 13: Governance und Architekturboard

Governance-Fragen sind Fragen nach Entscheidungssystem, nicht nach Kontrolle um der Kontrolle willen. Du fragst: Was muss entschieden werden? Wer entscheidet? Nach welchen Kriterien? Wie werden Ausnahmen dokumentiert? Wie wird Maßnahmenverfolgung sichergestellt?

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Entscheidungsbedarf | Du vermeidest Gremienleerlauf. | „Welche Architekturentscheidung braucht dieses Board wirklich?“ | Fokus. |
| Kriterien | Du klärst Bewertungsmaßstab. | „Nach welchen Prinzipien und Standards wird bewertet?“ | Konsistenz. |
| Rollen | Du klärst Beteiligung. | „Welche Rollen müssen bei dieser Entscheidung beteiligt sein?“ | Legitimation. |
| ADRs | Du sicherst Nachvollziehbarkeit. | „Ist die Entscheidung als ADR dokumentiert?“ | Entscheidungshistorie. |
| Ausnahmen | Du steuerst Abweichungen. | „Welche Vorgabe wird verletzt, warum, wie lange und mit welchem Risiko?“ | Ausnahmeprozess. |
| Maßnahmen | Du verhinderst Protokollfriedhöfe. | „Welche Maßnahme entsteht, wer verantwortet sie, bis wann?“ | Umsetzung. |
| Wirkung | Du prüfst Governance-Nutzen. | „Welche Nacharbeit wurde durch dieses Review vermieden?“ | Akzeptanz. |

Die zentrale Governancefrage lautet: „Welche Architekturentscheidung muss hier nachvollziehbar getroffen oder vorbereitet werden?“

## Kontext 14: Ausschreibung und Leistungsbeschreibung

In der Ausschreibung fragst du nach Steuerbarkeit. Du musst Architekturqualität in Anforderungen, Liefergegenstände und Nachweise übersetzen. Hier sind Fragen besonders konkret.

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Mindestanforderung | Du klärst, was zwingend ist. | „Welche Architekturvorgabe ist nicht verhandelbar?“ | Muss-Kriterien. |
| Liefergegenstand | Du machst Qualität sichtbar. | „Welches Artefakt muss der Auftragnehmer liefern?“ | Prüfbarkeit. |
| Nachweis | Du verlangst Belege. | „Wie belegt der Auftragnehmer die Erfüllung?“ | Evidenz. |
| Zeitpunkt | Du verhinderst späte Lieferung. | „Wann muss das Artefakt vorliegen: vor Implementierung, vor Test, vor Go-live?“ | Steuerung. |
| Bewertung | Du differenzierst Qualität. | „Welche Qualität wird höher bewertet als das Minimum?“ | Zuschlagskriterien. |
| Abweichung | Du regelst Sonderfälle. | „Wie werden Abweichungen von Architekturvorgaben beantragt und freigegeben?“ | Vertragsklarheit. |
| Abnahme | Du definierst Erfüllung. | „Woran erkennen wir objektiv, dass die Leistung akzeptiert wird?“ | Abnahmekriterien. |

Die wichtigste Ausschreibungsfrage lautet: „Welche Architekturqualität muss der Dienstleister liefern, und durch welches Artefakt wird sie prüfbar?“

## Kontext 15: Dienstleistersteuerung

Mit Dienstleistern fragst du nicht nur nach Status. Statusfragen erzeugen oft beruhigende Antworten. Du brauchst Liefer-, Nachweis-, Risiko- und Entscheidungsfragen.

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Lieferstand | Du fragst nach Artefakten, nicht nur Fortschritt. | „Welche Architekturartefakte wurden geliefert, reviewed und freigegeben?“ | Objektiver Stand. |
| Abweichungen | Du erkennst Zielbildverletzungen. | „Welche Architekturvorgaben können nicht eingehalten werden?“ | Frühe Korrektur. |
| Risiken | Du holst Probleme nach vorne. | „Welche Architekturentscheidung blockiert aktuell Umsetzung oder Test?“ | Risikosicht. |
| Nachweise | Du prüfst Behauptungen. | „Wo ist der Test-, Scan-, Review- oder Validierungsnachweis?“ | Evidenz. |
| Schnittstellen | Du vermeidest Integrationsüberraschungen. | „Welche Konsumenten haben die Spezifikation freigegeben?“ | Integrationssicherheit. |
| Betrieb | Du erzwingst Übergabefähigkeit. | „Welche Runbooks, Dashboards und Alarmregeln sind bereits vorhanden?“ | Betriebsreife. |
| Entscheidung | Du klärst Eskalationen. | „Welche Entscheidung braucht der Auftragnehmer vom Auftraggeber?“ | Blockaden lösen. |

Die zentrale Dienstleisterfrage lautet: „Was wurde konkret geliefert, wodurch ist es nachgewiesen, und welche offene Entscheidung verhindert die nächste Lieferfähigkeit?“

## Kontext 16: Abnahme

In der Abnahme fragst du nicht: „Funktioniert es?“ Das ist nur ein Teil. Du fragst: „Ist es fachlich korrekt, sicher, betreibbar, dokumentiert, getestet, integriert und übergabefähig?“ Abnahme ist der Kontext der Nachweise.

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Funktionsfähigkeit | Du prüfst fachliche Wirkung. | „Sind die vereinbarten fachlichen Szenarien erfolgreich durchlaufen?“ | Fachabnahme. |
| Architekturkonformität | Du prüfst Zielbild und Standards. | „Welche Architekturvorgaben sind erfüllt, welche abweichend?“ | Architekturabnahme. |
| Schnittstellen | Du prüfst Integration. | „Sind alle Schnittstellen spezifiziert, getestet und überwacht?“ | Integrationsabnahme. |
| Security | Du prüfst Sicherheitsnachweise. | „Sind kritische Befunde geschlossen oder formal akzeptiert?“ | Sicherheitsfreigabe. |
| Betrieb | Du prüfst Übergabefähigkeit. | „Kann der Betrieb das System anhand der Unterlagen betreiben?“ | Betriebsabnahme. |
| Dokumentation | Du prüfst Aktualität. | „Ist die Dokumentation releasebezogen, versioniert und vollständig?“ | Wissenssicherung. |
| Offene Punkte | Du klassifizierst Restmängel. | „Welche offenen Punkte sind abnahmeverhindernd, welche auflagenfähig?“ | Entscheidungsvorlage. |

Die wichtigste Abnahmefrage lautet: „Welche objektiven Nachweise zeigen, dass die Lieferung nicht nur funktioniert, sondern dauerhaft betreibbar, sicher und architekturkonform ist?“

## Kontext 17: Wissensübergabe

Wissensübergabe wird oft unterschätzt. Sie ist aber entscheidend, wenn eine Behörde nicht dauerhaft vom Dienstleister abhängig sein will. Hier fragst du nach Dokumentation, Schulung, Betriebsdurchläufen, Entscheidungswissen und Fähigkeitstransfer.

| Aspekt | Details/Erklärung | Beispielhafte Fragen | Ziel der Fragen |
|---|---|---|---|
| Zielgruppen | Du klärst, wer Wissen braucht. | „Wer muss was wissen: Fachseite, Betrieb, Entwicklung, Architektur, Support?“ | Trainingsplanung. |
| Inhalte | Du klärst notwendiges Wissen. | „Welche Architekturentscheidungen, Betriebsabläufe und Schnittstellen müssen verstanden werden?“ | Wissensumfang. |
| Form | Du klärst Vermittlung. | „Gibt es Schulung, Aufzeichnung, Handbuch, Workshop, Pairing oder Betriebsübung?“ | Transferformat. |
| Nachweis | Du prüfst Durchführung. | „Wurde Wissenstransfer dokumentiert und verstanden?“ | Übergabenachweis. |
| Nachhaltigkeit | Du reduzierst Abhängigkeit. | „Kann die Behörde Änderungen später selbst bewerten oder betreiben?“ | Souveränität. |
| Entscheidungswissen | Du sicherst Gründe. | „Sind wichtige Architekturentscheidungen als ADR dokumentiert?“ | Gedächtnisfähigkeit. |
| Supportfähigkeit | Du prüfst Alltagstauglichkeit. | „Kann der First-/Second-Level typische Fehlerbilder erkennen?“ | Betriebsfähigkeit. |

Die zentrale Frage lautet: „Welches Wissen muss beim Auftraggeber verbleiben, damit das System nicht nur übernommen, sondern verstanden und gesteuert werden kann?“

## Die wichtigsten Fragen nach Rolle

Nicht jede Rolle beantwortet dieselben Fragen. Du musst wissen, wen du was fragst. Sonst erzeugst du Frust oder bekommst falsche Antworten.

| Rolle | Details/Erklärung | Gute Fragen | Nicht geeignete Fragen |
|---|---|---|---|
| Management | Entscheidet Prioritäten, Risiken, Budget, Richtung. | „Welche Zielkonflikte sollen wir priorisieren?“ „Welche Risiken sind nicht akzeptabel?“ | Tiefe API-Details oder konkrete Klassenmodelle. |
| Fachseite | Kennt Prozesse, Regeln, Ausnahmen, fachliche Wirkung. | „Welche Fälle kommen häufig vor?“ „Wo entsteht Nacharbeit?“ | Technische Produktentscheidungen. |
| Projektleitung | Kennt Termine, Abhängigkeiten, Lieferplanung. | „Welche Architekturentscheidung gefährdet den Meilenstein?“ | Fachliche Detailregeln ohne Fachseite. |
| Betrieb | Kennt Stabilität, Monitoring, Incident, Restore, Übergabe. | „Wie erkennen und behandeln Sie diesen Fehlerfall?“ | Fachliche Priorisierung ohne Kontext. |
| Informationssicherheit | Prüft Risiken, Schutzbedarf, Maßnahmen, Freigaben. | „Welche Sicherheitsnachweise sind abnahmeerforderlich?“ | Reine Projektstatusfragen. |
| Datenschutz | Prüft Datenflüsse, Zwecke, Rollen, Aufbewahrung, Rechte. | „Welche personenbezogenen Daten fließen wohin und warum?“ | Infrastrukturdetails ohne Datenbezug. |
| Vergabe/Einkauf | Prüft Beschaffbarkeit, Leistungsbeschreibung, Bewertung, Vertrag. | „Wie formulieren wir diese Architekturqualität vergabefähig?“ | Architekturentscheidung ohne Leistungsbezug. |
| Dienstleister | Liefert Lösung, Artefakte, Nachweise, Risiken. | „Welches Artefakt belegt die Erfüllung?“ „Welche Abweichung sehen Sie?“ | Unklare Wunschfragen ohne Liefergegenstand. |
| Entwicklung | Kennt technische Umsetzung, Code, Build, Tests. | „Welche Architekturentscheidung beeinflusst Implementierung und Wartbarkeit?“ | Politische oder budgetäre Fragen. |
| Enterprise Architekt | Integriert Perspektiven und macht Entscheidungen belastbar. | „Welche Entscheidung ist nötig, wer muss sie treffen, und welche Nachweise brauchen wir?“ | Reine Detailkontrolle ohne Architekturwirkung. |

## Der wichtigste praktische Gesprächsablauf

In einem echten Termin solltest du nicht mit 40 Fragen starten. Du führst das Gespräch in Sequenzen. Erst klärst du Zweck. Dann Kontext. Dann Ist. Dann Risiken. Dann Ziel. Dann Entscheidungen. Dann Liefergegenstände. Dann nächste Schritte.

| Phase | Details/Erklärung | Kernfragen | Ergebnis |
|---|---|---|---|
| Einstieg | Zweck und Erwartung klären. | „Was soll nach diesem Termin klarer sein als vorher?“ | Gesprächsziel. |
| Kontext | Umfeld und Beteiligte klären. | „Welche Systeme, Rollen und Organisationseinheiten sind betroffen?“ | Kontextbild. |
| Fachlichkeit | Nutzen und Prozess verstehen. | „Welche fachliche Fähigkeit soll verbessert werden?“ | Capability-/Prozesssicht. |
| Ist | Realität erfassen. | „Wie läuft es heute tatsächlich, inklusive Workarounds?“ | Ist-Bild. |
| Risiken | Schwachstellen sichtbar machen. | „Was würde im Betrieb, bei Security oder Integration schiefgehen, wenn wir nichts klären?“ | Risikoliste. |
| Ziel | Zielzustand beschreiben. | „Wie soll der Zielzustand aussehen?“ | Zielbild. |
| Entscheidung | Optionen und Trade-offs klären. | „Welche Entscheidung steht an und welche Optionen gibt es?“ | Entscheidungsvorlage. |
| Artefakte | Liefergegenstände bestimmen. | „Welches Artefakt brauchen wir als Nächstes?“ | Arbeitsauftrag. |
| Abschluss | Verantwortlichkeit sichern. | „Wer liefert was bis wann, und wer prüft?“ | Maßnahmenliste. |

## Die zehn stärksten Universalfragen eines Enterprise Architekten

Diese Fragen kannst du fast immer verwenden. Sie sind nicht banal, wenn du sie konsequent stellst.

| Aspekt | Details/Erklärung | Frage | Warum sie stark ist |
|---|---|---|---|
| Zweck | Klärt, warum etwas existiert. | „Welches Problem lösen wir damit wirklich?“ | Verhindert Lösung ohne Problem. |
| Fähigkeit | Hebt auf Organisationsebene. | „Welche Fähigkeit der Organisation wird verbessert?“ | Verhindert reines Systemdenken. |
| Grenze | Klärt Scope. | „Was gehört ausdrücklich nicht dazu?“ | Verhindert schleichende Ausweitung. |
| Verantwortung | Klärt Ownership. | „Wer verantwortet diese Entscheidung, dieses System, diese Daten oder diese Schnittstelle?“ | Verhindert Grauzonen. |
| Daten | Macht Risiken sichtbar. | „Welche Daten fließen wohin, warum und mit welcher Kritikalität?“ | Grundlage für Security, Datenschutz, Betrieb. |
| Abhängigkeit | Zeigt Kettenrisiken. | „Wovon hängt diese Lösung ab?“ | Verhindert Überraschungen. |
| Nachweis | Macht Aussagen prüfbar. | „Wodurch ist das belegt?“ | Trennt Behauptung von Erfüllung. |
| Fehlerfall | Prüft Realität. | „Was passiert, wenn diese Komponente ausfällt?“ | Macht Betrieb und Resilienz sichtbar. |
| Entscheidung | Führt aus Diskussion heraus. | „Welche Entscheidung muss jetzt getroffen oder vorbereitet werden?“ | Verhindert endlose Analyse. |
| Konsequenz | Prüft Reife. | „Welche Konsequenzen akzeptieren wir mit dieser Option?“ | Macht Trade-offs ehrlich. |

## Typische Fehler beim Fragenstellen

Der erste Fehler ist, zu früh technische Detailfragen zu stellen. Dadurch wirkst du zwar kompetent, aber du kannst den eigentlichen Architekturkontext verpassen. Der zweite Fehler ist, Fragen ohne Ziel zu stellen. Jede Frage muss ein Artefakt, eine Entscheidung oder eine Prüfung unterstützen. Der dritte Fehler ist, nur nach dem Soll zu fragen und die reale Ist-Situation zu ignorieren. Der vierte Fehler ist, Aussagen nicht nachweisen zu lassen. „Das ist dokumentiert“ reicht nicht. Die richtige Anschlussfrage lautet: „Wo ist die aktuelle, freigegebene und versionierte Dokumentation?“ Der fünfte Fehler ist, Dienstleister nach Meinungen zu fragen, wenn du Liefergegenstände brauchst. Die bessere Frage lautet: „Welche Spezifikation, welcher Testreport, welches ADR oder welches Runbook belegt das?“

## Deine persönliche Frageformel

Nutze in jedem Architekturgespräch diese Formel: „Ich frage nach Zweck, Kontext, Verantwortung, Daten, Schnittstellen, Risiken, Betrieb, Entscheidung und Nachweis.“

Noch kürzer: „Warum? Wer? Was? Woher? Wohin? Was passiert bei Fehler? Wer entscheidet? Wodurch belegt?“

Diese Formel klingt einfach, aber sie ist stark. Sie verhindert, dass du dich in Details verlierst, bevor die Architekturfrage überhaupt verstanden ist.

## Praktische Übung für dich

Nimm unseren Behördenfall: Online-Antragsportal mit IAM, API-Gateway, Fachverfahren, Register, DMS, Datenbank und Betrieb. Erstelle für ein Erstgespräch mit der Fachseite genau zehn Fragen. Danach erstelle zehn Fragen für den Betrieb. Danach zehn Fragen für den Dienstleister. Die Fragen dürfen sich nicht wiederholen.

Eine gute Startlösung wäre: Für die Fachseite fragst du nach Prozess, Ausnahmen, Fachobjekten, Nacharbeit und Erfolg. Für den Betrieb fragst du nach Monitoring, Fehlerfällen, Wiederanlauf, Runbooks und Verantwortlichkeiten. Für den Dienstleister fragst du nach Liefergegenständen, Spezifikationen, Annahmen, Abweichungen und Nachweisen.

## Muster: Zehn Fragen für ein erstes Fachgespräch

| Aspekt | Details/Erklärung | Frage | Erwartetes Ergebnis |
|---|---|---|---|
| Ziel | Fachliche Wirkung klären. | „Welches fachliche Problem soll das Online-Antragsportal lösen?“ | Problemverständnis. |
| Fähigkeit | Capability identifizieren. | „Welche Fähigkeiten der Behörde sollen dadurch verbessert werden?“ | Capability-Liste. |
| Prozess | Ablauf verstehen. | „Wie läuft ein Antrag heute von Eingang bis Abschluss?“ | Prozessskizze. |
| Schmerzpunkt | Verbesserungspotenzial finden. | „Wo entsteht heute die meiste Nacharbeit?“ | Pain Points. |
| Ausnahmen | Realität erfassen. | „Welche Sonderfälle treten häufig auf?“ | Ausnahmefälle. |
| Fachobjekte | Datenbasis schaffen. | „Welche fachlichen Objekte sind zentral?“ | Fachobjektliste. |
| Regeln | Fachlogik verstehen. | „Welche Regeln entscheiden über Vollständigkeit oder Entscheidungsreife?“ | Regelkatalog. |
| Status | Transparenzbedarf klären. | „Welche Statusinformationen brauchen Bürger und Sachbearbeitung?“ | Statusmodell. |
| Erfolg | Messbarkeit klären. | „Woran erkennen Sie nach Einführung, dass die Lösung wirklich hilft?“ | Erfolgskriterien. |
| Risiken | Fachliche Risiken erkennen. | „Was darf fachlich auf keinen Fall schiefgehen?“ | Fachrisiken. |

## Muster: Zehn Fragen für den Betrieb

| Aspekt | Details/Erklärung | Frage | Erwartetes Ergebnis |
|---|---|---|---|
| Verantwortung | Betriebsklarheit schaffen. | „Wer betreibt welche Komponente?“ | Betriebsmodell. |
| Monitoring | Sichtbarkeit prüfen. | „Welche Zustände müssen überwacht werden?“ | Monitoring-Anforderungen. |
| Fehlerfall | Handlungsfähigkeit prüfen. | „Was passiert bei Ausfall der Registerschnittstelle?“ | Fehlerfallbeschreibung. |
| Logs | Diagnose ermöglichen. | „Welche Logs braucht der Betrieb zur Fehleranalyse?“ | Logging-Anforderungen. |
| Tracing | End-to-End-Sicht klären. | „Gibt es eine Korrelations-ID über alle beteiligten Systeme?“ | Traceability. |
| Alerting | Reaktion sichern. | „Welche Fehler lösen einen Alarm aus und wer reagiert?“ | Alertmodell. |
| RTO | Wiederherstellung klären. | „Wie schnell muss welche Funktion wieder verfügbar sein?“ | RTO-Matrix. |
| RPO | Datenverlust klären. | „Wie viel Datenverlust ist maximal tolerierbar?“ | RPO-Anforderung. |
| Runbook | Betriebshandeln sichern. | „Welche Runbooks müssen vor Produktivsetzung vorliegen?“ | Runbook-Liste. |
| Übergabe | Abnahme vorbereiten. | „Woran erkennt der Betrieb, dass die Lösung übergabefähig ist?“ | Betriebsabnahmekriterien. |

## Muster: Zehn Fragen an den Dienstleister

| Aspekt | Details/Erklärung | Frage | Erwartetes Ergebnis |
|---|---|---|---|
| Annahmen | Implizite Voraussetzungen sichtbar machen. | „Welche Architekturannahmen liegen Ihrem Lösungsansatz zugrunde?“ | Annahmenliste. |
| Liefergegenstände | Steuerbarkeit herstellen. | „Welche Architekturartefakte liefern Sie bis zu welchem Meilenstein?“ | Lieferplan. |
| Schnittstellen | Integration prüfen. | „Welche Schnittstellen werden neu erstellt oder geändert?“ | Schnittstellenliste. |
| Spezifikation | API-first prüfen. | „Wann liefern Sie die OpenAPI-Spezifikation vor Implementierung?“ | API-Liefertermin. |
| Abweichungen | Zielbildkonflikte erkennen. | „Welche Vorgaben können Sie nicht oder nur teilweise erfüllen?“ | Abweichungsliste. |
| Security | Nachweise verlangen. | „Welche Security-Prüfungen und Reports liefern Sie?“ | Security-Nachweise. |
| Betrieb | Betriebsfähigkeit prüfen. | „Welche Dashboards, Alerts und Runbooks liefern Sie?“ | Betriebsartefakte. |
| Tests | Qualität nachweisen. | „Welche Tests belegen die Erfüllung der Architekturanforderungen?“ | Testnachweise. |
| Dokumentation | Übergabe sichern. | „Wo wird die Dokumentation versioniert und releasebezogen abgelegt?“ | Dokumentationskonzept. |
| Entscheidungen | Blockaden klären. | „Welche Entscheidungen benötigen Sie vom Auftraggeber?“ | Entscheidungsbedarf. |

## Dein Merksatz

Im Mandat fragst du nach Verantwortung. Im Managementkontext fragst du nach Ziel und Risiko. Bei der Fachseite fragst du nach Fähigkeiten, Prozessen und Regeln. In der Ist-Analyse fragst du nach Realität und Abhängigkeiten. In der Zielarchitektur fragst du nach Richtung und Prinzipien. Bei Schnittstellen fragst du nach Vertrag und Verantwortung. Bei Daten fragst du nach Bedeutung, Herkunft und Lebenszyklus. Bei Security fragst du nach Schutzbedarf und Nachweisen. Bei Betrieb fragst du nach Fehlerfällen und Handlungsfähigkeit. Bei Ausschreibung fragst du nach Liefergegenständen. Bei Abnahme fragst du nach objektiven Prüfkriterien.

Der stärkste Satz für dich lautet: „Ich stelle die Frage, die den nächsten Architekturentscheid möglich macht.“ <>