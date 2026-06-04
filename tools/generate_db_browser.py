import sqlite3, json, os, html

PROJ = r"D:\Users\brown\Documents\Modding\FS25_ResearchProject"
con = sqlite3.connect(os.path.join(PROJ, "data", "fs25_xml.db"))
con.row_factory = sqlite3.Row
cur = con.cursor()

# value sets
valuesets = {}
for r in cur.execute("SELECT id,origin,source,values_json FROM valuesets"):
    valuesets[r["id"]] = {"o": r["origin"], "s": r["source"], "v": json.loads(r["values_json"])}

types = [dict(r) for r in cur.execute("SELECT name,root,n_nodes,n_attrs,n_enriched FROM types ORDER BY n_enriched DESC, name")]

# Build a compact tree per type: node = {t:tag, a:[[name,valtype,default,doc,vsid],...], c:[children]}
def build_type(tname):
    nodes = {}
    children = {}
    for r in cur.execute("SELECT id,parent,tag FROM nodes WHERE type=? ORDER BY id", (tname,)):
        nodes[r["id"]] = {"t": r["tag"], "a": [], "c": []}
        children.setdefault(r["parent"], []).append(r["id"])
    for r in cur.execute("SELECT node,name,valtype,dflt,doc,valueset FROM attrs WHERE type=? ORDER BY id", (tname,)):
        if r["node"] in nodes:
            nodes[r["node"]]["a"].append([r["name"], r["valtype"] or "", r["dflt"] or "", r["doc"] or "", r["valueset"]])
    # find root (parent is None)
    roots = children.get(None, [])
    def assemble(nid):
        n = nodes[nid]
        n["c"] = [assemble(c) for c in children.get(nid, [])]
        return n
    return [assemble(r) for r in roots]

DATA = {"types": types, "valuesets": valuesets, "trees": {t["name"]: build_type(t["name"]) for t in types}}
con.close()

payload = json.dumps(DATA, separators=(",", ":"))

HTML = r"""<!doctype html><html><head><meta charset="utf-8">
<title>FS25 XML — All Types Browser</title>
<style>
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,Segoe UI,Roboto,sans-serif;background:#0f1115;color:#d7dbe0;font-size:13px;display:flex;height:100vh;overflow:hidden}
#side{width:250px;min-width:250px;background:#13161c;border-right:1px solid #262b35;display:flex;flex-direction:column}
#side h2{font-size:13px;margin:10px 12px 6px;color:#fff}
#typefilter{margin:0 10px 8px;padding:6px 8px;border-radius:6px;border:1px solid #39404d;background:#0f1115;color:#fff}
#types{overflow:auto;flex:1}
.trow{padding:5px 12px;cursor:pointer;border-left:3px solid transparent;display:flex;justify-content:space-between;gap:6px}
.trow:hover{background:#1b212b}
.trow.sel{background:#1d2733;border-left-color:#3a6}
.tname{color:#cfe3ff;font-family:Consolas,monospace}
.tmeta{color:#5a6472;font-size:11px;white-space:nowrap}
.tmeta b{color:#3a6}
#main{flex:1;display:flex;flex-direction:column;overflow:hidden}
#bar{padding:10px 14px;background:#161a21;border-bottom:1px solid #262b35}
#bar h1{margin:0 0 6px;font-size:14px;color:#fff}
#q{width:55%;max-width:480px;padding:7px 10px;border-radius:6px;border:1px solid #39404d;background:#0f1115;color:#fff}
#bar button{padding:7px 10px;border-radius:6px;border:1px solid #39404d;background:#222834;color:#cfd5dd;cursor:pointer}
#status{color:#7f8896;margin-left:8px;font-size:12px}
#tree{overflow:auto;flex:1;padding:8px 14px 60px}
details.node{border-left:1px solid #232833;margin:1px 0 1px 8px;padding-left:8px}
summary{cursor:pointer;padding:2px 4px;border-radius:4px;list-style:none}
summary:hover{background:#1b212b}
summary::-webkit-details-marker{display:none}
summary::before{content:'\25B6';color:#5a6472;font-size:9px;margin-right:6px;display:inline-block}
details[open]>summary::before{content:'\25BC'}
.tag{color:#6cc4ff;font-family:Consolas,monospace}
.cnt{color:#5a6472;font-size:11px;margin-left:6px}
.attrs{margin:2px 0 4px 18px}
.attr{padding:2px 0;border-top:1px dotted #1c2128}
.attr.v{background:#11211a;border-radius:4px;padding:3px 6px;border-top:none;margin:2px 0}
.an{color:#ffd479;font-family:Consolas,monospace;font-weight:600}
.at{color:#7f8896;font-size:11px;margin-left:8px}
.ad{color:#c98fff;font-size:11px;margin-left:6px;font-family:Consolas,monospace}
.adesc{color:#9aa3af;font-size:11px}
.vals{margin-top:2px;font-family:Consolas,monospace;font-size:11px;color:#6fe3a8;line-height:1.5}
.vc{color:#3a6;font-weight:600;margin-right:4px}
.more{color:#d89b4a}.src{color:#5a6472;font-style:italic;margin-left:6px}
.hidden{display:none}
</style></head><body>
<div id="side">
  <h2>FS25 XML types</h2>
  <input id="typefilter" placeholder="filter types…">
  <div id="types"></div>
</div>
<div id="main">
  <div id="bar">
    <h1 id="title">FS25 XML — All Types Browser</h1>
    <input id="q" placeholder="search tags / attributes / values in this type…  (Esc clears)">
    <button id="expand">expand all</button><button id="collapse">collapse</button>
    <span id="status"></span>
  </div>
  <div id="tree"></div>
</div>
<script>
const DB = __PAYLOAD__;
const CAP=28;
let curType=null;
const typesEl=document.getElementById('types'),treeEl=document.getElementById('tree'),
      titleEl=document.getElementById('title'),statusEl=document.getElementById('status'),
      q=document.getElementById('q');

function valHtml(vsid){
  const vs=DB.valuesets[vsid]; if(!vs) return '';
  const n=vs.v.length; let shown,more='';
  if(n>CAP){shown=vs.v.slice(0,24).join(', ');more=' <span class="more">+'+(n-24)+' more</span>';}
  else shown=vs.v.join(', ');
  return '<div class="vals"><span class="vc">▸ '+n+' values</span> '+esc(shown)+more+
         '<span class="src">'+esc(vs.s)+'</span></div>';
}
function esc(s){return (s+'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}

function renderNode(n){
  const parts=[n.t.toLowerCase()];
  let body='';
  if(n.a.length){
    body+='<div class="attrs">';
    for(const a of n.a){
      parts.push(a[0].toLowerCase());
      const hasv=a[4]!=null;
      body+='<div class="attr'+(hasv?' v':'')+'">';
      body+='<span class="an">'+esc(a[0])+'</span>';
      if(a[1])body+='<span class="at">'+esc(a[1])+'</span>';
      if(a[2])body+='<span class="ad">= '+esc(a[2])+'</span>';
      if(a[3])body+='<div class="adesc">'+esc(a[3])+'</div>';
      if(hasv){body+=valHtml(a[4]);const vs=DB.valuesets[a[4]];if(vs)parts.push(vs.v.slice(0,12).join(' ').toLowerCase());}
      body+='</div>';
    }
    body+='</div>';
  }
  for(const c of n.c) body+=renderNode(c);
  const meta=[]; if(n.a.length)meta.push(n.a.length+' attr'); if(n.c.length)meta.push(n.c.length+' child');
  return '<details class="node" data-text="'+esc(parts.join(' '))+'">'+
    '<summary><span class="tag">&lt;'+esc(n.t)+'&gt;</span>'+(meta.length?'<span class="cnt">'+meta.join(', ')+'</span>':'')+'</summary>'+
    body+'</details>';
}

function loadType(name){
  curType=name;
  document.querySelectorAll('.trow').forEach(r=>r.classList.toggle('sel',r.dataset.name===name));
  const t=DB.types.find(x=>x.name===name);
  titleEl.textContent=name+'.xml  —  root <'+t.root+'>  ·  '+t.n_nodes+' nodes · '+t.n_attrs+' attrs · '+t.n_enriched+' with value-lists';
  treeEl.innerHTML=DB.trees[name].map(renderNode).join('');
  q.value=''; statusEl.textContent='';
}

function buildSidebar(filter){
  filter=(filter||'').toLowerCase();
  typesEl.innerHTML='';
  for(const t of DB.types){
    if(filter && !t.name.toLowerCase().includes(filter)) continue;
    const d=document.createElement('div');
    d.className='trow'+(t.name===curType?' sel':''); d.dataset.name=t.name;
    d.innerHTML='<span class="tname">'+esc(t.name)+'</span><span class="tmeta">'+t.n_attrs+(t.n_enriched?' · <b>'+t.n_enriched+'▸</b>':'')+'</span>';
    d.onclick=()=>loadType(t.name);
    typesEl.appendChild(d);
  }
}

function debounce(f,ms){let t;return(...a)=>{clearTimeout(t);t=setTimeout(()=>f(...a),ms)}}
const search=debounce(()=>{
  const s=q.value.toLowerCase().trim();
  const nodes=[...treeEl.querySelectorAll('details.node')];
  if(!s){nodes.forEach(n=>{n.classList.remove('hidden');n.open=false});statusEl.textContent='';return;}
  nodes.forEach(n=>n.classList.add('hidden'));
  let c=0;
  for(const n of nodes){ if(n.dataset.text.includes(s)){c++;n.classList.remove('hidden');n.open=true;
    let p=n.parentElement&&n.parentElement.closest('details.node');
    while(p){p.classList.remove('hidden');p.open=true;p=p.parentElement&&p.parentElement.closest('details.node');}}}
  statusEl.textContent=c+' matches';
},120);
q.addEventListener('input',search);
q.addEventListener('keydown',e=>{if(e.key==='Escape'){q.value='';search();}});
document.getElementById('typefilter').addEventListener('input',e=>buildSidebar(e.target.value));
document.getElementById('expand').onclick=()=>treeEl.querySelectorAll('details.node').forEach(n=>n.open=true);
document.getElementById('collapse').onclick=()=>treeEl.querySelectorAll('details.node').forEach(n=>n.open=false);

buildSidebar('');
loadType(DB.types[0].name);
</script></body></html>"""

out = HTML.replace("__PAYLOAD__", payload)
p = os.path.join(PROJ, "fs25_xml_browser.html")
open(p, "w", encoding="utf-8").write(out)
print("Wrote", p, "(%.1f MB)" % (len(out)/1e6))
print("Types:", len(types), "| payload %.1f MB" % (len(payload)/1e6))
