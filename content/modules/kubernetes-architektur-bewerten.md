## Checkliste: Was du als Enterprise Architekt bei Kubernetes sofort prüfen musst

1. **Ist klar, welche fachlichen Verfahren auf der Plattform laufen dürfen und welchen Schutzbedarf sie haben?**  
2. **Ist die Mandantentrennung technisch, organisatorisch und betrieblich nachvollziehbar geregelt?**  
3. **Gibt es ein klares Betriebsmodell: Wer betreibt Cluster, Plattformdienste, Namespaces, Deployments und Anwendungen?**  
4. **Sind Images nachvollziehbar gebaut, geprüft, signiert, versioniert und aus einer kontrollierten Registry bezogen?**  
5. **Sind Namespaces, RBAC, Service Accounts und Rechte nach Least Privilege modelliert?**  
6. **Gibt es Resource Requests, Limits, Quotas und Regeln gegen unkontrollierten Ressourcenverbrauch?**  
7. **Sind Secrets nicht im Git, nicht im Image und nicht in Klartext-Konfigurationen abgelegt?**  
8. **Sind Netzwerkzonen, Ingress, Egress, Network Policies und Schnittstellenfreigaben dokumentiert?**  
9. **Gibt es Logging, Monitoring, Tracing, Alerting und Runbooks für Fach- und Plattformbetrieb?**  
10. **Sind Patchmanagement, Kubernetes-Versionen, Node-Images, Add-ons und Abhängigkeiten geregelt?**  
11. **Sind Backup, Restore, Disaster Recovery, RTO/RPO und Wiederanlauf getestet – nicht nur behauptet?**  
12. **Sind Helm Charts, Operators und Plattform-Add-ons versioniert, geprüft und updatefähig?**  
13. **Gibt es Security-Gates in der Lieferpipeline: Image-Scan, IaC-Scan, Policy-Check, Secret-Scan, Admission Control?**  
14. **Sind Abnahmekriterien messbar: Nachweise, Konfigurationen, Tests, Protokolle, Verantwortlichkeiten?**  
15. **Ist klar, welche Teile der Plattform Standard sind und welche projektindividuell verändert wurden?**

## 1. Der Kern: Kubernetes ist kein Server, sondern ein Steuerungssystem

Kubernetes ist ein Open-Source-System zur automatisierten Bereitstellung, Skalierung und Verwaltung containerisierter Anwendungen. Wichtig ist dabei: Kubernetes ist keine klassische, vollständige PaaS-Lösung, sondern eine orchestrierende Plattform, die viele Fähigkeiten bereitstellt, aber Logging, Monitoring, Alerting, Security-Policies, Registry, CI/CD und Betriebsprozesse typischerweise über ergänzende Komponenten integriert. Genau deshalb darfst du Kubernetes als Enterprise Architekt nicht als „Technik der Plattformleute“ betrachten, sondern als Architekturbaustein mit Auswirkungen auf Sicherheit, Betriebsfähigkeit, Nachweisfähigkeit, Kosten, Souveränität und Lieferfähigkeit. ([kubernetes.io](https://kubernetes.io/docs/concepts/overview/))

Der Denkfehler vieler Organisationen lautet: „Wir haben Kubernetes, also haben wir eine Plattform.“ Fachlich richtig wäre: „Wir haben mit Kubernetes einen Orchestrierungskern; ob daraus eine belastbare Plattform wird, entscheidet sich an Betriebsmodell, Security Controls, Standardisierung, Mandantentrennung, Observability, Lieferpipeline und Governance.“ Kubernetes allein löst also weder Architektur-Governance noch Betriebsübergabe noch Compliance. Es macht nur sichtbar, ob diese Dinge sauber gedacht wurden.

## 2. Das mentale Modell: Von Image bis Fachverfahren

Ein **Container** ist eine paketierte Laufzeitumgebung für eine Anwendung. Er enthält Anwendungscode, Runtime-Abhängigkeiten und Konfigurationserwartungen, aber idealerweise keine Secrets, keine Umgebungsspezifika und keine manuell eingebauten Besonderheiten. NIST beschreibt Container als Form der Betriebssystemvirtualisierung kombiniert mit Anwendungspaketierung; der Nutzen liegt in Portabilität, Wiederverwendbarkeit und Automatisierbarkeit, aber damit entstehen auch eigene Sicherheitsrisiken entlang Image, Registry, Orchestrator und Host. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/190/final))

Ein **Image** ist die Vorlage, aus der Container gestartet werden. Aus EA-Sicht ist ein Image kein technisches Nebenprodukt, sondern ein lieferbares Artefakt. Du musst fragen: Wer baut es? Aus welchem Base Image? Wird es gescannt? Ist es reproduzierbar? Ist es signiert? Gibt es eine SBOM? Wird es nur aus einer freigegebenen Registry gezogen? Gibt es Regeln gegen `latest`-Tags? Gibt es Lifecycle-Regeln für veraltete Images?

Eine **Registry** ist das Artefaktlager für Images. In einer Behördenplattform ist die Registry ein sicherheitsrelevanter Kontrollpunkt. Sie entscheidet, welche Software überhaupt in die Plattform gelangen kann. Eine unreife Plattform erkennt man oft daran, dass Images direkt aus öffentlichen Registries gezogen werden, ohne Mirror, Freigabeprozess, Signaturprüfung oder Schwachstellenbewertung. Das ist architektonisch gefährlich, weil die Lieferkette nicht beherrscht wird.

Ein **Pod** ist die kleinste deploybare Einheit in Kubernetes. Ein Pod kann einen oder mehrere Container enthalten und teilt sich Netzwerk- und Storage-Kontext. Als Enterprise Architekt musst du nicht jeden Pod administrieren können, aber du musst verstehen: In Kubernetes wird nicht „ein Container“ als langlebiger Server betrieben; stattdessen wird ein gewünschter Zielzustand beschrieben, und Kubernetes versucht, diesen Zustand laufend herzustellen. ([kubernetes.io](https://kubernetes.io/docs/concepts/workloads/pods/?utm_source=chatgpt.com))

Ein **Deployment** beschreibt, wie viele Replikate einer Anwendung laufen sollen und wie Updates ausgerollt werden. Hier beginnt die Architekturfrage nach Verfügbarkeit, Rollout-Strategie, Skalierung, Ressourcenverbrauch und Rückfallfähigkeit. Wenn ein Fachverfahren nur mit einem Pod ohne Deployment, ohne Health Checks, ohne Limits und ohne Rollback betrieben wird, ist das kein professioneller Plattformbetrieb, sondern eine Containerablage.

Ein **Service** macht Pods stabil erreichbar. Pods kommen und gehen; Services geben Anwendungen eine stabile interne Adresse. Ein **Ingress** regelt typischerweise externen HTTP/HTTPS-Zugriff auf Services, etwa über Hostnamen, Pfade, TLS-Terminierung und Routing-Regeln. Kubernetes beschreibt Ingress als API-Objekt für externen Zugriff auf Services, typischerweise HTTP, inklusive Load Balancing, SSL/TLS-Terminierung und namensbasiertem Routing. ([kubernetes.io](https://kubernetes.io/docs/concepts/services-networking/ingress/?utm_source=chatgpt.com))

Eine **ConfigMap** enthält nicht-sensitive Konfiguration, zum Beispiel Feature-Schalter, URLs oder technische Parameter. Ein **Secret** enthält sensitive Informationen wie Passwörter, Token oder Schlüssel. Kubernetes erlaubt, Konfiguration und Secrets getrennt vom Image zu verwalten, damit Images nicht pro Umgebung neu gebaut werden müssen und sensitive Informationen nicht im Stack hart kodiert werden. Das ist sauber – aber nur dann, wenn Secrets zusätzlich verschlüsselt, zugriffsbeschränkt, rotiert und nicht unkontrolliert in Logs oder Umgebungsvariablen offengelegt werden. ([kubernetes.io](https://kubernetes.io/docs/concepts/overview/))

Ein **Namespace** ist eine logische Trennung innerhalb eines Clusters. Er eignet sich für Team-, Verfahrens-, Umgebungs- oder Mandantenabgrenzung. Aber: Ein Namespace ist keine harte Sicherheitsgrenze wie ein vollständig separater Cluster. Für hohen Schutzbedarf, unterschiedliche Mandanten oder stark getrennte Verantwortungsräume muss geklärt werden, ob Namespaces reichen oder ob getrennte Cluster, getrennte Netzwerkzonen, getrennte IAM-Strukturen oder sogar getrennte Betriebsdomänen erforderlich sind.

**Resource Requests und Limits** beschreiben, welche CPU- und Speicherressourcen eine Anwendung benötigt und maximal verbrauchen darf. Ohne diese Angaben kann eine einzelne fehlerhafte Anwendung andere Workloads beeinträchtigen. Aus Architekturperspektive geht es hier um Betriebsstabilität, Kostenkontrolle und Fairness zwischen Verfahren. In Behördenumgebungen ist das besonders relevant, weil mehrere Fachverfahren, Umgebungen und Dienstleister auf derselben Plattform konkurrieren können.

**Helm** ist der Paketmanager für Kubernetes. Helm Charts beschreiben Kubernetes-Ressourcen einer Anwendung und helfen dabei, komplexe Anwendungen wiederholbar zu installieren, zu versionieren und zu aktualisieren. Helm bietet auch Rollback-Möglichkeiten. Architektonisch ist Helm nicht nur Komfort, sondern ein Standardisierungsinstrument: Ein gutes Chart macht Deployments reproduzierbar; ein schlechtes Chart versteckt Wildwuchs, überprivilegierte Rechte, unsichere Defaults und unklare Abhängigkeiten. ([helm.sh](https://helm.sh/))

**Operators** erweitern Kubernetes um anwendungsspezifische Automatisierung. Sie nutzen Custom Resources und Controller, um komplexe Betriebsaufgaben zu automatisieren, etwa Backups, Upgrades, Schemaänderungen oder Failover. Das ist mächtig, aber auch riskant: Ein Operator ist faktisch ein automatisierter Administrator im Cluster. Deshalb musst du fragen, welche Rechte er hat, wer ihn patcht, wer seine CRDs versteht, wie er getestet wird und was passiert, wenn der Operator selbst ausfällt. ([kubernetes.io](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/))

**Network Policies** steuern, welche Pods mit welchen anderen Pods oder Zielen kommunizieren dürfen. Standardmäßig ist ohne Network Policies in einem Namespace der Verkehr zu und von Pods erlaubt; erst durch Policies wird Isolation hergestellt. Kubernetes beschreibt explizit Default-Deny-Policies für Ingress, Egress oder beides. Für Behördenplattformen ist diese Information zentral: Ohne explizite Netzwerkpolitik ist eine Namespace-Struktur noch keine saubere Segmentierung. ([kubernetes.io](https://kubernetes.io/docs/concepts/services-networking/network-policies/))

**Storage** in Kubernetes wird über Volumes, PersistentVolumes und PersistentVolumeClaims abstrahiert. Kubernetes trennt dabei die Bereitstellung von Storage von der Nutzung durch Pods. Für Enterprise Architecture bedeutet das: Du musst nicht nur fragen, ob Storage funktioniert, sondern ob Verschlüsselung, Backup, Restore, Performance, Datenklassifikation, Löschkonzept, Standort, Replikation und Eigentum geklärt sind. ([kubernetes.io](https://kubernetes.io/docs/concepts/storage/persistent-volumes/))

**Observability** umfasst Logs, Metriken und Traces. OpenTelemetry beschreibt sich als herstellerneutrales Observability-Framework zur Instrumentierung, Generierung, Sammlung und Weitergabe von Telemetriedaten wie Traces, Metriken und Logs. Für dich als Enterprise Architekt ist entscheidend: Observability ist nicht „nice to have“, sondern Voraussetzung für Betrieb, Abnahme, Incident Management, SLA/SLO-Steuerung und Fehleranalyse über verteilte Behördenverfahren hinweg. ([opentelemetry.io](https://opentelemetry.io/docs/))

## 3. Warum Kubernetes im Behördenkontext ein Architekturthema ist

In Behördenumgebungen laufen Fachverfahren oft mit personenbezogenen Daten, Registerbezügen, Dokumenten, Nachweisen, Fristen, Bescheiden, Zahlungen oder integrationskritischen Schnittstellen. Eine Containerplattform ist dort kein neutraler Technikraum, sondern ein Ort, an dem Schutzbedarf, Betriebspflichten, Nachweisführung, Verantwortlichkeiten und Vergabesteuerung zusammenkommen. Das BSI führt mit **APP.4.4 Kubernetes** einen eigenen IT-Grundschutz-Baustein für Einrichtung, Betrieb, Orchestrierung und spezialisierte Infrastruktur von Kubernetes-Clustern; für Containerisierung verweist **SYS.1.6 Containerisierung** auf diesen Kubernetes-Baustein, wenn Container orchestriert werden. ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/06_APP_Anwendungen/APP_4_4_Kubernetes_Edition_2023.pdf?__blob=publicationFile&v=4&utm_source=chatgpt.com))

Das bedeutet praktisch: Wenn eine Behörde Kubernetes einführt, entsteht nicht nur eine neue Laufzeitumgebung. Es entstehen neue Anforderungen an Berechtigungskonzepte, Mandantentrennung, Netzsegmentierung, Lieferkettenkontrolle, Sicherheitsprüfung, Protokollierung, Betriebsübergabe, Notfallvorsorge und Dienstleistersteuerung. Genau dort liegt deine Rolle als Enterprise Architekt: Du übersetzt Plattformtechnik in prüfbare Architektur-, Betriebs- und Sicherheitsanforderungen.

## 4. Die wichtigsten Bewertungsdimensionen

### 4.1 Mandantentrennung

Mandantentrennung ist die Frage, ob unterschiedliche Verfahren, Teams, Dienstleister, Schutzbedarfe oder Organisationseinheiten sauber voneinander getrennt sind. Eine einfache Namespace-Trennung kann für Entwicklungsumgebungen oder niedrige Schutzbedarfe genügen. Für produktive Verfahren mit erhöhtem Schutzbedarf kann sie zu schwach sein, insbesondere wenn gemeinsame Nodes, gemeinsame Ingress-Controller, gemeinsame Cluster-Add-ons, gemeinsame Admins oder unklare Network Policies existieren.

Du fragst hier nicht: „Gibt es Namespaces?“ Du fragst: „Welche Schutzgrenze soll der Namespace leisten, und wodurch wird sie technisch, organisatorisch und betrieblich abgesichert?“ Gute Antworten nennen Namespaces, RBAC, Network Policies, ResourceQuotas, Admission Policies, Pod Security Standards, separate Service Accounts, getrennte Secrets, getrennte Logsichten, getrennte Deployment-Rechte und eine dokumentierte Cluster-/Mandantenstrategie.

### 4.2 Schutzbedarf und Zonierung

Schutzbedarf ist die Grundlage jeder Plattformentscheidung. Eine Plattform für interne Testsysteme ist anders zu bewerten als eine Plattform für produktive Fachverfahren mit personenbezogenen Daten. In einer Behördenarchitektur musst du prüfen, ob die Plattform nach Datenklassen und Netzbereichen organisiert ist: Internetnaher Ingress, interne Fachverfahren, Registeranbindungen, Datenbankzonen, DMS-Zugriffe, Adminzugänge, Monitoring-Systeme und CI/CD-Verbindungen dürfen nicht zufällig entstehen.

Eine belastbare Plattformarchitektur beschreibt deshalb Netzwerkzonen, Kommunikationsbeziehungen, erlaubte Protokolle, Egress-Regeln, DNS-Nutzung, Zertifikatsmanagement, TLS-Terminierung, mTLS-Bedarfe, API-Gateway-Integration und Firewall-/CNI-Verantwortlichkeiten. Besonders kritisch ist Egress: Viele Plattformen kontrollieren eingehenden Verkehr gut, lassen aber ausgehenden Verkehr zu großzügig zu. Das ist im Behördenkontext ein Risiko, weil Datenabfluss, Schattenintegration und unkontrollierte Drittanbieterzugriffe entstehen können.

### 4.3 Betriebsverantwortung

Ein Kubernetes-Cluster hat mehrere Verantwortungszonen. Es gibt den Betrieb der Control Plane, den Betrieb der Worker Nodes, den Betrieb der Plattformdienste, den Betrieb der Add-ons, den Betrieb der Anwendungen und den Betrieb der Lieferpipeline. Wenn diese Schichten nicht getrennt beschrieben werden, entsteht später der klassische Fehler: Im Incident weiß jeder, was er nicht verantwortet.

Eine gute Plattform hat ein RACI-Modell. Darin steht, wer Kubernetes-Versionen patcht, wer Node-Images aktualisiert, wer Ingress-Controller betreibt, wer Zertifikate rotiert, wer StorageClasses verantwortet, wer Cluster-Add-ons freigibt, wer Namespaces anlegt, wer Deployments durchführen darf, wer Logs sehen darf, wer Secrets verwaltet und wer bei Sicherheitsvorfällen entscheidet. Ohne diese Klarheit ist Kubernetes nur technisch modern, aber organisatorisch unreif.

### 4.4 Patchmanagement

Patchmanagement betrifft Kubernetes selbst, die Nodes, Container-Runtimes, Betriebssysteme, Ingress-Controller, CNI-Plugins, CSI-Plugins, Helm Charts, Operators, Sidecars, Base Images und Anwendungen. Eine Plattform ist nicht patchfähig, nur weil sie „automatisiert“ ist. Patchfähigkeit bedeutet: Versionen sind inventarisiert, Abhängigkeiten sind bekannt, Updates sind testbar, Rollbacks sind möglich, Wartungsfenster sind definiert, Sicherheitsupdates werden priorisiert und Auswirkungen auf Fachverfahren sind bewertbar.

Für Behörden ist zusätzlich wichtig, dass Patches nicht nur durchgeführt, sondern nachgewiesen werden. Du brauchst also Evidence: Patchkalender, Versionstabellen, Schwachstellenberichte, Change Records, Testergebnisse, Rollback-Protokolle und Freigabevermerke.

### 4.5 Backup, Restore und Disaster Recovery

Kubernetes macht Anwendungen nicht automatisch wiederherstellbar. Deployments und Helm Charts können Infrastrukturzustände rekonstruieren, aber persistente Daten, Secrets, CRDs, Operator-Zustände, Volumes, Datenbanken und externe Abhängigkeiten müssen bewusst gesichert werden. Operators können Backups und Restores automatisieren, aber nur dann, wenn das Konzept getestet ist und Verantwortlichkeiten klar sind. ([kubernetes.io](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/))

Die zentrale Architekturfrage lautet: „Was muss nach einem Plattformausfall in welcher Reihenfolge wiederhergestellt werden?“ Daraus entstehen Anforderungen an RTO, RPO, Backup-Frequenz, Restore-Test, Abhängigkeitsreihenfolge, Datenintegrität, Zertifikate, Secret-Rotation, DNS, Ingress, externe Schnittstellen und Notbetrieb.

### 4.6 Monitoring, Logging und Tracing

Eine Behördenplattform muss drei Ebenen beobachten: Clusterzustand, Plattformdienste und Fachverfahren. Clusterzustand umfasst Nodes, Pods, Ressourcenverbrauch, Scheduling, API-Server, etcd, CNI, CSI, DNS und Ingress. Plattformdienste umfassen Registry, CI/CD, Secret-Management, Logging-Stack, Monitoring, Service Mesh, Policy Engine und Zertifikatsmanagement. Fachverfahren umfassen Verfügbarkeit, Fehlerquoten, Antwortzeiten, Transaktionen, fachliche Events und Schnittstellenketten.

Gute Observability beantwortet nicht nur „Ist der Pod grün?“, sondern: „Kann der Bürgerantrag eingereicht werden? Wird die Registerabfrage innerhalb der SLO beantwortet? Gibt es erhöhte Fehler im DMS? Ist ein bestimmter Release auffällig? Können wir einen Request über Portal, API-Gateway, Fachverfahren und Datenbank korrelieren?“ Genau deshalb sind Correlation IDs, strukturierte Logs und Tracing architekturrelevant.

### 4.7 Deployment und Release

Deployment ist das technische Ausrollen. Release ist die fachliche Verfügbarkeit einer Funktion. Diese Unterscheidung ist wichtig: Kubernetes kann neue Versionen deployen, aber die Behörde muss entscheiden, wann eine Funktion produktiv freigegeben wird, wie Fachabnahme erfolgt, welche Datenmigration nötig ist, wie Rollback funktioniert und wer im Fehlerfall entscheidet.

Aus EA-Sicht sind gute Deployment-Modelle reproduzierbar, Git-basiert, prüfbar und umgebungsübergreifend konsistent. Typische Bausteine sind Helm, GitOps, Pipeline-Gates, signierte Images, automatisierte Tests, Policy-as-Code, getrennte Umgebungen und nachvollziehbare Promotions von Dev über Test und Abnahme nach Produktion.

### 4.8 Rechte und Secrets

Kubernetes RBAC ist ein zentraler Sicherheitsmechanismus. Die offiziellen Kubernetes-Empfehlungen betonen Least Privilege, Namespace-bezogene Rechte statt Cluster-weite Rechte, Vermeidung von Wildcard-Berechtigungen und besondere Vorsicht bei `system:masters`, weil diese Gruppe praktisch uneingeschränkte Superuser-Rechte hat. ([kubernetes.io](https://kubernetes.io/docs/concepts/security/rbac-good-practices/))

Secrets sind noch kritischer. Du prüfst: Werden Secrets aus einem zentralen Secret Manager bezogen? Gibt es Rotation? Gibt es getrennte Secrets pro Umgebung und Mandant? Sind Secrets im Git ausgeschlossen? Werden Secrets in Logs maskiert? Wer darf sie lesen? Gibt es Break-Glass-Verfahren? Sind Zertifikate automatisiert erneuerbar? Eine Plattform ohne Secrets-Konzept ist im Behördenkontext nicht abnahmefähig.

## 5. Plattform-Review-Checkliste

| Aspekt | Details/Erklärung | Gute Nachweise | Warnsignal | Literatur/Quelle |
|---|---|---|---|---|
| Plattformzweck | Klärt, welche Verfahren, Schutzbedarfe und Umgebungen auf der Plattform laufen dürfen. | Plattformstrategie, Verfahrensliste, Schutzbedarfszuordnung. | „Alle Anwendungen können grundsätzlich drauf.“ | BSI APP.4.4 Kubernetes ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/06_APP_Anwendungen/APP_4_4_Kubernetes_Edition_2023.pdf?__blob=publicationFile&v=4&utm_source=chatgpt.com)) |
| Mandantentrennung | Bewertet Namespaces, Clustergrenzen, Nodes, Netzwerk, Rechte, Logs und Secrets. | Mandantenmodell, Namespace-Standards, RBAC, Quotas, Network Policies. | Namespace wird pauschal als Sicherheitsgrenze verkauft. | Kubernetes Network Policies ([kubernetes.io](https://kubernetes.io/docs/concepts/services-networking/network-policies/)) |
| Image-Lieferkette | Prüft Build, Base Images, Registry, Scans, Signaturen, SBOM und Freigaben. | Pipeline-Protokolle, Scanreports, Registry-Policy, Signaturprüfung. | Direkter Pull aus öffentlichen Registries. | NIST SP 800-190 ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/190/final)) |
| Registry | Bewertet, ob Images kontrolliert, versioniert und lifecycle-gesteuert abgelegt werden. | Private Registry, Retention, Vulnerability-Scan, Freigabestatus. | `latest` in Produktion. | NIST SP 800-190 ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/190/final)) |
| RBAC | Prüft Least Privilege für Menschen, Pipelines, Service Accounts und Operators. | Rollenmodell, RoleBindings, Auditlogs, Rezertifizierung. | ClusterRoleBindings ohne Begründung. | Kubernetes RBAC Good Practices ([kubernetes.io](https://kubernetes.io/docs/concepts/security/rbac-good-practices/)) |
| Secrets | Bewertet Secret-Ablage, Zugriff, Rotation, Verschlüsselung und Protokollierung. | Secret-Management-Konzept, Rotationstests, Zugriffsmatrix. | Secrets in Git, Helm values oder Images. | Kubernetes Overview ([kubernetes.io](https://kubernetes.io/docs/concepts/overview/)) |
| Network Policies | Prüft Default-Deny, erlaubte Kommunikationsbeziehungen und Egress-Kontrolle. | Policy-Matrix, Tests, CNI-Nachweis, Firewall-Abgleich. | Keine Egress-Regeln. | Kubernetes Network Policies ([kubernetes.io](https://kubernetes.io/docs/concepts/services-networking/network-policies/)) |
| Ingress | Prüft externen Zugriff, TLS, Zertifikate, Routing, WAF/API-Gateway-Integration. | Ingress-Standard, TLS-Konzept, Zertifikatsrotation, Freigabeprozess. | Jeder Dienstleister definiert eigene Ingress-Regeln. | Kubernetes Ingress ([kubernetes.io](https://kubernetes.io/docs/concepts/services-networking/ingress/?utm_source=chatgpt.com)) |
| Storage | Prüft PersistentVolumes, Verschlüsselung, Backup, Performance und Datenstandort. | StorageClass-Konzept, Backupplan, Restore-Protokolle, Datenklassifikation. | Stateful Workloads ohne Restore-Test. | Kubernetes Persistent Volumes ([kubernetes.io](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)) |
| Observability | Prüft Logs, Metriken, Traces, Dashboards, Alerts und Runbooks. | Dashboard-Katalog, Alert-Regeln, Trace-Beispiele, Incident-Protokolle. | Nur Infrastrukturmetriken, keine fachlichen SLOs. | OpenTelemetry ([opentelemetry.io](https://opentelemetry.io/docs/)) |
| Helm | Bewertet Chart-Qualität, Versionierung, Values, Defaults und Rollback. | Chart-Repository, Review-Regeln, Versionen, Rollback-Test. | Copy-paste YAML ohne Standardisierung. | Helm ([helm.sh](https://helm.sh/)) |
| Operators | Prüft Rechte, Updates, CRDs, Backup, Automatisierungslogik und Ausfallverhalten. | Operator-Inventar, Rechteprüfung, Upgradeplan, Betriebsdoku. | Operator mit Cluster-Admin-Rechten ohne Begründung. | Kubernetes Operator Pattern ([kubernetes.io](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)) |
| Resource Governance | Prüft Requests, Limits, Quotas, Prioritäten und Kapazitätsplanung. | Namespace-Quotas, LimitRanges, Kapazitätsreporting. | Anwendungen ohne Limits. | Kubernetes Security Checklist ([kubernetes.io](https://kubernetes.io/docs/concepts/security/security-checklist/)) |
| Patchmanagement | Bewertet Kubernetes-, Node-, Add-on-, Operator- und Image-Patching. | Patchkalender, Versionstabellen, CVE-Prozess, Testnachweise. | Unklare Zuständigkeit für Add-ons. | BSI APP.4.4 Kubernetes ([bsi.bund.de](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/06_APP_Anwendungen/APP_4_4_Kubernetes_Edition_2023.pdf?__blob=publicationFile&v=4&utm_source=chatgpt.com)) |
| Abnahmefähigkeit | Prüft, ob Architektur, Security, Betrieb und Lieferpipeline nachweisbar erfüllt sind. | Abnahmekatalog, Evidence-Ordner, Testprotokolle, ADRs. | „Das sieht man im Cluster.“ | Kubernetes Security Checklist ([kubernetes.io](https://kubernetes.io/docs/concepts/security/security-checklist/)) |

## 6. Zielbild-Vorlage für eine Behörden-Containerplattform

### 6.1 Zielbild in einem Satz

Die Behörde betreibt eine standardisierte, mandantenfähige, nachvollziehbar gesicherte und automatisiert belieferbare Containerplattform auf Kubernetes-Basis, auf der freigegebene Fachverfahren gemäß Schutzbedarf, Betriebsmodell, Netzwerkzonierung, Lieferkettenkontrolle und Observability-Anforderungen betrieben werden.

### 6.2 Architekturprinzipien

Das erste Prinzip lautet: **Keine Workloads ohne Eigentümer, Schutzbedarf und Betriebsmodell.** Jede Anwendung braucht einen fachlichen Owner, einen technischen Owner, eine Schutzbedarfsbewertung, eine Betriebsverantwortung, ein Deployment-Modell, ein Backup-/Restore-Konzept und eine definierte Observability-Anforderung.

Das zweite Prinzip lautet: **Keine Images ohne kontrollierte Lieferkette.** Images werden reproduzierbar gebaut, gescannt, versioniert, signiert und aus einer freigegebenen Registry bezogen. Produktive Deployments dürfen keine unkontrollierten öffentlichen Images verwenden.

Das dritte Prinzip lautet: **Keine produktiven Namespaces ohne Baseline Controls.** Jeder produktive Namespace erhält RBAC, ResourceQuotas, LimitRanges, Network Policies, Pod Security Standards, Secret-Anbindung, Logging, Monitoring und definierte Deployment-Rechte.

Das vierte Prinzip lautet: **Keine Plattform ohne Nachweisfähigkeit.** Architekturentscheidungen, Ausnahmen, Sicherheitsprüfungen, Deployments, Patches, Changes, Restore-Tests und Incidents werden dokumentiert und auditierbar abgelegt.

### 6.3 Zielbild-Bausteine

Die Plattform besteht aus einer Kubernetes-Laufzeit, einer privaten Registry, einer CI/CD- oder GitOps-Anbindung, zentralem Secret Management, Ingress/API-Gateway-Anbindung, zentralem Logging, Monitoring und Tracing, Policy Enforcement, Backup-/Restore-Komponenten, Storage-Integration, IAM/RBAC-Anbindung und einem Betriebsportal oder Servicekatalog für Teams.

Die Mandantentrennung wird über ein abgestuftes Modell geregelt. Für niedrigen Schutzbedarf können Namespaces innerhalb eines Clusters ausreichend sein. Für erhöhten oder sehr hohen Schutzbedarf werden getrennte Cluster, dedizierte Nodes, getrennte Netzbereiche, getrennte Adminrollen oder zusätzliche technische Isolation geprüft. Diese Entscheidung wird nicht aus Bequemlichkeit getroffen, sondern aus Schutzbedarf, Risiko und Betriebsverantwortung abgeleitet.

Die Lieferpipeline erzeugt signierte Images, scannt Abhängigkeiten, prüft Kubernetes-Manifeste oder Helm Charts, verhindert Secrets im Quellcode, prüft Policies vor dem Deployment und schreibt Deployment-Nachweise. Ein Release in Produktion erfolgt nur, wenn definierte Gates erfüllt sind.

Die Observability-Baseline umfasst technische und fachliche Sicht. Technisch werden Nodes, Pods, Ressourcen, Ingress, API-Server, DNS, Storage und Plattformdienste überwacht. Fachlich werden Antwortzeiten, Fehlerquoten, Transaktionsabbrüche, Schnittstellenfehler, Queue-Längen, Registerabfragen und DMS-Aufrufe beobachtet. Traces verbinden Portal, API-Gateway, Fachverfahren, Register, DMS und Datenbank.

## 7. Die wichtigsten Architekturfragen für Behördenplattformen

### Mandantentrennung

Welche Mandanten, Fachverfahren, Dienstleister und Umgebungen sollen auf derselben Plattform laufen? Welche Schutzbedarfe haben sie? Welche Trennmechanismen werden eingesetzt: Namespaces, getrennte Cluster, dedizierte Nodes, Netzwerkzonen, getrennte Ingress-Controller, getrennte Service Accounts, getrennte Secrets, getrennte Log-Sichten? Wer hat clusterweite Rechte? Welche Ausnahmen existieren?

### Schutzbedarf

Welche Daten werden verarbeitet: personenbezogene Daten, besondere Kategorien, Dokumente, Registerdaten, Zahlungsdaten, interne Verwaltungsdaten, Protokolldaten? Welche Anforderungen ergeben sich an Verschlüsselung, Protokollierung, Zugriff, Löschung, Datenstandort, Backup, Mandantentrennung und Incident Response?

### Betriebsverantwortung

Wer betreibt Control Plane, Worker Nodes, Add-ons, Registry, CI/CD, Secret Manager, Monitoring, Logging, Ingress, Storage und Anwendungen? Welche SLAs/SLOs gelten? Wer ist im Incident zuständig? Wer darf produktive Änderungen durchführen? Wie werden Dienstleister eingebunden?

### Patchmanagement

Wie häufig werden Kubernetes, Nodes, Container Runtime, Betriebssysteme, Ingress-Controller, CNI, CSI, Operators, Helm Charts und Base Images aktualisiert? Gibt es einen CVE-Prozess? Gibt es Testcluster? Wie wird Kompatibilität geprüft? Wer genehmigt Notfallpatches? Wie wird dokumentiert?

### Backup und Restore

Was wird gesichert: Cluster-Konfiguration, etcd, PersistentVolumes, Datenbanken, Secrets, CRDs, Operator-Zustände, Helm-Releases, Git-Repositories, Registry-Artefakte? Wie oft wird wiederhergestellt getestet? Welche RTO/RPO gelten je Verfahren? Wer entscheidet über Notbetrieb?

### Monitoring und Logging

Welche Logs werden gesammelt? Sind sie strukturiert? Gibt es Correlation IDs? Wer darf Logs lesen? Enthalten Logs sensitive Daten? Gibt es fachliche Dashboards? Gibt es Alert-Regeln mit klarer Zuständigkeit? Gibt es Runbooks? Werden Incidents nachbereitet?

### Deployment und Release

Wie kommen Anwendungen auf die Plattform? Wer darf deployen? Gibt es getrennte Umgebungen? Wird promotionfähig gebaut, also dasselbe Artefakt durch Dev, Test, Abnahme und Produktion bewegt? Gibt es Rollback? Gibt es Datenbankmigrationen? Gibt es Feature Flags? Wie wird fachlich abgenommen?

### Rechte und Secrets

Welche Benutzer, Gruppen, Service Accounts und Pipeline-Identitäten gibt es? Sind Rechte zeitlich begrenzt? Gibt es Break-Glass-Zugänge? Wie werden Secrets erstellt, rotiert, widerrufen und geprüft? Gibt es Zugriff auf Secrets über Logs, Debug-Shells oder Umgebungsvariablen?

### Netzwerkzonen

Welche Ingress-Wege gibt es aus Internet, Behördennetz, internen Netzen und Partnernetzen? Welche Egress-Ziele sind erlaubt? Gibt es Default-Deny? Wie werden Register, DMS, Datenbanken, externe APIs und Legacy-Systeme angebunden? Gibt es DNS- und Zertifikatskonzept?

### Skalierung

Welche Verfahren müssen horizontal skalieren? Welche Lastprofile gibt es? Gibt es Autoscaling? Sind Ressourcenlimits gesetzt? Wie wird Kapazität geplant? Gibt es Prioritätsklassen für kritische Verfahren? Was passiert bei Lastspitzen, etwa Fristende, Antragswellen oder Batchverarbeitung?

### Abnahme

Welche Mindestnachweise muss ein Dienstleister liefern? Welche Security-Scans sind Pflicht? Welche Betriebsdokumente? Welche Dashboards? Welche Runbooks? Welche Restore-Tests? Welche Architekturentscheidungen? Welche Risikoakzeptanzen? Welche offenen Punkte verhindern Go-live?

## 8. Typische Fehler, die du erkennen musst

Der erste Fehler ist **Kubernetes als Modernisierungsnachweis zu missverstehen**. Nur weil eine Anwendung containerisiert ist, ist sie nicht automatisch modern, sicher, skalierbar oder betreibbar. Ein schlecht gebauter Monolith im Container bleibt ein schlecht gebauter Monolith – nur mit YAML drumherum.

Der zweite Fehler ist **Namespace-Mandantentrennung zu überschätzen**. Namespaces sind hilfreich, aber keine vollständige Sicherheitsgrenze. Ohne RBAC, Network Policies, Quotas, Pod Security, getrennte Secrets und klare Adminprozesse ist der Namespace eher Ordnungskategorie als Schutzmechanismus.

Der dritte Fehler ist **Secrets zu verharmlosen**. Secrets in Git, Helm values, Umgebungsvariablen, Tickets, Wikis oder Logs sind ein schwerer Architekturfehler. Ein Secret-Konzept muss Rotation, Zugriff, Verschlüsselung, Maskierung, Notfallzugriff und Audit umfassen.

Der vierte Fehler ist **fehlende Egress-Kontrolle**. Viele Teams denken an eingehenden Zugriff, aber nicht an ausgehenden Verkehr. Gerade ausgehender Verkehr entscheidet, ob Workloads unkontrolliert externe Dienste erreichen oder Daten abfließen können.

Der fünfte Fehler ist **unklares Operator-Risiko**. Operators automatisieren Betrieb, aber sie haben oft weitreichende Rechte. Ein nicht verstandener Operator kann Backups, Datenbanken, Zertifikate oder Cluster-Ressourcen verändern. Deshalb gehören Operators ins Plattform-Inventar und in die Rechteprüfung.

Der sechste Fehler ist **Deployments ohne Betriebsreife**. Eine Anwendung ist nicht bereit für Produktion, wenn sie nur startet. Sie braucht Health Checks, Readiness, Liveness, Ressourcenlimits, Logs, Metriken, Traces, Alerts, Runbooks, Rollback und Restore-Fähigkeit.

Der siebte Fehler ist **fehlende Plattformprodukt-Sicht**. Eine Kubernetes-Plattform muss wie ein internes Produkt geführt werden: mit Servicekatalog, Standards, Supportmodell, Roadmap, Lifecycle, Dokumentation, Onboarding und klaren Schnittstellen zu Entwicklung, Betrieb und Security.

Der achte Fehler ist **Add-on-Wildwuchs**. Jeder Ingress-Controller, jede Policy Engine, jeder Operator, jedes Storage-Plugin und jedes Monitoring-Tool erweitert die Plattform. Ohne Standardisierung entstehen Sicherheitslücken, Updateprobleme und Verantwortungsdiffusion.

Der neunte Fehler ist **Abnahme über Screenshots**. Behörden brauchen belastbare Nachweise: Konfigurationsauszüge, Scanberichte, Tests, Protokolle, Architekturentscheidungen, Risikoanalysen und Betriebsdokumentation. Ein Screenshot aus dem Dashboard ersetzt keine Abnahme.

Der zehnte Fehler ist **fehlender Exit- und Migrationsgedanke**. Plattformen leben lange. Du musst früh fragen: Wie portabel sind Workloads? Sind Helm Charts proprietär? Gibt es Cloud-spezifische Abhängigkeiten? Sind Daten exportierbar? Gibt es eine Strategie für Plattformwechsel, Cluster-Neuaufbau oder Providerwechsel?

## 9. Mindestanforderungen an eine produktive Behördenplattform

Eine produktive Plattform sollte mindestens ein dokumentiertes Plattformzielbild, ein Rollen- und Verantwortungsmodell, ein Mandanten- und Schutzbedarfskonzept, eine kontrollierte Image-Lieferkette, private Registry, RBAC-Baseline, Namespace-Standards, ResourceQuotas, Network Policies, Secret-Management, Ingress-Standard, TLS-/Zertifikatskonzept, Logging, Monitoring, Tracing, Backup-/Restore-Konzept, Patchprozess, Schwachstellenmanagement, Deployment-Gates, Abnahmevorgaben und Audit-Nachweise besitzen.

Für Abnahmeformulierungen kannst du als Enterprise Architekt so schreiben: „Der Auftragnehmer weist vor Produktivsetzung nach, dass alle produktiven Workloads in dedizierten Namespaces mit dokumentierten Resource Requests, Resource Limits, Network Policies, Service Accounts, RBAC-Berechtigungen, Secret-Anbindung, Health Checks, Logging-Konfiguration, Monitoring-Metriken und Rollback-Verfahren betrieben werden. Der Nachweis erfolgt durch Konfigurationsauszüge, automatisierte Policy-Prüfungen, Scanberichte und einen erfolgreich durchgeführten Restore-Test.“

Diese Formulierung ist stark, weil sie nicht sagt „Kubernetes sicher betreiben“, sondern konkrete Liefergegenstände und Nachweise verlangt.

## 10. Beispiel: Behördenplattform für ein digitales Antragsverfahren

Stell dir ein Portal vor, über das Bürger einen Antrag stellen. Das Portal ruft ein API-Gateway auf, dahinter liegt ein Fachverfahren. Dieses Fachverfahren spricht mit einem Register, einem DMS und einer Datenbank. Die Plattform betreibt mehrere Umgebungen: Entwicklung, Test, Abnahme und Produktion.

Architektonisch würdest du prüfen: Liegt das Portal in einer internetnahen Zone? Ist das API-Gateway der definierte Eintrittspunkt? Sind direkte Zugriffe auf das Fachverfahren ausgeschlossen? Sind Register und DMS nur über erlaubte Egress-Regeln erreichbar? Gibt es getrennte Secrets für jede Umgebung? Werden Anträge und Dokumente persistent gespeichert und gesichert? Sind Datenbankmigrationen kontrolliert? Kann ein Antrag über Traces korreliert werden? Gibt es fachliche Metriken wie Antragseinreichung, Abbruchquote, Registerfehler, DMS-Fehler und Antwortzeiten? Sind Logs frei von sensiblen Inhalten? Gibt es einen getesteten Wiederanlauf?

Die Architekturentscheidung könnte lauten: Produktive Fachverfahren mit personenbezogenen Daten laufen nicht gemeinsam mit experimentellen Workloads auf denselben Nodes. Ingress erfolgt nur über den zentralen, gehärteten Ingress/API-Gateway-Pfad. Egress ist standardmäßig untersagt und wird pro Schnittstelle freigegeben. Jede Anwendung liefert Helm Chart, Security Scan, Resource-Konzept, Observability-Konzept und Runbook vor Abnahme.

## 11. Deine Rolle als Enterprise Architekt

Du musst Kubernetes nicht wie ein Plattformengineer bedienen. Du musst aber die richtigen Architekturwirkungen erkennen. Dein Job ist nicht, `kubectl`-Kommandos auswendig zu können. Dein Job ist, zu erkennen, ob die Plattform tragfähig, sicher, betreibbar, nachweisbar, mandantenfähig und steuerbar ist.

Du bewertest also nicht die Schönheit der YAML-Dateien, sondern die Qualität des Systems: Sind Verantwortlichkeiten klar? Sind Schutzbedarfe umgesetzt? Sind Lieferwege kontrolliert? Sind Rechte minimal? Sind Netze segmentiert? Sind Daten wiederherstellbar? Sind Incidents analysierbar? Sind Dienstleister steuerbar? Sind Abnahmen objektiv möglich?

## 12. Übung: Plattform-Review in 60 bis 90 Minuten

Du bekommst folgendes Szenario: Eine Behörde möchte drei Fachverfahren auf einer gemeinsamen Kubernetes-Plattform betreiben. Verfahren A ist ein öffentlich erreichbares Antragsportal. Verfahren B verarbeitet interne Registerdaten. Verfahren C ist ein Berichtssystem mit niedrigerem Schutzbedarf. Ein externer Dienstleister liefert Helm Charts. Die Plattform wird von einem zentralen Betriebsteam betrieben. CI/CD liegt bei einem anderen Dienstleister. Bisher gibt es Namespaces je Verfahren, aber keine dokumentierten Network Policies. Images werden teilweise aus öffentlichen Registries gezogen. Secrets liegen in Kubernetes Secrets, Rotation ist nicht beschrieben. Monitoring zeigt Pod-Status und CPU, aber keine fachlichen Metriken. Backup wurde eingerichtet, aber Restore wurde noch nie getestet.

Deine Aufgabe: Bewerte die Plattform in vier Schritten. Erstens ordnest du die Risiken: Lieferkette, Mandantentrennung, Secrets, Netzwerk, Observability, Backup, Betriebsverantwortung. Zweitens formulierst du zehn Mindestanforderungen vor Produktivsetzung. Drittens erstellst du eine Zielbildskizze mit Plattformdiensten, Verantwortlichkeiten und Kontrollpunkten. Viertens formulierst du fünf Abnahmekriterien, die ein Dienstleister objektiv erfüllen muss.

Eine gute Musterlösung würde sagen: Die Plattform ist noch nicht produktionsreif für Verfahren A und B. Hauptgründe sind unkontrollierte Image-Herkunft, fehlende Network Policies, ungeklärte Secret-Rotation, unzureichende Observability und fehlender Restore-Test. Vor Produktivsetzung müssen private Registry, Image-Scanning, signierte Images, Default-Deny-Network-Policies, dokumentierte Egress-Freigaben, Secret-Management mit Rotation, RBAC-Prüfung, ResourceQuotas, fachliche Dashboards, Runbooks und ein erfolgreicher Restore-Test nachgewiesen werden.

## 13. Dein persönlicher Lernanker

Merke dir diesen Satz: **Kubernetes ist aus Enterprise-Architecture-Sicht kein Zielbild, sondern ein Ausführungsraum für Zielbilder.** Die eigentliche Qualität entsteht durch Architekturentscheidungen: Welche Workloads dürfen hinein? Wie werden sie getrennt? Wie kommen sie hinein? Wer darf was? Wie werden sie beobachtet? Wie werden sie wiederhergestellt? Wie wird nachgewiesen, dass die Regeln eingehalten wurden?

Wenn du diese Fragen sauber stellst, wirkst du im Behördenkontext sofort professionell. Nicht, weil du jeden Controller intern erklären kannst, sondern weil du Kubernetes in die Sprache von Verantwortung, Schutzbedarf, Betrieb, Nachweis und Abnahme übersetzt. Genau das ist Enterprise Architecture. <>