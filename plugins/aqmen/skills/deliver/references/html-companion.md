# The HTML report — the deck's written companion

An optional, self-contained HTML document for readers who want the argument
in prose: the same storyline as the deck, the same figures, more room for
method and caveats. It lives **in the project as a page** — one `.html`
file Aqmen hosts in Deliverables and shows in a sandboxed frame, with the
deck and charts it was built from pinned beside it — so the reader opens it
where the deck is, and the page says when its sources move. The deck
remains the deliverable of record. When the reader wants Word, or the
write-up should stay live figure by figure, build a doc instead (`doc.md`).

Read `report-style.md` (the design system), the use case's section
structure (for a CDD, the "HTML report — sections" of each workstream
file), and `read_instructions('pages')` before the first `create_page`.

## The rule: the report's figures are the deck's

So that deck and report can never disagree, build the report **after** the
deck passes its hand-over gate, and read its figures from the deck:

1. `read_deck` (with `slides` for a large deck). Each sourced element's JSON
   carries the data the server pinned — a chart's series, a table's cells,
   a KPI's text — and its source line says what it was read from and when.
2. Every number in the report comes from that JSON: a chart's series
   become the ECharts series; a KPI text becomes the KPI tile; a range's
   cells become the table. Quote them as the deck shows them.
3. An exhibit the report draws but the deck does not (the marimekko, the
   expression tree, a tornado): read its figures from the same workspace
   artifacts the deck's sourced elements name (`read_spreadsheet` on the
   same cells, `get_chart` on the same chart) — never a fresh query that
   computes them another way.
4. Every figure in the report appears in a **Where each number lives**
   table in the appendix: figure → deck slide → workspace source, by its
   display name and the publication behind it — never SQL or a table
   identifier.

If the deck changes (a refresh, an edit), the page says so — "N sources
changed" — and **aqmen:refresh** rebuilds the report from the new version
and replaces the file (`update_page` with the new `html`); note the deck
version on the cover.

## Building it

1. Pick the template: `assets/<module>-report-template.html` for the
   workstream (market sizing, company analysis, competitive landscape; a
   full CDD starts from one and adds the others' sections in storyline
   order).
2. **Copy it to a working file** with a shell command
   (`cp assets/market-sizing-report-template.html <project>-report.html`),
   carrying the CSS, CSP, head and inlined logo at zero cost.
3. **Edit only the content** with targeted edits: the `[bracketed]`
   placeholders and the example text, section by section, in the use
   case's order. Never rewrite the whole file, never re-emit the `<style>`
   block or the base64 logo.
4. Keep it one HTML file, rendering in a sandboxed cross-origin iframe:
   inline CSS and JS, `data:` images, ECharts from the pinned cdnjs include
   only; the CSP untouched. The frame has no Aqmen session: everything the
   page shows must be in the file.
5. Lead with the bottom line; Base before scenarios; watch-outs from the
   data; close with Sources and confidence.

## Storing it

`create_page` in the project (`projectId`), in the Deliverables collection
(`collectionId`), with the file's text as `html` (or `uploadId` from
`create_upload_slot` for the file on disk), a `name` like
`<project>_report`, the report's title as `displayName`, one line of
`description`, and **`builtFrom`**: the deck, plus every chart and
spreadsheet range the report read directly (step 3 above) —

```json
"builtFrom": [
  {"kind": "deck", "deckId": "dk_…"},
  {"kind": "chart", "chartId": "ch_…"},
  {"kind": "spreadsheet", "spreadsheetId": "ss_…", "sheet": "Summary", "range": "B2:F9"}
]
```

Give the user the page's link. `update_page` with `notes` records how it
was built and what to check before sending. A later rebuild is
`update_page` with the new `html` and a `note` saying what moved — a new
version, the old one in History. The working file in the user's directory
may be deleted once the page is stored, unless they want the copy.
