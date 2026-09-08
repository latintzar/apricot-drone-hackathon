"""Render a small offline review exercise using Python's standard library."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_records(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data.get("trees"), list) or not data["trees"]:
        raise ValueError("Provide at least one tree record")
    seen = set()
    for tree in data["trees"]:
        if not isinstance(tree.get("id"), str) or not tree["id"] or tree["id"] in seen:
            raise ValueError("Each tree needs a unique text ID")
        seen.add(tree["id"])
        for key in ("x", "y"):
            value = tree.get(key)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or not 0 <= value <= 100:
                raise ValueError("Practice coordinates must be finite numbers from 0 to 100")
        if not isinstance(tree.get("observation"), str):
            raise ValueError("Each tree needs a text observation")
    return data


def render(data):
    # Escaping angle brackets prevents data from closing the JSON script element.
    payload = json.dumps(data, ensure_ascii=True).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    return PAGE.replace("__RECORDS__", payload)


PAGE = '''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Orchard review exercise</title>
<style>
body{font:17px/1.55 system-ui,sans-serif;max-width:960px;margin:40px auto;padding:0 20px;color:#242422;background:#faf9f5}
h1{font-size:30px;line-height:1.2}h2{font-size:21px}button,select,input{font:inherit;padding:7px;max-width:100%}
button{cursor:pointer;margin:8px 12px 8px 0}svg{width:100%;background:white;border:1px solid #bbb;max-height:340px}
article{border-top:1px solid #ccc;padding:18px 0}label{display:block;margin:10px 0}small{display:block}#status{min-height:1.6em}
</style>
<h1>Orchard review exercise</h1>
<p>Start with three practice records. Review them, select a tree for treatment planning, and export the decisions and a route drawing.</p>
<p><strong>Invented sample data.</strong> This schematic teaches the review flow. Its coordinates use an arbitrary local grid. Your project will add real images, a bird’s-eye map and checked geographic coordinates.</p>
<label>Your name for this practice review <input id="reviewer" value="Practice reviewer" maxlength="100"></label>
<h2>Practice map</h2><svg id="map" viewBox="0 0 600 300" role="img" aria-label="Schematic of three practice trees and a proposed route"></svg>
<p>The line joins selected trees in their listed order. It is a proposed planning route. Mission planning and field operation are later engineering steps.</p>
<div id="trees"></div>
<button id="save">Download decisions (JSON)</button><button id="image">Download route drawing (SVG)</button>
<p id="status" role="status" aria-live="polite"></p>
<p>Next experiment: replace these records with your own tree IDs and observations, then connect each tree to its images. The downloaded file preserves your decisions; reloading this exercise starts a fresh practice review.</p>
<script id="records" type="application/json">__RECORDS__</script>
<script>
const source=JSON.parse(document.getElementById('records').textContent);
const trees=source.trees.map(t=>({...t,review:'unreviewed',treatment_selected:false,evidence:''}));
const ns='http://www.w3.org/2000/svg',map=document.getElementById('map');
function el(tag,text){const e=document.createElement(tag);if(text)e.textContent=text;return e;}
function draw(){
 map.replaceChildren();
 const selected=trees.filter(t=>t.treatment_selected);
 if(selected.length>1){const line=document.createElementNS(ns,'polyline');line.setAttribute('points',selected.map(t=>`${40+t.x*5.2},${30+t.y*2.4}`).join(' '));line.setAttribute('fill','none');line.setAttribute('stroke','#235b85');line.setAttribute('stroke-width','3');map.append(line);}
 for(const t of trees){const x=40+t.x*5.2,y=30+t.y*2.4,c=document.createElementNS(ns,'circle');c.setAttribute('cx',x);c.setAttribute('cy',y);c.setAttribute('r',16);c.setAttribute('fill',t.treatment_selected?'#235b85':'#555');map.append(c);const label=document.createElementNS(ns,'text');label.setAttribute('x',x);label.setAttribute('y',y-25);label.setAttribute('text-anchor','middle');label.textContent=t.id+(t.treatment_selected?' · selected':'');map.append(label);}
}
for(const t of trees){
 const row=el('article');row.append(el('h2',t.id),el('p',t.observation));
 const label=el('label','Inspection decision '),select=el('select');
 for(const [value,text] of [['unreviewed','Awaiting review'],['reviewed','Reviewed'],['inspect_again','Inspect again'],['treatment_review','Treatment review']]){const option=el('option',text);option.value=value;select.append(option);}
 label.append(select);row.append(label);
 const evidenceLabel=el('label','Evidence or review note '),evidence=el('input');evidence.maxLength=500;evidenceLabel.append(evidence);row.append(evidenceLabel);
 const choice=el('label'),checkbox=el('input');checkbox.type='checkbox';checkbox.disabled=true;choice.append(checkbox,document.createTextNode(' Select for treatment planning'));row.append(choice,el('small','Record a treatment review and its evidence to enable this separate choice.'));
 function update(){t.review=select.value;t.evidence=evidence.value.trim();checkbox.disabled=t.review!=='treatment_review'||!t.evidence;if(checkbox.disabled){checkbox.checked=false;t.treatment_selected=false;}draw();}
 select.addEventListener('change',update);evidence.addEventListener('input',update);checkbox.addEventListener('change',()=>{t.treatment_selected=checkbox.checked;draw();});document.getElementById('trees').append(row);
}
function download(content,type,name){const url=URL.createObjectURL(new Blob([content],{type})),a=el('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);document.getElementById('status').textContent='Export prepared: '+name;}
document.getElementById('save').onclick=()=>{const reviewer=document.getElementById('reviewer').value.trim();if(!reviewer){document.getElementById('status').textContent='Enter your name for the review record.';return;}download(JSON.stringify({data_source:source.data_source,coordinate_system:source.coordinate_system,kind:'proposed_treatment_plan',reviewer,exported_at:new Date().toISOString(),route_order:trees.filter(t=>t.treatment_selected).map(t=>t.id),trees},null,2),'application/json','practice-plan.json');};
document.getElementById('image').onclick=()=>{const copy=map.cloneNode(true);copy.setAttribute('xmlns',ns);const caption=document.createElementNS(ns,'text');caption.setAttribute('x',12);caption.setAttribute('y',290);caption.setAttribute('font-size',12);caption.textContent='Invented practice data · Proposed treatment route · Arbitrary local grid';copy.append(caption);download(new XMLSerializer().serializeToString(copy),'image/svg+xml','practice-route.svg');};
draw();
</script></html>'''

if __name__ == "__main__":
    records = load_records(ROOT / "sample" / "trees.json")
    output = ROOT / "output" / "review.html"
    output.parent.mkdir(exist_ok=True)
    output.write_text(render(records), encoding="utf-8")
    print(f"Open {output} in your browser. Data: invented practice records.")
