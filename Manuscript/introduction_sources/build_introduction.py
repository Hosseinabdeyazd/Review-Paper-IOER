"""Build introduction, bibliography and audit from verified DOI metadata."""
from pathlib import Path
import re, json, csv, html, unicodedata

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
TITLE = 'From GeoAI to environmental impact assessment: A systematic review of uncertainty continuity and digital twin architecture for the circular built environment'
data = json.loads((HERE/'crossref_metadata.json').read_text(encoding='utf-8'))
draft = (HERE/'introduction_draft.txt').read_text(encoding='utf-8').strip()
bib = (ROOT/'references.bib').read_text(encoding='utf-8')
entries = re.findall(r'@article\{([^,]+),(.*?)(?=\n@|\Z)', bib, re.S)
existing = {}
for key, entry in entries:
    doi = re.search(r'doi\s*=\s*\{([^}]+)\}', entry)
    if doi: existing[doi.group(1).lower()] = key

def year(m):
    return m.get('published-print',m['published'])['date-parts'][0][0]

def label(m):
    names = [a['family'] for a in m['author']]
    return (names[0] if len(names)==1 else ' and '.join(names) if len(names)==2 else names[0]+' et al.')+', '+str(year(m))

def tex(s):
    s = html.unescape(s).replace('&',r'\&').replace('%',r'\%').replace('_',r'\_')
    s = s.replace('→',r'$\rightarrow$').replace('–','--').replace('—','---')
    replacements={'ł':r'{\l}', 'Ł':r'{\L}', 'ı':r'{\i}'}
    return ''.join(replacements.get(c,c) for c in s)

mapping = {}
rows = []
new_entries = []
for i,m in enumerate(data,1):
    ident=f'I{i:02d}'
    key=existing.get(m['DOI'].lower(),ident)
    mapping[ident]=(key,m)
    assert m['DOI'].startswith(('10.1016/','10.1038/'))
    authors=' and '.join(a['family']+', '+a.get('given','') for a in m['author'])
    fields={'title':'{'+html.unescape(m['title'][0])+'}','author':authors,'year':str(year(m)),
            'journal':html.unescape(m['container-title'][0]),'volume':m.get('volume',''),
            'pages':m.get('page',m.get('article-number','')),'doi':m['DOI']}
    entry='@article{'+key+',\n'+''.join('  '+f+' = {'+tex(v)+'},\n' for f,v in fields.items() if v)+'}\n'
    if key in [x[0] for x in entries]:
        bib=re.sub(r'@article\{'+re.escape(key)+r',.*?(?=\n@|\Z)',lambda _:entry,bib,flags=re.S)
    else: new_entries.append(entry)
    rows.append({'source_id':ident,'citation_key':key,'author_year':label(m),'year':year(m),'title':html.unescape(m['title'][0]),
                 'authors':authors,'journal':m['container-title'][0],'publisher':m['publisher'],'doi':m['DOI'],
                 'url':'https://doi.org/'+m['DOI'],'role':'Introduction/background; does not establish systematic-review inclusion',
                 'verified_date':'2026-11-02'})

def citation(match,mode):
    ids=match.group(1).split(',')
    if mode=='tex':return r'\citep{'+','.join(mapping[i][0] for i in ids)+'}'
    if mode=='plain':return '('+'; '.join(label(mapping[i][1]) for i in ids)+')'
    return '('+'; '.join('['+label(mapping[i][1])+'](https://doi.org/'+mapping[i][1]['DOI']+')' for i in ids)+')'

pattern=r'\[(I\d+(?:,I\d+)*)\]'
plain=re.sub(pattern,lambda m:citation(m,'plain'),draft)
latex=re.sub(pattern,lambda m:citation(m,'tex'),tex(draft))
markdown=re.sub(pattern,lambda m:citation(m,'md'),draft)
(ROOT/'sections/01_introduction.tex').write_text('\\section{Introduction}\n'+latex+'\n',encoding='utf-8')
(ROOT/'references.bib').write_text(bib.rstrip()+'\n\n'+'\n'.join(new_entries),encoding='utf-8')
refs=[]
for m in sorted(data,key=lambda m:(unicodedata.normalize('NFKD',m['author'][0]['family']).casefold(),year(m))):
    names=[]
    for a in m['author']:
        initials=''.join(p[0]+'.' for p in re.split(r'[\s-]+',a.get('given','')) if p)
        names.append(a['family']+', '+initials)
    refs.append(', '.join(names)+', '+str(year(m))+'. '+html.unescape(m['title'][0])+'. '+html.unescape(m['container-title'][0])+' '+m.get('volume','')+', '+m.get('page',m.get('article-number',''))+'. [https://doi.org/'+m['DOI']+'](https://doi.org/'+m['DOI']+').')
(ROOT/'Introduction.md').write_text('# '+TITLE+'\n\n## 1. Introduction\n\n'+markdown+'\n\n## References\n\n'+'\n\n'.join(refs)+'\n',encoding='utf-8')
with (HERE/'reference_audit.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
main=(ROOT/'main.tex').read_text(encoding='utf-8')
main=re.sub(r'\\title\{[^}]+\}',lambda _:r'\title{'+TITLE+'}',main)
main=main.replace('Working manuscript v0.1','Working manuscript v0.2').replace(r'\bibliographystyle{plainnat}',r'\bibliographystyle{elsarticle-harv}')
(ROOT/'main.tex').write_text(main,encoding='utf-8')
used=set(i for group in re.findall(pattern,draft) for i in group.split(','))
assert used==set(mapping)
stats={'body_word_count_excluding_citations':len(re.findall(r"\S+",re.sub(pattern,'',draft))),
       'body_word_count_including_author_year_citations':len(re.findall(r'\S+',plain)),
       'distinct_references':len(used),'references_2020_onward':sum(year(m)>=2020 for m in data),
       'elsevier_references':sum(m['DOI'].startswith('10.1016/') for m in data),
       'nature_portfolio_references':sum(m['DOI'].startswith('10.1038/') for m in data),
       'missing_citations':[], 'latex_compilation':'Not run: no LaTeX compiler available',
       'research_status':'Introduction draft; no new final screening counts or validation claims'}
assert 900<=stats['body_word_count_excluding_citations']<=1250
assert stats['body_word_count_including_author_year_citations']<=1250
(HERE/'validation.json').write_text(json.dumps(stats,indent=2),encoding='utf-8')
print(json.dumps(stats,indent=2))
