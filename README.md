# Aqmen Reports plugin

A Claude plugin (Claude Code + Claude Desktop) that bundles **standardized
output-report skills** for aqmen analyses, plus the **aqmen MCP connector**.
Installing it gives Claude both the aqmen tools (to read your analyses and store
reports) and aqmen's house report structure, design system, and
source/confidence conventions — so reports come out consistent and
decision-grade.

The report skills are **guidelines-only**: Claude assembles the report from the
analysis data (via the bundled connector) and the skill enforces *how it's
written and styled*.

## What's included

**Skills**

| Skill (invoke as) | Report | Status |
| --- | --- | --- |
| `aqmen-reports:market-sizing-report` | Market sizing | ✅ |
| `aqmen-reports:company-analysis-report` | Company analysis | ✅ |
| `aqmen-reports:competitive-landscape-report` | Competitive landscape | ✅ |

**MCP server** — `.mcp.json` wires up the aqmen connector (`aqmen`, an OAuth
HTTP MCP server). Claude runs the sign-in flow on first use.

## Install

```
/plugin marketplace add aqmen-ai/aqmen-skills
/plugin install aqmen-reports@aqmen
```

In **Claude Desktop** you can do the same from **Customize → Plugins** — add the
marketplace by its `owner/repo` handle, then install with a click. On first use
Claude will prompt you to sign in to aqmen (OAuth). Updates ship via git:
`/plugin marketplace update aqmen`.

_(Local dev on this plugin: `claude --plugin-dir ./plugins/aqmen-reports`.)_

## Customize which skills are included

Skills are just folders under `skills/`:

- **Remove** a report: delete its folder (`rm -r skills/company-analysis-report`).
- **Add** your own: create `skills/<your-report>/SKILL.md`, then run the sync
  script to pull in the shared design/standards files.
- **Retune the house style** for all reports: edit the canonical files in
  `shared/` and re-sync.

## How consistency works (shared vs per-type)

```
plugins/aqmen-reports/
  .claude-plugin/plugin.json     # manifest
  .mcp.json                      # bundled aqmen MCP connector
  shared/                        # CANONICAL shared files (edit here)
    report-standards.md          #   voice, base-first, sources & confidence scale
    report-data.md               #   how to pull & use aqmen MCP data fully
    report-style.md              #   design system + charts (ECharts) + constraints
    report-template.html         #   HTML skeleton (ECharts + executive components)
  scripts/sync-shared.mjs        # copies shared/* into each skill's references/
  skills/
    market-sizing-report/
      SKILL.md                   # trigger + workflow (short)
      references/                # self-contained copy of shared + this type's structure
        report-standards.md      #   (synced from shared/)
        report-data.md           #   (synced from shared/)
        report-style.md          #   (synced from shared/)
        report-template.html     #   (synced from shared/)
        market-sizing-structure.md   # per-type sections, charts & MCP data sources
```

Claude plugins don't reliably copy files outside a skill's own directory, so each
skill must be **self-contained**. We keep the shared files canonical in `shared/`
and copy them into every skill's `references/`:

```
node plugins/aqmen-reports/scripts/sync-shared.mjs
```

Run it after editing anything in `shared/`, or after adding a new skill.

## How reports render (charts + hosting)

Reports are stored as aqmen **artifacts** and viewed in a sandboxed, cross-origin
iframe. Each report is a single `.html` file — inline CSS/JS, `data:` images —
whose **only external resource is a pinned ECharts build from cdnjs** (integrity-
hashed, and whitelisted by the report's own `<meta>` CSP). This mirrors how
claude.ai's own Artifacts load charting libraries, and keeps report *data* inline
while charts stay powerful and interactive. With the connector present, the
finished file is saved to the project's Files via `upload_artifact`.

To bump the chart library, change the pinned version **and** its `integrity` hash
in `shared/report-template.html` (get the SRI from cdnjs), then re-sync.

## Validate

```
claude plugin validate ./plugins/aqmen-reports
```
