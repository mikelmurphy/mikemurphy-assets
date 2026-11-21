import subprocess, json, re, sys
def starts(pdf, anchors):
    n=int(subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout.split('Pages:')[1].split()[0])
    pages=[re.sub(r'\s+',' ',subprocess.run(['pdftotext','-f',str(p),'-l',str(p),pdf,'-'],capture_output=True,text=True).stdout) for p in range(1,n+1)]
    out={}
    for a,lvl,t in anchors:
        if lvl!=2: continue
        key=re.sub(r'\s+',' ',t).upper()[:38]
        for i,pg in enumerate(pages,1):
            if key in pg: out[a]=i; break
    return n,out
if __name__=='__main__':
    s=json.load(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'structure.json')))
    n,o=starts(sys.argv[1], s['anchors']); print(n, o)
    if len(sys.argv)>2: json.dump({'pages':n,'starts':o},open(sys.argv[2],'w'),indent=1)
