# Dot-Dash format (JSON → Excel + skeleton deck)

A Dot-Dash is the presentation plan: **one row per slide**, written before any
analysis is built. Reading the action titles top to bottom must argue the case
on their own; that is the test of a good Dot-Dash. It is shared with the client
as a skeleton deck to agree the storyline, so rework and scope creep drop.

`scripts/build_dotdash.py plan.json <outdir>` renders:
- `<slug> - Dot-Dash.xlsx` — three sheets: **Dot-Dash** (the plan), **Storyline**
  (titles in reading order), **Data request** (rows with data needs, for the
  client and the agents).
- `<slug> - Skeleton deck.pptx` — one slide per row in the house style: action
  title, exhibit title, a dashed placeholder box describing the exhibit, the
  purpose in the takeaways rail, and purpose / data / owner / image prompt in
  the speaker notes.

## Plan JSON

```json
{
  "title": "Car Wash in Spain",
  "subtitle": "Presentation plan for the Moeve readout",
  "client": "Moeve", "date": "October 2026", "slug": "moeve-car-wash",
  "slides": [
    {"type": "cover", "title": "Car Wash in Spain", "content": "Market opportunity and unit economics…"},
    {"type": "agenda"},
    {"type": "exec_summary", "title": "<bottom line sentence>"},
    {"type": "divider", "section": "Market"},
    {"type": "content", "section": "Market",
     "title": "The market is cars × penetration × frequency × ticket — two drivers uncertain",
     "content": "What the slide says: the expression, the four leaf drivers, which are uncertain",
     "exhibit": "Driver tree: market expression → variables → leaf drivers with certainty dots",
     "exhibit_title": "Spain car-wash market — expression & driver tree",
     "data": "DGT car parc; consumer survey (frequency); flagship ticket data",
     "owner": "agent",
     "purpose": "Shows the client where the judgement sits before any number is shown",
     "image_prompt": "Minimal flat illustration, navy on white, of a tree diagram flowing left to right into four labelled leaves; no text",
     "status": "planned"}
  ]
}
```

## Columns (one per slide)

| Column | What goes in it |
| --- | --- |
| `#` | Running number (auto). |
| `section` | The part of the storyline (Context, Market, Competition, Company, Appendix…). |
| `type` | `cover`, `agenda`, `divider`, `exec_summary`, `content`, `appendix`. Structure rows are tinted in Excel. |
| `title` | The **action title**: the finding as one sentence with its number, never a topic. This is the "dash" that carries the argument. |
| `content` | What the slide will say in 1–3 lines: the body bullets or the exhibit's message. |
| `exhibit` | The analysis that proves the title, named by kind (chart, Marimekko, driver tree, table, 2×2, harvey, heatmap, waterfall, text) and what it plots. |
| `exhibit_title` | The 14pt title shown above the exhibit on the slide (optional; derived from `exhibit` if absent). |
| `data` | What data the exhibit needs and where it comes from; long-lead items flagged. Feeds the Data request sheet. |
| `owner` | Who builds it: `consultant`, `analyst`, `engineer`, `agent`, `client`. |
| `purpose` | The so-what: why this slide is in the deck and what it makes the reader believe or decide. |
| `image_prompt` | The **prompt** to generate an illustrative image for the slide (not the image). Describe subject, style (flat, navy/blue palette, no text), composition. Leave empty where a chart carries the slide. |
| `status` | `planned`, `in progress`, `drafted`, `final`. |

## Conventions

- Titles argue; sections group. A title that reads "Market size" is wrong; "The
  SAM is €1.1bn and grows 4% a year" is right.
- One exhibit per slide. Two exhibits → two rows.
- Every `content` row has a `purpose`; a row whose purpose does not change what
  the reader believes is cut.
- Every exhibit that needs data not already in hand has a `data` entry; the Data
  request sheet is the first thing sent to the client.
- Keep to 25–35 rows for a demo/readout, 40–55 for a full CDD.
- The plan is also the bridge to the `cdd-output` content file: one Dot-Dash row
  → one content section (`kind` from `exhibit`, `headline` from `title`,
  `so_whats` from `purpose`). `build_dotdash.py --from-cdd content.json plan.json`
  goes the other way for existing analyses.
