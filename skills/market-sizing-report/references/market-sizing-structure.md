# Market Sizing Report — structure

The fixed section order for a market sizing output report. It mirrors how aqmen
builds a market sizing analysis (goal → research → scope → segmentation →
drivers → values → validate → scenarios), so the report reads as the conclusion
of that build. Omit a section only if it genuinely doesn't apply, and say so.

Read `report-standards.md` (tone, sources, confidence) and `report-style.md`
(design) first. Use `report-template.html` as the skeleton.

## Sections

1. **Objective & scope of use** — the question the sizing answers and the
   decision it informs; the precision level targeted. Lead with the headline
   number here in one line.
2. **Market definition** — what's in and out of scope, geography, time horizon &
   granularity (e.g. annual, base year ±5), currency.
3. **Data landscape** — what public data exists, what breakdowns were available,
   and where gaps forced estimates. Be explicit about thin spots.
4. **Segmentation** — the dimensions and segments used, and why each axis is
   analytically justified (not decorative). Note if the tree is
   asymmetric-but-complete.
5. **Sizing methodology** — the market expression (e.g. Price × Quantity, or
   Underlying Market × Attachment Rate) and the **driver tree**: the economic
   levers, and whether the approach is top-down, bottom-up, or both.
6. **Headline market size & trajectory** — the Base-case size and its
   time-series (base year + projection). KPI tiles for TAM (and SAM/SOM if
   modelled) and CAGR; a line/area chart for the trajectory.
7. **Triangulation & validation** — bottom-up vs top-down reference cross-check.
   **Explain any divergence > ~20%.**
8. **Sensitivity** — which drivers move the answer most; a simple ranked bar or
   tornado. State the swing range.
9. **Scenarios** — for each scenario: the **Trend** (qualitative directional
   thesis) in words, then the **driver-assertion overrides vs Base** that
   quantify it. Keep thesis and numbers visibly separate. Base first.
10. **Sources & confidence** — the shared closing table (see `report-standards.md`).

## Market-sizing specifics

- Distinguish **TAM / SAM / SOM** clearly if the model expresses them; don't
  conflate the total market with the serviceable/obtainable slices.
- Percentages and rates: state the base they apply to.
- When a value is a modelled estimate rather than sourced, label it and give it
  the appropriate low confidence — don't let estimates masquerade as data.
- The driver tree can be summarised as an indented list or a simple nested
  diagram; don't dump every cell — show the levers that matter.

## Suggested charts (ECharts)

- **Headline size & trajectory** — line/area of the time series; a **funnel** for
  TAM → SAM → SOM.
- **Segmentation** — stacked or grouped bar of the market by dimension.
- **Sensitivity** — **tornado** (horizontal diverging bars) ranking the drivers
  that move the answer most.
- **Triangulation** — grouped bar comparing bottom-up vs top-down.
- **Driver tree** — an indented list or simple bar; don't force a chart if a list
  is clearer.

## What to gather from aqmen

See `report-data.md` for the shared flow. For a market sizing report, gather:

- the **market definition & scope** — geography, time horizon & granularity,
  currency, and what's in/out;
- the **segmentation** (dimensions and segments) and the **driver tree**, with
  each item's format and unit;
- the **computed market values** — the total, the trajectory by period, and
  splits by segment — and the market expression behind them;
- for each value, its **source, confidence (1–5), and note**;
- the **list of sources** used across the analysis;
- the **scenarios** and their qualitative **Trend** levers (direction, magnitude,
  note). For sensitivity, compare driver/segment deltas across scenarios or flag
  the lowest-confidence, highest-leverage drivers.
