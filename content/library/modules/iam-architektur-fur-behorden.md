## Checkliste: IAM als Enterprise-Architekt sauber prüfen

1. Ist klar, **welche Identitäten** existieren: interne Mitarbeitende, externe Antragstellende, Dienstleister, Admins, technische Konten, Systeme, Schnittstellen, Bots und Jobs?  
2. Ist getrennt zwischen **Authentifizierung**: „Wer bist du?“ und **Autorisierung**: „Was darfst du hier tun?“  
3. Gibt es ein fachlich verständliches **Rollenmodell** statt historisch gewachsener Einzelrechte?  
4. Sind Rollen nach **Aufgabe, Organisationseinheit, Verfahren, Datenobjekt, Schutzbedarf und Umgebung** strukturiert?  
5. Wird **Least Privilege** konsequent umgesetzt: nur so viele Rechte wie nötig, nur so lange wie nötig, nur im richtigen Kontext?  
6. Sind **technische Konten und Service Accounts** vollständig sichtbar, zweckgebunden, geheimnisverwaltet, rotiert und auditierbar?  
7. Sind **Privilegien** für Administration, Datenbankzugriff, Produktivsysteme und Plattformen besonders geschützt?  
8. Sind **SSO, MFA, Federation, OAuth2, OpenID Connect und SAML** fachlich korrekt eingeordnet und nicht vermischt?  
9. Gibt es **Rezertifizierung**, also regelmäßige fachliche Überprüfung bestehender Berechtigungen?  
10. Gibt es definierte Prozesse für **Joiner, Mover, Leaver**, Delegation, Vertretung, Vier-Augen-Freigaben und Notfallzugriffe?  
11. Sind **Audit Logs** beweissicher genug, um Zugriffe, Berechtigungsänderungen, Adminhandlungen und Schnittstellenzugriffe nachvollziehbar zu machen?  
12. Sind IAM-Anforderungen als **Architekturbedingung** im Zielbild formuliert: verbindlich, prüfbar, betreibbar und abnahmefähig?

<>

## 1. Grundgedanke: IAM ist kein Login-Thema, sondern ein Architekturthema

Identity and Access Management, kurz IAM, ist die architektonische Antwort auf eine scheinbar einfache Frage: **Wer oder was darf unter welchen Bedingungen auf welche Informationen, Funktionen, Systeme und Schnittstellen zugreifen?** In Behörden ist diese Frage besonders kritisch, weil Fachverfahren häufig personenbezogene Daten, Registerdaten, Vorgangsdaten, Bescheide, interne Vermerke, Fristen, Zahlungsinformationen und sensible Kommunikationsdaten verarbeiten. Ein falsches Berechtigungsmodell ist deshalb nicht nur ein technischer Mangel, sondern ein Risiko für Vertraulichkeit, Integrität, Nachvollziehbarkeit, Betriebsfähigkeit und rechtssichere Verfahrensführung.

Das BSI behandelt Identitäts- und Berechtigungsmanagement im IT-Grundschutz ausdrücklich als eigenen Baustein. Ziel ist, dass Benutzende und IT-Komponenten nur auf die Ressourcen und Informationen zugreifen können, für die sie berechtigt sind. Genau diese Formulierung ist für dich als Enterprise Architekt entscheidend: Nicht nur Menschen haben Identitäten, sondern auch Anwendungen, Schnittstellen, Dienste, Jobs, Container, API-Clients, Datenbankverbindungen und Plattformkomponenten. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/02_ORP_Organisation_und_Personal/ORP_4_Identitaets_und_Berechtigungsmanagement_Editon_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com))

Die NIST Digital Identity Guidelines SP 800-63-4 wurden im Juli 2025 final veröffentlicht und strukturieren digitale Identität entlang von Identity Proofing, Authentication und Federation. Für Behördenarchitektur ist das wertvoll, weil es zeigt: IAM besteht nicht aus einem einzelnen Login-Mechanismus, sondern aus einem zusammenhängenden Vertrauensmodell aus Identitätsfeststellung, Authentifizierung, Authenticator Management, Federation und Assertions. ([pages.nist.gov](https://pages.nist.gov/800-63-4/))

OWASP ASVS ist für dich wichtig, weil IAM-Anforderungen dort als prüfbare Anwendungssicherheitsanforderungen behandelt werden. ASVS liefert keine Behördenarchitektur, aber es liefert eine gute technische Kontrollsicht für Authentifizierung, Sitzungsmanagement und Zugriffskontrolle in Webanwendungen und APIs. Die aktuelle OWASP-Seite verweist auf ASVS 5.0.0 als stabile Version und beschreibt ASVS als Grundlage für testbare Sicherheitsanforderungen, auch in Beschaffung und Verträgen. ([owasp.org](https://owasp.org/www-project-application-security-verification-standard/))

## 2. Das mentale Modell: Identität, Authentifizierung, Autorisierung, Nachweis

Wenn du IAM prüfen willst, musst du vier Ebenen sauber trennen. Die erste Ebene ist die **Identität**. Eine Identität beschreibt eine Person, Organisation, Maschine oder technische Entität eindeutig genug, damit ein System sie unterscheiden und verwalten kann. Beispiele sind eine interne Benutzerkennung, ein Bürgerkonto, ein Dienstleisterkonto, ein Service Account, ein API-Client oder eine Workload Identity in Kubernetes.

Die zweite Ebene ist die **Authentifizierung**. Sie beantwortet die Frage: **Wie weist diese Identität nach, dass sie wirklich diese Identität ist?** Das kann über Passwort, Smartcard, Zertifikat, Passkey, MFA, Client-Zertifikat, SAML Assertion, OIDC ID Token oder mTLS erfolgen. NIST SP 800-63-4 behandelt hierfür Authenticatoren, Authenticator Management und Assurance Levels. ([pages.nist.gov](https://pages.nist.gov/800-63-4/))

Die dritte Ebene ist die **Autorisierung**. Sie beantwortet die Frage: **Welche Handlung ist dieser Identität jetzt erlaubt?** Typische Entscheidungen sind Lesen, Erstellen, Ändern, Löschen, Freigeben, Exportieren, Administrieren, Stellvertreten, Bescheid erzeugen, Vorgang abschließen oder Protokolle einsehen. Genau hier entstehen die meisten Architekturfehler, weil Projekte Login mit Berechtigung verwechseln.

Die vierte Ebene ist **Nachvollziehbarkeit**. Sie beantwortet die Frage: **Kann später fachlich, technisch und revisionssicher nachvollzogen werden, wer oder was wann warum worauf zugegriffen hat?** Das betrifft Audit Logs, Admin Logs, Berechtigungsänderungen, Token-Ausstellungen, fehlgeschlagene Loginversuche, Rollenänderungen, Vier-Augen-Freigaben, Notfallzugriffe und Service-Account-Nutzung.

## 3. Die wichtigsten Begriffe sauber erklärt

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Identität | Eindeutige digitale Repräsentation einer Person, Organisation, Anwendung, Maschine oder technischen Komponente. | „sachbearbeiter123“, „externes-portal-client-prod“, „batch-register-sync“. | BSI ORP.4 betrachtet Benutzende und IT-Komponenten als zugriffsrelevante Entitäten. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/02_ORP_Organisation_und_Personal/ORP_4_Identitaets_und_Berechtigungsmanagement_Editon_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Authentifizierung | Nachweis, dass eine Identität tatsächlich genutzt wird. | Anmeldung mit Smartcard und PIN, MFA, OIDC Login, Client-Zertifikat. | NIST SP 800-63-4 behandelt Authentifizierung und Authenticator Management. ([pages.nist.gov](https://pages.nist.gov/800-63-4/)) |
| Autorisierung | Entscheidung, welche Funktion, Datenmenge oder Schnittstelle genutzt werden darf. | Sachbearbeitung darf Vorgang bearbeiten, aber keinen Adminexport starten. | OWASP ASVS behandelt Zugriffskontrolle als prüfbare Anwendungssicherheitsanforderung. ([owasp.org](https://owasp.org/www-project-application-security-verification-standard/)) |
| RBAC | Role Based Access Control: Rechte werden über Rollen gebündelt. | Rolle „Sachbearbeitung Aufenthalt“ enthält Lesen, Bearbeiten, Dokument hochladen. | Fachlich etablierter IAM-Ansatz; im Behördenkontext gut steuerbar, wenn Rollen sauber geschnitten sind. |
| ABAC | Attribute Based Access Control: Zugriff hängt zusätzlich von Attributen ab. | Zugriff nur auf Vorgänge der eigenen Organisationseinheit, Region oder Zuständigkeit. | Nützlich bei komplexen Behördenzuständigkeiten und dynamischen Kontexten. |
| SSO | Single Sign-On: eine Authentifizierung ermöglicht Zugriff auf mehrere Dienste. | Behördennutzer meldet sich zentral an und nutzt Portal, DMS und Fachverfahren. | OIDC und SAML sind typische SSO-/Federation-Technologien. ([openid.net](https://openid.net/specs/openid-connect-core-1_0-final.html?utm_source=chatgpt.com)) |
| MFA | Multi-Factor Authentication: mehrere unabhängige Faktoren erhöhen die Sicherheit. | Passwort plus FIDO2-Key oder Smartcard plus PIN. | NIST SP 800-63-4 behandelt Authenticatoren und Authentifizierungsanforderungen. ([pages.nist.gov](https://pages.nist.gov/800-63-4/)) |
| Federation | Vertrauensbeziehung zwischen Identity Provider und Anwendung/Service Provider. | Externe Antragstellende melden sich über ein Bürgerkonto an; Fachverfahren vertraut dem Identity Provider. | NIST SP 800-63-4 enthält einen eigenen Teil zu Federation & Assertions. ([pages.nist.gov](https://pages.nist.gov/800-63-4/)) |
| OAuth2 | Autorisierungsframework, besonders für API-Zugriffe und Delegation. Nicht primär Login. | Portal erhält Access Token, um eine API aufzurufen. | RFC 9700 beschreibt aktuelle OAuth2-Sicherheitspraxis und aktualisiert frühere OAuth-Security-Empfehlungen. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/rfc9700/)) |
| OpenID Connect | Authentifizierungsschicht auf OAuth2; liefert unter anderem ID Tokens mit Claims über die Authentifizierung. | Webanwendung erhält ID Token und weiß, welcher Nutzer authentifiziert wurde. | OpenID Connect Core definiert das ID Token als Token mit Claims über die Authentifizierung eines End-Users. ([openid.net](https://openid.net/specs/openid-connect-core-1_0-final.html?utm_source=chatgpt.com)) |
| SAML | XML-basiertes Framework für Assertions über Authentifizierung, Attribute und Autorisierung. | Klassisches Behörden-/Enterprise-SSO zwischen Identity Provider und Fachanwendung. | OASIS beschreibt SAML 2.0 als Standard für XML-kodierte Assertions über Authentication, Attributes und Authorization. ([oasis-open.org](https://www.oasis-open.org/standard/saml/?utm_source=chatgpt.com)) |
| Technisches Konto | Konto ohne natürliche Person als direkte Benutzerin; wird von Systemen, Jobs oder Diensten verwendet. | Datenbankkonto einer Anwendung, API-Client, Batch-User. | BSI ORP.4 bezieht IT-Komponenten ausdrücklich ein. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/02_ORP_Organisation_und_Personal/ORP_4_Identitaets_und_Berechtigungsmanagement_Editon_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Service Account | Spezielle technische Identität für Dienste, Prozesse oder Workloads. | Kubernetes Workload ruft Register-API mit eigener Identität auf. | Architektonisch relevant wegen Geheimnissen, Rotation, Scope und Nachvollziehbarkeit. |
| PAM | Privileged Access Management für besonders mächtige Konten und Aktionen. | Adminzugriff nur zeitlich befristet, genehmigt, protokolliert und mit MFA. | Steht im Zusammenhang mit Least Privilege, Need-to-know und kontrollierter Administration. |
| Rezertifizierung | Regelmäßige fachliche Überprüfung bestehender Berechtigungen. | Fachvorgesetzte bestätigen quartalsweise Rollen für Sachbearbeitende. | BSI-Grundschutz fordert kontrollierte Zuweisung, Entzug und Überprüfung von Berechtigungen. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2021/02_ORP_Organisation_und_Personal/ORP_4_Identitaets_und_Berechtigungsmanagement_Editon_2021.pdf?__blob=publicationFile&v=2&utm_source=chatgpt.com)) |
| Delegation | Eine Identität handelt befristet im Auftrag einer anderen Rolle oder Organisationseinheit. | Stellvertretung während Urlaub darf Vorgänge bearbeiten, aber keine Rollen vergeben. | Architektonisch nur sauber mit Zeitraum, Grund, Umfang und Protokollierung. |
| Vier-Augen-Prinzip | Kritische Aktion benötigt unabhängige zweite Freigabe. | Bescheidfreigabe, Auszahlung, Rollenvergabe, Datenexport. | Muss fachlich modelliert und technisch erzwungen werden. |
| Audit Logs | Nachvollziehbare Protokolle über sicherheits- und fachrelevante Ereignisse. | Wer hat wann welche Rolle vergeben, welchen Vorgang geöffnet, welchen Export gestartet? | OWASP ASVS unterstützt prüfbare technische Sicherheitskontrollen; BSI fordert nachvollziehbare Zugriffssteuerung. ([owasp.org](https://owasp.org/www-project-application-security-verification-standard/)) |

## 4. Der wichtigste Architekturfehler: Login ist nicht Berechtigung

Ein System kann SSO, MFA und OIDC perfekt implementieren und trotzdem ein schlechtes IAM haben. Warum? Weil Authentifizierung nur feststellt, **wer** da ist. Sie sagt noch nicht, **was diese Identität fachlich tun darf**.

In Behördenprojekten sehe ich gedanklich häufig diesen Fehler: „Wir hängen das Fachverfahren an den zentralen Identity Provider, damit ist IAM erledigt.“ Das ist falsch. Damit ist höchstens die zentrale Anmeldung gelöst. Danach braucht das Fachverfahren weiterhin ein fachliches Berechtigungsmodell, Rollen, Attribute, Zuständigkeitslogik, Mandantentrennung, technische Konten, Admintrennung, Rezertifizierung und Auditierbarkeit.

Die bessere Architekturfrage lautet also nicht: **„Haben wir SSO?“** Die bessere Frage lautet: **„Welche fachliche Entscheidung trifft welches System auf Basis welcher Identität, welcher Rolle, welcher Attribute und welcher Vertrauensquelle?“**

## 5. Behördenbeispiel: Fachverfahren „Antrags- und Vorgangsbearbeitung“

Nehmen wir ein realistisches Behördenverfahren. Externe Antragstellende nutzen ein Online-Portal, authentifizieren sich über ein Bürgerkonto oder eine andere föderierte Identität und stellen Anträge. Interne Sachbearbeitende bearbeiten Vorgänge. Fachaufsicht prüft Entscheidungen, erstellt Auswertungen und kontrolliert Qualität. Administratoren betreiben Plattform, Anwendung, Datenbank und Schnittstellen. Ein externer Dienstleister unterstützt Betrieb und Entwicklung. Technische Systemkonten verbinden Portal, API-Gateway, Fachverfahren, DMS, Registerschnittstelle, Monitoring und Datenbank.

Architektonisch besteht das System aus Identity Provider, Portal, API-Gateway, Fachanwendung, Rollen- und Berechtigungsdienst, Datenbank, DMS, Registerschnittstelle, Logging-/SIEM-Plattform, Monitoring und Administrationszugängen. Genau an diesen Übergängen entstehen IAM-Fragen.

Ein externer Antragsteller darf eigene Anträge erstellen, eigene Dokumente hochladen und eigene Bescheide lesen. Er darf aber keine fremden Vorgänge sehen, keine internen Vermerke lesen, keine Sachbearbeitungsnotizen verändern und keine Registerabfragen auslösen. Eine Sachbearbeiterin darf Vorgänge ihrer Zuständigkeit lesen und bearbeiten, aber nicht beliebig alle Vorgänge aller Organisationseinheiten exportieren. Eine Fachaufsicht darf prüfen, freigeben und aggregierte Berichte sehen, aber nicht zwangsläufig produktive Systemkonfiguration ändern. Ein Administrator darf Plattform und Anwendung betreiben, sollte aber fachliche Vorgangsdaten nicht ohne kontrollierten Anlass einsehen können. Ein Dienstleister darf produktionsnah analysieren, aber nicht dauerhaft unkontrolliert mit globalen Adminrechten arbeiten. Technische Konten dürfen exakt die Schnittstellen nutzen, für die sie vorgesehen sind, nicht mehr.

## 6. Rollenmodell-Vorlage für Behördenverfahren

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Rollenname | Fachlich verständlicher Name, nicht technischer Gruppenname. | „Sachbearbeitung Antrag“, nicht „APP_X_GRP_4711“. | BSI ORP.4 verlangt steuerbare Zugriffsbeschränkung auf berechtigte Benutzende und IT-Komponenten. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/02_ORP_Organisation_und_Personal/ORP_4_Identitaets_und_Berechtigungsmanagement_Editon_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Rollentyp | Fachrolle, technische Rolle, Adminrolle, Prüferrolle, Vertretungsrolle, Systemrolle. | Fachrolle „Sachbearbeitung“, technische Rolle „API-Client DMS“. | Trennung verhindert Rollenvermischung und Überprivilegierung. |
| Träger der Rolle | Wer oder was kann diese Rolle erhalten? | Mitarbeitende, Dienstleister, Service Account, Fachaufsicht. | NIST SP 800-63-4 bezieht Nutzergruppen wie Beschäftigte, Vertragspartner und private Personen in digitale Identitätsmodelle ein. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/63/4/final?utm_source=chatgpt.com)) |
| Zweck | Warum existiert diese Rolle fachlich? | Bearbeitung von Vorgängen im Zuständigkeitsbereich. | Zweckbindung erleichtert Rezertifizierung und Abnahme. |
| Berechtigungen | Konkrete Aktionen auf konkrete Objekte. | Vorgang lesen, Dokument hochladen, Bescheid freigeben. | OWASP ASVS unterstützt testbare Zugriffskontrollanforderungen. ([owasp.org](https://owasp.org/www-project-application-security-verification-standard/)) |
| Datenumfang | Welche Daten darf die Rolle sehen oder verändern? | Nur eigene Vorgänge, eigene Organisationseinheit, bestimmte Schutzbedarfsklasse. | ABAC kann Datenumfang über Attribute begrenzen. |
| Kontextattribute | Zusätzliche Bedingungen für Zugriff. | Dienststelle, Region, Verfahren, Schutzbedarf, Uhrzeit, Netzwerkzone, Gerätestatus. | NIST SP 800-63-4 betont risikoorientierten Kontext und Assurance Levels. ([pages.nist.gov](https://pages.nist.gov/800-63-4/)) |
| Genehmiger | Wer darf die Rolle vergeben? | Fachvorgesetzte, Verfahrensverantwortung, IAM-Team. | Rezertifizierung und Genehmigung sind zentrale Governance-Mechanismen. |
| Gültigkeit | Befristung, Start, Ende, Vertretungszeitraum. | Dienstleisterrolle gültig bis Projektende; Vertretung bis 30.09.2026. | Least Privilege bedeutet auch zeitliche Begrenzung. |
| Kritikalität | Normal, erhöht, hoch, privilegiert. | Adminrolle und Massendatenexport sind hochkritisch. | BSI-Schutzbedarf beeinflusst Berechtigungstiefe und Kontrollniveau. |
| MFA/PAM-Pflicht | Ob zusätzliche Absicherung erforderlich ist. | Adminrolle nur über PAM, MFA, Session Recording. | NIST und BSI fördern risikoadäquate starke Authentifizierung. ([pages.nist.gov](https://pages.nist.gov/800-63-4/)) |
| Vier-Augen-Pflicht | Ob kritische Aktionen zweite Freigabe benötigen. | Auszahlung, Bescheidfreigabe, Rollenvergabe. | Muss fachlich definiert und technisch kontrolliert werden. |
| Rezertifizierung | Wie oft die Rolle überprüft wird. | Quartalsweise für privilegierte Rollen, halbjährlich für Fachrollen. | BSI-Grundschutz fordert kontrollierte Zuweisung, Entzug und Kontrolle von Rechten. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2021/02_ORP_Organisation_und_Personal/ORP_4_Identitaets_und_Berechtigungsmanagement_Editon_2021.pdf?__blob=publicationFile&v=2&utm_source=chatgpt.com)) |
| Audit Events | Welche Ereignisse protokolliert werden müssen. | Rollenvergabe, Rollenentzug, Export, Adminzugriff, Loginfehler. | Auditierbarkeit ist Teil prüfbarer Sicherheitskontrollen. |
| Ausschlussregeln | Welche Rollen dürfen nicht kombiniert werden? | „Antrag bearbeiten“ und „Antrag final genehmigen“ nicht in derselben Person ohne Kontrollmechanismus. | Segregation of Duties verhindert kritische Rechtekumulation. |

## 7. Beispielrollen für das Behördenverfahren

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Externe Antragstellende | Dürfen eigene Anträge verwalten, aber keine internen Bearbeitungsdaten sehen. | Antrag erstellen, Status sehen, eigene Dokumente hochladen, Bescheid abrufen. | Federation und Identity Proofing sind hier besonders relevant. ([pages.nist.gov](https://pages.nist.gov/800-63-4/)) |
| Interne Sachbearbeitung | Bearbeitet Vorgänge im eigenen Zuständigkeitsbereich. | Vorgang lesen, fachliche Prüfung dokumentieren, Rückfrage stellen. | Zugriff muss rollen- und attributbasiert begrenzt werden. |
| Fachaufsicht | Prüft Qualität, entscheidet Eskalationen, gibt kritische Vorgänge frei. | Bescheidfreigabe, Stichprobenprüfung, Bericht lesen. | Vier-Augen-Prinzip und Audit Logs sind hier zentral. |
| Verfahrensadministration | Verwaltet fachliche Konfiguration, Kataloge, Fristen, Rollenanforderungen. | Fristparameter ändern, Vorlagen verwalten, Rollen beantragen. | Nicht mit technischer Systemadministration vermischen. |
| Technische Administration | Betreibt Anwendung, Plattform, Datenbank, Netz, Monitoring. | Deployment, Konfiguration, Fehleranalyse, Backupprüfung. | PAM, MFA und Protokollierung sind Pflichtkandidaten. |
| Externer Dienstleister | Unterstützt Entwicklung, Betrieb oder Analyse mit begrenztem Zugriff. | Zugriff über Bastion/PAM, keine dauerhaften globalen Adminrechte. | Dienstleisterzugriff braucht Befristung, Zweck, Genehmigung und Logging. |
| API-Gateway-Client | Technische Identität zwischen Portal und Backend. | Access Token mit Scope „antrag:create“. | OAuth2-Sicherheit nach RFC 9700 beachten. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/rfc9700/)) |
| DMS-Service-Account | Fachverfahren legt Dokumente im DMS ab und ruft sie ab. | Dokument schreiben, Metadaten lesen, Akte referenzieren. | Service Accounts dürfen nur zweckgebundene Schnittstellenrechte haben. |
| Registerschnittstellenkonto | Fachverfahren fragt Registerdaten ab. | Registerabfrage nur aus berechtigtem Vorgang heraus. | Zugriff auf Registerdaten braucht starke Nachvollziehbarkeit. |
| Monitoring-/Logging-Konto | Technische Telemetrie, keine fachliche Datenverarbeitung. | Metriken schreiben, Logs lesen, keine Vorgangsdaten exportieren. | Trennung von Betriebsdaten und Fachdaten minimiert Einsichtsrisiken. |
| Break-Glass-Konto | Notfallkonto für kritische Betriebsstörungen. | Nur im Notfall, stark protokolliert, nachträglich geprüft. | Muss selten, kontrolliert und nachvollziehbar genutzt werden. |

## 8. RBAC und ABAC: Wie du Rollenmodelle richtig strukturierst

RBAC ist der Einstieg: Du bündelst Rechte in Rollen. Das ist für Behörden gut, weil Fachbereiche Rollen verstehen können. Eine Rolle wie „Sachbearbeitung Aufenthalt – Lesen/Bearbeiten“ ist besser prüfbar als 73 Einzelrechte. Aber reines RBAC reicht oft nicht aus, weil Behördenzugriffe nicht nur von der Rolle abhängen, sondern auch von Zuständigkeit, Organisationseinheit, Region, Falltyp, Schutzbedarf, Verfahrensstand oder Vertretung.

Deshalb brauchst du meistens eine Kombination aus RBAC und ABAC. RBAC beantwortet: **Welche fachliche Funktion hat die Person?** ABAC beantwortet: **Unter welchen Bedingungen darf diese Funktion auf genau diesen Vorgang angewendet werden?**

Ein gutes Beispiel: Die Rolle „Sachbearbeitung“ darf grundsätzlich Vorgänge bearbeiten. Das Attribut „Dienststelle Leer“ begrenzt den Zugriff auf Vorgänge dieser Dienststelle. Das Attribut „Team Asylverfahren“ begrenzt fachlich weiter. Das Attribut „Vertretung aktiv bis 15.08.2026“ erlaubt befristeten Zugriff auf Vorgänge eines anderen Teams. Das Attribut „Schutzbedarf hoch“ erzwingt zusätzliche Freigabe oder Einsichtsbeschränkung.

Die Architektenfrage lautet hier: **Wo liegt die Autorisierungsentscheidung?** In der Anwendung? Im API-Gateway? In einem Policy Decision Point? In der Datenbank? In einem zentralen Berechtigungsdienst? Eine robuste Zielarchitektur macht diese Entscheidung explizit und testbar.

## 9. OAuth2, OpenID Connect und SAML richtig einordnen

OAuth2 ist ein Autorisierungsframework. Es wird häufig für API-Zugriffe genutzt: Ein Client erhält ein Access Token und ruft damit eine Resource Server API auf. Der aktuelle OAuth2 Security Best Current Practice RFC 9700 wurde im Januar 2025 veröffentlicht, aktualisiert RFC 6749, RFC 6750 und RFC 6819 und beschreibt moderne Schutzmaßnahmen gegen bekannte Angriffe und unsichere Muster. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/rfc9700/))

OpenID Connect baut auf OAuth2 auf und standardisiert die Übermittlung des Authentifizierungsergebnisses über ein ID Token. Das ID Token enthält Claims über die Authentifizierung des End-Users durch den Authorization Server. Für dich als Architekt heißt das: OIDC ist geeignet, wenn eine Anwendung wissen muss, welcher Nutzer authentifiziert wurde. ([openid.net](https://openid.net/specs/openid-connect-core-1_0-final.html?utm_source=chatgpt.com))

SAML 2.0 ist ein XML-basiertes Framework für Assertions über Authentifizierung, Attribute und Autorisierung. Es ist in Behörden, Hochschulen und großen Enterprise-Umgebungen weiterhin verbreitet, vor allem bei älteren oder klassischen SSO-Integrationen. OASIS beschreibt SAML 2.0 als Standard für XML-kodierte Aussagen über Authentication, Attributes und Authorization sowie die Protokolle zur Übermittlung dieser Informationen. ([oasis-open.org](https://www.oasis-open.org/standard/saml/?utm_source=chatgpt.com))

Der häufigste Denkfehler lautet: „Wir nutzen OAuth, also haben wir Login.“ Präzise ist: OAuth2 gibt einer Anwendung delegierten Zugriff auf Ressourcen. OpenID Connect liefert zusätzlich standardisierte Authentifizierungsinformationen. SAML liefert Assertions in einem XML-basierten SSO-/Federation-Modell. In Zielarchitekturen musst du diese Unterscheidung glasklar formulieren.

## 10. Technische Konten: Der blinde Fleck vieler IAM-Konzepte

Technische Konten sind in Behördenarchitekturen oft gefährlicher als normale Nutzerkonten, weil sie dauerhaft laufen, hohe Rechte haben, selten rezertifiziert werden und manchmal in Konfigurationsdateien, CI/CD-Variablen oder Skripten versteckt sind. Als Enterprise Architekt musst du technische Identitäten aktiv suchen.

Ein technisches Konto ist jedes Konto, das nicht unmittelbar einer natürlichen Person für interaktive Arbeit zugeordnet ist. Dazu gehören Datenbankuser, API-Clients, Batch-User, Deployment-User, Monitoring-User, Backup-User, Kubernetes Service Accounts, Cloud Workload Identities, SMTP-Konten, DMS-Schnittstellenkonten und Registerabfragekonten.

Deine Mindestanforderung lautet: Jedes technische Konto braucht Eigentümer, Zweck, Systembezug, Umgebung, Rechteumfang, Authentisierungsverfahren, Geheimnisablage, Rotationsprozess, Laufzeit, Rezertifizierung, Logging und Notfallverfahren. Konten wie „service“, „admin“, „batch“, „testuser“, „integration“ oder „verfahren_prod“ ohne Eigentümer und Zweckbeschreibung sind rote Flaggen.

## 11. Privileged Access Management: Adminrechte sind kein normales Rollenproblem

PAM betrifft privilegierte Zugriffe. Das sind Zugriffe, mit denen Systeme administriert, Daten großflächig gelesen, Sicherheitskontrollen verändert, Protokolle manipuliert, Rollen vergeben, Backups wiederhergestellt, produktive Datenbanken geöffnet oder Produktivsysteme konfiguriert werden können.

In einer Behördenzielarchitektur darf privilegierter Zugriff nicht dauerhaft, informell und unsichtbar sein. Er sollte über MFA, rollenbasierte Genehmigung, zeitliche Befristung, Just-in-Time-Zugriff, Session Logging, Vier-Augen-Freigabe für besonders kritische Aktionen, Trennung von Alltagskonto und Adminkonto sowie nachgelagerte Kontrolle abgesichert werden.

Ein besonders wichtiger Punkt: Admins müssen Systeme betreiben können, ohne automatisch fachliche Vollsicht auf alle Vorgangsdaten zu erhalten. In der Praxis ist das schwierig, aber architektonisch muss diese Trennung wenigstens als Zielbild, Risiko oder Kompensationsmaßnahme benannt werden. Wenn Betriebspersonal produktive Fachdaten einsehen kann, brauchst du Anlassbezug, Protokollierung, Freigabe, Schulung, Kontrollprozess und technische Minimierung.

## 12. Rezertifizierung: Berechtigungen altern schlecht

Berechtigungen sind nicht statisch. Menschen wechseln Teams, Aufgaben, Projekte, Dienststellen, Rollen und Zuständigkeiten. Dienstleister verlassen Projekte. Technische Konten werden durch neue Schnittstellen ersetzt. Notfallrechte bleiben versehentlich aktiv. Genau deshalb braucht IAM einen Rezertifizierungsprozess.

Rezertifizierung bedeutet: Fachlich verantwortliche Personen bestätigen regelmäßig, dass bestehende Berechtigungen weiterhin notwendig, angemessen und korrekt sind. Für normale Fachrollen kann das halbjährlich oder jährlich ausreichend sein. Für privilegierte Rollen, Dienstleisterzugriffe, technische Konten und Massendatenexportrechte sind kürzere Zyklen sinnvoll, etwa quartalsweise oder anlassbezogen nach Organisationsänderungen.

Eine schlechte Rezertifizierung fragt nur: „Ist der Nutzer noch da?“ Eine gute Rezertifizierung fragt: „Braucht diese Identität diese Rolle für diese Aufgabe in diesem Verfahren, in dieser Organisationseinheit, mit diesem Datenumfang und diesem Schutzbedarf weiterhin?“

## 13. IAM-Review-Checkliste für Architekturprüfungen

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Identitätsinventar | Sind alle menschlichen und technischen Identitäten bekannt? | Mitarbeitende, Antragstellende, Admins, Dienstleister, Service Accounts. | BSI ORP.4 bezieht Benutzende und IT-Komponenten ein. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/02_ORP_Organisation_und_Personal/ORP_4_Identitaets_und_Berechtigungsmanagement_Editon_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Vertrauensquellen | Woher kommt die Identität? | Behördenverzeichnis, Bürgerkonto, Dienstleisterverzeichnis, Zertifikatsstelle. | NIST SP 800-63-4 behandelt Identity Proofing und Federation. ([pages.nist.gov](https://pages.nist.gov/800-63-4/)) |
| Authentifizierung | Ist das Authentisierungsniveau zum Schutzbedarf passend? | MFA für Admins, starke Authentifizierung für externe Antragstellende bei sensiblen Daten. | NIST SP 800-63-4 definiert Anforderungen an Authentifizierung und Authenticator Management. ([pages.nist.gov](https://pages.nist.gov/800-63-4/)) |
| Autorisierung | Wo und wie wird entschieden, was erlaubt ist? | Anwendung, API-Gateway, Policy Engine, Datenbank. | OWASP ASVS liefert prüfbare Anforderungen an Zugriffskontrolle. ([owasp.org](https://owasp.org/www-project-application-security-verification-standard/)) |
| Rollenmodell | Sind Rollen fachlich verständlich, nicht zu grob und nicht zu kleinteilig? | „Sachbearbeitung Vorgang“ statt „Superuser“. | Fachliche Steuerbarkeit ist Kern guter IAM-Architektur. |
| Attributmodell | Werden Zuständigkeit, Organisationseinheit, Falltyp und Schutzbedarf berücksichtigt? | Zugriff nur auf eigene Dienststelle. | ABAC ergänzt RBAC bei komplexer Zuständigkeitslogik. |
| Mandantentrennung | Ist getrennt zwischen Behörden, Referaten, Dienststellen oder Verfahren? | Dienstleister sieht nur beauftragtes Verfahren. | Kritisch bei Shared Platforms und zentralen Fachverfahren. |
| Admintrennung | Sind Alltagskonto und Adminkonto getrennt? | „max.mustermann“ und „adm-max.mustermann“. | PAM reduziert Risiko privilegierter Alltagsnutzung. |
| Dienstleisterzugriff | Ist Zugriff befristet, genehmigt, protokolliert und zweckgebunden? | Externer Supportzugriff nur über PAM und Ticketbezug. | Besonders relevant für Produktivzugriffe. |
| Technische Konten | Haben Service Accounts Eigentümer, Zweck, Scope, Rotation und Logging? | API-Client darf nur „register:read“ ausführen. | Technische Identitäten sind in BSI ORP.4 mitgemeint. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/02_ORP_Organisation_und_Personal/ORP_4_Identitaets_und_Berechtigungsmanagement_Editon_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Token-Sicherheit | Sind OAuth2/OIDC-Flows aktuell und sicher konfiguriert? | Authorization Code Flow mit PKCE, keine unsicheren Legacy-Flows. | RFC 9700 beschreibt aktuelle OAuth2-Sicherheitspraktiken. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/rfc9700/)) |
| SAML-Sicherheit | Sind Assertions signiert, Empfänger, Ablaufzeit und Audience korrekt geprüft? | SAML Assertion nur für vorgesehenen Service Provider. | SAML definiert Assertions über Authentication, Attributes und Authorization. ([oasis-open.org](https://www.oasis-open.org/standard/saml/?utm_source=chatgpt.com)) |
| Sitzungsmanagement | Sind Sessions zeitlich begrenzt und bei Rollenänderung invalidierbar? | Rollenentzug beendet aktive Sitzung oder erzwingt Reauthentifizierung. | OWASP ASVS behandelt Session- und Zugriffskontrollen. ([owasp.org](https://owasp.org/www-project-application-security-verification-standard/)) |
| Vier-Augen-Prinzip | Sind kritische Aktionen technisch erzwungen? | Rollenvergabe, Auszahlung, Bescheidfreigabe. | Nur organisatorisch notiert reicht nicht. |
| Delegation | Ist Stellvertretung befristet, begründet und protokolliert? | Urlaubsvertretung für Fachteam bis Datum X. | Verhindert dauerhafte Schattenberechtigungen. |
| Rezertifizierung | Gibt es regelmäßige Überprüfung durch Fachverantwortliche? | Quartalsweise für privilegierte Rollen. | BSI-Grundschutz fordert Zuweisung, Entzug und Kontrolle von Rechten. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2021/02_ORP_Organisation_und_Personal/ORP_4_Identitaets_und_Berechtigungsmanagement_Editon_2021.pdf?__blob=publicationFile&v=2&utm_source=chatgpt.com)) |
| Audit Logs | Sind sicherheitsrelevante Ereignisse vollständig und unveränderungssicher genug protokolliert? | Rollenänderung, Adminzugriff, Export, Loginfehler. | Auditierbarkeit ist Kern von Nachweisfähigkeit. |
| Betriebsübergabe | Sind IAM-Prozesse im Betrieb verstanden und dokumentiert? | Runbook für Rollenanlage, Entzug, Break Glass. | IAM muss betreibbar sein, nicht nur konzeptionell korrekt. |
| Abnahmekriterien | Sind IAM-Anforderungen testbar formuliert? | „Rolle X darf Vorgang Y nicht öffnen; Testfall vorhanden.“ | ASVS eignet sich auch zur Beschaffung und Vertragsanforderung. ([owasp.org](https://owasp.org/www-project-application-security-verification-standard/)) |

## 14. Sicherheitsfragen für dein Reviewgespräch

Du beginnst nicht mit Tools. Du beginnst mit Zugriffsszenarien. Frage den Fachbereich zuerst: **Welche Personen, Organisationen, Dienstleister und Systeme interagieren mit dem Verfahren? Welche Daten sind besonders schützenswert? Welche Aktionen verändern rechtlich oder fachlich relevante Zustände? Welche Zugriffe wären bei Missbrauch besonders problematisch?**

Danach fragst du zur Identität: **Woher kommt die Identität? Wie wird sie eindeutig festgestellt? Gibt es externe Identitätsquellen? Wie werden externe Antragstellende, interne Mitarbeitende und Dienstleister voneinander getrennt? Wie werden technische Identitäten inventarisiert?**

Zur Authentifizierung fragst du: **Welche Verfahren nutzen Passwort, MFA, Zertifikat, Smartcard, Passkey, SAML, OIDC oder Client Credentials? Welche Zugriffe benötigen ein höheres Authentisierungsniveau? Was passiert bei verlorenen Authenticatoren? Wie werden privilegierte Anmeldungen abgesichert?**

Zur Autorisierung fragst du: **Welche Rollen gibt es? Wer genehmigt sie? Welche Rechte stecken darin? Welche Rollen dürfen nicht kombiniert werden? Wird Zugriff auf Vorgänge nach Zuständigkeit begrenzt? Werden Schutzbedarf, Organisationseinheit, Mandant, Falltyp und Umgebung berücksichtigt?**

Zu technischen Konten fragst du: **Welche Service Accounts existieren? Wer besitzt sie? Welche Secrets nutzen sie? Wo liegen diese Secrets? Wie oft werden sie rotiert? Welche Scopes haben API-Clients? Welche Konten dürfen produktive Datenbanken lesen? Welche technischen Konten sind in CI/CD, Monitoring, Backup, DMS und Registerschnittstellen enthalten?**

Zu Federation und Token fragst du: **Welche Identity Provider sind vertrauenswürdig? Welche Claims werden übernommen? Wer validiert Audience, Issuer, Signatur, Ablaufzeit und Scope? Werden OAuth2 und OIDC korrekt getrennt? Gibt es noch Implicit Flow, Resource Owner Password Credentials oder breit gefasste Tokens? RFC 9700 ist hier deine aktuelle Referenz für OAuth2-Sicherheitspraktiken.** ([datatracker.ietf.org](https://datatracker.ietf.org/doc/rfc9700/))

Zu Betrieb und Audit fragst du: **Wer sieht IAM-Logs? Welche Ereignisse gehen ins SIEM? Wie lange werden Logs aufbewahrt? Sind Logs manipulationsgeschützt? Gibt es Alarmierung bei ungewöhnlicher Rollenvergabe, Massenexport, fehlgeschlagenen Adminlogins oder Service-Account-Missbrauch? Wer prüft Break-Glass-Nutzung nach?**

## 15. Typische Fehler in IAM-Konzepten

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Login mit IAM verwechseln | SSO löst Anmeldung, aber nicht fachliche Autorisierung. | „Wir haben OIDC, also ist Berechtigung erledigt.“ | OIDC liefert Authentifizierungsinformationen; Autorisierung bleibt separat zu modellieren. ([openid.net](https://openid.net/specs/openid-connect-core-1_0-final.html?utm_source=chatgpt.com)) |
| Superrollen | Eine Rolle enthält zu viele Rechte. | „Sachbearbeitung_Admin_All“. | Verstößt gegen Least Privilege und erschwert Rezertifizierung. |
| Einzelrechte-Wildwuchs | Rechte werden direkt an Personen vergeben. | 200 individuelle Sonderrechte ohne fachliche Rolle. | Fachliche Steuerung und Review werden kaum möglich. |
| Technische Konten ohne Eigentümer | Service Accounts sind nicht inventarisiert. | „batch_prod“ ohne Verantwortlichen und Ablaufdatum. | BSI ORP.4 umfasst auch IT-Komponenten. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/02_ORP_Organisation_und_Personal/ORP_4_Identitaets_und_Berechtigungsmanagement_Editon_2023.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Dienstleister mit Daueradminrechten | Externe behalten produktive Rechte nach Projektende. | VPN plus globaler Admin ohne Befristung. | Erhöht Betriebs- und Nachweisrisiko massiv. |
| Keine Rezertifizierung | Rollen bleiben jahrelang aktiv. | Mitarbeitende wechseln Team, behalten alte Rechte. | Rechte müssen zugewiesen, entzogen und kontrolliert werden. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2021/02_ORP_Organisation_und_Personal/ORP_4_Identitaets_und_Berechtigungsmanagement_Editon_2021.pdf?__blob=publicationFile&v=2&utm_source=chatgpt.com)) |
| Keine Trennung von Admin und Fachzugriff | Admins sehen Fachvorgänge ohne Anlass. | Datenbankadmin liest produktive Vorgangsdaten. | Muss durch technische und organisatorische Kontrollen reduziert werden. |
| OAuth2 falsch verstanden | OAuth2 wird als Login-Protokoll behandelt. | Anwendung nutzt Access Token als Identitätsnachweis ohne OIDC-Verständnis. | OAuth2 ist Autorisierung; OIDC ergänzt Authentifizierung. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/rfc9700/)) |
| SAML/OIDC-Claims blind vertraut | Anwendungen prüfen Claims nicht korrekt. | Rollen werden aus unsignierten oder falsch validierten Attributen übernommen. | Federation braucht klare Trust Boundaries. |
| Keine Token-Begrenzung | Tokens sind zu lange gültig oder zu breit berechtigt. | Access Token mit „*“-Scope für mehrere APIs. | RFC 9700 adressiert moderne OAuth2-Bedrohungen und Privilegienbegrenzung. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/rfc9700/)) |
| Fehlende Auditierbarkeit | Kritische Aktionen sind nicht nachvollziehbar. | Niemand weiß, wer Rolle „Fachaufsicht“ vergeben hat. | Audit Logs sind Voraussetzung für Nachweisfähigkeit. |
| Vier-Augen-Prinzip nur auf Papier | Prozess ist beschrieben, aber technisch nicht erzwungen. | Freigabe kann durch dieselbe Person erfolgen. | Kritische Fachaktionen müssen systemisch kontrolliert werden. |
| Rollenmodell ohne Fachsprache | Nur IT-Gruppen, keine fachliche Bedeutung. | „CN_APP_4711_RW_PROD“. | Fachbereich kann Berechtigungen nicht verantworten. |
| Zu spätes IAM-Design | Rollenmodell wird kurz vor Go-live improvisiert. | Testrollen werden zu Produktivrollen. | IAM gehört in Zielarchitektur, Datenmodell, API-Design und Betriebskonzept. |
| Fehlende Umgebungstrennung | Test-, Abnahme- und Produktivrechte vermischen sich. | Entwickler mit Produktivdatenzugriff über Testkonto. | Besonders kritisch bei Dienstleistern und Migrationen. |

## 16. Wie du IAM-Anforderungen in Zielarchitekturen formulierst

Eine gute IAM-Anforderung ist nicht abstrakt, sondern prüfbar. Nicht: **„Das System muss sichere Authentifizierung unterstützen.“** Besser: **„Das Fachverfahren muss interne Nutzende über den zentralen Identity Provider per OpenID Connect authentifizieren. Für privilegierte Rollen ist MFA verpflichtend. Die Anwendung darf Zugriffsentscheidungen nicht allein aus der erfolgreichen Anmeldung ableiten, sondern muss fachliche Rollen und Attribute wie Organisationseinheit, Zuständigkeit, Verfahrenskontext und Schutzbedarf auswerten.“**

Nicht: **„Service Accounts müssen sicher sein.“** Besser: **„Jedes technische Konto muss einen fachlichen oder technischen Eigentümer, einen dokumentierten Zweck, eine Umgebung, einen minimalen Rechteumfang, ein Ablauf- oder Rezertifizierungsdatum, einen Secret-Rotationsprozess und Audit-Logging besitzen. Nicht zuordenbare technische Konten sind vor Produktionsfreigabe zu entfernen oder formal zu genehmigen.“**

Nicht: **„Es soll Logging geben.“** Besser: **„Das System muss Anmeldung, fehlgeschlagene Anmeldung, Token-Ausstellung, Rollenvergabe, Rollenentzug, privilegierte Anmeldung, Berechtigungsfehler, Massenexport, Break-Glass-Nutzung und fachlich kritische Freigaben mit Zeitstempel, Identität, Quellsystem, Zielobjekt, Aktion, Ergebnis und Korrelations-ID protokollieren. Die Logs müssen an die zentrale Logging-/SIEM-Plattform angebunden werden.“**

Nicht: **„Vier-Augen-Prinzip wird organisatorisch geregelt.“** Besser: **„Für die Freigabe von Bescheiden der Kritikalitätsklasse hoch muss das System technisch erzwingen, dass Ersteller und Freigebender unterschiedliche Identitäten sind. Die Freigabeentscheidung muss mit Zeitpunkt, Rolle, Vorgangs-ID und Entscheidungsstatus auditierbar protokolliert werden.“**

## 17. Konkretes Zielbild für dein Behördenbeispiel

Im Zielbild nutzt das Fachverfahren einen zentralen Identity Provider für interne Nutzende und einen föderierten Identity Provider für externe Antragstellende. Interne Anmeldung erfolgt über SSO mit MFA für privilegierte Rollen. Externe Antragstellende erhalten Zugriff nur auf eigene Anträge und Dokumente. Die Fachanwendung wertet Rollen und Attribute aus: Rolle, Organisationseinheit, Dienststelle, Zuständigkeit, Vertretung, Verfahrensstand und Schutzbedarf.

API-Zugriffe zwischen Portal, API-Gateway, Fachverfahren, DMS und Registerschnittstelle verwenden technische Identitäten mit klar begrenzten Scopes. OAuth2 wird für API-Autorisierung genutzt, OpenID Connect für nutzerbezogene Anmeldung. Für klassische Enterprise-Anwendungen kann SAML weiterhin zulässig sein, muss aber sauber validierte Assertions, Signaturen, Ablaufzeiten, Audience-Prüfung und Attributmapping verwenden.

Privilegierte Zugriffe laufen über PAM. Dienstleisterzugriffe sind befristet, genehmigt, protokolliert und an Tickets oder Arbeitsaufträge gekoppelt. Technische Konten werden in einem zentralen Inventar geführt. Secrets liegen nicht in Code, Wikis, Deployment-Dateien oder lokalen Skripten, sondern in einem dafür vorgesehenen Secret-Management-System. Rollen werden regelmäßig rezertifiziert. Kritische Aktionen unterliegen Vier-Augen-Freigaben. Audit Logs gehen an zentrale Auswertung.

## 18. Befundformulierungen, die du in Reviews verwenden kannst

**Befund 1: Unzureichendes Rollenmodell.** Das vorgelegte IAM-Konzept beschreibt zwar die Anmeldung über einen zentralen Identity Provider, enthält aber kein fachlich prüfbares Rollen- und Rechtemodell. Es bleibt unklar, welche Rolle welche Aktionen auf welchen Datenobjekten ausführen darf. Dadurch sind Least Privilege, fachliche Zuständigkeit, Vier-Augen-Prüfung und Rezertifizierung nicht belastbar bewertbar.

**Maßnahme:** Vor Architekturfreigabe ist ein Rollenmodell mit Rollenname, Zweck, Trägerkreis, konkreten Rechten, Datenumfang, Genehmiger, Gültigkeit, Kritikalität, Ausschlussregeln, Rezertifizierungszyklus und Audit Events zu liefern.

**Befund 2: Technische Konten nicht ausreichend kontrolliert.** Im Konzept werden technische Konten für DMS, Registerschnittstelle, Datenbank und Monitoring erwähnt, jedoch ohne Eigentümer, Rechteumfang, Secret-Rotation, Ablaufdatum und Protokollierung. Dadurch besteht das Risiko dauerhafter und nicht nachvollziehbarer Systemzugriffe.

**Maßnahme:** Jedes technische Konto ist vor Produktivsetzung zu inventarisieren, auf minimal notwendige Scopes/Rechte zu begrenzen, einem Eigentümer zuzuordnen, in Secret Management einzubinden und in die Rezertifizierung aufzunehmen.

**Befund 3: OAuth2/OIDC nicht sauber getrennt.** Das Konzept verwendet OAuth2-Begriffe für Anmeldung und Identitätsfeststellung, ohne OpenID Connect, ID Token, Claims, Audience, Issuer und Tokenvalidierung klar zu beschreiben. Dadurch besteht das Risiko fehlerhafter Vertrauensannahmen zwischen Client, Authorization Server und Resource Server.

**Maßnahme:** Das Zielbild muss präzisieren, welche Flows für Authentifizierung und API-Autorisierung genutzt werden, welche Tokenarten verwendet werden, wie Token validiert werden und welche Scopes/Claims für Autorisierungsentscheidungen zulässig sind. Aktuelle OAuth2-Sicherheitsempfehlungen nach RFC 9700 sind zu berücksichtigen. ([datatracker.ietf.org](https://datatracker.ietf.org/doc/rfc9700/))

**Befund 4: Dienstleisterzugriff zu breit.** Der vorgesehene Dienstleisterzugriff erlaubt produktionsnahe Analyse ohne klare Befristung, Rollenbegrenzung, Freigabe, Session Logging und Nachkontrolle. Das ist bei behördlichen Fachverfahren mit schützenswerten Daten nicht ausreichend.

**Maßnahme:** Dienstleisterzugriffe sind über PAM oder gleichwertige kontrollierte Zugangswege zu führen, zeitlich zu begrenzen, an Aufträge/Tickets zu koppeln, mit MFA abzusichern und revisionsfähig zu protokollieren.

## 19. Deine praktische Review-Methode in sieben Schritten

Im ersten Schritt zeichnest du eine Identitätslandkarte. Du notierst alle Personen- und Maschinenidentitäten: Antragstellende, interne Nutzende, Fachaufsicht, Admins, Dienstleister, API-Clients, Datenbankkonten, Batch-Jobs, Monitoring, Backup und CI/CD. Ohne diese Landkarte bleibt das IAM-Konzept unvollständig.

Im zweiten Schritt zeichnest du die Vertrauenskette. Du klärst, welche Identity Provider existieren, welche Anwendung welchen Provider akzeptiert, welche Claims übernommen werden, welche Federation-Beziehung besteht und wo Token oder Assertions validiert werden.

Im dritten Schritt prüfst du die fachlichen Rollen. Du lässt dir Rollen nicht nur als Gruppenliste zeigen, sondern als fachliches Modell: Zweck, Rechte, Datenumfang, Genehmigung, Gültigkeit, Ausschlüsse, Rezertifizierung und Audit Events.

Im vierten Schritt prüfst du technische Konten. Du verlangst ein Inventar. Jedes Konto ohne Zweck, Eigentümer und minimalen Scope ist ein Risiko. Besonders kritisch sind produktive Datenbankkonten, Registerschnittstellen, DMS-Schreibrechte, Deployment-User und Break-Glass-Konten.

Im fünften Schritt prüfst du privilegierte Zugriffe. Du fragst nach PAM, MFA, Just-in-Time, Session Logging, getrennten Adminkonten, Notfallverfahren und nachgelagerter Kontrolle. Dauerhafte Adminrechte ohne Anlassbezug sind eine rote Flagge.

Im sechsten Schritt prüfst du Auditierbarkeit. Du lässt dir nicht nur sagen, dass „geloggt wird“. Du fragst, welche Ereignisse mit welchen Feldern wohin geliefert werden, wie lange sie aufbewahrt werden, wer sie auswertet und welche Alarme existieren.

Im siebten Schritt übersetzt du Befunde in Architekturbedingungen. Das Ergebnis eines IAM-Reviews ist kein Bauchgefühl, sondern eine Liste prüfbarer Anforderungen, Risiken, Entscheidungen, offenen Punkte und Abnahmekriterien.

## 20. Übung: IAM-Konzept prüfen

Du erhältst folgendes Kurzkonzept: Ein neues Behördenportal nutzt einen zentralen Login. Interne Mitarbeitende melden sich per SSO an. Externe Antragstellende können Anträge stellen. Sachbearbeitende bearbeiten Vorgänge. Ein externer Dienstleister betreibt die Anwendung. Die Anwendung nutzt eine Datenbank, ein DMS, eine Registerschnittstelle und ein Monitoring-System. Für APIs werden Tokens verwendet. Es gibt Rollen „User“, „Admin“ und „ReadOnly“. Technische Konten heißen „appuser“, „batchuser“ und „dmsuser“. Logs werden lokal gespeichert.

Deine Aufgabe ist, das Konzept aus IAM-Sicht zu bewerten. Markiere mindestens zehn Befunde. Formuliere danach fünf konkrete Zielarchitektur-Anforderungen.

Eine sehr gute Lösung würde ungefähr so aussehen: Erstens sind die Rollen „User“, „Admin“ und „ReadOnly“ fachlich zu grob. Zweitens fehlt die Trennung zwischen Antragstellenden, Sachbearbeitung, Fachaufsicht, Verfahrensadministration, technischer Administration und Dienstleister. Drittens ist unklar, ob Sachbearbeitende nur eigene Zuständigkeiten sehen. Viertens fehlen Attribute wie Organisationseinheit, Dienststelle, Falltyp, Schutzbedarf und Vertretung. Fünftens sind technische Konten nicht zweckgebunden dokumentiert. Sechstens fehlen Eigentümer und Rezertifizierung für Service Accounts. Siebtens ist unklar, ob OAuth2 oder OIDC genutzt wird und welche Token validiert werden. Achtens fehlen MFA- und PAM-Anforderungen für Adminzugriffe. Neuntens ist Dienstleisterzugriff nicht befristet oder kontrolliert. Zehntens sind lokale Logs für Nachweisfähigkeit und zentrale Auswertung unzureichend. Elftens fehlen Vier-Augen-Regeln für kritische Freigaben. Zwölftens fehlen Abnahmetests für Zugriffskontrolle.

Fünf gute Zielarchitektur-Anforderungen wären: Erstens muss das Fachverfahren ein fachliches Rollenmodell mit mindestens Antragstellenden, Sachbearbeitung, Fachaufsicht, Verfahrensadministration, technischer Administration, Dienstleisterrolle und technischen Systemrollen liefern. Zweitens muss Zugriff auf Vorgänge über Rollen und Attribute wie Organisationseinheit, Zuständigkeit, Verfahrensstatus und Schutzbedarf entschieden werden. Drittens müssen alle Service Accounts mit Eigentümer, Zweck, Scope, Umgebung, Secret-Rotation, Rezertifizierung und Audit Events dokumentiert werden. Viertens müssen privilegierte Zugriffe über MFA, getrennte Adminkonten, PAM oder gleichwertige Kontrollen, Befristung und Protokollierung abgesichert werden. Fünftens müssen alle sicherheitsrelevanten Ereignisse zentral protokolliert und für Review, Incident Response und Nachweisführung auswertbar sein.

## 21. Was du am Ende fachlich sagen können musst

Du solltest nach diesem Modul nicht nur Begriffe kennen, sondern IAM als Architekturmechanismus erklären können. Eine starke Formulierung auf Augenhöhe wäre:

„Für dieses Fachverfahren reicht eine zentrale Anmeldung allein nicht aus. Wir brauchen ein fachliches Rollen- und Attributmodell, das Zugriff auf Vorgänge, Dokumente, Registerdaten, Adminfunktionen und Schnittstellen differenziert steuert. Menschliche und technische Identitäten müssen getrennt betrachtet werden. OAuth2, OIDC und SAML sind korrekt nach Zweck einzusetzen: API-Autorisierung, Authentifizierungsinformationen und Federation. Privilegierte Zugriffe, Dienstleisterzugriffe und Service Accounts benötigen zusätzliche Kontrollen, Rezertifizierung und Auditierbarkeit. Diese Anforderungen gehören nicht in die technische Restliste, sondern in die Zielarchitektur und in die Abnahmekriterien.“

Das ist genau die Haltung eines Enterprise Architekten: Du administrierst nicht das IAM-System, aber du stellst sicher, dass Identitäten, Rollen, Rechte, Schnittstellen, Betrieb, Sicherheit und Nachweisfähigkeit als zusammenhängende Architektur verstanden und prüfbar umgesetzt werden.

<>