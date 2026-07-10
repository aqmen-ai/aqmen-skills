# Company Analysis Report — structure (HTML)

How to render the company analysis **content** as a self-contained HTML report.
`company-analysis-content.md` is the single source of truth for *what* to cover,
the module rules, and what to gather from aqmen — read it first. This file covers
only *how* to lay that content out as a document. Also read `report-standards.md`
(voice, sources, confidence) and `report-style.md` (design); build from
`report-template.html`.

## Section order

Render the content topics as document sections, in this order (omit one only if
it genuinely doesn't apply, and say so):

1. **Objective & scope of use** — lead with the headline conclusion (valuation
   range or key margin finding) in one line.
2. **Data landscape**
3. **Operating performance (income statement)** — KPI tiles for revenue, growth,
   key margins; a chart for the revenue trajectory or margin bridge.
4. **Cash generation (cash flow)** — only if in scope.
5. **Balance sheet & working capital** — only if decision-relevant.
6. **KPIs & margins** — a compact tile row or table.
7. **Valuation (DCF)** — the FCFF spine → Enterprise Value; the WACC build; the
   terminal method with a terminal-share sanity check; enterprise → equity →
   value per share; a WACC × terminal sensitivity table.
8. **Scenarios** — Base first; state the Initiative thesis in words, then the
   overrides.
9. **Sources & confidence** — the shared closing table (see `report-standards.md`).

## Exhibits

The WACC tree and sensitivity heatmap are self-contained HTML/CSS flagship exhibits
(match the deck — see the "Flagship exhibits" section of `report-style.md`); the
rest are ECharts.

- **Revenue / cash** — line or bar of the trajectory (revenue, FCF).
- **Margin bridge** — a **waterfall** (Revenue → GP → EBITDA → EBIT → Net Income)
  using a transparent base series under the visible deltas.
- **Cost of capital (WACC)** — the **expression tree** (`.dtree`): WACC = wE·Ke +
  wD·Kd(1−t) → Ke = Rf + β·ERP, etc., cited leaf drivers + certainty dots.
- **Valuation sensitivity** — the **heatmap** (`table.heatmap`) of equity value /
  per share across WACC × terminal growth, base-case cell outlined.
- **Driver sensitivity** — **tornado** of the inputs that most move the valuation.

_Content, module rules (valuation as a range + terminal-value sanity check,
inputs vs computed, …), and what to gather from aqmen: see
`company-analysis-content.md`._
