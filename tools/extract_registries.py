import re, os, glob, json, xml.etree.ElementTree as ET

GAME = r"D:\SteamLibrary\steamapps\common\Farming Simulator 25\data"
DATAS = r"D:\Users\brown\Documents\Modding\ClaudeDir\dataS"
DLCS  = r"D:\Users\brown\Documents\Modding\ClaudeDir\dlcs"

out = {}

def read(p):
    with open(p, "r", encoding="utf-8-sig", errors="replace") as f:
        return f.read()

def attrs(text, tag, attr="name"):
    return re.findall(r'<%s\b[^>]*\b%s="([^"]*)"' % (tag, attr), text)

# ---------- fillTypes (base + DLC) ----------
fill = {}
base_fill = attrs(read(os.path.join(GAME, "maps", "maps_fillTypes.xml")), "fillType")
fill["__base__"] = base_fill
for dlc_xml in glob.glob(os.path.join(DLCS, "*", "fillTypes.xml")) + glob.glob(os.path.join(DLCS, "*", "*fillTypes*.xml")):
    name = os.path.basename(os.path.dirname(dlc_xml))
    fill[name] = attrs(read(dlc_xml), "fillType")
out["fillType"] = fill

# fillTypeCategories (inside maps_fillTypes.xml)
fcat = re.findall(r'<fillTypeCategory\s+name="([^"]*)"', read(os.path.join(GAME, "maps", "maps_fillTypes.xml")))
out["fillTypeCategory"] = fcat

# ---------- fruitTypes (read each referenced foliage xml for its registered name) ----------
ft_text = read(os.path.join(GAME, "maps", "maps_fruitTypes.xml"))
fruit_files = re.findall(r'<fruitType\s+filename="([^"]*)"', ft_text)
fruit_names = []
for ff in fruit_files:
    path = ff.replace("$data", GAME).replace("/", os.sep)
    nm = None
    if os.path.isfile(path):
        m = re.search(r'<fruitType[^>]*\bname="([^"]*)"', read(path))
        if m: nm = m.group(1)
    if nm is None:
        # fall back to filename stem upper-cased
        nm = os.path.splitext(os.path.basename(ff))[0].upper()
    fruit_names.append(nm)
out["fruitType"] = {"__base__": fruit_names}
# DLC fruit
for dlc_xml in glob.glob(os.path.join(DLCS, "*", "fruitTypes.xml")):
    name = os.path.basename(os.path.dirname(dlc_xml))
    files = re.findall(r'<fruitType\s+filename="([^"]*)"', read(dlc_xml))
    out["fruitType"][name] = [os.path.splitext(os.path.basename(f))[0].upper() for f in files]

# ---------- sprayTypes ----------
sp = os.path.join(GAME, "maps", "maps_sprayTypes.xml")
out["sprayType"] = {"__base__": attrs(read(sp), "sprayType")} if os.path.isfile(sp) else {}
for dlc_xml in glob.glob(os.path.join(DLCS, "*", "sprayTypes.xml")):
    out["sprayType"][os.path.basename(os.path.dirname(dlc_xml))] = attrs(read(dlc_xml), "sprayType")

# ---------- densityMapHeightTypes (keyed by fillTypeName) ----------
dh = os.path.join(GAME, "maps", "maps_densityMapHeightTypes.xml")
out["densityMapHeightType"] = re.findall(r'<densityMapHeightType\s+fillTypeName="([^"]*)"', read(dh)) if os.path.isfile(dh) else []

# ---------- brands ----------
out["brand"] = attrs(read(os.path.join(DATAS, "brands.xml")), "brand")
# DLC brands
for dlc_xml in glob.glob(os.path.join(DLCS, "*", "brands.xml")):
    out.setdefault("brand_dlc", {})[os.path.basename(os.path.dirname(dlc_xml))] = attrs(read(dlc_xml), "brand")

# ---------- store categories (types + category names, any attr order) ----------
sc_text = read(os.path.join(DATAS, "storeCategories.xml"))
out["storeCategoryType"] = re.findall(r'<type\s+name="([^"]*)"', sc_text)
def name_anyorder(text, tag):
    res = []
    for m in re.finditer(r'<%s\b[^>]*>' % tag, text):
        nm = re.search(r'\bname="([^"]*)"', m.group(0))
        if nm: res.append(nm.group(1))
    return res
out["storeCategory"] = name_anyorder(sc_text, "category")

# ---------- input actions ----------
out["inputAction"] = attrs(read(os.path.join(DATAS, "inputActions.xml")), "action")

# ---------- material templates ----------
out["materialTemplate_base"] = attrs(read(os.path.join(GAME, "shared", "detailLibrary", "materialTemplates.xml")), "template")
bmt = read(os.path.join(GAME, "shared", "brandMaterialTemplates.xml"))
out["materialTemplate_brand"] = attrs(bmt, "template")

# ---------- connection hoses ----------
ch = read(os.path.join(GAME, "shared", "connectionHoses", "connectionHoses.xml"))
out["connectionHoseType"] = attrs(ch, "connectionHoseType")
out["connectionHose_adapter"] = sorted(set(attrs(ch, "adapter")))
out["connectionHose_socket"] = attrs(ch, "socket")
out["connectionHose_material"] = sorted(set(attrs(ch, "material")))

# ---------- jointType (AttacherJoints) ----------
aj = read(os.path.join(DATAS, "scripts", "vehicles", "specializations", "AttacherJoints.lua"))
out["jointType"] = re.findall(r'registerJointType\("([^"]+)"', aj)

# ---------- workAreaType ----------
wat = []
for f in glob.glob(os.path.join(DATAS, "scripts", "**", "*.lua"), recursive=True):
    wat += re.findall(r'addWorkAreaType\("([^"]+)"', read(f))
out["workAreaType"] = sorted(set(wat))

# ---------- particleType ----------
pt = read(os.path.join(DATAS, "scripts", "materials", "ParticleSystemManager.lua"))
out["particleType"] = re.findall(r'addParticleType\("([^"]+)"', pt)

# ---------- effect classes (open set: any Effect subclass) ----------
eff = set()
for f in glob.glob(os.path.join(DATAS, "scripts", "effects", "*.lua")):
    txt = read(f)
    # Class(X, Effect) or Class(X, SomethingEffect)
    for m in re.finditer(r'(\w+)\s*=\s*\{\}\s*\n\s*local\s+\w+_mt\s*=\s*Class\((\w+)\s*,\s*(\w+)\)', txt):
        if "Effect" in m.group(1) or "Effect" in m.group(3):
            eff.add(m.group(1))
    for m in re.finditer(r'Class\((\w+),\s*(\w+Effect\w*)\)', txt):
        eff.add(m.group(1)); eff.add(m.group(2))
out["effectClass"] = sorted(e for e in eff if ("Effect" in e and e != "EffectManager"))

# ---------- rigidBodyType ----------
out["rigidBodyType"] = ["NONE", "STATIC", "DYNAMIC", "KINEMATIC"]

# Save
with open(os.path.join(r"D:\Users\brown\Documents\Modding\ClaudeDir", "registries.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2)

# Print verification summary
def cnt(v):
    if isinstance(v, dict):
        return sum(len(x) for x in v.values())
    return len(v)
print("=== REGISTRY EXTRACTION SUMMARY ===")
for k, v in out.items():
    print(f"{k:28} -> {cnt(v)} values")
print()
print("fillType base count:", len(out["fillType"]["__base__"]))
print("fillType DLC keys:", [k for k in out["fillType"] if k!="__base__"])
print("fruitType base:", out["fruitType"]["__base__"])
print("fillTypeCategory:", out["fillTypeCategory"])
print("sprayType:", out["sprayType"])
print("densityMapHeightType:", out["densityMapHeightType"])
print("jointType (%d):" % len(out["jointType"]), out["jointType"])
print("workAreaType (%d):" % len(out["workAreaType"]), out["workAreaType"])
print("particleType (%d):" % len(out["particleType"]), out["particleType"])
print("effectClass (%d):" % len(out["effectClass"]), out["effectClass"])
print("connectionHoseType (%d):" % len(out["connectionHoseType"]), out["connectionHoseType"])
print("storeCategoryType (%d):" % len(out["storeCategoryType"]), out["storeCategoryType"])
print("storeCategory (%d):" % len(out["storeCategory"]), out["storeCategory"])
print("densityMapHeightType (%d):" % len(out["densityMapHeightType"]), out["densityMapHeightType"])
print("brand count:", len(out["brand"]), "| brand_dlc:", out.get("brand_dlc"))
print("materialTemplate_base (%d)" % len(out["materialTemplate_base"]))
print("materialTemplate_brand (%d)" % len(out["materialTemplate_brand"]))
print("inputAction count:", len(out["inputAction"]))
