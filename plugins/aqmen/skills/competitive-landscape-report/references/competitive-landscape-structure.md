# Competitive Landscape Report — structure (HTML)

How to render the competitive landscape **content** as a self-contained HTML
report. `competitive-landscape-content.md` is the single source of truth for
*what* to cover, the module rules, and what to gather from aqmen — read it first.
This file covers only *how* to lay that content out as a document. Also read
`report-standards.md` (voice, sources, confidence) and `report-style.md`
(design); build from `report-template.html`.

## Section order

Render the content topics as document sections, in this order (omit one only if
it genuinely doesn't apply, and say so):

1. **Objective & scope of use** — lead with the headline takeaway in one line.
2. **Data landscape**
3. **Player set, tiering & archetypes** — explain the long-list → shortlist logic.
4. **Comparison framework** — the fields and why each is decision-relevant.
5. **The benchmark** — the players × fields table of key metrics; highlight the
   standout figures.
6. **Positioning** — a positioning chart (e.g. scatter on two axes) if it
   clarifies who's winning and how players cluster.
7. **Reliability review** — coverage strong / moderate / weak, sparse fields
   called out explicitly.
8. **So-what / implications**
9. **Scenarios** — if any; Base first.
10. **Sources & confidence** — the shared closing table (see `report-standards.md`).

## Exhibits

Flagship exhibits are self-contained HTML/CSS (match the deck — see the "Flagship
exhibits" section of `report-style.md`); other charts are ECharts.

- **Revenue build** (`table.rbuild`) — **lead with this**: players by archetype,
  each `revenue × % addressable = market revenue` (bar), summed bottom-up to the
  market total. The central competitive-landscape exhibit.
- **Archetype map** (`.pmatrix`) — 2-axis positioning; each archetype is the
  **bounding box** of its players' points, with unlabelled dots. Names are in the
  revenue build.
- **Benchmark** — the players × criteria **harvey-ball table** (consistent-size
  SVG balls, fills 0–1), or a sorted horizontal **bar** for a single measured field.
- **Archetypes** — grouped bar or scatter clustering by strategy.

_Content, module rules (apples-to-apples, tiering, mandatory reliability review,
`web` not `ai`, …), and what to gather from aqmen: see
`competitive-landscape-content.md`._
