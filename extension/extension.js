// FS25 XML — points Farming Simulator 25 mod XML at the bundled value-enriched GIANTS
// schemas so the Red Hat XML extension (LemMinX) gives tag/attribute/value autocomplete
// + validation. Two mechanisms:
//   1) Files that already carry a stock `xsi:noNamespaceSchemaLocation="…/shared/xml/schema/X.xsd"`
//      (GIANTS templates do) — REPOINT that ref to the enriched X.xsd (keeps the type it names).
//   2) Files with no schema ref — bind via `xml.fileAssociations` (no file edit).
const vscode = require("vscode");
const path = require("path");
const fs = require("fs");

let BINDING = { byFilename: {}, byRoot: {} };
let SCHEMA_DIR_BUNDLED = "";

function loadBinding(context) {
  try { BINDING = JSON.parse(fs.readFileSync(context.asAbsolutePath("schema_binding.json"), "utf8")); }
  catch (e) { console.error("FS25 XML: schema_binding.json", e); }
  SCHEMA_DIR_BUNDLED = context.asAbsolutePath("schemas");
}
// Where the enriched schemas live. Override with fs25xml.schemaDir for a stable path
// (e.g. your FS25_ResearchProject/schemas) so refs survive extension updates.
function schemaDir() {
  const s = vscode.workspace.getConfiguration("fs25xml").get("schemaDir");
  return (s && s.trim()) ? s.trim() : SCHEMA_DIR_BUNDLED;
}
function fwd(p) { return p.replace(/\\/g, "/"); }
// Set of valid schema filenames (from the bundled schemas dir), used in both local & URL modes.
let VALID = null;
function validNames() {
  if (!VALID) { try { VALID = new Set(fs.readdirSync(SCHEMA_DIR_BUNDLED).filter(f => f.endsWith(".xsd"))); } catch (e) { VALID = new Set(); } }
  return VALID;
}
function schemaValid(name) { return name && validNames().has(name); }
// Public raw-URL base (portable refs) takes precedence over the local schemaDir if set.
function baseUrl() {
  const u = vscode.workspace.getConfiguration("fs25xml").get("schemaBaseUrl");
  return (u && u.trim()) ? u.trim().replace(/\/$/, "") : "";
}
function schemaTarget(name) {
  const b = baseUrl();
  return b ? (b + "/" + name) : (fwd(schemaDir()) + "/" + name);
}

function rootElement(text) {
  const c = text.replace(/<!--[\s\S]*?-->/g, "").replace(/<\?[\s\S]*?\?>/g, "");
  const m = c.match(/<([A-Za-z_][\w.\-]*)/);
  return m ? m[1] : null;
}
function pickSchema(doc) {
  if (!doc || doc.languageId !== "xml") return null;
  const base = path.basename(doc.fileName, ".xml").toLowerCase();
  const hints = Object.keys(BINDING.byFilename).sort((a, b) => b.length - a.length);
  for (const h of hints) if (base.includes(h.toLowerCase())) return BINDING.byFilename[h];
  const root = rootElement(doc.getText());
  if (root && BINDING.byRoot[root]) return BINDING.byRoot[root];
  return null;
}

// ---- (1) repoint stock refs -> enriched, preserving the type filename it already names ----
// Handles BOTH GIANTS ref styles:
//   relative file:  ../../../shared/xml/schema/vehicle.xsd
//   online URL:     https://validation.gdn.giants-software.com/xml/fs25/vehicle.xsd
const STOCK_RE = /(noNamespaceSchemaLocation=")([^"]*?(?:\/shared\/xml\/schema\/|validation\.gdn\.giants-software\.com\/xml\/fs25\/))([A-Za-z0-9_]+\.xsd)(")/g;
function repointText(text) {
  let n = 0;
  const out = text.replace(STOCK_RE, (m, p1, prefix, typeFile, p4) => {
    if (!schemaValid(typeFile)) return m;                 // unknown type → leave
    const target = schemaTarget(typeFile);
    if (prefix + typeFile === target) return m;           // already pointing at target
    n++; return p1 + target + p4;
  });
  return [out, n];
}
async function applyFullText(doc, out) {
  const edit = new vscode.WorkspaceEdit();
  edit.replace(doc.uri, new vscode.Range(doc.positionAt(0), doc.positionAt(doc.getText().length)), out);
  await vscode.workspace.applyEdit(edit);
  await doc.save();
}
async function repointDoc(doc, { silent } = {}) {
  const [out, n] = repointText(doc.getText());
  if (n > 0) await applyFullText(doc, out);
  if (!silent) vscode.window.showInformationMessage(
    n ? `FS25 XML: repointed ${n} schema ref(s) → enriched.` : "FS25 XML: no stock schema refs found in this file.");
  return n;
}

// ---- (2) bind files that have NO schema ref, via xml.fileAssociations (no edit) ----
async function bindIfNoRef(doc, { silent } = {}) {
  if (/noNamespaceSchemaLocation/.test(doc.getText())) return false; // has a ref → handled by repoint
  const schema = pickSchema(doc);
  if (!schemaValid(schema)) return false;
  const abs = schemaTarget(schema);
  const ws = vscode.workspace.getWorkspaceFolder(doc.uri);
  const pattern = ws ? vscode.workspace.asRelativePath(doc.uri, false) : fwd(doc.uri.fsPath);
  const cfg = vscode.workspace.getConfiguration("xml");
  const cur = cfg.get("fileAssociations") || [];
  if (!cur.some(a => a && a.pattern === pattern && a.systemId === abs)) {
    const next = cur.filter(a => !(a && a.pattern === pattern)).concat([{ systemId: abs, pattern }]);
    await cfg.update("fileAssociations", next, ws ? vscode.ConfigurationTarget.Workspace : vscode.ConfigurationTarget.Global);
  }
  if (!silent) vscode.window.showInformationMessage(`FS25 XML: bound ${path.basename(doc.fileName)} → ${schema}`);
  return true;
}

async function handleDoc(doc, opts) {
  if (!doc || doc.languageId !== "xml") return;
  const n = await repointDoc(doc, { silent: true });
  if (n === 0) await bindIfNoRef(doc, { silent: true });
  if (opts && !opts.silent) vscode.window.showInformationMessage("FS25 XML: schema applied to current file.");
}

function activate(context) {
  loadBinding(context);

  context.subscriptions.push(
    vscode.commands.registerCommand("fs25xml.bindCurrent", () => {
      const ed = vscode.window.activeTextEditor; if (ed) handleDoc(ed.document, { silent: false });
    }),
    vscode.commands.registerCommand("fs25xml.repointWorkspace", async () => {
      const files = await vscode.workspace.findFiles("**/*.xml", "**/node_modules/**");
      const pick = await vscode.window.showWarningMessage(
        `FS25 XML: repoint stock schema refs in ${files.length} XML file(s) to the enriched schemas? This edits and saves the files.`,
        { modal: true }, "Repoint");
      if (pick !== "Repoint") return;
      let edited = 0, refs = 0;
      for (const uri of files) {
        const doc = await vscode.workspace.openTextDocument(uri);
        const n = await repointDoc(doc, { silent: true });
        if (n > 0) { edited++; refs += n; } else { await bindIfNoRef(doc, { silent: true }); }
      }
      vscode.window.showInformationMessage(`FS25 XML: repointed ${refs} ref(s) across ${edited} file(s).`);
    }),
    vscode.commands.registerCommand("fs25xml.insertSchemaRef", async () => {
      const ed = vscode.window.activeTextEditor; if (!ed) return;
      const doc = ed.document, schema = pickSchema(doc);
      if (!schemaValid(schema)) { vscode.window.showWarningMessage("FS25 XML: no matching schema for this file."); return; }
      const abs = schemaTarget(schema);
      const text = doc.getText();
      const m = text.match(/<([A-Za-z_][\w.\-]*)((?:\s+[^>]*?)?)(\/?)>/);
      if (!m) return;
      if (/noNamespaceSchemaLocation/.test(m[0])) { await repointDoc(doc, { silent: false }); return; }
      const at = doc.positionAt(m.index + 1 + m[1].length);
      await ed.edit(b => b.insert(at, ` xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="${abs}"`));
      vscode.window.showInformationMessage(`FS25 XML: added schema reference → ${schema}`);
    }),
    vscode.workspace.onDidOpenTextDocument(doc => {
      const cfg = vscode.workspace.getConfiguration("fs25xml");
      if (cfg.get("autoRepointOnOpen") && /noNamespaceSchemaLocation/.test(doc.getText())) repointDoc(doc, { silent: true });
      else if (cfg.get("autoBindOnOpen")) bindIfNoRef(doc, { silent: true });
    })
  );

  const cfg = vscode.workspace.getConfiguration("fs25xml");
  for (const doc of vscode.workspace.textDocuments) {
    if (cfg.get("autoRepointOnOpen") && /noNamespaceSchemaLocation/.test(doc.getText())) repointDoc(doc, { silent: true });
    else if (cfg.get("autoBindOnOpen")) bindIfNoRef(doc, { silent: true });
  }
}
function deactivate() {}
module.exports = { activate, deactivate };
