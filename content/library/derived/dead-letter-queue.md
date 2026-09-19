# Dead Letter Queue (DLQ) – Fehlerbehandlung in asynchronen Architekturen

## Definition

Eine **Dead Letter Queue** ist eine kontrollierte Ablage für Nachrichten, die nach definierten Verarbeitungsversuchen nicht erfolgreich verarbeitet werden konnten. Sie verhindert, dass fehlerhafte Nachrichten endlos wiederholt werden oder unbemerkt verloren gehen.

## Grundablauf

```text
Producer → Haupt-Queue/Topic → Consumer
                         ├─ erfolgreich → Verarbeitung abgeschlossen
                         └─ wiederholt fehlerhaft → Dead Letter Queue
```

## Warum eine DLQ sinnvoll sein kann

- fehlerhafte Nachrichten bleiben nachvollziehbar erhalten
- die Hauptverarbeitung wird nicht dauerhaft blockiert
- Betrieb und Entwicklung können Ursachen untersuchen
- eine kontrollierte Korrektur oder erneute Verarbeitung wird möglich
- fachliche Rückstände können sichtbar gemacht werden

## Technischer vs. fachlicher Fehler

**Technische Fehler:** Datenbank nicht erreichbar, Netzwerkstörung, Timeout, temporär nicht verfügbarer Dienst. Hier kann Retry sinnvoll sein.

**Fachliche/strukturelle Fehler:** Pflichtfeld fehlt, unbekannter Status, Vertragsverletzung, fachlich unzulässiger Zustandswechsel. Hier hilft ein blindes Retry meist nicht.

## Retry-Strategie

Retries müssen begrenzt und kontrolliert sein. Häufig wird die Wartezeit verlängert (**exponentielles Backoff**) und mit **Jitter** leicht variiert, damit viele Clients nicht gleichzeitig erneut anfragen.

```text
Versuch 1 → warten → Versuch 2 → länger warten → Versuch 3 → DLQ/Klärfall
```

## Metadaten einer guten DLQ

- ursprüngliche Nachricht
- ursprüngliche Queue/Topic
- Zeitpunkt
- Anzahl Versuche
- Fehlercode/-text
- Consumer/Service
- Message-/Correlation-/Trace-ID
- Schema-/Versionsinformation
- fachliche Vorgangs-ID, falls zulässig

## Idempotenz

Replay darf keine ungewollten Doppelwirkungen erzeugen. Wenn die erste Verarbeitung fachlich erfolgreich war, aber die technische Bestätigung verloren ging, kann eine Wiederholung sonst z. B. ein Dokument, eine Zahlung oder einen Vorgang doppelt erzeugen.

Ein idempotenter Consumer erkennt Wiederholungen oder gestaltet die Operation so, dass dieselbe Nachricht mehrfach verarbeitet werden kann, ohne die fachliche Wirkung zu vervielfachen.

## Eine DLQ ist nicht immer Pflicht

Eine DLQ ist **ein mögliches Mittel**, nicht die Definition guter Event-Architektur. Alternativen oder Ergänzungen sind Retry Queues, Parking-Lot Queues, Fehlerdatenbanken, manuelle Klärfälle, Replay, Kompensation oder kontrolliertes Verwerfen unkritischer Nachrichten.

Entscheidend ist eine explizite Strategie für Zustellung, Wiederholung, Duplikate, Fehlerbehandlung und Nachbearbeitung.

## Behördenbeispiel

Ein Fachverfahren sendet die Anweisung, ein Dokument einem Vorgang im DMS zuzuordnen. Der Vorgang existiert dort nicht oder die fachliche Referenz ist ungültig. Nach begrenzten Versuchen landet die Nachricht im Klärfall/DLQ.

Nun sind nicht nur technische Fragen relevant:

- Ist die Vorgangs-ID falsch?
- Wurde die Nachricht zu früh erzeugt?
- Ist der Zielvorgang fachlich bereits geschlossen?
- Entsteht eine Frist- oder Nachweislücke?
- Darf die Nachricht erneut verarbeitet werden?
- Muss eine Fachrolle informiert werden?

Damit wird sichtbar: Eine DLQ kann eine **fachliche Arbeitswarteschlange** sein.

## EA-Reviewfragen

1. Welche Nachrichten dürfen in die DLQ gelangen?
2. Nach wie vielen Versuchen?
3. Wie werden technische und fachliche Fehler unterschieden?
4. Wer besitzt die DLQ fachlich und betrieblich?
5. Welche Service-/Bearbeitungszeit gilt?
6. Wie wird alarmiert?
7. Wie wird Replay durchgeführt?
8. Wie wird Idempotenz/Deduplizierung sichergestellt?
9. Welche personenbezogenen/schutzbedürftigen Daten liegen dort?
10. Wie lange werden Nachrichten aufbewahrt?
11. Wie wird die Bearbeitung nachvollziehbar dokumentiert?
12. Wie wird verhindert, dass die DLQ zum „Fehlerfriedhof“ wird?

## Arbeitsformel

**Eine DLQ ist kein Müllkorb, sondern eine kontrollierte technische und häufig fachliche Arbeitswarteschlange.**
