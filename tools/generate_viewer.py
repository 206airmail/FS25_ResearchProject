import re, json, os, html, collections

DOC = r"D:\SteamLibrary\steamapps\common\Farming Simulator 25\shared\xml\documentation\vehicle.html"
CLAUDE = r"D:\Users\brown\Documents\Modding\ClaudeDir"
PROJ = r"D:\Users\brown\Documents\Modding\FS25_ResearchProject"

enums = json.load(open(os.path.join(CLAUDE, "vehicle_enums.json"), encoding="utf-8"))
reg   = json.load(open(os.path.join(CLAUDE, "registries.json"), encoding="utf-8"))

# ---------- value lookups (same logic as the tooltip enricher) ----------
A = {}
for r in enums:
    if r["attr"] == "(element text)":
        continue
    A[(r["path"], r["attr"].lstrip("#"))] = r["values"]

_byleaf = collections.defaultdict(list)
for r in enums:
    if r["attr"] == "(element text)":
        continue
    _byleaf[(r["path"].split(".")[-1], r["attr"].lstrip("#"))].append(tuple(r["values"]))
A_fb = {k: list(v[0]) for k, v in _byleaf.items() if len(set(v)) == 1}

def base(x): return x["__base__"] if isinstance(x, dict) else x
B = {
    "jointType": (reg["jointType"], "AttacherJoints.lua"),
    "fillType": (base(reg["fillType"]), "maps_fillTypes.xml"),
    "fillTypes": (base(reg["fillType"]), "maps_fillTypes.xml"),
    "fillTypeCategories": (reg["fillTypeCategory"], "maps_fillTypes.xml"),
    "fruitType": (base(reg["fruitType"]), "maps_fruitTypes.xml (case-insensitive)"),
    "sprayType": (base(reg["sprayType"]), "maps_sprayTypes.xml"),
    "particleType": (reg["particleType"], "ParticleSystemManager.lua"),
    "effectClass": (reg["effectClass"], "Effect subclasses (open set)"),
    "rigidBodyTypeActive": (reg["rigidBodyType"], "RigidBodyType (case-insensitive)"),
    "rigidBodyTypeInactive": (reg["rigidBodyType"], "RigidBodyType (case-insensitive)"),
    "inputAction": (reg["inputAction"], "inputActions.xml"),
    "vehicleBrand": (reg["brand"], "brands.xml"),
    "displayBrand": (reg["brand"], "brands.xml"),
    "brand": (reg["brand"], "brands.xml"),
    "category": (reg["storeCategory"], "storeCategories.xml"),
    "subCategory": (reg["storeCategory"], "storeCategories.xml"),
    "materialTemplateName": (reg["materialTemplate_base"] + reg["materialTemplate_brand"], "materialTemplates.xml"),
    "defaultColorMaterialTemplateName": (reg["materialTemplate_base"] + reg["materialTemplate_brand"], "material templates"),
    "materialTemplateNameColor": (reg["materialTemplate_base"] + reg["materialTemplate_brand"], "material templates"),
}
WORKAREA = reg["workAreaType"]

def lookup(path, tag, attr):
    if (path, attr) in A: return A[(path, attr)], "schema"
    if (tag, attr) in A_fb: return A_fb[(tag, attr)], "schema"
    if attr in B: return B[attr][0], B[attr][1]
    if attr == "type" and tag == "workArea": return WORKAREA, "workAreaType"
    return None, None

# ---------- parse game HTML into a tree ----------
text = open(DOC, encoding="utf-8").read()
elem_pat = r'margin-left:(\d+)em"><span class="idTag">&lt;(\w+)'
attr_pat = r'<span class="idAttr">(\w+)</span>=<span class="idVal">"([^"]*)"</span><span class="attrInfo">(.*?)</span>'
combined = re.compile(elem_pat + "|" + attr_pat, re.S)

class Node:
    __slots__ = ("tag", "attrs", "children")
    def __init__(self, tag):
        self.tag = tag; self.attrs = []; self.children = []

root = Node("vehicle")
stack = [root]  # index = depth

def field(info, key):
    m = re.search(re.escape(key) + r":\s*(.*?)<br>", info, re.S)
    return m.group(1).strip() if m else ""

for m in combined.finditer(text):
    if m.group(1) is not None:  # element open
        depth = int(m.group(1)) // 2          # 2em -> depth 1 (root 'vehicle' is depth 0)
        node = Node(m.group(2))
        stack = stack[:depth]                 # keep ancestors strictly above this depth
        if not stack:
            stack = [root]
        stack[-1].children.append(node)
        stack.append(node)                    # stack[depth] = node
    else:  # attribute on current node
        name, default, info = m.group(3), m.group(4), m.group(5)
        cur = stack[-1]
        path = ".".join(n.tag for n in stack)  # includes root 'vehicle'
        vals, src = lookup(path, cur.tag, name)
        cur.attrs.append({
            "name": name,
            "type": field(info, "Type"),
            "default": field(info, "Default") or default,
            "desc": field(info, "Description"),
            "req": field(info, "Required"),
            "values": vals, "src": src,
        })

# ---------- render ----------
CAP = 28
def esc(s): return html.escape(s or "")

def vals_html(vals, src):
    n = len(vals)
    if n > CAP:
        shown = ", ".join(esc(v) for v in vals[:24])
        more = f' <span class="more">+{n-24} more → see Reference.md</span>'
    else:
        shown = ", ".join(esc(v) for v in vals); more = ""
    return f'<div class="vals"><span class="vcount">▸ {n} values</span> {shown}{more}<span class="src">{esc(src)}</span></div>'

out = []
def render(node, is_root):
    searchparts = [node.tag]
    body = []
    if node.attrs:
        body.append('<div class="attrs">')
        for a in node.attrs:
            searchparts.append(a["name"])
            cls = "attr has-vals" if a["values"] else "attr"
            body.append(f'<div class="{cls}">')
            body.append(f'<span class="aname">{esc(a["name"])}</span>')
            if a["type"]: body.append(f'<span class="atype">{esc(a["type"])}</span>')
            if a["default"]: body.append(f'<span class="adef">= {esc(a["default"])}</span>')
            if a["desc"]: body.append(f'<div class="adesc">{esc(a["desc"])}</div>')
            if a["values"]:
                body.append(vals_html(a["values"], a["src"]))
                searchparts.extend(a["values"][:12])
            body.append('</div>')
        body.append('</div>')
    for ch in node.children:
        body.append(render(ch, False))
    nattr = len(node.attrs); nch = len(node.children)
    meta = []
    if nattr: meta.append(f'{nattr} attr')
    if nch: meta.append(f'{nch} child')
    metas = f' <span class="cnt">{", ".join(meta)}</span>' if meta else ''
    data = esc(" ".join(searchparts).lower())
    rootcls = " root" if is_root else ""
    return (f'<details class="node{rootcls}" data-text="{data}">'
            f'<summary><span class="tag">&lt;{esc(node.tag)}&gt;</span>{metas}</summary>'
            f'{"".join(body)}</details>')

tree_html = "".join(render(ch, True) for ch in root.children)
total_attrs = len(re.findall(r'class="aname"', tree_html))

CSS = """
*{box-sizing:border-box}
body{font-family:-apple-system,Segoe UI,Roboto,sans-serif;margin:0;background:#0f1115;color:#d7dbe0;font-size:13px}
header{position:sticky;top:0;background:#161a21;border-bottom:1px solid #2a2f3a;padding:10px 14px;z-index:10}
header h1{margin:0 0 6px;font-size:15px;color:#fff}
header .sub{color:#8a93a0;font-size:12px;margin-bottom:8px}
#q{width:60%;max-width:520px;padding:7px 10px;border-radius:6px;border:1px solid #39404d;background:#0f1115;color:#fff;font-size:13px}
header button{padding:7px 10px;border-radius:6px;border:1px solid #39404d;background:#222834;color:#cfd5dd;cursor:pointer;font-size:12px}
header button:hover{background:#2c3340}
#status{color:#7f8896;margin-left:8px;font-size:12px}
main{padding:10px 14px 60px}
details.node{border-left:1px solid #232833;margin:1px 0 1px 8px;padding-left:8px}
details.node.root{border-left:2px solid #3a6;margin-top:6px}
summary{cursor:pointer;padding:2px 4px;border-radius:4px;list-style:none}
summary:hover{background:#1b212b}
summary::-webkit-details-marker{display:none}
summary::before{content:'▶';color:#5a6472;font-size:9px;margin-right:6px;display:inline-block;transition:transform .1s}
details[open]>summary::before{transform:rotate(90deg)}
.tag{color:#6cc4ff;font-family:Consolas,monospace}
details.node.root>summary .tag{color:#5fd49a;font-weight:600}
.cnt{color:#5a6472;font-size:11px;margin-left:6px}
.attrs{margin:2px 0 4px 18px}
.attr{padding:2px 0;border-top:1px dotted #1c2128}
.attr.has-vals{background:#11211a;border-radius:4px;padding:3px 6px;margin:2px 0;border-top:none}
.aname{color:#ffd479;font-family:Consolas,monospace;font-weight:600}
.atype{color:#7f8896;margin-left:8px;font-size:11px}
.adef{color:#c98fff;margin-left:6px;font-size:11px;font-family:Consolas,monospace}
.adesc{color:#9aa3af;font-size:11px;margin:1px 0 1px 0}
.vals{margin-top:2px;font-family:Consolas,monospace;font-size:11px;color:#6fe3a8;line-height:1.5}
.vcount{color:#3a6;font-weight:600;margin-right:4px}
.more{color:#d89b4a}
.src{color:#5a6472;font-style:italic;margin-left:6px}
mark{background:#5a4a00;color:#ffe08a;padding:0 1px}
.hidden{display:none}
"""

JS = """
const q=document.getElementById('q'),status=document.getElementById('status');
const nodes=[...document.querySelectorAll('details.node')];
function setDefault(){nodes.forEach(n=>{n.classList.remove('hidden');n.open=false;});status.textContent=nodes.length+' tags';}
function debounce(f,ms){let t;return(...a)=>{clearTimeout(t);t=setTimeout(()=>f(...a),ms)}}
const run=debounce(()=>{
  const s=q.value.toLowerCase().trim();
  if(!s){setDefault();return;}
  nodes.forEach(n=>n.classList.add('hidden'));
  let c=0;
  for(const n of nodes){
    if(n.dataset.text.includes(s)){
      c++;n.classList.remove('hidden');n.open=true;
      let p=n.parentElement&&n.parentElement.closest('details.node');
      while(p){p.classList.remove('hidden');p.open=true;p=p.parentElement&&p.parentElement.closest('details.node');}
    }
  }
  status.textContent=c+' matching tag'+(c===1?'':'s');
},120);
q.addEventListener('input',run);
document.getElementById('expand').onclick=()=>nodes.forEach(n=>n.open=true);
document.getElementById('collapse').onclick=()=>setDefault();
q.addEventListener('keydown',e=>{if(e.key==='Escape'){q.value='';setDefault();}});
setDefault();
"""

page = f"""<!doctype html><html><head><meta charset="utf-8">
<title>FS25 Vehicle XML — Navigable Value Reference</title>
<style>{CSS}</style></head><body>
<header>
<h1>FS25 Vehicle XML — Navigable Value Reference</h1>
<div class="sub">Every tag collapsible · live search (tag / attribute / value) · valid value lists inline (green).
Built from vehicle.xsd + data + dataS + DLCs · game 1.19.0.0 · {total_attrs} attributes · large sets truncated → see Vehicle_XML_Value_Reference.md</div>
<input id="q" placeholder="Search tags, attributes, or values… (e.g. jointType, fillType, dashboard)  —  Esc to clear" autofocus>
<button id="expand">expand all</button>
<button id="collapse">collapse all</button>
<span id="status"></span>
</header>
<main>{tree_html}</main>
<script>{JS}</script>
</body></html>"""

os.makedirs(PROJ, exist_ok=True)
p = os.path.join(PROJ, "vehicle_browser.html")
with open(p, "w", encoding="utf-8") as f:
    f.write(page)
print("Wrote", p)
print("Size: %.1f MB" % (len(page)/1e6))
print("Attributes rendered:", total_attrs)
print("Root specs:", len(root.children))
