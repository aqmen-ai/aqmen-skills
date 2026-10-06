# CDD content format (JSON → deck + HTML + Word summary)

`scripts/build_cdd.py content.json <outdir>` renders one content file into the
three deliverables. The file holds every word and number; the scripts hold the
layout. Worked example: `assets/example-carwash.json`.

## Top level

```json
{
  "title": "Car wash in Spain",
  "subtitle": "Market opportunity and unit economics of a forecourt car wash",
  "slug": "moeve-car-wash",
  "doctype": "Commercial Due Diligence",
  "client": "Moeve",
  "project": "Project Bubbles",
  "author": "Aqmen",
  "date": "September 2026",
  "confidence": 3,
  "bottom_line": "One sentence: the answer and the decision it informs.",
  "exec_summary": [["Context", ["bullet", "bullet"]], ["Market", ["…"]], ["Competition", ["…"]], ["Company", ["…"]]],
  "kpis": [["€1.2bn", "SAM, 2025", "▲ 4% CAGR"], ["3.8 yrs", "Payback, base", null]],
  "need_to_believe": ["assertion with number and evidence", "…"],
  "parts": [ {"name": "Context", "subitems": ["Objective", "Data"], "intro": "optional paragraph", "sections": [ … ]}, … ],
  "sources": [["Source name", 5, "what it supports"], …]
}
```

- `parts` are the four CDD parts in order (Context, Market, Competition,
  Company). Each becomes an agenda slide in the deck and a numbered chapter in
  the HTML. `subitems` show under the part on the agenda slide.
- The renderer always closes with an **Appendix** (divider, then Sources &
  confidence). A part named `Appendix` (any case, any position) merges into it:
  no second divider or agenda entry; its sections render after the Appendix
  divider and before Sources, its `subitems` under Appendix on the agenda. In
  the HTML it becomes the last chapter, with Sources as its final subsection.
  The Word summary leaves it out.
- `exec_summary` rows render as the banded exec-summary slide, the HTML
  summary and the Word summary bands.
- `kpis` are `[value, label, delta_or_null]`; three or four.
- `sources` are `[name, confidence 1–5, note]`; feed the closing table.

## Sections

Every section has `kind`, `title` (short, for the eyebrow and chapter list),
`headline` (the finding, one sentence, this is the slide title), optional
`so_whats` (2–3 bullets for the Key Takeaways rail), optional `watchout`,
`source`, `illustrative` (true marks directional exhibits). Body bullets are
`["text", bold, level]` or plain strings.

| kind | extra fields | deck | HTML |
| --- | --- | --- | --- |
| `content` | `body`, `left_title` | headline + bullets + takeaways rail | bullets + insight callout |
| `scenario` | same as content | same; use `left_title` "Trend" / "Initiative" | same |
| `table` | `columns`, `rows`, `chart_title` | bullet list (native table pending) | HTML table |
| `chart` | `chart: {kind: column\|bar\|line\|stacked_column, categories, series: [[name, [values]]], number_format, legend, y_title}`, `chart_title` | native chart | ECharts |
| `waterfall` | `steps: [[label, value, is_total]]`, `chart_title`, `number_format` | stacked column bridge | ECharts waterfall |
| `mekko` | `mekko: [[label, width, [[segment, value], …]], …]`, `chart_title` | Marimekko; segment named "Whitespace" hatches | CSS Marimekko |
| `driver_tree` | `tree: [{header, nodes: [{label, value, short_value, certainty 0/1/2, expr, parent, operator}]}]`, `note`, `chart_title` | expression tree | CSS tree |
| `positioning` | `items: [{label, num, points: [[x, y]]}]`, `x_title`, `y_title`, `x_ticks`, `y_ticks` | archetype 2×2 | CSS matrix |
| `harvey` | `columns` (players), `rows: [[criterion, [fills 0–1]]]`, `row_header` | harvey-ball matrix | SVG balls |
| `heatmap` | `cols`, `rows`, `values`, `base: [r, c]`, `col_header`, `row_header`, `value_fmt` | shaded grid | shaded grid |
| `revenue_build` | `groups: [{archetype, players: [{name, hq, employees, revenue, pct, market_rev}]}]`, `total`, `unit`, `info_cols` | revenue build | table with bars |

Series values are numbers; `null` allowed only in `revenue_build` players
(revenue-only players).

Driver-tree boxes are small. The deck steps a label or value from 8pt down to
6pt to fit its box, then cuts the value with "…". Give a long `value` a
`short_value` (e.g. "€1.2bn" for "€1.2bn (2024, est.)"): the deck uses it when
the full value won't fit at 6pt; the HTML always shows `value`.

## Refs to the workspace

A section may carry a `ref` to the workspace object its numbers come from, so
a rebuild re-reads them instead of copying by hand:

```json
"ref": {"chartId": "ch_…", "resolved": "2026-10-06"}
"ref": {"spreadsheetId": "ss_…", "sheet": "Market", "range": "B4:H9", "resolved": "2026-10-06"}
```

The agent resolves each ref before building (`get_chart` for a chart's rows,
`read_spreadsheet` for the range), writes the literal values into the
section's own fields (`chart`, `steps`, `rows`, …), and sets `resolved` to the
date. The ids stay in `ref`; on the next build, resolve again and overwrite.
The renderer never calls the workspace: it refuses a section whose `ref` has
no `resolved` or whose data fields are empty, naming the section.

## Conventions

- Headlines are findings, not topics: "The SAM is €1.1bn and grows 4% a year",
  not "Market size".
- One exhibit per section. If a topic needs two charts, make two sections.
- Numbers in headlines carry units. Use `illustrative: true` for any shape that
  is modelled rather than measured.
- Keep `so_whats` to what changes the reader's mind; the rail is small.
- `slug` names the output files; keep it short and stable across iterations.
