# aqmen

A Claude plugin for strategic-decision work on the [aqmen platform](https://try.aqmen.ai):
the **aqmen MCP connector** plus **skills** for each step of a project, from the
brief to the deliverable. Installing it gives your assistant the aqmen tools *and*
the practice around them: research in passes with every figure cited, models
built as a chain from data to answer, adversarial critics before anything is
called done, and deliverables in aqmen's house style.

The platform's own `read_instructions` topics stay the spec for what correct
work is. The skills add the order of the work, the gates between steps, and
the parallel research and review around it.

## Install

```
/plugin marketplace add aqmen-ai/aqmen-skills
/plugin install aqmen@aqmen-skills
```

In the desktop app: **Customize → Plugins → Add marketplace** (`aqmen-ai/aqmen-skills`),
then install. On first use you'll be prompted to sign in to aqmen (OAuth). Updates
ship via git: `/plugin marketplace update aqmen-skills`.

The connector points at `https://platform.aqmen.ai/api/mcp`. Any other assistant
with MCP support can connect to the same URL; the skills are for clients that
load plugins.

_(Local dev: `claude --plugin-dir ./plugins/aqmen` from the repo root.)_

## What's included

**The steps of a project** (invoke as `aqmen:<skill>`, or just describe the work):

| Step | Skill | Does | Ends when |
| --- | --- | --- | --- |
| 0 | `aqmen:project` | Runs the whole flow, step by step or autonomously | Every gate below holds |
| 1 | `aqmen:scope` | Writes the brief to the workspace: the decision, the questions, the frame, the deliverable | The user confirms the brief |
| 2 | `aqmen:research` | Parallel researchers find the data; each finding lands as a cited dataset | Every driver has a dataset or a named gap |
| 3 | `aqmen:model` | Builds the model: datasets → transformations → a spreadsheet → driver trees and bridges. Market sizing, company analysis, competitive landscape or custom | Checks hold, nothing stale, the structure critic passed |
| 4 | `aqmen:challenge` | Runs the structure and values critics in fresh contexts | Findings resolved or accepted |
| 5 | `aqmen:conclude` | One insight per claim on the chart that shows it; a view per question | Every question answered or "cannot say" |
| 6 | the deliverable skills | `aqmen:cdd-output`, `aqmen:bp-assessment`, or a framework's report or deck, below | Every number traces to the workspace |
| 7 | `aqmen:refresh` | New data in, the chain rerun, every stale insight re-checked | Nothing stale |

**Around the engagement**, before the work starts and when it is delivered:

| Skill | Output |
| --- | --- |
| `aqmen:aqmen-scope` | The client proposal or statement of work (editable `.docx`) from call notes or a brief: workstreams, rated hypotheses, analyses, workplan, data request, commercials |
| `aqmen:dot-dash` | The presentation plan: one row per slide (action title, exhibit, data, owner) as Excel plus a skeleton deck, to agree the storyline before the analysis |
| `aqmen:cdd-output` | The full CDD deliverable set from one content file: deck (`.pptx`), HTML report and a Word/PDF executive summary |
| `aqmen:bp-assessment` | A management business plan rated assumption by assumption on market, competitive position and track record: matrix, deep-dive slides and Excel |

The proposal and the slide plan feed `aqmen:scope`: the client's questions,
the hypotheses and the data request become the workspace brief and the
research agenda.

**Deliverables per framework** (step 6), assembled from the workspace:

| Skill | Output |
| --- | --- |
| `aqmen:market-sizing-report`, `aqmen:market-sizing-deck` | Market sizing, HTML report or editable `.pptx` |
| `aqmen:company-analysis-report`, `aqmen:company-analysis-deck` | Company analysis and valuation |
| `aqmen:competitive-landscape-report`, `aqmen:competitive-landscape-deck` | Competitive landscape |

**Agents**, spawned by the step skills or on request ("critique the model",
"audit the sources", "find data for these drivers"):

| Agent | Role |
| --- | --- |
| `researcher` | Read-only, parallel: scoping scans and value packages with cited sources, returned as tables the main agent loads as datasets |
| `structure-critic` | Adversarial, read-only review of segmentation, decomposition, dependencies, units and the chain, before values are trusted |
| `values-critic` | Adversarial, read-only review of every driver's citation, confidence and method, and the triangulation, before "done" |

Researchers and critics only read. The main agent is the one writer, one call
at a time.

Two output formats per framework: a document-style **HTML report** (`*-report`)
and a client-facing **PowerPoint deck** (`*-deck`, a real editable `.pptx` in the
"Discussion Materials" house style, with native charts). Both formats of a
framework render the **same content**: the narrative, so-whats, rules and what
to gather live in one shared `shared/<module>-content.md` spec that both skills
read. The **starter templates** are likewise generated from one source:
`scripts/example_content.py` holds each module's example content, and
`build-templates.py` (PPTX) and `build-html-examples.py` (HTML) render it.

## Repo layout

The repo is a marketplace with one plugin under `plugins/aqmen/`.

```
.claude-plugin/marketplace.json   # marketplace (aqmen-skills) → ./plugins/aqmen
plugins/aqmen/
  .claude-plugin/plugin.json      # the plugin (name: "aqmen")
  .mcp.json                       # aqmen connector (https://platform.aqmen.ai/api/mcp)
  shared/                         # CANONICAL shared files (edit here)
    practice.md                   #   pacing, one writer, sources & confidence  (step skills)
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
  agents/                         # researcher, structure-critic, values-critic
  skills/
    project/ scope/ research/     # the step skills → practice.md
    model/ challenge/ conclude/ refresh/
      SKILL.md
      references/                 # practice.md (+ model's framework guides)
    market-sizing-report/         # HTML report skills → common + report files
      SKILL.md
      references/                 # self-contained: synced shared files + this type's structure
    market-sizing-deck/           # PowerPoint deck skills → common + deck files
      SKILL.md
      references/
```

The sync script routes files by skill name: the step skills get the shared
practice, `*-report` skills get the common + HTML-report files, `*-deck` skills
get the common + deck files, `cdd-output` gets every content spec and both
style systems, `bp-assessment` and `dot-dash` the deck builder, and `*-scope`
(Word-document) skills only `report-standards.md`, so each
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

Reports are opened locally, emailed, or viewed in a sandboxed, cross-origin
iframe. Each is a single `.html` file — inline CSS/JS, the aqmen logo as a `data:`
URI — whose **only external resource is a pinned ECharts build from cdnjs**
(integrity-hashed, whitelisted by the report's own `<meta>` CSP), so report *data*
stays inline while charts stay powerful and interactive.

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

## How projects run (multi-agent orchestration)

- **Parallel research, one writer.** Researchers run scoping scans and value
  packages in parallel and return cited tables; the main agent loads each as a
  dataset with its sources, one write at a time.
- **Adversarial gates.** Two fresh-context, read-only critics audit the work
  where fixes are cheapest: the **structure critic** after the model's shape
  exists and before values are trusted, the **values critic** before anyone
  calls it done. Critics receive only the workspace, the spreadsheet and the
  brief verbatim, never the builder's rationale.
- **The brief is the thread.** `aqmen:scope` writes the decision and the
  questions into the workspace docs; every later step reads them, and appends
  to the brief's log, so the next session starts where the last one stopped.

## Validate

```
claude plugin validate .              # the marketplace
claude plugin validate ./plugins/aqmen  # the plugin
```
