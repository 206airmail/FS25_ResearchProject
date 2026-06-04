import re, json, os, html, glob, collections
import xml.etree.ElementTree as ET

SCHEMADIR = r"D:\SteamLibrary\steamapps\common\Farming Simulator 25\shared\xml\schema"
CLAUDE = r"D:\Users\brown\Documents\Modding\ClaudeDir"
OUT = r"D:\Users\brown\Documents\Modding\FS25_ResearchProject\extension\schemas"
reg = json.load(open(os.path.join(CLAUDE, "registries.json"), encoding="utf-8"))
NS = "{http://www.w3.org/2001/XMLSchema}"

OPEN = False
def basev(x): return x["__base__"] if isinstance(x, dict) else x

# named type -> (values, doc). These registries are GLOBAL (apply in any XML type).
TYPES = {
    "fs25_jointType": (reg["jointType"], "Attacher joint type"),
    "fs25_fillType": (basev(reg["fillType"]), "Fill type name (UPPERCASE)"),
    "fs25_fruitType": (basev(reg["fruitType"]), "Fruit/crop type (case-insensitive)"),
    "fs25_particleType": (reg["particleType"], "Particle system type"),
    "fs25_effectClass": (reg["effectClass"], "Effect class (open set)"),
    "fs25_rigidBodyType": (reg["rigidBodyType"], "RigidBodyType (case-insensitive)"),
    "fs25_inputAction": (reg["inputAction"], "Input action name"),
    "fs25_brand": (reg["brand"], "Brand id"),
    "fs25_storeCategory": (reg["storeCategory"], "Shop category"),
    "fs25_materialTemplate": (reg["materialTemplate_base"] + reg["materialTemplate_brand"], "Material template name"),
}
# (attr-or-element name, current type token) -> named type
ATTR_MAP = {
    "jointType": ("g_string", "fs25_jointType"),
    "fillType": ("g_string", "fs25_fillType"),
    "fruitType": ("g_string", "fs25_fruitType"),
    "particleType": ("g_string", "fs25_particleType"),
    "effectClass": ("g_string", "fs25_effectClass"),
    "rigidBodyTypeActive": ("g_string", "fs25_rigidBodyType"),
    "rigidBodyTypeInactive": ("g_string", "fs25_rigidBodyType"),
    "inputAction": ("g_string", "fs25_inputAction"),
    "vehicleBrand": ("g_string", "fs25_brand"),
    "displayBrand": ("g_string", "fs25_brand"),
    "brand": ("g_string", "fs25_brand"),
    "category": ("g_string", "fs25_storeCategory"),
    "materialTemplateName": ("g_vehicle_material", "fs25_materialTemplate"),
}

def simpletype_xml(name, values, doc):
    enums = "\n".join('      <xs:enumeration value="%s"/>' % html.escape(v) for v in values)
    restr = '    <xs:restriction base="xs:string">\n%s\n    </xs:restriction>' % enums
    inner = ('    <xs:union memberTypes="xs:string">\n      <xs:simpleType>\n%s\n      </xs:simpleType>\n    </xs:union>' % restr) if OPEN else restr
    return ('  <xs:simpleType name="%s">\n    <xs:annotation><xs:documentation>%s — %d values (FS25_ResearchProject)</xs:documentation></xs:annotation>\n%s\n  </xs:simpleType>' % (name, html.escape(doc), len(values), inner))

os.makedirs(OUT, exist_ok=True)
root_map = {}          # root element name -> [schema files]
filename_map = {}      # schema stem -> root element name
summary = []

for path in sorted(glob.glob(os.path.join(SCHEMADIR, "*.xsd"))):
    stem = os.path.splitext(os.path.basename(path))[0]
    xsd = open(path, encoding="utf-8").read()
    # root element(s): direct xs:element children of xs:schema
    try:
        tree = ET.fromstring(xsd)
        roots = [e.get("name") for e in tree.findall(NS + "element")]
    except ET.ParseError:
        roots = []
    for r in roots:
        root_map.setdefault(r, []).append(stem)
    filename_map[stem] = roots

    # which targets are present (as attribute or element) with the expected old type
    needed = {}
    retypes = []
    for nm, (oldtype, newtype) in ATTR_MAP.items():
        pat_attr = r'(<xs:attribute name="%s"[^>]*?) type="%s"' % (re.escape(nm), re.escape(oldtype))
        pat_elem = r'(<xs:element name="%s"[^>]*?) type="%s"' % (re.escape(nm), re.escape(oldtype))
        if re.search(pat_attr, xsd) or re.search(pat_elem, xsd):
            needed[newtype] = TYPES[newtype]
            retypes.append((nm, oldtype, newtype, pat_attr, pat_elem))
    if needed:
        block = "\n".join(simpletype_xml(k, v[0], v[1]) for k, v in needed.items())
        xsd, n = re.subn(r'(<xs:schema\b[^>]*>)', lambda m: m.group(1) + "\n" + block, xsd, count=1)
        total = 0
        for nm, oldtype, newtype, pa, pe in retypes:
            xsd, a = re.subn(pa, r'\1 type="%s"' % newtype, xsd)
            xsd, b = re.subn(pe, r'\1 type="%s"' % newtype, xsd)
            total += a + b
        # validate
        try:
            ET.fromstring(xsd); ok = True
        except ET.ParseError as e:
            ok = False; print("PARSE FAIL", stem, e)
        summary.append((stem, total, sorted(needed)))
    open(os.path.join(OUT, os.path.basename(path)), "w", encoding="utf-8").write(xsd)

print("Schemas written:", len(glob.glob(os.path.join(OUT, "*.xsd"))))
print("Schemas value-enriched:", len(summary))
for stem, total, types in sorted(summary, key=lambda x: -x[1])[:25]:
    print("  %-26s %3d retypes  %s" % (stem, total, ", ".join(t.replace("fs25_", "") for t in types)))
print("\nAmbiguous root elements (same root, multiple schemas):")
amb = {r: s for r, s in root_map.items() if len(s) > 1}
for r, s in sorted(amb.items(), key=lambda x: -len(x[1]))[:12]:
    print("  <%s> -> %s" % (r, ", ".join(s)))

# write root->schema map for the extension (only UNAMBIGUOUS roots auto-bind by root)
binding = {
    "byRoot": {r: s[0] + ".xsd" for r, s in root_map.items() if len(s) == 1},
    "byFilenameHint": {  # for ambiguous-root data files, match on filename substring
        "fillTypes": "fillTypes.xsd", "fruitTypes": "fruitTypes.xsd",
        "sprayTypes": "sprayTypes.xsd", "densityMapHeightTypes": "densityMapHeightTypes.xsd",
        "map": "map.xsd", "storeItems": "storeItems.xsd",
    },
}
json.dump(binding, open(os.path.join(CLAUDE, "schema_binding.json"), "w"), indent=2)
print("\nUnambiguous root bindings:", len(binding["byRoot"]), "(e.g. vehicle, placeable, handTool)")
