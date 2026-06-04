# FS25 XML autocomplete + validation in VS Code

This gives you, while editing a vehicle XML:
- **Tag completion** — only valid child tags are suggested
- **Attribute completion** — valid attributes per tag, with type + description on hover
- **Value completion** — dropdowns of valid values for the registry-backed keys
  (`jointType`, `fillType`, `fruitType`, `particleType`, `effectClass`,
  `rigidBodyTypeActive/Inactive`, `inputAction`, brand, `materialTemplateName`,
  store `<category>`) — the values the stock docs hide
- **Validation/linting** — red squiggles for unknown tags, wrong attribute types,
  missing required attributes, and out-of-range enum values

No custom plugin required — it's the mature **Red Hat XML** extension reading an
**enriched copy of the game's own `vehicle.xsd`**.

## One-time setup

1. **Install the extension:** `redhat.vscode-xml` (VS Code will prompt you because
   `.vscode/extensions.json` recommends it). Requires Java, which the extension
   bundles/installs automatically.

2. **Attach the schema** to your vehicle XML — pick one:

   **Option A — per file (exact, recommended).** Add to the root `<vehicle>` element:
   ```xml
   <vehicle xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:noNamespaceSchemaLocation="D:/Users/brown/Documents/Modding/FS25_ResearchProject/schemas/vehicle.xsd">
   ```
   (Use a relative path if your mod lives near this folder.) This is exactly how
   GIANTS' own `data/**` XML files reference their schemas.

   **Option B — workspace glob.** Edit `.vscode/settings.json` →
   `xml.fileAssociations` so the `pattern` matches *only* your vehicle files
   (it currently assumes a `vehicles/` folder). Don't bind `**/*.xml` to
   `vehicle.xsd` — other XML types (placeable, modDesc, map) would all show false
   errors.

3. Open a vehicle XML and start typing `jointType="` → the 22 joint types appear.

## What's enriched vs stock

`schemas/vehicle.xsd` is the stock 1.19.0.0 schema with 10 value-sets injected as
named types (`fs25_jointType`, `fs25_fillType`, …). Regenerate after a patch with
`tools/enrich_xsd.py`.

- **Strict mode (default):** unknown values are flagged as errors — great for
  catching typos. Because maps/mods can register *new* fill types / brands / etc.,
  a legitimate mod-added value would also be flagged. If that bothers you, set
  `OPEN = True` at the top of `tools/enrich_xsd.py` and regenerate: values become a
  `union` with `xs:string`, so they're *suggested* but never error.

- **Not enriched (left as stock):** `sprayType` (it's an integer index, not a name),
  and the space-separated **list** attributes `fillTypes` / `fillTypeCategories`
  (a list-of-enum is finicky for completion). `workArea@type` shares the name
  `type` with many unrelated attributes, so it can't be safely bound by name alone —
  it needs per-path targeting (a later refinement).

## Other XML types (placeable, map, fillTypes, …)

The game ships an `.xsd` for all ~88 XML types under
`…/Farming Simulator 25/shared/xml/schema/`. Reference any of them via
`xsi:noNamespaceSchemaLocation` for **structural** autocomplete + validation today —
no enrichment needed. The value-level enrichment in this project currently covers
`vehicle.xsd`; the same `tools/enrich_xsd.py` approach generalizes to the others
(e.g. `fillType` appears in placeable XML too).
