---
name: model
description: 'Build the model behind a strategic decision on the aqmen platform — a market sizing, a company P&L and valuation, a competitive landscape, or a custom driver model — as datasets adapted by transformations into an Excel-compatible spreadsheet, drawn as charts. Use for "build the sizing / the model / the P&L / the landscape", "model the market", "set up the driver tree", or after aqmen:research. Step 3 of the aqmen project flow; aqmen:challenge reviews it.'
---

# Model — the chain from data to answer

A model on aqmen is a chain, and every number the reader sees traces down
it: **datasets** at the grain their sources publish → **transformations**
that adapt each driver to the model's grain (the SQL is the method) → one
**feed** transformation joining them → a **spreadsheet** connected to the
feed, with calculated columns holding the variables → **charts** (driver
trees, bridges) over the spreadsheet's ranges.

Read `references/practice.md` once per session. Then read the MCP topics
`modeling` and `spreadsheets` before the first write. They are the spec.
This skill adds the framework guidance, the order and the gate.

## 1. Pick the framework

The brief names it (`describe_workspace`, the workspace docs). If it does
not, ask.

| Framework | Follow |
| --- | --- |
| Market sizing | The MCP's `market-sizing` topic, stages 1 to 9. Nothing to add here. |
| Company analysis | `references/company-analysis.md` |
| Competitive landscape | `references/competitive-landscape.md` |
| Custom | The `modeling` topic: the chain, adaptation, dependencies, hypotheses. |

## 2. Build in layers, confirming each

Step-by-step by default. After each layer, summarise in plain words and
wait, unless the user said "go autonomous".

1. **Structure.** The dimensions and their segments, the top expression,
   the variables and their drivers, each driver's dependencies with a
   one-line reason. Propose it, grounded in what research found. Push for
   the segmentation a diligence reader expects; under-segmenting is the
   common failure.
2. **Structure gate.** Run **aqmen:challenge** with the structure critic
   now, before values matter. Fixing structure after values are in means
   redoing research.
3. **Adaptations.** One transformation per driver that needs one
   (aggregate, allocate, broadcast, proxy, interpolate), with a `method`
   column where rows differ and docs stating the method and confidence.
   `run_transformation`, then check the output with `run_sql`.
4. **The feed.** One transformation joining the adapted drivers: one row
   per leaf segment per period, ordered by segment then period, no nulls.
   Check null counts by driver and period with `run_sql`.
5. **The spreadsheet.** `create_spreadsheet`, then `update_spreadsheet`
   with `addConnection` to the feed and `calculated` columns for the
   variables and the top measure, each with a `unit`. Pass `checks` on the
   totals you know. Read the report and the lint; fix what applies.
   Totals go in a summary block, never as rows in the rectangle.
6. **Charts.** `create_chart` with a `driver-tree` over the model's range,
   the dimensions as levels and the top measure first. Add a `waterfall`
   for the bridge between two periods where the brief asks what moved.
   `show_chart` to put them on screen.
7. **Describe it.** `annotate_spreadsheet` and `annotate_workspace`/`edit_docs`:
   what the model is, its grain, its assumptions, how to read it. File
   everything in the project's collection. Append a line to the brief's Log.

Missing data at any layer goes back to **aqmen:research**, never into a
typed constant. A number typed into a formula is lint; it belongs in a
labelled, noted input cell or, better, in a dataset.

## 3. Forecasts and scenarios

Only after Base is complete and the user has validated it. Follow the
`modeling` topic's hypotheses section: a scenario is its hypotheses,
history never differs by scenario, a cell no hypothesis touches holds flat.

## Gate

- The structure critic has passed, or its findings are resolved or
  accepted by the user.
- `read_spreadsheet` shows no formula errors, no stale or broken
  connection, and no lint left unexplained.
- `checks` hold, and two grains of the same model agree on the total.
- The bottom-up total is within 20% of a published top-down figure, or
  the gap is explained by a named assumption.

Then offer **aqmen:challenge** for the values critic before anyone calls
the model done.
