import json, re, os, textwrap, unicodedata
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
CONTENT=ROOT/'content'
BOOKS_MD=Path('/mnt/data/EA_Fachbibliothek_2026.md')

# ---------- Helpers ----------
def slug(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    s=re.sub(r'[^a-z0-9]+','-',s).strip('-')
    return s

def sentence_list(items):
    return ' '.join(items)

def parse_books():
    txt=BOOKS_MD.read_text(encoding='utf-8')
    sections={}
    current=None
    book=None
    for line in txt.splitlines():
        m=re.match(r'^# (\d+)\. (.+)$',line)
        if m:
            current=int(m.group(1)); sections[current]=[]; book=None; continue
        m=re.match(r'^### \d+\. (.+)$',line)
        if m and current:
            book={'title':m.group(1).strip(),'author':'','language':'','edition':'','summary':''}; sections[current].append(book); continue
        if book:
            if line.startswith('- **Autor/Hrsg.:** '): book['author']=line.split('** ',1)[1]
            elif line.startswith('- **Sprache:** '): book['language']=line.split('** ',1)[1]
            elif line.startswith('- **Ausgabe/Jahr:** '): book['edition']=line.split('** ',1)[1]
            elif line.startswith('- **Kurzfassung:** '): book['summary']=line.split('** ',1)[1]
    return sections

BOOKS=parse_books()

# Current official anchors, verified 2026-09-19.
ANCHORS={
    'nita': {'name':'Nationale IT-Architekturrichtlinie / IT-Architektur Bund','url':'https://bmds.bund.de/themen/digitaler-staat/it-architektur','asOf':'2026-09-19','note':'Gemeinsamer Kern der Architekturrichtlinien von Bund und Ländern; bundesspezifische und föderale Ableitungen ergänzen ihn.'},
    'bsi': {'name':'BSI IT-Grundschutz','url':'https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html','asOf':'2026-09-19','note':'Für Sicherheitsmanagement, Schutzbedarf, Risikobehandlung und BCM immer die aktuell gültigen BSI-Standards/Kompendien prüfen.'},
    'evbit': {'name':'EVB-IT / öffentliche IT-Beschaffung','url':'https://bmds.bund.de/aktuelles/pressemitteilungen/detail/open-source-rechtssicher-beschaffen','asOf':'2026-09-19','note':'Modernisierte EVB-IT sind 2026 in Kraft; aktuelle Vertragsmuster und das EVB-IT-Vertragserstellungstool verwenden.'},
    'fit': {'name':'FIT-Connect / FITKO','url':'https://docs.fitko.de/fit-connect/docs/intro/','asOf':'2026-09-19','note':'Föderale Basisinfrastruktur für Antragsübermittlung; Versionen und Abkündigungen prüfen. API-Versionen 1.x sind zum 01.10.2026 abgekündigt.'},
    'ai': {'name':'EU AI Act – High-Risk Guidelines / Service Desk','url':'https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-high-risk-systems','asOf':'2026-09-19','note':'Zeitplan und Leitlinien sind dynamisch. Für Hochrisiko-Bereiche wie Migration/Asyl gelten nach aktuellem Kommissionsstand verschobene Anwendungszeitpunkte; immer aktuelle EU-Quelle prüfen.'},
    'gdpr': {'name':'DSGVO / EUR-Lex','url':'https://eur-lex.europa.eu/eli/reg/2016/679/oj','asOf':'2026-09-19','note':'Privacy-by-Design, Rechtsgrundlage, Zweckbindung, Datenminimierung, Betroffenenrechte und Sicherheit als Architekturconstraints behandeln.'},
}

# Project source module mapping and snippet extraction.
INDEX=json.load(open(CONTENT/'index.json',encoding='utf-8'))
MODULES={m['id']:m for m in INDEX['modules']}

def source_excerpt(mid, keywords):
    m=MODULES.get(mid)
    if not m: return {'moduleId':mid,'title':mid,'category':'Projektquelle','excerpt':''}
    p=ROOT/m['path']
    text=p.read_text(encoding='utf-8',errors='ignore') if p.exists() else ''
    chunks=[c.strip() for c in re.split(r'\n\s*\n',text) if c.strip()]
    chosen=''
    for kw in keywords:
        for c in chunks:
            if kw.lower() in c.lower() and len(c)>80:
                chosen=c; break
        if chosen: break
    if not chosen:
        chosen=next((c for c in chunks if len(c)>120 and not c.startswith('#')),chunks[0] if chunks else '')
    chosen=re.sub(r'\[([^\]]+)\]\([^\)]+\)',r'\1',chosen)
    chosen=re.sub(r'[#*_`>|]',' ',chosen)
    chosen=re.sub(r'\s+',' ',chosen).strip()
    if len(chosen)>650: chosen=chosen[:647]+'…'
    return {'moduleId':mid,'title':m.get('title') or m.get('sourceTitle') or mid,'category':m.get('category','Projektquelle'),'excerpt':chosen}

# Each course is a complete progression from simple foundations to professional EA delivery.
C=[
{
'n':1,'title':'EA Profession & TOGAF','competency':'EA Profession','description':'Rolle, Mandat, Abstraktion, TOGAF/ADM und Entscheidungsfähigkeit als Fundament professioneller Enterprise Architecture.',
'analogy':'Ein Enterprise Architect ist weniger der Bauzeichner eines einzelnen Hauses als der Stadtplaner: Er entscheidet nicht selbst über jede Wohnung, sorgt aber dafür, dass Straßen, Versorgung, Regeln und Entwicklung zusammenpassen.',
'model':'Auftrag → Treiber → Fähigkeiten → Daten/Anwendungen/Technologie → Optionen → Entscheidung → Roadmap → Governance → Lernen',
'concepts':[('Enterprise Architecture','Verbindet fachliche Ziele, Organisation, Daten, Anwendungen, Technologie und Veränderung.','Eine Behörde will nicht „Cloud“, sondern schnellere, sichere und nachvollziehbare Leistungen.'),('Mandat','Legt Scope, Auftraggeber, Entscheidungsrechte und Grenzen der EA-Arbeit fest.','Der externe EA empfiehlt; ein internes Gremium entscheidet.'),('ADM','TOGAF-Logik für Architekturentwicklung und Veränderung.','Vor einer Plattformentscheidung werden Vision, Business, Daten, Anwendungen und Technologie geklärt.'),('Architecture Principle','Verbindliche Leitplanke mit Begründung und Konsequenzen.','Neue Fachverfahren nutzen zentrales IAM statt eigener Passwörter.'),('Decision Rights','Regeln, wer welche Architekturentscheidung treffen darf.','Security gibt Sicherheitsanforderungen vor; Architekturboard entscheidet Ausnahmen.')],
'connections':[('Business Architecture','EA beginnt bei Wirkung und Fähigkeiten, nicht beim Produktnamen.'),('Governance','Architektur wird erst wirksam, wenn Entscheidungen und Ausnahmen verbindlich geregelt sind.'),('Consulting','Externe EAs wirken über Klarheit, Optionen und Evidenz statt Linienmacht.'),('Portfolio','EA verbindet einzelne Vorhaben mit dem Gesamtbild und verhindert lokale Optimierung.'),('Betrieb','Zielarchitektur ist unvollständig, wenn Betriebsfähigkeit nicht mitgedacht wird.')],
'distinctions':[('EA vs. Solution Architecture','EA entscheidet über domänen- und organisationsweite Leitplanken; Solution Architecture konkretisiert eine Lösung im gegebenen Rahmen.'),('Framework vs. Realität','TOGAF strukturiert Denken und Arbeit, ersetzt aber keine Kenntnis des Mandats, der Behörde oder der Entscheidungswege.'),('Empfehlung vs. Entscheidung','Der externe EA bereitet Optionen, Risiken und Konsequenzen vor; formale Verantwortung bleibt bei der Behörde.')],
'method':['Mandat und Auftraggeber klären','Entscheidungsfrage präzisieren','Stakeholder und Constraints erfassen','Ist- und Zielbild auf geeigneter Abstraktion formulieren','Optionen und Trade-offs entwickeln','Entscheidung vorbereiten und dokumentieren','Umsetzung und Änderungen über Governance begleiten'],
'questions':['Welche Entscheidung soll am Ende möglich sein?','Wer trägt fachliche Verantwortung?','Welche Architekturdomänen sind betroffen?','Welche Vorgaben und Standards gelten?','Welche Annahmen sind noch unbewiesen?','Was ist Enterprise-relevant und was lokal?','Wie wird eine Ausnahme entschieden?','Welche Evidence braucht das Gremium?'],
'artifacts':['Mandatssteckbrief','Architecture Vision','Architecture Requirements & Decisions Log','Prinzipienkatalog','Roadmap und Reviewkalender'],
'mistakes':[('TOGAF als Dokumentenmaschine','Nur Artefakte erstellen, die Entscheidungen, Risiken oder Umsetzung steuern.'),('Mit Technologie beginnen','Zuerst fachliche Wirkung und Qualitätsanforderungen klären.'),('Alles zentral entscheiden','Lokale Autonomie zulassen, solange Enterprise-Constraints eingehalten werden.'),('Unklare Decision Rights','Vor dem ersten Review klären, wer empfiehlt, entscheidet, genehmigt und eskaliert.')],
'case':'Ein Referat fordert „eine Kubernetes-Zielarchitektur“ für ein neues Fachverfahren, kann aber weder Ziel-Nutzerzahlen, Schutzbedarf noch Betriebsmodell benennen.',
'caseSolution':'Nicht Kubernetes bewerten, bevor die Entscheidungsfrage geklärt ist. Mandat, fachliche Ziele, Qualitätsattribute, Daten, Betriebsverantwortung und Plattformvorgaben erheben; dann mindestens zwei tragfähige Optionen mit Trade-offs und Entscheidungsvorlage liefern.',
'deliverable':'Mandatssteckbrief + Architecture Vision + erste Decision Map','exec':'„Wir entscheiden heute nicht über ein Werkzeug, sondern darüber, welche Architekturbedingungen die Behörde für eine sichere und betreibbare Lösung braucht.“',
'sources':['togaf-adm-im-behordenkontext','eam-leistungsbild-fur-behorden','enterprise-architecture-hard-skills','adr-erstellung-und-praxis'],'anchors':['nita']},
{
'n':2,'title':'Strategie & Operating Model','competency':'Strategie & Operating Model','description':'Strategische Ziele in Fähigkeiten, Wertströme, Verantwortungen, Sourcing und eine tragfähige Zielorganisation übersetzen.',
'analogy':'Strategie ist das Reiseziel; das Operating Model ist die Art, wie die Organisation reist: Wer fährt, welche Wege sind gemeinsam, welche Informationen werden geteilt und welche Dienste werden zentral bereitgestellt.',
'model':'Mission/Ziele → strategische Treiber → Operating Model → Capabilities/Value Streams → Plattformen & Shared Services → Roadmap → Nutzenmessung',
'concepts':[('Strategischer Treiber','Ein Grund, warum die Organisation ihre Fähigkeiten oder Architektur verändern muss.','Neue gesetzliche Fristen erzwingen schnellere Ende-zu-Ende-Bearbeitung.'),('Operating Model','Beschreibt, wie Prozesse, Organisation, Informationen, Lieferanten und Standorte zusammenarbeiten.','Mehrere Standorte nutzen ein gemeinsames Fachverfahren, aber regionale Zuständigkeiten bleiben getrennt.'),('Value Stream','End-to-End-Kette, die für einen Stakeholder ein Ergebnis erzeugt.','Von Antragseingang bis rechtswirksamem Bescheid.'),('Shared Service','Zentral bereitgestellte Fähigkeit für mehrere Domänen.','IAM, Dokumentenerzeugung oder Monitoring als gemeinsame Dienste.'),('Sourcing','Entscheidung, welche Fähigkeiten intern, extern oder gemeinsam erbracht werden.','Plattformbetrieb beim IT-Dienstleister, fachliche Produktverantwortung in der Behörde.')],
'connections':[('Capability Mapping','Strategie wird über Fähigkeiten in eine stabile Architekturübersetzung gebracht.'),('Portfolio','Investitionen werden danach priorisiert, welche Fähigkeiten und Outcomes sie verbessern.'),('Organisation','Ein Zielbild ohne Verantwortungs- und Betriebsmodell bleibt technisch.'),('Cloud/Plattform','Zentrale Plattformen sind Operating-Model-Entscheidungen, nicht nur Infrastruktur.'),('Vergabe','Sourcing-Entscheidungen müssen in Leistungsbeschreibung, Exit und Governance übersetzt werden.')],
'distinctions':[('Ziel vs. Maßnahme','„Bearbeitungszeit halbieren“ ist Ziel; „neues Portal“ ist nur eine mögliche Maßnahme.'),('Operating Model vs. Organigramm','Das Operating Model beschreibt Zusammenarbeit und Verantwortungslogik, nicht nur Stellenkästchen.'),('Standardisierung vs. Zentralisierung','Einheitliche Regeln können dezentral umgesetzt werden; Zentralisierung ist nur eine Ausprägung.')],
'method':['Strategische Ziele und Rechts-/Politiktreiber erfassen','Outcomes messbar machen','Value Streams und Capabilities zuordnen','Integrations- und Standardisierungsbedarf bestimmen','Sourcing und Shared Services festlegen','Ziel-Operating-Model skizzieren','Architekturinitiativen und Nutzenkennzahlen ableiten'],
'questions':['Welches Ergebnis soll für Bürger, Fachseite oder Leitung besser werden?','Welche Fähigkeiten sind dafür kritisch?','Wo brauchen wir Standardisierung, wo lokale Autonomie?','Welche Daten müssen gemeinsam sein?','Welche Services sollten geteilt werden?','Welche Verantwortung bleibt zwingend intern?','Welche Abhängigkeit entsteht durch Sourcing?','Wie messen wir den Nutzen nach Umsetzung?'],
'artifacts':['Strategy-to-Architecture Map','Target Operating Model Canvas','Capability Heatmap','Value-Stream-to-Capability Map','Strategic Roadmap'],
'mistakes':[('Strategie als Buzzword-Sammlung','Ziele mit messbaren Outcomes und Entscheidungen verbinden.'),('Jedes Problem mit einem System lösen','Erst prüfen, ob Prozess, Verantwortung oder Daten das eigentliche Problem sind.'),('Shared Service ohne Produktverantwortung','Owner, Serviceversprechen, Finanzierung und Lifecycle definieren.'),('Sourcing ohne Exit','Datenportabilität, Dokumentation, Wissenstransfer und Exit-Kriterien festlegen.')],
'case':'Eine Bundesbehörde hat fünf ähnliche Fachverfahren in verschiedenen Organisationseinheiten. Die Leitung fordert „eine Plattform“, die Bereiche wollen ihre Autonomie behalten.',
'caseSolution':'Zuerst Operating-Model-Frage klären: Welche fachlichen Fähigkeiten und Daten brauchen Standardisierung, welche bleiben domänenspezifisch? Shared Services wie IAM, Dokumente, Observability und Integrationsplattform identifizieren; Domänenverantwortung und Migration in Stufen entwerfen.',
'deliverable':'Target Operating Model + Capability/Value-Stream-Zielbild','exec':'„Wir standardisieren nicht Organisationseinheiten, sondern nur dort, wo gemeinsame Fähigkeiten, Daten oder Betriebsrisiken einen messbaren Vorteil erzeugen.“',
'sources':['enterprise-architektur-strategie','capability-mapping-bundesbehorden','roadmap-mit-ubergangsarchitekturen','applikationsportfolio-bewerten'],'anchors':['nita']},
{
'n':3,'title':'Business Architecture','competency':'Business Architecture','description':'Fähigkeiten, Wertströme, Prozesse, Rollen und Entscheidungslogik als fachliches Fundament der Architektur verstehen und modellieren.',
'analogy':'Wenn IT die Werkzeuge sind, beschreibt Business Architecture die Arbeit: Was muss die Behörde können, welches Ergebnis erzeugt sie, wer ist beteiligt und welche Regeln steuern den Ablauf?',
'model':'Leistung/Outcome → Value Stream → Capability → Prozess → Rolle → Entscheidung/Regel → Daten/Systemunterstützung',
'concepts':[('Capability','Stabile Fähigkeit einer Organisation, ein Ergebnis zu erbringen.','„Antrag prüfen“ bleibt bestehen, auch wenn das Fachverfahren ausgetauscht wird.'),('Value Stream','Folge von Wertschritten aus Sicht eines Stakeholders.','Antrag einreichen → prüfen → entscheiden → Bescheid erhalten.'),('Business Process','Konkreter Ablauf mit Ereignissen, Aufgaben, Rollen und Entscheidungen.','Nachweis fehlt → Nachforderung → Wiedervorlage → Fortsetzung.'),('Business Role','Verantwortliche fachliche Rolle, unabhängig von konkreten Personen.','Sachbearbeitung, Fachaufsicht, Datenschutzkoordination.'),('Decision Logic','Fachliche Regel, die aus Eingaben ein Ergebnis bestimmt.','Welche Nachweise sind für Falltyp X erforderlich?')],
'connections':[('BPMN','Macht Abläufe, Wartezeiten, Medienbrüche und Verantwortungswechsel sichtbar.'),('DMN','Trennt regelbasierte Entscheidungen vom Prozessfluss.'),('Data Architecture','Jede fachliche Aktivität erzeugt, liest oder verändert Datenobjekte.'),('Application Architecture','Systemrollen werden aus benötigten fachlichen Fähigkeiten abgeleitet.'),('Observability','Fachliche Prozesskennzahlen zeigen, ob das Ergebnis tatsächlich geliefert wird.')],
'distinctions':[('Capability vs. Prozess','Capability = was die Organisation kann; Prozess = wie sie es in einem Ablauf tut.'),('Prozess vs. Value Stream','Prozess ist interne Ausführung; Value Stream fokussiert Wert aus Stakeholdersicht.'),('Rolle vs. Organisationseinheit','Eine Rolle beschreibt Verantwortung; dieselbe Rolle kann in mehreren Einheiten vorkommen.')],
'method':['Verwaltungsleistung und Ergebnis definieren','Stakeholder und Trigger bestimmen','Capabilities grob erfassen','Value Stream skizzieren','kritische Prozesse und Ausnahmen modellieren','Entscheidungslogik aus BPMN in DMN auslagern','Architekturprobleme und Anforderungen ableiten'],
'questions':['Was ist das fachliche Ergebnis?','Wer erhält den Wert?','Welche Fähigkeit ist wirklich notwendig?','Wo entstehen Wartezeiten?','Wo wechseln Verantwortung oder Medium?','Welche Entscheidungen sind regelbasiert?','Welche Datenobjekte sind zentral?','Welche IT-Unterstützung ist heute problematisch?'],
'artifacts':['Capability Map','Value Stream Map','BPMN-Prozessmodell','DMN-Entscheidungstabelle','Business Architecture Brief'],
'mistakes':[('Capability = Systemname','Capabilities in fachlicher Verb-Objekt-Sprache formulieren.'),('Happy Path only','Ausnahmen, Rückfragen, Fristen und manuelle Klärung mitmodellieren.'),('Gateways als Regelwerk','Komplexe Fachregeln in DMN auslagern.'),('Prozessdiagramm ohne Architekturwirkung','Aus Medienbrüchen und Verantwortungswechseln konkrete Anforderungen ableiten.')],
'case':'Anträge kommen über Portal, E-Mail und Papier. Sachbearbeitung führt zusätzlich Excel-Listen für Fristen. DMS-Ablage erfolgt erst am Ende.',
'caseSolution':'Value Stream und Ist-BPMN modellieren; Medienbrüche, Schattenlisten und späte Aktenbildung markieren; Capability „Vorgang steuern“, Datenobjekte Status/Frist und Systemrollen ableiten; Soll-Prozess mit führendem Status und früher DMS/eAkte-Integration entwerfen.',
'deliverable':'Capability Map + Soll-BPMN + Architekturimplikationen','exec':'„Das Prozessmodell ist kein Dokumentationsartefakt; es zeigt, an welchen Übergängen Architekturentscheidungen notwendig werden.“',
'sources':['capability-mapping-bundesbehorden','bpmn-fur-verwaltungsprozesse','dmn-entscheidungslogik-und-bpmn','archimate-fur-behorden-ea'],'anchors':['fit']},
{
'n':4,'title':'Requirements & Qualitätsarchitektur','competency':'Requirements & Qualität','description':'Bedarfe, Constraints und Qualitätsattribute so formulieren, dass Architekturentscheidungen und Abnahmen objektiv möglich werden.',
'analogy':'Eine Anforderung wie „das System muss schnell sein“ ist wie „das Auto muss gut fahren“. Erst wenn Situation, erwartete Reaktion und Messgröße feststehen, kann Architektur darauf optimieren.',
'model':'Stakeholder Need → Requirement/Constraint → Quality Scenario → Architekturentscheidung → Test/Evidence → Traceability',
'concepts':[('Requirement','Notwendige Eigenschaft oder Leistung eines Systems oder einer Organisation.','Statusabfrage muss für berechtigte Antragstellende verfügbar sein.'),('Constraint','Randbedingung, die Lösungsraum begrenzt.','Zentrales IAM und vorgegebene Betriebsplattform müssen genutzt werden.'),('Quality Attribute','Qualitätsmerkmal wie Verfügbarkeit, Sicherheit, Änderbarkeit oder Performance.','Registerausfall darf die gesamte Sachbearbeitung nicht blockieren.'),('Quality Scenario','Konkreter Trigger, Kontext, Reaktion und Messwert für ein Qualitätsziel.','Bei Registerausfall wird binnen 5 Sekunden Wartestatus gesetzt; kein Datenverlust.'),('Acceptance Evidence','Nachweis, dass eine Anforderung erfüllt ist.','Restore-Testprotokoll, Lasttest, Security-Test, Architekturreview.')],
'connections':[('Architekturentscheidungen','Requirements liefern Kriterien für Optionen und Trade-offs.'),('Vergabe','Unprüfbare Anforderungen führen zu unprüfbaren Liefergegenständen.'),('Security','Schutzbedarf und Threats werden in testbare Security-Anforderungen übersetzt.'),('Operations','RTO, RPO, SLO und Runbooks operationalisieren Betriebsqualität.'),('Governance','Traceability verbindet Vorgabe, Entscheidung, Umsetzung und Abnahme.')],
'distinctions':[('Need vs. Requirement','Need beschreibt Bedarf; Requirement formuliert überprüfbare Erwartung.'),('Requirement vs. Design','„OIDC“ ist meist Designentscheidung; „föderierte Authentifizierung“ ist die Anforderung.'),('NFR vs. Quality Scenario','Ein Adjektiv ist keine prüfbare Qualitätsanforderung.')],
'method':['Stakeholderbedarfe sammeln','Constraints getrennt erfassen','Architekturtreiber priorisieren','Qualitätsszenarien formulieren','Konflikte/Trade-offs explizit machen','Requirements mit Entscheidungen verknüpfen','Abnahmekriterien und Evidence definieren'],
'questions':['Welcher Stakeholder braucht was und warum?','Ist dies Bedarf, Requirement oder bereits Lösung?','Wie messen wir die Qualität?','Was passiert im Fehlerfall?','Welche Anforderung ist nicht verhandelbar?','Welche Anforderungen widersprechen sich?','Welche Evidence beweist Erfüllung?','Wie bleibt die Traceability erhalten?'],
'artifacts':['Architecture Requirements Log','Quality Attribute Scenarios','Acceptance/Evidence Matrix','Traceability Map','Architecture Evaluation Brief'],
'mistakes':[('Adjektive statt Messgrößen','Kontext, Trigger, Reaktion und Akzeptanzkriterium formulieren.'),('Design als Requirement verkaufen','Lösungsneutralen Bedarf und Designentscheidung trennen.'),('Abnahme erst am Ende','Evidence und Test bereits bei Anforderungsformulierung festlegen.'),('Requirements ohne Owner','Quelle, fachlichen Owner und Priorität dokumentieren.')],
'case':'In einer Ausschreibung steht: „Die Lösung muss hochverfügbar, sicher, performant und datenschutzkonform sein.“',
'caseSolution':'Aussagen in messbare Szenarien zerlegen: kritische Geschäftsprozesse, RTO/RPO, SLO, Lastprofile, IAM/Autorisierung, Logging, Löschung, Restore, Security-Tests; pro Requirement Evidence und Verantwortlichen definieren.',
'deliverable':'Architecture Requirements & Evidence Matrix','exec':'„Eine Qualitätsanforderung ist erst architekturwirksam, wenn sie eine Designentscheidung beeinflusst und später objektiv geprüft werden kann.“',
'sources':['togaf-adm-im-behordenkontext','arc42-in-behorden-anwenden','architekturqualitat-in-ausschreibungen','adr-erstellung-und-praxis'],'anchors':['bsi','evbit']},
{
'n':5,'title':'Datenarchitektur, Governance & Privacy','competency':'Daten & Privacy','description':'Daten als fachliche Verantwortung, Lebenszyklus, Qualitäts- und Datenschutzobjekt modellieren – nicht nur als Tabellen und Datenbanken.',
'analogy':'Daten sind wie Akten mit vielen Kopien: Entscheidend ist nicht nur, wo sie liegen, sondern wer sie führen darf, welche Kopie verbindlich ist, wer sie sehen darf und wann sie verschwinden müssen.',
'model':'Fachobjekt → Semantik → Owner/Steward → führende Quelle → Lebenszyklus → Flüsse/Kopien → Qualität → Schutz/Löschung → Nutzung',
'concepts':[('Data Owner','Fachlich verantwortliche Rolle für Bedeutung, Qualität und Nutzung eines Datenbereichs.','Fachreferat verantwortet Statussemantik, IT betreibt die Datenbank.'),('System of Record','Quelle, deren Wert im definierten Kontext verbindlich ist.','Vorgangsstatus wird im Fachverfahren geführt; Reporting ist nur Konsument.'),('Data Lineage','Nachvollziehbare Herkunft und Transformation von Daten.','Kennzahl im Dashboard lässt sich bis zum Quellattribut zurückverfolgen.'),('Data Quality','Eignung von Daten für ihren fachlichen Zweck.','Vollständigkeit, Aktualität und Eindeutigkeit der Registerdaten.'),('Privacy by Design','Datenschutz wird in Datenflüsse, Zugriff, Speicherung und Löschung eingebaut.','Logs enthalten IDs statt vollständiger Personendaten; Retention ist begrenzt.')],
'connections':[('DDD','Bounded Contexts definieren semantische Grenzen und Datenownership.'),('Integration','Kopien brauchen Synchronisations-, Konflikt- und Löschregeln.'),('Reporting','Kennzahlen sind nur vertrauenswürdig, wenn Lineage und Datenführerschaft klar sind.'),('Security','Schutzbedarf und Zugriff gelten für Datenklassen, nicht nur Anwendungen.'),('AI','RAG und ML benötigen nachvollziehbare, zulässige und qualitativ geeignete Quellen.')],
'distinctions':[('Owner vs. System Owner','Data Owner verantwortet fachliche Bedeutung; System Owner verantwortet das technische System.'),('SoR vs. einzige Kopie','Ein führendes System kann Daten verteilen; Kopien bleiben abgeleitet.'),('Datenqualität vs. technische Validität','Syntaktisch korrekt bedeutet nicht fachlich richtig oder aktuell.')],
'method':['Fachobjekte und Zwecke erfassen','Owner/Stewards benennen','führende Attribute/Quellen festlegen','CRUD und Datenflüsse modellieren','Kopien und Transformationen dokumentieren','Qualitäts-/Schutzregeln definieren','Retention, Löschung und Lineage nachweisen'],
'questions':['Was bedeutet dieses Datenobjekt fachlich?','Wer darf den Wert ändern?','Welche Quelle gewinnt bei Konflikt?','Welche Kopien existieren?','Warum werden Daten gespeichert?','Wer darf sie lesen?','Wann müssen sie gelöscht oder archiviert werden?','Wie wird eine Kennzahl zurück zur Quelle erklärt?'],
'artifacts':['Datenlandkarte','Data Ownership Matrix','System-of-Record-Matrix','Data Lineage Map','Privacy/Data Lifecycle Brief'],
'mistakes':[('System führt „alle Daten“','Attribut- und Kontextführerschaft differenziert festlegen.'),('Reporting erzeugt Wahrheit','Reporting als abgeleitete Sicht mit Lineage behandeln.'),('Löschung nur im Primärsystem','Kopien, Logs, Backups und Exporte in Löschkonzept aufnehmen.'),('Privacy als Dokument','Personenbezug und Zweck direkt in Architekturmodellen sichtbar machen.')],
'case':'Drei Systeme führen Adresse und Bearbeitungsstatus. Das Reporting korrigiert Werte manuell. Niemand kann erklären, welcher Wert im Widerspruchsfall gilt.',
'caseSolution':'Datenobjekte und Attribute trennen, fachliche Owner bestimmen, pro Attribut führende Quelle definieren, Synchronisations- und Konfliktregeln festlegen, manuelle Reporting-Korrekturen eliminieren oder kontrolliert zurückführen; Lineage dokumentieren.',
'deliverable':'Data Ownership & System-of-Record Map','exec':'„Die zentrale Frage ist nicht, wo Daten gespeichert sind, sondern wo ihre fachliche Verbindlichkeit entsteht und wie jede Kopie darauf zurückgeführt wird.“',
'sources':['datenlandkarten-fur-behorden','security-by-architecture-review-anleitung','capability-mapping-bundesbehorden','dmn-entscheidungslogik-und-bpmn'],'anchors':['gdpr','bsi','fit']},
{
'n':6,'title':'Anwendungen, DDD & Domänen','competency':'Anwendungen & Domänen','description':'Fachliche Verantwortungsgrenzen in Domänen, Bounded Contexts und sinnvolle Systemrollen übersetzen; Monolith vs. Microservices kritisch entscheiden.',
'analogy':'Ein Bounded Context ist wie eine Fachsprache mit eigener Bedeutung. „Fall“, „Vorgang“ oder „Kunde“ können in zwei Bereichen unterschiedlich gemeint sein – und sollten nicht automatisch dasselbe Datenmodell teilen.',
'model':'Domäne → Subdomäne → Bounded Context → fachliche Verantwortung → Datenownership → Anwendung/Service → Schnittstellen → Team/Owner',
'concepts':[('Domain','Fachlicher Problemraum, den die Organisation beherrschen muss.','Asylverfahren, Integration, Registerauskunft.'),('Bounded Context','Grenze, innerhalb der Begriffe und Modelle konsistent gelten.','„Status“ im Fachverfahren bedeutet etwas anderes als Zustellstatus im Kommunikationsdienst.'),('Ubiquitous Language','Gemeinsame Sprache von Fachseite und Technik innerhalb eines Kontextes.','Antrag, Nachweis, Vorgang und Bescheid werden eindeutig definiert.'),('System Role','Primäre Verantwortung einer Anwendung im Portfolio.','Führen, Verarbeiten, Anzeigen, Integrieren oder Berichten.'),('Modularer Monolith','Eine deploybare Anwendung mit klar getrennten internen Modulen.','Fachliche Grenzen werden zuerst stabilisiert, bevor verteilte Betriebsprobleme eingeführt werden.')],
'connections':[('Data Ownership','Jeder Kontext braucht klare Datenverantwortung.'),('Integration','Context Maps zeigen, welche Übersetzung an Grenzen notwendig ist.'),('Team Topologies','Teamgrenzen sollten mit stabilen Verantwortungsgrenzen kompatibel sein.'),('Microservices','Servicegrenzen ohne Domänengrenzen erzeugen einen verteilten Monolithen.'),('Portfolio','Zielrollen und Ablöseentscheidungen hängen von fachlicher Verantwortung ab.')],
'distinctions':[('Domain vs. System','Eine Domäne ist fachlich; ein System ist eine technische Realisierung.'),('Bounded Context vs. Microservice','Ein Kontext kann durch einen oder mehrere Module/Services realisiert werden.'),('Modularer Monolith vs. Legacy-Monolith','Modularität und explizite Grenzen sind entscheidend, nicht die Zahl der Deployments.')],
'method':['Fachdomänen und Begriffe entdecken','Konflikte in Begriffsbedeutungen markieren','Bounded Contexts schneiden','Ownership für Daten/Funktionen festlegen','Context Map und Abhängigkeiten modellieren','Applikationsrollen zuordnen','Deployment-/Service-Schnitt erst nach fachlichen Grenzen entscheiden'],
'questions':['Welche Begriffe bedeuten in verschiedenen Bereichen Unterschiedliches?','Wer verantwortet welche Geschäftsregel?','Welche Daten gehören zusammen geändert?','Welche Änderungsgeschwindigkeiten unterscheiden sich?','Welche Teams tragen End-to-End-Verantwortung?','Wo ist Übersetzung zwischen Kontexten nötig?','Brauchen wir wirklich unabhängige Deployments?','Welche Betriebsmehrkosten entstehen durch Verteilung?'],
'artifacts':['Domain Map','Bounded Context Map','Application Role Map','Context Map','Decomposition Decision Record'],
'mistakes':[('Microservices als Modernität','Nur verteilen, wenn fachliche/organisatorische Vorteile die Komplexität rechtfertigen.'),('Datenbanktabellen als Domänengrenzen','Grenzen aus Verantwortung und Sprache ableiten.'),('Shared Database zwischen Kontexten','Ownership und Kopplung explizit machen; Integrationsverträge bevorzugen.'),('DDD nur als Code-Muster','Strategisches DDD zuerst für EA-Systemgrenzen nutzen.')],
'case':'Ein großes Fachverfahren enthält 20 Jahre gewachsene Funktionen. Das Programm fordert „Microservices“, aber Teams und Datenmodell sind weiterhin zentral organisiert.',
'caseSolution':'Domänenanalyse durchführen, Bounded Contexts und Datenownership definieren, zunächst Module kapseln; nur Kontexte mit klarer Ownership, unabhängigen Änderungsbedarfen und Betriebsfähigkeit als Services extrahieren. Transition statt Big Bang.',
'deliverable':'Domain/Bounded-Context Map + Decomposition ADR','exec':'„Wir schneiden nicht nach technischen Schichten, sondern nach fachlicher Verantwortung und Änderungsautonomie.“',
'sources':['applikationsportfolio-bewerten','archimate-fur-behorden-ea','arc42-in-behorden-anwenden','enterprise-architektur-strategie'],'anchors':['nita']},
{
'n':7,'title':'Integration & Distributed Systems','competency':'Integration & Distributed Systems','description':'Schnittstellen, Events und verteilte Fehlerfälle fachlich und technisch beherrschen – von Contract bis Idempotenz, Retry, Saga und Observability.',
'analogy':'Eine Schnittstelle ist kein Rohr, sondern ein Vertrag zwischen zwei verantwortlichen Parteien. Wie bei Postsendungen muss klar sein: Was bedeutet die Nachricht, wer bestätigt, was passiert bei Verlust, Doppelung oder falscher Adresse?',
'model':'Fachliche Übergabe → Contract → Delivery-Modell → Fehler-/Retry-Semantik → Konsistenz → Beobachtbarkeit → Ownership/Lifecycle',
'concepts':[('Interface Contract','Fachlich-technischer Vertrag über Ergebnis, Daten, Fehler, Versionierung und Verantwortung.','Registerabfrage definiert nicht nur JSON, sondern auch fachliche Fehler und SLA.'),('Idempotenz','Wiederholte gleiche Verarbeitung erzeugt nicht mehrfach fachliche Wirkung.','Doppelt zugestellte Zahlungsanweisung löst nur eine Zahlung aus.'),('At-least-once','Nachricht kann mehrfach ankommen, soll aber nicht verloren gehen.','Consumer dedupliziert per fachlicher ID.'),('Eventual Consistency','Verteilte Kopien werden nicht sofort, aber kontrolliert konsistent.','Reporting erhält Statusänderung Sekunden später.'),('Saga','Koordination mehrerer lokaler Transaktionen mit Kompensationen.','Vorgang anlegen, Dokument speichern, Benachrichtigung versenden; Fehler werden gezielt kompensiert.')],
'connections':[('Data Ownership','Integration darf Ownership nicht verwischen; jede Änderung braucht eine verantwortliche Quelle.'),('DDD','Context Boundaries bestimmen, welche Daten und Events Kontextgrenzen überschreiten.'),('Observability','Trace-Kontext und fachliche Korrelation machen End-to-End-Flüsse diagnostizierbar.'),('Security','APIs und Events brauchen Authentifizierung, Autorisierung, Integrität und Datenschutz.'),('Betrieb','Retry, DLQ, Backpressure und Replay sind Betriebsmodelle, nicht nur Code.')],
'distinctions':[('API vs. Event','API fordert direkt Leistung an; Event informiert über eine eingetretene fachliche Tatsache.'),('Asynchron vs. entkoppelt','Zeitliche Entkopplung beseitigt keine semantischen oder organisatorischen Abhängigkeiten.'),('Exactly once vs. fachliche Einmaligkeit','Transportgarantien ersetzen keine idempotente fachliche Verarbeitung.')],
'method':['Fachliches Ergebnis der Übergabe definieren','Provider/Consumer/Owner benennen','Synchron vs. asynchron begründen','Contract inkl. Fehler und Versionierung beschreiben','Delivery-/Retry-/Idempotenzmodell festlegen','Konsistenz und Kompensation entwerfen','Observability, SLO und Betriebsprozesse definieren'],
'questions':['Welche fachliche Wirkung löst die Übergabe aus?','Wer darf Daten ändern?','Was passiert bei Timeout?','Kann eine Nachricht doppelt kommen?','Wie wird Reihenfolge behandelt?','Wie werden Fehler sichtbar und bearbeitet?','Wie wird Versionierung durchgeführt?','Wie können wir einen Vorgang Ende-zu-Ende korrelieren?'],
'artifacts':['Interface Contract','Event Catalog','Error & Retry Matrix','Consistency/Delivery Decision Record','Integration Observability Map'],
'mistakes':[('Nur Endpoint/Payload dokumentieren','Fachliche Semantik, Fehler, Owner und Betrieb ergänzen.'),('Retry ohne Idempotenz','Wiederholung kann doppelte fachliche Wirkung erzeugen.'),('DLQ als Endstation','Owner, Alarmierung, Analyse, Replay und Daten-/Datenschutzregeln definieren.'),('EDA für alles','Asynchronität nur wählen, wenn Nutzen die zusätzliche Komplexität rechtfertigt.')],
'case':'Ein Antrag wird an ein Fachverfahren gesendet. Bei Timeout wiederholt das Portal den Request. Später erscheinen zwei Vorgänge und zwei DMS-Akten.',
'caseSolution':'Idempotency Key und fachliche Korrelation definieren; Create-Operation deduplizieren; Timeout-Semantik und Statusabfrage festlegen; DMS-Erzeugung ebenfalls idempotent gestalten; End-to-End-Tracing und Fehlerstatus ergänzen.',
'deliverable':'Schnittstellenvertrag + Fehler-/Delivery-Matrix','exec':'„Die Architekturfrage lautet nicht nur, ob Nachrichten ankommen, sondern ob fachliche Wirkung unter Fehlern eindeutig und nachvollziehbar bleibt.“',
'sources':['schnittstellenvertrag-erstellen','openapi-asyncapi-bewertung','eda-im-behordenkontext','observability-anforderungen-definieren'],'anchors':['fit','bsi']},
{
'n':8,'title':'Cloud, Plattform & Netzwerk','competency':'Cloud, Plattform & Netzwerk','description':'Cloud- und Plattformentscheidungen als Zusammenspiel von Verantwortungen, Netzwerk, IAM, IaC, Kubernetes, Souveränität, Betrieb und Exit verstehen.',
'analogy':'Eine Plattform ist wie ein gut geführtes Gewerbegebiet: Sie stellt Straßen, Energie, Sicherheitsregeln und gemeinsame Dienste bereit. Die einzelnen Unternehmen bleiben für ihr Geschäft verantwortlich.',
'model':'Workload/Qualitätsziele → Verantwortungsmodell → Landing/Platform Zone → Netzwerk/IAM → Runtime/IaC → Observability/BCM → Kosten/Exit',
'concepts':[('Shared Responsibility','Provider und Nutzer teilen Sicherheits- und Betriebsverantwortung je Service-Modell.','Cloud verschiebt Patchverantwortung, aber nicht Daten- oder Zugriffsverantwortung.'),('Platform Engineering','Interne Plattform als Produkt mit Self-Service und Standards.','Teams bestellen standardisierte Laufzeit, Logging und Secrets über Golden Paths.'),('Landing Zone','Vorkonfigurierte Governance-, IAM-, Netzwerk- und Sicherheitsbasis für Cloud-Nutzung.','Accounts/Subscriptions, Policies, Logging und Netzanbindung sind vorgegeben.'),('Infrastructure as Code','Infrastruktur wird deklarativ, versioniert und reproduzierbar beschrieben.','Netz, Cluster und Policies werden über geprüfte Pull Requests geändert.'),('Network Trust Boundary','Grenze mit expliziten Kommunikations- und Sicherheitsannahmen.','Internet → Gateway → interne Anwendungszone → Datenzone.')],
'connections':[('IAM','Plattformgrenzen sind wertlos ohne Identitäts- und Berechtigungsmodell.'),('Security','Netzsegmentierung, Secrets, Images und Supply Chain sind Architekturthemen.'),('Operations','Plattform muss Monitoring, Backup, Restore und Incident-Fähigkeit liefern.'),('Team Topologies','Plattformprodukt reduziert Cognitive Load, wenn Schnittstellen und Ownership klar sind.'),('Economics','Cloud-Kosten und Exit-Fähigkeit beeinflussen Architekturentscheidungen.')],
'distinctions':[('Cloud vs. Kubernetes','Kubernetes ist Runtime/Orchestrierung; Cloud ist viel breiteres Betriebs- und Servicemodell.'),('Plattform vs. Infrastruktur','Plattform bietet konsumierbare Fähigkeiten und Produktverantwortung, nicht nur Server.'),('Zero Trust vs. kein Netzwerk','Zero Trust ersetzt Netzarchitektur nicht, sondern beseitigt implizites Vertrauen.')],
'method':['Workloads und Qualitätsattribute klassifizieren','Cloud-/Hosting-Constraints und Souveränität klären','Responsibility Matrix erstellen','Netz/IAM/Schlüssel/Logging-Architektur definieren','Runtime und Plattformservices auswählen','IaC/CI-CD/Policy Gates einbauen','Exit, BCM, Kosten und Lifecycle planen'],
'questions':['Welche Daten und Schutzbedarfe liegen vor?','Wer betreibt welche Schicht?','Welche Netze/Zonen kommunizieren?','Wie werden Identitäten föderiert?','Wo liegen Schlüssel und Secrets?','Wie wird Infrastruktur reproduzierbar?','Wie funktioniert Restore/DR?','Wie verlassen wir Provider/Plattform kontrolliert?'],
'artifacts':['Cloud/Platform Decision Canvas','Responsibility Matrix','Network/Trust-Zone Map','Platform Capability Map','Exit & Portability Plan'],
'mistakes':[('Cloud = Rechenzentrum eines anderen','Managed Services, Responsibility und Operating Model differenziert betrachten.'),('Kubernetes als Pflicht','Nur wählen, wenn Workload und Organisation Nutzen daraus ziehen.'),('Netzwerkdetails ignorieren','Zonen, DNS, Proxy, TLS, Ingress/Egress und Verbindungen als Architekturabhängigkeit verstehen.'),('Exit nur vertraglich','Datenexport, IaC, Dokumentation, Skills und Ersatzbetrieb technisch testen.')],
'case':'Ein Dienstleister schlägt Public Cloud + Managed Kubernetes vor. Die Behörde fordert digitale Souveränität und hat zentrale Netz-/IAM-Vorgaben, aber keine Exit-Strategie.',
'caseSolution':'Schutzbedarf/Constraints erfassen, Shared Responsibility und Landing-Zone-Anforderungen definieren, zentrale IAM-/Netzanbindung prüfen, Plattformnutzen bewerten, Daten/Schlüssel/Logs klassifizieren, Kosten- und Exit-Szenario inklusive Portabilität und Ersatzbetrieb erstellen.',
'deliverable':'Cloud/Platform Architecture Brief + Exit Plan','exec':'„Cloud ist keine Standortentscheidung, sondern ein Verantwortungs-, Betriebs- und Sourcingmodell.“',
'sources':['kubernetes-architektur-bewerten','cd-und-iac-architektur','rpo-betriebsfahigkeit-prufen','security-by-architecture-review-anleitung','archimate-fur-behorden-ea'],'anchors':['nita','bsi']},
{
'n':9,'title':'Security, IAM & Privacy','competency':'Security, IAM & Privacy','description':'Security-by-Architecture von Schutzbedarf und Trust Boundaries über IAM, Autorisierung und Privacy bis zu Nachweisen und Dienstleisterzugriffen.',
'analogy':'Security ist wie ein Gebäude mit verschiedenen Sicherheitszonen. Ein Ausweis an der Eingangstür reicht nicht: Jede Zone braucht klare Regeln, wer hinein darf, warum, wie lange und wie der Zugriff nachweisbar wird.',
'model':'Zweck/Schutzbedarf → Assets → Akteure/Identitäten → Trust Boundaries → AuthN/AuthZ → Daten/Controls → Logging/Monitoring → Evidence/Review',
'concepts':[('Authentication','Beweist, wer oder was eine Identität ist.','MFA für Administratoren, OIDC für Nutzer.'),('Authorization','Entscheidet, was eine authentifizierte Identität tun darf.','Sachbearbeiter sieht nur zugewiesene Vorgänge.'),('RBAC/ABAC','Rollen- bzw. attributbasierte Berechtigungsmodelle.','Rolle Sachbearbeitung plus Organisationseinheit und Zuständigkeit.'),('Threat Modeling','Strukturierte Analyse von Assets, Angreifern, Trust Boundaries und Missbrauchspfaden.','Externer Dienstleisterzugang als eigener Angriffsweg.'),('Privacy by Design','Datenschutzanforderungen werden technisch/organisatorisch in den Entwurf integriert.','Minimierte Logs, Retention, Löschpfade, Zugriffstrennung.')],
'connections':[('Data Architecture','Datenklassen und Zwecke bestimmen Schutz- und Löschanforderungen.'),('API/Integration','Objektbezogene Autorisierung und Token-/Serviceidentitäten müssen an Grenzen durchgesetzt werden.'),('Platform','Secrets, Zertifikate, Images und Adminzugriffe sind Plattformkontrollen.'),('Operations','Security Events müssen sichtbar, alarmierbar und untersuchbar sein.'),('Procurement','Security-Anforderungen brauchen testbare Liefergegenstände und Evidence.')],
'distinctions':[('AuthN vs. AuthZ','Identität beweisen ist nicht Berechtigung prüfen.'),('Gateway vs. fachliche Autorisierung','Gateway kann Tokens prüfen; Objekt-/Fachrechte gehören auch ins Backend.'),('Compliance vs. Security','Erfüllte Checkliste ist kein Beweis für wirksame Risikoreduktion.')],
'method':['Zweck und Schutzbedarf klären','Assets/Akteure/Trust Boundaries modellieren','Identity Lifecycle und Rollen definieren','AuthN/AuthZ/Privileged Access entwerfen','Daten-/Privacy-Controls festlegen','Logging/Monitoring/Incident-Evidence definieren','Security Review und Abnahme planen'],
'questions':['Welche Assets sind kritisch?','Welche Identitäten existieren – Menschen und Services?','Wo wechselt Vertrauen?','Wer genehmigt Rollen?','Wie werden Rechte rezertifiziert?','Wie werden Dienstleisterzugriffe begrenzt?','Welche personenbezogenen Daten erscheinen in Logs?','Welche Evidenz beweist Security-Anforderungen?'],
'artifacts':['Security Architecture Review','IAM/Rollenmodell','Trust-Boundary Diagram','Privileged Access Matrix','Security Evidence Plan'],
'mistakes':[('SSO = gutes IAM','Lifecycle, Rollen, Service Accounts und Rezertifizierung zusätzlich klären.'),('Gateway macht API sicher','Backend muss fachliche Autorisierung durchsetzen.'),('Adminzugriff als Dauerlösung','JIT, MFA, Ticketbindung, Logging und Ablaufdatum verlangen.'),('Privacy nur DSFA','Datenflüsse, Löschung, Logs und Zweckbindung technisch sichtbar machen.')],
'case':'Ein externer Dienstleister besitzt dauerhaft VPN- und Cluster-Adminrechte. Nutzerrollen werden lokal gepflegt, Service Accounts haben langlebige Secrets.',
'caseSolution':'Identitäten inventarisieren; zentrale/föderierte AuthN, RBAC/ABAC, PAM/JIT, Ticketbindung, MFA, Session-/Audit-Logs, Secret Rotation und Rezertifizierung einführen; Dienstleisterzugriffe minimieren und Offboarding nachweisen.',
'deliverable':'IAM & Security Architecture Review','exec':'„Security-by-Architecture fragt nicht nur, welche Kontrolle existiert, sondern welche Annahme sie absichert und wie ihre Wirksamkeit nachgewiesen wird.“',
'sources':['iam-architektur-fur-behorden','schutzbedarf-einordnen-bsi','security-by-architecture-review-anleitung','arc42-in-behorden-anwenden'],'anchors':['bsi','gdpr']},
{
'n':10,'title':'Betrieb, Observability & Resilienz','competency':'Betrieb & Resilienz','description':'Betriebsfähigkeit als Architekturqualität: SLI/SLO, Telemetrie, Fehlerklassen, Runbooks, Backup/Restore, RTO/RPO und Notbetrieb.',
'analogy':'Ein Auto ist nicht zuverlässig, weil der Motor im Labor läuft. Es ist zuverlässig, wenn es unter realen Bedingungen beobachtbar ist, Fehler beherrscht, repariert werden kann und nach Ausfall wieder sicher fährt.',
'model':'kritischer Fachprozess → SLI/SLO → Telemetrie/Korrelation → Alert/Runbook → Incident → Recovery/Restore → Lernen/Verbesserung',
'concepts':[('SLI','Messgröße für beobachtbares Serviceverhalten.','Anteil erfolgreich eingereichter Anträge.'),('SLO','Zielwert für ein SLI.','99,5 % erfolgreiche Antragseinreichung im Monatsfenster.'),('Observability','Fähigkeit, innere Systemzustände aus Telemetrie zu verstehen.','Trace zeigt Portal → API → Register → DMS für einen Vorgang.'),('RTO','Zielzeit bis zu einem definierten Wiederanlaufzustand.','Binnen 4 Stunden wieder begrenzte Sachbearbeitung möglich.'),('RPO','Maximal tolerierbarer Datenverlust in Zeit.','Höchstens 15 Minuten bestätigte Vorgangsdaten verlieren.')],
'connections':[('Requirements','RTO/RPO/SLO müssen fachlich abgeleitet und messbar formuliert werden.'),('Integration','Korrelation, Queue Age, Retry und DLQ sind Teil der Observability.'),('Security','Logs sind Security-Evidence, aber zugleich Datenschutzobjekte.'),('Platform','Backup, Restore, HA und DR hängen von Plattformdiensten und Verantwortungen ab.'),('Procurement','Runbooks, Dashboards und Restore-Nachweise gehören in Liefergegenstände.')],
'distinctions':[('Monitoring vs. Observability','Monitoring prüft bekannte Signale; Observability ermöglicht Erklärung unbekannter Zustände.'),('HA vs. DR','Hochverfügbarkeit reduziert Ausfälle; Disaster Recovery stellt nach schwerem Ausfall wieder her.'),('Backup vs. Recovery','Backup ist nur gespeicherte Kopie; Recovery beweist Wiederherstellbarkeit der gesamten Kette.')],
'method':['kritische Fachprozesse/BIA erfassen','SLI/SLO und RTO/RPO ableiten','Telemetrie- und Korrelationskonzept definieren','Fehlerklassen, Alerts und Runbooks festlegen','Backup/Restore/DR-Kette entwerfen','Recovery regelmäßig testen','Post-Incident-Lernen in Architektur/Governance zurückführen'],
'questions':['Welche Nutzerwirkung ist kritisch?','Wie messen wir Erfolg statt nur CPU?','Welche Abhängigkeit kann die Kette stoppen?','Welche Fehler sind fachlich vs. technisch?','Wer reagiert auf welches Alert?','Was ist der Zielzustand nach RTO?','Wann wurde Restore zuletzt real getestet?','Wie werden Lessons Learned umgesetzt?'],
'artifacts':['Operational Architecture Brief','SLI/SLO Catalog','Observability Map','RTO/RPO Matrix','Recovery Evidence Pack'],
'mistakes':[('Alles grün = Prozess funktioniert','End-to-End-Fachwirkung messen.'),('Backups ohne Restore-Test','Recovery-Kette in produktionsnaher Umgebung testen.'),('Alert ohne Owner/Runbook','Jede Alarmierung braucht Handlung und Verantwortlichkeit.'),('RTO als Serverstartzeit','Fachlich nutzbaren Zielzustand definieren.')],
'case':'Alle technischen Dashboards sind grün, aber Bürger erhalten keine Eingangsbestätigung, weil eine Queue langsam wächst. Niemand alarmiert auf Queue Age.',
'caseSolution':'E2E-SLI „Antrag erfolgreich verarbeitet“ definieren, Queue Age und Processing Lag erfassen, fachliche Korrelation einführen, SLO/Alert mit Runbook und Owner definieren; Failure Mode und Capacity/Backpressure analysieren.',
'deliverable':'Observability & Recovery Architecture Pack','exec':'„Betriebsfähigkeit ist erreicht, wenn wir Nutzerwirkung messen, Fehler beherrschen und Wiederherstellung nachweisen können – nicht wenn einzelne Komponenten grün sind.“',
'sources':['observability-anforderungen-definieren','rpo-betriebsfahigkeit-prufen','cd-und-iac-architektur','security-by-architecture-review-anleitung'],'anchors':['bsi']},
{
'n':11,'title':'Transformation & Architekturökonomie','competency':'Transformation & Ökonomie','description':'Roadmaps, Transition Architectures, TCO, technische Schulden, Flow und FinOps zu wirtschaftlich begründbaren Transformationsentscheidungen verbinden.',
'analogy':'Eine Zielarchitektur ist wie das Ziel einer Brückensanierung. Entscheidend ist nicht nur das Endbild, sondern wie der Verkehr während des Umbaus weiterläuft und was jede Zwischenstufe kostet und riskiert.',
'model':'Ist → Treiber/Gaps → Optionen → TCO/Risiko/Nutzen → Transition Architectures → Work Packages → Roadmap → Nutzen-/Kostenkontrolle',
'concepts':[('Transition Architecture','Definierter Zwischenzustand auf dem Weg zum Ziel.','Legacy bleibt lesend aktiv, neue Fälle laufen bereits im Zielsystem.'),('TCO','Gesamtkosten über Lebenszyklus, nicht nur Projektbudget.','Lizenzen, Betrieb, Personal, Migration, Exit und Abschaltung.'),('Cost of Delay','Wertverlust durch verspätete Umsetzung.','Manuelle Bearbeitung verursacht jeden Monat zusätzliche Personentage.'),('Technical Debt','Bewusste oder gewachsene technische Last mit zukünftigen Kosten/Risiken.','Nicht standardisierte Schnittstellen erhöhen jede neue Integration.'),('FinOps','Gemeinsame Steuerung variabler Cloud-Kosten durch Technik, Finance und Business.','Kosten pro Umgebung/Service sichtbar und verantwortet.')],
'connections':[('Portfolio','Roadmaps priorisieren nicht nur Projekte, sondern Capability-Wirkung und Risiko.'),('Operating Model','Transformation ändert Verantwortungen und Betriebsmodelle.'),('Procurement','Vergabe- und Vertragslaufzeiten sind harte Roadmap-Abhängigkeiten.'),('Data Migration','Transitionen müssen Datenführerschaft und Koexistenz regeln.'),('Governance','Gates prüfen, ob Zwischenzustände Zielprinzipien und Risiken beherrschen.')],
'distinctions':[('Roadmap vs. Projektplan','Roadmap ordnet strategische Zustände, Abhängigkeiten und Entscheidungen; Projektplan steuert konkrete Aufgaben.'),('Business Case vs. reine Kostenrechnung','Nutzen, Risiko, Optionen und Unsicherheit gehören dazu.'),('Big Bang vs. Transition','Übergangsarchitektur macht Koexistenz explizit und reduziert Migrationsrisiko.')],
'method':['Ist/Ziel/Gaps beschreiben','Optionen inkl. Nichtstun entwickeln','Kosten/Nutzen/Risiken über Lebenszyklus schätzen','Abhängigkeiten und Vergabefenster erfassen','Transition Architectures definieren','Work Packages priorisieren','Nutzen, Kosten und Architekturgesundheit laufend messen'],
'questions':['Was kostet Nichtstun?','Welche Kosten entstehen erst im Betrieb?','Welche Legacy-Komponente blockiert andere Vorhaben?','Welche Zwischenzustände sind nötig?','Welche Daten koexistieren wie lange?','Welche Verträge laufen wann aus?','Welche Nutzenkennzahl zeigt Fortschritt?','Wann kann Alt wirklich abgeschaltet werden?'],
'artifacts':['Architecture Business Case','Transition Architecture Set','Transformation Roadmap','TCO/Cost-of-Delay Matrix','Decommission Plan'],
'mistakes':[('Nur Projektkosten vergleichen','Lifecycle, Betrieb, Skills, Exit und Ablösung einbeziehen.'),('Roadmap ohne Transition','Zwischenzustände und Koexistenz explizit modellieren.'),('Legacy abschalten „später“','Abschaltkriterien, Datenmigration und Verantwortlichen definieren.'),('Cloudkosten als Finance-Thema','Architekturentscheidungen mit Verbrauchs-/Kostenmodell verbinden.')],
'case':'Eine 20 Jahre alte Anwendung ist teuer, aber fachlich kritisch. Eine sofortige Ablösung dauert drei Jahre und blockiert andere Vorhaben.',
'caseSolution':'Nicht Alter, sondern Wert/Risiko/TCO bewerten. Stabilisierung und Kapselung als erste Transition; Schnittstellen und Datenownership ordnen; schrittweise Funktionsmigration nach Capability/Priorität; Abschaltplan und Nutzenmessung definieren.',
'deliverable':'Transformation Roadmap + Architecture Business Case','exec':'„Wir modernisieren nicht, weil ein System alt ist, sondern weil die Kombination aus fachlichem Wert, Risiko, Änderbarkeit und Lebenszykluskosten eine bessere Option rechtfertigt.“',
'sources':['roadmap-mit-ubergangsarchitekturen','applikationsportfolio-bewerten','architektur-governance-fur-behorden','enterprise-architektur-strategie'],'anchors':['evbit','nita']},
{
'n':12,'title':'Governance, Entscheidungen & Vergabe','competency':'Governance & Vergabe','description':'Decision Rights, Prinzipien, Reviews, ADRs, Ausnahmen und öffentliche Beschaffung so verbinden, dass Architektur vor Umsetzung steuerbar und abnahmefähig wird.',
'analogy':'Governance ist nicht die Polizei der Architektur, sondern die Verkehrsordnung: Sie legt fest, wer Vorfahrt hat, welche Regeln gelten und wie Ausnahmen sicher entschieden werden.',
'model':'Prinzip → Standard → Requirement → Liefergegenstand → Review/Gate → Entscheidung/ADR → Ausnahme → Evidence/Abnahme → Lifecycle',
'concepts':[('Architecture Governance','Strukturen und Prozesse, mit denen Architekturentscheidungen verbindlich und nachvollziehbar werden.','Review vor Ausschreibung und vor Produktionsfreigabe.'),('ADR','Dokumentiert Kontext, Optionen, Entscheidung und Konsequenzen.','Zentrales IAM statt lokaler Nutzerverwaltung.'),('Architecture Principle','Langfristige Leitplanke für wiederkehrende Entscheidungen.','API-Verträge vor Implementierung spezifizieren.'),('Exception','Befristete, begründete Abweichung mit Owner, Risiko und Kompensation.','Legacy-API darf 12 Monate vom Standard abweichen.'),('Acceptance Evidence','Objektiver Nachweis eines Liefergegenstands.','OpenAPI-Datei, Restore-Test, SBOM, Security-Report.')],
'connections':[('Requirements','Standards müssen in prüfbare Anforderungen übersetzt werden.'),('Procurement','Architekturvorgaben wirken nur, wenn sie Teil von Leistungsbeschreibung und Vertrag sind.'),('Security','Security Controls brauchen Evidence und Exception Handling.'),('Roadmap','Gates und Entscheidungen müssen mit Transformationszeitpunkten synchronisiert werden.'),('Consulting','Governance braucht Akzeptanz und verständliche Entscheidungssprache.')],
'distinctions':[('Governance vs. Bürokratie','Governance reduziert Wiederholungsdiskussionen und macht Risiken entscheidbar.'),('Prinzip vs. Standard','Prinzip beschreibt Leitidee; Standard operationalisiert konkrete Prüfkriterien.'),('Review vs. Abnahme','Review bewertet Architektur; Abnahme prüft vertraglich geschuldete Lieferung.')],
'method':['Decision Rights und Gremien klären','Prinzipien/Standards operationalisieren','Review-Trigger und Gates definieren','Entscheidungen per ADR dokumentieren','Ausnahmeprozess mit Ablaufdatum gestalten','Vorgaben in Ausschreibung/Vertrag übersetzen','Evidence und Abnahmeplan führen'],
'questions':['Welche Entscheidung braucht welches Gremium?','Was ist verbindlich, was Empfehlung?','Wie wird Standarderfüllung geprüft?','Was passiert bei Ausnahme?','Welche Architekturartefakte sind Liefergegenstand?','Welche Evidence akzeptiert die Behörde?','Wie wird Open Source/SBOM/Exit geregelt?','Wer verfolgt Auflagen nach dem Review?'],
'artifacts':['Architecture Governance Operating Model','ADR/Decision Log','Review Checklist','Exception Register','Architecture Acceptance Matrix'],
'mistakes':[('Prinzip ohne Prüfkriterium','Konsequenzen, Reviewfrage und Ausnahmeweg ergänzen.'),('Review zu spät','Vor Vergabe, Design-Freeze und Go-live einplanen.'),('Ausnahme ohne Ende','Ablaufdatum, Kompensationsmaßnahme und erneutes Review verlangen.'),('Architektur außerhalb Vertrag','Liefergegenstände, Nachweise und Abnahmekriterien in Vergabe integrieren.')],
'case':'Ein Dienstleister liefert funktional korrekt, aber ohne ADRs, SBOM, Restore-Nachweis und vereinbarte Schnittstellendokumentation. Projektleitung möchte trotzdem abnehmen.',
'caseSolution':'Vertragliche und architektonische Abnahmekriterien prüfen; fehlende Evidence als konkrete Findings dokumentieren; Risiko/Business-Auswirkung erklären; ggf. befristete Teilabnahme nur mit genehmigten Auflagen und Terminen. Governance nicht nachträglich erfinden.',
'deliverable':'Architecture Governance & Acceptance Pack','exec':'„Architekturvorgaben sind erst steuerungswirksam, wenn sie als prüfbare Liefergegenstände, Entscheidungen und Ausnahmen im Lebenszyklus verankert sind.“',
'sources':['architektur-governance-fur-behorden','adr-erstellung-und-praxis','architekturqualitat-in-ausschreibungen','eam-leistungsbild-fur-behorden'],'anchors':['evbit','nita','bsi']},
{
'n':13,'title':'Behördenarchitektur & Verwaltungsdigitalisierung','competency':'Behördenarchitektur','description':'Rechtsbindung, Föderalität, FIM/XÖV/FIT-Connect, DMS/eAkte, digitale Souveränität und behördliche Entscheidungswege als eigene EA-Dimension verstehen.',
'analogy':'Verwaltungs-IT ist kein normaler Online-Shop: Ein digitaler Prozess muss nicht nur bequem sein, sondern rechtlich wirksam, nachvollziehbar, zuständigkeitsgerecht, aktenfähig und revisionsfest funktionieren.',
'model':'Rechts-/Leistungsauftrag → Zuständigkeit → FIM/Prozess → Datenstandard → Fachverfahren/Basisdienste → eAkte/Nachweis → föderale Integration → Betrieb/Governance',
'concepts':[('Verwaltungsleistung','Rechtlich/fachlich definierte Leistung einer öffentlichen Stelle.','Antrag, Prüfung und Bescheid zu einer gesetzlichen Leistung.'),('FIM','Föderales Informationsmanagement für standardisierte Leistungs-, Prozess- und Dateninformationen.','Datenfeldbeschreibung für einen Onlineantrag.'),('XÖV','Standardisierungsrahmen für strukturierten Datenaustausch in der Verwaltung.','XBau oder andere Fachstandards.'),('FIT-Connect','Föderale Infrastruktur zur standardisierten Übermittlung zwischen Onlinediensten und Verwaltungssystemen.','Antrag wird maschinenlesbar an zuständige Behörde übermittelt.'),('eAkte/DMS','Nachweis- und dokumentenzentrierte Informationsführung mit Lebenszyklus und Metadaten.','Bescheid, Nachweise und Kommunikation werden aktenkonform abgelegt.')],
'connections':[('Business Architecture','Gesetzliche Leistung und Prozess sind Startpunkt, nicht die technische Lösung.'),('Data Architecture','FIM/XÖV und Register definieren Semantik und Austausch.'),('Integration','Föderale Basisdienste schaffen standardisierte Übergaben.'),('Security/Privacy','Hoheitliche Daten und Entscheidungen haben hohe Nachweis- und Schutzanforderungen.'),('Procurement','Öffentliche Vergabe, Souveränität und offene Standards beeinflussen Zielarchitektur.')],
'distinctions':[('Digitalisierung vs. PDF','Ein digitaler Prozess ist strukturiert, medienbrucharm und systemisch integrierbar.'),('FIM vs. XÖV','FIM standardisiert Verwaltungsinformationen; XÖV standardisiert fachlichen Datenaustausch in konkreten Domänen.'),('DMS vs. Fachverfahren','DMS/eAkte führt Dokument-/Aktennachweise; Fachverfahren führt fachliche Bearbeitungslogik.')],
'method':['Rechts-/Leistungsauftrag verstehen','Zuständigkeit und Stakeholder erfassen','FIM/Prozess-/Datenstandards prüfen','Fachverfahren, Register, Basisdienste und DMS kartieren','föderale Schnittstellen/Versionen planen','Security/Privacy/Aktenführung einbauen','Architekturrichtlinien und Vergabevorgaben in Governance integrieren'],
'questions':['Welche Rechtsgrundlage und Zuständigkeit gilt?','Welche Datenfelder/Standards existieren?','Welche föderalen Basisdienste sind verbindlich oder sinnvoll?','Welche Nachweise müssen aktenfähig sein?','Welche Register sind autoritativ?','Welche Versionen/Abkündigungen drohen?','Welche Souveränitäts-/Open-Source-Vorgaben gelten?','Welche Gremien entscheiden?'],
'artifacts':['Government Context Map','FIM/XÖV/FIT-Connect Integration Brief','Document/Akte Lifecycle Map','Federal Dependency Map','Authority Architecture Decision Pack'],
'mistakes':[('Unternehmensmuster 1:1 übertragen','Rechtsbindung, Zuständigkeit, Nachweis und Föderalität explizit berücksichtigen.'),('PDF = Digitalisierung','Strukturierte Daten und medienbrucharme Integration anstreben.'),('Standards nur technisch prüfen','Version, Governance, fachliche Semantik und Lifecycle berücksichtigen.'),('DMS zu spät','Akten-/Dokumentenlebenszyklus früh in Prozess und Datenarchitektur integrieren.')],
'case':'Ein neuer Onlinedienst sendet PDF-Anträge per E-Mail. Das Fachverfahren erfasst Daten manuell; DMS-Ablage erfolgt per Upload. Die Behörde möchte „schnell digitalisieren“.',
'caseSolution':'Leistung/FIM-Daten prüfen, strukturierte Fachdatenübermittlung über passende föderale Infrastruktur/Fachstandard untersuchen, Fachverfahrenintegration und DMS/eAkte-Lifecycle gestalten, Zuständigkeit/Routing und Security/Privacy klären; Übergangslösung von Zielbild trennen.',
'deliverable':'Behörden-Integrations- und Aktenarchitektur','exec':'„Verwaltungsdigitalisierung ist erst dann durchgängig, wenn Rechtswirkung, strukturierte Daten, Zuständigkeit, Fachbearbeitung und Aktennachweis in einer Kette funktionieren.“',
'sources':['bpmn-fur-verwaltungsprozesse','capability-mapping-bundesbehorden','security-by-architecture-review-anleitung','togaf-adm-im-behordenkontext','architekturqualitat-in-ausschreibungen'],'anchors':['nita','fit','bsi','evbit']},
{
'n':14,'title':'Consulting, Change & Leadership','competency':'Consulting & Leadership','description':'Als externer EA ohne Linienmacht über Contracting, Fragen, Moderation, Konfliktklärung, Verhandlung und Veränderungsfähigkeit Wirkung erzeugen.',
'analogy':'Ein guter externer EA ist wie ein Navigator: Er steuert nicht selbst das Schiff, aber hilft Crew und Kapitän, Lage, Optionen, Risiken und Kurs so klar zu verstehen, dass gute Entscheidungen möglich werden.',
'model':'Contracting → Stakeholder verstehen → Fragen/Discovery → gemeinsames Bild → Optionen/Trade-offs → Entscheidung → Commitment → Change/Adoption → Nachhalten',
'concepts':[('Contracting','Klärung von Auftrag, Erwartungen, Rollen, Grenzen und Erfolgskriterien.','Sponsor erwartet Zielbild; Projekt erwartet tägliche Designentscheidungen – Konflikt wird früh geklärt.'),('Stakeholder Mapping','Analyse von Einfluss, Interesse, Verantwortung und Haltung.','Fachreferat, IT, ISB, Datenschutz, Betrieb, Vergabe, Dienstleister.'),('Facilitation','Strukturieren eines Gruppenprozesses, ohne die Entscheidung zu dominieren.','Workshop führt von Problem über Optionen zu Beschlussbedarf.'),('Interest-based Negotiation','Interessen hinter Positionen sichtbar machen.','Security fordert „nein“, Projekt fordert „Go-live“ – gemeinsame Interessen: Risiko begrenzen und Termin schützen.'),('Change Adoption','Sicherstellen, dass neue Architektur tatsächlich in Verhalten, Rollen und Prozesse übergeht.','Neuer API-Standard wird durch Templates, Reviews und Coaching verankert.')],
'connections':[('Governance','Moderation führt zu Entscheidungen; Governance macht sie verbindlich.'),('Strategy','Stakeholder akzeptieren Architektur eher, wenn Wirkung und Nutzen sichtbar sind.'),('Requirements','Gute Interviews trennen Bedürfnisse, Annahmen und Lösungen.'),('Leadership','Principal EAs skalieren Wirkung über andere, nicht über eigene Detailarbeit.'),('Change','Ein Zielbild ohne Adoption ist nur Dokumentation.')],
'distinctions':[('Beraten vs. Entscheiden','Beratung verbessert Entscheidungsfähigkeit; Verantwortung bleibt beim Auftraggeber.'),('Moderieren vs. neutral sein','Facilitator steuert Prozess und Qualität, ohne Ergebnis verdeckt vorzugeben.'),('Widerstand vs. Unvernunft','Widerstand enthält oft Information über Risiko, Verlust, Anreiz oder fehlende Beteiligung.')],
'method':['Auftrag/Erfolg explizit contracten','Stakeholder/Interessen kartieren','Interviews mit offenen Hypothesen führen','Problem und Optionen visualisieren','Trade-offs und Konflikte moderieren','Entscheidung/Commitment dokumentieren','Change-Impact, Kommunikation und Adoption nachhalten'],
'questions':['Wer ist Sponsor und wer entscheidet?','Wer verliert durch die Veränderung etwas?','Welche Position verbirgt welches Interesse?','Welche Annahme teilen die Stakeholder nicht?','Was wäre ein akzeptabler Kompromiss?','Welche Grenze darf Architektur nicht überschreiten?','Welche Entscheidung muss eskaliert werden?','Wie erkennen wir echte Adoption?'],
'artifacts':['Stakeholder Map','Consulting Working Agreement','Workshop Decision Canvas','Conflict/Interest Map','Change & Adoption Plan'],
'mistakes':[('Zu früh Lösung präsentieren','Erst Problemverständnis und gemeinsame Kriterien schaffen.'),('Technische Sprache vor Leitung','Wirkung, Risiko, Optionen und Beschlussbedarf formulieren.'),('Widerstand bekämpfen','Ursache und legitime Interessen untersuchen.'),('Unklare Beratungserwartung','Mandat und Grenzen regelmäßig recontracten.')],
'case':'Security lehnt eine Ausnahme ab, Projektleitung droht mit Terminverlust, Fachseite versteht das technische Risiko nicht und Dienstleister behauptet, es gebe keine Alternative.',
'caseSolution':'Positionen in Interessen übersetzen; Risiko und Terminwirkung visualisieren; mindestens drei Optionen inkl. Kompensationskontrollen und Konsequenzen entwickeln; zuständiges Gremium mit klarer Entscheidungsfrage, Empfehlung und Restrestrisiko befähigen.',
'deliverable':'Stakeholder-/Conflict Map + Executive Decision Facilitation Pack','exec':'„Meine Aufgabe ist nicht, den Konflikt zu gewinnen, sondern ihn so zu strukturieren, dass die verantwortliche Stelle eine informierte Entscheidung treffen kann.“',
'sources':['eam-leistungsbild-fur-behorden','togaf-adm-im-behordenkontext','adr-erstellung-und-praxis','enterprise-architecture-hard-skills'],'anchors':['nita']},
{
'n':15,'title':'Innovation, AI & Emerging Technology','competency':'Innovation & AI','description':'Neue Technologien und KI systematisch bewerten: fachlicher Nutzen, Daten, Architektur, Risiko, Evaluation, Human Oversight, Betrieb und Regulierung.',
'analogy':'Ein LLM ist kein allwissender Sachbearbeiter, sondern ein probabilistisches Werkzeug: Es erzeugt plausible Ausgaben aus Mustern. Deshalb muss Architektur festlegen, welche Quellen es nutzen darf, wie Qualität gemessen wird und wo Menschen entscheiden.',
'model':'Use Case/Outcome → Risiko/Klassifikation → Daten/Knowledge → Modell/Build-vs-Buy → Guardrails/Evaluation → Integration → Human Oversight → Monitoring/Governance',
'concepts':[('Foundation Model','Großes vortrainiertes Modell, das für viele Aufgaben angepasst werden kann.','LLM erzeugt Zusammenfassungen oder Klassifikationen.'),('RAG','Retrieval-Augmented Generation verbindet Modellantworten mit externen Wissensquellen.','Assistent sucht freigegebene Verfahrenshinweise und zitiert sie.'),('Evaluation','Messung von Qualität, Sicherheit und Eignung anhand definierter Testfälle.','Faktentreue, Vollständigkeit, Bias, Halluzinationen und Robustheit messen.'),('Human-in-the-loop','Mensch prüft/entscheidet an definierten Stellen.','KI erstellt Entwurf; Sachbearbeitung trifft rechtswirksame Entscheidung.'),('AI Governance','Regeln für Zulässigkeit, Risiko, Daten, Modelle, Monitoring und Verantwortlichkeiten.','Use-Case-Register, Risikoklasse, Freigabe, Monitoring, Incident-Prozess.')],
'connections':[('Data Governance','KI-Qualität hängt von zulässigen, aktuellen und nachvollziehbaren Daten ab.'),('Security/Privacy','Prompts, RAG-Quellen, Modellzugriffe und Logs können sensible Daten enthalten.'),('Architecture Evaluation','Modelle müssen mit Testsets und Qualitätskriterien statt Demo-Eindruck bewertet werden.'),('Procurement','Build-vs-Buy, Daten-/Modellrechte, Exit und Transparenz gehören in Vertrag.'),('Behördenkontext','Grundrechte, Nachvollziehbarkeit und gesetzliche Entscheidungsverantwortung begrenzen Automatisierung.')],
'distinctions':[('Automation vs. AI','Deterministische Regeln unterscheiden sich von probabilistischen Modellen.'),('RAG vs. Fine-Tuning','RAG bringt externes Wissen zur Laufzeit; Fine-Tuning verändert Modellverhalten/Parameter.'),('Assistenz vs. Entscheidung','Textentwurf ist etwas anderes als eine rechtswirksame Bewertung oder Entscheidung.')],
'method':['Use Case und erwarteten Outcome beschreiben','rechtliche/ethische Risikoklasse prüfen','Daten- und Wissensquellen bewerten','Build-vs-Buy und Modellarchitektur entscheiden','Evaluation/Guardrails/Human Oversight definieren','Integration, IAM, Logging und Betrieb entwerfen','Monitoring, Incident, Re-Evaluation und Exit etablieren'],
'questions':['Welche Entscheidung/Wirkung unterstützt KI?','Darf KI hier überhaupt eingesetzt werden?','Welche Daten werden gesendet/gespeichert?','Wie messen wir Fehler/Halluzinationen?','Wo ist menschliche Kontrolle zwingend?','Wie erklären/rekonstruieren wir eine Ausgabe?','Was passiert bei Modell-/Providerwechsel?','Welche AI-Act-/Datenschutzpflichten gelten aktuell?'],
'artifacts':['AI Use-Case Assessment','AI Architecture & Data Flow','Evaluation Plan','Human Oversight/Guardrail Matrix','AI Governance & Monitoring Plan'],
'mistakes':[('Demo = produktionsreif','Evaluation gegen reale Fälle und Risiken verlangen.'),('RAG löst Halluzination','Retrieval, Prompting, Modell und Quellenqualität gemeinsam evaluieren.'),('KI entscheidet „nur unterstützend“','Tatsächliche Wirkung und menschliche Kontrollfähigkeit prüfen.'),('Regelstand auswendig lernen','AI Act und Leitlinien wegen dynamischer Zeitpläne aktuell verifizieren.')],
'case':'Eine Behörde möchte ein LLM zur „Unterstützung der Asylsachbearbeitung“ einsetzen. Der Vorschlag umfasst RAG über Fallakten und eine Empfehlung zur Beweiswürdigung.',
'caseSolution':'Use Case in Teilfunktionen zerlegen; hochriskante/regulatorisch sensible Entscheidungsunterstützung besonders prüfen; Daten-/Grundrechtsrisiken, Zugriff und Protokollierung klären; zulässige Assistenzfunktionen abgrenzen; Evaluation, Human Oversight, Transparenz und Governance entwerfen; aktuelle AI-Act-Zeitlinie verifizieren.',
'deliverable':'AI Architecture & Risk Assessment','exec':'„Bei KI entscheiden wir zuerst über zulässige Wirkung und messbare Qualität – erst danach über Modell, Prompt oder Anbieter.“',
'sources':['enterprise-architektur-strategie','datenlandkarten-fur-behorden','security-by-architecture-review-anleitung','architektur-governance-fur-behorden','observability-anforderungen-definieren'],'anchors':['ai','gdpr','bsi']},
{
'n':16,'title':'EA Practice, Principal Skills & Architecture Leadership','competency':'EA Practice & Leadership','description':'EA als Organisationsfähigkeit etablieren: Repository, Metamodell, Metriken, Communities, Coaching, Priorisierung und Principal-Level-Einfluss.',
'analogy':'Ein Principal EA ist nicht der beste Feuerwehrmann, sondern jemand, der Brandschutz, Bauordnung, Ausbildung und Frühwarnsystem so verbessert, dass weniger Brände entstehen und andere sie sicher beherrschen können.',
'model':'EA Operating Model → Services/Rollen → Repository/Metamodel → Standards/Reviews → Metrics → Community/Coaching → Portfolio Influence → kontinuierliche Verbesserung',
'concepts':[('EA Capability','Organisationsfähigkeit, Architektur systematisch zu entwickeln und zu steuern.','Mandat, Rollen, Services, Governance, Repository und Skills.'),('Metamodel','Regeln, welche Architektur-Objekte und Beziehungen im Repository geführt werden.','Capability → Application → Data Object → Interface → Technology.'),('Architecture Metric','Messgröße für Gesundheit oder Wirkung der Architekturpraxis.','Anteil Anwendungen mit Owner/EOL, Ausnahmealter, Review Lead Time.'),('Community of Practice','Netzwerk für Wissensaustausch, Standards und Lernen.','Solution Architects tauschen ADRs und Patterns aus.'),('Principal Influence','Wirkung über Strategie, Coaching, Standards und schwierige Entscheidungen statt Detailkontrolle.','Ein Principal EA entwickelt drei Architekten und etabliert Reviewprinzipien.')],
'connections':[('Governance','Practice definiert Entscheidungs- und Reviewprozesse.'),('Repository','Architekturwissen muss als Datenmodell gepflegt, nicht nur in Folien gespeichert werden.'),('Leadership','Mentoring und Delegation skalieren Architekturkompetenz.'),('Metrics','Metriken zeigen, ob Standards und Transformation tatsächlich wirken.'),('Strategy/Portfolio','Principal EAs verbinden Architekturprioritäten mit strategischer Investitionssteuerung.')],
'distinctions':[('Repository vs. Dokumentablage','Repository pflegt strukturierte Objekte/Beziehungen/Lifecycle; Ablage speichert Dateien.'),('Metric vs. KPI-Theater','Metriken müssen Entscheidungen oder Verbesserungen ermöglichen.'),('Principal vs. Zentralarchitekt','Principal skaliert andere und Systeme; Zentralarchitekt wird sonst Bottleneck.')],
'method':['EA-Servicekatalog und Rollen definieren','Metamodell/Repository-Governance etablieren','Prinzipien/Standards/Reviewpfade integrieren','Metriken und Reifegradmodell definieren','Community/Coaching-Routinen aufbauen','Portfolio/Strategie-Foren beeinflussen','jährlich Wirkung und Operating Model verbessern'],
'questions':['Welche EA-Services braucht die Organisation wirklich?','Welche Daten müssen im Repository verlässlich sein?','Wer besitzt Architektur-Objekte?','Welche Kennzahl führt zu einer Entscheidung?','Wo ist EA Bottleneck?','Welche Entscheidungen können delegiert werden?','Wie werden Architekten entwickelt?','Wie beweisen wir EA-Nutzen?'],
'artifacts':['EA Operating Model','Architecture Repository Metamodel','EA KPI Dashboard','Maturity Assessment','Architecture Community & Coaching Plan'],
'mistakes':[('EA als zentrale Freigabestelle','Triage, Delegation und klare Standards statt Bottleneck.'),('Repository vollständig modellieren','Nur entscheidungsrelevante Objekte mit Owner/Lifecycle pflegen.'),('Metriken ohne Verhaltenseffekt','Nur Kennzahlen nutzen, die Maßnahmen oder Priorisierung auslösen.'),('Principal macht alles selbst','Coachen, Standards setzen und Entscheidungssysteme verbessern.')],
'case':'Die EA-Funktion wird in fast jedes Projekt gerufen. Drei Architekten bearbeiten 40 Vorhaben, Reviews dauern sechs Wochen, das Repository ist veraltet.',
'caseSolution':'Demand-Triage nach Risiko/Enterprise-Impact einführen; Standards und Self-Service-Templates für Low-Risk-Fälle; Repository-Owner/Lifecycle definieren; Reviews delegieren; KPI für Lead Time, Exception Age und Datenqualität; Community of Practice etablieren.',
'deliverable':'EA Practice Operating Model + Repository/Metric System','exec':'„Principal-EA-Leistung zeigt sich nicht daran, wie viele Entscheidungen ich selbst treffe, sondern wie zuverlässig die Organisation ohne mich gute Architekturentscheidungen treffen kann.“',
'sources':['eam-leistungsbild-fur-behorden','architektur-governance-fur-behorden','enterprise-architektur-strategie','enterprise-architecture-hard-skills'],'anchors':['nita']},
]

STAGES=[
('Grundlagen einfach verstehen','Grundlage',14),
('Begriffe, Bausteine und Abgrenzungen','Grundlage+',17),
('Querverbindungen und systemisches Denken','Aufbau',20),
('Methode im EA-Mandat anwenden','Praxis',24),
('Behördenfall Schritt für Schritt lösen','Transfer',26),
('Profi-Niveau: liefern, reviewen und verteidigen','Professional',30),
]

# Cross-course links: course numbers that are especially related.
REL={1:[2,12,14,16],2:[1,3,11,16],3:[2,4,5,6],4:[3,9,10,12],5:[3,6,7,9,15],6:[5,7,8,11],7:[5,6,9,10],8:[7,9,10,11],9:[4,5,7,8,10],10:[4,7,8,9,11],11:[2,6,8,10,12],12:[1,4,9,11,14],13:[3,5,7,9,12],14:[1,2,12,16],15:[5,8,9,12,13],16:[1,2,12,14]}

COURSE_BY_N={x['n']:x for x in C}

def lit_for(course, stage_idx):
    books=BOOKS.get(course['n'],[])
    if not books: return []
    # Four references per unit, rotating through all 10 over the course.
    start=(stage_idx*2)%len(books)
    picks=[books[(start+i)%len(books)] for i in range(4)]
    return picks

def anchor_objs(course): return [ANCHORS[k] for k in course.get('anchors',[]) if k in ANCHORS]

def project_sources(course):
    kws=[t for t,_,_ in course['concepts'][:3]]+[course['title'].split('&')[0].strip()]
    return [source_excerpt(mid,kws) for mid in course['sources'][:4]]

def concepts_text(course):
    return ' '.join(f"{term}: {simple} Beispiel: {ex}" for term,simple,ex in course['concepts'])

def method_text(course):
    return ' '.join(f"{i+1}. {x}." for i,x in enumerate(course['method']))

def questions_text(course): return ' '.join(f"• {q}" for q in course['questions'])

def stage_unit(course, si):
    stage_title, level, mins=STAGES[si]
    uid=f"v4-{course['n']:02d}-{si+1:02d}-{slug(course['title'])}"
    literature=lit_for(course,si)
    if si==0:
        core=f"{course['title']} von Grund auf: zuerst Zweck, Sprache und einfache Beispiele verstehen."
        narrative=[
          {'heading':'1. Das Thema in einem Satz','text':course['description']},
          {'heading':'2. Einfache Vorstellung','text':course['analogy']},
          {'heading':'3. Die fünf Grundbegriffe','text':concepts_text(course)},
          {'heading':'4. Ein einfaches Behördenbeispiel','text':f"Stell dir folgende Situation vor: {course['case']} Noch musst du sie nicht vollständig lösen. Suche nur nach den Begriffen aus dieser Einheit: Wer trägt Verantwortung? Welche Daten, Systeme, Risiken oder Entscheidungen erkennst du?"},
          {'heading':'5. Warum ein EA das braucht','text':f"Als externer EA musst du {course['title']} nicht als Spezialist bis ins letzte Implementierungsdetail beherrschen. Du musst jedoch genug verstehen, um die richtigen Fragen zu stellen, lokale Entscheidungen auf Enterprise-Wirkung zu prüfen und geeignete Spezialisten einzubinden. Das mentale Grundmodell lautet: {course['model']}"},
          {'heading':'6. Merksatz','text':course['exec']},
        ]
        objectives=[f"die Kernidee von {course['title']} in einfacher Sprache erklären",'die fünf Grundbegriffe mit eigenen Beispielen wiedergeben','im Behördenfall erste relevante Architekturfragen erkennen','das Thema von benachbarten Begriffen grob abgrenzen']
        soc=['Wie würdest du das Thema einer fachlichen Führungskraft ohne Fachjargon erklären?','Welche zwei Begriffe werden in Projekten wahrscheinlich verwechselt?','Welche Entscheidung wäre gefährlich, wenn dieses Grundwissen fehlt?']
        scenario={'label':'Erster Transfer','prompt':course['case'],'answer':f"Erster Schritt: Problem nicht vorschnell technisch lösen. Nutze das Grundmodell {course['model']} und identifiziere Verantwortungen, fachliche Wirkung und offene Annahmen. Die vollständige Lösung folgt in Stufe 5."}
        deliver=f"Einseitiger Lernzettel: Kernidee, 5 Begriffe, 1 Behördenbeispiel zu {course['title']}"
    elif si==1:
        core=f"Die Bausteine von {course['title']} sauber unterscheiden und als Modell zusammensetzen."
        narrative=[
          {'heading':'1. Vom Wort zum Modell','text':f"Nachdem die Grundbegriffe bekannt sind, brauchst du eine Struktur. Nutze dieses Modell: {course['model']}. Es zeigt eine Reihenfolge, aber keine starre Wasserfallmethode. In realen Mandaten springst du zurück, wenn neue Erkenntnisse frühere Annahmen verändern."},
          {'heading':'2. Begriffe im Zusammenhang','text':concepts_text(course)},
          {'heading':'3. Wichtige Abgrenzungen','text':sentence_list([f"{a}: {b}" for a,b in course['distinctions']])},
          {'heading':'4. Negativbeispiel','text':f"Typisch problematisch ist: {course['mistakes'][0][0]}. Warum? {course['mistakes'][0][1]} Ein EA trainiert, ähnliche Begriffe und Ebenen nicht zu vermischen."},
          {'heading':'5. Modellierungsfrage','text':f"Versuche den Behördenfall in fünf Kästen zu zeichnen. Nutze {course['model']}. Markiere danach, welche Kästen Fakten, Annahmen oder Entscheidungen enthalten."},
          {'heading':'6. Ergebnis','text':f"Du solltest jetzt erklären können, wie die Bausteine zusammenhängen, ohne sofort in Tools oder Technologien zu springen."},
        ]
        objectives=['die zentralen Bausteine voneinander abgrenzen',f"das mentale Modell {course['model']} erklären",'typische Ebenenverwechslungen erkennen','einen einfachen Zusammenhang als Architekturmodell skizzieren']
        soc=['Welche zwei Konzepte sehen ähnlich aus, haben aber unterschiedliche Verantwortung?','Wo im mentalen Modell entsteht fachliche Wahrheit, wo technische Realisierung?','Welche falsche Modellgrenze würde später Kopplung erzeugen?']
        scenario={'label':'Modellierungsübung','prompt':course['case'],'answer':f"Ordne den Fall entlang des Modells: {course['model']}. Nutze die Abgrenzungen, bevor du Lösungskomponenten auswählst."}
        deliver=f"Konzept-/Abgrenzungsdiagramm zu {course['title']}"
    elif si==2:
        core=f"{course['title']} mit anderen EA-Domänen verbinden und Trade-offs systemisch erkennen."
        narrative=[
          {'heading':'1. Warum Querverbindungen entscheidend sind','text':"Enterprise Architecture beginnt dort, wo eine lokale Entscheidung systemische Folgen hat. Deshalb lernst du jetzt nicht mehr nur das Thema selbst, sondern seine Wirkung auf andere Architekturdomänen."},
          {'heading':'2. Die wichtigsten Verbindungen','text':sentence_list([f"{a}: {b}" for a,b in course['connections']])},
          {'heading':'3. Kausalkette','text':f"Nutze als Denkkette: {course['model']}. Frage bei jeder Station: Wenn ich hier eine Entscheidung ändere – welche Stationen verändern sich mit?"},
          {'heading':'4. Trade-off-Denken','text':f"Eine gute Architekturentscheidung maximiert nicht alle Ziele gleichzeitig. Beispiel aus dem Thema: {course['case']} Eine strengere Standardisierung kann Betrieb vereinfachen, aber lokale Änderungsfreiheit reduzieren. Mehr Entkopplung kann Autonomie erhöhen, aber Observability und Konsistenz komplexer machen."},
          {'heading':'5. Behördenkontext','text':"In Behörden kommen zusätzliche Kopplungen hinzu: Rechtsgrundlage, Zuständigkeit, Datenschutz, BSI-Security, Betrieb, Vergabe, föderale Standards und externe Dienstleister. Eine technisch lokale Änderung kann deshalb eine organisatorische oder regulatorische Enterprise-Wirkung haben."},
          {'heading':'6. Systemischer Merksatz','text':"Frage nie nur: Funktioniert die Lösung? Frage zusätzlich: Welche Verantwortung, Daten, Risiken, Kosten, Betriebsmodelle und zukünftigen Veränderungen bindet sie an sich?"},
        ]
        objectives=['mindestens fünf Querverbindungen erklären','eine Kausalkette über mehrere EA-Domänen bilden','Trade-offs statt „beste Lösung“ formulieren','Enterprise-Auswirkung einer lokalen Entscheidung beurteilen']
        soc=['Welche Entscheidung in diesem Thema kann Datenownership verändern?','Welche Entscheidung erhöht Betriebs- oder Security-Komplexität?','Welche scheinbar lokale Wahl könnte Vergabe oder Roadmap beeinflussen?']
        scenario={'label':'Systemischer Transfer','prompt':course['case'],'answer':f"Analysiere nicht nur das unmittelbare Problem. Prüfe mindestens die Verbindungen zu {', '.join(a for a,_ in course['connections'][:4])}. Formuliere pro Verbindung eine Auswirkung oder offene Frage."}
        deliver=f"Cross-Domain Impact Map für {course['title']}"
    elif si==3:
        core=f"Eine wiederholbare Methode für {course['title']} im realen Behördenmandat anwenden."
        narrative=[
          {'heading':'1. Methode statt Bauchgefühl','text':f"Professionelle Beratung braucht ein reproduzierbares Vorgehen. Für {course['title']} nutzt du folgende Sequenz: {method_text(course)}"},
          {'heading':'2. Schritt-für-Schritt','text':method_text(course)},
          {'heading':'3. Interview- und Reviewfragen','text':questions_text(course)},
          {'heading':'4. Artefakte','text':f"Typische Liefergegenstände sind: {', '.join(course['artifacts'])}. Du erstellst sie nicht automatisch alle. Wähle nur Artefakte, die eine Entscheidung, Risikoaufklärung, Abstimmung oder Umsetzung konkret unterstützen."},
          {'heading':'5. Evidence','text':"Jede wichtige Aussage braucht einen Evidenztyp: bestätigte Fachinformation, System-/Konfigurationsnachweis, Test, Messwert, Vertrag, Standard oder dokumentierte Entscheidung. Markiere Annahmen explizit und plane, wie sie verifiziert werden."},
          {'heading':'6. Externer-EA-Rollenregel','text':"Du erhebst, analysierst, visualisierst, bewertest, entwickelst Optionen und Empfehlungen und dokumentierst Konsequenzen. Hoheitliche, fachliche und formale Entscheidungen verbleiben bei den verantwortlichen Stellen der Behörde."},
        ]
        objectives=['die Methode ohne Vorlage wiedergeben','geeignete Fragen für Interviews/Reviews stellen','Artefakte nach Entscheidungsnutzen auswählen','Evidence und Annahmen sauber trennen']
        soc=['Welcher Methodenschritt wird in Projekten am ehesten übersprungen?','Welche Frage würde eine falsche Annahme am schnellsten entlarven?','Welches Artefakt wäre hier überflüssig, wenn keine Entscheidung daran hängt?']
        scenario={'label':'Mandatsübung','prompt':f"Du erhältst Montagmorgen den Auftrag zu {course['title']}. Nach zwei Wochen soll ein entscheidungsfähiges Ergebnis vorliegen. Wie strukturierst du die Arbeit?",'answer':f"Nutze die Sequenz {method_text(course)}. Plane Stakeholder, Evidenz, Artefakt und Entscheidung explizit. Ergebnis soll keine Themenliste, sondern eine klare Entscheidungsgrundlage sein."}
        deliver=f"Arbeitsplan + {course['artifacts'][0]}"
    elif si==4:
        core=f"Einen realistischen Behördenfall zu {course['title']} vollständig analysieren und lösen."
        narrative=[
          {'heading':'1. Fall','text':course['case']},
          {'heading':'2. Nicht sofort lösen','text':"Formuliere zuerst Problem, betroffene Stakeholder, bekannte Fakten, Annahmen und fehlende Informationen. Trenne Symptome von Ursachen."},
          {'heading':'3. Analyse','text':f"Nutze das Modell {course['model']} und die Methode aus Stufe 4. Stelle mindestens diese Fragen: {questions_text(course)}"},
          {'heading':'4. Musterlösung – Denkweg','text':course['caseSolution']},
          {'heading':'5. Optionen und Trade-offs','text':"Formuliere mindestens zwei realistische Optionen plus ‚Nichtstun/Status quo‘. Bewerte fachliche Wirkung, Daten, Security/Privacy, Betrieb, Kosten, Lieferfähigkeit, Abhängigkeiten und Transformationsrisiko. Eine Empfehlung ohne verworfene Alternative ist schwer prüfbar."},
          {'heading':'6. Kommunikation','text':f"Executive-Formulierung: {course['exec']}"},
        ]
        objectives=['einen komplexen Behördenfall strukturiert zerlegen','fehlende Informationen von Annahmen trennen','mindestens zwei Optionen mit Trade-offs bilden','eine begründete EA-Empfehlung formulieren']
        soc=['Welches sichtbare Symptom ist wahrscheinlich nicht die eigentliche Ursache?','Welche Information könnte deine Empfehlung komplett drehen?','Welche Option würdest du einem Architekturboard zeigen und warum?']
        scenario={'label':'Behördenfall','prompt':course['case'],'answer':course['caseSolution']}
        deliver=f"Decision Brief zum Fall: {course['artifacts'][0]} + Optionen/Trade-offs"
    else:
        core=f"{course['title']} auf professionellem EA-Niveau liefern, reviewen, verteidigen und in Governance verankern."
        narrative=[
          {'heading':'1. Definition von Profi-Niveau','text':"Profi-Niveau bedeutet nicht, jedes Detail selbst implementieren zu können. Es bedeutet: fachlich richtige Fragen stellen, Spezialisten auf Augenhöhe challengen, Auswirkungen über Domänen hinweg erkennen und ein belastbares Artefakt erzeugen, das eine Entscheidung oder Abnahme trägt."},
          {'heading':'2. Kernliefergegenstand','text':f"Du sollst professionell liefern können: {course['deliverable']}. Typische Bestandteile: Ziel/Scope, Annahmen, Stakeholder/Owner, Ist-/Zielbild, Optionen, Trade-offs, Risiken, Entscheidungen, offene Punkte, Evidence und nächste Schritte."},
          {'heading':'3. Qualitätskriterien','text':"Ein gutes Artefakt ist entscheidungsorientiert, nachvollziehbar, aktuell, versioniert, adressatengerecht und prüfbar. Es zeigt nicht nur die Empfehlung, sondern auch verworfene Optionen, Restunsicherheiten und Konsequenzen."},
          {'heading':'4. Reviewfähigkeit','text':f"Reviewfragen: {questions_text(course)} Ergänze immer: Welche Annahme ist nicht belegt? Welche Gegenposition ist plausibel? Welche Evidence fehlt vor Freigabe?"},
          {'heading':'5. Gremienfähigkeit','text':f"Du verdichtest technische Komplexität auf Wirkung, Risiko, Optionen und Beschlussbedarf. Beispiel: {course['exec']}"},
          {'heading':'6. Transfer in Governance','text':"Nach der Entscheidung endet EA-Arbeit nicht: ADR/Decision Log aktualisieren, Requirements/Standards übersetzen, Auflagen verfolgen, Review-/Abnahmezeitpunkte planen und neue Erkenntnisse in Roadmap oder Prinzipien zurückführen."},
        ]
        objectives=[f"{course['deliverable']} erstellen",'das Artefakt gegen Fach-, Security-, Betriebs- und Governancefragen verteidigen','eine Executive Summary mit klarer Entscheidung formulieren','Entscheidung in Governance und Umsetzung nachhalten']
        soc=['Woran erkennt ein unabhängiger Reviewer, dass deine Empfehlung belastbar ist?','Welche Gegenargumente würde ein guter Dienstleister oder Fachbereich bringen?','Welche Evidence fehlt, bevor du „grün“ empfehlen würdest?']
        scenario={'label':'Board-Simulation','prompt':f"Du hast 7 Minuten im Architekturboard. Stelle die Empfehlung zu folgendem Fall vor und beantworte kritische Rückfragen: {course['case']}",'answer':f"Struktur: 1) Entscheidungssatz, 2) fachlicher Treiber, 3) Optionen/Trade-offs, 4) Empfehlung, 5) Hauptrisiken/Evidence, 6) konkrete Beschluss-/Auflagenfrage. Kerninhalt: {course['caseSolution']}"}
        deliver=course['deliverable']

    # Common fields
    mistakes=[{'claim':a,'correction':b} for a,b in course['mistakes']]
    distinctions=[{'title':a,'text':b} for a,b in course['distinctions']]
    connections=[{'title':a,'text':b} for a,b in course['connections']]
    examples=[{'context':'Einfaches Beispiel','text':x[2]} for x in course['concepts'][:3]]
    terms=[x[0] for x in course['concepts']]
    checkpoints=[
      [f"Was ist die Kernidee dieser Stufe von {course['title']}?",core],
      ["Nenne eine wichtige Abgrenzung.",f"{course['distinctions'][0][0]}: {course['distinctions'][0][1]}"],
      ["Welche Querverbindung ist besonders wichtig?",f"{course['connections'][0][0]}: {course['connections'][0][1]}"],
      ["Was musst du auf Profi-Niveau liefern können?",course['deliverable']],
    ]
    mastery={
      'wissen':f"Du kannst die Begriffe und Kernidee dieser Stufe zu {course['title']} ohne Vorlage erklären.",
      'verstehen':f"Du kannst Abgrenzungen und mindestens drei Querverbindungen von {course['title']} begründen.",
      'anwenden':f"Du kannst den Behördenfall analysieren: {course['case']}",
      'liefern':f"Du kannst professionell liefern/reviewen: {course['deliverable']}.",
    }
    return {
      'id':uid,'courseId':f"course-{course['n']:02d}",'courseOrder':si+1,'title':f"{stage_title}: {course['title']}",
      'track':f"{course['n']} · {course['title']}",'competency':course['competency'],'level':level,'minutes':mins,
      'basis':'Projektquellen + Fachliteratur + aktuelle Behördenanker','sourceModules':course['sources'],'terms':terms,
      'objectives':objectives,'core':core,'whyItMatters':course['description'],'mentalModel':course['model'],'narrative':narrative,
      'connections':connections,'distinctions':distinctions,'misconceptions':mistakes,'examples':examples,'scenario':scenario,
      'deliverable':deliver,'checkpoints':checkpoints,'reviewQuestions':course['questions'],'socraticQuestions':soc,'mastery':mastery,
      'sources':project_sources(course),'sourceNote':'Projektquellen bilden den Behörden-/Projektanker. Die didaktische Synthese wird durch die ausgewählte Fachliteratur ergänzt; normative Aussagen sind gegen die angegebenen Aktualitätsanker zu prüfen.',
      'literature':literature,'currentAnchors':anchor_objs(course),'executiveStatement':course['exec'],
      'relatedUnits':[]
    }

UNITS=[stage_unit(c,si) for c in C for si in range(6)]
U_BY={(u['courseId'],u['courseOrder']):u for u in UNITS}
# Related units: adjacent stages + related courses matching same stage or foundation.
for u in UNITS:
    n=int(u['courseId'].split('-')[1]); order=u['courseOrder']; rel=[]
    for o in (order-1,order+1):
        x=U_BY.get((u['courseId'],o))
        if x: rel.append({'id':x['id'],'title':x['title'],'track':x['track'],'reason':'Vorherige/nächste Lernstufe desselben Kurses.'})
    for rn in REL.get(n,[])[:4]:
        rc=f"course-{rn:02d}"; ro=3 if order>=3 else 1
        x=U_BY.get((rc,ro))
        if x: rel.append({'id':x['id'],'title':x['title'],'track':x['track'],'reason':'Fachliche Querverbindung zwischen den Kompetenzfeldern.'})
    u['relatedUnits']=rel[:6]

# Cards: five active-recall cards per unit.
CARDS=[]
for u in UNITS:
    course=COURSE_BY_N[int(u['courseId'].split('-')[1])]
    base={'unit':u['id'],'module':course['sources'][0],'competency':u['competency'],'concepts':u['terms']}
    cards=[
      ('concept',f"Erkläre die Kernidee: {u['title']}.",u['core'],'Verdichte Zweck und Wirkung in eigenen Worten.',1),
      ('distinction',f"Grenze im Kontext von {course['title']} ab: {course['distinctions'][0][0]}.",course['distinctions'][0][1],'Abgrenzungen verhindern Ebenen- und Verantwortungsverwechslungen.',2),
      ('connection',f"Welche Verbindung besteht zwischen {course['title']} und {course['connections'][0][0]}?",course['connections'][0][1],'Denke über Domänengrenzen hinweg.',2),
      ('scenario',u['scenario']['prompt'],u['scenario']['answer'],'Formuliere erst Problem, fehlende Information, Optionen und Risiken.',3),
      ('delivery',f"Was musst du zu „{u['title']}“ professionell liefern oder reviewen können?",u['deliverable'],'Profi-Kompetenz zeigt sich an belastbarer Lieferung und Verteidigung, nicht am Wiedererkennen von Begriffen.',3),
    ]
    for i,(typ,q,a,e,diff) in enumerate(cards,1):
        CARDS.append({'id':f"{u['id']}-c{i}",**base,'type':typ,'question':q,'answer':a,'explanation':e,'difficulty':diff})

# Curriculum paths = 16 stepwise courses.
PATHS=[]
for c in C:
    ids=[u['id'] for u in UNITS if u['courseId']==f"course-{c['n']:02d}"]
    PATHS.append({'id':f"course-{c['n']:02d}",'title':c['title'],'description':c['description'],'units':ids})

# Keep original source paths but replace curriculum and cards.
learning=json.load(open(CONTENT/'learning.json',encoding='utf-8'))
learning['version']='4.0.0'
learning['cards']=CARDS
learning['competencies']=[c['competency'] for c in C]
learning['curriculumPaths']=PATHS
json.dump(learning,open(CONTENT/'learning.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)

units_obj={'version':'4.0.0','generatedAt':datetime.now(timezone.utc).isoformat(),'method':'16 stepwise courses × 6 levels: foundations → distinctions → connections → method → authority case → professional delivery','courses':[{'id':f"course-{c['n']:02d}",'title':c['title'],'description':c['description'],'competency':c['competency'],'model':c['model'],'deliverable':c['deliverable']} for c in C],'units':UNITS}
json.dump(units_obj,open(CONTENT/'units.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)

# Books JSON for app/reference use.
books_obj={'version':'2026.09','generatedAt':datetime.now(timezone.utc).isoformat(),'themes':[]}
for c in C:
    books_obj['themes'].append({'courseId':f"course-{c['n']:02d}",'title':c['title'],'books':BOOKS.get(c['n'],[])})
json.dump(books_obj,open(CONTENT/'books.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)

# Version/index.
INDEX['contentVersion']='4.0.0'; INDEX['generated']=datetime.now(timezone.utc).isoformat()
json.dump(INDEX,open(CONTENT/'index.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
json.dump({'version':'4.0.0','released':'2026-09-19','message':'Neues Schritt-für-Schritt-Curriculum: 16 Kurse, 96 Lerneinheiten, 480 aktive Lernkarten, Fachliteratur und aktuelle Behördenanker.'},open(CONTENT/'version.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)

print(f"Built {len(PATHS)} courses, {len(UNITS)} units, {len(CARDS)} cards")
