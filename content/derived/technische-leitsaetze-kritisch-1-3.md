# Kritische Vertiefung der technischen Leitsätze 1–3

## 1. Jede technische Entscheidung braucht einen fachlichen Grund

**Kritische Gegenfrage:** Muss wirklich jede technische Detailentscheidung fachlich begründet sein?

Nein. Lokale Implementierungsdetails können im Team bleiben. Architekturrelevant wird eine Entscheidung, sobald sie mehrere Systeme, Teams, Daten, Betrieb, Security, Kosten, Abnahme oder spätere Änderbarkeit beeinflusst. Dann muss die fachliche Rückbindung erklärbar sein.

**Prüffragen:** Welche Fähigkeit wird unterstützt? Welche Daten, Schnittstellen und Rollen sind betroffen? Welche Risiken werden reduziert oder erzeugt? Welche Betriebs-, Security- und Datenschutzfolgen entstehen? Wie wird die Entscheidung später geprüft?

**Arbeitsformel:** Eine technische Entscheidung ist dann stark, wenn sie fachlich begründet, architektonisch eingeordnet, betrieblich tragfähig, sicher prüfbar und nachvollziehbar dokumentiert ist.

## 2. Eine Architekturentscheidung ist erst vollständig, wenn ihre Konsequenzen benannt sind

Konsequenzen sind nicht nur Risiken. Sie können positiv, negativ, neutral oder noch offen sein. Eine Entscheidung muss zumindest ihre wesentlichen Wirkungen auf Fachlichkeit, Daten, Schnittstellen, Security, Datenschutz, Betrieb, Migration, Dienstleister, Portfolio und Governance sichtbar machen.

**Prüffragen:** Welche Folgepflichten entstehen? Welche weiteren Entscheidungen werden ausgelöst? Wer trägt Umsetzung und Pflege? Welche Übergangs- oder Migrationsschritte sind nötig?

**Arbeitsformel:** Eine Architekturentscheidung ist reif, wenn Nutzen, Folgepflichten, Risiken, Abhängigkeiten und offene Prüfpunkte sichtbar sind.

## 3. Technische Eleganz ersetzt keine Betriebsfähigkeit

Eine moderne oder konzeptionell saubere Lösung ist nicht automatisch produktionsreif. Betriebsfähigkeit umfasst Ownership, Monitoring/Observability, Fehlerbehandlung, Wiederanlauf, Security, Datenschutz, Support, Runbooks und Abnahme.

**Wichtige Präzisierung:** Architekturreife, Umsetzungsreife, Produktionsreife, Abnahmereife und Betriebsübernahme sind unterschiedliche Reifezustände.

Eine eventbasierte Architektur braucht eine explizite Zustell-, Wiederholungs-, Duplikat- und Fehlerbehandlungsstrategie. Eine Dead Letter Queue ist ein mögliches Mittel, aber nicht in jeder Architektur zwingend.

**Arbeitsformel:** Als Enterprise Architect betreibe ich das System nicht selbst. Ich stelle sicher, dass Betriebsfähigkeit als Architektur- und Qualitätsanforderung früh definiert, im Design berücksichtigt und vor Produktionsfreigabe prüfbar nachgewiesen wird.
