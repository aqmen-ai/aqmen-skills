# Storyline plan format (JSON → Excel, and the ghost deck)

The plan (consultants call it the Dot-Dash) is the presentation written
before the analysis: **one row per slide**. Reading the action titles top to
bottom must argue the case on their own; that is the test of a good plan.

`scripts/build_plan.py plan.json <outdir>` renders
`<slug> - Storyline plan.xlsx` with three sheets: **Plan** (the rows),
**Storyline** (the titles in reading order), **Data request** (the rows with
data needs, for the client and the agents). The ghost deck is built from the
same JSON in the workspace (`SKILL.md`, "The ghost deck").

## Plan JSON

```json
{
  "title": "Car Wash in Spain",
  "subtitle": "Storyline plan for the readout",
  "client": "Moeve", "date": "October 2026", "slug": "moeve-car-wash",
  "slides": [
    {"type": "cover", "title": "Car Wash in Spain", "content": "Market opportunity and unit economics…"},
    {"type": "agenda"},
    {"type": "exec_summary", "title": "<bottom line sentence>"},
    {"type": "divider", "section": "Market"},
    {"type": "content", "section": "Market",
     "title": "The market is cars × penetration × frequency × ticket — two drivers uncertain",
     "content": "What the slide says: the expression, the four leaf drivers, which are uncertain",
     "exhibit": "Driver tree: market expression → variables → leaf drivers with confidence (rebuilt; cells of the model)",
     "exhibit_title": "Spain car-wash market — expression and driver tree",
     "data": "DGT car parc; consumer survey (frequency); flagship ticket data",
     "owner": "agent",
     "purpose": "Shows the client where the judgement sits before any number is shown",
     "image_prompt": "",
     "status": "planned"}
  ]
}
```

## Columns (one per slide)

| Column | What goes in it |
| --- | --- |
| `#` | Running number (auto). |
| `section` | The part of the storyline (Context, Market, Competition, Company, Appendix…). |
| `type` | `cover`, `agenda`, `divider`, `exec_summary`, `content`, `appendix`. `appendix` is the Appendix divider; the slides after it are `content` rows with `section: "Appendix"`. Structure rows are tinted in Excel. |
| `title` | The **action title**: the finding as one sentence with its number, never a topic. It carries the argument. Before the analysis it is a hypothesis; the deliver step rewrites it to what the data shows. |
| `content` | What the slide will say in 1–3 lines. |
| `exhibit` | The analysis that proves the title, by kind (chart type, table, driver tree, 2×2, harvey, heatmap, waterfall, text) and what it plots — and, where known, how it will reach the slide (a saved chart, a model cell or range, a validated insight, or rebuilt; `cdd-storyline.md`). |
| `exhibit_title` | The title above the exhibit, with its unit (optional; derived from `exhibit` if absent). |
| `data` | What data the exhibit needs and where it comes from; long-lead items flagged. Feeds the Data request sheet and the research agenda. |
| `owner` | Who builds it: `consultant`, `analyst`, `engineer`, `agent`, `client`. |
| `purpose` | The so-what: why this slide is in the deck and what it makes the reader believe or decide. |
| `image_prompt` | Optional: a prompt for an illustrative image (subject, flat style, navy/blue palette, no text). Empty where a chart carries the slide. |
| `status` | `planned`, `in progress`, `drafted`, `final`. |

## Conventions

- Titles argue; sections group. "Market size" is wrong; "The SAM is €1.1bn
  and grows 4% a year" is right.
- One exhibit per slide. Two exhibits → two rows.
- Every `content` row has a `purpose`; a row whose purpose does not change
  what the reader believes is cut.
- Every exhibit that needs data not already in hand has a `data` entry; the
  Data request sheet is the first thing sent to the client.
- The agenda closes with one "Appendix". A `divider` named Appendix counts as
  the `appendix` row, never a second entry; the executive summary has one
  row per section, Appendix excluded.
- 25–35 rows for a demo or interim readout, 40–55 for a full CDD.
