# Using aqmen data (shared)

A deliverable is only as good as how fully it draws on the workspace. An
aqmen workspace holds far more than headline numbers: every dataset cites
the documents it came from and states its method and confidence (1–5),
every derived figure traces back through lineage, and conclusions are
recorded as insights on the charts that show them. Use all of it. **Never
invent numbers or sources.**

> Shared verbatim across all aqmen report and deck skills. Each
> `*-content.md` says what to gather for its framework.

## Gather before you write

Read the whole project first; do not write from partial data.

1. **The workspace and the brief.** `list_workspaces`, then
   `describe_workspace`: the datasets with their column semantics, the
   transformations, spreadsheets, charts, views, insight titles, and the
   workspace docs. The docs hold the brief: the decision, the questions,
   the frame, the sources register and the log. The deliverable answers
   the brief's questions, in its order.
2. **The model.** `list_spreadsheets`, then `read_spreadsheet` with no
   range for the layout, connections, report and lint, and with the model
   sheet and range for the cells and the column structure (which column
   is computed from which). `show_spreadsheet_range` returns a range
   rendered for the reader; use it for statement tables and summaries.
3. **The computed values.** Headline figures and splits come from the
   spreadsheet's summary blocks and KPI cells, or from `run_sql` over the
   model's feed and the derived datasets. A figure the deliverable prints
   is one the workspace computes.
4. **The charts.** `list_charts`, then `get_chart` for each chart's
   definition and data, `show_chart` to see it as the reader does. The
   driver tree, the bridges and the benchmark charts are already built;
   reuse their data and titles rather than re-deriving them.
5. **Provenance.** For each dataset the model reads, `get_dataset`: its
   `sources` (label, URL), its docs (method, confidence, caveats) and a
   `confidence` or `method` column where rows differ. For a derived
   dataset, `get_transformation` on the transformation that produced it:
   its SQL is the method.
6. **The conclusions.** `list_insights`, then `get_insight` where the
   body matters: each is one claim with its figure, on the chart,
   spreadsheet or view that demonstrates it, with a status (open,
   validated, rejected) and a stale flag.
7. **The views.** `list_views` and `read_view`: the pages the team built
   for readers. Their structure is a good draft of the narrative.
8. **Scenarios,** where the model has them: the `Hypotheses` sheet (each
   named claim, the drivers it moves, its growth by period) and the
   realization table per scenario, read with `read_spreadsheet`.

## Use the data fully

- **Numbers come from the workspace.** Headline figures, KPIs and every
  chart series are values the workspace computes. Do not round away
  precision it has, and do not add figures it does not contain.
- **Citations come from the datasets.** Populate the Sources & confidence
  table from the datasets the headline figures depend on: the source label
  and URL, its type (official statistics, analyst, filing, company
  release, news, estimate), the dataset's confidence and the method from
  its docs. Never fabricate a source or a score.
- **Conclusions come from insights.** Lead with the validated insights
  that answer the brief's questions. An open insight can be used, marked
  as not yet validated. A rejected insight is never presented as a
  finding. A stale insight must be re-checked (the aqmen:refresh skill) or
  flagged.
- **Watch-outs are data-driven.** Surface as ⚠ watch-outs:
  - figures resting on datasets with **confidence ≤ 2**;
  - figures resting on an **estimate** or a **news source** (confidence
    capped at 3), or on an **allocation or proxy** (method in the docs);
  - **gaps**: questions in the brief marked "cannot say", nulls, stale or
    broken items `describe_workspace` or `read_spreadsheet` reports;
  - the **drivers that most move the result**, from the model's
    sensitivity or the scenario deltas.
- **Scenarios: Base first.** Present the validated Base case, then each
  scenario as the hypotheses it activates (the claim, the drivers it
  moves, the realization) and the resulting difference from Base. Keep
  the thesis and the numbers visibly separate.
- **Gaps are stated, not filled.** If the workspace lacks something a
  section needs, say so in a watch-out.

## Overall confidence

Set the cover's overall confidence from the confidence of the datasets
behind the headline conclusion, roughly the low end of the load-bearing
figures, and name what drags it down in a watch-out.

## Traceability

Every number in the deliverable should resolve to a chart, a spreadsheet
cell or a dataset in the workspace. Keep a short list as you write
(figure → where it lives) and include it as the appendix's "Where each
number lives" table, so a reviewer can open the workspace and check it.

## Saving the deliverable

Save the file to the user's working directory with a clear name
(`<project>-market-sizing-report.html`). Offer to record the headline
conclusions as insights in the workspace if any are not there yet; the
workspace, not the file, is where conclusions stay current.
