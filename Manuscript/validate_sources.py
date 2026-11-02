from pathlib import Path
import re,json
root=Path(__file__).resolve().parent
main=(root/'main.tex').read_text(encoding='utf-8')
inputs=re.findall(r'\\input\{([^}]+)\}',main)
missing=[p for p in inputs if not (root/(p+'.tex')).exists()]
text=main+'\n'+'\n'.join(p.read_text(encoding='utf-8') for p in (root/'sections').glob('*.tex'))
keys=set(re.findall(r'@\w+\{([^,]+),',(root/'references.bib').read_text(encoding='utf-8')))
cited={k.strip() for group in re.findall(r'\\cite\w*\{([^}]+)\}',text) for k in group.split(',')}
result={'missing_inputs':missing,'missing_citation_keys':sorted(cited-keys),'cited_references':len(cited),'bibliography_entries':len(keys),'static_pass':not missing and not(cited-keys),'compiled':False,'visual_layout_verified':False}
(root/'validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
assert result['static_pass']
