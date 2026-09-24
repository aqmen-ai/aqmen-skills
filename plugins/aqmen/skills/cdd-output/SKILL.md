---
name: cdd-output
description: Produce aqmen's standard commercial-due-diligence deliverable set from analysis data — a client-ready PowerPoint deck (editable, native charts), a self-contained HTML report and a two-page Word/PDF executive summary — all from one content file, in the fixed four-part storyline (executive summary → market → competition → company). Use this whenever the user wants the output, deliverable, readout, demo deck, final presentation, report or executive summary of a CDD, market study, opportunity assessment or investment case — including phrasings like "put the analysis into the deck", "what does the client see at the end", "prepare the demo output", "write up the car-wash case", "make the Moeve deck" — especially in a workspace connected to the aqmen MCP. Covers both an operating company (P&L, DCF) and a project/investment case (payback, break-even, what you need to believe).
---

# Aqmen CDD Output

Turn a finished (or demo) analysis into the deliverable set a client receives:

| Format | File | Use |
| --- | --- | --- |
| Deck | `<slug>.pptx` | The presentation. Editable, native charts, house style. |
| Report | `<slug>.html` | The artifact for the aqmen viewer; prints to PDF. |
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

Pull the whole analysis from the aqmen MCP: market definition, driver tree and
values, segment splits and trajectory, scenarios and trends; the competitive
dataset (players, fields, archetypes); the company or project model (inputs vs
computed, periods, valuation or payback outputs); every value's source,
confidence and note; the source list. Decide the **company variant**: corporate
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
- **Base before scenario**; Trend or Initiative thesis in words first, then the
  overrides.
- **Estimates labelled**: `illustrative: true` on modelled shapes; low
  confidence surfaced as a `watchout`; nothing implied complete.
- **Reconcile across parts**: the revenue build total should sit near the SAM;
  project volumes should be a plausible share of local SAM; the company's
  growth should be explainable by the trends.
- **Exec summary last**, from the headlines. Four rows (Context, Market,
  Competition, Company); for project cases add `need_to_believe`.

### 4. Render

```
python scripts/build_cdd.py content.json ./out --pdf
```

(`pip install python-pptx python-docx` if missing.) `--final` removes the DRAFT
tag; `--only deck|html|summary` renders one format. `--pdf` exports the Word
summary through Word on Windows; skip it elsewhere.

Open the `.pptx` if you can (PowerPoint export to PDF and rasterise, or read
slide text back with python-pptx) and check: headlines fit on two lines, charts
have units, no slide is empty, the agenda reflects the parts.

### 5. Hand over

Tell the user in a few lines: the bottom line, which exhibits rest on the
weakest data, what you assumed where the model was silent, and the three files.
If the aqmen connector is available, offer to store the HTML and the deck as
artifacts in the project's Files.

## Where the skill stops

It renders analysis that exists. Building the driver tree, the competitive grid
or the project model is the aqmen MCP's job (or the consultant's). The
presentation plan that precedes this deliverable (the Dot-Dash) is a separate
skill; the scope that precedes both is `aqmen-scope`.
