#!/usr/bin/env python3
import json, re, pathlib, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONTENT = ROOT / 'content'
CAT = json.loads((CONTENT/'index.json').read_text(encoding='utf-8'))

# Curated EA vocabulary. Definitions are concise syntheses of the project material;
# examples are extracted from the actual project modules below.
TERMS = {
'TOGAF': ('Framework und Methodensammlung für Enterprise Architecture; im Projekt vor allem als strukturierte Klärungs- und Entscheidungslogik über den Architekturlebenszyklus genutzt.', ['The Open Group Architecture Framework']),
'ADM': ('Architecture Development Method von TOGAF: ein iteratives Vorgehen von Mandat und Vision über Architekturdomänen, Optionen und Migration bis Governance und Veränderung.', ['Architecture Development Method']),
'Architecture Vision': ('Kurzes, entscheidungsorientiertes Ziel- und Nutzenbild, das Scope, Treiber, Leitplanken und gewünschte Richtung der Architekturarbeit festhält.', ['Architekturvision']),
'Business Architecture': ('Sicht auf Fähigkeiten, Leistungen, Prozesse, Rollen und Verantwortungen einer Organisation – unabhängig von konkreter Technologie.', ['Geschäftsarchitektur']),
'Data Architecture': ('Sicht auf Datenobjekte, Datenverantwortung, Führerschaft, Flüsse, Qualität, Schutzbedarf und Lebenszyklus.', ['Datenarchitektur']),
'Application Architecture': ('Sicht auf Anwendungen, Anwendungsservices, Systemrollen und ihre Beziehungen zu Fachfähigkeiten und Daten.', ['Applikationsarchitektur', 'Anwendungsarchitektur']),
'Technology Architecture': ('Sicht auf Plattformen, Infrastruktur, Runtime, Netzwerk, IAM, Deployment, Monitoring, Backup und andere technische Betriebsgrundlagen.', ['Technologiearchitektur']),
'Requirements Management': ('Laufende Steuerung von Anforderungen, Constraints, Risiken, Annahmen und Entscheidungen über alle Architekturphasen hinweg.', ['Anforderungsmanagement']),
'Baseline Architecture': ('Dokumentierter relevanter Ist-Zustand einer Architektur, gegen den ein Zielbild und Veränderungsbedarf bewertet werden.', ['Baseline', 'Ist-Architektur']),
'Target Architecture': ('Angestrebter Soll-Zustand einer Architektur, der Fähigkeiten, Daten, Anwendungen und Technologie in einen konsistenten Zielzustand bringt.', ['Target', 'Zielarchitektur']),
'Gap': ('Relevante Lücke zwischen Ist- und Zielarchitektur, aus der ein konkreter Veränderungs-, Risiko- oder Entscheidungsbedarf abgeleitet wird.', ['Gap Analysis', 'Gap-Analyse']),
'Transition Architecture': ('Bewusst gestalteter Zwischenzustand auf dem Weg von Ist zu Ziel – mit klaren Bedingungen, Risiken, Verantwortungen und Ablösepfad.', ['Übergangsarchitektur']),
'Roadmap': ('Begründete Reihenfolge von Architekturmaßnahmen, Work Packages, Übergangszuständen, Abhängigkeiten und Entscheidungsfenstern.', ['Architekturroadmap', 'Transformationsroadmap']),
'Work Package': ('Abgrenzbare Veränderungseinheit, die einen Teil der Zielarchitektur realisiert und Liefergegenstände, Abhängigkeiten, Risiken und Akzeptanzkriterien besitzt.', ['Arbeitspaket']),
'Capability': ('Relativ stabile Fähigkeit einer Organisation, ein fachliches Ergebnis zu erbringen – unabhängig von konkretem Prozess, Projekt oder IT-System.', ['Fähigkeit']),
'Capability Mapping': ('Methode, Fähigkeiten einer Organisation strukturiert zu erfassen und mit Verantwortungen, Daten, Anwendungen, Risiken und Vorhaben zu verbinden.', ['Capability Map']),
'BPMN': ('Notation zur Modellierung von Geschäfts- und Verwaltungsprozessen, besonders geeignet für Abläufe, Rollen, Ereignisse, Entscheidungen und Übergaben.', ['Business Process Model and Notation']),
'DMN': ('Notation zur expliziten Modellierung von Entscheidungslogik und Entscheidungsregeln, oft ergänzend zu BPMN.', ['Decision Model and Notation']),
'ArchiMate': ('Modellierungssprache für Enterprise Architecture, mit der Beziehungen zwischen Business, Anwendungen, Daten, Technologie und Transformation sichtbar werden.', []),
'arc42': ('Struktur für Softwarearchitekturdokumentation, die Kontext, Bausteine, Laufzeit, Verteilung, Entscheidungen, Qualitätsziele und Risiken systematisch ordnet.', []),
'ADR': ('Architecture Decision Record: kompakte Dokumentation einer relevanten Architekturentscheidung mit Kontext, Treibern, Optionen, Entscheidung und Konsequenzen.', ['Architecture Decision Record']),
'Governance': ('Verbindlicher Klärungs- und Entscheidungsrahmen, der Rollen, Reviews, Regeln, Ausnahmen und Nachweise für Architekturarbeit festlegt.', ['Architektur-Governance']),
'Architecture Board': ('Gremium oder Entscheidungsformat, in dem architekturrelevante Fragen, Abweichungen und Zielbildentscheidungen bewertet und entschieden werden.', ['Architekturboard']),
'Architecture Principle': ('Verbindliche Leitplanke für wiederkehrende Architekturentscheidungen, typischerweise mit Begründung, Konsequenzen und Ausnahmeregel.', ['Architekturprinzip']),
'Datenführerschaft': ('Festlegung, welche Stelle bzw. welches System ein Datenobjekt oder Attribut fachlich verbindlich erzeugen und ändern darf.', ['Data Ownership', 'führendes System']),
'Source of Truth': ('Quelle, deren Daten für einen definierten fachlichen Sachverhalt als verbindlicher Referenzstand gelten.', ['SoT', 'Single Source of Truth']),
'Data Lineage': ('Nachvollziehbare Herkunft, Transformation und Weitergabe von Daten über Systeme, Schnittstellen und Verarbeitungsschritte hinweg.', ['Datenlinie', 'Datenherkunft']),
'Statusmodell': ('Explizite Definition fachlicher Zustände und erlaubter Übergänge eines Vorgangs, Dokuments oder anderen Geschäftsobjekts.', ['Zustandsmodell']),
'Applikationsportfolio': ('Gesamtsicht auf Anwendungen mit Bewertung von Fachwert, Risiko, Kritikalität, Lebenszyklus und strategischer Zielrolle.', ['Application Portfolio']),
'Schnittstellenvertrag': ('Fachlich-technischer Vertrag zwischen Provider und Consumer, der Zweck, Daten, Semantik, Fehlerverhalten, Sicherheit, Betrieb und Versionierung festlegt.', ['Interface Contract']),
'API': ('Definierte Programmierschnittstelle, über die Systeme Funktionen oder Daten kontrolliert und vertraglich beschrieben bereitstellen.', ['Application Programming Interface']),
'OpenAPI': ('Maschinenlesbare Spezifikation für HTTP-basierte APIs, mit der Endpunkte, Operationen, Datenstrukturen und technische Verträge beschrieben werden.', []),
'AsyncAPI': ('Spezifikation zur Beschreibung asynchroner, nachrichten- oder eventbasierter Schnittstellen und ihrer Channels, Messages und Schemas.', []),
'API Gateway': ('Zentraler technischer Einstiegspunkt für APIs, der unter anderem Routing, Authentifizierung, Policies, Rate Limits oder Beobachtbarkeit bündeln kann.', ['Gateway']),
'EDA': ('Event-Driven Architecture: Architekturstil, bei dem fachlich relevante Ereignisse asynchron veröffentlicht und von interessierten Konsumenten verarbeitet werden.', ['Event-Driven Architecture']),
'Event': ('Feststellung, dass etwas fachlich oder technisch bereits geschehen ist; Events werden typischerweise veröffentlicht, nicht angefordert.', ['Domain Event', 'Integration Event']),
'Command': ('Aufforderung an einen klaren Empfänger, eine bestimmte Aktion auszuführen; im Unterschied zum Event beschreibt ein Command eine gewünschte Handlung.', ['Kommando']),
'Idempotenz': ('Eigenschaft einer Verarbeitung, bei Wiederholung derselben fachlichen Operation keine unerwünschte zusätzliche Wirkung zu erzeugen.', ['Idempotent']),
'Retry': ('Kontrollierter erneuter Verarbeitungsversuch nach einem vorübergehenden Fehler, typischerweise mit Limit, Wartezeit und Fehlerstrategie.', ['Wiederholungsversuch']),
'Dead Letter Queue': ('Kontrollierte Fehlerablage für Nachrichten, die nach definierten Verarbeitungsversuchen nicht erfolgreich verarbeitet werden konnten.', ['DLQ', 'Dead-Letter-Queue']),
'Replay': ('Gezieltes erneutes Abspielen bereits gespeicherter Nachrichten oder Events, etwa zur Wiederherstellung oder Nachverarbeitung.', ['Event Replay']),
'Saga': ('Muster zur Koordination verteilter fachlicher Transaktionen über mehrere Services durch lokale Schritte und gegebenenfalls Kompensationen.', ['Saga Pattern']),
'Outbox Pattern': ('Muster, bei dem fachliche Datenänderung und zu veröffentlichende Nachricht zunächst gemeinsam lokal persistiert werden, um verlorene Events zu vermeiden.', ['Transactional Outbox', 'Outbox']),
'Eventual Consistency': ('Konsistenzmodell, bei dem verteilte Datenstände vorübergehend abweichen dürfen, sich aber bei ausbleibenden neuen Änderungen angleichen sollen.', ['eventuelle Konsistenz']),
'Authentifizierung': ('Prüfung, welche Identität hinter einem Zugriff steht.', ['Authentication', 'AuthN']),
'Autorisierung': ('Prüfung, welche Aktionen eine bereits bekannte Identität auf einer Ressource ausführen darf.', ['Authorization', 'AuthZ']),
'IAM': ('Identity and Access Management: Architektur und Prozesse für Identitäten, Authentifizierung, Berechtigungen, Rollen und deren Lebenszyklus.', ['Identity and Access Management']),
'Service Account': ('Nicht-personenbezogene technische Identität, die von Diensten, Automatisierungen oder Integrationen zur Authentifizierung genutzt wird.', ['technisches Konto', 'technische Identität']),
'Trust Boundary': ('Grenze zwischen Bereichen mit unterschiedlichem Vertrauensniveau, an der Identität, Datenfluss und Sicherheitskontrollen bewusst geprüft werden müssen.', ['Vertrauensgrenze']),
'Schutzbedarf': ('Bewertung des möglichen Schadens bei Verletzung von Vertraulichkeit, Integrität oder Verfügbarkeit einer Information oder eines Systems.', ['Schutzbedarfsfeststellung']),
'BSI': ('Bundesamt für Sicherheit in der Informationstechnik; im Projekt zentrale Referenz für Informationssicherheit und IT-Grundschutz im Behördenkontext.', ['IT-Grundschutz']),
'Security by Architecture': ('Prinzip, Sicherheitsanforderungen, Vertrauensgrenzen und Schutzmaßnahmen früh in Architekturentscheidungen einzubauen statt erst vor Go-live zu prüfen.', ['Security-by-Architecture']),
'Observability': ('Fähigkeit, internen System- und Prozesszustand aus geeigneten Signalen so abzuleiten, dass Betrieb, Fehleranalyse und fachliche Wirkung verstanden werden können.', ['Beobachtbarkeit']),
'Logs': ('Zeitlich geordnete Ereignis- und Zustandsprotokolle, die technische oder fachliche Aktivitäten nachvollziehbar machen.', ['Logging']),
'Metrics': ('Messwerte über Zeit, mit denen System-, Plattform- oder Prozesszustände quantifiziert und überwacht werden.', ['Metriken']),
'Traces': ('Verteilte Ablaufspuren, die einen Request oder Vorgang über mehrere technische Komponenten hinweg korrelieren.', ['Distributed Tracing', 'Tracing']),
'SLI': ('Service Level Indicator: konkret gemessene Kennzahl, die eine relevante Serviceeigenschaft wie Verfügbarkeit oder Latenz beschreibt.', ['Service Level Indicator']),
'SLO': ('Service Level Objective: internes Ziel für einen oder mehrere Service Level Indicators innerhalb eines definierten Zeitraums.', ['Service Level Objective']),
'SLA': ('Service Level Agreement: formale Vereinbarung über zugesicherte Servicequalitäten und gegebenenfalls Folgen bei Nichterfüllung.', ['Service Level Agreement']),
'Betriebsfähigkeit': ('Nachweisbare Fähigkeit einer Lösung, unter realen Betriebsbedingungen beobachtbar, supportbar, wiederherstellbar und verantwortet betrieben zu werden.', ['Operational Readiness']),
'RTO': ('Recovery Time Objective: angestrebte maximale Zeit bis zur Wiederherstellung eines definierten betriebsfähigen Zustands nach einer Störung.', ['Recovery Time Objective']),
'RPO': ('Recovery Point Objective: maximal tolerierbarer Datenverlust gemessen als Zeitspanne zwischen letztem wiederherstellbaren Datenstand und Störungszeitpunkt.', ['Recovery Point Objective']),
'Backup': ('Gesicherte Kopie von Daten oder Systemzuständen, die eine spätere Wiederherstellung ermöglichen soll; allein noch kein Nachweis eines erfolgreichen Wiederanlaufs.', ['Datensicherung']),
'Restore': ('Technischer Vorgang, Daten oder Systeme aus einer Sicherung wiederherzustellen.', ['Wiederherstellung']),
'CI/CD': ('Automatisierte Verfahren für Integration, Prüfung, Build, Bereitstellung und Auslieferung von Softwareänderungen.', ['Continuous Integration', 'Continuous Delivery', 'Continuous Deployment']),
'IaC': ('Infrastructure as Code: versionierte, automatisiert ausführbare Beschreibung von Infrastruktur und Plattformkonfiguration.', ['Infrastructure as Code']),
'Kubernetes': ('Orchestrierungsplattform für Container-Workloads; im EA-Kontext vor allem hinsichtlich Plattformverantwortung, Betriebsmodell, Security und Standardisierung zu bewerten.', ['K8s']),
'Microservices': ('Architekturstil aus unabhängig entwickel- und deploybaren Services mit klaren Verantwortungsgrenzen, der zusätzliche verteilte Betriebs- und Integrationskomplexität erzeugt.', ['Microservice']),
'DMS': ('Dokumentenmanagementsystem zur strukturierten Verwaltung von Dokumenten, Metadaten, Versionen und dokumentbezogenen Lebenszyklen.', ['Dokumentenmanagementsystem', 'eAkte']),
'Vergabe': ('Formalisierter Beschaffungsprozess, in dem Architekturqualität in prüfbare Anforderungen, Liefergegenstände, Nachweise und Abnahmekriterien übersetzt werden muss.', ['Ausschreibung']),
'Abnahme': ('Formale Feststellung, dass vereinbarte Liefergegenstände und Kriterien erfüllt sind; Architektur muss dafür prüfbare Nachweise und Akzeptanzkriterien liefern.', ['Architekturabnahme']),
'Dienstleister': ('Externe Organisation oder Person, die definierte Leistungen liefert; im Behördenkontext muss Architektur klare Liefergegenstände, Verantwortungen und Nachweise ermöglichen.', ['Lieferant', 'Provider']),
'Solution Architect': ('Architekturrolle mit Schwerpunkt auf einer konkreten Lösung, ihren Komponenten, Integrationen, Qualitätsanforderungen und technischen Entscheidungen.', []),
'Enterprise Architect': ('Architekturrolle mit Schwerpunkt auf organisationsweiter Kohärenz: Fähigkeiten, Daten, Anwendungen, Standards, Zielbilder, Roadmaps und Governance über Vorhaben hinweg.', ['EA']),
}


def slugify(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn').lower()
    s = re.sub(r'[^a-z0-9]+','-',s).strip('-')
    return s or 'term'

def clean_md(s):
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', s)
    s = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'[`*_>#|]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def word_pattern(names):
    names = sorted(set(n for n in names if n), key=len, reverse=True)
    # custom boundaries handle slash and hyphen aliases better than \b
    return re.compile(r'(?i)(?<![\w])(?:' + '|'.join(re.escape(n) for n in names) + r')(?![\w])')

def blocks_with_headings(text):
    lines = text.replace('\r','').split('\n')
    blocks=[]; heading=None; heading_anchor=None; heading_count=0; buf=[]
    def flush():
        nonlocal buf
        raw='\n'.join(buf).strip(); buf=[]
        if raw:
            cleaned=clean_md(raw)
            if len(cleaned)>=45:
                blocks.append({'text': cleaned, 'heading': heading, 'anchor': heading_anchor})
    for line in lines:
        hm=re.match(r'^(#{1,4})\s+(.+)$',line)
        if hm:
            flush()
            heading=clean_md(hm.group(2))
            heading_anchor=f"h-{slugify(heading)}-{heading_count}"
            heading_count+=1
            continue
        if not line.strip():
            flush(); continue
        if line.strip().startswith('```'):
            flush(); continue
        buf.append(line)
    flush()
    return blocks

mods=[]
for m in CAT['modules']:
    path=ROOT/m['path']
    if not path.exists(): continue
    txt=path.read_text(encoding='utf-8', errors='ignore')
    mods.append((m, txt, blocks_with_headings(txt)))

entries=[]
for term,(definition,aliases) in TERMS.items():
    names=[term,*aliases]
    pat=word_pattern(names)
    candidates=[]
    for m,txt,blocks in mods:
        if not pat.search(txt): continue
        for b in blocks:
            mm=pat.search(b['text'])
            if not mm: continue
            excerpt=b['text']
            # Keep the relevant part centered when the block is long.
            if len(excerpt)>420:
                pos=mm.start(); a=max(0,pos-145); z=min(len(excerpt),max(pos+265,mm.end()+110))
                # avoid cutting in the middle of words and prefer nearby sentence boundaries
                if a>0:
                    sa=max(excerpt.rfind('. ',0,a),excerpt.rfind('? ',0,a),excerpt.rfind('! ',0,a))
                    a=sa+2 if sa>=max(0,a-80) else excerpt.rfind(' ',0,a)
                    if a<0: a=0
                if z<len(excerpt):
                    ends=[x for x in (excerpt.find('. ',z),excerpt.find('? ',z),excerpt.find('! ',z)) if x!=-1]
                    z=(min(ends)+1) if ends and min(ends)<=z+90 else excerpt.find(' ',z)
                    if z<0: z=len(excerpt)
                excerpt=('… ' if a else '')+excerpt[a:z].strip()+(' …' if z<len(b['text']) else '')
            score=(20 if m.get('kind')=='project-source' else 5)
            score+=8 if term.lower() in m['title'].lower() or term.lower() in m.get('sourceTitle','').lower() else 0
            score+=4 if any(n.lower() in ' '.join(m.get('tags',[])).lower() for n in names) else 0
            score+=max(0,4-len(excerpt)//140)
            candidates.append((score,m,b,excerpt))
            break
    # choose up to 4 distinct modules, preferring project sources and different categories
    candidates.sort(key=lambda x:x[0], reverse=True)
    chosen=[]; used_cats=set()
    for item in candidates:
        score,m,b,excerpt=item
        if any(x['moduleId']==m['id'] for x in chosen): continue
        bonus=2 if m['category'] not in used_cats else 0
        chosen.append({
            'moduleId':m['id'], 'moduleTitle':m['title'], 'sourceTitle':m.get('sourceTitle',m['title']),
            'category':m['category'], 'anchor':b['anchor'], 'section':b['heading'], 'excerpt':excerpt,
            'sourceKind':m.get('kind','derived'), 'rank':score+bonus
        })
        used_cats.add(m['category'])
        if len(chosen)>=4: break
    # sort final by source-kind and rank, then keep 3
    chosen=sorted(chosen,key=lambda x:(x['sourceKind']!='project-source',-x['rank']))[:3]
    for c in chosen: c.pop('rank',None)
    if len(chosen)<2:
        # Do not promise multiple project-text examples when project material does not support it.
        coverage='limited'
    else:
        coverage='multi-source'
    entries.append({
        'id':slugify(term), 'term':term, 'aliases':aliases, 'definition':definition,
        'examples':chosen, 'coverage':coverage
    })

# longest terms first is useful for client-side auto-linking
entries.sort(key=lambda e:e['term'].lower())
out={
    'version':'2.1.0',
    'generatedAt':'2026-09-18',
    'method':'Definitions are concise syntheses of project material. Examples are extracted from distinct project modules and link back to the corresponding section.',
    'entries':entries
}
(CONTENT/'lexicon.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(f"Wrote {len(entries)} lexicon entries")
print('multi-source',sum(e['coverage']=='multi-source' for e in entries),'limited',sum(e['coverage']=='limited' for e in entries))
for e in entries:
    if e['coverage']=='limited': print('LIMITED',e['term'],len(e['examples']))
