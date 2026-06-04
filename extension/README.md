# FS25 XML — Farming Simulator 25 modding support for VS Code

Autocomplete + validation for **all ~88 Farming Simulator 25 XML types** (vehicle,
placeable, map, modDesc, fillTypes, handTool, …), including **valid-value dropdowns
the stock GIANTS docs hide** — `jointType`, `fillType`, `fruitType`, `particleType`,
`effectClass`, `rigidBodyType`, `inputAction`, `brand`, store `category`, and material
templates.

It bundles the GIANTS 1.19.0.0 schemas **enriched** with those value-sets (extracted
from the game's `data`, `dataS`, and unpacked DLCs) and wires them to your files through
the [Red Hat XML extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml),
which does the actual completion/validation. (That extension is installed automatically
as a dependency.)

## How it works

When you open an FS25 XML file, the extension figures out which type it is — by filename
(e.g. `*fillTypes*.xml`) or by root element (`<vehicle>`, `<placeable>`, …) — and binds
the matching bundled schema via the `xml.fileAssociations` setting. **Your XML file is not
modified.** Red Hat XML then gives you:

- valid child-tag and attribute completion
- value dropdowns for the registry-backed keys (type `jointType="` → 22 options)
- red squiggles for unknown tags, wrong types, missing required attributes, bad enum values

## Commands

- **FS25: Bind schema to current XML file**
- **FS25: Bind schemas to all XML in workspace**
- **FS25: Insert xsi schema reference into current file** — writes the FS25-native
  `xsi:noNamespaceSchemaLocation` onto the root element (portable, file-local alternative)

## Settings

- `fs25xml.autoBindOnOpen` (default `true`) — auto-bind the right schema on open.

## Notes

- **Strict value validation:** unknown enum values are flagged (great for typos). Because
  maps/mods can register *new* fill types, brands, etc., a legitimate mod-added value may
  also be flagged — see the project's `tools/enrich_all_xsd.py` (`OPEN=True`) to rebuild
  the schemas in permissive (suggest-only) mode.
- Value-enriched types: vehicle, placeable, handTool, feedingRobot, ferry, wheel, crawler,
  fillTypes, foliageType, weed, modDesc, and more. All other types still get full
  structural autocomplete + validation from their stock schema.
- Regenerate schemas after a game patch with the project's `tools/` scripts.

MIT licensed. Schemas © GIANTS Software, redistributed for modding convenience.
