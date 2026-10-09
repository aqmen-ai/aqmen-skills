# Workstream: Market (market sizing)

What the Market part of a CDD deliverable covers, how each exhibit reaches
the deck, how the HTML report lays it out, and what to gather. The
**method** — stages, dimensions, the driver tree, the feed, values,
validation, scenarios, the critics' checklist — is the platform's
`market-sizing` topic (after `modeling`). Read it before modeling; this file
starts where the model is built.

## Objective

Size the market and its trajectory to inform a specific decision
(underwrite an investment thesis, prioritise entry). State the question
answered and the precision targeted. Lead with the headline number.

## What the part must cover

Each topic carries a so-what. Omit one only if it genuinely does not
apply, and say so.

1. **Objective and scope of use** — the question, the decision, the
   precision. Headline size up front.
2. **Market definition** — in and out of scope, geography, horizon and
   granularity, currency.
3. **Data landscape** — what public data exists, at which breakdowns, and
   where gaps forced estimates or allocations.
4. **Segmentation and driver tree** — the dimensions and why each is
   justified; the market expression (price × quantity, underlying ×
   attachment) and the levers; top-down, bottom-up or both.
5. **Headline size and trajectory** — Base size and its time series; TAM
   (and SAM/SOM where modelled) and the CAGR.
6. **Triangulation** — bottom-up against top-down; **explain any gap above
   ~20%** by a named assumption.
7. **Sensitivity** — which drivers move the answer most, and the swing.
8. **Scenarios** — each as the hypotheses it activates, in words, then the
   driver changes against Base. Base first.
9. **Sources and confidence.**

## The slides — elements and sources

The platform's `market-sizing` topic ends with this framework's sourceable
exhibits and the ones a slide cannot draw; follow it. In the storyline:

| Slide | Exhibit | How it reaches the slide |
| --- | --- | --- |
| Market definition | scope, in/out | typed |
| Method and driver tree | expression → variables → drivers, confidence per leaf | **rebuilt**: shapes and lines, each box's value a sourced `cell` of the model's summary (the demo deck `hr_software_market_readout` has the layout: `read_deck` it) |
| Headline size, TAM → SAM | size KPI; TAM/SAM by the main dimension | KPI from a `cell` or a `number` chart; a stacked or 100%-stacked `bar` chart (the sourceable cut of a marimekko) |
| SAM by the cuts that matter | market by segment | stacked `bar` chart, or a `range` when two dimensions matter |
| Trajectory | market over time by segment; CAGR | stacked `bar` or `line` chart; CAGR from a `cell` or in the insight headline |
| Growth bridge | what moved between two periods | `waterfall` chart over the model's bridge block |
| Sensitivity | drivers ranked by swing | horizontal `bar` chart over the sensitivity block, or its `range` |
| Scenarios | side by side, Base first | `range` over the scenario summary; hypotheses typed beside it |
| Triangulation (appendix) | bottom-up vs top-down | `bar` chart over the top-down dataset joined to the model total |
| What you need to believe | assumption, implied metric, reference, verdict, break-even | `range` over the model's `Believe` rows (`modeling`) |
| Sanity checks (appendix) | back-of-envelope tests, PASS/FLAG | `range` over the `Believe` sanity-check rows — never typed |

A figure a slide needs that the workspace has not saved yet goes back to
**aqmen:model** or **aqmen:conclude** to be saved as a chart or a summary
cell first.

## The HTML report — sections

1. Objective and scope of use — the headline size in one line.
2. Market definition.
3. Data landscape.
4. Segmentation and driver tree — the expression tree (`.dtree`), the
   levers that matter, not every cell.
5. Headline size and trajectory — KPI tiles (TAM, SAM/SOM, CAGR), a
   trajectory chart.
6. Triangulation and validation — grouped bar.
7. Sensitivity — tornado.
8. Scenarios — Base first, tabs.
9. Sources and confidence.

Exhibits: the expression tree and the marimekko (`.mekko`, TAM with hatched
whitespace) are the HTML's flagships — a report can draw what a slide
cannot. Their figures come from the same cells the deck's rebuilt tree and
bar read.

## Module rules

- Keep **TAM / SAM / SOM** distinct.
- Percentages and rates **state their base**.
- Estimates are labelled as estimates, at the confidence they deserve.
- Show the levers that matter, not every driver-tree cell.
- A **validated Base before any scenario**.

## What to gather

- The **brief**: decision, questions, definition, geography, horizon,
  currency, in and out.
- The **model spreadsheet** (`read_spreadsheet`): dimensions and segments,
  the calculated columns (expression, variables, units), the variants and
  their reasons, the summary blocks and their totals — the cells a deck
  sources.
- The **charts**: driver tree, bridge, trajectory, segment splits
  (`list_charts`; each one's type decides whether a slide can draw it).
- Per driver, its **dataset**: sources, method (the adapting
  transformation's docs), confidence.
- The **top-down reference** dataset and the gap.
- The **insights** that answer the brief's market questions, and their
  status.
- The **scenarios**: the hypotheses each activates, the realization, the
  summary block comparing them.
