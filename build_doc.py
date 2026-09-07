#!/usr/bin/env python3
import os, sys, json, re, urllib.request
AT = os.environ["ACCESS_TOKEN"]
PAPER = {"red": 1, "green": 1, "blue": 1}; INK = {"red": 0, "green": 0, "blue": 0}; ACC = {"red": 0.3, "green": 0.3, "blue": 0.3}; CODEBG = {"red": 0.95, "green": 0.95, "blue": 0.95}
BODY, DISP, MONO = "Arial", "Arial", "Courier New"
def api(url, method="POST", body=None):
    h = {"Authorization": "Bearer " + AT, "Content-Type": "application/json"}
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None, method=method, headers=h)
    try: return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e: print("API ERROR:", e.read().decode()[:1500]); raise
def color(c): return {"color": {"rgbColor": c}}
def inline_prompts(md):
    base = os.path.dirname(os.path.abspath("CHALLENGE-PACK.md"))
    def rep(m):
        p = open(os.path.join(base, m.group(1))).read(); p = "\n".join(l for l in p.splitlines() if not l.startswith("# "))
        return "```\n" + p.strip() + "\n```"
    return re.sub(r"^See (prompts/[A-Za-z0-9\-]+\.md)$", rep, md, flags=re.M)
def emit(md, idx):
    ins, sty = [], []; lines = md.splitlines(); i = 0; runs = []; cur = None
    def T(s):
        nonlocal idx
        ins.append({"insertText": {"location": {"index": idx}, "text": s}}); a = idx; idx += len(s); return a, idx
    def para(text, named=None, font=BODY, size=11, bold=False, col=INK, space_above=0, space_below=8, code=False, keep=False):
        spans=[]; bolds=[]; out=""
        for part in re.split(r"(`[^`]+`|\*\*[^*]+\*\*)", text):
            if part.startswith("`") and part.endswith("`") and len(part)>2: spans.append((len(out),len(out)+len(part)-2)); out+=part[1:-1]
            elif part.startswith("**") and part.endswith("**") and len(part)>4: bolds.append((len(out),len(out)+len(part)-4)); out+=part[2:-2]
            else: out+=part
        s,e=T(out+"\n")
        ps={"spaceAbove":{"magnitude":space_above,"unit":"PT"},"spaceBelow":{"magnitude":space_below,"unit":"PT"},"avoidWidowAndOrphan":True,"keepWithNext":keep,"lineSpacing":128 if not code else 118}
        f="spaceAbove,spaceBelow,avoidWidowAndOrphan,keepWithNext,lineSpacing"
        if named: ps["namedStyleType"]=named; f+=",namedStyleType"
        if code: ps["shading"]={"backgroundColor":color(CODEBG)}; ps["indentStart"]={"magnitude":12,"unit":"PT"}; ps["indentEnd"]={"magnitude":12,"unit":"PT"}; f+=",shading,indentStart,indentEnd"
        sty.append({"updateParagraphStyle":{"range":{"startIndex":s,"endIndex":e},"paragraphStyle":ps,"fields":f}})
        sty.append({"updateTextStyle":{"range":{"startIndex":s,"endIndex":e},"textStyle":{"weightedFontFamily":{"fontFamily":font,"weight":700 if bold else 400},"fontSize":{"magnitude":size,"unit":"PT"},"bold":bold,"italic":False,"foregroundColor":color(col)},"fields":"weightedFontFamily,fontSize,bold,italic,foregroundColor"}})
        for a,b in bolds: sty.append({"updateTextStyle":{"range":{"startIndex":s+a,"endIndex":s+b},"textStyle":{"bold":True,"weightedFontFamily":{"fontFamily":font,"weight":700}},"fields":"bold,weightedFontFamily"}})
        for a,b in spans: sty.append({"updateTextStyle":{"range":{"startIndex":s+a,"endIndex":s+b},"textStyle":{"weightedFontFamily":{"fontFamily":MONO,"weight":400},"fontSize":{"magnitude":max(size-1.5,8),"unit":"PT"},"backgroundColor":color(CODEBG)},"fields":"weightedFontFamily,fontSize,backgroundColor"}})
        return s,e
    while i < len(lines):
        l=lines[i]
        if l.startswith("```"):
            i+=1; block=[]
            while i<len(lines) and not lines[i].startswith("```"): block.append(lines[i]); i+=1
            i+=1
            for k,bl in enumerate(block): para(bl if bl.strip() else " ", font=MONO, size=9, code=True, space_above=6 if k==0 else 0, space_below=8 if k==len(block)-1 else 0)
            continue
        if l.startswith("# "): para(l[2:], named="TITLE", font=DISP, size=24, bold=True, space_below=6, keep=True); i+=1; continue
        if l.startswith("## "): para(l[3:], named="HEADING_1", font=DISP, size=16, bold=True, space_above=18, space_below=6, keep=True); i+=1; continue
        if l.startswith("### "): para(l[4:], named="HEADING_2", size=12, bold=True, space_above=12, space_below=4, keep=True); i+=1; continue
        m=re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", l)
        if m:
            kind="BULLET_DISC_CIRCLE_SQUARE" if m.group(2) in "-*" else "NUMBERED_DECIMAL_ALPHA_ROMAN"
            s,e=para(m.group(3), space_below=3)
            if cur and cur[2]==kind and cur[1]==s: cur[1]=e
            else:
                if cur: runs.append(tuple(cur))
                cur=[s,e,kind]
            i+=1; continue
        if cur: runs.append(tuple(cur)); cur=None
        if not l.strip(): i+=1; continue
        buf=[l]; i+=1
        while i<len(lines) and lines[i].strip() and not re.match(r"^(#|```|\s*[-*]\s|\s*\d+\.\s)", lines[i]): buf.append(lines[i]); i+=1
        text=" ".join(x.strip() for x in buf)
        if text.startswith("[") and text.endswith("]"): para(text, font=MONO, size=9, col=ACC, space_below=14); continue
        para(text)
    if cur: runs.append(tuple(cur))
    for s,e,kind in sorted(runs, reverse=True): sty.append({"createParagraphBullets":{"range":{"startIndex":s,"endIndex":e},"bulletPreset":kind}})
    return ins, sty, idx
def run(doc_id, ins, sty):
    for chunk in (ins, sty):
        for k in range(0, len(chunk), 200): api(f"https://docs.googleapis.com/v1/documents/{doc_id}:batchUpdate", body={"requests": chunk[k:k+200]})
cmd=sys.argv[1]
if cmd=="rebuild":
    ID, md = sys.argv[2], inline_prompts(open(sys.argv[3]).read())
    d=api(f"https://docs.googleapis.com/v1/documents/{ID}","GET"); end=d["body"]["content"][-1]["endIndex"]
    if end>2: api(f"https://docs.googleapis.com/v1/documents/{ID}:batchUpdate", body={"requests":[{"deleteContentRange":{"range":{"startIndex":1,"endIndex":end-1}}}]})
    ins,sty,_=emit(md,1); run(ID,ins,sty); print("REBUILT https://docs.google.com/document/d/%s/edit"%ID)
elif cmd=="create":
    md=inline_prompts(open(sys.argv[2]).read()); doc=api("https://docs.googleapis.com/v1/documents", body={"title":sys.argv[3]}); ID=doc["documentId"]
    api(f"https://docs.googleapis.com/v1/documents/{ID}:batchUpdate", body={"requests":[{"updateDocumentStyle":{"documentStyle":{"background":{"color":color(PAPER)},"marginTop":{"magnitude":64,"unit":"PT"},"marginBottom":{"magnitude":64,"unit":"PT"},"marginLeft":{"magnitude":72,"unit":"PT"},"marginRight":{"magnitude":84,"unit":"PT"}},"fields":"background,marginTop,marginBottom,marginLeft,marginRight"}}]})
    ins,sty,_=emit(md,1); run(ID,ins,sty); print("DOCLINK: https://docs.google.com/document/d/%s/edit"%ID)
