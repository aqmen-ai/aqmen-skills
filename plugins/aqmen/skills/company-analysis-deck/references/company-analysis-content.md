# Company Analysis — content (shared)

The **format-agnostic** spec of *what* an aqmen company analysis deliverable
covers: the narrative, the topics and their so-whats, the module rules, and what
to gather from the aqmen workspace. Both formats render **this** content and differ
only in presentation:

- **HTML report** → `company-analysis-structure.md` (document sections + ECharts)
- **PPTX deck** → `company-analysis-deck-structure.md` (slide sequence + `aqmen_deck.py`)

This file is the single source of truth for content, so the two formats never
drift. Read it alongside `report-standards.md` (voice, base-first, sources &
confidence) and `report-data.md` (how to pull the analysis). Build only once you
have the whole model; never invent numbers or sources.

## Objective

Assess the target's financial trajectory and value the business to inform a
specific decision. State the question answered and which statements are in scope.
Lead the deliverable with the so-what — the **valuation range** or the key margin
/ value-creation finding.

## What the deliverable must cover

Each topic below carries a so-what; the format docs decide how to render it (a
report section vs. one or more slides). The order mirrors how aqmen builds the
analysis. Omit a topic only if it genuinely doesn't apply, and say so.

1. **Objective & scope of use** — the question answered and the decision it
   informs; which statements are in scope (income statement / cash flow / balance
   sheet) and the precision level. Headline conclusion stated up front.
2. **Data landscape** — what's disclosed (line items, segment breakdowns,
   non-GAAP bridges) and whether cash-flow / balance-sheet detail is observable;
   where figures had to be estimated.
3. **Operating performance (income statement)** — the revenue build (volume ×
   price / growth / segment sum) and the **margin bridge** as the chain of named
   results (Gross Profit → EBITDA → EBIT → EBT → Net Income); cost structure
   (fixed vs variable, COGS decomposition); revenue, growth, key margins.
4. **Cash generation (cash flow)** — if in scope: Net Income → CFO → FCF → net
   change in cash (indirect method); cash conversion.
5. **Balance sheet & working capital** — if decision-relevant: NWC, leverage, and
   the days-based levers (DSO / DIO / DPO) and their effect on cash.
6. **KPIs & margins** — the ratio outputs (Gross Margin %, EBITDA Margin %,
   Revenue Growth %, …).
7. **Valuation (DCF)** — the FCFF spine (EBIT → NOPAT → FCFF → discounted cash
   flows → **Enterprise Value**); the **WACC** build (CAPM inputs); the terminal
   method (Gordon growth or exit multiple) with a **terminal-share sanity check**;
   the enterprise → equity bridge (net debt, shares → **value per share**); and a
   **WACC × terminal** sensitivity.
8. **Scenarios** — for each: the **hypotheses** it activates (management actions or
   market claims) in words, then the **input changes vs Base** that
   quantify it. Keep thesis and numbers visibly separate. Base first.
9. **Sources & confidence** — attribution for every quantitative claim (source,
   confidence 1–5, note), per `report-standards.md`.

## Module rules (analytical non-negotiables)

- Build only the **statements that are in scope** — don't force a balance sheet or
  cash flow the decision doesn't need; say why it's excluded.
- Keep the **margin bridge legible** — show the named steps, not every input node.
- Show **valuation as a range**, never a false-precision point; always
  **sanity-check the terminal value's share** of enterprise value and flag if it
  dominates.
- Distinguish **input** (researched) figures from **computed** (derived) ones so
  the reader knows what's an assumption.
- Present a **validated Base case before any scenario**.

## What to gather from aqmen

See `report-data.md` for the shared flow. For company analysis, gather:

- the **brief** from the workspace docs: the decision, the questions, the
  company, the fiscal year, the currency and the statements in scope;
- the **statement sheets** of the model spreadsheet (income statement,
  cash flow, balance sheet, DCF), with `show_spreadsheet_range` for the
  tables as a reader sees them and `read_spreadsheet` for which rows are
  inputs and which are computed, the per-period values and the growth
  rates;
- the **KPI block** (margins, growth, the business's own KPIs) and the
  **valuation**: the FCFF spine, the WACC build, enterprise and equity
  value, value per share, terminal value and its share of enterprise
  value;
- for each historical figure, the **dataset** it comes from (the filing,
  the page), its confidence and method;
- the **bridge** and **driver tree** charts over the model;
- the **insights** that answer the brief's questions;
- the **scenarios**, if any: the hypotheses each activates (the claim,
  the lines it moves, the realization).
