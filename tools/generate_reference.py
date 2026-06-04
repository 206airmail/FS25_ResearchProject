import json, os, collections, textwrap

CLAUDE = r"D:\Users\brown\Documents\Modding\ClaudeDir"
PROJ   = r"D:\Users\brown\Documents\Modding\FS25_ResearchProject"

enums = json.load(open(os.path.join(CLAUDE, "vehicle_enums.json"), encoding="utf-8"))
reg   = json.load(open(os.path.join(CLAUDE, "registries.json"), encoding="utf-8"))

L = []
def w(s=""): L.append(s)

def cols(items, per=6, code=True):
    """Render a list as comma-joined wrapped lines inside a code fence."""
    items = list(items)
    if code: w("```")
    line = []
    for i, it in enumerate(items):
        line.append(it)
        if len(line) == per:
            w(", ".join(line) + ",")
            line = []
    if line:
        w(", ".join(line))
    if code: w("```")

w("# Farming Simulator 25 — Vehicle XML Complete Value Reference")
w()
w("> Companion to `shared/xml/documentation/vehicle.html`. That file lists every valid **tag** and **attribute** for a vehicle XML, but for many attributes it only shows the *default* value (e.g. it documents `attacherJoint#jointType` as `Type: String, Default: implement` and never reveals the other 21 joint types). This document fills that gap: the **complete set of valid values** for every enumerated/registry-backed vehicle-XML key, extracted directly from the game's schema, data files, and decompiled Lua.")
w()
w("**Game version:** 1.19.0.0 (descVersion 109)  ")
w("**Generated from:**")
w("- `shared/xml/schema/vehicle.xsd` — schema-carried `xs:enumeration` value sets")
w("- `data/maps/maps_*.xml`, `data/shared/**`, `dataS/*.xml` — registry data files")
w("- `dataS/scripts/**` — decompiled Lua registration calls")
w("- `ClaudeDir/dlcs/*` — unpacked DLC packs (additions labeled per pack)")
w()
w("**Two kinds of values:**")
w("1. **Schema-defined enums (Part 1)** — the XSD itself constrains the value to a fixed list. The HTML *sometimes* shows these inline and sometimes doesn't.")
w("2. **Registry-backed strings (Part 2)** — the XSD types the attribute as a free `g_string`, but the game only accepts values that were registered in a data file or Lua at load time. **This is the `jointType` problem.** These sets are *extensible*: maps, DLCs, and mods can register more at runtime, so the lists below are the **base-game + unpacked-DLC** baseline.")
w()
w("---")
w()

# ============ PART 1 ============
w("## Part 1 — Schema-defined enums (from `vehicle.xsd`)")
w()
w(f"{len(enums)} enum-constrained attribute locations across the vehicle XML, collapsing to the distinct value-sets below. Each block lists the attribute(s) that use the set, the default (if any), and the full value list.")
w()

groups = collections.defaultdict(list)
for r in enums:
    groups[tuple(sorted(r["values"]))].append(r)

# sort: by number of values desc, then by usage count desc
for key, rs in sorted(groups.items(), key=lambda kv:(-len(kv[0]), -len(kv[1]))):
    attr_labels = sorted(set(r["attr"] for r in rs))
    # representative paths (unique), cap at 6
    paths = sorted(set(r["path"] for r in rs))
    default = next((r["default"] for r in rs if r["default"]), None)
    doc = next((r["doc"] for r in rs if r["doc"]), "")
    label = ", ".join(f"`{a}`" for a in attr_labels)
    w(f"### {label}  ({len(key)} values)")
    if doc:
        w(f"*{doc}*  ")
    if default:
        w(f"**Default:** `{default}`  ")
    w(f"**Used at {len(rs)} location(s):** " + ("; ".join(f"`{p}`" for p in paths[:6]) + (" …" if len(paths)>6 else "")))
    w()
    cols(key, per=6)
    w()

w("---")
w()

# ============ PART 2 ============
w("## Part 2 — Registry-backed string values (the `jointType` gap)")
w()
w("These attributes are typed `String` in the docs but only accept registered values. Source file and base/DLC origin noted per registry.")
w()

def section(title, vehicle_keys, source, values, note=None, per=6, dlc=None, caseins=False):
    w(f"### {title}")
    w(f"**Vehicle-XML key(s):** {vehicle_keys}  ")
    w(f"**Source:** `{source}`  ")
    w(f"**Count:** {len(values)} (base game)" + (f" + DLC additions below" if dlc else ""))
    if caseins:
        w("**Case-insensitive** — the game upper/normalizes the XML string before lookup.  ")
    w()
    if note:
        w(note); w()
    cols(values, per=per)
    w()
    if dlc:
        for pack, vals in dlc.items():
            if vals:
                w(f"**+ `{pack}` DLC adds {len(vals)}:**")
                cols(vals, per=per)
                w()

# jointType
section("`jointType` — attacher joint type",
        "`attacherJoint#jointType`, `inputAttacherJoint#jointType` (and combine/cutter joints)",
        "dataS/scripts/vehicles/specializations/AttacherJoints.lua (AttacherJoints.registerJointType)",
        reg["jointType"],
        note="The int value of each = registration order (implement=1 … train=22). Default when omitted: `implement`. Mods can register more via `AttacherJoints.registerJointType`.")

# fillType
fill_base = reg["fillType"]["__base__"]
fill_dlc = {k:v for k,v in reg["fillType"].items() if k != "__base__"}
section("`fillType` / `fillTypes` — fill type names",
        "`#fillType`, `<fillTypes>` lists, fillUnit/discharge/sprayer fill refs (≈43 spots)",
        "data/maps/maps_fillTypes.xml",
        fill_base,
        note="Case-sensitive UPPERCASE names. Maps and mods add their own fill types; these are the base-game set. Names are also what `densityMapHeightType`, `fillTypeCategory` membership, and most fill-unit refs use.",
        per=6, dlc=fill_dlc)

# fillTypeCategory
section("`fillTypeCategories` — fill type category names",
        "`#fillTypeCategories` (space-separated list; expands to member fill types)",
        "data/maps/maps_fillTypes.xml → <fillTypeCategories>",
        reg["fillTypeCategory"],
        note="Use these as shorthand for a group of fill types (e.g. `BULK`, `LIQUID`). They expand to their member `fillType`s.")

# fruitType
section("`fruitType` — fruit (crop) type names",
        "`#fruitType`, cutter/header `<fruitTypes>`, fruitPreparer, planter refs",
        "data/maps/maps_fruitTypes.xml → data/foliage/<crop>/<crop>.xml",
        reg["fruitType"]["__base__"],
        note="Registered names are camelCase (`sugarBeet`, `riceLongGrain`), **but lookups are case-insensitive** — base vehicle XML uses both `GRAPE` and `canola`. 25 base crops.",
        caseins=True)

# sprayType
section("`sprayType` — sprayer/spreader spray types",
        "`sprayer#sprayType`, spray fill conversions",
        "data/maps/maps_sprayTypes.xml",
        reg["sprayType"]["__base__"])

# densityMapHeightType
section("`densityMapHeightType` (by `fillTypeName`) — heap/tip height types",
        "tip/heap height refs keyed by fill type name",
        "data/maps/maps_densityMapHeightTypes.xml",
        reg["densityMapHeightType"],
        note="These are the fill types that have a defined physical heap/height profile (what can be tipped into a heap). Keyed by `fillTypeName`.")

# workAreaType
section("`workArea#type` — work area types",
        "`workAreas.workArea#type`",
        "dataS/scripts/vehicles/**/*.lua (g_workAreaTypeManager:addWorkAreaType)",
        reg["workAreaType"],
        note="Default when omitted: `default`.")

# rigidBodyType
section("`rigidBodyTypeActive` / `rigidBodyTypeInactive` — physics body type",
        "objectChange `#rigidBodyTypeActive`, `#rigidBodyTypeInactive`",
        "engine enum RigidBodyType (parsed via RigidBodyType[string.upper(str)] in ObjectChangeUtil.lua)",
        reg["rigidBodyType"],
        caseins=True)

# particleType
section("`particleType` — particle system type",
        "particle/effect `#particleType`",
        "dataS/scripts/materials/ParticleSystemManager.lua (addParticleType)",
        reg["particleType"])

# effectClass
section("`effectClass` — effect implementation class",
        "`effectNode#effectClass`, `<effects>` entries",
        "dataS/scripts/effects/*.lua (resolved via ClassUtil.getClassObject — any loaded Effect subclass)",
        reg["effectClass"],
        note="**Open set.** Unlike the others, `effectClass` accepts ANY globally-registered class derived from `Effect`. Below are the base-game Effect subclasses; mods can add more (referenced as `ModName.MyEffect`). Default: `ShaderPlaneEffect`.")

# connection hoses
w("### Connection hoses — `connectionHoses` registry")
w("**Source:** `data/shared/connectionHoses/connectionHoses.xml` (g_connectionHoseManager)  ")
w()
w(f"**`connectionHoseType` / hose `#type` ({len(reg['connectionHoseType'])}):**")
cols(reg["connectionHoseType"], per=4)
w()
w(f"**`adapter#name` / adapterType ({len(reg['connectionHose_adapter'])}):** " + ", ".join(f"`{x}`" for x in reg["connectionHose_adapter"]))
w()
w(f"**`socket#name` ({len(reg['connectionHose_socket'])}):**")
cols(reg["connectionHose_socket"], per=4)
w()
w(f"**`material#name` ({len(reg['connectionHose_material'])}):** " + ", ".join(f"`{x}`" for x in reg["connectionHose_material"]))
w()

# input actions
section("`inputAction` / input binding names",
        "`#inputAction`, `actionBinding`, `<inputAttacherJoint>` action refs",
        "dataS/inputActions.xml",
        reg["inputAction"],
        note="Base-game input action names. Mods register their own via modDesc `<inputBinding>`.", per=5)

# brands
dlc_brands = reg.get("brand_dlc") or {}
section("`vehicleBrand` / `brand` — brand id",
        "`storeData.brand`, brand-keyed material templates",
        "dataS/brands.xml",
        reg["brand"],
        note="No DLC-exclusive brands were found in the unpacked packs — DLC vehicles reuse these base ids. `NONE` is the unbranded sentinel.", per=6,
        dlc=dlc_brands if dlc_brands else None)

# store categories
w("### `storeData.category` — shop categories")
w("**Source:** `dataS/storeCategories.xml`  ")
w()
w(f"**Category *types* (top-level grouping, {len(reg['storeCategoryType'])}):**")
cols(reg["storeCategoryType"], per=5)
w()
w(f"**Category names (what a vehicle's `<category>` uses, {len(reg['storeCategory'])}):**")
cols(reg["storeCategory"], per=5)
w()

# material templates
w("### `materialTemplateName` / `defaultColorMaterialTemplateName` — material templates")
w("**Source:** `data/shared/detailLibrary/materialTemplates.xml` (generic) + `data/shared/brandMaterialTemplates.xml` (brand colors)  ")
w()
w("> Note: `materialSlotName` is **not** an enum — it is an arbitrary per-model material slot name baked into each vehicle's i3d, so there is no global list. `materialTemplateName` IS a closed registry, below.")
w()
w(f"**Generic material templates ({len(reg['materialTemplate_base'])}):**")
cols(reg["materialTemplate_base"], per=4)
w()
w(f"**Brand color templates ({len(reg['materialTemplate_brand'])})** — naming pattern `BRAND_COLORn`. Grouped by brand prefix:")
w()
bt = collections.defaultdict(list)
for t in reg["materialTemplate_brand"]:
    prefix = t.split("_")[0] if "_" in t else t
    bt[prefix].append(t)
w("<details><summary>Expand full brand-color template list (%d)</summary>" % len(reg["materialTemplate_brand"]))
w()
for prefix in sorted(bt):
    w(f"**{prefix}** ({len(bt[prefix])}): " + ", ".join(f"`{x}`" for x in bt[prefix]))
w()
w("</details>")
w()

w("---")
w()
w("## Caveats & methodology")
w()
w("- **Extensibility:** Part 2 sets are the base-game + unpacked-DLC baseline. Any installed **map** or **mod** can register additional `fillType`, `fruitType`, `sprayType`, `jointType`, `brand`, `inputAction`, `effectClass`, etc. at load time. Always treat these as \"valid unless the active modset adds more.\"")
w("- **Case sensitivity:** `fillType`/`sprayType`/`fillTypeCategory`/`densityMapHeightType` are UPPERCASE and matched as written. `fruitType` and `rigidBodyType` are normalized, so case doesn't matter. `jointType`/`workAreaType`/`particleType`/connection-hose names are lowercase/camelCase as written.")
w("- **`effectClass` is an open set** resolved by class name at load — not a fixed registry.")
w("- **`materialSlotName` is intentionally omitted as an enum** — it's per-model, not a registry.")
w("- All Part 2 values were extracted directly from the cited source files and cross-checked against actual usage in `data/vehicles/**`, not transcribed by hand.")

md = "\n".join(L) + "\n"
os.makedirs(PROJ, exist_ok=True)
with open(os.path.join(PROJ, "Vehicle_XML_Value_Reference.md"), "w", encoding="utf-8") as f:
    f.write(md)
print("Wrote reference:", len(md), "chars,", md.count("\n"), "lines")
