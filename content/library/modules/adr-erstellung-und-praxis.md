## Checkliste: Was ein professioneller ADR leisten muss

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Entscheidungswürdigkeit prüfen | Ein ADR ist nur nötig, wenn die Entscheidung architekturrelevant ist, also Auswirkungen auf Qualität, Kosten, Betrieb, Sicherheit, Migration oder spätere Änderbarkeit hat. | „Nutzen wir zentrales IAM oder Fachverfahrens-eigene Benutzerverwaltung?“ | ADRs dokumentieren wichtige Architekturentscheidungen samt Kontext und Konsequenzen; die Sammlung heißt Architecture Decision Log. ([github.com](https://github.com/architecture-decision-record/architecture-decision-record?utm_source=chatgpt.com)) |
| Eine Entscheidung pro ADR | Ein ADR darf nicht mehrere Entscheidungen vermischen. Sonst wird er später nicht sauber ersetzbar. | Nicht: „API-Gateway, IAM und Logging festlegen“. Besser: drei ADRs. | Nygards ADR-Ansatz beschreibt eine einzelne bedeutsame Entscheidung mit Kontext, Entscheidung und Konsequenzen. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Kontext klar beschreiben | Der Kontext erklärt, warum die Entscheidung jetzt nötig ist. Er ist keine technische Romansammlung. | „Drei Fachverfahren stellen REST-APIs uneinheitlich bereit; Betrieb fordert zentrale Authentisierung und Monitoring.“ | arc42 betont, dass Stakeholder Architekturentscheidungen nachvollziehen können müssen. ([docs.arc42.org](https://docs.arc42.org/section-9/?utm_source=chatgpt.com)) |
| Entscheidungsfrage präzise formulieren | Die Frage muss so klar sein, dass Optionen dagegen bewertet werden können. | „Welcher Integrationsstandard wird für Registerabfragen verbindlich festgelegt?“ | MADR beschreibt ADRs als strukturierte Dokumentation architekturrelevanter Entscheidungen. ([adr.github.io](https://adr.github.io/madr/?utm_source=chatgpt.com)) |
| Optionen vollständig genug darstellen | Mindestens realistische Alternativen, inklusive „nichts ändern“, müssen benannt werden. | Option A: bestehende Punkt-zu-Punkt-Schnittstellen; Option B: API-Gateway; Option C: Integrationsplattform. | ADR-Templates wie Nygard und MADR strukturieren Entscheidung, Kontext und Alternativen. ([github.com](https://github.com/adr/madr?utm_source=chatgpt.com)) |
| Kriterien vor Bewertung festlegen | Bewertungskriterien müssen vor der Entscheidung sichtbar sein, sonst wirkt der ADR nachträglich zurechtgebogen. | Betrieb, Schutzbedarf, Herstellerbindung, Kosten, Standardkonformität, Migrationsaufwand. | ADRs sollen Entscheidungsrationale erhalten und nicht nur das Ergebnis dokumentieren. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Entscheidung eindeutig treffen | Am Ende muss klar sein, was gilt. Ein ADR ist kein Diskussionsprotokoll. | „Für externe und interne REST-APIs wird ein zentrales API-Gateway verbindlich genutzt.“ | Martin Fowler beschreibt ADRs als kurze Dokumente, die eine Entscheidung, ihren Kontext und wesentliche Auswirkungen erklären. ([martinfowler.com](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html?utm_source=chatgpt.com)) |
| Konsequenzen ehrlich formulieren | Gute ADRs zeigen nicht nur Vorteile, sondern auch neue Pflichten, Risiken und Kompromisse. | „Teams verlieren kurzfristig Autonomie bei API-Exposition; gewinnen aber einheitliche Security- und Betriebsfähigkeit.“ | Nygard betont, dass Konsequenzen eines ADR oft Kontext für spätere ADRs werden. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Status und Lebenszyklus pflegen | Ein ADR braucht Status wie vorgeschlagen, akzeptiert, verworfen, ersetzt oder außer Kraft gesetzt. | „Accepted“, später „Superseded by ADR-014“. | arc42 beschreibt Status wie proposed, accepted, deprecated und superseded. ([docs.arc42.org](https://docs.arc42.org/tips/9-5/?utm_source=chatgpt.com)) |
| Owner und Review-Termin setzen | Ohne Verantwortliche veralten ADRs still. | Owner: Enterprise Architect; Review: nach Pilotmigration oder nach 6 Monaten. | ADRs sollten als lebendige Entscheidungsdokumentation im Projekt oder in der Organisation gepflegt werden. ([github.com](https://github.com/architecture-decision-record/architecture-decision-record?utm_source=chatgpt.com)) |
| Entscheidungslog führen | Einzelne ADRs gehören in ein Decision Log, sonst findet sie niemand. | `ADR-008-api-gateway-standard.md`, verlinkt aus Zielarchitektur und Board-Protokoll. | Ein Architecture Decision Log ist die Sammlung der ADRs für Projekt oder Organisation. ([github.com](https://github.com/architecture-decision-record/architecture-decision-record?utm_source=chatgpt.com)) |
| Governance-Anbindung sicherstellen | ADRs müssen mit Architekturboard, Ausnahmeprozess, Standards, Dienstleistersteuerung und Abnahme verbunden sein. | „Abweichungen vom Logging-Standard benötigen Ausnahme-ADR mit Ablaufdatum.“ | TOGAF beschreibt Architektur-Governance, Architekturboard und Compliance Review als zentrale Steuerungsmechanismen. ([opengroup.org](https://www.opengroup.org/architecture/togaf7-doc/arch/p4/comp/comp.htm?utm_source=chatgpt.com)) |

## 1. Was ein ADR wirklich ist

Ein Architecture Decision Record ist ein kurzes, strukturiertes Entscheidungsdokument. Es hält fest, welche architekturrelevante Entscheidung getroffen wurde, in welchem Kontext sie entstand, welche Optionen betrachtet wurden, warum eine Option gewählt wurde und welche Folgen diese Entscheidung hat. Der entscheidende Punkt ist: Ein ADR dokumentiert nicht nur das Ergebnis, sondern die Denkarbeit hinter dem Ergebnis. Genau dadurch wird Architektur übergabefähig, auditierbar und in Gremien erklärbar. ADRs sind vor allem dann wertvoll, wenn Systeme lange leben, Teams wechseln, Dienstleister kommen und gehen, Behördenverfahren über Jahre modernisiert werden und Entscheidungen später gegen neue Anforderungen geprüft werden müssen. Die ursprüngliche ADR-Idee wird stark mit Michael Nygard verbunden; etablierte Quellen beschreiben die Kernstruktur typischerweise über Status, Kontext, Entscheidung und Konsequenzen. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com))

Der häufigste Fehler ist, ADRs als „Dokumentationspflicht“ zu verstehen. Das ist zu klein gedacht. Ein ADR ist ein Führungsinstrument für Architekturentscheidungen. Er zwingt dich, die Entscheidungsfrage sauber zu formulieren, Alternativen fair zu bewerten, Konsequenzen sichtbar zu machen und spätere Abweichungen nicht im Nebel verschwinden zu lassen. In einer Bundesbehörde ist das besonders wichtig, weil Entscheidungen nicht nur technisch wirken, sondern auch Vergabe, Datenschutz, Informationssicherheit, Betrieb, Nachweisfähigkeit, Haushaltslogik, Fachverantwortung und politische Anschlussfähigkeit berühren.

## 2. Der Unterschied zwischen ADR, Architekturkonzept, Board-Beschluss und Protokoll

Ein ADR ist kein vollständiges Architekturkonzept. Das Architekturkonzept beschreibt Zielbild, Sichten, Datenflüsse, Schnittstellen, Betriebsmodell, Security, Migration und Risiken. Der ADR hält einzelne, besonders folgenreiche Entscheidungen innerhalb dieses Konzepts fest. Ein Board-Beschluss ist wiederum die formale Gremienentscheidung oder Freigabe. Das Protokoll hält fest, was im Termin gesagt wurde. Der ADR hält fest, was als architektonische Entscheidung gilt und warum.

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Architekturkonzept | Beschreibt das Gesamtbild und mehrere Sichten. | Zielarchitektur für Fachverfahrenmodernisierung. | arc42 ordnet Architekturentscheidungen als eigenen Abschnitt in Architekturdokumentation ein. ([docs.arc42.org](https://docs.arc42.org/section-9/?utm_source=chatgpt.com)) |
| ADR | Dokumentiert genau eine wesentliche Entscheidung. | „Zentrales API-Gateway wird verbindlicher Zugangspunkt für REST-APIs.“ | ADRs erfassen wichtige Architekturentscheidungen mit Kontext und Konsequenzen. ([github.com](https://github.com/architecture-decision-record/architecture-decision-record?utm_source=chatgpt.com)) |
| Entscheidungslog | Sammlung und Index aller ADRs. | ADR-001 bis ADR-035 mit Status, Owner und Reviewdatum. | Der Begriff Architecture Decision Log bezeichnet die ADR-Sammlung. ([github.com](https://github.com/architecture-decision-record/architecture-decision-record?utm_source=chatgpt.com)) |
| Board-Beschluss | Formale Freigabe durch zuständiges Gremium. | Architekturboard akzeptiert ADR-008 mit Auflagen. | TOGAF beschreibt Architekturboard und Compliance Reviews als Governance-Bausteine. ([opengroup.org](https://www.opengroup.org/architecture/togaf7-doc/arch/p4/board/ab.htm?utm_source=chatgpt.com)) |
| Ausnahmeentscheidung | Zeitlich begrenzte Abweichung von einem Standard. | Ein Altsystem darf 12 Monate ohne Gateway angebunden bleiben. | In Governance-Kontexten sind Compliance Reviews und Abweichungsbehandlung zentrale Mechanismen. ([opengroup.org](https://www.opengroup.org/architecture/togaf7-doc/arch/p4/comp/comp.htm?utm_source=chatgpt.com)) |
| Protokoll | Gesprächs- und Ergebnisnotiz eines Termins. | „Diskussion über Gateway-Lösung, Betrieb bittet um Monitoringkonzept.“ | Ein ADR ersetzt kein Sitzungsprotokoll, sondern verdichtet die tragende Entscheidung. |

## 3. Wann du einen ADR schreiben solltest

Du schreibst einen ADR, wenn eine Entscheidung später erklärungsbedürftig ist. In Behördenarchitekturen sind das meistens Entscheidungen mit Auswirkungen auf Schutzbedarf, Datenverantwortung, Integration, IAM, Betriebsmodell, Herstellerbindung, Cloud-Nutzung, Vergabe, Standardisierung, Migration oder Abnahme. Ein ADR ist nicht nötig für triviale Implementierungsdetails, etwa die Benennung einer Hilfsklasse oder die Farbe eines Buttons. Er ist aber zwingend sinnvoll, wenn ein Fachverfahren künftig ein zentrales IAM verwenden soll, wenn eine Legacy-Schnittstelle abgelöst wird, wenn Registerdaten synchron oder asynchron integriert werden, wenn Logging zentralisiert wird oder wenn eine Cloud-Option zugelassen oder ausgeschlossen wird.

Eine einfache Prüffrage lautet: „Wird jemand in sechs Monaten fragen, warum wir das so gemacht haben?“ Falls ja, schreib einen ADR. Die zweite Prüffrage lautet: „Kann diese Entscheidung Kosten, Betrieb, Sicherheit, Lieferfähigkeit, Abnahme oder spätere Migration wesentlich beeinflussen?“ Falls ja, schreib einen ADR. Die dritte Prüffrage lautet: „Müssen Dienstleister, Betrieb, Fachseite, Datenschutz oder Informationssicherheit dieselbe Entscheidung verstehen?“ Falls ja, schreib einen ADR.

## 4. Der Lebenszyklus eines ADR

Ein ADR beginnt nicht mit „Accepted“. Er beginnt häufig als Vorschlag. In professioneller Governance ist der Lebenszyklus wichtig, weil er zeigt, ob eine Entscheidung nur diskutiert, abgestimmt, verbindlich, verworfen oder durch eine spätere Entscheidung ersetzt wurde. Viele Teams machen den Fehler, alte ADRs zu überschreiben. Das ist gefährlich, weil dadurch die Entscheidungsgeschichte verloren geht. Besser ist: Ein akzeptierter ADR bleibt grundsätzlich stabil. Wenn sich die Lage ändert, entsteht ein neuer ADR, der den alten ersetzt. Genau diese Nachvollziehbarkeit ist einer der Kernnutzen von ADRs. Fowler beschreibt ebenfalls den Ansatz, geänderte Entscheidungen nicht einfach umzuschreiben, sondern durch verlinkte neue Entscheidungen zu ersetzen. ([martinfowler.com](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html?utm_source=chatgpt.com))

| Status | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Draft | Erste Arbeitsfassung, noch nicht abgestimmt. | Architekt erstellt ADR-Entwurf zur Gateway-Auswahl. | Statusmodelle sind fester Bestandteil gängiger ADR-Templates. ([docs.arc42.org](https://docs.arc42.org/tips/9-5/?utm_source=chatgpt.com)) |
| Proposed | Entscheidungsvorschlag liegt zur Prüfung vor. | Fachseite, Betrieb und Informationssicherheit prüfen Optionen. | arc42 nennt „proposed“ als möglichen Status vor Zustimmung. ([docs.arc42.org](https://docs.arc42.org/tips/9-5/?utm_source=chatgpt.com)) |
| Accepted | Entscheidung ist verbindlich angenommen. | Architekturboard akzeptiert ADR mit Umsetzungsauflagen. | „Accepted“ ist ein gängiger ADR-Status. ([docs.arc42.org](https://docs.arc42.org/tips/9-5/?utm_source=chatgpt.com)) |
| Rejected | Option wurde bewusst nicht gewählt. | „Direkte Punkt-zu-Punkt-Anbindung an Register wird verworfen.“ | Auch verworfene Optionen sind wichtig, damit Diskussionen nicht ständig neu beginnen. |
| Superseded | Entscheidung wurde durch neuen ADR ersetzt. | ADR-006 wird durch ADR-021 ersetzt. | arc42 beschreibt „superseded“ als Status für ersetzte Entscheidungen. ([docs.arc42.org](https://docs.arc42.org/tips/9-5/?utm_source=chatgpt.com)) |
| Deprecated | Entscheidung gilt noch historisch, soll aber nicht mehr für neue Vorhaben genutzt werden. | SOAP-only-Integrationsstandard wird außer Kraft gesetzt. | „Deprecated“ ist ein etablierter Status in ADR-Konventionen. ([docs.arc42.org](https://docs.arc42.org/tips/9-5/?utm_source=chatgpt.com)) |
| Review due | Entscheidung bleibt gültig, muss aber geprüft werden. | Cloud-Option wird nach Änderung der Rahmenbedingungen neu bewertet. | Owner und Reviewzeitpunkt sind praktische Ergänzungen für Governance-Fähigkeit. |

## 5. Die professionelle ADR-Struktur

Ein belastbarer ADR braucht mehr als „Kontext, Entscheidung, Konsequenzen“. Für Behörden und größere Programme empfehle ich eine erweiterte Struktur, weil du dort nicht nur für Entwickler dokumentierst, sondern für Fachverantwortliche, Betrieb, Informationssicherheit, Datenschutz, Vergabe, Dienstleister und Architekturboard.

| Abschnitt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| ID und Titel | Eindeutige Nummer und sprechender Titel. | ADR-008: Zentrales API-Gateway für REST-Schnittstellen. | ADRs werden oft als einzelne Dateien mit fortlaufender Nummer geführt. ([production-ready.de](https://www.production-ready.de/2023/12/28/lightweight-architecture-documentation-adr-en.html?utm_source=chatgpt.com)) |
| Status | Lebenszyklusstatus. | Proposed, Accepted, Superseded. | Status ist Kernbestandteil gängiger ADR-Templates. ([docs.arc42.org](https://docs.arc42.org/tips/9-5/?utm_source=chatgpt.com)) |
| Datum | Zeitpunkt der Entscheidung oder Fassung. | 2026-06-13. | Datierung ist wichtig für spätere Nachvollziehbarkeit. |
| Owner | Verantwortliche Rolle, nicht nur Person. | Enterprise Architect Fachverfahrenmodernisierung. | Owner macht Pflege und Review steuerbar. |
| Review-Zeitpunkt | Zeitpunkt oder Ereignis, bei dem neu geprüft wird. | Nach Pilotmigration, spätestens nach 6 Monaten. | Review-Termine verhindern veraltete Entscheidungslogik. |
| Kontext | Ausgangslage, Randbedingungen, Zwänge. | Gewachsene Fachverfahren, uneinheitliche Schnittstellen, zentrale IAM-Vorgabe. | Nygard-Format verwendet Kontext als Kernabschnitt. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Entscheidungsfrage | Präzise Frage, die beantwortet wird. | „Wie werden REST-APIs behördenweit abgesichert und veröffentlicht?“ | Gute Entscheidungsqualität beginnt mit einer prüfbaren Frage. |
| Treiber und Anforderungen | Warum ist die Entscheidung bedeutsam? | Schutzbedarf, Auditierbarkeit, Betrieb, Standardisierung, Herstellerbindung. | Architecturally Significant Requirements haben messbaren Einfluss auf Architektur und Qualität. ([adr.github.io](https://adr.github.io/?utm_source=chatgpt.com)) |
| Optionen | Realistische Alternativen. | Kein Gateway, dezentrales Gateway je Verfahren, zentrales Gateway. | MADR unterstützt strukturierte Alternativenbetrachtung. ([adr.github.io](https://adr.github.io/madr/?utm_source=chatgpt.com)) |
| Bewertung | Kriterienbasierte Abwägung. | Sicherheit 30 %, Betrieb 25 %, Migration 20 %. | ADRs sollen die Begründung der Entscheidung erhalten. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Entscheidung | Klare, verbindliche Formulierung. | „Wir verwenden ein zentrales API-Gateway als verbindlichen Einstiegspunkt.“ | Entscheidung ist Kernbestandteil jedes ADR. ([github.com](https://github.com/joelparkerhenderson/architecture-decision-record/blob/main/locales/en/templates/decision-record-template-by-michael-nygard/index.md?utm_source=chatgpt.com)) |
| Begründung | Warum diese Option? | Einheitliche Policies, zentrale Observability, geringere Schnittstellenvarianz. | Kontext und Rationale verhindern Wissensverlust. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Konsequenzen | Positive und negative Folgen. | Mehr Standardisierung, aber Migrationsaufwand und Gateway-Betriebsabhängigkeit. | Konsequenzen sind Kernbestandteil des klassischen ADR-Formats. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Umsetzungsauflagen | Was muss passieren, damit die Entscheidung tragfähig wird? | Betriebsmodell, SLIs/SLOs, IAM-Anbindung, Dokumentation, Migrationsplan. | Governance braucht prüfbare Umsetzung und Compliance Review. ([opengroup.org](https://www.opengroup.org/architecture/togaf7-doc/arch/p4/comp/comp.htm?utm_source=chatgpt.com)) |
| Beziehungen | Links zu anderen ADRs, Standards, Konzepten, Tickets. | Verweist auf IAM-ADR, Logging-ADR, Zielarchitektur. | ADRs werden im Entscheidungslog und in Architekturunterlagen verknüpft. |
| Offene Punkte | Was ist noch nicht entschieden? | Produktauswahl, Mandantentrennung, Betriebsverantwortung. | Offene Punkte verhindern Scheingenauigkeit. |

## 6. Qualitätskriterien: Woran du einen guten ADR erkennst

Ein guter ADR ist knapp, aber nicht dünn. Er ist eindeutig, aber nicht dogmatisch. Er zeigt Alternativen, aber verliert sich nicht in endlosen Varianten. Er ist für technische Stakeholder präzise genug und für Gremien verständlich genug. In Behördenkontexten muss er zusätzlich nachweisfähig sein: Man muss später erkennen können, welche Randbedingungen galten, wer beteiligt war, was beschlossen wurde, welche Risiken akzeptiert wurden und welche Auflagen daraus entstanden sind.

| Qualitätskriterium | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Nachvollziehbarkeit | Leser verstehen, warum die Entscheidung getroffen wurde. | „Registerintegration erfolgt asynchron, weil Registerantworten nicht immer innerhalb der fachlichen Prozesszeit verfügbar sind.“ | arc42 betont das Nachvollziehen von Architekturentscheidungen durch Stakeholder. ([docs.arc42.org](https://docs.arc42.org/section-9/?utm_source=chatgpt.com)) |
| Entscheidungsstärke | Der ADR enthält eine klare Entscheidung, keine weichgespülte Absicht. | „Alle neuen REST-APIs müssen über Gateway veröffentlicht werden.“ | ADRs dokumentieren eine konkrete Architekturentscheidung. ([github.com](https://github.com/architecture-decision-record/architecture-decision-record?utm_source=chatgpt.com)) |
| Optionsfairness | Alternativen werden nicht karikiert. | Punkt-zu-Punkt wird als kurzfristig schnell, aber langfristig riskant bewertet. | ADRs erhalten die Begründung und die abgewogenen Alternativen. ([adr.github.io](https://adr.github.io/madr/?utm_source=chatgpt.com)) |
| Konsequenzklarheit | Vor- und Nachteile werden sichtbar. | „Zentralisierung verbessert Auditierbarkeit, erzeugt aber Gateway-Abhängigkeit.“ | Konsequenzen gehören zum klassischen ADR-Kern. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Prüfbarkeit | Aus dem ADR lassen sich Abnahmekriterien ableiten. | „Jede API liefert Korrelations-ID, Fehlerstandard und Gateway-Policy.“ | Governance benötigt Compliance Reviews gegen Architekturvorgaben. ([opengroup.org](https://www.opengroup.org/architecture/togaf7-doc/arch/p4/comp/comp.htm?utm_source=chatgpt.com)) |
| Aktualisierbarkeit | Der ADR kann ersetzt, aber nicht still manipuliert werden. | „Superseded by ADR-017“. | Fowler beschreibt, dass geänderte Entscheidungen über neue verlinkte ADRs behandelt werden sollten. ([martinfowler.com](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html?utm_source=chatgpt.com)) |
| Übertragbarkeit | Dienstleister und neue Teammitglieder können daraus handeln. | ADR wird Teil der Liefergegenstände und Onboarding-Unterlagen. | ADRs unterstützen Wissenserhalt bei Teamwechseln. ([cognitect.com](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com)) |
| Governance-Fähigkeit | Der ADR passt in Board, Entscheidungslog, Ausnahmeprozess und Abnahme. | Board-Freigabe mit Auflagen und Review-Termin. | TOGAF verankert Architekturboard und Compliance Review in Governance. ([opengroup.org](https://www.opengroup.org/architecture/togaf7-doc/arch/p4/board/ab.htm?utm_source=chatgpt.com)) |

## 7. ADRs in Architektur-Governance einbetten

In einer reifen Architektur-Governance ist der ADR kein loses Markdown-Dokument in irgendeinem Repository. Er ist ein verbindlicher Baustein des Entscheidungsprozesses. Ein Vorhaben bringt eine Entscheidungsfrage ein. Der zuständige Architekt formuliert einen ADR-Entwurf. Fachseite, Betrieb, Informationssicherheit, Datenschutz, Plattformteam und gegebenenfalls Vergabe kommentieren. Das Architekturboard entscheidet oder gibt Auflagen. Der ADR wird akzeptiert, verworfen oder zur Nacharbeit zurückgegeben. Danach wird er im Entscheidungslog geführt, in Zielarchitektur, Standards und Liefergegenstände verlinkt und bei Abnahme oder Compliance Review geprüft.

Der Zusammenhang mit Ausnahmeprozessen ist besonders wichtig. Ein Standard ohne Ausnahmeprozess wird in der Praxis entweder ignoriert oder bürokratisch überdehnt. Ein ADR kann festlegen: „Neue Fachverfahren müssen Standard X verwenden.“ Eine Ausnahmeentscheidung kann dann als eigener ADR dokumentieren: „Fachverfahren Y darf für zwölf Monate vom Standard abweichen, weil Schnittstelle Z bis Q4 abgelöst wird; Kompensationsmaßnahmen sind A, B und C; Review am Datum D.“ Damit wird Abweichung nicht heimlich, sondern steuerbar.

Für Dienstleistersteuerung ist der ADR ebenfalls ein Hebel. In Leistungsbeschreibung und Abnahme kann stehen: „Der Auftragnehmer liefert für architekturrelevante Entscheidungen ADRs im vorgegebenen Template. Entscheidungen mit Auswirkungen auf Schnittstellen, Datenhaltung, IAM, Logging, Betrieb, Cloud, Sicherheitsmaßnahmen oder Herstellerbindung sind vor Umsetzung als ADR vorzulegen.“ Dadurch entscheidest du nicht im Nachhinein über fertige Implementierung, sondern steuerst vor der technischen Festlegung.

## 8. Konkreter Governance-Ablauf für Bundesbehörden

| Schritt | Details/Erklärung | Ergebnis | Beteiligte Rollen |
|---|---|---|---|
| 1. Entscheidungsbedarf erkennen | Im Architekturreview, in der Zielbildarbeit, bei Ausschreibung, bei Betriebsübergabe oder bei Sicherheitsprüfung entsteht eine relevante Entscheidungsfrage. | ADR-Kandidat | Enterprise Architect, Solution Architect, Fachverantwortung |
| 2. Entscheidungsfrage formulieren | Die Frage wird so formuliert, dass Optionen vergleichbar werden. | Präzise Entscheidungsfrage | Enterprise Architect |
| 3. Optionen bestimmen | Realistische Optionen inklusive Beibehaltung des Ist-Zustands werden beschrieben. | Optionsliste | Architektur, Betrieb, Dienstleister |
| 4. Bewertungskriterien festlegen | Kriterien werden vor Bewertung festgelegt. | Bewertungsraster | Architekturboard oder Architekturteam |
| 5. ADR-Entwurf schreiben | Kontext, Optionen, Bewertung, Entscheidungsvorschlag und Konsequenzen werden dokumentiert. | ADR Draft/Proposed | Owner des ADR |
| 6. Fachliche und technische Prüfung | Fachseite, Informationssicherheit, Datenschutz, Betrieb und Plattform prüfen Auswirkungen. | Kommentare, Auflagen | Fachbereich, ISB, Datenschutz, Betrieb |
| 7. Board-Entscheidung | Architekturboard akzeptiert, verwirft oder fordert Nacharbeit. | Accepted/Rejected/Needs Work | Architekturboard |
| 8. Umsetzung ableiten | Maßnahmen, Tickets, Liefergegenstände und Abnahmekriterien werden erstellt. | Umsetzungspfad | Projektleitung, Dienstleister, Product Owner |
| 9. Entscheidungslog aktualisieren | ADR wird indexiert, verlinkt und auffindbar gemacht. | Decision Log | Architekturmanagement |
| 10. Review durchführen | Entscheidung wird bei Ereignis oder Termin erneut geprüft. | Weiter gültig, ersetzt oder außer Kraft gesetzt | Owner, Board, Betrieb |

## 9. ADR-Vorlage für professionelle Behördenarchitektur

Diese Vorlage ist bewusst etwas reichhaltiger als das minimalistische Nygard-Format, weil sie in Governance-, Ausschreibungs- und Abnahmekontexten besser trägt. Für kleine Teams kann man sie kürzen; für Bundesbehörden, Modernisierungsprogramme und Dienstleistersteuerung ist diese Form praxistauglicher.

```markdown id="b0kets"
# ADR-XXX: [Sprechender Entscheidungstitel]

## Status
[Draft | Proposed | Accepted | Rejected | Deprecated | Superseded]

## Datum
[YYYY-MM-DD]

## Owner
[Rolle, Organisationseinheit, optional Name]

## Review-Zeitpunkt
[Datum oder Ereignis, z. B. nach Pilotmigration, vor Ausschreibung, nach Sicherheitsfreigabe]

## Kontext
[Ausgangslage, Problem, Randbedingungen, fachliche und technische Treiber. Keine Lösung vorwegnehmen.]

## Entscheidungsfrage
[Eine klare Frage, die durch diesen ADR beantwortet wird.]

## Ziele
- [Ziel 1]
- [Ziel 2]
- [Ziel 3]

## Nicht-Ziele
- [Was mit diesem ADR ausdrücklich nicht entschieden wird.]
- [Was später gesondert entschieden wird.]

## Anforderungen und Bewertungskriterien
| Kriterium | Gewichtung | Erläuterung |
|---|---:|---|
| Fachliche Passung | [%] |  |
| Betrieb | [%] |  |
| Informationssicherheit | [%] |  |
| Datenschutz | [%] |  |
| Migrationsfähigkeit | [%] |  |
| Kosten/Nutzen | [%] |  |
| Herstellerbindung | [%] |  |
| Standardkonformität | [%] |  |

## Betrachtete Optionen
### Option A: [Name]
[Beschreibung, Vorteile, Nachteile, Risiken]

### Option B: [Name]
[Beschreibung, Vorteile, Nachteile, Risiken]

### Option C: [Name]
[Beschreibung, Vorteile, Nachteile, Risiken]

## Bewertung
| Option | Fachliche Passung | Betrieb | Sicherheit | Migration | Kosten/Nutzen | Gesamtbewertung |
|---|---:|---:|---:|---:|---:|---:|
| Option A |  |  |  |  |  |  |
| Option B |  |  |  |  |  |  |
| Option C |  |  |  |  |  |  |

## Entscheidung
[Klare verbindliche Entscheidung in 3 bis 8 Sätzen.]

## Begründung
[Warum diese Option gewählt wird. Bezug auf Kriterien, Risiken, Randbedingungen.]

## Konsequenzen
### Positive Konsequenzen
[Was verbessert sich?]

### Negative Konsequenzen / Trade-offs
[Welche Nachteile, Pflichten oder Risiken entstehen?]

### Kompensationsmaßnahmen
[Wie werden Risiken begrenzt?]

## Umsetzungsauflagen
- [Auflage 1]
- [Auflage 2]
- [Auflage 3]

## Auswirkungen auf Architektur-Sichten
| Sicht | Auswirkung |
|---|---|
| Fachliche Fähigkeiten |  |
| Daten |  |
| Anwendungen |  |
| Schnittstellen |  |
| Plattform |  |
| IAM |  |
| Logging/Monitoring |  |
| Betrieb |  |
| Security |  |
| Migration |  |
| Governance |  |

## Beziehungen zu anderen Entscheidungen
- Vorgänger: [ADR-...]
- Ersetzt: [ADR-...]
- Wird ersetzt durch: [ADR-...]
- Verwandte Dokumente: [Zielarchitektur, Sicherheitskonzept, Betriebsmodell, Schnittstellenstandard]

## Offene Punkte
- [Offener Punkt 1]
- [Offener Punkt 2]

## Board-Entscheidung / Freigabe
- Entscheidungsgremium: [Name]
- Datum: [YYYY-MM-DD]
- Ergebnis: [Accepted/Rejected/Accepted with conditions]
- Auflagen: [Liste]
```

## 10. Beispiel-ADR 1: Zentrales API-Gateway für Fachverfahren

```markdown id="3k2vl6"
# ADR-008: Zentrales API-Gateway als verbindlicher Zugangspunkt für REST-Schnittstellen

## Status
Proposed

## Datum
2026-06-13

## Owner
Enterprise Architect Fachverfahrenmodernisierung

## Review-Zeitpunkt
Nach Abschluss der Pilotmigration von Fachverfahren A und vor Rollout auf weitere Fachverfahren.

## Kontext
Die Behörde betreibt mehrere gewachsene Fachverfahren mit unterschiedlichen REST-Schnittstellen. Authentifizierung, Autorisierung, Rate Limiting, Protokollierung, Fehlerbehandlung und technische Dokumentation sind uneinheitlich umgesetzt. Einige Schnittstellen werden direkt aus den Fachverfahren veröffentlicht. Dadurch entstehen erhöhte Betriebsaufwände, uneinheitliche Sicherheitskontrollen, erschwerte Fehleranalyse und geringe Vergleichbarkeit bei Abnahmen.

## Entscheidungsfrage
Sollen neue und modernisierte REST-Schnittstellen direkt durch die Fachverfahren bereitgestellt werden oder über ein zentrales API-Gateway veröffentlicht und abgesichert werden?

## Ziele
Die Behörde möchte Schnittstellen standardisieren, Sicherheitskontrollen zentral durchsetzen, API-Nutzung beobachtbar machen, Betriebsfähigkeit verbessern und Dienstleisterlieferungen vergleichbarer abnehmen.

## Nicht-Ziele
Dieser ADR entscheidet nicht über das konkrete Gateway-Produkt. Er entscheidet ebenfalls nicht über die vollständige Integrationsarchitektur für asynchrone Events.

## Anforderungen und Bewertungskriterien
| Kriterium | Gewichtung | Erläuterung |
|---|---:|---|
| Sicherheitsdurchsetzung | 30 % | Einheitliche Authentifizierung, Autorisierung, TLS, Rate Limiting, Policy Enforcement. |
| Betriebsfähigkeit | 25 % | Monitoring, Logging, Fehleranalyse, zentrale Betriebsprozesse. |
| Migrationsfähigkeit | 20 % | Schrittweise Anbindung bestehender und neuer Schnittstellen. |
| Dienstleistersteuerung | 15 % | Einheitliche Vorgaben für API-Liefergegenstände. |
| Kosten/Nutzen | 10 % | Einführungs- und Betriebskosten gegenüber Standardisierungsnutzen. |

## Betrachtete Optionen
### Option A: Direkte Veröffentlichung aus jedem Fachverfahren
Diese Option ist kurzfristig einfach und vermeidet zusätzliche Gateway-Komplexität. Sie führt aber zu uneinheitlichen Sicherheits- und Betriebsmechanismen. Jedes Fachverfahren müsste eigene Querschnittsfunktionen umsetzen.

### Option B: Dezentrale Gateways je Fachverfahren
Diese Option ermöglicht lokale Autonomie, erzeugt aber mehrere Betriebsmodelle, unterschiedliche Konfigurationen und erhöhten Standardisierungsaufwand.

### Option C: Zentrales API-Gateway
Diese Option bündelt Authentifizierung, Autorisierung, Routing, Rate Limiting, Logging, Monitoring und API-Policy-Durchsetzung an einer zentralen Stelle. Sie erzeugt zusätzliche Plattformabhängigkeit, verbessert aber Standardisierung, Nachweisfähigkeit und Betriebsfähigkeit.

## Bewertung
| Option | Sicherheit | Betrieb | Migration | Dienstleistersteuerung | Gesamtbewertung |
|---|---:|---:|---:|---:|---:|
| A: Direkte Veröffentlichung | 2/5 | 2/5 | 3/5 | 2/5 | 2,25/5 |
| B: Dezentrale Gateways | 3/5 | 3/5 | 3/5 | 3/5 | 3,00/5 |
| C: Zentrales API-Gateway | 5/5 | 4/5 | 4/5 | 5/5 | 4,50/5 |

## Entscheidung
Neue und modernisierte REST-Schnittstellen werden künftig über ein zentrales API-Gateway veröffentlicht. Direkte externe API-Veröffentlichungen aus Fachverfahren sind nicht zulässig, sofern keine genehmigte Ausnahmeentscheidung vorliegt. Bestehende Schnittstellen werden im Rahmen der Modernisierungsroadmap schrittweise migriert.

## Begründung
Das zentrale Gateway verbessert die Durchsetzung einheitlicher Sicherheits- und Betriebsanforderungen. Es reduziert Variantenvielfalt, erleichtert Monitoring und schafft eine klare Abnahmelinie für Dienstleister. Die zusätzliche Gateway-Abhängigkeit wird akzeptiert, weil sie durch Hochverfügbarkeit, Betriebsmodell, Monitoring und klare Verantwortlichkeiten begrenzt werden kann.

## Konsequenzen
### Positive Konsequenzen
API-Security, Rate Limiting, zentrale Protokollierung, Nutzungsmonitoring und Routing werden standardisierbar. API-Dokumentation und Schnittstellenabnahme werden vergleichbarer.

### Negative Konsequenzen / Trade-offs
Das Gateway wird zu einer zentralen Betriebsabhängigkeit. Teams müssen Gateway-Policies, Deployment-Prozesse und Freigaben berücksichtigen. Kurzfristig entsteht Migrationsaufwand.

### Kompensationsmaßnahmen
Das Gateway benötigt Hochverfügbarkeit, Monitoring, definierte SLOs, Runbooks, Notfallprozesse und klare Betriebsverantwortung.

## Umsetzungsauflagen
Alle neuen APIs müssen OpenAPI-Spezifikationen, Fehlerstandard, Authentifizierungsverfahren, Autorisierungsmodell, Korrelations-ID und Monitoring-Anforderungen dokumentieren. Für Bestands-APIs wird eine Migrationsliste erstellt. Ausnahmen benötigen einen eigenen Ausnahme-ADR mit Ablaufdatum.

## Auswirkungen auf Architektur-Sichten
| Sicht | Auswirkung |
|---|---|
| Anwendungen | Fachverfahren liefern APIs, veröffentlichen sie aber nicht direkt extern. |
| Schnittstellen | API-Gateway wird verbindlicher Einstiegspunkt für REST. |
| IAM | Gateway muss mit zentralem IAM integriert werden. |
| Logging/Monitoring | API-Aufrufe werden zentral beobachtbar. |
| Betrieb | Gateway benötigt eigenes Betriebsmodell, SLIs, SLOs und Runbooks. |
| Governance | API-Standards werden über Architekturreview und Abnahme geprüft. |

## Beziehungen zu anderen Entscheidungen
Verwandt mit ADR-009 IAM-Standard, ADR-010 Logging-Standard und ADR-011 OpenAPI-Mindeststandard.

## Offene Punkte
Konkrete Produktauswahl, Mandantentrennung, Betriebsverantwortung und Lizenzmodell sind in separaten Entscheidungen zu klären.

## Board-Entscheidung / Freigabe
Ausstehend.
```

## 11. Beispiel-ADR 2: Modularer Monolith statt Microservices für die erste Modernisierungswelle

```markdown id="ri0pcr"
# ADR-012: Modularer Monolith für die erste Modernisierungswelle des Fachverfahrensverbunds

## Status
Accepted

## Datum
2026-06-13

## Owner
Solution Architect Modernisierung Fachverfahren

## Review-Zeitpunkt
Nach Abschluss Release 1.2 und vor Zerlegung in eigenständig betreibbare Services.

## Kontext
Mehrere Fachverfahren sind fachlich eng gekoppelt. Die Domänengrenzen sind teilweise unklar, Datenverantwortung ist nicht vollständig geklärt und es existieren zahlreiche implizite Prozessabhängigkeiten. Gleichzeitig besteht Modernisierungsdruck, weil Wartbarkeit, Testbarkeit und Betriebsfähigkeit unzureichend sind. Ein direkter Umstieg auf Microservices würde klare Domänenschnitte, reife CI/CD-Prozesse, Observability, API-Governance, Plattformbetrieb und DevOps-Verantwortung voraussetzen.

## Entscheidungsfrage
Soll die erste Modernisierungswelle als Microservice-Architektur oder als modularer Monolith mit klaren fachlichen Modulen umgesetzt werden?

## Ziele
Die Modernisierung soll fachliche Struktur schaffen, technische Schulden reduzieren, Tests verbessern, Datenverantwortung sichtbar machen und eine spätere Zerlegung vorbereiten, ohne frühzeitig verteilte Komplexität einzuführen.

## Nicht-Ziele
Dieser ADR schließt Microservices nicht grundsätzlich aus. Er entscheidet nur über die erste Modernisierungswelle.

## Betrachtete Optionen
### Option A: Microservices ab Start
Diese Option verspricht unabhängige Deployments und Skalierung. Sie erfordert jedoch stabile Domänengrenzen, reife Betriebsprozesse und hohe Observability. Bei unklaren Datenverantwortungen drohen verteilte Inkonsistenzen.

### Option B: Modularer Monolith
Diese Option hält Deployment und Betrieb zunächst einfacher, erzwingt aber klare Modulgrenzen, interne Schnittstellen, Domänenstruktur und Testbarkeit. Sie kann eine spätere Service-Zerlegung vorbereiten.

### Option C: Bestehenden Monolithen nur technisch refaktorisieren
Diese Option reduziert kurzfristige Risiken, verbessert aber fachliche Struktur und Zukunftsfähigkeit nur begrenzt.

## Bewertung
| Option | Fachliche Struktur | Betrieb | Migrationsrisiko | Zukunftsfähigkeit | Gesamtbewertung |
|---|---:|---:|---:|---:|---:|
| A: Microservices ab Start | 3/5 | 2/5 | 2/5 | 4/5 | 2,75/5 |
| B: Modularer Monolith | 4/5 | 4/5 | 4/5 | 4/5 | 4,00/5 |
| C: Technisches Refactoring | 2/5 | 3/5 | 4/5 | 2/5 | 2,75/5 |

## Entscheidung
Die erste Modernisierungswelle wird als modularer Monolith umgesetzt. Fachliche Module werden anhand von Domänen, Datenverantwortung und Prozessgrenzen strukturiert. Modulgrenzen werden technisch durch Package-Regeln, ArchUnit-Tests, interne APIs und klare Datenzugriffsvorgaben geschützt. Eine spätere Herauslösung einzelner Module in Services bleibt möglich, wird aber nicht vor Klärung der Domänenschnitte und Betriebsreife entschieden.

## Begründung
Die Organisation benötigt zunächst fachliche und technische Struktur, bevor verteilte Systemkomplexität eingeführt wird. Ein modularer Monolith ermöglicht bessere Wartbarkeit, Testbarkeit und fachliche Entkopplung, ohne sofort die volle Last aus Netzwerkkommunikation, verteiltem Deployment, verteilter Fehleranalyse und Datenkonsistenz tragen zu müssen.

## Konsequenzen
### Positive Konsequenzen
Die erste Modernisierung bleibt betrieblich beherrschbar. Teams können Domänengrenzen schärfen, technische Abhängigkeiten messen und spätere Service-Kandidaten identifizieren.

### Negative Konsequenzen / Trade-offs
Unabhängige Skalierung und unabhängiges Deployment einzelner Module sind zunächst eingeschränkt. Es besteht das Risiko, dass der modulare Monolith ohne Governance wieder zu einem ungeordneten Monolithen wird.

### Kompensationsmaßnahmen
Modulgrenzen werden automatisiert geprüft. Architekturverletzungen blockieren Pull Requests. Jede spätere Service-Herauslösung benötigt einen eigenen ADR mit Betriebskonzept, Datenverantwortung, Schnittstellenvertrag und Observability-Anforderungen.

## Umsetzungsauflagen
Es werden Modulregeln, Architekturtests, technische Abhängigkeitsberichte, fachliche Modulverantwortliche und ein Service-Kandidaten-Register eingeführt.

## Auswirkungen auf Architektur-Sichten
| Sicht | Auswirkung |
|---|---|
| Fachliche Fähigkeiten | Module orientieren sich an fachlichen Fähigkeiten und Prozessgrenzen. |
| Daten | Datenzugriff wird pro Modul geregelt; führende Datenobjekte werden identifiziert. |
| Anwendungen | Eine deploybare Anwendung mit interner modularer Struktur. |
| Schnittstellen | Externe Schnittstellen bleiben stabil; interne Modul-APIs werden definiert. |
| Betrieb | Betrieb bleibt zunächst einfacher als bei vielen Services. |
| Migration | Schrittweise Modernisierung ohne Big-Bang-Zerlegung. |
| Governance | Modulgrenzen werden Bestandteil von Reviews und Abnahme. |

## Beziehungen zu anderen Entscheidungen
Verwandt mit ADR-013 Datenverantwortung je Modul und ADR-014 Schnittstellenstandard für spätere Service-Herauslösung.

## Offene Punkte
Kriterien für Service-Herauslösung, Teamzuschnitt und Zielplattform für spätere Services werden später entschieden.

## Board-Entscheidung / Freigabe
Accepted with conditions: Architekturtests und Modulreview sind verpflichtend.
```

## 12. Beispiel-ADR 3: Zentraler Logging- und Korrelationsstandard

```markdown id="n2oh5i"
# ADR-010: Zentraler Logging- und Korrelationsstandard für Fachverfahren

## Status
Accepted

## Datum
2026-06-13

## Owner
Enterprise Architect Betrieb und Observability

## Review-Zeitpunkt
Nach Anbindung der ersten drei Fachverfahren an die zentrale Protokollierungsinfrastruktur.

## Kontext
Fehleranalysen in der bestehenden Fachverfahrenslandschaft sind aufwendig, weil Logformate, Log-Level, technische IDs und fachliche Vorgangsbezüge uneinheitlich sind. Bei übergreifenden Prozessketten über Portal, API-Gateway, Fachverfahren, Registerschnittstelle und DMS ist nicht zuverlässig nachvollziehbar, welcher Aufruf zu welchem Vorgang gehört. Sicherheitsrelevante Ereignisse werden nicht konsistent erfasst. Das BSI beschreibt in OPS.1.1.5 Anforderungen an Protokollierung; der Baustein behandelt übergreifende Aspekte für angemessene Protokollierung und sicherheitsrelevante Ereignisse. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2022/04_OPS_Betrieb/OPS_1_1_5_Protokollierung_Edition_2022.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com))

## Entscheidungsfrage
Welcher Logging- und Korrelationsstandard gilt verbindlich für neue und modernisierte Fachverfahren?

## Ziele
Die Behörde möchte übergreifende Fehleranalyse ermöglichen, sicherheitsrelevante Ereignisse konsistent erfassen, Betriebsfähigkeit verbessern und Nachvollziehbarkeit entlang verteilter Prozessketten herstellen.

## Nicht-Ziele
Dieser ADR entscheidet nicht über das konkrete SIEM- oder Logmanagement-Produkt. Er entscheidet auch nicht über Detailregeln zur Aufbewahrungsdauer, die mit Datenschutz, Informationssicherheit und Fachverantwortung gesondert festzulegen sind.

## Betrachtete Optionen
### Option A: Jedes Fachverfahren definiert eigenes Logging
Diese Option ist lokal einfach, führt aber zu uneinheitlicher Betriebs- und Analysefähigkeit.

### Option B: Minimaler technischer Standard ohne fachliche Korrelation
Diese Option verbessert technische Logs, lässt aber fachliche Vorgänge weiter schwer nachvollziehbar.

### Option C: Zentraler Logging- und Korrelationsstandard
Diese Option definiert einheitliche Pflichtfelder, Korrelations-ID, fachliche Vorgangsreferenz, Log-Level, technische Fehlercodes, sicherheitsrelevante Ereignisse und Übergabe an zentrale Protokollierungsinfrastruktur.

## Bewertung
| Option | Fehleranalyse | Sicherheitsnachweis | Betriebsfähigkeit | Datenschutzsteuerung | Gesamtbewertung |
|---|---:|---:|---:|---:|---:|
| A: Dezentral beliebig | 1/5 | 1/5 | 2/5 | 2/5 | 1,50/5 |
| B: Minimal technisch | 3/5 | 2/5 | 3/5 | 3/5 | 2,75/5 |
| C: Zentraler Standard | 5/5 | 4/5 | 5/5 | 4/5 | 4,50/5 |

## Entscheidung
Für neue und modernisierte Fachverfahren wird ein zentraler Logging- und Korrelationsstandard verbindlich eingeführt. Jeder technische Request erhält eine Korrelations-ID. Fachliche Prozessschritte müssen, soweit zulässig und erforderlich, mit einer fachlichen Vorgangsreferenz korrelierbar sein. Sicherheitsrelevante Ereignisse werden nach definierten Kategorien protokolliert und an die zentrale Protokollierungsinfrastruktur übergeben.

## Begründung
Ohne einheitliche Korrelation bleiben Fehleranalyse, Incident-Bearbeitung, Betriebsübergabe und Nachweisfähigkeit unnötig schwach. Ein zentraler Standard verbessert die Betriebsfähigkeit und reduziert Analyseaufwand. Gleichzeitig müssen Datenschutz und Zweckbindung sorgfältig berücksichtigt werden, damit Protokollierung nicht zu unkontrollierter Datensammlung wird.

## Konsequenzen
### Positive Konsequenzen
Übergreifende Prozessketten werden nachvollziehbarer. Betrieb, Support und Sicherheitsanalyse erhalten bessere Diagnosefähigkeit. Dienstleister können gegen klare Logging-Anforderungen liefern.

### Negative Konsequenzen / Trade-offs
Teams müssen bestehende Logging-Implementierungen anpassen. Es entsteht zusätzlicher Abstimmungsbedarf zu Logfeldern, Aufbewahrung, Zugriffen und Maskierung.

### Kompensationsmaßnahmen
Es werden Logging-Guidelines, Pflichtfelder, verbotene Felder, Maskierungsregeln, Zugriffskonzept und Review-Prozess festgelegt. Fachliche Daten dürfen nur protokolliert werden, wenn Zweck, Rechtsgrundlage, Schutzbedarf und Aufbewahrung geklärt sind.

## Umsetzungsauflagen
Jedes neue Fachverfahren muss Korrelations-ID, Service-Name, Umgebung, Zeitstempel, technische Operation, Ergebnisstatus, Fehlercode und definierte sicherheitsrelevante Ereignisse protokollieren. Personenbezogene Inhalte dürfen nicht pauschal in Logs geschrieben werden. Der Betrieb erhält Dashboards, Alerts und Runbooks.

## Auswirkungen auf Architektur-Sichten
| Sicht | Auswirkung |
|---|---|
| Daten | Logdaten werden als eigene Datenklasse mit Schutzbedarf betrachtet. |
| Anwendungen | Anwendungen müssen strukturierte Logs liefern. |
| Schnittstellen | Korrelations-ID wird über Schnittstellen weitergereicht. |
| Plattform | Zentrale Protokollierungsinfrastruktur wird Zielkomponente. |
| Security | Sicherheitsereignisse werden konsistent erfassbar. |
| Betrieb | Incident-Analyse, Monitoring und Support werden verbessert. |
| Governance | Logging wird Abnahmekriterium für neue Lieferungen. |

## Beziehungen zu anderen Entscheidungen
Verwandt mit ADR-008 API-Gateway, ADR-015 Observability-Standard und ADR-016 Aufbewahrung von Protokolldaten.

## Offene Punkte
Konkrete Logplattform, Aufbewahrungsfristen, Rollenmodell für Logzugriffe und SIEM-Integration werden separat entschieden.

## Board-Entscheidung / Freigabe
Accepted.
```

## 13. Typische Fehler bei ADRs und wie du sie korrigierst

| Fehler | Details/Erklärung | Korrektur | Beispiel |
|---|---|---|---|
| ADR als Ergebnisnotiz | Es steht nur „Wir nutzen X“, aber nicht warum. | Kontext, Optionen, Kriterien und Konsequenzen ergänzen. | Statt „Wir nutzen Gateway“: „Wir nutzen Gateway, weil zentrale Policy-Durchsetzung und Observability höher bewertet wurden als kurzfristige Autonomie.“ |
| Zu viele Entscheidungen in einem ADR | API-Gateway, IAM, Logging und Deployment werden zusammen entschieden. | In mehrere ADRs schneiden und verlinken. | ADR-008 Gateway, ADR-009 IAM, ADR-010 Logging. |
| Optionen nachträglich konstruiert | Die bevorzugte Lösung wirkt alternativlos. | Echte Alternativen fair darstellen. | Auch „Ist-Zustand beibehalten“ bewerten. |
| Keine negativen Konsequenzen | Der ADR liest sich wie Werbung für eine Lösung. | Trade-offs ausdrücklich benennen. | „Zentralisierung erzeugt Betriebsabhängigkeit.“ |
| Keine Nicht-Ziele | Leser erwarten mehr, als der ADR entscheidet. | Abschnitt „Nicht-Ziele“ ergänzen. | Produktauswahl wird nicht im Standard-ADR entschieden. |
| Unklare Verbindlichkeit | Es bleibt offen, ob die Entscheidung Empfehlung oder Pflicht ist. | Entscheidung mit Geltungsbereich formulieren. | „Gilt für alle neuen REST-APIs ab Stichtag X.“ |
| Kein Owner | Niemand pflegt Review und Aktualität. | Rolle und Verantwortlichkeit benennen. | „Owner: Enterprise Architect Integration.“ |
| Kein Review-Zeitpunkt | Entscheidungen veralten unbemerkt. | Ereignis- oder Datumsreview setzen. | „Review nach Pilotmigration.“ |
| Alte ADRs überschrieben | Entscheidungsgeschichte geht verloren. | Neuen ADR erstellen und alten auf „Superseded“ setzen. | ADR-006 ersetzt durch ADR-021. |
| Nicht mit Umsetzung verbunden | ADR bleibt Papier. | Maßnahmen, Tickets, Abnahme und Standards ableiten. | API-Gateway-ADR erzeugt OpenAPI-Gate und Gateway-Onboarding-Checkliste. |
| Zu technisch für Gremien | Der ADR ist nur für Entwickler lesbar. | Executive Summary oder verständliche Begründung ergänzen. | „Die Entscheidung reduziert Variantenvielfalt und verbessert Nachweisfähigkeit.“ |
| Zu allgemein | Der ADR sagt nur „Wir standardisieren Schnittstellen“. | Konkrete Entscheidung und Geltungsbereich formulieren. | „REST-APIs müssen OpenAPI 3.x, Fehlerobjekt, Versionierung und Authentisierung dokumentieren.“ |

## 14. Bewertungskriterien für Optionen

Ein professioneller ADR bewertet Optionen nicht nach Bauchgefühl, sondern anhand vorher festgelegter Kriterien. Die Kriterien hängen von der Entscheidung ab. Für Bundesbehörden empfehle ich ein Standardraster, das du je nach Entscheidung gewichten kannst.

| Aspekt | Details/Erklärung | Leitfrage | Beispiel |
|---|---|---|---|
| Fachliche Passung | Unterstützt die Option die fachlichen Fähigkeiten und Prozesse? | Passt die Lösung zum Fachverfahren und seinen Prozessketten? | Modularer Monolith passt, wenn Domänenschnitte noch reifen müssen. |
| Schutzbedarf | Unterstützt die Option Anforderungen an Vertraulichkeit, Integrität und Verfügbarkeit? | Kann die Option mit hohem Schutzbedarf umgehen? | Zentrales IAM stärkt kontrollierte Zugriffe. |
| Datenverantwortung | Klärt oder verschleiert die Option führende Systeme und Datenhoheit? | Wer ist System of Record? | Registerdaten werden nicht lokal führend nachgebaut. |
| Betriebsfähigkeit | Kann Betrieb die Lösung überwachen, patchen, sichern und wiederherstellen? | Gibt es Monitoring, Backup, Runbooks, SLOs? | Gateway benötigt klare Betriebsverantwortung. |
| Migrationsfähigkeit | Erlaubt die Option schrittweisen Übergang? | Gibt es Übergangsarchitekturen statt Big Bang? | Legacy-Schnittstellen werden über Adapter schrittweise abgelöst. |
| Standardkonformität | Passt die Option zu behördeninternen oder übergreifenden Standards? | Verletzt sie bestehende Architekturprinzipien? | OpenAPI wird Mindeststandard für REST. |
| Dienstleistersteuerung | Kann die Option in Liefergegenstände und Abnahme übersetzt werden? | Ist sie prüfbar vertraglich beschreibbar? | ADR wird Teil der technischen Lieferdokumentation. |
| Herstellerbindung | Erhöht oder reduziert die Option Abhängigkeit von Anbieter oder Produkt? | Wie austauschbar bleibt die Lösung? | Proprietäre Integrationslogik erhöht Bindung. |
| Kosten/Nutzen | Sind Einführungs-, Betriebs- und Migrationskosten angemessen? | Wo entsteht Nutzen, wo Aufwand? | Gateway kostet Plattformbetrieb, reduziert aber Variantenkosten. |
| Zukunftsfähigkeit | Unterstützt die Option spätere Erweiterung, Skalierung und Modernisierung? | Ist sie ein Zwischenzustand oder Zielzustand? | Modularer Monolith kann spätere Service-Zerlegung vorbereiten. |
| Auditierbarkeit | Ist später nachvollziehbar, wer was warum entschieden hat? | Ist die Entscheidung prüf- und belegbar? | ADR plus Entscheidungslog plus Board-Freigabe. |
| Risiko | Welche technischen, organisatorischen und betrieblichen Risiken entstehen? | Welche Risiken werden akzeptiert, welche kompensiert? | Cloud-Option braucht Exit-Strategie und Schutzbedarfsprüfung. |

## 15. Entscheidungslog: So bettest du ADRs sauber ein

Das Entscheidungslog ist die Landkarte deiner Architekturentscheidungen. Ohne Log werden ADRs zwar geschrieben, aber nicht gefunden. In einem Programm zur Fachverfahrenmodernisierung sollte das Log mindestens ID, Titel, Status, Datum, Owner, betroffene Architekturdomäne, Geltungsbereich, Review-Datum und Beziehungen enthalten.

| ADR-ID | Titel | Status | Domäne | Owner | Review | Beziehungen |
|---|---|---|---|---|---|---|
| ADR-008 | Zentrales API-Gateway | Proposed | Integration | EA Integration | Nach Pilotmigration | Verweist auf ADR-009, ADR-010 |
| ADR-009 | Zentraler IAM-Standard | Draft | IAM/Security | IAM Architect | Vor Ausschreibung | Abhängig von Ziel-IAM |
| ADR-010 | Logging- und Korrelationsstandard | Accepted | Betrieb/Observability | EA Betrieb | Nach 3 Anbindungen | Verweist auf BSI OPS.1.1.5 |
| ADR-012 | Modularer Monolith | Accepted | Anwendung | Solution Architect | Release 1.2 | Voraussetzung für Modul-Governance |
| ADR-016 | Ablösung Legacy-Schnittstelle | Proposed | Migration | Integration Architect | Nach Schnittstelleninventar | Ersetzt Altstandard |

In der Praxis legst du das Entscheidungslog an drei Stellen sichtbar ab: im Architektur-Repository, im Architekturdokument beziehungsweise Zielbild und im Board-Arbeitsraum. Für Dienstleister gehört der Verweis zusätzlich in die Liefergegenstände: „Architekturentscheidungen sind gemäß ADR-Template zu dokumentieren und im Entscheidungslog zu referenzieren.“

## 16. Executive-Formulierungen für Gremien

In Gremien brauchst du eine andere Sprache als im Entwicklerreview. Du musst nicht technischer werden, sondern anschlussfähiger. Die Formulierungen müssen Entscheidung, Nutzen, Risiko und Auflage in wenigen Sätzen transportieren.

| Situation | Formulierung | Zweck |
|---|---|---|
| Entscheidung einbringen | „Wir legen heute nicht nur ein technisches Werkzeug fest, sondern eine verbindliche Architekturregel für künftige Schnittstellen. Der ADR dokumentiert die geprüften Optionen, die Begründung und die daraus folgenden Auflagen.“ | Klärt Tragweite. |
| Risiko ehrlich benennen | „Die gewählte Option reduziert Variantenvielfalt und verbessert Nachweisfähigkeit. Gleichzeitig entsteht eine zentrale Betriebsabhängigkeit, die wir durch Hochverfügbarkeit, Monitoring und Runbooks absichern müssen.“ | Verhindert Schönfärbung. |
| Ausnahme erklären | „Die Ausnahme wird nicht als Freibrief formuliert, sondern als befristete Abweichung mit Kompensationsmaßnahmen und Review-Termin.“ | Macht Abweichung steuerbar. |
| Dienstleistersteuerung erklären | „Der ADR wird als verbindliche Vorgabe in Liefergegenstände und Abnahmekriterien übersetzt. Damit entscheiden wir vor der Implementierung, nicht erst bei der Abnahme.“ | Zeigt Steuerungsnutzen. |
| Modernisierung begründen | „Wir wählen in der ersten Welle den modularen Monolithen nicht aus Bequemlichkeit, sondern weil die fachlichen Grenzen zuerst stabilisiert werden müssen, bevor wir verteilte Betriebs- und Datenkomplexität einführen.“ | Entschärft Microservices-Debatte. |
| Governance entbürokratisieren | „Der ADR soll keine zusätzliche Papierlage erzeugen. Er verhindert, dass dieselbe Grundsatzfrage in jedem Projekt neu diskutiert wird.“ | Positioniert Governance als Entlastung. |

## 17. So schreibst du einen ADR in der Praxis: Schritt-für-Schritt

Zuerst formulierst du die Entscheidungsfrage. Nicht „API-Gateway“, sondern „Wie veröffentlichen und sichern wir REST-Schnittstellen künftig verbindlich?“ Danach beschreibst du den Kontext, ohne die Lösung vorwegzunehmen. Dann bestimmst du realistische Optionen. Wichtig ist, dass du mindestens eine konservative Option, eine Zielbildoption und gegebenenfalls eine Übergangsoption betrachtest. Anschließend legst du Bewertungskriterien fest. Erst dann bewertest du. Danach formulierst du die Entscheidung als verbindliche Aussage. Zum Schluss schreibst du Konsequenzen, Auflagen, offene Punkte, Beziehungen und Review-Termin.

Die beste praktische Regel lautet: Ein guter ADR beantwortet sieben Fragen. Was war los? Was musste entschieden werden? Welche Optionen gab es? Nach welchen Kriterien wurde bewertet? Was wurde entschieden? Warum wurde so entschieden? Was bedeutet das jetzt konkret für Umsetzung, Betrieb, Risiken und Abnahme?

## 18. Mini-Beispiele für weitere ADR-Kandidaten aus Bundesbehörden

| Thema | Entscheidungsfrage | Mögliche Entscheidung | Typische Konsequenz |
|---|---|---|---|
| Registerintegration | Erfolgt Registerabfrage synchron, asynchron oder hybrid? | Synchrone Abfrage für einfache Validierung, asynchrone Verarbeitung für langlaufende Prüfungen. | Prozessmodell, Fehlerhandling und Benutzerkommunikation müssen angepasst werden. |
| IAM-Standard | Wird OAuth2/OIDC oder SAML als Standard für neue Anwendungen genutzt? | OIDC für neue Web- und API-basierte Anwendungen, SAML nur für Bestand und spezifische Föderationsfälle. | Token-Handling, Rollenmodell und technische Clients müssen standardisiert werden. |
| Cloud-Option | Darf ein Fachverfahren eine Cloud-Plattform nutzen? | Cloud nur nach Schutzbedarfsprüfung, Exit-Konzept, Betriebsmodell und Freigabe. | Architekturentscheidung wird mit Sicherheits- und Beschaffungsprüfung gekoppelt. |
| Legacy-Schnittstelle | Wird eine proprietäre Dateiübertragung weiterbetrieben oder abgelöst? | Ablösung durch standardisierte API oder Event-Schnittstelle innerhalb von 18 Monaten. | Übergangsadapter und Migrationswellen werden nötig. |
| Logging-Standard | Welche Pflichtfelder gelten für Logs? | Strukturierte Logs mit Korrelations-ID und definierten Sicherheitsereignissen. | Anwendungen müssen Logging technisch und organisatorisch anpassen. |
| Datenverantwortung | Welches System ist führend für Personendaten? | Register bleibt führend, Fachverfahren hält nur Referenz und fachliche Ergänzungen. | Datenkopien und Synchronisationsregeln müssen bereinigt werden. |

## 19. Übung: Schreibe deinen eigenen ADR

### Ausgangslage

Eine Bundesbehörde betreibt drei gewachsene Fachverfahren. Fachverfahren A hält Personendaten, Fachverfahren B hält Vorgangsdaten, Fachverfahren C erzeugt Bescheide. Zusätzlich gibt es eine Registerschnittstelle, ein DMS, ein zentrales IAM-Projekt und ein neues API-Gateway. Heute existieren direkte Punkt-zu-Punkt-Schnittstellen, unterschiedliche Authentisierungsmuster, uneinheitliches Logging und keine eindeutige Datenverantwortung für Statusinformationen. Ein Dienstleister schlägt vor, sofort mehrere Microservices zu bauen und alle Schnittstellen neu zu schneiden.

### Aufgabe

Erstelle einen ADR zur Frage: „Soll die Modernisierung der Statusinformationen über einen zentralen Status-Service erfolgen oder bleiben Statusinformationen je Fachverfahren lokal?“ Verwende die Vorlage und bewerte mindestens drei Optionen: lokaler Status je Fachverfahren, zentraler Status-Service, Event-basierte Statusprojektion. Formuliere eine klare Entscheidung, mindestens fünf Bewertungskriterien, positive und negative Konsequenzen, Umsetzungsauflagen und einen Review-Zeitpunkt.

### Muster-Bewertungskriterien

| Aspekt | Details/Erklärung | Beispiel |
|---|---|---|
| Fachliche Eindeutigkeit | Status muss für Sachbearbeitung und Antragstellende konsistent verständlich sein. | „In Prüfung“, „Nachweis fehlt“, „Bescheid erstellt“. |
| Datenverantwortung | Es muss klar sein, welches System welchen Status führt. | Vorgangsstatus durch Fachverfahren B, Bescheidstatus durch Fachverfahren C. |
| Integrationsaufwand | Aufwand für bestehende Fachverfahren und neue Schnittstellen. | Event-Projektion benötigt Broker und Schema-Governance. |
| Betriebsfähigkeit | Monitoring, Fehleranalyse, Wiederanlauf. | Status-Service braucht SLO und Recovery-Konzept. |
| Migrationsfähigkeit | Schrittweiser Übergang ohne Big Bang. | Erst Projektion aus Bestand, später führende Statuslogik. |
| Nutzerwirkung | Verlässliche Statusanzeige für Portal und Sachbearbeitung. | Keine widersprüchlichen Anzeigen im Portal. |
| Risiko | Gefahr falscher Statusinformationen. | Veraltete Projektion könnte falsche Auskunft anzeigen. |

### Erwartete Ergebnisqualität

Ein guter Übungs-ADR würde nicht einfach „zentral ist besser“ behaupten. Er würde sauber klären, ob der zentrale Status-Service führend sein soll oder nur eine lesende Projektion. Er würde formulieren, welche Statusarten es gibt, welche Systeme sie erzeugen, welche Latenz akzeptabel ist, wie Fehler korrigiert werden, wie Ereignisse versioniert werden und welche fachlichen Stellen Statusdefinitionen verantworten. Genau an dieser Stelle trennt sich Formulararbeit von echter Architekturarbeit.

## 20. Dein Zielbild als ADR-Coach

Du solltest ADRs künftig als Architektur-Nachweislinie verwenden. Für jede wesentliche Entscheidung fragst du: Ist sie architekturrelevant? Ist sie später erklärungsbedürftig? Betrifft sie mehrere Stakeholder? Erzeugt sie Standards oder Ausnahmen? Muss ein Dienstleister danach liefern? Muss ein Gremium sie verstehen? Wenn ja, bekommt sie einen ADR. Der ADR wird nicht als Bürokratie geschrieben, sondern als Entscheidungswerkzeug: präzise Frage, fair bewertete Optionen, klare Entscheidung, ehrliche Konsequenzen, verbindliche Auflagen und sichtbarer Platz im Entscheidungslog.

Damit kannst du in einer Bundesbehörde sehr souverän auftreten. Du wirkst nicht wie jemand, der nur Technologiepräferenzen vertritt, sondern wie ein Enterprise Architect, der Entscheidungen steuerbar, prüfbar, übergabefähig und anschlussfähig macht. Genau das ist der professionelle Unterschied: Architektur ist nicht nur, gute Lösungen zu kennen. Architektur ist, tragfähige Entscheidungen unter realen Randbedingungen so zu formulieren, dass Organisationen danach handeln können. <>