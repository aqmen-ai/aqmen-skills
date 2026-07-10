# Market Sizing Report — structure (HTML)

How to render the market sizing **content** as a self-contained HTML report.
`market-sizing-content.md` is the single source of truth for *what* to cover, the
module rules, and what to gather from aqmen — read it first. This file covers
only *how* to lay that content out as a document. Also read `report-standards.md`
(voice, sources, confidence) and `report-style.md` (design); build from
`report-template.html`.

## Section order

Render the content topics as document sections, in this order (omit one only if
it genuinely doesn't apply, and say so):

1. **Objective & scope of use** — lead with the headline size in one line.
2. **Market definition**
3. **Data landscape**
4. **Segmentation & driver tree** — summarise as an indented list or a simple
   nested diagram; don't dump every cell.
5. **Headline market size & trajectory** — KPI tiles for TAM (and SAM/SOM if
   modelled) and CAGR; a line/area chart for the trajectory.
6. **Triangulation & validation**
7. **Sensitivity**
8. **Scenarios** — Base first; state the Trend thesis in words, then the overrides.
9. **Sources & confidence** — the shared closing table (see `report-standards.md`).

## Exhibits

Flagship exhibits are self-contained HTML/CSS (match the deck 1:1 — see the
"Flagship exhibits" section of `report-style.md`); everything else is ECharts.

- **Market structure** — the **value/expression tree** (`.dtree`): market
  expression → variables (with formulas) → leaf drivers, certainty dots. Note
  segmentation with `.dtnote`; don't explode every segment.
- **TAM / SAM** — one or two **Marimekkos** (`.mekko`, variable-width): TAM by
  region with `SAM` (solid) + `Whitespace` (hatched), then SAM split by another
  dimension (e.g. deal size).
- **Trajectory** — stacked column split by region (evolution by dimension), or a
  line/area of the time series.
- **Sensitivity** — **tornado** (horizontal diverging bars) ranking the drivers.
- **Triangulation** — grouped bar comparing bottom-up vs top-down.

_Content, module rules (TAM/SAM/SOM distinct, label estimates, …), and what to
gather from aqmen: see `market-sizing-content.md`._
