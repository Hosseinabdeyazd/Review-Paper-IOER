"""Refresh local availability and SHA256 checks without changing scientific decisions.
Run: python refresh_manifest.py [collection_directory]
Standard library only. PDFs must already be obtained through authorized sources.
"""
from pathlib import Path
import csv,hashlib,json,sys
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent
with (root/'selected_papers.csv').open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f))
assert len(rows)==21 and len({r['doi'].lower().strip() for r in rows})==21
manifest=[]
for r in rows:
    pdf=root/'papers'/(r['paper_id']+'.pdf');txt=pdf.with_suffix('.txt')
    r['local_fulltext']='';r['local_status']='not_yet_located'
    if pdf.exists():
        assert pdf.read_bytes().startswith(b'%PDF'),str(pdf)
        r['local_fulltext']=pdf.relative_to(root).as_posix();r['local_status']='pdf_saved'
    elif txt.exists():
        r['local_fulltext']=txt.relative_to(root).as_posix();r['local_status']='publisher_fulltext_text_saved_pdf_pending'
for p in sorted((root/'papers').glob('*')):
    b=p.read_bytes();manifest.append({'file':p.relative_to(root).as_posix(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
with (root/'selected_papers.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(root/'file_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
counts={'records':len(rows),'unique_doi':len({r['doi'].lower() for r in rows}),'main_pdfs':sum(r['local_status']=='pdf_saved' for r in rows),'publisher_text_only':sum(r['local_status']=='publisher_fulltext_text_saved_pdf_pending' for r in rows),'missing':[r['paper_id'] for r in rows if not r['local_fulltext']]}
(root/'availability_counts.json').write_text(json.dumps(counts,indent=2),encoding='utf-8')
print(json.dumps(counts))
