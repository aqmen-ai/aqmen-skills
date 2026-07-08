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

## Charts (ECharts)

- **Headline size & trajectory** — line/area of the time series; a **funnel** for
  TAM → SAM → SOM.
- **Segmentation** — stacked or grouped bar of the market by dimension.
- **Sensitivity** — **tornado** (horizontal diverging bars) ranking the drivers.
- **Triangulation** — grouped bar comparing bottom-up vs top-down.
- **Driver tree** — an indented list or simple bar; don't force a chart if a list
  is clearer.

_Content, module rules (TAM/SAM/SOM distinct, label estimates, …), and what to
gather from aqmen: see `market-sizing-content.md`._
