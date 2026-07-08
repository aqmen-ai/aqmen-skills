# Company Analysis — content (shared)

The **format-agnostic** spec of *what* an aqmen company analysis deliverable
covers: the narrative, the topics and their so-whats, the module rules, and what
to gather from the aqmen MCP. Both formats render **this** content and differ
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
8. **Scenarios** — for each: the **Initiative** (qualitative management action /
   thesis) in words, then the **input-node assertion overrides vs Base** that
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

- which **statement groups** the model contains;
- for each statement in scope — the **income statement** (revenue build, margin
  bridge, KPI/margin outputs), **cash flow**, **balance sheet**, and the **DCF
  valuation** (FCFF spine, WACC, enterprise & equity value, value per share,
  terminal value): the structure (which nodes are **inputs** vs **computed**), the
  per-period values, and growth rates;
- for each value, its **source, confidence (1–5), and note**;
- the **list of sources** used;
- the **scenarios** and their qualitative **Initiative** levers (direction,
  magnitude, note).
