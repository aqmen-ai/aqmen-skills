# Company Analysis Report — structure

The fixed section order for a company analysis output report. It mirrors how
aqmen builds a company analysis (goal → research → statements → margin bridge →
cash/working capital → KPIs → valuation → scenarios), so the report reads as the
conclusion of that build. Omit a section only if it genuinely doesn't apply, and
say so.

Read `report-standards.md` (tone, sources, confidence) and `report-style.md`
(design) first. Use `report-template.html` as the skeleton.

## Sections

1. **Objective & scope of use** — the question the model answers and the decision
   it informs; which statements are in scope (income statement / cash flow /
   balance sheet) and the precision level. Lead with the headline conclusion
   (e.g. valuation range or key margin finding) in one line.
2. **Data landscape** — what's disclosed (line items, segment breakdowns,
   non-GAAP bridges) and whether cash-flow / balance-sheet detail is observable.
   Be explicit where figures had to be estimated.
3. **Operating performance (income statement)** — the revenue build (volume ×
   price / growth / segment sum) and the **margin bridge** as the chain of named
   results: Gross Profit → EBITDA → EBIT → EBT → Net Income. Cost structure
   (fixed vs variable, COGS decomposition). KPI tiles for revenue, growth,
   key margins; a chart for the revenue trajectory or margin bridge.
4. **Cash generation (cash flow)** — only if in scope: Net Income → CFO → FCF →
   net change in cash (indirect method).
5. **Balance sheet & working capital** — only if decision-relevant: NWC, leverage,
   and the days-based levers (DSO / DIO / DPO) and their effect on cash.
6. **KPIs & margins** — the ratio outputs (Gross Margin %, EBITDA Margin %,
   Revenue Growth %, etc.) as a compact tile row or table.
7. **Valuation (DCF)** — the FCFF spine (EBIT → NOPAT → FCFF → discounted cash
   flows → **Enterprise Value**); the **WACC** build (CAPM inputs); the terminal
   method (Gordon growth or exit multiple) with a terminal-share sanity check;
   the enterprise → equity bridge (net debt, shares → **value per share**); and a
   **WACC × terminal** sensitivity table.
8. **Scenarios** — for each scenario: the **Initiative** (qualitative management
   action / thesis) in words, then the **input-node assertion overrides vs Base**
   that quantify it. Keep thesis and numbers visibly separate. Base first.
9. **Sources & confidence** — the shared closing table (see `report-standards.md`).

## Company-analysis specifics

- Only build the statements that are in scope — don't force a balance sheet or
  cash flow if the decision doesn't need it; say why it's excluded.
- Keep the **margin bridge** legible: show the named steps, not every input node.
- In valuation, always sanity-check the terminal value's share of enterprise
  value; flag if it dominates. Present a **range**, not a false-precision point.
- Separate **input** (researched) figures from **computed** (derived) ones so the
  reader knows what's an assumption.

## Suggested charts (ECharts)

- **Margin bridge** — a **waterfall** (Revenue → GP → EBITDA → EBIT → Net Income)
  using a transparent base series under the visible deltas.
- **Revenue / cash** — line or bar of the trajectory (revenue, FCF).
- **KPIs & margins** — small multiples or a grouped bar of margin % over time.
- **Valuation sensitivity** — a **heatmap** of value per share across WACC ×
  terminal assumptions.
- **Driver sensitivity** — **tornado** of the inputs that most move the valuation.

## What to gather from aqmen

See `report-data.md` for the shared flow. For a company analysis report, gather:

- which **statement groups** the model contains;
- for each statement in scope — the **income statement** (revenue build, margin
  bridge, and KPI/margin outputs), **cash flow**, **balance sheet**, and the
  **DCF valuation** (FCFF spine, WACC, enterprise & equity value, value per share,
  terminal value): the structure (which nodes are **inputs** vs **computed**), the
  per-period values, and growth rates;
- for each value, its **source, confidence (1–5), and note**;
- the **list of sources** used;
- the **scenarios** and their qualitative **Initiative** levers (direction,
  magnitude, note).
