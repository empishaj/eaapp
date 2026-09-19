## Checkliste: CI/CD und IaC aus Enterprise-Architecture-Sicht

* Prüfe zuerst, ob die Pipeline den kompletten Lieferweg vom Commit bis zur Produktion nachvollziehbar abbildet.  
* Trenne sauber zwischen Build, Deployment und Release; viele Organisationen vermischen diese Begriffe gefährlich.  
* Stelle sicher, dass Artefakte einmal gebaut und danach unverändert durch die Umgebungen promotet werden.  
* Verlange ein zentrales Artifact Repository mit Versionierung, Zugriffsschutz, Aufbewahrung und Nachvollziehbarkeit.  
* Prüfe, ob Security Scans als verbindliche Gates wirken oder nur dekorative Reports erzeugen.  
* Bewerte, ob Infrastructure as Code wirklich deklarativ, versioniert, reviewbar und reproduzierbar ist.  
* Kontrolliere, ob Secrets niemals im Code, in Logs, in Pipeline-Variablen ohne Schutz oder in Artefakten landen.  
* Prüfe, ob Umgebungen konsistent erzeugt werden können oder ob manuelle Sonderstände existieren.  
* Verlange Rollback-, Rollforward- und Wiederanlaufverfahren als Teil der Architektur, nicht als spätere Betriebsnotiz.  
* Prüfe, ob GitOps, Terraform, Ansible und Helm klar abgegrenzte Aufgaben haben und nicht chaotisch dieselben Dinge verändern.  
* Stelle sicher, dass jede produktionsrelevante Änderung eine nachvollziehbare Genehmigungs-, Prüf- und Ausführungsspur besitzt.  
* Bewerte die Pipeline als Teil der Software Supply Chain; sie ist selbst ein schützenswertes System.  

## 1. Der Kern: CI/CD ist nicht „Automatisierung“, sondern kontrollierte Lieferfähigkeit

Aus Enterprise-Architecture-Sicht ist CI/CD keine Sammlung technischer Jobs, sondern das Steuerungssystem für Softwarelieferungen. Eine Pipeline entscheidet, welcher Code gebaut wird, welche Qualität nachgewiesen ist, welches Artefakt weitergegeben wird, welche Umgebung verändert wird, wer freigibt, welche Risiken akzeptiert werden und ob ein Produktionsstand reproduzierbar erklärt werden kann. Genau deshalb ist CI/CD im Behördenkontext nicht nur ein DevOps-Thema, sondern ein Architektur-, Security-, Betriebs-, Beschaffungs- und Nachweisthema.

Die zentrale EA-Frage lautet nicht: „Habt ihr Jenkins, GitLab CI, GitHub Actions, Azure DevOps oder Argo CD?“ Die zentrale Frage lautet: „Könnt ihr für jeden produktiven Stand belastbar nachweisen, aus welchem Quellcode, mit welchem Build-Prozess, mit welchen Abhängigkeiten, mit welchen Prüfungen, mit welchem Artefakt, durch welche Freigabe und auf welcher Infrastruktur dieser Stand entstanden ist?“ Diese Sicht passt unmittelbar zu Secure Software Development und Software-Supply-Chain-Gedanken, wie sie NIST SSDF und SLSA beschreiben: Softwareentwicklung muss kontrollierte, überprüfbare und gegen Manipulation geschützte Praktiken enthalten; SLSA fokussiert explizit Integrität, Herkunftsnachweis und Schutz der Artefaktkette. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com))

## 2. Die wichtigsten Begriffe sauber getrennt

| Aspekt | Details/Erklärung | Beispiel | Literatur/Quelle |
|---|---|---|---|
| Continuous Integration | Entwickleränderungen werden häufig integriert, automatisiert gebaut und getestet. Ziel ist frühes Feedback. | Jeder Merge Request startet Build, Unit Tests, SAST und Dependency Scan. | OWASP beschreibt CI/CD-Pipelines als zentrale, wiederholbare Build- und Deployment-Prozesse, die selbst abgesichert werden müssen. ([cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html?utm_source=chatgpt.com)) |
| Build | Der Quellcode wird in ein ausführbares oder deploybares Artefakt übersetzt. | Java-Code wird zu einem JAR, Container Image oder Helm-fähigem Deployment-Paket. | NIST SSDF fordert sichere Entwicklungspraktiken über den SDLC hinweg. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com)) |
| Test | Automatisierte Prüfungen gegen Funktion, Regression, Integration, Security und technische Qualität. | Unit Tests, Integration Tests, Contract Tests, API Tests, Smoke Tests. | Der BSI-Baustein OPS.1.1.6 behandelt Software-Tests und Freigaben als Betriebs- und Freigabethema. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2022/04_OPS_Betrieb/OPS_1_1_6_Software_Tests_und_Freigaben_Edition_2022.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Security Scan | Automatisierte Erkennung von Schwachstellen, Fehlkonfigurationen, Lizenzrisiken und Secrets. | SAST, SCA, Container Scan, IaC Scan, Secret Scan. | OWASP CI/CD Security Cheat Sheet adressiert Schutz der Pipeline, Secrets, Artefakte und Supply-Chain-Risiken. ([cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html?utm_source=chatgpt.com)) |
| Artifact Repository | Zentrale Ablage für versionierte, unveränderliche Build-Ergebnisse. | Nexus, Artifactory, GitHub Packages, GitLab Package Registry, OCI Registry. | SLSA betont Herkunft, Integrität und Schutz von Artefakten in der Lieferkette. ([slsa.dev](https://slsa.dev/?utm_source=chatgpt.com)) |
| Deployment | Technisches Ausbringen eines Artefakts in eine Umgebung. | Container Image wird in Kubernetes-Cluster ausgerollt. | Helm definiert Charts als Paketformat zur Definition, Installation und Aktualisierung von Kubernetes-Anwendungen. ([helm.sh](https://helm.sh/?utm_source=chatgpt.com)) |
| Release | Fachlich/organisatorische Freigabe einer Funktion für Nutzer. | Feature ist deployt, wird aber erst über Feature Flag aktiviert. | Trennung ist Architekturpraxis; die Nachweisforderung ergibt sich aus Test-, Freigabe- und Supply-Chain-Anforderungen. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2022/04_OPS_Betrieb/OPS_1_1_6_Software_Tests_und_Freigaben_Edition_2022.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Promotion | Weitergabe desselben Artefakts von Umgebung zu Umgebung. | `app:1.8.4` läuft zuerst in Test, dann Abnahme, dann Produktion. | SLSA- und Supply-Chain-Logik verlangen nachvollziehbare Artefaktintegrität. ([slsa.dev](https://slsa.dev/?utm_source=chatgpt.com)) |
| Rollback | Rückkehr auf einen vorherigen stabilen Stand. | Helm Rollback auf vorherige Release-Version oder Rücksetzen des GitOps-Zielstands. | GitOps-Prinzipien verlangen versionierten, unveränderlichen Zielzustand und kontinuierliche Abgleichbarkeit. ([opengitops.dev](https://opengitops.dev/?utm_source=chatgpt.com)) |
| Environment Management | Standardisierte Verwaltung von Dev, Test, Abnahme, PreProd und Prod. | Jede Umgebung wird per Terraform/Helm erzeugt, nicht manuell zusammengeklickt. | Terraform beschreibt IaC als versionierbare, wiederverwendbare und wiederholbare Infrastrukturdefinition. ([developer.hashicorp.com](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/infrastructure-as-code?utm_source=chatgpt.com)) |
| Auditierbarkeit | Jede Änderung, Prüfung, Freigabe und Ausführung ist nachvollziehbar. | Commit, Pull Request, Approval, Pipeline Run, Scan Report, Artefakt-Hash, Deployment-Protokoll. | NIST CSF 2.0 stellt Governance und Risikomanagement als zentrale Funktionen heraus. ([nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf?utm_source=chatgpt.com)) |

## 3. Die Architekturperspektive: Was eine gute Pipeline leisten muss

Eine gute Enterprise-Pipeline beantwortet fünf Fragen. Erstens: Ist der Ursprung klar? Das bedeutet: Quellcode, Commit, Branch, Autor, Review und Freigabe sind nachvollziehbar. Zweitens: Ist das Artefakt vertrauenswürdig? Das bedeutet: Es wurde in einer kontrollierten Build-Umgebung erzeugt, versioniert, gegen Manipulation geschützt und idealerweise signiert. Drittens: Ist die Qualität nachgewiesen? Das bedeutet: Tests, Security Scans, Lizenzprüfung, IaC-Prüfung und Policy Checks erzeugen verwertbare Ergebnisse. Viertens: Ist die Umgebung reproduzierbar? Das bedeutet: Infrastruktur, Konfiguration und Deployment-Zustand sind als Code definiert. Fünftens: Ist der Betrieb vorbereitet? Das bedeutet: Observability, Runbooks, Rollback, Backup-/Restore-Abhängigkeiten, Betriebsdokumentation und Übergabeinformationen entstehen nicht erst nach dem Go-live.

Der wichtigste fachliche Fehler ist, CI/CD als „schneller ausliefern“ zu verkaufen. In einer Behörde ist die bessere Formulierung: CI/CD erhöht kontrollierte Lieferfähigkeit, reduziert manuelle Fehler, verbessert Nachweisbarkeit, verkürzt Feedbackzyklen und macht Risiken früher sichtbar. Geschwindigkeit ist ein Nebeneffekt, nicht der Hauptzweck.

## 4. Der Lieferfluss als Zielbild

Ein belastbares Zielbild sieht in der Grundform so aus: Entwickler committen Code in ein versioniertes Repository. Ein Merge Request erzwingt Review, automatisierte Tests und erste Security-Prüfungen. Nach Merge auf den Hauptzweig erzeugt die Build-Pipeline ein Artefakt. Dieses Artefakt wird in ein zentrales Repository geschrieben, mit Metadaten versehen und gegen Veränderung geschützt. Anschließend wird dasselbe Artefakt durch Test-, Integrations-, Abnahme- und Produktionsumgebungen promotet. Jede Promotion erzeugt Nachweise. Deployment und Umgebungskonfiguration erfolgen über deklarative Definitionen. Der produktive Zielzustand ist versioniert. Jede Änderung ist über Commit, Pipeline Run, Artefaktversion, Freigabe und Deployment-Ereignis nachvollziehbar.

Ein einfaches Zielbild in Textform:

`Git Commit → Merge Request → Build → Unit Tests → SAST/SCA/Secret Scan → Artefakt erzeugen → SBOM/Provenance/Signatur → Artifact Repository → Deploy Test → Integration/Contract Tests → Deploy Abnahme → fachliche Abnahme → Change-/Release-Freigabe → Deploy Produktion → Smoke Test → Monitoring/Alerting → Rollback-Fähigkeit → Betriebsnachweis`

Dieses Zielbild ist bewusst nicht toolgebunden. Ob eine Organisation GitLab CI, Jenkins, Tekton, Azure DevOps, GitHub Actions, Argo CD, Flux, Nexus, Artifactory oder Harbor nutzt, ist zweitrangig. Aus EA-Sicht zählt, ob die Kontrollpunkte, Nachweise, Rollen und Übergänge sauber funktionieren.

## 5. Infrastructure as Code: Der Architekturwert

Infrastructure as Code bedeutet, dass Infrastruktur nicht primär über manuelle Klicks, sondern über versionierte, prüfbare und wiederholbare Konfigurationen beschrieben wird. Terraform beschreibt Infrastrukturressourcen deklarativ und verwaltet dazu einen State, der reale Ressourcen der Konfiguration zuordnet; HashiCorp beschreibt Terraform als Werkzeug, um Infrastruktur sicher und effizient zu bauen, zu ändern und zu versionieren. ([developer.hashicorp.com](https://developer.hashicorp.com/terraform/docs?utm_source=chatgpt.com))

Ansible ist stärker auf Konfigurationsmanagement, Systemkonfiguration, Softwareverteilung und Orchestrierung ausgerichtet; die offizielle Dokumentation beschreibt es als Werkzeug, um Betriebssysteme zu konfigurieren, Software auszurollen und fortgeschrittene Workflows zu orchestrieren. ([docs.ansible.com](https://docs.ansible.com/?utm_source=chatgpt.com))

Helm ist im Kubernetes-Kontext ein Paketmanager. Helm Charts beschreiben zusammengehörige Kubernetes-Ressourcen und ermöglichen Installation, Upgrade und Versionierung komplexer Anwendungen. ([helm.sh](https://helm.sh/?utm_source=chatgpt.com))

GitOps ergänzt diese Werkzeuge durch ein Betriebsmodell: Der gewünschte Zustand wird deklarativ beschrieben, versioniert und unveränderlich abgelegt, automatisch gezogen und kontinuierlich mit dem Ist-Zustand abgeglichen. Diese vier Prinzipien werden von OpenGitOps als deklarativ, versioniert/immutable, automatisch gezogen und kontinuierlich abgeglichen beschrieben. ([opengitops.dev](https://opengitops.dev/?utm_source=chatgpt.com))

## 6. Terraform, Ansible, Helm und GitOps sauber voneinander abgrenzen

| Aspekt | Details/Erklärung | Beispiel | Typischer EA-Prüfpunkt | Literatur/Quelle |
|---|---|---|---|---|
| Terraform | Provisioniert Infrastrukturressourcen deklarativ; wichtig sind Module, State, Provider-Versionen, Plan/Apply-Prozess und Drift-Erkennung. | Netzwerk, Datenbank, Kubernetes-Cluster, IAM-Rollen, DNS. | Gibt es Remote State, State Locking, Review für `plan`, getrennte Rechte für Plan und Apply? | Terraform-Dokumentation zu IaC und State. ([developer.hashicorp.com](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/infrastructure-as-code?utm_source=chatgpt.com)) |
| Ansible | Konfiguriert Systeme, installiert Software, orchestriert Abläufe und kann Legacy-/VM-Welten gut bedienen. | Härtung eines Linux-Servers, Installation von Agenten, Konfiguration von Middleware. | Sind Playbooks idempotent, versioniert, getestet und ohne harte Secrets? | Offizielle Ansible-Dokumentation. ([docs.ansible.com](https://docs.ansible.com/?utm_source=chatgpt.com)) |
| Helm | Paketiert Kubernetes-Anwendungen als Charts; geeignet für wiederholbare Deployments mit Values je Umgebung. | Deployment, Service, Ingress, ConfigMap, HorizontalPodAutoscaler. | Sind Charts versioniert, Werte getrennt, Secrets ausgelagert, Templates validiert? | Helm-Dokumentation zu Charts. ([helm.sh](https://helm.sh/docs/topics/charts/?utm_source=chatgpt.com)) |
| GitOps | Betriebsmodell, bei dem Git den gewünschten Zielzustand hält und Agenten den Zielzustand automatisch abgleichen. | Argo CD oder Flux synchronisiert Kubernetes-Manifeste aus Git. | Ist Git wirklich führend oder wird Produktion parallel manuell verändert? | OpenGitOps-Prinzipien. ([opengitops.dev](https://opengitops.dev/?utm_source=chatgpt.com)) |
| Artifact Repository | Speichert Artefakte kontrolliert und versioniert. | Maven-Artefakte, Container Images, Helm Charts, SBOMs. | Sind Artefakte immutable, signiert, gescannt und aufbewahrt? | SLSA und OWASP fokussieren Artefaktintegrität und Pipeline-Schutz. ([slsa.dev](https://slsa.dev/?utm_source=chatgpt.com)) |
| Secrets Management | Verwaltet Zugangsdaten kontrolliert außerhalb des Codes. | Vault, Cloud Secrets Manager, Kubernetes External Secrets. | Gibt es Rotation, Least Privilege, keine Secrets in Logs und keine Langzeit-Tokens in Pipelines? | OWASP CI/CD Security Cheat Sheet adressiert Secrets und Pipeline-Schutz. ([cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html?utm_source=chatgpt.com)) |

## 7. Warum das im Behördenkontext besonders relevant ist

Im Behördenumfeld wirken mehrere Anforderungen gleichzeitig. Fachverfahren haben oft lange Lebenszyklen, mehrere Dienstleister, strenge Betriebsübergaben, nachvollziehbare Freigabeprozesse, Datenschutzanforderungen, Informationssicherheitsvorgaben, Vergabe- und Abnahmelogiken sowie heterogene Betriebsmodelle. Eine Pipeline ist hier nicht nur ein Entwicklerwerkzeug, sondern ein Nachweissystem. Sie zeigt, ob Liefergegenstände vollständig sind, ob Sicherheitsprüfungen stattgefunden haben, ob Betriebsfähigkeit vorbereitet wurde und ob ein Dienstleister steuerbar liefert.

Der BSI-Grundschutz-Baustein zu Software-Tests und Freigaben macht deutlich, dass Test- und Freigabeprozesse für Software organisatorisch und betrieblich relevant sind; NIST SSDF fordert sichere Softwareentwicklungspraktiken, die in unterschiedliche SDLC-Modelle integrierbar sind; OWASP weist darauf hin, dass CI/CD-Pipelines selbst attraktive Angriffsziele sind und deshalb abgesichert werden müssen. Zusammengenommen ergibt sich eine klare EA-Schlussfolgerung: Die Lieferpipeline ist Teil der Zielarchitektur und gehört in Architekturreviews, Ausschreibungen, Abnahmekriterien und Betriebsübergaben. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2022/04_OPS_Betrieb/OPS_1_1_6_Software_Tests_und_Freigaben_Edition_2022.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com))

## 8. Mindestanforderungen, die du als Enterprise Architekt formulieren kannst

Eine gute Mindestanforderung ist nicht „Der Auftragnehmer nutzt CI/CD“. Das ist zu weich. Besser ist: „Der Auftragnehmer liefert und betreibt eine nachvollziehbare, versionierte und automatisierte Lieferpipeline, die Quellcode, Build, Tests, Security-Prüfungen, Artefakterzeugung, Artefaktablage, Deployment, Promotion, Rollback und Deployment-Nachweise vollständig abbildet. Für jeden produktiven Stand müssen Commit, Build-Run, Artefaktversion, Prüfergebnisse, Freigabeentscheidung, Deployment-Zeitpunkt und Zielumgebung nachvollziehbar sein.“

Für IaC lautet eine belastbare Mindestanforderung: „Alle produktionsrelevanten Infrastruktur- und Deployment-Konfigurationen sind als Code zu liefern, in einem versionierten Repository zu verwalten, über Pull/Merge Requests zu ändern, automatisiert zu prüfen und reproduzierbar auf Zielumgebungen anzuwenden. Manuelle Änderungen an produktionsrelevanten Ressourcen sind zu dokumentieren, zu begründen und in den Code zurückzuführen.“

Für Security Gates lautet eine belastbare Mindestanforderung: „Die Pipeline muss mindestens SAST, SCA, Secret Detection, Container Image Scanning, IaC-/Policy-Prüfung und Lizenzprüfung unterstützen. Kritische Befunde verhindern die Promotion in produktionsnahe und produktive Umgebungen, sofern keine dokumentierte, befristete und genehmigte Ausnahme vorliegt.“

Für Betriebsübergabe lautet eine belastbare Mindestanforderung: „Mit jedem Release sind Betriebsinformationen zu liefern: Deployment Notes, Konfigurationsänderungen, Migrationshinweise, Rollback-Verfahren, Smoke-Test-Ergebnis, bekannte Einschränkungen, Observability-Anpassungen, neue Alerts, relevante Dashboards und aktualisierte Runbooks.“

## 9. Pipeline-Review-Fragen für Architekturreviews

| Aspekt | Details/Erklärung | Konkrete Review-Fragen | Beispiel | Literatur/Quelle |
|---|---|---|---|---|
| Source Control | Jede produktionsrelevante Änderung muss aus versioniertem Code entstehen. | Wo liegt der Source of Truth? Gibt es Branch Protection? Sind Reviews verpflichtend? Sind direkte Commits auf Hauptzweige gesperrt? | Pull Request mit zwei Reviews vor Merge. | NIST SSDF und SLSA stützen die Notwendigkeit kontrollierter Entwicklungs- und Herkunftsprozesse. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/218/final?utm_source=chatgpt.com)) |
| Build | Der Build muss reproduzierbar, isoliert und nachvollziehbar sein. | Wird in sauberer Build-Umgebung gebaut? Sind Abhängigkeiten gepinnt? Gibt es Build-Logs und Build-ID? | Containerisierter Build mit festgelegter Toolchain-Version. | SLSA fokussiert Integrität und Provenance der Build- und Artefaktkette. ([slsa.dev](https://slsa.dev/?utm_source=chatgpt.com)) |
| Tests | Tests müssen stufenweise Qualität belegen. | Welche Unit-, Integration-, Contract-, Regression- und Smoke-Tests laufen? Welche Mindestabdeckung oder kritischen Pfade sind verpflichtend? | API-Contract-Test gegen Registerschnittstelle. | BSI OPS.1.1.6 behandelt Software-Tests und Freigaben. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2022/04_OPS_Betrieb/OPS_1_1_6_Software_Tests_und_Freigaben_Edition_2022.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |
| Security Scans | Scans müssen steuernde Wirkung haben. | Welche Scans laufen wann? Welche Befunde blockieren? Wer genehmigt Ausnahmen? Wie werden False Positives behandelt? | Kritische CVE blockiert Deployment nach Abnahme. | OWASP CI/CD Security Cheat Sheet. ([cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html?utm_source=chatgpt.com)) |
| Artefakte | Ein Artefakt darf nach dem Build nicht je Umgebung neu gebaut werden. | Wird einmal gebaut und mehrfach promotet? Sind Artefakte immutable? Gibt es Hash, Signatur oder Provenance? | Image `fachportal:2.4.7` wird unverändert von Test nach Prod promotet. | SLSA zu Artefaktintegrität. ([slsa.dev](https://slsa.dev/?utm_source=chatgpt.com)) |
| SBOM/SCA | Abhängigkeiten müssen transparent sein. | Wird eine SBOM erzeugt? Wird sie abgelegt? Wird sie fortlaufend gegen neue Schwachstellen geprüft? | CycloneDX-SBOM in Dependency-Track. | OWASP Dependency-Track nutzt SBOMs zur Analyse von Software-Component-Risiken. ([owasp.org](https://owasp.org/www-project-dependency-track/?utm_source=chatgpt.com)) |
| Deployment | Deployment muss wiederholbar und rücksetzbar sein. | Ist Deployment automatisiert? Gibt es manuelle Schritte? Gibt es Rollback/Rollforward? | Helm Upgrade mit dokumentiertem Rollback. | Helm beschreibt Installation und Upgrade von Kubernetes-Anwendungen. ([helm.sh](https://helm.sh/?utm_source=chatgpt.com)) |
| Environments | Umgebungen müssen vergleichbar sein. | Wie werden Dev, Test, Abnahme, PreProd und Prod erzeugt? Gibt es Konfigurationsdrift? | Terraform erzeugt Basisinfrastruktur, Helm deployt Anwendung. | Terraform beschreibt wiederholbare Infrastruktur über Konfigurationsdateien. ([developer.hashicorp.com](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/infrastructure-as-code?utm_source=chatgpt.com)) |
| Secrets | Geheimnisse müssen zentral und kontrolliert verwaltet werden. | Wo liegen Secrets? Wie werden sie rotiert? Haben Pipelines nur minimale Rechte? Werden Secrets maskiert? | Pipeline nutzt kurzlebige Credentials statt statischer Admin-Tokens. | OWASP CI/CD Security Cheat Sheet. ([cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html?utm_source=chatgpt.com)) |
| Audit | Nachweise müssen ohne Heldentum verfügbar sein. | Kann man für Release X alle Nachweise innerhalb weniger Minuten zeigen? | Release-Dossier mit Commit, Build, Scans, Freigabe, Deployment. | NIST CSF 2.0 betont Governance und Risikomanagement. ([nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf?utm_source=chatgpt.com)) |

## 10. IaC-Bewertungskriterien

| Aspekt | Details/Erklärung | Bewertung gut | Bewertung kritisch | Literatur/Quelle |
|---|---|---|---|---|
| Versionierung | Infrastrukturdefinitionen liegen im Repository und werden wie Anwendungscode behandelt. | Pull Request, Review, Historie, Tags, Releases. | Lokale Skripte, Wiki-Anleitungen, manuelle Konsolenklicks. | Terraform-IaC-Dokumentation. ([developer.hashicorp.com](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/infrastructure-as-code?utm_source=chatgpt.com)) |
| Reproduzierbarkeit | Eine Umgebung kann aus Code erneut erzeugt oder plausibel rekonstruiert werden. | Module, feste Versionen, automatisierte Ausführung, dokumentierte Parameter. | „Nur Kollege X weiß, wie Prod gebaut wurde.“ | Terraform beschreibt Build/Change/Versioning von Infrastruktur. ([developer.hashicorp.com](https://developer.hashicorp.com/terraform/docs?utm_source=chatgpt.com)) |
| State Management | Terraform State ist geschützt, zentral und gegen parallele Änderungen gesichert. | Remote State, Locking, Verschlüsselung, Zugriffsschutz. | Lokale State-Dateien auf Entwicklernotebooks. | Terraform State-Dokumentation. ([developer.hashicorp.com](https://developer.hashicorp.com/terraform/language/state?utm_source=chatgpt.com)) |
| Idempotenz | Wiederholte Ausführung führt kontrolliert zum gleichen Zielzustand. | Ansible Playbooks und Terraform Apply sind wiederholbar. | Skripte erzeugen bei jedem Lauf neue Nebenwirkungen. | Ansible-Dokumentation zu Konfigurations- und Orchestrierungsaufgaben. ([docs.ansible.com](https://docs.ansible.com/?utm_source=chatgpt.com)) |
| Modularisierung | Wiederverwendbare Bausteine statt Copy-and-Paste. | Standardmodule für Netzwerk, Logging, IAM, Datenbank. | Jedes Projekt baut eigene Infrastrukturvarianten. | Terraform-Konfigurationen beschreiben Ressourcensammlungen in Dateien/Verzeichnissen. ([developer.hashicorp.com](https://developer.hashicorp.com/terraform/language?utm_source=chatgpt.com)) |
| Policy as Code | Regeln werden automatisiert geprüft. | Keine öffentlichen Buckets, keine offenen Security Groups, Mindest-Tags, Verschlüsselungspflicht. | Architekturregeln stehen nur in PowerPoint. | OWASP und CNCF betonen automatisierte Kontrollen entlang der Lieferkette. ([cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html?utm_source=chatgpt.com)) |
| Secrets | Keine Zugangsdaten in Repositories, State, Logs oder Artefakten. | Externer Secret Store, Rotation, Least Privilege. | Passwörter in `values.yaml`, `.tfvars`, Pipeline-Logs. | OWASP CI/CD Security Cheat Sheet. ([cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html?utm_source=chatgpt.com)) |
| Drift-Erkennung | Abweichungen zwischen Code und Realität werden erkannt. | GitOps-Reconciliation, Terraform Plan, Drift Reports. | Produktion wird manuell verändert und niemand merkt es. | OpenGitOps beschreibt kontinuierlichen Abgleich des Zielzustands. ([opengitops.dev](https://opengitops.dev/?utm_source=chatgpt.com)) |
| Umgebungsparität | Umgebungen unterscheiden sich nur bewusst und dokumentiert. | Gleiche Module, unterschiedliche Parameter. | Test und Produktion sind architektonisch verschieden. | Terraform-IaC-Ansatz unterstützt wiederverwendbare Konfigurationen. ([developer.hashicorp.com](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/infrastructure-as-code?utm_source=chatgpt.com)) |
| Betriebsübergabe | IaC ist verständlich, dokumentiert und betreibbar. | README, Runbooks, Ownership, Notfallverfahren. | Dienstleister liefert Code, aber Betrieb kann ihn nicht anwenden. | BSI-Test-/Freigabeprozess und NIST-Governance-Gedanke stützen Übergabe- und Nachweisfähigkeit. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2022/04_OPS_Betrieb/OPS_1_1_6_Software_Tests_und_Freigaben_Edition_2022.pdf?__blob=publicationFile&v=3&utm_source=chatgpt.com)) |

## 11. Pipeline Gates: Wo du harte und weiche Gates unterscheidest

Nicht jedes Gate muss hart blockieren, aber jedes Gate muss eine klare Entscheidung erzeugen. Harte Gates blockieren automatisch, wenn Mindestanforderungen nicht erfüllt sind. Weiche Gates erzeugen Befunde, die bewertet und dokumentiert werden müssen. In Behördenprojekten ist diese Unterscheidung wichtig, weil sonst entweder alles blockiert oder alles ignoriert wird.

| Aspekt | Details/Erklärung | Hartes Gate | Weiches Gate | Beispiel |
|---|---|---|---|---|
| Build Gate | Ohne erfolgreichen Build gibt es kein Artefakt. | Build fehlgeschlagen. | Nicht sinnvoll. | Maven Build bricht ab. |
| Unit-Test Gate | Basistests müssen grün sein. | Kritische Tests fehlgeschlagen. | Niedrige Coverage als Warnung. | Fachliche Kernlogik defekt. |
| SAST Gate | Kritische Code-Schwachstellen blockieren. | Kritischer Injection-Befund. | Medium Findings mit Ticket und Frist. | Unsicherer SQL-Zugriff. |
| SCA Gate | Kritische verwundbare Abhängigkeiten blockieren. | Kritische CVE mit Exploit-Pfad. | Veraltete Bibliothek ohne akuten Befund. | Vulnerable Logging Library. |
| Secret Gate | Geheimnisse im Code blockieren immer. | Token im Repository gefunden. | Nicht sinnvoll. | API-Key in Testdatei. |
| IaC Gate | Gefährliche Infrastrukturkonfiguration blockiert. | Öffentlich erreichbare Datenbank. | Fehlende Tags als Warnung. | Security Group `0.0.0.0/0` auf Admin-Port. |
| License Gate | Unzulässige Lizenzen blockieren. | Lizenz nicht kompatibel mit Nutzungsvorgaben. | Unklare Lizenz muss geprüft werden. | Unbekannte Transitive Dependency. |
| Abnahme Gate | Fachliche Abnahme vor Produktion. | Fehlende Abnahme. | Abnahme mit bekannten Einschränkungen. | Fachbereich genehmigt Release mit Restpunkt. |
| Betrieb Gate | Ohne Betriebsfähigkeit kein Go-live. | Kein Rollback, kein Monitoring, kein Runbook. | Dashboard-Erweiterung nachgelagert mit Frist. | Alert fehlt für neuen Batchlauf. |

Der Fehler, den du in Reviews sofort erkennen musst: Teams zeigen Scan-Tools, aber keine Entscheidungslogik. Ein Tool ohne Gate ist kein Kontrollpunkt, sondern ein Berichtsgenerator. Für Architektursteuerung zählt: Welche Befunde verhindern Promotion? Wer darf Ausnahmen genehmigen? Wie lange gelten Ausnahmen? Wo werden sie nachverfolgt? Wann wird ein Risiko erneut geprüft?

## 12. Secrets Management: der häufig unterschätzte Kern

Secrets Management ist eines der wichtigsten Pipeline-Themen, weil CI/CD-Systeme oft hochprivilegierte Automationsrechte besitzen. Ein kompromittierter Runner, ein geleakter Token oder ein zu breites Deployment-Secret kann produktive Systeme verändern. Deshalb darf eine Pipeline nicht mit dauerhaften Admin-Zugangsdaten arbeiten. Gute Zielbilder nutzen kurzlebige Credentials, Rollenbindung, Secret Stores, Maskierung, Rotation, getrennte Berechtigungen je Umgebung und minimale Rechte pro Job. OWASP behandelt Pipeline-Sicherheit explizit als eigenen Risikobereich und benennt unter anderem Pipeline-Zugriffe, Secrets, Artefakte und Supply-Chain-Risiken als zentrale Schutzobjekte. ([cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html?utm_source=chatgpt.com))

Für dich als Enterprise Architekt lautet die Review-Frage: „Welche Identität handelt hier eigentlich?“ Eine Pipeline ist ein nicht-menschlicher Akteur. Sie braucht eine eindeutige, begrenzte, überprüfbare Identität. Wenn alle Deployments mit einem generischen Superuser laufen, ist das kein Automatisierungsfortschritt, sondern ein verdeckter Architekturfehler.

## 13. Auditierbarkeit: Was ein Release-Dossier enthalten sollte

Für jedes produktive Release sollte ein Release-Dossier erzeugbar sein. Es muss nicht zwingend ein manuelles Dokument sein; besser ist ein automatisch zusammenstellbarer Nachweissatz. Enthalten sein sollten Release-Version, fachlicher Inhalt, Commit-IDs, Merge Requests, Reviewer, Build-ID, Artefakt-ID, Artefakt-Hash, SBOM, Scan-Ergebnisse, Testergebnisse, Ausnahmen, Freigaben, Deployment-Zeitpunkt, Zielumgebung, Smoke-Test-Ergebnis, Rollback-Hinweis, Monitoring-Hinweis und bekannte Einschränkungen.

Das Ziel ist nicht Papierproduktion. Das Ziel ist Rekonstruierbarkeit. Wenn drei Monate nach einem Vorfall gefragt wird, welche Version mit welcher verwundbaren Komponente wann und wohin ausgeliefert wurde, darf die Antwort nicht aus Chatverläufen, Erinnerungen und Excel-Dateien zusammengesucht werden müssen.

## 14. Beispiel: Behördenportal mit Fachverfahren und Registerschnittstelle

Angenommen, eine Behörde betreibt ein Online-Portal. Bürger stellen Anträge. Das Portal ruft ein API-Gateway auf, dahinter ein Fachverfahren, eine Registerschnittstelle, ein DMS und eine Datenbank. Der Dienstleister liefert neue Funktionen für Antragserfassung, Dokumentenupload und Statusabfrage.

Ein schwaches Liefermodell wäre: Entwickler bauen lokal, kopieren Artefakte in eine Umgebung, Betrieb passt Konfiguration manuell an, Security scannt gelegentlich, Abnahme erfolgt per E-Mail, Produktion wird nach Checkliste verändert. Dieses Modell ist langsam, fehleranfällig und kaum nachweisbar.

Ein starkes Liefermodell wäre: Codeänderungen laufen über Pull Requests. Die Pipeline baut ein Container Image, führt Tests und Scans aus, erzeugt eine SBOM und legt das Image unveränderlich in einer Registry ab. Terraform definiert Netzwerk, Datenbank, IAM-Rollen und Plattformressourcen. Helm beschreibt die Anwendung auf Kubernetes. Secrets liegen in einem Secret Store. GitOps synchronisiert den gewünschten Zielzustand in Test und Abnahme. Für Produktion erfolgt Promotion nach Freigabe. Deployment erzeugt Nachweise. Dashboards und Alerts werden mitgeliefert. Rollback ist auf die vorherige Image-/Chart-Version möglich.

Als EA bewertest du nicht nur, ob das technisch hübsch ist. Du bewertest, ob diese Lieferkette die fachliche Kritikalität trägt: Datenschutz, Registerverfügbarkeit, Nachvollziehbarkeit von Antragsständen, Betriebsfähigkeit, Incident-Fähigkeit und Dienstleistersteuerung.

## 15. Beispiel-Zielbild als Architekturbaustein

| Aspekt | Details/Erklärung | Zielanforderung | Abnahmekriterium |
|---|---|---|---|
| Source Code | Anwendungscode, IaC und Deployment-Konfiguration liegen in versionierten Repositories. | Alle produktionsrelevanten Änderungen erfolgen über Pull/Merge Requests. | Stichprobe zeigt: Produktiver Stand ist auf Commit und Review zurückführbar. |
| Build | Build läuft automatisiert in kontrollierter Umgebung. | Keine lokalen produktionsrelevanten Builds. | Artefakt enthält Build-ID, Commit-ID und Version. |
| Artefakt | Einmal bauen, mehrfach promoten. | Artefakt wird zwischen Umgebungen nicht neu gebaut. | Hash/Image Digest bleibt über Test, Abnahme und Produktion identisch. |
| Security | Security Gates sind verbindlich. | Kritische Befunde blockieren Promotion. | Pipeline-Protokoll zeigt blockierende Gates und dokumentierte Ausnahmen. |
| IaC | Infrastruktur ist versioniert und reproduzierbar. | Terraform/Ansible/Helm-Code ist Teil der Lieferung. | Testumgebung kann aus Code neu aufgebaut oder plausibel rekonstruiert werden. |
| GitOps | Zielzustand ist deklarativ und versioniert. | Produktive Deployments folgen versioniertem Zielzustand. | Abweichungen zwischen Git und Cluster werden erkannt und behandelt. |
| Secrets | Secrets liegen außerhalb des Codes. | Keine Secrets in Repositories, Artefakten, Logs oder Helm Values. | Secret Scan und Stichprobe sind unauffällig. |
| Betrieb | Betriebsfähigkeit wird mit jedem Release geliefert. | Runbooks, Monitoring, Alerts, Rollback und Known Issues sind aktualisiert. | Betriebsübergabe ist Bestandteil der Release-Abnahme. |
| Audit | Nachweise sind abrufbar. | Release-Dossier je produktivem Stand. | Auditorische Stichprobe kann vollständig beantwortet werden. |

## 16. Typische Fehler, die du als EA klar benennen solltest

Der erste Fehler ist „Pipeline-Theater“: Es gibt eine Pipeline, aber produktive Änderungen laufen teilweise daran vorbei. Das ist gefährlicher als keine Pipeline, weil es Scheinsicherheit erzeugt.

Der zweite Fehler ist „Build per Environment“: Für Test, Abnahme und Produktion wird jeweils neu gebaut. Dadurch ist nicht sicher, dass exakt derselbe Stand getestet und produktiv gesetzt wurde.

Der dritte Fehler ist „Security nur als Report“: SAST, SCA und Container Scans laufen zwar, aber Befunde blockieren nichts und landen nicht in einem verbindlichen Maßnahmenprozess.

Der vierte Fehler ist „Secrets in falschen Schichten“: Zugangsdaten liegen in Git, Helm Values, Terraform Variablen, Pipeline-Umgebungsvariablen ohne Schutz oder sogar in Logs.

Der fünfte Fehler ist „Terraform ohne State-Governance“: Infrastruktur wird zwar als Code definiert, aber State-Dateien liegen lokal, Zugriffe sind unklar, parallele Änderungen erzeugen Drift.

Der sechste Fehler ist „GitOps als Synonym für Git plus Pipeline“: GitOps bedeutet nicht, dass irgendwo YAML in Git liegt. Entscheidend sind deklarativer Zielzustand, Versionierung, automatisches Pull-Modell und kontinuierlicher Abgleich. ([opengitops.dev](https://opengitops.dev/?utm_source=chatgpt.com))

Der siebte Fehler ist „Helm als Template-Müllhalde“: Charts enthalten zu viele Sonderfälle, unklare Values, eingebettete Secrets und keine klare Versionierung.

Der achte Fehler ist „Betrieb kommt später“: Monitoring, Runbooks, Alerting und Rollback werden erst kurz vor Go-live diskutiert. Dann ist Betriebsfähigkeit nicht architektonisch eingebaut, sondern nachträglich angeklebt.

Der neunte Fehler ist „Dienstleisterabhängigkeit durch Toolwissen“: Der Dienstleister kann deployen, aber Auftraggeber und Betrieb können Lieferung, Risiken und Wiederanlauf nicht nachvollziehen.

Der zehnte Fehler ist „Keine Ausnahmeprozesse“: Es gibt nur bestanden/nicht bestanden. In echten Behördenprojekten braucht man befristete, begründete, genehmigte und nachverfolgte Ausnahmen, sonst werden Gates heimlich umgangen.

## 17. Wie du Mindestanforderungen in Ausschreibungen formulierst

Eine sehr gute Ausschreibungsanforderung verbindet Liefergegenstand, Qualität und Nachweis. Beispiel:

„Der Auftragnehmer erstellt eine CI/CD-Lieferpipeline für Anwendungscode, Infrastrukturcode und Deployment-Konfiguration. Die Pipeline muss Build, automatisierte Tests, Security Scans, Artefakterzeugung, Artefaktablage, Promotion, Deployment, Rollback und Nachweiserzeugung unterstützen. Für jede produktive Auslieferung ist nachzuweisen: Quellcommit, Build-ID, Artefaktversion, Testergebnisse, Security-Scan-Ergebnisse, SBOM, Freigaben, Deployment-Zeitpunkt, Zielumgebung und Rollback-Option.“

Dazu ein Abnahmekriterium:

„Die Anforderung gilt als erfüllt, wenn anhand einer produktionsnahen Beispieländerung gezeigt wird, dass ein Commit über Pull Request, Build, Tests, Security Gates, Artefaktablage, Deployment in Test, Promotion nach Abnahme und Deployment in Produktion nachvollziehbar durchlaufen wird und die zugehörigen Nachweise vollständig exportierbar oder einsehbar sind.“

Das ist stark, weil es nicht nur „Tool vorhanden“ prüft, sondern Lieferfähigkeit.

## 18. Mentales Modell für deine EA-Praxis

Merke dir vier Ebenen.

Die erste Ebene ist die Entwicklerfähigkeit: Kann das Team schnell, sauber und häufig integrieren?

Die zweite Ebene ist die Produktqualität: Wird nachweisbar getestet, geprüft und kontrolliert?

Die dritte Ebene ist die Betriebsfähigkeit: Kann das System stabil, wiederholbar, beobachtbar und rücksetzbar betrieben werden?

Die vierte Ebene ist die Steuerungsfähigkeit: Kann die Organisation Entscheidungen, Risiken, Freigaben und Lieferstände nachvollziehen?

Wenn eine Pipeline nur Ebene eins bedient, ist sie eine Entwicklerpipeline. Wenn sie alle vier Ebenen bedient, ist sie ein Architekturbaustein.

## 19. Übung: Pipeline-Review im Behördenprojekt

Stell dir folgendes Szenario vor: Ein Dienstleister liefert ein neues Modul für ein Antragsportal. Es gibt GitLab, Maven, Docker, Kubernetes und Helm. Terraform wird für Infrastruktur genutzt. Die Pipeline baut Images und deployt automatisch nach Test. Für Produktion gibt es ein manuelles Approval. Security Scans laufen, blockieren aber nicht. Secrets liegen teilweise als GitLab CI Variables. Helm Values enthalten Datenbanknamen und technische URLs. Runbooks werden einmal pro Quartal aktualisiert. Rollback wurde noch nie getestet.

Deine Aufgabe besteht aus fünf Schritten.

Erstens bewertest du die Pipeline entlang der Lieferkette: Source, Build, Test, Scan, Artefakt, Promotion, Deployment, Betrieb, Audit.

Zweitens identifizierst du die drei höchsten Risiken. In diesem Szenario wären das wahrscheinlich: Security Scans ohne Gate-Wirkung, unklare Secrets-Governance und fehlend getesteter Rollback.

Drittens formulierst du Mindestanforderungen. Beispiel: „Kritische Security-Befunde blockieren Promotion ab Abnahmeumgebung.“ Beispiel: „Secrets dürfen nicht in Repositories, Helm Values, Logs oder ungeschützten Pipeline-Variablen gespeichert werden.“ Beispiel: „Rollback muss für jedes Major-/Minor-Release in einer produktionsnahen Umgebung nachgewiesen werden.“

Viertens definierst du Abnahmekriterien. Beispiel: „Ein absichtlich eingebrachtes Test-Secret wird durch Secret Detection erkannt und blockiert.“ Beispiel: „Ein Helm Rollback auf die vorherige Version wird in PreProd demonstriert.“ Beispiel: „Für Release 1.3.0 kann ein Release-Dossier mit Commit, Build, Artefakt, Scans, Freigabe und Deployment gezeigt werden.“

Fünftens formulierst du eine Executive-Erklärung: „Die Pipeline ist nicht nur ein Entwicklerwerkzeug. Sie ist der kontrollierte Lieferweg des Fachverfahrens. Wenn dieser Lieferweg nicht prüfbar ist, können wir Qualität, Sicherheit, Betriebsfähigkeit und Dienstleisterleistung nicht belastbar steuern.“

## 20. Dein Prüfkompass für echte Termine

Wenn du in einem Architekturreview sitzt, stelle am Anfang nicht zu viele Detailfragen. Beginne mit diesen fünf Fragen:

„Können Sie mir für den aktuellen Produktionsstand den Commit, den Build, das Artefakt, die Testergebnisse, die Security-Befunde und die Freigabe zeigen?“

„Wird dasselbe Artefakt durch die Umgebungen promotet oder wird je Umgebung neu gebaut?“

„Welche Pipeline-Befunde blockieren eine Auslieferung wirklich?“

„Welche produktionsrelevanten Ressourcen werden manuell verändert und wie wird das in den Code zurückgeführt?“

„Wie sieht ein Rollback konkret aus, wer löst ihn aus, und wann wurde er zuletzt getestet?“

Mit diesen Fragen erkennst du schnell, ob eine Organisation nur Tooling besitzt oder echte Lieferarchitektur beherrscht.

## 21. Lernauftrag für dich als Enterprise Architekt

Dein Ziel ist nicht, jede Pipeline selbst zu bauen. Dein Ziel ist, Lieferfähigkeit architektonisch beurteilen und verbindlich einfordern zu können. Dafür musst du die Begriffe präzise verwenden, Artefaktflüsse verstehen, IaC-Werkzeuge unterscheiden, Security Gates fachlich einordnen, Nachweise verlangen und Betriebsübergaben verbessern.

Die wichtigste Kompetenz ist Übersetzung: Aus „Wir machen DevOps“ machst du prüfbare Architektur. Aus „Wir nutzen Terraform“ machst du Reproduzierbarkeit, State-Governance und Drift-Kontrolle. Aus „Wir haben Security Scans“ machst du blockierende Gates, Ausnahmeprozesse und Maßnahmenverfolgung. Aus „Wir deployen mit Helm“ machst du versionierte, rücksetzbare und betrieblich verstandene Kubernetes-Releases. Aus „Wir nutzen GitOps“ machst du deklarativen Zielzustand, Audit Trail und Drift-Erkennung.

Damit bist du nicht der Pipeline-Administrator. Du bist derjenige, der dafür sorgt, dass Softwarelieferung im Behördenkontext steuerbar, prüfbar und betreibbar wird. <>