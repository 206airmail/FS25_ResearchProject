import re, os, glob, json, sqlite3, html, collections
import xml.etree.ElementTree as ET

SCHEMADIR = r"D:\SteamLibrary\steamapps\common\Farming Simulator 25\shared\xml\schema"
DOCDIR    = r"D:\SteamLibrary\steamapps\common\Farming Simulator 25\shared\xml\documentation"
CLAUDE = r"D:\Users\brown\Documents\Modding\ClaudeDir"
PROJ   = r"D:\Users\brown\Documents\Modding\FS25_ResearchProject"
NS = "{http://www.w3.org/2001/XMLSchema}"
reg = json.load(open(os.path.join(CLAUDE, "registries.json"), encoding="utf-8"))

def basev(x): return x["__base__"] if isinstance(x, dict) else x
# registry value-sets that apply globally (attr/element name -> (values, source))
REGISTRY = {
    "jointType": (reg["jointType"], "AttacherJoints.lua"),
    "fillType": (basev(reg["fillType"]), "maps_fillTypes.xml"),
    "fruitType": (basev(reg["fruitType"]), "maps_fruitTypes.xml"),
    "particleType": (reg["particleType"], "ParticleSystemManager.lua"),
    "effectClass": (reg["effectClass"], "Effect subclasses"),
    "rigidBodyTypeActive": (reg["rigidBodyType"], "RigidBodyType"),
    "rigidBodyTypeInactive": (reg["rigidBodyType"], "RigidBodyType"),
    "inputAction": (reg["inputAction"], "inputActions.xml"),
    "vehicleBrand": (reg["brand"], "brands.xml"),
    "displayBrand": (reg["brand"], "brands.xml"),
    "brand": (reg["brand"], "brands.xml"),
    "category": (reg["storeCategory"], "storeCategories.xml"),
    "materialTemplateName": (reg["materialTemplate_base"] + reg["materialTemplate_brand"], "material templates"),
}

db = os.path.join(PROJ, "data", "fs25_xml.db")
os.makedirs(os.path.dirname(db), exist_ok=True)
if os.path.exists(db): os.remove(db)
con = sqlite3.connect(db); cur = con.cursor()
cur.executescript("""
CREATE TABLE types(name TEXT PRIMARY KEY, root TEXT, n_nodes INT, n_attrs INT, n_enriched INT);
CREATE TABLE nodes(id INTEGER PRIMARY KEY, type TEXT, parent INT, tag TEXT, path TEXT, depth INT);
CREATE TABLE attrs(id INTEGER PRIMARY KEY, node INT, type TEXT, name TEXT, kind TEXT,
                   valtype TEXT, dflt TEXT, doc TEXT, valueset INT);
CREATE TABLE valuesets(id INTEGER PRIMARY KEY, origin TEXT, source TEXT, n INT, values_json TEXT);
CREATE INDEX ix_nodes_type ON nodes(type);
CREATE INDEX ix_attrs_node ON attrs(node);
CREATE INDEX ix_attrs_name ON attrs(name);
""")

# dedup value-sets
vs_cache = {}
def valueset_id(values, origin, source):
    key = (tuple(values), origin)
    if key in vs_cache: return vs_cache[key]
    vid = len(vs_cache) + 1
    cur.execute("INSERT INTO valuesets(id,origin,source,n,values_json) VALUES(?,?,?,?,?)",
                (vid, origin, source, len(values), json.dumps(values)))
    vs_cache[key] = vid
    return vid

node_id = 0
def add_node(type_, parent, tag, path, depth):
    global node_id
    node_id += 1
    cur.execute("INSERT INTO nodes(id,type,parent,tag,path,depth) VALUES(?,?,?,?,?,?)",
                (node_id, type_, parent, tag, path, depth))
    return node_id

attr_id = 0
def add_attr(node, type_, name, kind, valtype, dflt, doc, vsid):
    global attr_id
    attr_id += 1
    cur.execute("INSERT INTO attrs(id,node,type,name,kind,valtype,dflt,doc,valueset) VALUES(?,?,?,?,?,?,?,?,?)",
                (attr_id, node, type_, name, kind, valtype, dflt, doc, vsid))

def doc_of(el):
    a = el.find(NS+"annotation")
    if a is not None:
        d = a.find(NS+"documentation")
        if d is not None and d.text: return d.text.strip()
    return ""

def enum_of(el):
    st = el.find(NS+"simpleType")
    if st is None: return None
    r = st.find(NS+"restriction")
    if r is None: return None
    e = r.findall(NS+"enumeration")
    return [x.get("value") for x in e] if e else None

def walk(type_, el, parent, path, depth):
    """Recursively register element children + their attributes."""
    for child in el:
        tag = child.tag.split('}')[-1]
        if tag == "element":
            name = child.get("name")
            cpath = (path + "." + name) if path else name
            nid = add_node(type_, parent, name, cpath, depth+1)
            # element-text enum?
            ev = enum_of(child)
            if ev:
                add_attr(nid, type_, "(text)", "schema", "", child.get("default"), doc_of(child),
                         valueset_id(ev, "schema", "xsd enumeration"))
            elif name in REGISTRY:
                vals, src = REGISTRY[name]
                add_attr(nid, type_, "(text)", "registry", "", child.get("default"), doc_of(child),
                         valueset_id(vals, "registry", src))
            walk(type_, child, nid, cpath, depth+1)
        elif tag == "attribute":
            aname = child.get("name")
            ev = enum_of(child)
            vsid = None; kind = "plain"
            if ev:
                vsid = valueset_id(ev, "schema", "xsd enumeration"); kind = "schema"
            elif aname in REGISTRY:
                vals, src = REGISTRY[aname]
                vsid = valueset_id(vals, "registry", src); kind = "registry"
            add_attr(parent, type_, aname, kind, child.get("type",""), child.get("default"), doc_of(child), vsid)
        elif tag in ("complexType","sequence","choice","all","group","simpleContent","complexContent","extension"):
            walk(type_, child, parent, path, depth)

for xsd_path in sorted(glob.glob(os.path.join(SCHEMADIR, "*.xsd"))):
    stem = os.path.splitext(os.path.basename(xsd_path))[0]
    try:
        tree = ET.parse(xsd_path).getroot()
    except ET.ParseError as e:
        print("skip", stem, e); continue
    roots = [e.get("name") for e in tree.findall(NS+"element")]
    root_name = roots[0] if roots else stem
    rid = add_node(stem, None, root_name, root_name, 0)
    # the root element's own subtree:
    rootel = tree.find(NS+"element")
    if rootel is not None:
        # attrs + children of the root element
        walk(stem, rootel, rid, root_name, 0)
    n_nodes = cur.execute("SELECT COUNT(*) FROM nodes WHERE type=?", (stem,)).fetchone()[0]
    n_attrs = cur.execute("SELECT COUNT(*) FROM attrs WHERE type=?", (stem,)).fetchone()[0]
    n_enr = cur.execute("SELECT COUNT(*) FROM attrs WHERE type=? AND kind IN('schema','registry')", (stem,)).fetchone()[0]
    cur.execute("INSERT INTO types(name,root,n_nodes,n_attrs,n_enriched) VALUES(?,?,?,?,?)",
                (stem, root_name, n_nodes, n_attrs, n_enr))

con.commit()
# report
print("DB:", db, "(%.1f MB)" % (os.path.getsize(db)/1e6))
tot = cur.execute("SELECT COUNT(*) FROM types"), cur.execute("SELECT COUNT(*) FROM nodes").fetchone()[0], cur.execute("SELECT COUNT(*) FROM attrs").fetchone()[0], cur.execute("SELECT COUNT(*) FROM valuesets").fetchone()[0]
print("types: 88 | nodes: %d | attrs: %d | distinct value-sets: %d" % tot[1:])
print("\nMost enriched types:")
for r in cur.execute("SELECT name,n_nodes,n_attrs,n_enriched FROM types ORDER BY n_enriched DESC LIMIT 12"):
    print("  %-24s nodes=%-5d attrs=%-6d enriched=%d" % r)
print("\nValue-attr coverage: %d of %d attributes have a known value-set" %
      (cur.execute("SELECT COUNT(*) FROM attrs WHERE valueset IS NOT NULL").fetchone()[0],
       cur.execute("SELECT COUNT(*) FROM attrs").fetchone()[0]))
con.close()
