# Changelog

## 0.3.0
- **Hosted schemas / portable refs.** New `fs25xml.schemaBaseUrl` (defaults to the public
  raw.githubusercontent.com/206airmail/FS25_ResearchProject/main/schemas). Repoint/bind/insert
  now write `https://` schema refs that Red Hat XML downloads + caches — so your mod XML stays
  machine-independent and distributable (no local absolute paths). Clear the URL to use a local
  `fs25xml.schemaDir` instead. Requires `xml.downloadExternalResources.enabled` (on by default).

## 0.2.0
- **Repoint stock schema refs.** GIANTS templates ship an `xsi:noNamespaceSchemaLocation`
  pointing at the stock schema — either a relative `…/shared/xml/schema/X.xsd` (varying depth)
  or the online `https://validation.gdn.giants-software.com/xml/fs25/X.xsd`. That in-file ref
  overrides binding, so the enriched schema never applied. New behavior rewrites those refs to
  the enriched copy, **keeping the type they name** (e.g. `map.xml` stays `mission00.xsd`).
- Command **“FS25: Repoint all stock schema refs in workspace to enriched”** (one click per mod,
  with a confirm prompt). Files with no ref still bind via `xml.fileAssociations`.
- New settings: `fs25xml.autoRepointOnOpen` (default off) and `fs25xml.schemaDir` (use a stable
  schemas path so repointed refs survive extension updates).
- List-valued attributes (`fillTypeCategories`, `fillTypes`, `fruitTypes`) now complete/validate
  each space-separated token; added registries groundType, treeType, animalType + fill/material/
  input aliases (~2,280 enriched attribute locations, 26 strict-enriched types).

## 0.1.0
- Initial release.
- Bundles all ~88 GIANTS 1.19.0.0 XSD schemas, value-enriched with registry value-sets
  (jointType, fillType, fruitType, particleType, effectClass, rigidBodyType, inputAction,
  brand, store category, material templates).
- Auto-binds the matching schema to FS25 XML files by filename / root element via
  `xml.fileAssociations` (no file modification).
- Commands to bind current file / whole workspace, and to insert an `xsi` schema reference.
- FS25 snippets (modDesc, attacherJoint, inputAttacherJoint, fillUnit, storeData).
