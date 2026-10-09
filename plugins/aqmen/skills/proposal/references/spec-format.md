# Scope spec format (JSON → Word)

`scripts/build_scope.py spec.json out.docx` renders a spec into the house-style
Word document. The spec holds all content; the script holds all formatting. Keep
prose in the spec so the consultant can edit either the JSON or the resulting
`.docx`.

A complete worked example: `assets/example-meridian.json` (a CDD scope).

## Top level

```json
{
  "header":  {"left": "AQMEN · Project X proposal", "right": "Strictly private & confidential"},
  "footer":  "Aqmen AI Limited | Prepared under NDA",
  "cover":   { ... },
  "sections": [ {"heading": "1 · Context and objectives", "blocks": [ ... ]}, ... ],
  "closing": "Aqmen AI Limited · Company No. … · aqmen.ai"
}
```

`cover` fields: `kicker` (small caps line, e.g. "Proposal to Ares Management |
Opportunistic Credit"), `title`, `subtitle` (one-line promise), `summary` (2–3
lines: what, for whom, how long), `confidentiality`, `date`, `footer_lines`
(list of 1–2 strings; see `aqmen-boilerplate.md`).

## Inline markup

Inside any text: `**bold**` and `_italic_`. Nothing else. Use bold for the lead
phrase of a bullet ("**AI-first consulting.** The Aqmen team …"), which is how
the house style signals structure without headings.

## Blocks

Each section has `blocks`, rendered in order. Types:

| type | fields | renders as | use for |
| --- | --- | --- | --- |
| `para` | `text` | body paragraph | prose |
| `label` | `text` | small navy caps line | introducing a group ("THE DECISION ARES FACES") |
| `bullets` | `items[]` | bulleted list | most content |
| `numbered` | `items[]` | numbered list | ordered steps, layers |
| `callout` | `items[]` | light-blue box, one paragraph per item | the client's questions, fee box, key facts |
| `hypotheses` | `items[]` of `{id?, text, confidence?, importance?, action?}` | box with H1/H2… in navy, statement in italics, ratings in grey | hypotheses of a workstream |
| `subheading` | `text` | small navy bold | "Approach", "Data and sources", "Outputs" inside a workstream |
| `workstream` | `title`, `blocks[]` | navy heading with left bar, then nested blocks | one per workstream |
| `table` | `columns[]`, `rows[][]`, `widths[]?`, `header?`, `bold_first?` | navy header row, light borders | deliverables, timeline, team, workplan, data request |
| `columns` | `columns[]` of `{title, items[]}` | side-by-side boxes with navy titles | phases of a build engagement (Month 1 / 2 / 3) |
| `gantt` | `columns[]` (week labels), `rows[]` of `{name, bars[[from,to]], owner?}`, `milestones[]` of `{column, label}`, `label?`, `label_width?` | Gantt drawn as a table: navy bars per week, azure diamonds for gates and sessions | the workplan — always include one; it is the fastest way to read the project |
| `quote` | `text` | grey italic with left bar | client verbatims |
| `page_break` | — | page break | before a long section if needed |
| `signature` | `parties[]` of `{party, name, title}` | two-column signature block | build/contract-style proposals |

Table `widths` are in dxa (twentieths of a point); the text width is **9411**.
Good defaults: two columns `[2381, 7030]`; three `[1500, 2600, 5311]`; a
workstream × weeks grid `[1900, 2504, 2504, 2503]`; a data request
(Item | Owner | By) `[5511, 2200, 1700]`; an options table with equal columns
(pass `"bold_first": false` so no column reads as a row label).

A complete build-engagement example: `assets/example-build.json`. Cells accept a string or a
list of strings (one paragraph each).

Gantt example (bars are inclusive, 1-based week numbers):

```json
{"type": "gantt",
 "columns": ["W1\n6 Oct", "W2\n13 Oct", "W3\n20 Oct"],
 "rows": [
   {"name": "WS1 Market model", "owner": "Ignacio + agent", "bars": [[1, 3]]},
   {"name": "WS4 Adviser interviews", "owner": "Analyst", "bars": [[1, 2]]}
 ],
 "milestones": [{"column": 1, "label": "Kick-off"}, {"column": 3, "label": "SteerCo"}]}
```

Keep week labels short (two lines max: week number, start date). For programmes
longer than ~12 weeks, use one column per fortnight or per month.

Hypothesis ratings use `Low` / `Medium` / `High`. `action` is the client
decision the hypothesis unlocks; render it only where it adds something.

## Conventions the renderer relies on

- Section headings are numbered by you: `"1 · Context and objectives"` (middle
  dot, not a hyphen).
- Workstream titles: `"Workstream 2: Pricing sustainability, fee pressure and the impact of AI"`.
- Hypothesis IDs default to H1, H2… per box; the Meridian convention restarts at
  H1 in each workstream.
- Leave fees as `£[XX]k` unless the consultant gave a number.
- No empty strings in `items` — the renderer will happily print an empty bullet,
  and that is exactly the defect the quality gate exists to catch.
