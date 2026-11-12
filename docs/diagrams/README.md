# Source-boundary diagram

- [Editable Excalidraw scene](source-boundaries.excalidraw)
- [Matching SVG preview](source-boundaries.svg)
- [Deterministic Python 3.11 stdlib generator](render_source_boundaries.py)

This is a source-derived overview of the baseline
[`1c3b0731de3c7c5fbc281c7bdedc6b5f1724d43a`](https://github.com/JDKristenson/compound-engineering-plugin/tree/1c3b0731de3c7c5fbc281c7bdedc6b5f1724d43a),
rechecked on 2026-11-12. It distinguishes inherited EveryInc/community
implementation, the two JD-attributed CI/lint commits, static documentation,
and optional tool execution. It does not certify authorship, upstream PR
acceptance, license clearance, installation, deployment, or runtime behavior.
Solid arrows describe source relationships; dashed arrows describe optional
execution paths, not observed network traffic.

## Evidence

- [Marketplace catalog](../../.claude-plugin/marketplace.json): local plugin
  paths, credited authors, catalog versions. The catalog has 19 commands in its
  description, whereas the tracked compound-engineering tree has 20 command
  Markdown files. The preview shows the tree count, not catalog consistency.
- [Plugin manifest](../../plugins/compound-engineering/.claude-plugin/plugin.json):
  version 2.20.0, Playwright MCP (`pw`) and Context7 configuration.
- [Root README](../../README.md): pinned provenance, setup boundaries,
  contribution links, and unresolved nested-license references.
- [CI workflow](../../.github/workflows/ci.yml): configured checks, not a runtime
  proof. No workflow was changed for this documentation addition.

## Edit and regenerate

Open/import the `.excalidraw` file in Excalidraw to edit its independent text,
rectangle, and arrow elements. It contains no embedded files, personal data,
credentials, environment identifiers, or private deployment addresses.

The SVG and Excalidraw are generated from the same scene. For a synchronized
checked-in change, edit the generator's labels/positions and run from the
repository root:

```bash
python3 docs/diagrams/render_source_boundaries.py
```

The generator uses only Python's standard library. It writes the two diagram
files beside itself; it does not run the plugin, install packages, or contact
services. Direct edits in Excalidraw do not update the generator or SVG
implicitly: port them back to the generator before regenerating, or explicitly
replace both exports together and explain the new source of truth.

Verification for this addition covers JSON/XML structure, stable regeneration,
label parity and visual inspection of the SVG preview. Native Excalidraw
import/edit/export round-trip has not been exercised. The SVG is a matching
programmatic preview, not a claim of an export made by the Excalidraw app.

This documentation and its generator/diagram were prepared with Reason (AI
assistance). Existing upstream, human, community and recorded AI attribution
and license notices remain in place; this addition does not relicense inherited
skills, assets, dependencies or services.
