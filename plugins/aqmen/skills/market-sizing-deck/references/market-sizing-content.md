# Market Sizing — content (shared)

The **format-agnostic** spec of *what* an aqmen market sizing deliverable covers:
the narrative, the topics and their so-whats, the module rules, and what to
gather from the aqmen workspace. Both formats render **this** content and differ only
in presentation:

- **HTML report** → `market-sizing-structure.md` (document sections + ECharts)
- **PPTX deck** → `market-sizing-deck-structure.md` (slide sequence + `aqmen_deck.py`)

This file is the single source of truth for content, so the two formats never
drift. Read it alongside `report-standards.md` (voice, base-first, sources &
confidence) and `report-data.md` (how to pull the analysis). Build only once you
have the whole model; never invent numbers or sources.

## Objective

Size the market and its trajectory to inform a specific decision (e.g.
underwrite an investment thesis, prioritise entry). State the question answered
and the precision targeted. Lead the deliverable with the headline number.

## What the deliverable must cover

Each topic below carries a so-what; the format docs decide how to render it (a
report section vs. one or more slides). The order mirrors how aqmen builds the
analysis, so the deliverable reads as the conclusion of that build. Omit a topic
only if it genuinely doesn't apply, and say so.

1. **Objective & scope of use** — the question answered and the decision it
   informs; the precision level. Headline size stated up front.
2. **Market definition** — what's in/out of scope, geography, time horizon &
   granularity (e.g. annual, base year ±5), currency.
3. **Data landscape** — what public data exists, which breakdowns were available,
   and where gaps forced estimates. Be explicit about thin spots.
4. **Segmentation & driver tree** — the dimensions/segments used and why each
   axis is analytically justified; the **market expression** (e.g. Price ×
   Quantity, or Underlying Market × Attachment Rate) and the economic levers.
   Note whether the approach is top-down, bottom-up, or both.
5. **Headline market size & trajectory** — the Base-case size and its time series
   (base year + projection); TAM (and SAM/SOM if modelled) and the CAGR.
6. **Triangulation & validation** — bottom-up vs top-down cross-check. **Explain
   any divergence > ~20%.**
7. **Sensitivity** — which drivers move the answer most; state the swing range.
8. **Scenarios** — for each: the **hypotheses** it activates (each a named
   claim) in words, then the **driver changes vs Base** that quantify them. Keep
   thesis and numbers visibly separate. Base first.
9. **Sources & confidence** — attribution for every quantitative claim (source,
   confidence 1–5, note), per `report-standards.md`.

## Module rules (analytical non-negotiables)

- Keep **TAM / SAM / SOM** distinct; don't conflate the total market with the
  serviceable/obtainable slices.
- Percentages and rates: **state the base** they apply to.
- Label modelled estimates as estimates and give them the appropriate low
  confidence — don't let estimates masquerade as data.
- Don't dump every driver-tree cell — show the levers that matter.
- Present a **validated Base case before any scenario**.

## What to gather from aqmen

See `report-data.md` for the shared flow. For market sizing, gather:

- the **brief** from the workspace docs: the decision, the questions, the
  market definition and scope (geography, horizon, currency, what is in
  and out);
- the **model spreadsheet**: its dimensions (the feed's segment columns)
  and segments, the calculated columns (the market expression and the
  variables, with their formulas and units), the variants per segment and
  their reasons, and the summary blocks with the totals;
- the **driver tree** and **bridge** charts (`get_chart`, `show_chart`),
  which already draw the decomposition and the change between periods;
- the **computed market values**: the total, the trajectory by period and
  the splits by segment, from the summary blocks or `run_sql` over the
  feed;
- for each driver, the **dataset** it comes from: its sources, its method
  (the adapting transformation and its docs: aggregated, allocated,
  broadcast, proxied, interpolated) and its confidence;
- the **top-down reference** dataset and the triangulation gap;
- the **insights** that answer the brief's questions;
- the **scenarios**, if any: the hypotheses each activates (the claim, the
  drivers it moves, the realization). For sensitivity, compare scenario
  totals, or flag the lowest-confidence drivers that move the total most.
