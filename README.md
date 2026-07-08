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

_(Local dev: `claude --plugin-dir ./plugins/aqmen` from the repo root.)_

## What's included

**Skills** (invoke as `aqmen:<skill>`):

| Skill | Does | Status |
| --- | --- | --- |
| `aqmen:market-sizing-report` | Market sizing report (HTML) | ✅ |
| `aqmen:company-analysis-report` | Company analysis report (HTML) | ✅ |
| `aqmen:competitive-landscape-report` | Competitive landscape report (HTML) | ✅ |
| `aqmen:market-sizing-deck` | Market sizing deck (editable `.pptx`) | ✅ |
| `aqmen:company-analysis-deck` | Company analysis deck (editable `.pptx`) | ✅ |
| `aqmen:competitive-landscape-deck` | Competitive landscape deck (editable `.pptx`) | ✅ |
| `aqmen:check-sources`, `aqmen:triangulate-analysis`, … | Analysis tasks | ⏳ planned |

Two output formats per module: a document-style **HTML report** (`*-report`,
renders inline as an artifact) and a client-facing **PowerPoint deck** (`*-deck`,
a real editable `.pptx` in the "Discussion Materials" house style, with native
charts). Both formats of a module render the **same content** — the analytical
narrative, so-whats, module rules, and what-to-gather live in one shared
`shared/<module>-content.md` spec that both skills read — so a module's report
and deck never drift; they differ only in presentation. The **starter
templates** are likewise generated from one source: `scripts/example_content.py`
holds each module's example content, and `build-templates.py` (PPTX) and
`build-html-examples.py` (HTML) render it into the deck and report starters — so
a module's example deck and example report show the same information.

**MCP connector** — `.mcp.json` wires up the aqmen server (`aqmen`, an OAuth HTTP
MCP server); you sign in to aqmen on first use.

## Repo layout

The repo is a marketplace with one plugin under `plugins/aqmen/`.

```
.claude-plugin/marketplace.json   # marketplace (aqmen-skills) → ./plugins/aqmen
plugins/aqmen/
  .claude-plugin/plugin.json      # the plugin (name: "aqmen")
  .mcp.json                       # aqmen connector
  shared/                         # CANONICAL shared files (edit here)
    report-standards.md           #   voice, base-first, sources & confidence scale  (all skills)
    report-data.md                #   how to pull & use aqmen data fully (tool-agnostic) (all skills)
    <module>-content.md           #   format-agnostic content spec per module (report + deck)
    report-style.md               #   HTML design system (navy/logo) + charts (ECharts) (*-report)
    report-template.html          #   canonical HTML shell — CSS source for the generator (NOT synced)
    <module>-report-template.html #   populated, styled HTML example per module (the only html shipped) (*-report)
    deck-style.md                 #   deck design system + slide taxonomy + chart rules   (*-deck)
    aqmen_deck.py                 #   python-pptx builder for house-style .pptx decks     (*-deck)
    <module>-deck-template.pptx   #   populated, styled starter deck per module           (*-deck)
  scripts/example_content.py      # SINGLE SOURCE of per-module example content (both formats)
  scripts/build-templates.py      # renders example_content → shared/*-deck-template.pptx
  scripts/build-html-examples.py  # renders example_content → shared/*-report-template.html
  scripts/sync-shared.mjs         # copies the right shared files into each skill's references/
  skills/
    market-sizing-report/         # HTML report skills → common + report files
      SKILL.md
      references/                 # self-contained: synced shared files + this type's structure
    market-sizing-deck/           # PowerPoint deck skills → common + deck files
      SKILL.md
      references/
```

The sync script routes files by skill-name suffix: `*-report` skills get the
common + HTML-report files, `*-deck` skills get the common + deck files, so each
skill's `references/` carries only what its format needs. A module's
`<module>-content.md` spec is routed into **both** that module's report and deck
skills. Within each skill, a thin `*-structure.md` (report) or
`*-deck-structure.md` (deck) says only *how* to render that shared content in its
format.

## Adding / customizing skills

Skills are folders under `skills/`. To add one: create `skills/<name>/SKILL.md`,
then run the sync script to pull the shared files in. To retune the house style
for all skills, edit `shared/` and re-sync:

```
node plugins/aqmen/scripts/sync-shared.mjs
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

## How decks build (editable PowerPoint)

Deck skills produce a **real, editable `.pptx`** — the CDD "Discussion Materials"
deliverable — via the `shared/aqmen_deck.py` builder (a thin, opinionated wrapper
around [`python-pptx`](https://python-pptx.readthedocs.io); `pip install
python-pptx`). Slides are 16:9 in aqmen's blue-dominant, Montserrat house style, with
standard chrome (DRAFT tag, section eyebrow, wordmark, source line, page number)
and **native PowerPoint charts** — column/bar/line/stacked, plus a variable-width
**Marimekko** (market sizing) and a **harvey-ball matrix** (competitive
landscape) — so consultants can keep editing the deck and its charts. A PDF can
be exported with `soffice --headless --convert-to pdf <name>.pptx`.

`Deck()` **self-brands from blank** — it injects the aqmen theme (brand colour
scheme + Montserrat fonts) into the deck's theme XML and bakes the wordmark onto
the slide master, so no external base file is needed.

Each deck skill also ships a **populated starter template** — a full, styled
example deck for that module (`shared/<module>-deck-template.pptx`), modelled on
the reference CDD deliverable. Open it to see the house style, edit its slides as
a manual starting point, or build on it with
`Deck(template="…/<module>-deck-template.pptx")` (the builder clears the example
slides but keeps the theme/master/layouts). The starter decks are generated by
the same builder, so they stay identical in style to live output:

```
python3 plugins/aqmen/scripts/build-templates.py   # regenerate the starter decks
node   plugins/aqmen/scripts/sync-shared.mjs         # copy them into deck skills
```

To retune the brand, slide construction, or chart rules, edit
`shared/deck-style.md` (the spec) and `shared/aqmen_deck.py` (the builder), then
regenerate and re-sync.

## Validate

```
claude plugin validate .              # the marketplace
claude plugin validate ./plugins/aqmen  # the plugin
```
