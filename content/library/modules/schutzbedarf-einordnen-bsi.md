## Checkliste: Schutzbedarf professionell einordnen

| Aspekt | Details/Erklärung | Literatur/Quelle |
|---|---|---|
| Zielobjekt sauber bestimmen | Kläre zuerst, was bewertet wird: Information, Prozess, Anwendung, Schnittstelle, Plattform, Infrastruktur, Raum, Dienstleisterzugang oder Datenfluss. | BSI-Methodik nach IT-Grundschutz ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-200-2-IT-Grundschutz-Methodik/bsi-standard-200-2-it-grundschutz-methodik_node.html?utm_source=chatgpt.com)) |
| Drei Grundwerte getrennt bewerten | Vertraulichkeit, Integrität und Verfügbarkeit werden einzeln bewertet; nicht pauschal „das System ist kritisch“. | BSI-Schutzbedarfsfeststellung ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Schaden statt Technologie bewerten | Schutzbedarf fragt: Welcher Schaden entsteht, wenn ein Grundwert verletzt wird? Nicht: Welche Technik gefällt uns? | BSI-Lerneinheit Schutzbedarf ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Kategorien verwenden | Üblich sind „normal“, „hoch“ und „sehr hoch“; die konkrete Bedeutung muss die Organisation über Schadensszenarien operationalisieren. | BSI 200-3 / Schutzbedarf ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_3.pdf?__blob=publicationFile&v=2&utm_source=chatgpt.com)) |
| Fachprozess einbeziehen | Der Fachbereich muss die Folgen bewerten: falscher Bescheid, Fristversäumnis, Datenabfluss, Registerausfall, politische Außenwirkung, Arbeitsunfähigkeit. | BSI 200-2 ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_2.pdf?__blob=publicationFile&v=2&utm_source=chatgpt.com)) |
| Datenschutz gesondert mitdenken | Bei personenbezogenen Daten sind Vertraulichkeit, Integrität, Verfügbarkeit, Belastbarkeit und Wiederherstellbarkeit auch Anforderungen aus Art. 32 DSGVO. | DSGVO Art. 32 / BfDI ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX%3A32016R0679)) |
| Vererbung beachten | Anwendungen, Schnittstellen, Datenbanken, Plattformen und Dienstleisterzugänge erben Schutzbedarf aus Daten und Fachprozessen. | BSI-IT-Grundschutz-Logik ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_2.pdf?__blob=publicationFile&v=2&utm_source=chatgpt.com)) |
| Kumulation erkennen | Viele einzeln „normale“ Daten können durch Menge, Verknüpfbarkeit oder zentrale Aggregation zu hohem Schutzbedarf führen. | BSI-Schadensorientierung ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |
| Architekturfolgen ableiten | Schutzbedarf muss zu IAM, Netzsegmentierung, Verschlüsselung, Logging, Backup, Monitoring, Wiederanlauf und Dienstleistersteuerung führen. | BSI 200-2 / DSGVO Art. 32 ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-200-2-IT-Grundschutz-Methodik/bsi-standard-200-2-it-grundschutz-methodik_node.html?utm_source=chatgpt.com)) |
| Risikoanalyse auslösen | Bei hohem oder sehr hohem Schutzbedarf reicht Standardbetrachtung häufig nicht; dann ist eine explizite Risikoanalyse nach BSI 200-3 naheliegend. | BSI 200-3 ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-200-3-Risikomanagement/bsi-standard-200-3-risikomanagement_node.html?utm_source=chatgpt.com)) |
| Nachweisfähigkeit verlangen | Jede Schutzbedarfsentscheidung braucht Begründung, Verantwortliche, Datum, Annahmen, Reviewtermin und Architekturmaßnahmen. | BSI-ISMS-Methodik ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-200-2-IT-Grundschutz-Methodik/bsi-standard-200-2-it-grundschutz-methodik_node.html?utm_source=chatgpt.com)) |
| Nicht mit Klassifizierung verwechseln | Schutzbedarf ist nicht dasselbe wie Dokumentenklassifizierung, Datenschutzkategorie, Geheimhaltungsstufe oder Kritikalitätslabel; diese Informationen fließen nur in die Bewertung ein. | BSI-/DSGVO-Systematik ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com)) |

## 1. Grundverständnis: Was Schutzbedarf wirklich bedeutet

Schutzbedarf ist die fachlich begründete Aussage darüber, wie schwer der Schaden wäre, wenn ein Zielobjekt in Vertraulichkeit, Integrität oder Verfügbarkeit beeinträchtigt wird. Das BSI beschreibt Schutzbedarfsfeststellung genau über diese Frage: Welcher Schaden kann entstehen, wenn für ein Zielobjekt einer der Grundwerte verletzt wird? ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com))

Für dich als Enterprise Architekt ist das entscheidend: Du bewertest nicht zuerst Firewalls, Kubernetes, Datenbanken oder Verschlüsselungsverfahren. Du bewertest zuerst den Schaden. Erst danach leitest du Architekturbedingungen ab. Ein gutes Architekturreview fragt also nicht: „Ist das System sicher?“, sondern: „Welche Schäden entstehen bei Offenlegung, Manipulation oder Ausfall — und welche Architekturentscheidungen müssen deshalb verbindlich sein?“

Die BSI-Methodik ist dafür besonders relevant, weil der IT-Grundschutz als strukturierte Methode für ein Informationssicherheitsmanagementsystem dient und Anforderungen an Geschäftsprozesse, Anwendungen, Systeme, Kommunikationsverbindungen und Räume methodisch zusammenführt. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-200-2-IT-Grundschutz-Methodik/bsi-standard-200-2-it-grundschutz-methodik_node.html?utm_source=chatgpt.com))

## 2. Die drei Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit

Vertraulichkeit bedeutet, dass Informationen nur von berechtigten Personen, Systemen oder Organisationseinheiten eingesehen oder genutzt werden dürfen. In einer Behörde betrifft das beispielsweise personenbezogene Daten, Vorgangsdaten, Registerauskünfte, interne Bewertungen, Dienstanweisungen, Entwürfe, Bescheide, Rechtspositionen oder Kommunikationsinhalte.

Integrität bedeutet, dass Informationen vollständig, korrekt, unverändert und nachvollziehbar verarbeitet werden. Für Behörden ist Integrität oft der unterschätzte Grundwert. Ein unberechtigt geänderter Bescheid, ein falscher Registerstatus, eine manipulierte Aktennotiz oder ein fehlerhaftes Berichtsdashboard kann fachlich gravierender sein als ein kurzer Ausfall. Integrität betrifft nicht nur Daten, sondern auch Regeln, Workflows, Berechnungen, Freigaben, Schnittstellenverträge und Protokolle.

Verfügbarkeit bedeutet, dass Informationen, Anwendungen, Schnittstellen und Prozesse rechtzeitig nutzbar sind. In Behörden ist Verfügbarkeit nicht nur „Uptime“. Sie hängt an Fristen, gesetzlichen Bearbeitungszeiten, Krisenlagen, politischer Steuerungsfähigkeit, Bürgerzugang, Registerabfragen, Zahlungen, Bescheiderstellung und Betriebsfortführung.

Bei personenbezogenen Daten verstärkt Art. 32 DSGVO diese Sicht: Verantwortliche und Auftragsverarbeiter müssen geeignete technische und organisatorische Maßnahmen treffen, unter anderem Pseudonymisierung und Verschlüsselung, dauerhafte Vertraulichkeit, Integrität, Verfügbarkeit und Belastbarkeit sowie rasche Wiederherstellung bei physischen oder technischen Zwischenfällen. Der BfDI stellt für die Bundesverwaltung ebenfalls heraus, dass Art. 32 DSGVO eine enge Verbindung zwischen Datenschutz und IT-Sicherheitsmanagement herstellt. ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX%3A32016R0679))

## 3. Die drei Schutzbedarfskategorien

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Normal | Der Schaden ist begrenzt und beherrschbar. Normale organisatorische, technische und prozessuale Grundschutzmaßnahmen reichen typischerweise aus, sofern keine besonderen Risiken hinzukommen. | Interne Terminabstimmung ohne sensible Inhalte; allgemeine Berichtsdaten ohne Personenbezug; nichtkritisches Informationsportal. | BSI-Schutzbedarfskategorien ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_3.pdf?__blob=publicationFile&v=2&utm_source=chatgpt.com)) |
| Hoch | Der Schaden wäre beträchtlich. Es drohen erhebliche Auswirkungen auf Personen, Rechtskonformität, Aufgabenerfüllung, Vertrauen, Betrieb oder Finanzen. Architekturentscheidungen müssen nachweisbar verschärft werden. | Fachverfahren mit personenbezogenen Vorgangsdaten; Bescheiderstellung; Registerschnittstelle; produktives DMS mit behördlichen Akten. | BSI 200-2 / 200-3 ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_2.pdf?__blob=publicationFile&v=2&utm_source=chatgpt.com)) |
| Sehr hoch | Der Schaden wäre besonders schwerwiegend, möglicherweise existenzbedrohend für die Institution, katastrophal für Betroffene oder massiv beeinträchtigend für staatliche Aufgabenerfüllung. Hier sind Risikoanalyse, Sondermaßnahmen und Managemententscheidung erforderlich. | Kritisches Fachverfahren in Krisenlage; zentrale Identitätsplattform; Register mit sehr sensiblen Masseninformationen; Systeme mit Wirkung auf Schutz, Versorgung, hoheitliche Entscheidung oder akute Rechtsfolgen. | BSI 200-3 Risikoanalyse ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/BSI-Standard-200-3-Risikomanagement/bsi-standard-200-3-risikomanagement_node.html?utm_source=chatgpt.com)) |

Wichtig: Diese Kategorien sind keine dekorativen Labels. Sie müssen in einer Behörde über konkrete Schadensszenarien definiert werden. Typische Schadenssichten sind Rechtsverstöße, Beeinträchtigung von Betroffenenrechten, Beeinträchtigung der Aufgabenerfüllung, negative Innen- und Außenwirkung, finanzielle Schäden und Auswirkungen auf Personen. Das BSI verweist darauf, dass Schutzbedarf sich an den möglichen Schäden bei Verletzung der Grundwerte orientiert. ([bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Zertifizierte-Informationssicherheit/IT-Grundschutzschulung/Online-Kurs-IT-Grundschutz/Lektion_4_Schutzbedarfsfeststellung/4_01_Definitionen.html?utm_source=chatgpt.com))

## 4. Schutzbedarf nach Zielobjekten bewerten

| Aspekt | Details/Erklärung | Beispiel | Architekturfolge |
|---|---|---|---|
| Information | Informationen sind der fachliche Kern der Bewertung. Frage: Was passiert, wenn diese Information offengelegt, manipuliert oder nicht verfügbar ist? | Registerdaten, Vorgangsdaten, Bescheide, interne Kommunikation. | Datenklassifikation, Verschlüsselung, Zugriffskontrolle, Protokollierung, Löschkonzept. |
| Fachprozess | Prozesse erzeugen Schaden durch falsche Entscheidung, Fristversäumnis, Arbeitsunfähigkeit oder rechtswidrige Bearbeitung. | Antrag prüfen, Bescheid erstellen, Widerspruch bearbeiten, Register abfragen. | RTO/RPO, Vier-Augen-Prinzip, Fallvertretung, Notbetrieb, Prozessmonitoring. |
| Anwendung | Anwendungen erben Schutzbedarf aus Daten und Prozessen, können aber durch zentrale Rolle zusätzlichen Schutzbedarf erzeugen. | Fachverfahren, Portal, Sachbearbeitungsoberfläche, DMS. | Rollenmodell, Mandantentrennung, sichere Sessionsteuerung, Audit Trail, sichere Konfiguration. |
| Schnittstelle | Schnittstellen erben Schutzbedarf aus übertragenen Daten und aus ihrer fachlichen Abhängigkeit. | API-Gateway zu Register, DMS-API, Melde-/Statusschnittstelle. | mTLS, OAuth2/OIDC, technische Service-Identitäten, Schema-Validierung, Rate Limits, Monitoring. |
| Datenbank | Datenbanken kumulieren Informationen. Dadurch steigt Schutzbedarf oft deutlich gegenüber einzelnen Datensätzen. | Vorgangsdatenbank mit Millionen Datensätzen. | Verschlüsselung at rest, strenge Adminrechte, Datenbank-Audit, Backup-Verschlüsselung, Separierung. |
| Infrastruktur | Infrastruktur erbt Schutzbedarf aus allen darauf betriebenen Anwendungen und aus ihrer Kontrollfunktion. | Kubernetes-Cluster, IAM, Netzwerk, Logging-Plattform. | Segmentierung, Hardening, Patchmanagement, privilegierter Zugriff, Plattform-Monitoring. |
| Dienstleisterzugriff | Externe Zugriffe erhöhen Angriffsfläche und Governance-Anforderungen. | Betriebsdienstleister mit Adminzugang, Entwicklerzugriff auf Testdaten, Supportzugang. | Jump Host, Just-in-Time-Zugriff, MFA, Freigabeprozess, Session Recording, AVV, Protokollprüfung. |

Als Architekt musst du hier konsequent sein: Der Schutzbedarf „wandert“ entlang der Abhängigkeiten. Wenn eine Fachanwendung Bescheide erzeugt, eine Datenbank diese speichert, ein DMS sie archiviert und ein Dienstleister produktiven Zugriff erhält, dann darf der hohe Schutzbedarf nicht an der Anwendungsgrenze stehen bleiben. Er muss in Datenfluss, Plattform, Betrieb, Monitoring, Backup, IAM und Lieferantensteuerung sichtbar werden.

## 5. Behördenbeispiele: typische Schutzbedarfsbewertung

| Aspekt | Details/Erklärung | Beispielbewertung | Architekturentscheidung |
|---|---|---|---|
| Personenbezogene Stammdaten | Namen, Anschriften, Geburtsdaten oder Aktenzeichen sind nicht automatisch „sehr hoch“, aber bei Menge, Verknüpfung, Schutzkontext oder besonderer Betroffenheit schnell mindestens hoch in Vertraulichkeit. | Vertraulichkeit: hoch; Integrität: hoch; Verfügbarkeit: normal bis hoch. | Striktes Rollenmodell, Need-to-know, Verschlüsselung, Protokollierung von Zugriffen, keine sensiblen Logpayloads. |
| Vorgangsdaten | Vorgänge zeigen behördliche Entscheidungen, Bearbeitungsstände, Historie, Zuständigkeiten und oft sensible Lebenssachverhalte. | Vertraulichkeit: hoch; Integrität: hoch; Verfügbarkeit: hoch. | Fallbezogene Berechtigungen, Aktenhistorie, unveränderbare Änderungsprotokolle, Datenqualitätsprüfungen. |
| Bescheide | Bescheide erzeugen Rechtswirkung. Hier ist Integrität besonders kritisch, weil falsche oder manipulierte Bescheide unmittelbare Folgen haben können. | Vertraulichkeit: hoch; Integrität: sehr hoch; Verfügbarkeit: hoch. | Vier-Augen-Freigabe, digitale Signatur/Siegel, revisionssichere Ablage, Versionierung, Nachweis der Zustellung. |
| Registerdaten | Registerdaten stammen oft aus autoritativen Quellen. Falsche Registerauskünfte können Folgeentscheidungen verfälschen. | Vertraulichkeit: hoch; Integrität: sehr hoch; Verfügbarkeit: hoch bis sehr hoch. | mTLS, Herkunftsnachweis, Antwortsignatur oder Integritätsschutz, technische Vertrauensbeziehung, Schnittstellenmonitoring. |
| Interne Kommunikation | Nicht jede interne Nachricht ist kritisch. Kritisch wird es bei Personalthemen, Sicherheitsvorfällen, Rechtsbewertungen, Lageeinschätzungen oder Strategie. | Vertraulichkeit: normal bis hoch; Integrität: normal bis hoch; Verfügbarkeit: normal. | Klassifizierung, Zugriffsbeschränkung, Aufbewahrungsregeln, sichere Kollaborationsräume. |
| Berichtsdaten | Aggregierte Berichtsdaten wirken oft harmlos. Risiko entsteht durch Fehlsteuerung, politische Außenwirkung, Re-Identifikation oder falsche Managemententscheidungen. | Vertraulichkeit: normal bis hoch; Integrität: hoch; Verfügbarkeit: normal bis hoch. | Datenherkunft, Kennzahlen-Governance, Freigabeprozess, Dashboard-Audit, Plausibilitätskontrollen. |
| Kritisches Fachverfahren | Kritikalität entsteht, wenn hoheitliche Aufgaben, Fristen, Massenvorgänge, Bürgerzugang, Krisenfähigkeit oder zentrale Abhängigkeiten betroffen sind. | Vertraulichkeit: hoch; Integrität: hoch bis sehr hoch; Verfügbarkeit: hoch bis sehr hoch. | Hochverfügbarkeit, Notbetrieb, RTO/RPO, Monitoring, Incident Runbooks, regelmäßige Restore-Tests, Risikoanalyse. |

Ein häufiger Denkfehler wäre: „Personenbezogen = immer sehr hoch.“ Das ist zu grob. Richtig ist: Personenbezug ist ein starker Hinweis, aber die Bewertung hängt von Art, Umfang, Kontext, Betroffenenrisiko, Datenmenge, Verknüpfbarkeit, Rechtsfolgen und Prozesskritikalität ab. Art. 32 DSGVO verlangt ein dem Risiko angemessenes Schutzniveau, nicht pauschal dieselbe Maßnahme für jede Verarbeitung. ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX%3A32016R0679))

## 6. Wie Schutzbedarf Architekturentscheidungen beeinflusst

### 6.1 IAM

Bei normalem Schutzbedarf reicht häufig ein solides Rollenmodell mit Standard-MFA, sauberem Joiner-Mover-Leaver-Prozess und Protokollierung administrativer Änderungen. Bei hohem Schutzbedarf brauchst du rollen- oder attributbasierte Zugriffskontrolle, Need-to-know, Funktionstrennung, regelmäßige Rezertifizierung, starke Authentifizierung, technische Service-Identitäten, keine Sammelkonten und nachvollziehbare Berechtigungsentscheidungen. Bei sehr hohem Schutzbedarf kommen privilegiertes Zugriffsmanagement, Just-in-Time-Rechte, Vier-Augen-Freigaben, Break-Glass-Verfahren, Session Recording und eng kontrollierte Administrationspfade hinzu.

### 6.2 Netzsegmentierung

Schutzbedarf entscheidet, ob Systeme in einfachen Standardzonen laufen dürfen oder ob eine strengere Zonierung erforderlich ist. Ein Portal, ein API-Gateway, eine Fachanwendung, eine Datenbank, ein DMS und eine Registerschnittstelle gehören nicht automatisch in dieselbe Netzwerkzone. Bei hohem Schutzbedarf trennst du Präsentationszone, Applikationszone, Datenzone, Managementzone und Monitoringzugänge. Bei sehr hohem Schutzbedarf prüfst du zusätzlich dedizierte Mandantentrennung, Egress-Kontrolle, Admin-Netze, Jump Hosts und restriktive Ost-West-Kommunikation.

### 6.3 Verschlüsselung

Verschlüsselung ist nicht nur „HTTPS an“. Bei hohem Schutzbedarf erwartest du Transportverschlüsselung, starke Zertifikatsverwaltung, Verschlüsselung ruhender Daten, verschlüsselte Backups und getrennt verwaltete Schlüssel. Bei sehr hohem Schutzbedarf musst du zusätzlich Schlüsselmanagement, HSM/KMS, Schlüsselrotation, Mandantentrennung, Zugriff auf Klartextdaten und Notfallzugriffe prüfen. DSGVO Art. 32 nennt Verschlüsselung ausdrücklich als mögliche Maßnahme zur Sicherheit der Verarbeitung. ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX%3A32016R0679))

### 6.4 Logging

Logging ist bei Schutzbedarf ambivalent. Für Integrität, Nachvollziehbarkeit und Incident Response brauchst du Logs. Für Vertraulichkeit und Datenschutz dürfen Logs aber keine unnötigen personenbezogenen Inhalte, Geheimnisse, Tokens oder vollständigen Fachpayloads enthalten. Bei hohem Schutzbedarf verlangst du manipulationsgeschützte Audit Logs, Zeitstempel, Korrelations-IDs, Zugriffsauswertungen, Aufbewahrungskonzepte und geregelte Logeinsicht. Bei sehr hohem Schutzbedarf prüfst du zentrale, unveränderbare Logablage, SIEM-Anbindung, Alarmregeln und regelmäßige Auswertung.

### 6.5 Backup und Wiederanlauf

Verfügbarkeit ist ohne Backup- und Restore-Nachweis wertlos. Schutzbedarf muss in RTO und RPO übersetzt werden. RTO beantwortet: Wie schnell muss das Verfahren wieder laufen? RPO beantwortet: Wie viel Datenverlust ist maximal tolerierbar? Bei hohem Schutzbedarf brauchst du regelmäßige Backups, verschlüsselte Backupablage, Restore-Tests, dokumentierte Wiederanlaufverfahren und klare Verantwortlichkeiten. Bei sehr hohem Schutzbedarf brauchst du zusätzlich Notbetrieb, Disaster-Recovery-Szenarien, getrennte Backup-Domänen, Schutz gegen Ransomware und geübte Wiederanlaufverfahren.

### 6.6 Monitoring

Monitoring folgt aus Verfügbarkeit und Integrität. Bei hohem Schutzbedarf reicht es nicht, nur Server-CPU und Speicher zu überwachen. Du brauchst fachliche und technische Signale: Antwortzeiten, Fehlerraten, Schnittstellenverfügbarkeit, Queue-Längen, Registerantworten, DMS-Latenz, Login-Fehler, ungewöhnliche Zugriffsmuster und erfolgreiche Verarbeitung von Kerntransaktionen. Bei sehr hohem Schutzbedarf brauchst du proaktive Alarmierung, SLOs, Eskalationsketten, Bereitschaftsmodell und getestete Runbooks.

### 6.7 Dienstleisterzugriff

Dienstleisterzugriffe sind architektonisch kritisch, weil sie oft technische Macht mit organisatorischer Distanz kombinieren. Bei hohem Schutzbedarf müssen externe Zugriffe genehmigt, befristet, personenbezogen, protokolliert und regelmäßig geprüft werden. Produktivzugriffe sollten über MFA, Jump Host, privilegiertes Zugriffsmanagement, Session-Protokollierung und klare Verantwortlichkeit laufen. Datenschutzrechtlich sind bei personenbezogener Verarbeitung Verantwortlichkeiten, Auftragsverarbeitung, Weisungsbindung und technische/organisatorische Maßnahmen relevant; Art. 32 DSGVO fordert ein angemessenes Schutzniveau, der BfDI betont diese Verbindung zur IT-Sicherheit in der Bundesverwaltung. ([bfdi.bund.de](https://www.bfdi.bund.de/SharedDocs/Downloads/DE/Broschueren/INFO6.pdf?__blob=publicationFile&v=11))

## 7. Schutzbedarfsraster für Architekturreviews

| Aspekt | Details/Erklärung | Leitfrage | Mögliche Architekturbedingung |
|---|---|---|---|
| Zielobjekt | Was genau wird bewertet? | Bewerten wir Daten, Prozess, Anwendung, Schnittstelle, Plattform oder Dienstleisterzugang? | Jedes Zielobjekt erhält eigene CIA-Bewertung mit Begründung. |
| Vertraulichkeit | Schaden bei unbefugter Offenlegung. | Wer wäre betroffen, wenn diese Information öffentlich, intern breit sichtbar oder einem Dienstleister zugänglich würde? | Need-to-know, Verschlüsselung, Protokollierung, Datenminimierung, Zugriffstrennung. |
| Integrität | Schaden bei Manipulation, Fehler, Verlust von Nachvollziehbarkeit. | Welche falsche Entscheidung, Zahlung, Rechtsfolge oder Statistik könnte entstehen? | Vier-Augen-Prinzip, Signatur, Validierung, Versionierung, Audit Trail, fachliche Plausibilisierung. |
| Verfügbarkeit | Schaden bei Ausfall oder Verzögerung. | Welche Frist, Aufgabe, Bürgerleistung oder Folgekette bricht bei Ausfall? | RTO/RPO, HA, Backup, Notbetrieb, Monitoring, Eskalation. |
| Kumulation | Schaden durch Menge und Verknüpfung. | Werden viele Datensätze, mehrere Behördenquellen oder Historien zusammengeführt? | Separierung, restriktive Auswertung, Datenschutzprüfung, besondere Datenbankkontrollen. |
| Schnittstellenwirkung | Schaden durch fehlerhafte oder nicht verfügbare Datenflüsse. | Welche Folgeprozesse verlassen sich auf diese Schnittstelle? | mTLS, Schema-Validierung, Retry/Circuit Breaker, Schnittstellenmonitoring, Fehlersemantik. |
| Betriebsmodell | Schaden durch unklare Verantwortung. | Wer erkennt, bewertet und behebt Störungen oder Sicherheitsereignisse? | Betriebsübergabe, Runbooks, Incidentprozess, SLAs, Bereitschaft. |
| Nachweisfähigkeit | Belegbarkeit von Entscheidungen und Zugriffen. | Können wir später nachweisen, wer was wann warum getan hat? | Audit Logs, Berechtigungsnachweise, Reviewprotokolle, revisionsfähige Ablage. |
| Dienstleister | Externe Machtpositionen und Lieferkettenrisiken. | Welche externen Parteien haben Zugriff auf Produktivdaten, Plattformen oder Schlüssel? | AVV, JIT-Zugriff, PAM, Session Recording, Subdienstleisterprüfung. |
| Restrisiko | Akzeptierte Lücke zwischen Schutzbedarf und Maßnahme. | Wer trägt welches Restrisiko bewusst? | Risikoentscheidung mit Owner, Frist, Maßnahme, Managementfreigabe. |

## 8. Interviewfragen für Fachbereich, Betrieb, Security und Datenschutz

| Aspekt | Details/Erklärung | Konkrete Fragen |
|---|---|---|
| Fachlicher Schaden | Der Fachbereich muss Schaden beschreiben, nicht Technik. | Was passiert, wenn ein Bescheid falsch erzeugt wird? Welche Fristen sind kritisch? Welche Personengruppen wären betroffen? Welche Entscheidung wäre nicht mehr belastbar? |
| Datenkontext | Datenart, Menge, Verknüpfung und Sensibilität bestimmen Vertraulichkeit. | Welche Datenarten werden verarbeitet? Gibt es besondere Kategorien, Kinder, Schutzkontexte, Massenverarbeitung, Registerdaten oder Historien? Können Daten kombiniert Personenprofile ergeben? |
| Integritätsfolgen | Integrität betrifft Rechtswirkung und Entscheidungsqualität. | Welche Daten sind führend? Wo entstehen autoritative Entscheidungen? Wer darf Daten ändern? Wie werden Änderungen erkannt? Gibt es Vier-Augen-Prinzip oder Freigabelogik? |
| Verfügbarkeitsfolgen | Verfügbarkeit muss fachlich in Zeit übersetzt werden. | Wie lange darf der Prozess ausfallen? Was passiert nach 1 Stunde, 4 Stunden, 1 Tag, 3 Tagen? Gibt es manuellen Notbetrieb? Welche Rückstände entstehen? |
| Schnittstellenabhängigkeit | Behördenverfahren sind oft Ketten. | Welche Systeme müssen erreichbar sein? Was passiert, wenn Register, DMS, IAM, API-Gateway oder Datenbank ausfallen? Gibt es Fallbacks? |
| IAM | Rechte sind Architektur, nicht nur Administration. | Wer darf lesen, ändern, freigeben, exportieren, administrieren? Gibt es Funktionstrennung? Wie werden Rollen rezertifiziert? Wie werden Dienstleisterrechte beendet? |
| Logging | Logs müssen Nutzen und Datenschutz ausbalancieren. | Welche Ereignisse sind nachweispflichtig? Welche Logs enthalten personenbezogene Daten? Wer darf Logs lesen? Sind Logs manipulationsgeschützt? |
| Backup/Restore | Backup ohne Restore-Test ist nur Hoffnung. | Wann wurde zuletzt wiederhergestellt? Welche Datenstände sind wiederherstellbar? Sind Backups gegen Ransomware geschützt? Sind Schlüssel separat gesichert? |
| Dienstleister | Externe Zugriffe müssen steuerbar sein. | Wer hat Produktivzugriff? Erfolgt Zugriff personenbezogen? Gibt es MFA, Freigabe, Protokollierung, zeitliche Begrenzung, Subdienstleisterübersicht? |
| Risikoentscheidung | Hoher Schutzbedarf braucht bewusste Steuerung. | Welche Risiken bleiben offen? Wer akzeptiert sie? Bis wann werden Maßnahmen umgesetzt? Welche Abnahmebedingung gilt? |

## 9. Beispielbewertung: Behördenfachverfahren mit Portal, API-Gateway, Fachanwendung, Datenbank, Register, DMS, Monitoring und Dienstleister

Angenommen wird ein Fachverfahren, in dem Bürger über ein Portal Anträge stellen. Das Portal ruft über ein API-Gateway eine Fachanwendung auf. Die Fachanwendung speichert Vorgangsdaten in einer Datenbank, ruft Registerdaten ab, erzeugt Bescheide, legt Dokumente im DMS ab und sendet Betriebsdaten an Monitoring und Logging. Ein externer Dienstleister unterstützt Betrieb und Fehleranalyse.

| Aspekt | Details/Erklärung | Bewertung | Architekturfolge |
|---|---|---|---|
| Portal | Exponierter Zugang für Bürger; verarbeitet Authentifizierung, Antragseingaben und Statusinformationen. | C: hoch, I: hoch, V: hoch | Starke Authentifizierung, sichere Sessionsteuerung, WAF/API-Schutz, Barrierefreiheit, Rate Limits, Monitoring. |
| API-Gateway | Zentraler Kontrollpunkt für Aufrufe, Authentisierung, Autorisierung, Routing und Protokollierung. | C: hoch, I: hoch, V: hoch | OAuth2/OIDC-Prüfung, mTLS intern, Schema-Validierung, zentrale Policies, keine sensiblen Payload-Logs. |
| Fachanwendung | Trägt fachliche Entscheidung, Workflow, Bescheiderstellung und Statuslogik. | C: hoch, I: sehr hoch, V: hoch | Rollenmodell, Vier-Augen-Freigabe, fachliche Validierungen, Audit Trail, Release-Gates, Testnachweise. |
| Datenbank | Kumuliert Vorgänge, personenbezogene Daten, Historie und Entscheidungsgrundlagen. | C: hoch, I: sehr hoch, V: hoch | Verschlüsselung at rest, restriktive Adminrechte, DB-Audit, Backup-Verschlüsselung, Restore-Test. |
| Registerschnittstelle | Liefert autoritative Daten für Entscheidungen. Fehler oder Ausfall beeinflussen Folgeentscheidungen. | C: hoch, I: sehr hoch, V: hoch bis sehr hoch | mTLS, Integritätsschutz, Timeout-/Retry-Konzept, fachliche Fehlercodes, Schnittstellen-SLO. |
| DMS | Speichert Akten, Nachweise, Bescheide, Anlagen und revisionsrelevante Dokumente. | C: hoch, I: sehr hoch, V: hoch | revisionsfähige Ablage, Versionierung, Lösch-/Aufbewahrungskonzept, Zugriffstrennung, Exportkontrolle. |
| Monitoring/Logging | Unterstützt Betrieb, Nachweis und Incident Response; kann selbst sensible Daten enthalten. | C: hoch, I: hoch, V: hoch | zentrale Logplattform, Maskierung, Zugriffsbeschränkung, Manipulationsschutz, Alarmregeln. |
| Dienstleisterzugriff | Externer Zugriff auf Betrieb, Logs oder Produktivsysteme erhöht Steuerungsbedarf. | C: hoch, I: hoch, V: hoch | MFA, Jump Host, JIT-Zugriff, Session Recording, Ticketbindung, AVV, regelmäßige Rechteprüfung. |

Die zusammenfassende Architekturbedingung könnte lauten: „Das Fachverfahren verarbeitet personenbezogene Vorgangs- und Bescheiddaten mit hoher Vertraulichkeit und sehr hoher Integritätsanforderung an Entscheidungs- und Bescheiddaten. Die Architektur muss deshalb eine durchgängige Zugriffstrennung, manipulationsgeschützte Nachvollziehbarkeit, Integritätsschutz der Registerkommunikation, getestete Wiederherstellbarkeit, restriktive Dienstleisterzugriffe und fachliches Monitoring nachweisen. Abweichungen sind als Restrisiko mit Owner, Frist und Kompensationsmaßnahme zu dokumentieren.“

## 10. Typische Fehler bei Schutzbedarfsfeststellungen

| Aspekt | Details/Erklärung | Korrektur |
|---|---|---|
| Pauschalbewertung | „Das System ist hoch“ ist zu ungenau. | Immer je Grundwert bewerten: C, I, V getrennt. |
| Technik vor Schaden | Teams diskutieren Verschlüsselung, bevor der Schaden verstanden ist. | Erst Schadensszenario, dann Architekturmaßnahme. |
| Personenbezug falsch behandelt | Entweder wird jeder Personenbezug automatisch maximal bewertet oder unterschätzt. | Art, Umfang, Kontext, Menge, Verknüpfung und Folgen betrachten. |
| Integrität unterschätzt | Viele Teams fokussieren Vertraulichkeit und vergessen falsche Entscheidungen. | Bei Bescheiden, Registern, Berichten und Zahlungen Integrität explizit prüfen. |
| Verfügbarkeit technisch verkürzt | „99,5 % Uptime“ ersetzt keine fachliche Ausfallanalyse. | RTO/RPO aus Prozessfolgen ableiten. |
| Schnittstellen vergessen | Schutzbedarf endet fälschlich an der Anwendung. | Datenflüsse, APIs, Register, DMS, IAM und Monitoring einbeziehen. |
| Logs als harmlos betrachtet | Logs enthalten oft IDs, Fehlerdetails, Nutzerdaten oder Tokens. | Logdaten klassifizieren, minimieren, schützen und auswerten. |
| Dienstleister zu spät bewertet | Externe Zugriffe werden erst im Betrieb geklärt. | Dienstleisterzugriff als Architektur- und Abnahmekriterium behandeln. |
| Keine Nachweisführung | Bewertung wird mündlich getroffen und später nicht mehr verstanden. | Entscheidung, Begründung, Annahmen, Owner und Reviewdatum dokumentieren. |
| Keine Risikoanalyse bei hohem Schutzbedarf | Hoher Schutzbedarf wird festgestellt, aber Maßnahmen bleiben Standard. | Bei hoch/sehr hoch Risikoanalyse, Sondermaßnahmen und Managemententscheidung prüfen. |

## 11. Formulierungen, mit denen du auf Augenhöhe sprichst

Ein guter Satz im Architekturreview lautet nicht: „Wir brauchen mehr Security.“ Ein guter Satz lautet: „Für die Bescheiderstellung bewerten wir Integrität als sehr hoch, weil manipulierte oder fehlerhafte Bescheide unmittelbare Rechtsfolgen erzeugen können. Daraus folgen verpflichtende fachliche Validierung, Vier-Augen-Freigabe, Versionierung, manipulationsgeschützter Audit Trail und ein nachgewiesener Wiederherstellungspfad.“

Für Schnittstellen sagst du nicht: „Die API muss sicher sein.“ Du sagst: „Die Registerschnittstelle verarbeitet autoritative Daten mit hoher Vertraulichkeit und sehr hoher Integritätsrelevanz. Deshalb sind technische Service-Identitäten, mTLS, Schema-Validierung, fachliche Fehlersemantik, Korrelations-IDs, Monitoring und ein dokumentierter Umgang mit widersprüchlichen Registerantworten erforderlich.“

Für Dienstleister sagst du nicht: „Der Dienstleister soll Zugriff bekommen.“ Du sagst: „Produktivzugriffe externer Dienstleister sind wegen des hohen Schutzbedarfs personenbezogen, zeitlich begrenzt, MFA-geschützt, ticketgebunden, protokolliert und regelmäßig zu rezertifizieren. Sammelkonten und dauerhafte Volladministration sind nicht akzeptabel, sofern keine begründete Ausnahme mit Kompensation vorliegt.“

## 12. Übung: Schutzbedarf selbst bewerten

Nimm folgendes Szenario: Eine Bundesbehörde betreibt ein Fachverfahren zur Bearbeitung von Anträgen. Bürger reichen online Anträge ein. Sachbearbeiter prüfen die Vorgänge, rufen Registerdaten ab, erzeugen Bescheide und speichern Dokumente im DMS. Ein externer Dienstleister hat Supportzugriff auf die Produktionsumgebung. Das Management erhält wöchentliche Berichte aus aggregierten Vorgangsdaten.

Bearbeite die Übung in fünf Schritten. Erstens bestimmst du die Zielobjekte: Portal, Fachanwendung, Datenbank, Registerschnittstelle, DMS, Reporting, IAM, Logging, Dienstleisterzugriff. Zweitens bewertest du je Zielobjekt Vertraulichkeit, Integrität und Verfügbarkeit mit normal, hoch oder sehr hoch. Drittens begründest du jede Bewertung mit einem Schadensszenario. Viertens leitest du je Zielobjekt mindestens drei Architekturbedingungen ab. Fünftens formulierst du drei offene Risiken, die du mit Security, Datenschutz, Fachbereich und Betrieb klären würdest.

Eine starke Musterantwort beginnt beispielsweise so: „Für die Vorgangsdatenbank wird Vertraulichkeit als hoch bewertet, weil personenbezogene Vorgangs- und Nachweisdaten in größerem Umfang gespeichert werden. Integrität wird als sehr hoch bewertet, weil falsche oder manipulierte Daten zu fehlerhaften Bescheiden führen können. Verfügbarkeit wird als hoch bewertet, weil Ausfälle die Bearbeitung gesetzlicher Fristen und den Bürgerzugang beeinträchtigen. Daraus folgen Verschlüsselung ruhender Daten, restriktive Administrationsrechte, Datenbank-Auditing, regelmäßige Restore-Tests, Zugriff über Fachrollen statt Direktzugriff und ein dokumentiertes Notfallverfahren.“

## 13. Deine Architekten-Merksätze

Schutzbedarf ist die Übersetzung von Schaden in Architektur. Vertraulichkeit schützt vor unbefugter Kenntnisnahme. Integrität schützt vor falschen, manipulierten oder nicht nachweisbaren Entscheidungen. Verfügbarkeit schützt die rechtzeitige Erfüllung der Aufgabe. In Behörden ist Integrität häufig genauso kritisch wie Vertraulichkeit, manchmal sogar kritischer. Eine Registerauskunft, ein Bescheid oder ein Bericht muss nicht nur verborgen bleiben, sondern vor allem stimmen.

Der professionelle Architekt fragt deshalb nicht nur: „Welche Daten sind sensibel?“ Er fragt: „Welche Entscheidung hängt daran? Welche Frist hängt daran? Welche Person ist betroffen? Welche Behörde verlässt sich darauf? Welche Folgeprozesse werden falsch gesteuert? Welche Nachweise brauchen wir später? Wer darf im Notfall eingreifen? Und welche Maßnahmen sind zwingend, weil der Schutzbedarf sie verlangt?“

<>