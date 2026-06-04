import re, json, os, html
import xml.etree.ElementTree as ET

SRC = r"D:\SteamLibrary\steamapps\common\Farming Simulator 25\shared\xml\schema\vehicle.xsd"
CLAUDE = r"D:\Users\brown\Documents\Modding\ClaudeDir"
PROJ = r"D:\Users\brown\Documents\Modding\FS25_ResearchProject"
reg = json.load(open(os.path.join(CLAUDE, "registries.json"), encoding="utf-8"))

OPEN = False  # False = strict (validation flags typos); True = union w/ xs:string (no false errors, suggest-only)

def basev(x): return x["__base__"] if isinstance(x, dict) else x

# named simpleType key -> (values, doc, source)
TYPES = {
    "fs25_jointType":   (reg["jointType"], "Attacher joint type (base game; mods may add more via registerJointType)"),
    "fs25_fillType":    (basev(reg["fillType"]), "Fill type name (base+DLC; maps/mods add more) — UPPERCASE"),
    "fs25_fruitType":   (basev(reg["fruitType"]), "Fruit/crop type (case-insensitive)"),
    "fs25_particleType":(reg["particleType"], "Particle system type (ParticleSystemManager.lua)"),
    "fs25_effectClass": (reg["effectClass"], "Effect implementation class (open set; mods add ModName.MyEffect)"),
    "fs25_rigidBodyType":(reg["rigidBodyType"], "Engine RigidBodyType (case-insensitive)"),
    "fs25_inputAction": (reg["inputAction"], "Input action name (inputActions.xml; mods add own)"),
    "fs25_brand":       (reg["brand"], "Brand id (brands.xml)"),
    "fs25_storeCategory":(reg["storeCategory"], "Shop category (storeCategories.xml)"),
    "fs25_materialTemplate":(reg["materialTemplate_base"] + reg["materialTemplate_brand"], "Material template name (generic + brand colors)"),
}

# vehicle-XML attribute name -> (current type token in xsd, target named type)
ATTR_MAP = [
    ('jointType', 'g_string', 'fs25_jointType'),
    ('fillType', 'g_string', 'fs25_fillType'),
    ('fruitType', 'g_string', 'fs25_fruitType'),
    ('particleType', 'g_string', 'fs25_particleType'),
    ('effectClass', 'g_string', 'fs25_effectClass'),
    ('rigidBodyTypeActive', 'g_string', 'fs25_rigidBodyType'),
    ('rigidBodyTypeInactive', 'g_string', 'fs25_rigidBodyType'),
    ('inputAction', 'g_string', 'fs25_inputAction'),
    ('vehicleBrand', 'g_string', 'fs25_brand'),
    ('displayBrand', 'g_string', 'fs25_brand'),
    ('brand', 'g_string', 'fs25_brand'),
    ('category', 'g_string', 'fs25_storeCategory'),
    ('materialTemplateName', 'g_vehicle_material', 'fs25_materialTemplate'),
]

def simpletype_xml(name, values, doc):
    enums = "\n".join(f'      <xs:enumeration value="{html.escape(v)}"/>' for v in values)
    restr = f'    <xs:restriction base="xs:string">\n{enums}\n    </xs:restriction>'
    if OPEN:
        inner = (f'    <xs:union memberTypes="xs:string">\n'
                 f'      <xs:simpleType>\n{restr}\n      </xs:simpleType>\n'
                 f'    </xs:union>')
    else:
        inner = restr
    return (f'  <xs:simpleType name="{name}">\n'
            f'    <xs:annotation><xs:documentation>{html.escape(doc)} — {len(values)} values, injected by FS25_ResearchProject</xs:documentation></xs:annotation>\n'
            f'{inner}\n'
            f'  </xs:simpleType>')

xsd = open(SRC, encoding="utf-8").read()

# 1. Insert named simpleTypes right after the <xs:schema ...> opening tag
block = "\n".join(simpletype_xml(k, v[0], v[1]) for k, v in TYPES.items())
xsd, nins = re.subn(r'(<xs:schema\b[^>]*>)', r'\1\n' + block.replace('\\', r'\\'), xsd, count=1)
assert nins == 1, "schema open tag not found"

# 2. Re-type the target attributes
counts = {}
for attr, oldtype, newtype in ATTR_MAP:
    # allow other attributes between name="..." and type="..." within the same tag
    pat = r'(<xs:attribute name="%s"[^>]*?) type="%s"' % (re.escape(attr), re.escape(oldtype))
    xsd, n = re.subn(pat, r'\1 type="%s"' % newtype, xsd)
    counts[attr] = n

# 2b. Re-type enum-valued ELEMENTS (text content), e.g. storeData <category>
ELEM_MAP = [('category', 'g_string', 'fs25_storeCategory')]
for el, oldtype, newtype in ELEM_MAP:
    pat = r'(<xs:element name="%s"[^>]*?) type="%s"' % (re.escape(el), re.escape(oldtype))
    xsd, n = re.subn(pat, r'\1 type="%s"' % newtype, xsd)
    counts["<%s>" % el] = n

# 3. validate it still parses as XML
try:
    ET.fromstring(xsd)
    valid = "OK (well-formed XML)"
except ET.ParseError as e:
    valid = "PARSE ERROR: " + str(e)

os.makedirs(os.path.join(PROJ, "schemas"), exist_ok=True)
dst = os.path.join(PROJ, "schemas", "vehicle.xsd")
open(dst, "w", encoding="utf-8").write(xsd)

print("Mode:", "OPEN union" if OPEN else "STRICT enumeration")
print("Named types inserted:", len(TYPES))
print("Attribute re-types:")
for a, n in counts.items():
    flag = "" if n else "   <-- 0! check type token"
    print(f"  {a:24} x{n}{flag}")
print("XML validity:", valid)
print("Wrote", dst, "(%.0f KB)" % (len(xsd)/1024))
