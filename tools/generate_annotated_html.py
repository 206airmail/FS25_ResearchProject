import re, json, os, html, collections

DOC = r"D:\SteamLibrary\steamapps\common\Farming Simulator 25\shared\xml\documentation\vehicle.html"
CLAUDE = r"D:\Users\brown\Documents\Modding\ClaudeDir"
PROJ = r"D:\Users\brown\Documents\Modding\FS25_ResearchProject"

enums = json.load(open(os.path.join(CLAUDE, "vehicle_enums.json"), encoding="utf-8"))
reg   = json.load(open(os.path.join(CLAUDE, "registries.json"), encoding="utf-8"))

# ---- Bucket A: exact (path, attr) -> values
A = {}
for r in enums:
    attr = r["attr"].lstrip("#")
    if r["attr"] == "(element text)":
        continue
    A[(r["path"], attr)] = r["values"]

# ---- Bucket A fallback: (last_element_name, attr) -> values, ONLY when unambiguous
#      (e.g. modifier#type is always the same 23-set; priority always the same 5;
#       but dashboard#valueType varies, so it is excluded automatically)
_byleaf = collections.defaultdict(list)
for r in enums:
    if r["attr"] == "(element text)":
        continue
    leaf = r["path"].split(".")[-1]
    _byleaf[(leaf, r["attr"].lstrip("#"))].append(tuple(r["values"]))
A_fb = {k: list(v[0]) for k, v in _byleaf.items() if len(set(v)) == 1}

# ---- Bucket B: attr-name -> (values, source-label)
def base(x): return x["__base__"] if isinstance(x, dict) else x
B = {
    "jointType":      (reg["jointType"], "AttacherJoints.registerJointType"),
    "fillType":       (base(reg["fillType"]), "maps_fillTypes.xml"),
    "fillTypes":      (base(reg["fillType"]), "maps_fillTypes.xml"),
    "fillTypeCategories": (reg["fillTypeCategory"], "maps_fillTypes.xml <fillTypeCategories>"),
    "fruitType":      (base(reg["fruitType"]), "maps_fruitTypes.xml (case-insensitive)"),
    "sprayType":      (base(reg["sprayType"]), "maps_sprayTypes.xml"),
    "particleType":   (reg["particleType"], "ParticleSystemManager.lua"),
    "effectClass":    (reg["effectClass"], "Effect subclasses (open set; mods add more)"),
    "rigidBodyTypeActive":   (reg["rigidBodyType"], "engine RigidBodyType (case-insensitive)"),
    "rigidBodyTypeInactive": (reg["rigidBodyType"], "engine RigidBodyType (case-insensitive)"),
    "inputAction":    (reg["inputAction"], "inputActions.xml"),
    "vehicleBrand":   (reg["brand"], "brands.xml"),
    "displayBrand":   (reg["brand"], "brands.xml"),
    "brand":          (reg["brand"], "brands.xml"),
    "category":       (reg["storeCategory"], "storeCategories.xml"),
    "subCategory":    (reg["storeCategory"], "storeCategories.xml"),
    "materialTemplateName": (reg["materialTemplate_base"] + reg["materialTemplate_brand"], "materialTemplates.xml + brandMaterialTemplates.xml"),
    "defaultColorMaterialTemplateName": (reg["materialTemplate_base"] + reg["materialTemplate_brand"], "material templates"),
    "materialTemplateNameColor": (reg["materialTemplate_base"] + reg["materialTemplate_brand"], "material templates"),
}
# path-qualified: workArea#type -> workAreaType
WORKAREA = reg["workAreaType"]

CAP = 30  # above this, truncate in the tooltip and point to the reference
def fmt_values(vals, source=None):
    vals = list(vals)
    n = len(vals)
    if n > CAP:
        shown = ", ".join(html.escape(v) for v in vals[:20])
        tail = f" … (+{n-20} more of {n} — see Vehicle_XML_Value_Reference.md)"
    else:
        shown = ", ".join(html.escape(v) for v in vals)
        tail = ""
    src = f" <i>[{html.escape(source)}]</i>" if source else ""
    return (f'<br><b style="color:#2a7">Values ({n}):</b> '
            f'<span style="color:#2a7">{shown}{tail}</span>{src}<br>')

text = open(DOC, encoding="utf-8").read()

# Combined scanner: element-open OR attribute-with-attrInfo, in document order
elem_re = re.compile(r'margin-left:(\d+)em"><span class="idTag">&lt;(\w+)')
attr_re = re.compile(r'<span class="idAttr">(\w+)</span>=<span class="idVal">"[^"]*"</span><span class="attrInfo">(.*?)</span>', re.S)
combined = re.compile(elem_re.pattern + "|" + attr_re.pattern, re.S)

stack = []  # stack[d] = element name at depth d
injections = []  # (insert_pos, text)
stats = collections.Counter()
matched_A = set()

for m in combined.finditer(text):
    if m.group(1) is not None:  # element open
        depth = int(m.group(1)) // 2
        name = m.group(2)
        del stack[depth:]
        # pad if needed
        while len(stack) < depth:
            stack.append("?")
        stack.append(name)
    else:  # attribute
        attr = m.group(3)
        inner = m.group(4)
        path = "vehicle." + ".".join(stack[1:]) if len(stack) > 1 else "vehicle." + (stack[0] if stack else "")
        # also a path that doesn't drop root, fallback
        vals = None; source = None
        key = (path, attr)
        leaf_key = (stack[-1] if stack else "", attr)
        if key in A:
            vals = A[key]; source = "schema enum"; stats["A"] += 1; matched_A.add(key)
        elif leaf_key in A_fb:
            vals = A_fb[leaf_key]; source = "schema enum"; stats["A_fb"] += 1
        elif attr in B:
            vals, source = B[attr]; stats["B"] += 1
        elif attr == "type" and stack and stack[-1] == "workArea":
            vals = WORKAREA; source = "workAreaType"; stats["workArea"] += 1
        if vals:
            # inject before the closing </span> of attrInfo => at end of inner
            inner_end = m.end(4)  # end of captured inner content (before </span>)
            injections.append((inner_end, fmt_values(vals, source)))

# Apply injections end->start
injections.sort(key=lambda x: -x[0])
out = text
for pos, ins in injections:
    out = out[:pos] + ins + out[pos:]

# Add a banner note near <body>
banner = ('<div style="background:#eef;border:1px solid #88a;padding:8px;margin:6px;font-family:sans-serif">'
          '<b>ENRICHED COPY</b> — value lists added to attribute tooltips by FS25_ResearchProject. '
          'Green <b>Values(n)</b> lines are injected; large sets (brands, categories, material templates) '
          'are truncated with a pointer to <code>Vehicle_XML_Value_Reference.md</code>. '
          'Base game 1.19.0.0 + unpacked DLCs.</div>')
out = re.sub(r'(<body[^>]*>)', r'\1' + banner, out, count=1)

os.makedirs(PROJ, exist_ok=True)
with open(os.path.join(PROJ, "vehicle_annotated.html"), "w", encoding="utf-8") as f:
    f.write(out)

print("Injections:", len(injections))
print("  Bucket A (schema, by exact path):", stats["A"], "/", len(A), "known A locations")
print("  Bucket B (registry, by name):", stats["B"])
print("  workArea#type:", stats["workArea"])
print("Unmatched A locations:", len(set(A) - matched_A))
miss = sorted(set(A) - matched_A)[:15]
for k in miss:
    print("   MISS", k)
