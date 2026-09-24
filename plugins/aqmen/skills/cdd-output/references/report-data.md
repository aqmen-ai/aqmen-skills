# Using aqmen data (shared)

A report is only as good as how fully it draws on the analysis. aqmen holds far
more than headline numbers — every value carries a **source, a confidence score
(1–5), and a note**, plus computed outputs and scenarios. Use all of it via the
aqmen connector. **Never invent numbers or sources.**

> Shared verbatim across all aqmen report skills. Use whatever read tools the
> connector exposes to obtain each item below — this guide names the
> *information* to gather, not specific tools. Each `*-structure.md` says what to
> gather for its analysis type.

## Gather before you write

Pull the whole analysis from aqmen first — don't write from partial data:

1. **The analysis** — locate the project and the specific analysis you're
   reporting on.
2. **The model structure** — the shape of the analysis (its dimensions/drivers,
   statements/nodes, or dataset fields), with each item's format and unit.
3. **The computed values** — the numbers the model produces: headline outputs,
   time series, and per-segment / per-node results.
4. **Provenance for each value** — its source (and source type), its confidence
   (1–5), and any note.
5. **The source list** — the bibliography of sources used across the analysis.
6. **Scenarios** — the base case and each scenario, plus the qualitative levers
   behind them (the directional hypotheses/actions, with their direction,
   magnitude, and notes).

## Use the data fully — this is what makes a report high quality

- **Numbers come from the model.** Headline figures, KPIs, and every chart series
  are the computed values aqmen returns — not estimates you produce. Don't round
  away precision the model has, and don't add figures the model doesn't contain.
- **Citations come from the model.** Every value has a source (with its type and
  reference), a confidence (1–5), and a note. **Populate the Sources & confidence
  table directly from these** — map source type → the Type column, confidence →
  the badge, note → the Note. Never fabricate a source or a score.
- **Watch-outs are data-driven.** Surface, automatically, as ⚠ watch-outs:
  - values with **confidence ≤ 2**,
  - values whose only support is an **unreferenced model estimate** (no external
    source) or a **news article** (confidence capped at 3),
  - notable **gaps / uncovered** cells,
  - the **drivers/inputs that most move the result** (from sensitivity or scenario
    deltas).
  aqmen gives you confidence per value — let the weak spots drive the watch-outs.
- **Scenarios: Base first.** Present the validated Base case, then each scenario
  as its qualitative lever (direction, magnitude, note) plus the overridden values
  vs Base. Keep the thesis and the numbers visibly separate, and heed any
  contradiction warnings the model surfaces.
- **Respect the model's semantics** (see per-type notes).
- **Gaps are stated, not filled.** If the model lacks something a section needs,
  say so in a watch-out — don't invent it.

## Overall confidence

Set the cover's overall confidence from the spread of confidences on the values
that back the headline conclusion (roughly the low end of the load-bearing
figures), and name what's dragging it down in a watch-out.

## Saving the report

Render the HTML, then — when asked, and if the connector is available — store the
finished file in the project's files as an artifact (HTML renders inline there;
reusing a filename replaces it).
