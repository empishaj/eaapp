import json, re, textwrap
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
mods={}
for p in list((ROOT/'content/modules').glob('*.md'))+list((ROOT/'content/derived').glob('*.md')):
    mods[p.stem]=p.read_text(encoding='utf-8')
cat=json.load(open(ROOT/'content/index.json',encoding='utf-8'))
titles={m['id']:m['title'] for m in cat['modules']}
categories={m['id']:m['category'] for m in cat['modules']}

def excerpt(mid, keys, maxlen=360):
    txt=mods.get(mid,'')
    # strip table delimiter/noise, split into paragraphs
    paras=[re.sub(r'\s+',' ',p.strip()) for p in re.split(r'\n\s*\n',txt) if p.strip()]
    keys=[k.lower() for k in keys]
    best=''
    bestscore=-1
    for p in paras:
        clean=re.sub(r'^#+\s*','',p)
        if clean.startswith('|---') or len(clean)<45: continue
        score=sum(2 if k in clean.lower() else 0 for k in keys)
        score += min(len(clean),500)/500
        if score>bestscore:
            bestscore=score; best=clean
    best=re.sub(r'\|[^\n]+\|',' ',best)
    best=re.sub(r'\s+',' ',best).strip()
    return best[:maxlen].rstrip(' |')+('…' if len(best)>maxlen else '')

def src(mid, keys):
    return {'moduleId':mid,'title':titles.get(mid,mid),'category':categories.get(mid,''),'excerpt':excerpt(mid,keys)}

def unit(id,title,competency,level,minutes,sources,terms,objectives,core,distinctions,scenario,checkpoints,review):
    return {
      'id':id,'title':title,'competency':competency,'level':level,'minutes':minutes,
      'sourceModules':[s[0] for s in sources], 'terms':terms,'objectives':objectives,
      'core':core,'distinctions':distinctions,
      'scenario':scenario,
      'checkpoints':checkpoints,'reviewQuestions':review,
      'sources':[src(mid,keys) for mid,keys in sources]
    }

U=[]
U.append(unit('ea-mandat-leistungsbild','EA-Mandat und Leistungsbild in der Behörde','EA Core','Grundlage',14,
 [('eam-leistungsbild-fur-behorden',['entscheidungsinfrastruktur','leistungsbild']),('ea-rollenmodell-kern-mittel-peripherie',['Kern','Dienstleister']),('ea-kernaufgaben-12',['Mandat','Scope'])],
 ['EAM','Mandat','Governance','Stakeholder'],
 ['Ein EAM-Leistungsbild als Entscheidungsinfrastruktur erklären','Mandat, Leistung und Entscheidungsrecht auseinanderhalten','Die Rolle eines externen EA sauber begrenzen'],
 'EAM ist im Behördenkontext dann wirksam, wenn es nicht als Modellierungsstelle, sondern als dauerhafte Entscheidungsinfrastruktur verstanden wird. Ein externer EA schafft Transparenz, strukturiert Optionen, macht Risiken sichtbar und bereitet Entscheidungen vor; die hoheitliche und organisatorische Entscheidung bleibt bei der Behörde.',
 [{'title':'Leistung vs. Entscheidung','text':'Der EA liefert Analyse, Zielbilder, Optionen, Reviews und Roadmaps. Entscheidungshoheit und Linienverantwortung verbleiben bei den zuständigen Behördenrollen.'},{'title':'Artefakt vs. Nutzen','text':'Capability Map, Datenlandkarte oder ADR sind kein Selbstzweck. Ihr Wert entsteht, wenn sie eine Entscheidung, Verantwortung oder Umsetzung klären.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein Fachreferat erwartet, dass du als externer EA die Zielarchitektur „freigibst“. Wie formulierst du deine Rolle?','answer':'Du bereitest die Architekturentscheidung belastbar vor, dokumentierst Optionen, Risiken und Konsequenzen und moderierst die Abstimmung. Die Freigabe erfolgt durch die zuständige interne Entscheidungsinstanz.'},
 [('Was ist der Kernnutzen von EAM?','Bessere, nachvollziehbare und bereichsübergreifend konsistente Architekturentscheidungen.'),('Warum braucht ein externer EA einen klaren Scope?','Damit Liefergegenstände, Entscheidungsspielräume, Verantwortungen und Nicht-Scope transparent bleiben.'),('Wann ist ein Architekturartefakt sinnvoll?','Wenn es eine Entscheidung vorbereitet, ein Risiko sichtbar macht, Verantwortung klärt oder Umsetzung steuert.')],
 ['Wer entscheidet tatsächlich?','Welche konkrete Behördenentscheidung soll durch EAM besser werden?','Welche Artefakte sind verbindlich und wer pflegt sie?']))

U.append(unit('togaf-mandatslogik','TOGAF ADM als Mandatslogik','EA Core','Grundlage',16,
 [('togaf-adm-im-behordenkontext',['ADM','Mandatslogik']),('roadmap-mit-ubergangsarchitekturen',['Transition Architecture','Roadmap'])],
 ['TOGAF','ADM','Baseline','Target','Gap','Transition Architecture'],
 ['Die ADM als iterative Klärungslogik erklären','Business, Data, Application und Technology sauber unterscheiden','Von Ist/Soll zu Gap, Option und Roadmap ableiten'],
 'TOGAF liefert eine geordnete Klärungsfolge: Mandat und Vision, fachliche Fähigkeiten, Daten, Anwendungen, Technologie, Optionen, Migration, Governance und Veränderung. Requirements Management verbindet die Phasen. Im Behördenmandat wird diese Logik in verständliche Entscheidungssprache übersetzt.',
 [{'title':'ADM ist kein Wasserfall','text':'Erkenntnisse aus späteren Phasen können frühere Annahmen verändern. Rückkopplung ist normal und gewollt.'},{'title':'Technologie folgt Kontext','text':'Eine Technology Architecture ist ohne geklärte fachliche Ziele, Daten- und Anwendungszusammenhänge nur eine technische Wunschgrafik.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Eine Behörde verlangt sofort eine Kubernetes-Zielarchitektur. Was klärst du zuerst?','answer':'Fachlichen Treiber, Scope, betroffene Fähigkeiten, Daten, Anwendungen, Qualitätsanforderungen, Sicherheits- und Betriebsconstraints. Erst danach wird die Technologiearchitektur belastbar.'},
 [('Was ist ein Gap?','Eine präzise Veränderungslücke zwischen Baseline und Target Architecture.'),('Warum läuft Requirements Management quer durch die ADM?','Weil Anforderungen, Constraints, Risiken und Entscheidungen in allen Phasen entstehen und rückgekoppelt werden.'),('Was ist eine Transition Architecture?','Ein bewusst gestalteter, zeitlich begrenzter Zwischenzustand zwischen Ist und Ziel.')],
 ['Welche Entscheidung ermöglicht die aktuelle ADM-Phase?','Welche Annahmen müssen rückgekoppelt werden?','Welche Übergangszustände sind betrieblich beherrschbar?']))

U.append(unit('capability-denken','Capability statt Systemdenken','Business','Grundlage',14,
 [('capability-mapping-bundesbehorden',['Fähigkeit','Prozess','Anwendung']),('archimate-fur-behorden-ea',['Capability','Strategy View'])],
 ['Capability','Prozess','Anwendung','Organisationseinheit'],
 ['Capability, Prozess, Organisation und Anwendung trennen','Capabilities als stabile Sprache verwenden','Capabilities mit Daten, Anwendungen, Risiken und Roadmap verbinden'],
 'Eine Capability beschreibt, was eine Behörde dauerhaft können muss. Ein Prozess beschreibt, wie es abläuft; eine Organisationseinheit, wer zuständig ist; eine Anwendung, womit technisch unterstützt wird. Diese Trennung schützt die Architektur vor historisch gewachsenen System- und Referatsnamen.',
 [{'title':'Capability','text':'Relativ stabile fachliche Befähigung, z. B. „Identität prüfen“ oder „Akte führen“.'},{'title':'Prozess','text':'Konkreter Ablauf mit Reihenfolge, Rollen, Ereignissen und Entscheidungen.'},{'title':'Anwendung','text':'Technische Unterstützung einer oder mehrerer Fähigkeiten; nicht die Fähigkeit selbst.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein Projekt heißt „DMS-Modernisierung“. Wie formulierst du die Architekturfrage capability-orientiert?','answer':'Welche fachlichen Fähigkeiten rund um Akten-, Dokument- und Nachweisführung sollen verbessert werden, welche Daten und Prozesse sind betroffen und welche Systemrolle soll das DMS künftig übernehmen?'},
 [('Warum sollte EA bei Fähigkeiten beginnen?','Weil Fähigkeiten stabiler als Systeme, Projekte und Organisationseinheiten sind und fachliche Wirkung beschreiben.'),('Ist „Referat 42“ eine Capability?','Nein. Es ist eine Organisationseinheit.'),('Kann eine Anwendung mehrere Capabilities unterstützen?','Ja. Anwendungen werden Fähigkeiten zugeordnet, sind aber nicht mit ihnen gleichzusetzen.')],
 ['Ist die Capability fachlich und stabil formuliert?','Welche Daten und Systeme unterstützen sie?','Welches Risiko entsteht, wenn die Capability ausfällt?']))

U.append(unit('bpmn-verantwortung-uebergabe','BPMN: Verantwortung, Übergaben und Medienbrüche','Business','Anwendung',17,
 [('bpmn-fur-verwaltungsprozesse',['Pools','Lanes','Nachrichtenflüsse']),('dmn-entscheidungslogik-und-bpmn',['BPMN','Entscheidungslogik'])],
 ['BPMN','Pool','Lane','Sequenzfluss','Nachrichtenfluss','Gateway'],
 ['Modellzweck vor Modellierung klären','Pools/Lanes und Nachrichtenflüsse korrekt einsetzen','Wartezeiten, Fristen und Medienbrüche sichtbar machen'],
 'BPMN ist im Behördenkontext eine Präzisionssprache für Ablauf, Verantwortung und Übergabe. Pools modellieren eigenständige Beteiligte, Lanes Verantwortlichkeiten innerhalb eines Pools. Sequenzflüsse bleiben innerhalb eines Pools; Nachrichtenflüsse verbinden Beteiligte. Ein BPMN-Modell ist nicht automatisch ausführbare Prozessautomation.',
 [{'title':'Fachprozess vs. Automation','text':'Ein fachliches BPMN-Modell kann Verständnis und Abstimmung schaffen, ohne technisch ausführbar zu sein.'},{'title':'Gateway vs. Fachregel','text':'Gateways zeigen Verzweigungen im Ablauf; komplexe Entscheidungslogik sollte bei Bedarf in DMN ausgelagert werden.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein Nachweis wird per E-Mail von einer Außenstelle an ein Fachreferat geschickt und anschließend manuell im DMS abgelegt. Was muss dein BPMN-Modell sichtbar machen?','answer':'Die beteiligten Pools/Lanes, den Nachrichtenfluss, die manuelle Übergabe, Warte- bzw. Bearbeitungszustände und den Medienbruch zur DMS-Ablage.'},
 [('Was ist der Unterschied zwischen Sequenz- und Nachrichtenfluss?','Sequenzfluss verbindet Aktivitäten innerhalb eines Pools; Nachrichtenfluss verbindet eigenständige Beteiligte/Pools.'),('Warum sind Wartezeiten architekturrelevant?','Weil Fristen, Rückmeldungen, Wiedervorlagen und Eskalationen die tatsächliche Prozess- und Betriebsfähigkeit bestimmen.'),('Warum ist BPMN nicht automatisch Automation?','Weil Fachprozessmodelle zunächst fachliche Abläufe beschreiben; technische Ausführbarkeit erfordert zusätzliche Präzision und Plattformbezug.')],
 ['Was ist der Modellzweck?','Wo wechselt Verantwortung?','Wo warten Vorgänge oder werden Informationen manuell übertragen?']))

U.append(unit('dmn-fachregeln','DMN: Fachregeln aus Prozess und Code lösen','Business','Anwendung',16,
 [('dmn-entscheidungslogik-und-bpmn',['Prozesslogik','Entscheidungslogik']),('bpmn-fur-verwaltungsprozesse',['Gateway','Entscheidung'])],
 ['DMN','Decision Table','DRD','BPMN'],
 ['Prozess- und Entscheidungslogik trennen','Entscheidungstabellen strukturiert lesen','BPMN und DMN sinnvoll koppeln'],
 'DMN beschreibt Entscheidungslogik, während BPMN den Ablauf beschreibt. Fachregeln sollen nicht unkontrolliert in Code, Excel oder Einzelwissen verschwinden. Entscheidungen wie Fristlage, Nachweispflicht oder Risikoklasse können als explizite Entscheidungslogik modelliert und aus Prozessen aufgerufen werden.',
 [{'title':'BPMN','text':'Wann passiert etwas und wer ist beteiligt?'},{'title':'DMN','text':'Nach welchen Regeln wird entschieden?'},{'title':'Decision Requirements Diagram','text':'Zeigt, welche Entscheidungen und Eingangsdaten voneinander abhängen.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein Gateway im BPMN enthält fünf verschachtelte Bedingungen für Nachweispflichten. Was ist die bessere Modellierungsstrategie?','answer':'Die fachliche Entscheidungslogik in DMN auslagern und im BPMN nur den Entscheidungspunkt bzw. das Ergebnis verwenden.'},
 [('Warum DMN statt komplexer Gateway-Bedingungen?','Weil Fachregeln eigenständig, nachvollziehbar und änderbar bleiben.'),('Was ist der Kernunterschied BPMN/DMN?','BPMN modelliert Ablauf; DMN modelliert Entscheidungslogik.'),('Was sollte eine Entscheidungstabelle sichtbar machen?','Eingaben, Regeln/Bedingungen und resultierende Entscheidungsausgaben.')],
 ['Welche Regel ändert sich häufiger als der Prozess?','Wer ist fachlicher Owner der Regel?','Ist die Entscheidungslogik prüf- und versionierbar?']))

U.append(unit('datenfuehrerschaft-landkarte','Datenführerschaft mit Datenlandkarten klären','Data','Anwendung',18,
 [('datenlandkarten-fur-behorden',['führendes System','Data Owner','CRUD']),('togaf-adm-im-behordenkontext',['Data Architecture','führende Systeme'])],
 ['Datenführerschaft','Data Owner','CRUD','Datenlandkarte','System of Record'],
 ['Datenobjekte fachlich definieren','Führende Quelle und Änderungsrechte klären','Datenflüsse, Schutzbedarf und Lebenszyklus verbinden'],
 'Eine Datenlandkarte zeigt nicht nur, wo Daten gespeichert sind, sondern wer sie erzeugt, ändert, liest, weitergibt und archiviert. Die zentrale EA-Frage lautet: Wer darf ein Datum fachlich verbindlich ändern? Unklare Datenführerschaft erzeugt Doppelpflege, widersprüchliche Auskünfte und riskante Korrekturen.',
 [{'title':'Data Owner vs. System','text':'Der fachliche Owner verantwortet Bedeutung und Regeln; das führende System ist die technische Quelle für den verbindlichen Zustand.'},{'title':'Kopie vs. Führerschaft','text':'Ein System darf Daten kennen, ohne sie fachlich führen zu dürfen.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Fachverfahren, DMS und Reporting enthalten jeweils einen „Vorgangsstatus“. Was prüfst du zuerst?','answer':'Fachliche Definition und Zustandsmodell, wer den Status ändern darf, welches System führend ist, wie Kopien aktualisiert werden und wie Konflikte behandelt werden.'},
 [('Welche Frage deckt ungeklärte Datenführerschaft schnell auf?','Wer darf dieses Datum fachlich verbindlich ändern?'),('Warum reicht eine Speicherortliste nicht?','Weil Verantwortung, Flüsse, Änderungsrechte, Schutzbedarf und Lebenszyklus fehlen.'),('Darf ein Reporting-System Daten kopieren?','Ja, sofern Führerschaft, Aktualisierung, Zweck und Konfliktregeln geklärt sind.')],
 ['Was ist das fachliche Datenobjekt?','Wer ist Owner und wer darf schreiben?','Wo entstehen Kopien und wie bleiben sie konsistent?']))

U.append(unit('applikationsportfolio-steuern','Applikationsportfolio: Wert, Risiko und Zielrolle','Transformation','Anwendung',17,
 [('applikationsportfolio-bewerten',['fachlicher Wert','Risiko','Portfolio']),('roadmap-mit-ubergangsarchitekturen',['Work Package','Roadmap'])],
 ['Applikationsportfolio','fachlicher Wert','technisches Risiko','Zielrolle'],
 ['Anwendungen nicht nur inventarisieren, sondern bewerten','Fachwert und Risiko getrennt betrachten','Aus Portfolioergebnissen Roadmap-Entscheidungen ableiten'],
 'Applikationsportfolio ist Architektursteuerung, nicht Inventur. Anwendungen werden nach fachlichem Wert, Risiko, Kritikalität, Anschlussfähigkeit und strategischer Passung bewertet. Eine rote Anwendung wird nicht automatisch sofort abgelöst; die Entscheidung hängt von Abhängigkeiten, Übergangsfähigkeit und Transformationspfad ab.',
 [{'title':'Wert','text':'Welche fachlichen Fähigkeiten und kritischen Leistungen werden unterstützt?'},{'title':'Risiko','text':'Wie hoch sind technische, betriebliche, Sicherheits- oder Lifecycle-Risiken?'},{'title':'Zielrolle','text':'Beibehalten, modernisieren, konsolidieren, ablösen oder als Übergangslösung tolerieren – jeweils begründet.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein Legacy-System ist technisch kritisch, unterstützt aber eine zentrale Verwaltungsleistung ohne kurzfristige Alternative. Was folgt daraus?','answer':'Nicht automatische Ablösung, sondern Risikoabsicherung, Zielrolle, Übergangsarchitektur, Abhängigkeiten und ein belastbarer Ablösepfad.'},
 [('Warum ist ein Portfolio mehr als Inventur?','Weil es Anwendungen anhand fachlichem Wert, Risiko und strategischer Zielrolle steuerbar macht.'),('Warum wird eine rote Anwendung nicht automatisch abgeschaltet?','Weil fachliche Kritikalität, Abhängigkeiten und Übergangsfähigkeit berücksichtigt werden müssen.'),('Was verbindet Portfolio und Roadmap?','Bewertete Handlungsbedarfe werden in priorisierte Work Packages und Übergangsschritte übersetzt.')],
 ['Welche Capability hängt von der Anwendung ab?','Welche Risiken sind aktuell tragbar?','Welche Zielrolle ist realistisch und bis wann?']))

U.append(unit('adr-entscheidungsqualitaet','ADR: Entscheidungen nachvollziehbar machen','Governance','Anwendung',16,
 [('adr-erstellung-und-praxis',['ADR','Kontext','Alternativen']),('architektur-governance-fur-behorden',['ADR','Entscheidung'])],
 ['ADR','Decision Driver','Konsequenz','Superseded'],
 ['ADR von Konzept und Protokoll unterscheiden','Kontext, Alternativen und Konsequenzen dokumentieren','ADRs in Governance und Lebenszyklus einbetten'],
 'Ein ADR dokumentiert eine konkrete Architekturentscheidung mit Kontext, Treibern, betrachteten Alternativen, Entscheidung und Konsequenzen. Es ist kein vollständiges Architekturkonzept und kein Sitzungsprotokoll. Gute ADRs machen spätere Nachvollziehbarkeit und kontrollierte Ablösung alter Entscheidungen möglich.',
 [{'title':'ADR vs. Protokoll','text':'Ein Protokoll dokumentiert Gespräch und Beschlussverlauf; ein ADR fokussiert die Architekturentscheidung und ihre Gründe.'},{'title':'ADR vs. Architekturkonzept','text':'Das Konzept beschreibt die Lösung umfassender; der ADR hält eine wesentliche Entscheidung kompakt und dauerhaft nachvollziehbar fest.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein Projekt entscheidet „Kafka einsetzen“, dokumentiert aber keine Alternativen oder Konsequenzen. Was fehlt?','answer':'Entscheidungskontext, fachliche und technische Treiber, realistische Alternativen, Konsequenzen, Risiken, Gültigkeitsbereich und ggf. Review-/Ablösebedingungen.'},
 [('Wann lohnt sich ein ADR?','Bei architekturrelevanten Entscheidungen mit längerfristigen, bereichsübergreifenden oder schwer reversiblen Auswirkungen.'),('Warum gehören Alternativen hinein?','Damit sichtbar wird, dass die Entscheidung gegenüber realistischen Optionen abgewogen wurde.'),('Was bedeutet „superseded“?','Eine frühere Entscheidung bleibt historisch nachvollziehbar, wurde aber durch eine neue ADR ersetzt.')],
 ['Was ist die konkrete Entscheidungsfrage?','Welche realistischen Alternativen wurden betrachtet?','Welche Konsequenzen und Folgepflichten entstehen?']))

U.append(unit('archimate-sichten','ArchiMate: Sichten für Entscheidungen statt Vollmodell','Modeling','Anwendung',17,
 [('archimate-fur-behorden-ea',['View','Capability','Application']),('capability-mapping-bundesbehorden',['Capability','Anwendung'])],
 ['ArchiMate','View','Viewpoint','Capability','Application Component'],
 ['ArchiMate als Architektur-Grammatik verwenden','Sichten an Stakeholderfragen ausrichten','Capability-to-Technology-Zusammenhänge zeigen'],
 'ArchiMate hilft, Beziehungen zwischen Motivation, Fähigkeiten, Business, Anwendungen, Daten, Technologie sowie Umsetzung sichtbar zu machen. Das Ziel ist nicht, alles in eine Grafik zu pressen, sondern eine konkrete Frage mit einer passenden Sicht zu beantworten.',
 [{'title':'Modell vs. View','text':'Das Modell kann viele Elemente enthalten; eine View zeigt nur den für eine Fragestellung relevanten Ausschnitt.'},{'title':'Capability-to-Technology','text':'Eine starke EA-Sicht verbindet fachliche Fähigkeit über Anwendungen und Services mit der tragenden Technologie.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Die Leitung will wissen, welche kritischen Fähigkeiten von einer auslaufenden Plattform abhängen. Welche Sicht baust du?','answer':'Eine fokussierte Capability-to-Application-to-Technology-Sicht mit betroffenen Fähigkeiten, Anwendungen, Technologiekomponenten und relevanten Risiken.'},
 [('Warum ist „alles zeigen“ eine schlechte ArchiMate-Praxis?','Weil die Sicht unlesbar wird und keine konkrete Entscheidung mehr unterstützt.'),('Was ist eine View?','Ein zielgruppen- und fragestellungsbezogener Ausschnitt aus dem Architekturmodell.'),('Warum Capabilities in ArchiMate nutzen?','Sie verbinden strategische/fachliche Bedürfnisse mit späteren Business-, Application- und Technology-Sichten.')],
 ['Welche Frage soll die Sicht beantworten?','Wer ist die Zielgruppe?','Welche Beziehungen müssen sichtbar sein – und welche nicht?']))

U.append(unit('arc42-solution-dokumentation','arc42 richtig in EA einordnen','Modeling','Anwendung',15,
 [('arc42-in-behorden-anwenden',['arc42','Kontextabgrenzung','Qualitätsziele']),('ea-rollenmodell-kern-mittel-peripherie',['Solution Architect','Software Architect'])],
 ['arc42','Systemkontext','Qualitätsziel','Bausteinsicht'],
 ['arc42 als Kommunikationsstruktur für Lösungsarchitektur verstehen','EA- und Solution-Architektur sauber abgrenzen','arc42-Artefakte in Reviews gezielt nutzen'],
 'arc42 strukturiert die Dokumentation einer konkreten Software-/Lösungsarchitektur: Ziele, Randbedingungen, Kontext, Bausteine, Laufzeit, Verteilung, Querschnittskonzepte, Entscheidungen, Qualität und Risiken. Als EA nutzt du diese Informationen für Reviews und Einordnung, ohne jede Detaildokumentation selbst zu besitzen.',
 [{'title':'EA-Perspektive','text':'Domänen, Zielrollen, Standards, Datenführerschaft, Integrationsprinzipien, Roadmap und Governance.'},{'title':'arc42-Perspektive','text':'Konkrete System-/Solution-Architektur mit Kontext, Bausteinen, Laufzeit und Qualitätszielen.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein Dienstleister liefert ein 80-seitiges arc42-Dokument. Welche Teile prüfst du als EA zuerst?','answer':'Ziele und Randbedingungen, Systemkontext, relevante Schnittstellen, Architekturentscheidungen, Qualitätsanforderungen, Risiken sowie Abweichungen von Zielarchitektur und Standards.'},
 [('Was ist arc42 im Kern?','Eine strukturierte Kommunikations- und Dokumentationsform für konkrete Software-/Lösungsarchitektur.'),('Ersetzt arc42 TOGAF?','Nein. Es adressiert eine andere Ebene und kann EA-Arbeit ergänzen.'),('Warum sind Qualitätsziele wichtig?','Weil sie Architekturentscheidungen und spätere Bewertung der Lösung treiben.')],
 ['Welche EA-Vorgaben muss die Lösung erfüllen?','Welche Qualitätsziele sind architekturrelevant?','Welche Entscheidungen oder Risiken gehören in den EA-Kontext zurückgespiegelt?']))

U.append(unit('schnittstellenvertrag','Schnittstellenvertrag: fachliche Übergabe vor Technik','Integration','Anwendung',18,
 [('schnittstellenvertrag-erstellen',['fachlicher Zweck','Provider','Consumer']),('openapi-asyncapi-bewertung',['Vertrag','Schema','Fehler'])],
 ['Schnittstellenvertrag','Provider','Consumer','Versionierung','SLO'],
 ['Fachlichen Zweck vor Endpoint/Payload klären','Verantwortung, Daten, Sicherheit, Fehler und Betrieb vertraglich beschreiben','Technische Spezifikation von fachlichem Vertrag unterscheiden'],
 'Ein belastbarer Schnittstellenvertrag beantwortet nicht nur, wie eine API aufgerufen wird. Er klärt, warum der Austausch existiert, welche fachlichen Datenobjekte übertragen werden, wer Provider und Consumer verantwortet, wie Sicherheit, Fehler, Versionierung, Betrieb, Monitoring und Änderung geregelt sind.',
 [{'title':'OpenAPI ist Teil, nicht Ganzes','text':'OpenAPI kann HTTP-Operationen und Schemas beschreiben; der fachliche und organisatorische Vertrag geht darüber hinaus.'},{'title':'Fehler sind Vertrag','text':'Fehlercodes, fachliche Fehlerfälle, Wiederanlauf und Verantwortungen gehören zur Schnittstellenqualität.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein Dienstleister liefert ein vollständiges Swagger/OpenAPI-Dokument und nennt die Schnittstelle „abnahmefähig“. Was fehlt möglicherweise?','answer':'Fachlicher Zweck, Verantwortliche, Datenführerschaft, fachliche Fehler- und Quittierungslogik, Versionierung/Deprecation, Betriebs-SLOs, Support, Monitoring, Security und Abnahmekriterien.'},
 [('Warum ist ein Schnittstellenvertrag kein Swagger-File?','Weil fachliche, organisatorische, sicherheitsbezogene und betriebliche Vereinbarungen über die technische API-Beschreibung hinausgehen.'),('Welche Rollen müssen klar sein?','Mindestens Provider, Consumer und organisatorische Verantwortliche/Eskalationswege.'),('Warum gehört Versionierung in den Vertrag?','Damit Änderungen und Kompatibilität kontrolliert und nachvollziehbar bleiben.')],
 ['Was ist das fachliche Ergebnis des Austauschs?','Wer ist verantwortlich, wenn die Übergabe scheitert?','Wie wird Änderung und Abkündigung geregelt?']))

U.append(unit('openapi-asyncapi','OpenAPI und AsyncAPI richtig einordnen','Integration','Anwendung',18,
 [('openapi-asyncapi-bewertung',['OpenAPI','AsyncAPI','Idempotenz']),('eda-im-behordenkontext',['Event','Nachricht'])],
 ['OpenAPI','AsyncAPI','REST','Event','Idempotenz','Schema'],
 ['HTTP- und nachrichtengetriebene Verträge unterscheiden','HTTP-Semantik und Schemas als Vertragsbestandteil verstehen','Idempotenz und Kompatibilität als Architekturthemen erkennen'],
 'OpenAPI beschreibt HTTP-basierte Schnittstellen, AsyncAPI nachrichtengetriebene Kommunikation. Entscheidend ist nicht das Format selbst, sondern die fachliche Semantik: Anfrage, Befehl, Ereignis oder Nachricht. Schemas, Fehlerverhalten, AuthN/AuthZ, Versionierung und Kompatibilität gehören zur Architekturqualität.',
 [{'title':'Synchron','text':'Der Consumer wartet typischerweise auf eine direkte Antwort und trägt eine Laufzeitabhängigkeit.'},{'title':'Asynchron','text':'Zeitliche Entkopplung reduziert direkte Laufzeitabhängigkeit, verschiebt aber Verantwortung in Zustellung, Wiederholung, Reihenfolge und Fehlerbehandlung.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Eine Fachanwendung muss eine sofortige Registerauskunft anzeigen; ein anderes System soll nur informiert werden, dass ein Vorgang abgeschlossen wurde. Welche Integrationsarten liegen nahe?','answer':'Für die unmittelbare Auskunft eine synchrone HTTP/API-Interaktion; für die reine Ereignisinformation eine asynchrone Event-Kommunikation – jeweils nach fachlichen und betrieblichen Constraints zu prüfen.'},
 [('Was beschreibt OpenAPI primär?','HTTP-basierte APIs mit Operationen, Parametern, Schemas und weiteren Vertragsdetails.'),('Was beschreibt AsyncAPI primär?','Nachrichtengetriebene/asynchrone Schnittstellen und ihre Kanäle, Nachrichten und Schemas.'),('Warum ist Idempotenz wichtig?','Damit Wiederholung einer Operation oder Nachricht nicht ungewollt doppelte fachliche Wirkung erzeugt.')],
 ['Ist die Interaktion fachlich Anfrage, Befehl oder Ereignis?','Welche Konsistenz- und Zeitabhängigkeit ist akzeptabel?','Wie werden Wiederholung, Fehler und Schemaänderungen behandelt?']))

U.append(unit('eda-kopplungsmodell','EDA: Ereignisse als Kopplungsmodell','Integration','Vertiefung',19,
 [('eda-im-behordenkontext',['Event','Kopplung','Event Storming']),('openapi-asyncapi-bewertung',['AsyncAPI','Nachricht']),('dead-letter-queue',['DLQ','Retry'])],
 ['EDA','Domain Event','Integration Event','Eventual Consistency','Replay'],
 ['Events von Commands und Notifications unterscheiden','Zeitliche Entkopplung samt Folgen verstehen','Fehler-, Wiederholungs- und Zustellstrategie mitdenken'],
 'Event-Driven Architecture ist kein Techniktrick, sondern ein Kopplungsmodell. Systeme reagieren auf fachlich bedeutsame Ereignisse. Asynchronität entkoppelt Zeit, aber nicht Verantwortung: Zustellung, Duplikate, Reihenfolge, Wiederholung, Fehlerbehandlung und fachliche Konsistenz müssen explizit entworfen werden.',
 [{'title':'Ereignis','text':'Beschreibt etwas, das fachlich bereits geschehen ist.'},{'title':'Command','text':'Fordert eine Aktion an; Erfolg ist noch nicht eingetreten.'},{'title':'Notification','text':'Kann nur auf Veränderung hinweisen, ohne vollständigen Zustand mitzugeben.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein System publiziert „Vorgang abgeschlossen“. Drei Consumer reagieren. Welche EA-Fragen stellst du?','answer':'Fachliche Bedeutung und Schema, Owner, Zustellgarantie, Reihenfolge, Duplikate/Idempotenz, Retry/DLQ, Replay, Datenschutz, Monitoring und Auswirkungen bei verzögerten Consumer-Verarbeitungen.'},
 [('Warum entkoppelt Asynchronität Verantwortung nicht?','Weil weiterhin geklärt sein muss, wer Zustellung, Fehler, fachliche Wirkung und Nachbearbeitung verantwortet.'),('Was unterscheidet Event und Command?','Ein Event beschreibt etwas Geschehenes; ein Command fordert eine Handlung an.'),('Welche Fehlerstrategie braucht EDA?','Explizite Regeln für Retry, Duplikate/Idempotenz, Poison Messages, ggf. DLQ/Replay und Monitoring.')],
 ['Ist das Ereignis fachlich eindeutig benannt?','Was passiert bei doppelter oder verspäteter Zustellung?','Wie wird ein fachlicher Rückstand sichtbar?']))

U.append(unit('dlq-retry-idempotenz','DLQ, Retry und Idempotenz zusammen denken','Integration','Vertiefung',16,
 [('dead-letter-queue',['Dead Letter Queue','Retry','Idempotenz']),('openapi-asyncapi-bewertung',['Idempotenz']),('eda-im-behordenkontext',['Retry','Fehler'])],
 ['Dead Letter Queue','Retry','Idempotenz','Replay','Poison Message'],
 ['Temporäre und dauerhafte Fehler unterscheiden','Retry begrenzen und Fehler kontrolliert parken','Wiederholung gegen doppelte Wirkung absichern'],
 'Eine DLQ ist eine kontrollierte Fehlerablage für Nachrichten, die nach definierten Verarbeitungsversuchen nicht erfolgreich verarbeitet werden konnten. Sie ersetzt keinen Betriebsprozess. Retry ist bei temporären Fehlern sinnvoll; bei strukturellen oder fachlichen Fehlern kann endlose Wiederholung schädlich sein. Idempotenz schützt vor doppelter fachlicher Wirkung.',
 [{'title':'Retry','text':'Erneuter Verarbeitungsversuch bei potenziell temporären Fehlern.'},{'title':'DLQ','text':'Kontrollierte Ablage nach definiertem Scheitern, inklusive Analyse- und Nachbearbeitungsprozess.'},{'title':'Idempotenz','text':'Mehrfache Verarbeitung führt nicht mehrfach zur gleichen fachlichen Wirkung.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Eine Dokumentübergabe wurde erfolgreich verarbeitet, die Bestätigung ging aber verloren. Ein Retry erfolgt. Welches Risiko besteht?','answer':'Doppelte fachliche Wirkung, z. B. doppelte Dokumentanlage. Consumer bzw. Operation müssen deshalb eine Idempotenz- oder Deduplizierungsstrategie besitzen.'},
 [('Wann ist Retry sinnvoll?','Vor allem bei temporären technischen Fehlern, wenn Wiederholung fachlich sicher ist.'),('Was löst eine DLQ nicht automatisch?','Ursache, Ownership, Nachbearbeitung, Datenschutz, Replay- und Betriebsprozess.'),('Warum ist Idempotenz bei Replay wichtig?','Damit erneut eingespielte Nachrichten keine unerwünschten Doppelwirkungen erzeugen.')],
 ['Welche Fehler sind retrybar?','Wer besitzt die DLQ und wie schnell wird sie bearbeitet?','Wie wird doppelte Verarbeitung verhindert?']))

U.append(unit('iam-authn-authz','IAM: Identität, Authentifizierung und Autorisierung','Security','Anwendung',18,
 [('iam-architektur-fur-behorden',['Authentifizierung','Autorisierung','RBAC']),('security-by-architecture-review-anleitung',['IAM','Rollen'])],
 ['IAM','Authentifizierung','Autorisierung','RBAC','ABAC','PAM'],
 ['Login und Berechtigung trennen','RBAC/ABAC kontextbezogen einordnen','Technische Konten und privilegierte Rechte mitprüfen'],
 'IAM ist kein Login-Thema, sondern Architektur. Authentifizierung klärt, wer eine Identität ist; Autorisierung, was diese Identität tun darf. Fachliche Rollenmodelle, technische Konten, privilegierte Zugriffe, Rezertifizierung und Nachvollziehbarkeit gehören zur Gesamtarchitektur.',
 [{'title':'Authentifizierung','text':'Nachweis einer Identität.'},{'title':'Autorisierung','text':'Entscheidung, welche Handlung/Ressource erlaubt ist.'},{'title':'Fachliche Berechtigung','text':'Übersetzt Aufgaben und Verantwortungen in konkrete erlaubte Fachhandlungen.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein Benutzer kann sich über SSO erfolgreich anmelden, darf danach aber alle Vorgänge sehen. Welcher Denkfehler liegt vor?','answer':'Authentifizierung wurde mit Autorisierung verwechselt. SSO bestätigt die Identität; fachliche und technische Berechtigungen müssen separat modelliert und durchgesetzt werden.'},
 [('Warum ist Login nicht Berechtigung?','Weil Identitätsnachweis und erlaubte Handlungen unterschiedliche Architekturfragen sind.'),('Was ist PAM?','Steuerung und Absicherung privilegierter administrativer Zugriffe.'),('Warum sind technische Konten kritisch?','Sie besitzen oft weitreichende Rechte, laufen dauerhaft und brauchen Owner, Zweck, Rotation und Nachvollziehbarkeit.')],
 ['Welche Identitäten gibt es – Menschen und Maschinen?','Wie werden fachliche Rollen in technische Rechte übersetzt?','Wie werden privilegierte Rechte rezertifiziert und protokolliert?']))

U.append(unit('schutzbedarf-architektur','Schutzbedarf in Architekturentscheidungen übersetzen','Security','Anwendung',17,
 [('schutzbedarf-einordnen-bsi',['Vertraulichkeit','Integrität','Verfügbarkeit']),('security-by-architecture-review-anleitung',['Schutzbedarf','Trust'])],
 ['Schutzbedarf','Vertraulichkeit','Integrität','Verfügbarkeit'],
 ['Die drei BSI-Grundwerte unterscheiden','Schutzbedarf nicht nur dokumentieren, sondern in Architekturmaßnahmen übersetzen','Schäden fachlich begründen'],
 'Schutzbedarf bewertet, welche Schäden bei Verlust von Vertraulichkeit, Integrität oder Verfügbarkeit entstehen können. Für EA ist die Einstufung kein Formularende: Sie beeinflusst IAM, Netzsegmentierung, Verschlüsselung, Logging, Backup/Wiederanlauf, Monitoring und Dienstleisterzugriff.',
 [{'title':'Vertraulichkeit','text':'Informationen dürfen nur berechtigten Stellen zugänglich sein.'},{'title':'Integrität','text':'Daten und Funktionen müssen korrekt und unverfälscht sein.'},{'title':'Verfügbarkeit','text':'Informationen und Funktionen müssen im erforderlichen Zeitraum nutzbar sein.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein System verarbeitet sensible Personendaten, hat aber nur lokale Admin-Konten und unverschlüsselte Exporte. Wie nutzt du Schutzbedarf im Review?','answer':'Du leitest aus dem fachlich begründeten Schutzbedarf konkrete Anforderungen an Zugriff, Verschlüsselung, Nachvollziehbarkeit und Datenflüsse ab und lässt Abweichungen als Risiko behandeln.'},
 [('Welche drei Grundwerte betrachtet die Schutzbedarfslogik?','Vertraulichkeit, Integrität und Verfügbarkeit.'),('Warum ist Schutzbedarf architekturrelevant?','Weil er technische und organisatorische Schutzmaßnahmen und Qualitätsanforderungen beeinflusst.'),('Wer sollte Schutzbedarf fachlich begründen?','Die zuständigen fachlichen und sicherheitsbezogenen Rollen; der EA integriert die Auswirkungen in Architekturentscheidungen.')],
 ['Welcher Schaden entsteht bei Verletzung jedes Grundwerts?','Welche Architekturmaßnahmen folgen daraus?','Welche Abhängigkeiten übertragen den Schutzbedarf weiter?']))

U.append(unit('security-review','Security-by-Architecture-Review durchführen','Security','Vertiefung',20,
 [('security-by-architecture-review-anleitung',['Prüfachsen','Review','Befund']),('schutzbedarf-einordnen-bsi',['Schutzbedarf']),('iam-architektur-fur-behorden',['IAM'])],
 ['Security-by-Architecture','Trust Boundary','Threat','Befund'],
 ['Security früh als Architekturmaterial behandeln','Systemkontext, Datenflüsse und Vertrauensgrenzen systematisch prüfen','Befunde entscheidungsfähig formulieren'],
 'Ein Security-by-Architecture-Review prüft nicht nur einzelne Controls, sondern den Zusammenhang aus Schutzbedarf, Systemkontext, Datenflüssen, Trust Boundaries, IAM, APIs, Registern, DMS, Logging, Plattform, Backup, Lieferkette, Dienstleistern und Datenschutz. Befunde müssen Ursache, Wirkung, Risiko und Maßnahme verbinden.',
 [{'title':'Review statt Checkliste abhaken','text':'Die Prüfachsen strukturieren die Analyse; entscheidend sind Beziehungen und konkrete Risiken im betrachteten System.'},{'title':'Befund','text':'Ein guter Befund beschreibt Kontext, Schwachstelle/Abweichung, mögliche Wirkung, Priorität und konkrete Maßnahme.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein Antragsportal nutzt externen Dienstleisterbetrieb, zentrale IAM-Anmeldung und mehrere Register. Welche drei Sichten sind für den Security-Review zuerst zentral?','answer':'System-/Trust-Boundary-Kontext, Datenflüsse samt Schutzbedarf sowie Identitäts-/Berechtigungs- und Dienstleisterzugriffe; anschließend Logging, Plattform, Wiederanlauf und Lieferkette.'},
 [('Warum gehört Security früh in Architektur?','Weil Schutzbedarf, Trust Boundaries, IAM und Betriebsanforderungen grundlegende Strukturentscheidungen beeinflussen.'),('Was ist eine Trust Boundary?','Eine Grenze, an der sich Vertrauensannahmen, Verantwortungen oder Sicherheitskontexte ändern.'),('Wie wird ein Befund entscheidungsfähig?','Durch klaren Kontext, Risiko/Wirkung, Priorisierung und umsetzbare Maßnahme.')],
 ['Wo ändern sich Vertrauenszonen?','Welche Daten passieren welche Grenzen?','Welche Security-Abweichung braucht Entscheidung oder Kompensation?']))

U.append(unit('kubernetes-plattformreview','Kubernetes als Plattformarchitektur bewerten','Platform','Vertiefung',19,
 [('kubernetes-architektur-bewerten',['Mandantentrennung','Betriebsverantwortung','Secrets']),('cd-und-iac-architektur',['Deployment','IaC']),('observability-anforderungen-definieren',['Monitoring','Logging'])],
 ['Kubernetes','Mandantentrennung','Secrets Management','Observability','Disaster Recovery'],
 ['Kubernetes nicht mit Server/Hosting verwechseln','Plattformverantwortung und Mandantentrennung prüfen','Deployment, Secrets, Observability und Wiederanlauf gemeinsam bewerten'],
 'Kubernetes ist ein Steuerungssystem für containerisierte Workloads und damit im Behördenkontext eine Plattformarchitekturfrage. Entscheidend sind Mandantentrennung, Schutzbedarf/Zonierung, Betriebsverantwortung, Patchmanagement, Backup/Restore/DR, Observability, Releaseprozesse, Rechte und Secrets.',
 [{'title':'Plattformfähigkeit','text':'Die Plattform stellt standardisierte Betriebs- und Lieferfähigkeiten bereit; sie ersetzt keine fachliche oder Anwendungsschnitt-Entscheidung.'},{'title':'Mandantentrennung','text':'Muss technisch, organisatorisch und betrieblich begründet werden – nicht nur per Namespace-Namen.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein Projekt argumentiert: „Wir gehen auf Kubernetes, dann sind Hochverfügbarkeit und Betrieb gelöst.“ Wie reagierst du?','answer':'Kubernetes kann technische Mechanismen bereitstellen, ersetzt aber keine fachlich abgeleiteten Verfügbarkeitsziele, Wiederanlaufkonzepte, Owner, Monitoring, Backup/Restore, Kapazitäts- oder Incident-Prozesse.'},
 [('Welche Dimensionen prüft ein EA bei Kubernetes?','U. a. Mandantentrennung, Schutzbedarf/Zonen, Betrieb, Patching, Backup/DR, Observability, Deployment, Rechte/Secrets.'),('Löst Kubernetes automatisch Resilienz?','Nein. Resilienz entsteht aus Architektur, Konfiguration, Betrieb und getesteten Wiederanlaufverfahren.'),('Warum ist Secrets Management zentral?','Weil Zugangsdaten/Schlüssel nicht wie normale Konfiguration behandelt und geschützt, rotiert und nachvollziehbar verwaltet werden müssen.')],
 ['Wer besitzt die Plattform und ihre SLOs?','Wie sind Mandanten und Schutzbedarfe getrennt?','Wie wird ein Ausfall praktisch wiederhergestellt?']))

U.append(unit('cicd-iac','CI/CD und IaC als kontrollierte Lieferfähigkeit','Platform','Vertiefung',18,
 [('cd-und-iac-architektur',['kontrollierte Lieferfähigkeit','IaC','Auditierbarkeit']),('architektur-governance-fur-behorden',['Quality Gates','Standards'])],
 ['CI/CD','Infrastructure as Code','GitOps','Pipeline Gate','Release-Dossier'],
 ['Lieferweg als Teil der Architektur verstehen','IaC als reproduzierbare, versionierte Infrastruktur behandeln','Pipeline-Gates und Nachweise risikobasiert gestalten'],
 'CI/CD ist aus EA-Sicht kontrollierte Lieferfähigkeit: Änderungen müssen reproduzierbar gebaut, geprüft, freigegeben, ausgeliefert und nachvollzogen werden. IaC macht Infrastruktur versionierbar und reproduzierbar. Terraform, Ansible, Helm und GitOps erfüllen unterschiedliche Rollen und dürfen nicht gedanklich vermischt werden.',
 [{'title':'CI/CD','text':'Lieferprozess mit Build, Tests, Prüfungen, Freigabe und Deployment.'},{'title':'IaC','text':'Infrastrukturzustand wird in versionierter, prüfbarer Form beschrieben und reproduzierbar erzeugt.'},{'title':'Gate','text':'Kontrollpunkt im Lieferweg; hart oder weich je nach Risiko und Policy.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein Dienstleister kann produktiv deployen, ohne dass der verwendete Build eindeutig einem Commit und Prüfnachweisen zugeordnet werden kann. Was ist das EA-Risiko?','answer':'Fehlende Reproduzierbarkeit, Auditierbarkeit und Lieferkettenvertrauen. Ein Release muss Herkunft, Artefakt, Prüfungen, Freigabe und Zielumgebung nachvollziehbar verbinden.'},
 [('Warum ist CI/CD Architekturthema?','Weil der Lieferweg Qualität, Sicherheit, Reproduzierbarkeit, Betriebsfähigkeit und Nachweisführung bestimmt.'),('Was ist der Architekturwert von IaC?','Versionierung, Reviewbarkeit, Reproduzierbarkeit und kontrollierte Änderung von Infrastruktur.'),('Warum braucht eine Pipeline Gates?','Damit relevante Qualitäts-, Security- und Compliance-Anforderungen vor Weitergabe oder Produktion geprüft werden.')],
 ['Ist jeder Build reproduzierbar und zurückverfolgbar?','Sind Secrets aus Code/Config getrennt?','Welche Nachweise muss ein Release erzeugen?']))

U.append(unit('observability','Observability: technische und fachliche Wirkung sehen','Operations','Vertiefung',18,
 [('observability-anforderungen-definieren',['Logs','Metriken','Traces','SLI']),('schnittstellenvertrag-erstellen',['Monitoring','SLO']),('rpo-betriebsfahigkeit-prufen',['Betriebsfähigkeit'])],
 ['Observability','Logs','Metrics','Traces','SLI','SLO','Error Budget'],
 ['Logs, Metriken und Traces unterscheiden','Technische Signale mit Nutzer-/Prozesswirkung verbinden','SLI/SLO als steuerbare Qualitätsziele nutzen'],
 'Observability ist Betriebsarchitektur, nicht Monitoring-Kosmetik. Logs erklären Ereignisse, Metriken zeigen Zustände/Verläufe, Traces machen End-to-End-Aufrufketten sichtbar. SLI misst, SLO setzt ein Ziel; Alerting soll Handlungsfähigkeit erzeugen statt Lärm.',
 [{'title':'Monitoring','text':'Überwacht bekannte Signale und Zustände.'},{'title':'Observability','text':'Ermöglicht, aus Telemetrie den internen Zustand und Fehlerketten eines Systems zu verstehen.'},{'title':'Fachliche Sicht','text':'Technisch „grün“ reicht nicht, wenn Vorgänge fachlich stehen bleiben oder Fristen gefährdet sind.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Portal, API und Datenbank sind „grün“, aber 2.400 Vorgänge warten seit Stunden auf Registerrückmeldungen. Was fehlt?','answer':'Eine service-/prozessrelevante Observability-Sicht auf fachliche Warteschlangen, externe Abhängigkeiten und Durchlauf-/Rückmeldezeiten statt nur Infrastrukturmetriken.'},
 [('Was sind die drei klassischen Telemetriesignale?','Logs, Metriken und Traces.'),('Was unterscheidet SLI und SLO?','SLI ist die Messgröße; SLO der angestrebte Zielwert.'),('Warum ist ein Dashboard allein keine Observability?','Weil Signale, Korrelation, Alarmierung, Handlungswege und Ursachenanalyse zusammengehören.')],
 ['Welche Nutzer-/Prozesswirkung soll beobachtbar sein?','Welche Korrelation verbindet Systeme und Vorgang?','Wer handelt bei welchem Alert?']))

U.append(unit('rto-rpo','RTO/RPO und Betriebsfähigkeit fachlich ableiten','Operations','Vertiefung',19,
 [('rpo-betriebsfahigkeit-prufen',['RTO','RPO','Wiederanlauf']),('kubernetes-architektur-bewerten',['Backup','Restore']),('observability-anforderungen-definieren',['SLO'])],
 ['RTO','RPO','Backup','Restore','Disaster Recovery','Notbetrieb'],
 ['Verfügbarkeit, RTO und RPO trennen','Wiederanlaufziele aus fachlicher Wirkung ableiten','Backup von getesteter Wiederherstellung unterscheiden'],
 'Betriebsfähigkeit ist Architekturqualität. RTO beschreibt die Zielzeit zur Wiederherstellung eines definierten Betriebszustands; RPO den maximal tolerierbaren Datenverlustzeitraum. Backup ist nur eine Voraussetzung – erst getestete Restore- und Wiederanlaufketten zeigen, dass Wiederherstellung funktioniert.',
 [{'title':'RTO','text':'Wie schnell muss ein definierter Zielzustand nach Störung wieder erreicht sein?'},{'title':'RPO','text':'Wie viel Datenverlust in Zeit gemessen ist maximal tolerierbar?'},{'title':'Notbetrieb','text':'Bewusst reduzierter Betriebszustand, der fachlich definiert sein muss.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein Dienstleister sagt: „Wir haben tägliche Backups, also RPO 24h und DR sind erfüllt.“ Warum reicht das nicht?','answer':'Backup-Frequenz allein beweist weder Restore-Fähigkeit noch End-to-End-Wiederanlauf, Zielzustand, Abhängigkeiten oder fachliche Nachpflege. RPO/RTO müssen fachlich begründet und Wiederherstellung getestet werden.'},
 [('Was ist der Unterschied RTO/RPO?','RTO betrifft Wiederherstellungszeit; RPO maximal tolerierbaren Datenverlust.'),('Warum ist Backup nicht gleich Restore?','Weil vorhandene Sicherungen noch nicht beweisen, dass Daten und Systemketten erfolgreich wiederhergestellt werden können.'),('Was muss beim RTO-Zielzustand geklärt werden?','Ob Notbetrieb, Teilbetrieb oder vollständiger Normalbetrieb gemeint ist.')],
 ['Welche fachliche Wirkung hat der Ausfall?','Welche Abhängigkeiten müssen mitwiederhergestellt werden?','Wann wurde Restore/Wiederanlauf zuletzt getestet?']))

U.append(unit('roadmap-transition','Roadmaps mit Übergangsarchitekturen','Transformation','Anwendung',18,
 [('roadmap-mit-ubergangsarchitekturen',['Transition Architecture','Work Package','Abhängigkeit']),('togaf-adm-im-behordenkontext',['Migration Planning','Roadmap'])],
 ['Roadmap','Transition Architecture','Plateau','Gap','Work Package','Entscheidungsfenster'],
 ['Roadmap von Terminplan unterscheiden','Transition Architectures als beherrschbare Zwischenzustände gestalten','Abhängigkeiten und Entscheidungsfenster sichtbar machen'],
 'Eine Architekturroadmap begründet die notwendige Reihenfolge von Veränderungen. Sie verbindet Baseline, Target, Gaps, Transition Architectures, Work Packages, Abhängigkeiten, Risiken und Entscheidungsfenster. Übergangsarchitekturen sind keine Niederlage, sondern professionelle Gestaltung realer Zwischenzustände.',
 [{'title':'Terminplan','text':'Sagt, wann Arbeit geplant ist.'},{'title':'Architekturroadmap','text':'Erklärt zusätzlich, warum eine Reihenfolge architektonisch notwendig ist und welche stabilen Zwischenzustände entstehen.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Legacy-Fachverfahren kann erst in 18 Monaten ersetzt werden, muss aber heute sicherer integriert werden. Wie sieht eine Transition Architecture aus?','answer':'Das Legacy bleibt befristet, erhält klar dokumentierte Schnittstellen/Adapter, Monitoring, Daten- und Betriebsverantwortung, ggf. IAM-Integration sowie einen expliziten Rückbau-/Ablösepfad.'},
 [('Was ist ein Plateau?','Ein zeitlich begrenzter, relativ stabiler Architekturzustand.'),('Was ist ein Work Package?','Ein logisch zusammengehöriges Veränderungspaket, das einen Teil der Zielarchitektur realisiert.'),('Warum sind Entscheidungsfenster wichtig?','Weil verspätete Architekturentscheidungen nachgelagerte Maßnahmen blockieren oder verteuern können.')],
 ['Welche Zwischenzustände sind wirklich betreibbar?','Welche Abhängigkeit erzwingt Reihenfolge?','Welche technische Schuld entsteht temporär und wann wird sie zurückgebaut?']))

U.append(unit('governance-light','Architecture Governance: leichtgewichtig und risikobasiert','Governance','Anwendung',18,
 [('architektur-governance-fur-behorden',['Entscheidungssystem','Review','Ausnahme']),('adr-erstellung-und-praxis',['Governance','ADR'])],
 ['Architecture Governance','Architecture Board','Review Gate','Exception','ADR'],
 ['Governance als Entscheidungssystem statt Genehmigung verstehen','Prinzipien in Standards und Reviewfragen übersetzen','Ausnahmen und Eskalationen transparent behandeln'],
 'Architektur-Governance ist ein System aus Prinzipien, Standards, Entscheidungsrechten, Reviews, ADRs, Ausnahmen und Maßnahmenverfolgung. Sie soll früh unterstützen und Risiken sichtbar machen, nicht jedes Detail zentral genehmigen. Architecture Boards gehören vor allem zu risikoreichen, bereichsübergreifenden oder standardabweichenden Themen.',
 [{'title':'Prinzip','text':'Stabile Leitlinie für gewünschtes Architekturverhalten.'},{'title':'Standard','text':'Prüfbare Konkretisierung eines Prinzips.'},{'title':'Ausnahme','text':'Bewusste, dokumentierte Abweichung mit Begründung, Risiko, Kompensation und ggf. Ablaufdatum.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein Projekt möchte wegen Legacy-Zwang vom zentralen IAM-Standard abweichen. Was sollte Governance leisten?','answer':'Früh prüfen, ADR/Exception dokumentieren, Risiko und Kompensationsmaßnahmen bewerten, Gültigkeitsdauer bzw. Rückbaupfad festlegen und zuständige interne Entscheidung einholen.'},
 [('Warum ist Governance nicht gleich Genehmigung?','Weil gute Governance klare Spielregeln, frühe Beratung, risikobasierte Reviews und dokumentierte Abweichungen kombiniert.'),('Wann gehört ein Thema ins Architecture Board?','Vor allem bei hohem Risiko, bereichsübergreifender Wirkung oder relevanter Standardabweichung.'),('Warum braucht Governance Ausnahmen?','Damit notwendige Abweichungen transparent und kontrolliert statt als Schattenentscheidung erfolgen.')],
 ['Welche Entscheidungsebene ist angemessen?','Welche Evidenz muss vorliegen?','Wie wird die Ausnahme beendet oder überprüft?']))

U.append(unit('ausschreibung-abnahme','Architekturqualität beschaffbar und abnahmefähig machen','Governance','Vertiefung',19,
 [('architekturqualitat-in-ausschreibungen',['prüfbar','Nachweis','Abnahme']),('schnittstellenvertrag-erstellen',['Abnahme','Vertrag']),('cd-und-iac-architektur',['Nachweis','Release'])],
 ['Leistungsbeschreibung','Liefergegenstand','Nachweis','Abnahmekriterium','Quality Gate'],
 ['Architekturprinzipien in prüfbare Anforderungen übersetzen','Liefergegenstand und Nachweis explizit machen','Abnahme nicht auf Funktionsdemo reduzieren'],
 'Architekturfragen sind Steuerungsinstrumente: Von der fachlichen Wirkung über Verantwortung und Datenflüsse bis zu Betriebsfähigkeit und Nachweisen. Für Beschaffung muss Architekturqualität in konkrete Anforderungen, Liefergegenstände, Nachweise, Reviewpunkte und Abnahmekriterien übersetzt werden.',
 [{'title':'Anforderung','text':'Was muss erfüllt sein?'},{'title':'Liefergegenstand','text':'Welches konkrete Ergebnis/Dokument/Artefakt muss geliefert werden?'},{'title':'Nachweis','text':'Woran ist objektiv erkennbar, dass die Anforderung erfüllt ist?'},{'title':'Abnahmekriterium','text':'Welche überprüfbare Bedingung entscheidet über Akzeptanz?' }],
 {'label':'Abgeleitete Anwendung','prompt':'In einer Ausschreibung steht nur „Die Lösung muss hochverfügbar sein“. Warum ist das zu schwach?','answer':'Der Begriff ist nicht prüfbar genug. Es fehlen fachlich begründete Ziele, Mess-/Nachweisverfahren, Abhängigkeiten, Wiederanlauf/Restore, Betriebsmodell und konkrete Abnahmekriterien.'},
 [('Warum reichen Architekturprinzipien allein in Ausschreibungen nicht?','Weil sie in prüfbare Anforderungen, Liefergegenstände und Nachweise übersetzt werden müssen.'),('Was ist ein guter Nachweis?','Ein überprüfbares Artefakt oder Testergebnis, das direkt auf eine Anforderung verweist.'),('Was sollte ein EA bei Abnahme prüfen?','Nicht nur Funktion, sondern Architekturkonformität, Security, Betrieb, Schnittstellen, Nachweise und offene Abweichungen.')],
 ['Kann der Bieter objektiv erkennen, was geliefert werden muss?','Ist jede wichtige Anforderung nachweisbar?','Welche Abweichungen verhindern Abnahme oder erfordern Entscheidung?']))

U.append(unit('architecture-review-fragelogik','Architecture Review: vom Unklaren zum Prüfbaren','Governance','Vertiefung',18,
 [('architekturqualitat-in-ausschreibungen',['Fragetrichter','Orientierungsfragen','Kontextfragen']),('security-by-architecture-review-anleitung',['Review','Befund']),('rpo-betriebsfahigkeit-prufen',['Interviewfragen'])],
 ['Architecture Review','Orientierungsfrage','Kontextfrage','Review Gate'],
 ['Fragen passend zur Architekturphase wählen','Von offenem Kontext zu prüfbarer Evidenz führen','Review mit Entscheidungen, Ownern und nächsten Artefakten beenden'],
 'Ein EA fragt nicht, um möglichst viel Wissen zu sammeln, sondern um Komplexität entscheidbar, lieferbar und prüfbar zu machen. Die Fragelogik führt von Orientierung über Kontext und Struktur zu Annahmenprüfung, Entscheidung und Nachweis. Zu frühe Technikfragen können den Problemraum verengen.',
 [{'title':'Orientierung','text':'Welches fachliche Problem soll gelöst werden?'},{'title':'Kontext','text':'Welche Systeme, Rollen und externen Stellen sind betroffen?'},{'title':'Struktur','text':'Welche Fähigkeiten, Daten, Anwendungen und Schnittstellen sind relevant?'},{'title':'Nachweis','text':'Woran erkennen wir objektiv, dass eine Architektur- oder Qualitätsanforderung erfüllt ist?'}],
 {'label':'Abgeleitete Anwendung','prompt':'Du startest ein Review und fragst sofort „Welche Datenbank nutzt ihr?“. Was wäre eine bessere erste Sequenz?','answer':'Zuerst fachliches Ziel und Scope, dann Stakeholder/Verantwortung, Fähigkeiten/Prozesse, Daten und Abhängigkeiten; technische Detailfragen folgen aus dem Kontext.'},
 [('Was ist der Zweck guter Architekturfragen?','Komplexität in prüfbare Entscheidungen, Risiken, Verantwortungen und Liefergegenstände zu überführen.'),('Warum sind frühe Technikfragen problematisch?','Sie können Lösungen vorwegnehmen, bevor fachlicher Kontext und Qualitätsanforderungen geklärt sind.'),('Wie endet ein gutes Review?','Mit offenen Punkten, Entscheidungen, Verantwortlichen, Fristen/Nachweisen und nächstem Artefakt/Gate.')],
 ['Welche Entscheidung soll nach dem Review möglich sein?','Welche Annahme ist noch unbewiesen?','Welche Evidenz fehlt?']))

U.append(unit('cross-domain-modernisierung','Capstone: Fachverfahrensmodernisierung als EA-End-to-End-Fall','EA Core','Capstone',25,
 [('togaf-adm-im-behordenkontext',['Fachverfahren','Zielarchitektur']),('capability-mapping-bundesbehorden',['Capability','Anwendung']),('datenlandkarten-fur-behorden',['Datenlandkarte','führendes System']),('schnittstellenvertrag-erstellen',['Schnittstellenvertrag']),('roadmap-mit-ubergangsarchitekturen',['Transition Architecture']),('architektur-governance-fur-behorden',['Review','Governance'])],
 ['Capability','Datenführerschaft','Schnittstellenvertrag','Transition Architecture','Governance'],
 ['Ein Modernisierungsvorhaben über mehrere Architekturdomänen strukturieren','Lokale Lösungsideen in Enterprise-Zusammenhänge übersetzen','Aus Analyse einen entscheidungsfähigen Zielpfad ableiten'],
 'Ein echtes EA-Mandat verbindet Fähigkeiten, Prozesse, Daten, Anwendungen, Schnittstellen, Technologie, Security, Betrieb und Governance. Die Aufgabe ist nicht, sofort eine Zieltechnologie zu wählen, sondern die relevanten Abhängigkeiten und Entscheidungen in eine nachvollziehbare Reihenfolge zu bringen.',
 [{'title':'1. Problemraum','text':'Mandat, Stakeholder, fachliche Fähigkeiten, aktuelle Risiken.'},{'title':'2. Architekturdomänen','text':'Datenführerschaft, Systemrollen, Schnittstellen, Plattform/Security/Betrieb.'},{'title':'3. Transformation','text':'Gaps, Optionen, Transition Architectures, Work Packages und Entscheidungen.'},{'title':'4. Governance','text':'Reviews, ADRs, Ausnahmen, Nachweise und Abnahme.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Drei Fachverfahren, zwei Dienstleister, uneinheitliches IAM, manuelle Registerabgleiche und unterschiedliche DMS-Anbindungen sollen modernisiert werden. Welche ersten sechs EA-Schritte setzt du?','answer':'1 Mandat/Scope und Entscheider klären; 2 Capabilities und kritische Prozesse erfassen; 3 Datenobjekte/Führerschaft klären; 4 Anwendungen/Schnittstellen/Abhängigkeiten ordnen; 5 Security/Betrieb/Plattformconstraints erfassen; 6 Optionen, Gaps, Übergangsarchitekturen und Roadmap zur Entscheidung vorbereiten.'},
 [('Was ist der häufigste Fehler bei komplexer Modernisierung?','Zu früh auf eine technische Lösung zu springen, bevor Problem, Fähigkeiten, Daten und Verantwortungen geklärt sind.'),('Wie entsteht die Roadmap?','Aus Zielbild, Gaps, Abhängigkeiten, Risiken, Work Packages und beherrschbaren Übergangsarchitekturen.'),('Wie bleibt der externe EA in seiner Rolle?','Er strukturiert, bewertet und empfiehlt; die interne Behörde entscheidet und bleibt Owner der Governance.')],
 ['Welche sechs Entscheidungen sind aktuell unklar?','Welche Risiken sind fachlich statt nur technisch?','Welche Transition Architecture reduziert Risiko ohne das Zielbild zu verwässern?']))

# Ensure 25 units by adding role/technical principle units
U.append(unit('technische-entscheidung-fachgrund','Technische Entscheidungen fachlich begründen','Technical','Vertiefung',15,
 [('technische-leitsaetze-kritisch-1-3',['fachlichen Grund','technische Entscheidung']),('technische-leitsaetze-100',['fachlichen Grund']),('adr-erstellung-und-praxis',['Decision Driver'])],
 ['Decision Driver','Qualitätsanforderung','Constraint'],
 ['Technologiepräferenz von fachlichem Treiber trennen','Decision Driver explizit machen','Konsequenzen einer Entscheidung benennen'],
 'Eine technische Entscheidung ist dann belastbar, wenn ihr fachlicher oder qualitätsbezogener Treiber sichtbar ist. Nicht jede Implementierungsentscheidung braucht eine Enterprise-Begründung; architekturrelevante Entscheidungen jedoch sollten auf Anforderungen, Risiken, Constraints oder Lebenszykluswirkungen zurückführbar sein.',
 [{'title':'Treiber','text':'Fachlicher Bedarf, Qualitätsanforderung, Security/Betrieb, Standard, Risiko oder Lifecycle.'},{'title':'Präferenz','text':'„Wir kennen Technologie X gut“ kann ein Faktor sein, ersetzt aber keine Eignungsbewertung.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein Team will Kafka einsetzen, weil es „modern und skalierbar“ ist. Welche Antwort erwartest du?','answer':'Welcher fachliche Kommunikationsbedarf, welche Last-/Zeit-/Kopplungsanforderung und welches Fehler-/Betriebsmodell rechtfertigen EDA/Kafka gegenüber einfacheren Optionen?'},
 [('Was macht eine technische Entscheidung architekturrelevant?','Wenn sie systemische Wirkung auf Kopplung, Daten, Qualität, Risiko, Lebenszyklus, Standards oder andere Teams erzeugt.'),('Was ist ein Decision Driver?','Ein maßgeblicher fachlicher oder qualitativer Grund, der eine Architekturentscheidung beeinflusst.'),('Warum Alternativen dokumentieren?','Damit die Eignung der gewählten Lösung gegenüber realistischen Optionen nachvollziehbar ist.')],
 ['Welches Problem löst die Technologie konkret?','Welche einfachere Option wurde geprüft?','Welche langfristigen Konsequenzen entstehen?']))

U.append(unit('betriebsfaehigkeit-vor-eleganz','Technische Eleganz vs. Betriebsfähigkeit','Operations','Vertiefung',17,
 [('technische-leitsaetze-kritisch-1-3',['Betriebsfähigkeit','technische Eleganz']),('rpo-betriebsfahigkeit-prufen',['Betriebsfähigkeit']),('observability-anforderungen-definieren',['Observability'])],
 ['Betriebsfähigkeit','Runbook','Operational Handover','RTO','RPO'],
 ['Produktionsreife von Architekturästhetik trennen','Betriebsfähigkeit als Architekturanforderung formulieren','Nachweis vor Go-live verlangen'],
 'Eine technisch saubere Lösung ist erst produktionsreif, wenn Betriebsfähigkeit nachgewiesen ist. Dazu gehören Verantwortung, beobachtbares Verhalten, beherrschte Abhängigkeiten und Fehlerfälle, fachlich abgeleitete Wiederanlaufziele, getestete Wiederherstellung, Betriebsverfahren und geregelte Übergabe.',
 [{'title':'Architekturreife','text':'Struktur und Entscheidungen sind fachlich/technisch konsistent.'},{'title':'Produktionsreife','text':'Lösung ist implementiert, getestet, betreibbar und mit Nachweisen versehen.'}],
 {'label':'Abgeleitete Anwendung','prompt':'Ein Microservice-System ist sauber geschnitten, aber es gibt keine Runbooks, kein End-to-End-Monitoring und nie getestete Restores. Ist es produktionsreif?','answer':'Nein. Technische Struktur allein beweist keine Betriebsfähigkeit. Die fehlenden Betriebs- und Wiederherstellungsnachweise sind Go-live-relevant.'},
 [('Warum ist Betriebsfähigkeit Architekturqualität?','Weil Zielarchitektur und Lösungsdesign Ausfall, Beobachtbarkeit, Wiederanlauf und Verantwortungen von Anfang an berücksichtigen müssen.'),('Ist Backup ein Betriebsfähigkeitsnachweis?','Nein. Erst erfolgreicher Restore und getestete Wiederanlaufkette liefern belastbare Evidenz.'),('Was ist Operational Handover?','Geregelte Übergabe in Betrieb inklusive Rollen, Runbooks, Monitoring, Support, Nachweisen und offenen Risiken.')],
 ['Wer betreibt und unterstützt die Lösung?','Welche Fehlerfälle wurden real getestet?','Welche Nachweise fehlen vor Go-live?']))

assert len(U)==28, len(U)

# add generated learning cards: 4 per unit
learning=json.load(open(ROOT/'content/learning.json',encoding='utf-8'))
existing={c['id'] for c in learning['cards']}
newcards=[]
for u in U:
    # first 3 checkpoints
    for i,(q,a) in enumerate(u['checkpoints'][:3],1):
        cid=f"unit-{u['id']}-{i}"
        if cid in existing: continue
        newcards.append({'id':cid,'module':u['sourceModules'][0],'unit':u['id'],'competency':u['competency'],'type':'recall' if i==1 else 'understanding','question':q,'answer':a,'explanation':f"Quellengebundener Lerncheck aus der Lerneinheit „{u['title']}“.",'difficulty':1 if u['level']=='Grundlage' else 2,'concepts':u['terms'][:4]})
    cid=f"unit-{u['id']}-4"
    newcards.append({'id':cid,'module':u['sourceModules'][0],'unit':u['id'],'competency':u['competency'],'type':'scenario','question':u['scenario']['prompt'],'answer':u['scenario']['answer'],'explanation':'Abgeleitete Transferaufgabe auf Basis der angegebenen Projektquellen.','difficulty':3,'concepts':u['terms'][:5]})
learning['cards']=[c for c in learning['cards'] if not c['id'].startswith('unit-')]+newcards
learning['version']='2.2.0'
# add curated curriculum path
learning['paths']=[p for p in learning['paths'] if p['id']!='curriculum-22']
learning['paths'].append({'id':'curriculum-22','title':'EA Curriculum 2.2','description':'25 quellengebundene Lerneinheiten von EA-Grundlagen bis Capstone.','modules':['ea-kernaufgaben-12','togaf-adm-im-behordenkontext','capability-mapping-bundesbehorden','datenlandkarten-fur-behorden','schnittstellenvertrag-erstellen','iam-architektur-fur-behorden','rpo-betriebsfahigkeit-prufen','roadmap-mit-ubergangsarchitekturen','architektur-governance-fur-behorden']})
json.dump(learning,open(ROOT/'content/learning.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
json.dump({'version':'2.2.0','units':U},open(ROOT/'content/units.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('units',len(U),'cards',len(learning['cards']),'new',len(newcards))
