"""Maintainer utility: hash exact distributable file set. Does not sign evidence."""
from analyze import ROOT, sha
def main():
    files=[p for p in sorted(ROOT.rglob('*')) if p.is_file() and not any(x in {'.git','__pycache__'} for x in p.relative_to(ROOT).parts) and p.name!='SHA256SUMS.txt']
    (ROOT/'SHA256SUMS.txt').write_text(''.join(sha(p.read_bytes())+'  '+str(p.relative_to(ROOT))+'\n' for p in files),encoding='utf-8')
    print(f'Sealed {len(files)} files. Run verify.py before committing.')
if __name__=='__main__':main()
