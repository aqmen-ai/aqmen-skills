# aqmen

A Claude plugin for strategic-decision work on the [aqmen platform](https://try.aqmen.ai):
the **aqmen MCP connector** plus **skills** organized by use case. Installing it
gives your assistant the aqmen tools *and* the consulting practice around them:
research in passes with every figure cited, models built as a chain from data to
answer, adversarial critics before anything is called done, and a deliverable —
a deck in the workspace — whose every figure is sourced from the model.

**The platform explains the platform; the skills explain the process.** The MCP's
`read_instructions` topics (`workflow`, `datasets`, `sql`, `charts`,
`spreadsheets`, `insights`, `views`, `decks`, `collections`, `modeling`,
`market-sizing`, `company-analysis`, `competitive-landscape`) are the spec for
how every tool, model and deck works. The skills reference them by name and add
what the platform does not: the steps, the gates, the critics and the standard a
deliverable is held to.

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

### Use cases

| Skill | Use it when | What it runs |
| --- | --- | --- |
| `aqmen:cdd` | "We're running a CDD on X", "is there an opportunity in Y" | A commercial due diligence end to end: the three workstreams — **market** (`market-sizing`), **competition** (`competitive-landscape`), **company** (`company-analysis`) — through the shared steps with their gates, reconciled across workstreams, ending in one CDD deck in the fixed four-part storyline |

More use cases will reuse the same steps.

### Shared steps (any use case)

| Skill | Does | Ends when |
| --- | --- | --- |
| `aqmen:scope` | Writes the brief to the workspace: the decision, the questions (`Q1 [open]: …`), the frame, the deliverable | The user confirms the brief |
| `aqmen:research` | Parallel researchers find the data and return load-ready packets; a data loader checks and loads each as a cited dataset | Every driver has a dataset or a named gap |
| `aqmen:model` | Builds the model on the platform's framework topics, with summary blocks and charts a deck can source | Checks hold, nothing stale, the model critic passed |
| `aqmen:challenge` | Runs the model and values critics, the skeptic (the client's IC) and the deck critic in fresh contexts | Findings resolved or accepted |
| `aqmen:conclude` | One insight per claim on the chart that shows it, challenged by the skeptic and validated; a view per question, built by background view builders in parallel | Every question answered or "cannot say" |
| `aqmen:deliver` | Builds the deck in the workspace from the use case's storyline, every figure by source; audits, shows, files and exports it; optionally an HTML report read from the deck | Nothing stale, audit passed, deck shown |
| `aqmen:refresh` | New data in, the chain rerun, every stale insight and deck figure re-checked, the words around moved figures fixed | Nothing stale, decks included |
| `aqmen:demo-prep` | A run-of-show (`demo_script.md`): per question, the figure, the slide, chart or view to open, the fallback | Every question opens a saved figure |

### Before the work

| Skill | Output |
| --- | --- |
| `aqmen:proposal` | The client proposal or statement of work (editable `.docx`) from call notes or a brief — analysis, build or internal engagement: workstreams, rated hypotheses, analyses, workplan, data request, commercials |
| `aqmen:storyline` | The slide plan (one row per slide: action title, exhibit, data, owner, purpose) as Excel, and — once the workspace exists — a **ghost deck** in it with dashed placeholders, to agree the storyline before the analysis; `deliver` later fills it |

The proposal and the storyline feed `aqmen:scope`: the client's questions, the
hypotheses and the data request become the workspace brief and the research
agenda; the ghost deck becomes the deliverable.

### Agents

Spawned by the steps or on request ("critique the model", "what will the IC
ask", "audit the deck", "find data for these drivers", "load these files"):

| Agent | Kind | Scope | Writes | Spawned by |
| --- | --- | --- | --- | --- |
| `researcher` | Build | Web research on a disjoint assignment: scoping scans and value packages, returned as load-ready packets (CSV-shaped tables with units and scale, one citation per document, a confidence) | Nothing | `research`, parallel |
| `data-loader` | Build | Packets or client files → clean, checked, cited, annotated datasets; preview first, then load | Datasets only | `research`, `refresh`; one at a time per workspace |
| `view-builder` | Build | One view from a spec, saved clean, read back, its figures checked | One view only | `conclude` (one per question), `refresh`, `demo-prep`; background, parallel |
| `model-critic` | Critique | The chain datasets → transformations → spreadsheet: segmentation, decomposition, dependencies, units, formulas, lint, scenarios | Nothing | `model` (gate), `challenge` |
| `values-critic` | Critique | Figures and sources: citations, confidence, methods, data integrity, triangulation | Nothing | `challenge` (before done, before deliver) |
| `deck-critic` | Critique | The deck as communication (storyline, action titles, so-whats, consistency, house look) and its sourcing (typed, stale, drifted, detached) | Nothing | `deliver` (gate before hand-over) |
| `skeptic` | Critique | The client's investment committee against the conclusions: alternatives, load-bearing assumptions, gaps, the hardest questions | Nothing | `conclude`, `challenge` (CDD by default) |

Critics run in a fresh context and receive only ids, the scope and the brief
verbatim — never the builder's reasoning — and return findings with ids for a
recheck. Writers stay in their scope; everything else (transformations,
spreadsheets, charts, insights, decks, the brief) is the main agent's, one call
at a time. Research and views run in parallel; dataset loading and deck writing
are serialized.

## How decks work

The deliverable is a **deck in the aqmen workspace**, not a file built locally:

- **Built through the MCP**: `create_deck` and `update_deck` ops against a base
  version, `read_deck` to read it back, `list_decks` to find it again. The house
  look, the option reference and tested recipes are the platform's `decks`
  topic.
- **Figures by source**: a chart, a KPI or a table that the workspace computes
  goes on a slide as an element with a `source` (a saved chart, a spreadsheet
  cell or range, one field of a chart, a validated insight). The server fills
  the data and pins it. Words are typed; numbers are the workspace's.
- **Staleness is tracked**: when the model moves, the deck's sourced figures go
  stale; `refreshSource` re-reads them (`aqmen:refresh`), and the words around
  them are re-checked. Nothing goes to the client while a figure is stale.
- **Shown and exported**: `show_deck` puts the slides in the chat, the deck page
  has a Present mode, and `export_deck` gives an editable PowerPoint (`.pptx`,
  native charts and tables).
- **An optional HTML report** (`aqmen:deliver`) reads its figures from the
  deck's pins, so the two can never disagree.

## How projects run

- **Parallel research, scoped writers.** Researchers run scoping scans and
  value packages in parallel and return load-ready tables; a data loader checks
  and loads them as cited datasets, one loader at a time; view builders build
  one view each, in the background. Everything else is the main agent's.
- **Adversarial gates.** Fresh-context, read-only critics audit the work where
  fixes are cheapest: the **model critic** after the model's shape exists,
  the **values critic** before anyone calls it done, the **skeptic** on the
  conclusions, and the **deck critic** before the deck is handed over. Critics receive only the ids and the brief
  verbatim, never the builder's rationale.
- **The brief is the thread.** `aqmen:scope` writes the decision and the
  questions into the workspace docs; every later step reads them and appends to
  the brief's Log, so the next session starts where the last one stopped.

## Repo layout

```
.claude-plugin/marketplace.json   # marketplace (aqmen-skills) → ./plugins/aqmen
plugins/aqmen/
  .claude-plugin/plugin.json      # the plugin (name: "aqmen")
  .mcp.json                       # aqmen connector (https://platform.aqmen.ai/api/mcp)
  agents/                         # build: researcher, data-loader, view-builder;
                                  #   critique: model-critic, values-critic, deck-critic, skeptic
  shared/                         # CANONICAL shared references (edit here, then sync)
    practice.md                   #   topics first, pacing, agents, numbers by source, the brief, gates
    deliverable-standards.md      #   voice, base first, traceability, sources & confidence
    cdd-storyline.md              #   the CDD deck storyline (cdd, storyline)
    engagement-method.md          #   Answer First, ratings, backwards planning (proposal, storyline)
  scripts/
    sync-shared.mjs               # copies shared/ files into each skill's references/
    build-html-examples.py        # renders the HTML report templates into skills/deliver/assets/
    example_content.py            #   their placeholder content
    report-shell.html             #   their canonical HTML shell (CSS, CSP, logo, ECharts)
  skills/
    cdd/                          # use case: SKILL.md + workstream-*.md (per framework: content,
                                  #   slides as elements + sources, report sections, what to gather)
    scope/ research/ model/       # shared steps
    challenge/ conclude/ deliver/
    refresh/ demo-prep/
    deliver/                      #   + references/ (gather, deck, html-companion, report-style)
                                  #   + assets/<module>-report-template.html
    proposal/                     # pre-project: .docx proposal builder (scripts/, assets/)
    storyline/                    # pre-project: .xlsx plan builder; ghost deck via the MCP
```

Plugins don't reliably ship files outside a skill's own directory, so a file
several skills read is canonical in `shared/` and copied into each skill's
`references/` by the sync script; a file one skill reads lives only there.

```
node plugins/aqmen/scripts/sync-shared.mjs             # after editing shared/
python3 plugins/aqmen/scripts/build-html-examples.py   # after editing the report shell or example content
```

## How HTML reports render

Reports are opened locally, emailed, or viewed in a sandboxed, cross-origin
iframe. Each is a single `.html` file — inline CSS/JS, the aqmen logo as a `data:`
URI — whose **only external resource is a pinned ECharts build from cdnjs**
(integrity-hashed, whitelisted by the report's own `<meta>` CSP). To bump the
chart library, change the pinned version **and** its `integrity` hash in
`scripts/report-shell.html`, then regenerate the templates.

## Validate

```
claude plugin validate .                # the marketplace
claude plugin validate ./plugins/aqmen  # the plugin
```
