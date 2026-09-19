# 100 technische Master-Leitsätze für Enterprise Architects

## Architekturgrundsätze
1. Jede technische Entscheidung braucht einen fachlichen Grund.
2. Eine Architekturentscheidung ist erst vollständig, wenn ihre Konsequenzen benannt sind.
3. Technische Eleganz ersetzt keine Betriebsfähigkeit.
4. Architektur beginnt dort, wo lokale Optimierung systemische Folgen hat.
5. Ein System darf intern komplex sein, aber seine Verantwortung muss extern klar sein.
6. Ich entscheide nicht nach Technologiepräferenz, sondern nach Eignung, Risiko und Lebenszyklus.
7. Eine Architektur ohne Annahmenliste ist eine getarnte Vermutung.
8. Architekturqualität muss prüfbar sein.
9. Ein Zielbild ohne Übergangsarchitektur ist technisch gefährlich.
10. Jede technische Zielarchitektur braucht einen Rückbauplan für das Alte.

## Domänenschnitt und Applikationsarchitektur
11. Systemgrenzen müssen an fachlichen Verantwortungen ausgerichtet sein.
12. Ein System sollte eine klare Primärrolle haben: führen, verarbeiten, anzeigen, integrieren oder berichten.
13. Nicht jedes System darf führendes System sein.
14. Ein Anwendungsschnitt ist gut, wenn er Verantwortung reduziert statt verteilt.
15. Technische Wiederverwendung ist nur wertvoll, wenn Verantwortung und Änderbarkeit geklärt sind.
16. Ein Shared Service braucht Produktverantwortung, SLOs und klare Consumer-Verträge.
17. Eine Anwendung ohne Owner ist ein Betriebsrisiko.
18. Eine Zielrolle pro Anwendung verhindert Architektur-Nebel.
19. Doppelungen sind nicht immer falsch, aber immer begründungspflichtig.
20. Architektur entscheidet nicht nur, was gebaut wird, sondern auch, was nicht weitergebaut wird.

## Datenarchitektur
21. Datenführerschaft ist eine Architekturentscheidung, keine Datenbankeigenschaft.
22. Ein Datenobjekt braucht Zweck, Owner, Quelle, Qualität und Lebenszyklus.
23. Attributführerschaft kann wichtiger sein als Objektführerschaft.
24. Kopierte Daten brauchen eine Aktualisierungs- und Konfliktregel.
25. Datenqualität muss dort gemessen werden, wo sie fachliche Wirkung hat.
26. Ein Statusmodell ist Architekturkern, nicht UI-Detail.
27. Fristen sind steuernde Daten und müssen führend geklärt werden.
28. Datenmigration ist kein technischer Import, sondern fachliche Übersetzung.
29. Ein Reportingmodell ohne Datenlinie ist nicht belastbar.
30. Metadaten sind Steuerungsdaten.

## Schnittstellen und Integration
31. Eine Schnittstelle ohne fachlichen Vertrag ist nur eine technische Leitung.
32. Jede kritische Schnittstelle braucht ein explizites Fehlerverhalten.
33. Quittierung ist fachliche Semantik, nicht nur HTTP-Status.
34. Schnittstellen müssen versioniert werden, bevor sie geändert werden.
35. Eine synchrone Schnittstelle ist eine Laufzeitabhängigkeit.
36. Asynchronität entkoppelt Zeit, aber nicht Verantwortung.
37. Events brauchen fachliche Bedeutung, Idempotenz und Wiederholbarkeit.
38. Batch-Schnittstellen brauchen Kontrollsummen, Wiederanlauf und fachliche Fehlerliste.
39. Ein Gateway ersetzt keine Integrationsarchitektur.
40. Eine Schnittstelle ist erst abnahmefähig, wenn Fachfall, Fehlerfall und Betriebsfall getestet sind.

## Security und IAM
41. Schutzbedarf muss technische Architekturentscheidungen auslösen.
42. Vertrauensgrenzen gehören ins Architekturmodell.
43. Least Privilege ist nur wirksam, wenn Rollen fachlich sauber geschnitten sind.
44. Technische Konten brauchen Owner, Zweck, Ablauf und Rotation.
45. Adminrechte sind kein Betriebsnormalfall.
46. Authentifizierung klärt Identität, Autorisierung klärt Handlung.
47. Protokollierung muss fachlich relevante Änderungen nachvollziehbar machen.
48. Logs sind selbst schutzbedürftige Daten.
49. Security-Ausnahmen brauchen Ablaufdatum und Kompensation.
50. Security muss im Lieferweg geprüft werden, nicht nur im Zielsystem.

## Datenschutz und Datenlebenszyklus
51. Datenflussdiagramme sind Datenschutz-Artefakte.
52. Zweckbindung muss in Datenmodell, Schnittstelle und Zugriff sichtbar werden.
53. Aufbewahrung und Löschung müssen systemübergreifend gedacht werden.
54. Testumgebungen sind kein rechtsfreier Technikraum.
55. Pseudonymisierung ist eine Architekturentscheidung, kein Häkchen.
56. Datenminimierung heißt nicht Datenblindheit.
57. Löschbarkeit muss vor der Speicherung bedacht werden.
58. Ein Datenschutzrisiko ist oft ein Architekturhinweis.
59. Datenschutz und Nachvollziehbarkeit müssen zusammen entworfen werden.
60. Jeder neue Datenabzug braucht Zweck, Owner, Empfänger und Ablaufdatum.

## Plattform, Cloud und Infrastruktur
61. Plattform ist ein Produkt, nicht nur Infrastruktur.
62. Kubernetes löst kein Architekturproblem, das fachlich ungelöst ist.
63. Mandantentrennung muss fachlich, technisch und betrieblich erklärt werden.
64. IaC ist nur wertvoll, wenn es versioniert, geprüft und reproduzierbar ist.
65. Umgebungsgleichheit reduziert Überraschungen.
66. Konfiguration gehört nicht heimlich ins System, sondern kontrolliert in den Lieferweg.
67. Secrets sind keine Konfiguration.
68. Skalierung muss an Lastprofilen und Fachereignissen ausgerichtet sein.
69. Resilienz entsteht durch Architektur, nicht durch Hoffnung auf stabile Infrastruktur.
70. Plattformstandards müssen Ausnahmen aushalten, aber nicht beliebig werden.

## CI/CD, Qualität und Test
71. Der Lieferweg ist Teil der Architektur.
72. Ein nicht reproduzierbarer Build ist ein Betriebsrisiko.
73. Qualitätssicherung beginnt nicht im Test, sondern bei Architekturentscheidungen.
74. Automatisierte Tests müssen Architekturverträge schützen.
75. Contract Tests sind Pflicht, wenn mehrere Systeme voneinander abhängen.
76. Security-Scans ohne Befundprozess sind nur Geräusch.
77. Ein Release ohne Rückfallplan ist unvollständig.
78. Deployment-Frequenz ist wertlos ohne Stabilität und Nachweisfähigkeit.
79. Definition of Done muss Architekturartefakte einschließen.
80. Technische Schulden brauchen Bewertung, Owner und Rückzahlungsplan.

## Betrieb, Observability und Resilienz
81. Betrieb ist kein Nachgang der Architektur, sondern ihr Realitätscheck.
82. RTO und RPO müssen aus Fachwirkung abgeleitet werden.
83. Monitoring ohne Handlungsanweisung ist Beobachtung, kein Betrieb.
84. Ein Dashboard muss eine Entscheidung ermöglichen.
85. Runbooks müssen getestet werden.
86. Wiederanlauf muss fachliche Nachpflege einschließen.
87. Retries ohne Idempotenz sind gefährlich.
88. Timeouts sind Architekturentscheidungen.
89. Incident-Daten sind Lernmaterial für Architektur.
90. Betriebsfähigkeit muss vor Go-live nachgewiesen werden.

## Modellierung, Dokumentation und Nachweis
91. Ein Modell ist gut, wenn es eine Frage beantwortet.
92. Architektur dokumentiert Entscheidungen, nicht nur Strukturen.
93. Jede Sicht braucht Zielgruppe und Entscheidungskontext.
94. Confluence ist kein Archiv, sondern ein Arbeitsraum mit Pflegeverantwortung.
95. Jira steuert Maßnahmen, nicht Architekturverständnis.
96. ArchiMate ist hilfreich, wenn es Beziehungen sichtbar macht, nicht wenn es alles zeigt.
97. Ein Repository ist nur so gut wie seine Datenpflege.
98. Lokale Dateien sind der Feind organisatorischer Architekturfähigkeit.
99. Nachweisfähigkeit ist technische Führungsarbeit.
100. Meine technische Architekturarbeit ist erfolgreich, wenn andere Systeme, Teams und Entscheidungen dadurch stabiler werden.
