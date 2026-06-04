import xml.etree.ElementTree as ET
import json, sys, collections

XSD = r"D:\SteamLibrary\steamapps\common\Farming Simulator 25\shared\xml\schema\vehicle.xsd"
NS = "{http://www.w3.org/2001/XMLSchema}"

def local(tag):
    return tag.split('}')[-1] if '}' in tag else tag

tree = ET.parse(XSD)
root = tree.getroot()

# results: list of dicts {path, attr, default, doc, values[]}
results = []

def get_doc(el):
    for ann in el.findall(NS+"annotation"):
        for doc in ann.findall(NS+"documentation"):
            if doc.text:
                return doc.text.strip()
    return ""

def enum_values(el):
    """If this xs:attribute/xs:element has an inline restriction with enumerations, return list."""
    st = el.find(NS+"simpleType")
    if st is None:
        return None
    restr = st.find(NS+"restriction")
    if restr is None:
        return None
    enums = restr.findall(NS+"enumeration")
    if not enums:
        return None
    return [e.get("value") for e in enums]

def walk(el, path):
    tag = local(el.tag)
    newpath = path
    if tag == "element":
        name = el.get("name")
        if name:
            newpath = path + [name]
    # check attributes defined at this level
    for child in el:
        ctag = local(child.tag)
        if ctag == "attribute":
            aname = child.get("name")
            vals = enum_values(child)
            if vals:
                results.append({
                    "path": ".".join(newpath) if newpath else "(root)",
                    "attr": "#"+(aname or "?"),
                    "default": child.get("default"),
                    "doc": get_doc(child),
                    "values": vals,
                })
        elif ctag == "element":
            # an element whose value (text) is an enum
            vals = enum_values(child)
            if vals:
                ename = child.get("name")
                ep = ".".join(newpath+[ename]) if ename else ".".join(newpath)
                results.append({
                    "path": ep,
                    "attr": "(element text)",
                    "default": child.get("default"),
                    "doc": get_doc(child),
                    "values": vals,
                })
            walk(child, newpath)
        else:
            walk(child, newpath)

walk(root, [])

print("Total enum-constrained attributes/elements found:", len(results))

# Group by the frozenset of values to dedupe identical enums
groups = collections.defaultdict(list)
for r in results:
    key = tuple(sorted(r["values"]))
    groups[key].append(r)

print("Distinct value-sets:", len(groups))

# Save full JSON
with open(r"D:\Users\brown\Documents\Modding\ClaudeDir\vehicle_enums.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

# Print summary: each distinct value-set, its size, # of attrs using it, sample attr names
sets_sorted = sorted(groups.items(), key=lambda kv: (-len(kv[0]), -len(kv[1])))
print("\n=== DISTINCT VALUE SETS (by size) ===")
for key, rs in sets_sorted:
    attrs = sorted(set((r["path"].split(".")[-1] if r["attr"]=="(element text)" else r["attr"]) for r in rs))
    # short attr label set
    attr_labels = sorted(set(r["attr"] for r in rs))
    print(f"\n[{len(key)} values, used by {len(rs)} attr-locations]")
    print("  attrs:", ", ".join(attr_labels[:12]) + (" ..." if len(attr_labels)>12 else ""))
    print("  values:", ", ".join(key))
