# Lernroadmap – offene und weiter zu vertiefende EA-Themen

Diese Seite trennt **bereits vorhandene Projektinhalte** von Themen, die im Projekt als nächste Lernblöcke identifiziert wurden. Ein Themenname bedeutet nicht automatisch, dass bereits ein vollständiger Kurs dafür vorliegt.

## Priorität 1 – 100 technische Leitsätze vollständig vertiefen

Die 100 technischen Leitsätze liegen vollständig als Übersicht vor. Kritisch vertieft sind derzeit Leitsätze 1–3. Die Leitsätze 4–100 sollen jeweils mit Gegenposition, Grenzen, technischen Beispielen, Behördenkontext, Reviewfragen und Arbeitsformel bearbeitet werden.

## Priorität 2 – technische EA-Basis

### Distributed Systems
At-most-once, at-least-once, exactly-once, Idempotenz, Deduplizierung, Retry, Backoff, Jitter, Timeout, Circuit Breaker, Bulkhead, Rate Limiting, Backpressure, DLQ, Parking Lot Queue, Poison Messages, Replay, Eventual Consistency, Saga, Outbox/Inbox und Distributed Tracing.

### Konsistenz und Datenverteilung
CAP, Netzwerkpartitionen, Strong/Eventual Consistency, Read-your-writes, Quorum, Leader/Follower, Multi-Leader und Konfliktauflösung.

### API Architecture
REST, URI-/Resource-Design, HTTP-Semantik, Versionierung, Fehlerobjekte, AuthN/AuthZ, Rate Limits, OpenAPI, gRPC, GraphQL, Webhooks, API Gateway, BFF und Contract Testing.

### Event-Driven Architecture
Commands vs. Events, Domain/Integration Events, Event Schema Evolution, Broker vs. Event Log, Kafka-Grundlagen, Topics, Partitionen, Consumer Groups, Offset, Replay, Retention und Schema Registry.

### Domain-Driven Design
Domain, Subdomain, Core/Supporting/Generic Domain, Bounded Context, Ubiquitous Language, Context Maps, Anti-Corruption Layer, Shared Kernel und Published Language.

### Microservices kritisch bewerten
Microservices vs. modularer Monolith, Service Boundaries, Database per Service, Distributed Transactions, Deployment Independence, Service Mesh und Distributed Monolith.

### Plattformarchitektur
Platform Engineering, Internal Developer Platform, Golden Paths, Self-Service, Landing Zones, Kubernetes, Registry, Secrets, Policy-as-Code, IaC und GitOps.

## Priorität 3 – Production Architecture

### Cloud Architecture
Public/Private/Hybrid/Sovereign Cloud, Shared Responsibility, Landing Zones, IAM, Segmentierung, Verschlüsselung, Backup/DR, FinOps, Exit und Vendor Lock-in.

### IAM
IdP/SP, Federation, SSO, MFA, OAuth, OIDC, SAML, RBAC, ABAC, ReBAC, PAM, JIT, Service Accounts, Machine Identities, Zertifikate und Identity Lifecycle.

### Security Architecture
Zero Trust, Defense in Depth, Trust Boundaries, Threat Modeling, STRIDE, Attack Surface, Secure by Design, Supply Chain Security, SBOM, SAST/DAST/SCA, Secrets und SIEM.

### Observability/SRE
Metrics, Logs, Traces, Events, Correlation IDs, OpenTelemetry, SLI/SLO/SLA, Error Budgets, Alerting, Dashboards und fachliche Observability.

### Resilienz/BCM
HA, Resilience, Disaster Recovery, Business Continuity, Backup, Restore, RTO, RPO, MTPD/MBCO, Notbetrieb, Wiederanlauf und Nachpflege.

## Priorität 4 – Behörden-EA

- DMS/eAkte und Dokumentenlebenszyklus
- Datenschutz-by-Architecture
- Architektur in Ausschreibung und EVB-IT
- technische Dienstleistersteuerung
- Architekturabnahme und Nachweisführung
- Behörden-/Registerintegration
- Gremienkommunikation und Executive Decision Papers

## Priorität 5 – Senior-/Principal-EA

- EA vs. Solution/Software/Platform Architecture
- Entscheidungsarchitektur und Decision Debt
- Architekturmetriken und KPIs
- EA-Reifegradmodell
- Architektur-Anti-Patterns
- Architecture Review Mastercheckliste mit 100+ Fragen
- EA in Krisen, Incidents und Eskalationen
- AI Architecture für Behörden

## Lernregel

Neue Themen werden erst dann als „vollständig vorhanden“ markiert, wenn sie einen eigenen Lerninhalt mit Grundlagen, Praxisbeispielen, Grenzen, Reviewfragen und Artefakten besitzen. Eine bloße Nennung in dieser Roadmap zählt nicht als vollständiger Lernstoff.
