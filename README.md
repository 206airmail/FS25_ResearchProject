# FS25 Research Project — XML value reference, browser & VS Code tooling

The **complete set of valid values** for every enumerated / registry-backed key across
**all ~88 Farming Simulator 25 XML types**, plus tooling to actually use them: a fast
all-types browser and a VS Code extension that gives autocomplete + validation.

## Why this exists

The game ships `shared/xml/documentation/*.html` — every valid **tag** and **attribute**
per XML type — but for many attributes it only shows the *default* value. It documents
`attacherJoint#jointType` as `Type: String, Default: implement` and never reveals the
other 21 joint types; same story for `fillType`, `fruitType`, brands, and dozens more.
Those value sets live in the game's `data`, `dataS`, and DLCs, not the docs. This project
extracts them and makes them usable.

## Architecture — one SQLite DB, three consumers

```
   game schemas + data + dataS + DLCs
                 │  tools/extract_*.py, build_db.py
                 ▼
        data/fs25_xml.db   ← single source of truth (4.9 MB, 88 types,
                 │           11.5k nodes, 31k attrs, 52 deduped value-sets)
        ┌────────┼─────────────────────────┐
        ▼        ▼                          ▼
   EDIT       BROWSE                     LOOK UP
 extension/   fs25_xml_browser.html      Vehicle_XML_Value_Reference.md
 (.vsix)      (2.5 MB, all 88 types)     (markdown, grep/Ctrl-F)
```

## Deliverables — pick the format for the task

| Want to… | Use | File |
|----------|-----|------|
| **Edit any FS25 XML with autocomplete + validation** | VS Code extension | `extension/fs25-xml-0.1.0.vsix` |
| **Browse all 88 types** — collapse, search tag/attr/value | unified browser | `fs25_xml_browser.html` |
| **Ctrl-F / grep** a value list (vehicle) | markdown | `Vehicle_XML_Value_Reference.md` |
| **Query programmatically** | SQLite DB | `data/fs25_xml.db` |
| Manual schema setup (no extension) | enriched schema + Red Hat XML | `schemas/vehicle.xsd` + `schemas/VSCODE_SETUP.md` |
| Values in the game's own doc layout (tooltips) | enriched game HTML | `vehicle_annotated.html` |

### VS Code extension (`extension/fs25-xml-0.1.0.vsix`)
Install: `code --install-extension extension/fs25-xml-0.1.0.vsix` (or Extensions panel →
"Install from VSIX…"). It bundles all 88 GIANTS 1.19 schemas **value-enriched** with the
registry value-sets, auto-binds the right one per file (by filename / root element), and
leans on the Red Hat XML extension (auto-installed) for completion + linting. Type
`jointType="` and get all 22 options; misspell a `fillType` and get a red squiggle.
Source is in `extension/` — repackage with `npx @vscode/vsce package`.

### Unified browser (`fs25_xml_browser.html`)
One self-contained, double-clickable file for **all 88 types**: left sidebar of types
(with attribute / enriched counts), per-type collapsible tree (collapsed by default), live
search over tags + attributes + values, value lists inline. 2.5 MB total — vs the game's
19 MB for a *single* type — because the DB tree is deduped.

### The DB (`data/fs25_xml.db`)
Canonical store. Tables: `types`, `nodes` (element tree), `attrs` (name, type, default,
doc, valueset), `valuesets` (deduped). Everything else is generated from it.

## Reproducibility

```sh
python tools/extract_vehicle_enums.py   # vehicle.xsd enumerations  -> data/vehicle_enums.json
python tools/extract_registries.py      # data/dataS/DLC registries -> data/registries.json
python tools/build_db.py                # all 88 schemas            -> data/fs25_xml.db
python tools/enrich_all_xsd.py          # value-enriched schemas    -> extension/schemas/*.xsd
python tools/generate_db_browser.py     # all-types browser         -> fs25_xml_browser.html
python tools/generate_reference.py      # markdown reference (vehicle)
python tools/enrich_xsd.py              # standalone enriched vehicle.xsd (schemas/)
python tools/generate_annotated_html.py # game-HTML tooltips (vehicle)
# then: cd extension && npx @vscode/vsce package
```

## Source paths (machine-specific)

- Game data: `D:\SteamLibrary\steamapps\common\Farming Simulator 25\data`
- Schema/docs: `D:\SteamLibrary\steamapps\common\Farming Simulator 25\shared\xml`
- Decompiled Lua: `D:\Users\brown\Documents\Modding\ClaudeDir\dataS`
- Unpacked DLCs: `D:\Users\brown\Documents\Modding\ClaudeDir\dlcs`

## Caveats

- Value sets are the **base-game + unpacked-DLC** baseline; maps/DLCs/mods register more at
  load. Schemas are **strict** (flag typos) — set `OPEN=True` in `tools/enrich_all_xsd.py`
  for permissive (suggest-only) mode if mod-added values trip false errors.
- 25 of 88 types are value-enriched (where registries apply); the rest still get full
  **structural** autocomplete + validation from their stock schema. Registry value-sets:
  jointType, fillType (+ aliases incomingFillType/outgoingFillType/defaultFillType/to/from),
  fruitType, particleType, effectClass, rigidBodyType, inputAction (+inputBindingName), brand,
  storeCategory, materialTemplate (+color/rim aliases), groundType, treeType, animalType,
  connectionHoseType (+hoseType), adapterType. ~2,280 attribute locations across all types.
- Not enriched: `sprayType` (integer index), space-separated list attrs
  (`fillTypes`/`fillTypeCategories`/`fruitTypes` — shown in the browser but not strict-validated),
  `workArea@type`/`mountType`/`specType` (ambiguous or uncertain value sets).
- `effectClass` is an open set; `materialSlotName` is a per-model i3d name, not a registry.

Generated against game version **1.19.0.0** (descVersion 109).
Bundled schemas © GIANTS Software, redistributed for modding convenience.
