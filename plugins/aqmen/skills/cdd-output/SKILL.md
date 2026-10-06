---
name: cdd-output
description: Produce aqmen's standard commercial-due-diligence deliverable set from analysis data — a client-ready PowerPoint deck (editable, native charts), a self-contained HTML report and a two-page Word/PDF executive summary — all from one content file, in the fixed four-part storyline (executive summary → market → competition → company). Use this whenever the user wants the output, deliverable, readout, demo deck, final presentation, report or executive summary of a CDD, market study, opportunity assessment or investment case — including phrasings like "put the analysis into the deck", "what does the client see at the end", "prepare the demo output", "write up the car-wash case", "make the Moeve deck" — especially in a session connected to the aqmen MCP, where the analysis lives in an aqmen workspace. Covers both an operating company (P&L, DCF) and a project/investment case (payback, break-even, what you need to believe).
---

# Aqmen CDD Output

Turn a finished (or demo) analysis into the deliverable set a client receives:

| Format | File | Use |
| --- | --- | --- |
| Deck | `<slug>.pptx` | The presentation. Editable, native charts, house style. |
| Report | `<slug>.html` | Self-contained; opens anywhere and prints to PDF. |
| Summary | `<slug> - Executive Summary.docx` (+ `.pdf`) | Two-page leave-behind. |

All three render from **one content JSON**, so they never disagree. Your job is
the content: the storyline, the exhibits, the numbers from the model, the
so-whats. The scripts do the layout.

## Read first

1. `references/cdd-storyline.md` — the four-part structure and which exhibit
   kind carries each topic. This is the spec Miguel set; follow its order.
2. `references/content-format.md` — the JSON the renderer takes.
3. `references/report-standards.md` and `references/report-data.md` — voice,
   base-first, sources & confidence, and how to pull everything from aqmen.
4. The module specs for the analytical rules of each part:
   `market-sizing-content.md`, `competitive-landscape-content.md`, and for the
   company part either `company-analysis-content.md` (operating business) or
   `project-economics-content.md` (a site, format or investment case).
5. `references/deck-style.md` and `references/report-style.md` only if you need
   to understand why an exhibit looks the way it does; the scripts apply them.

`assets/example-carwash.json` is a complete, illustrative content file (Spanish
car-wash market + project economics of a forecourt wash). Pattern-match against
it; do not copy its numbers.

## Workflow

### 1. Gather everything before writing

Read the whole project from the aqmen workspace, following
`references/report-data.md`: the brief in the workspace docs; the market
model (its spreadsheet, driver tree and bridge charts, segment splits and
trajectory, scenario hypotheses); the landscape table (players, fields,
tiers, archetypes); the company or project model (the statement sheets,
inputs vs computed, valuation or payback outputs); for every figure, the
dataset it comes from with its sources, method and confidence; the insights
that answer the brief's questions. The `What to gather from aqmen` section
of each content spec lists the detail. Decide the **company variant**: corporate
(P&L/DCF) or project economics (payback/break-even). If the aqmen connector is
not available, work from the files and notes the user gives you and mark every
figure you could not verify as an estimate. **Never invent a number.** If a
part has no data, say so in a `watchout` and keep the section short rather than
filling it.

### 2. Build the storyline before the exhibits

For each part, write the headlines first: one sentence per exhibit stating the
finding with its number. Read them in sequence; they should form an argument a
partner could present without the slides. Then pick the exhibit kind for each
from `cdd-storyline.md`. Typical demo deck: 25–35 exhibits across the four
parts. Cut anything whose takeaway does not change what the reader believes.

### 3. Write the content JSON

Follow `content-format.md`. Rules that matter most:

- **Headlines are findings**, with units. Topics go in `title`.
- **So-whats are for the rail**: two or three, each a consequence, not a
  restatement of the chart.
- **Base before scenario**; the scenario's hypotheses in words first, then the
  changes vs Base.
- **Estimates labelled**: `illustrative: true` on modelled shapes; low
  confidence surfaced as a `watchout`; nothing implied complete.
- **Reconcile across parts**: the revenue build total should sit near the SAM;
  project volumes should be a plausible share of local SAM; the company's
  growth should be explainable by the trends.
- **Exec summary last**, from the headlines. Four rows (Context, Market,
  Competition, Company); for project cases add `need_to_believe`.

Point each exhibit at what it shows: a `ref` with the saved chart's
`chartId`, or the `spreadsheetId`, `sheet` and `range` of the model cells
(`content-format.md`, "Refs to the workspace").

### 4. Resolve refs

Before every build, resolve each section's `ref` from the workspace:
`get_chart` for a `chartId`, `read_spreadsheet` for a range. Write the literal
values into the section's fields and set `ref.resolved` to today's date; keep
the ids. A rebuild re-resolves from the ids, so the deck follows the model
instead of a hand-copied snapshot. The renderer refuses a section with an
unresolved ref.

### 5. Render

```
python scripts/build_cdd.py content.json ./out --pdf
```

(`pip install python-pptx python-docx` if missing.) `--final` removes the DRAFT
tag; `--only deck|html|summary` renders one format. `--pdf` exports the Word
summary through Word on Windows; skip it elsewhere.

Each build records the content hash per format in `<slug>.build.json`. With
`--only`, a skipped format whose file was built from other content gets a
`stale` warning: rebuild it before handing over, or the three files disagree.

Open the `.pptx` if you can (PowerPoint export to PDF and rasterise, or read
slide text back with python-pptx) and check: headlines fit on two lines, charts
have units, no slide is empty, the agenda reflects the parts.

### 6. Hand over

Tell the user in a few lines: the bottom line, which exhibits rest on the
weakest data, what you assumed where the model was silent, and the three files.
Offer to record any headline finding that is not yet an insight in the
workspace, on the chart or spreadsheet that shows it.

## Where the skill stops

It renders analysis that exists. Building the market model, the landscape or the
project model is the job of `aqmen:model` (or the consultant's). The
presentation plan that precedes this deliverable (the Dot-Dash) is a separate
skill; the scope that precedes both is `aqmen-scope`.
