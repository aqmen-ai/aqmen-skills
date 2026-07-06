# Aqmen

A single plugin that bundles the **aqmen MCP connector** plus **skills** for
commercial due diligence — standardized reports today, and analysis tasks (source
checks, triangulation, …) over time. Installing it provides the aqmen tools *and*
aqmen's house structure, design system, and source/confidence conventions, so
outputs come out consistent and decision-grade.

The report skills are **guidelines-only**: the assistant assembles the output
from the analysis data (via the connector), and the skill enforces *how it's
written and styled*.

## Install

```
/plugin marketplace add aqmen-ai/aqmen-skills
/plugin install aqmen@aqmen-skills
```

In the desktop app: **Customize → Plugins → Add marketplace** (`aqmen-ai/aqmen-skills`),
then install. On first use you'll be prompted to sign in to aqmen (OAuth). Updates
ship via git: `/plugin marketplace update aqmen-skills`.

_(Local dev: `claude --plugin-dir .` from the repo root.)_

## What's included

**Skills** (invoke as `aqmen:<skill>`):

| Skill | Does | Status |
| --- | --- | --- |
| `aqmen:market-sizing-report` | Market sizing report | ✅ |
| `aqmen:company-analysis-report` | Company analysis report | ✅ |
| `aqmen:competitive-landscape-report` | Competitive landscape report | ✅ |
| `aqmen:check-sources`, `aqmen:triangulate-analysis`, … | Analysis tasks | ⏳ planned |

**MCP connector** — `.mcp.json` wires up the aqmen server (`aqmen`, an OAuth HTTP
MCP server); you sign in to aqmen on first use.

## Repo layout (single-plugin repo)

The repo root *is* the plugin; the marketplace file is a thin wrapper so
installation works.

```
.claude-plugin/
  plugin.json            # the plugin (name: "aqmen")
  marketplace.json       # 1 entry, source "." → the repo root
.mcp.json                # aqmen connector
shared/                  # CANONICAL shared files (edit here)
  report-standards.md    #   voice, base-first, sources & confidence scale
  report-data.md         #   how to pull & use aqmen data fully (tool-agnostic)
  report-style.md        #   design system (navy/logo) + charts (ECharts)
  report-template.html   #   branded HTML skeleton (ECharts + exec components)
scripts/sync-shared.mjs  # copies shared/* into each skill's references/
skills/
  market-sizing-report/
    SKILL.md
    references/          # self-contained: synced shared files + this type's structure
```

## Adding / customizing skills

Skills are folders under `skills/`. To add one: create `skills/<name>/SKILL.md`,
then run the sync script to pull the shared files in. To retune the house style
for all skills, edit `shared/` and re-sync:

```
node scripts/sync-shared.mjs
```

Plugins don't reliably copy files outside a skill's own directory, so each skill
is **self-contained** — the shared files are canonical in `shared/` and copied
into every skill's `references/`.

## How reports render (charts + branding)

Reports are stored as aqmen **artifacts** and viewed in a sandboxed, cross-origin
iframe. Each is a single `.html` file — inline CSS/JS, the aqmen logo as a `data:`
URI — whose **only external resource is a pinned ECharts build from cdnjs**
(integrity-hashed, whitelisted by the report's own `<meta>` CSP), so report *data*
stays inline while charts stay powerful and interactive. With the connector
present, the finished file is saved to the project's Files.

To bump the chart library, change the pinned version **and** its `integrity` hash
in `shared/report-template.html` (SRI from cdnjs), then re-sync.

## Validate

```
claude plugin validate .
```
