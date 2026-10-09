# Gather before you build

A deliverable is only as good as how fully it draws on the workspace. The
workspace holds far more than headline numbers: every dataset cites its
documents and states its method and confidence, every derived figure traces
back through lineage, and conclusions are insights on the artifacts that show
them. Read the whole project first; never build from partial data, and never
invent a number or a source.

The use case says what to gather for its frameworks (for a CDD, each
`workstream-*.md` in the cdd skill). The general flow:

1. **The brief.** `describe_workspace`: the datasets with their semantics,
   the transformations, spreadsheets, charts, views, insights and decks, and
   the workspace docs — the decision, the questions with their status, the
   frame, the deliverable, the sources register, the Log. The deliverable
   answers the brief's questions, in its order.
2. **The decks already there.** `list_decks` (with stale and broken counts):
   a ghost deck from **aqmen:storyline** to fill, or an earlier version of
   this deliverable to update. Update rather than duplicate. `read_deck` it
   (large decks come back as an outline; pass `slides` for the ones you
   edit).
3. **The figures, as artifacts a slide can source.** `list_charts` — note
   each chart's type: bar, line, pie, waterfall, table and number charts
   draw on a slide; any chart gives a `field`. `list_spreadsheets` and
   `read_spreadsheet` for the model's summary blocks, KPI cells and ranges
   (a slide sources a summary block, not the model's rectangle).
4. **The conclusions.** `list_insights`, `get_insight` where the body
   matters: the claim with its figure, the parent, the status (open,
   validated, rejected) and staleness. Only validated insights head a slide
   by source.
5. **Provenance.** For each dataset a headline figure rests on,
   `get_dataset`: its sources (label, URL), its docs (method, confidence,
   caveats), a `confidence` or `method` column where rows differ; for a
   derived one, `get_transformation` — its SQL is the method. This is the
   Sources and confidence slide and the source lines.
6. **The views** (`list_views`, `read_view`): the pages the team built for
   readers. Their order is often a good draft of the narrative.
7. **Scenarios**, where the model has them: the hypotheses sheet, the
   realization per scenario, the summary block comparing them.

## Map every figure before you write a slide

Keep a short map as you plan: **figure → the artifact that computes it →
how it reaches the slide** (chart, cell, range, field, insight; or typed
under a check when it lives in a sentence). A figure with no artifact goes
back to **aqmen:model** or **aqmen:conclude** to be saved first — a chart of
a type a slide draws, or a summary cell. A figure from outside the
workspace is loaded as a dataset first; typed only for a one-off quote,
its origin in the source line.

## Watch-outs come from the data

Surface, on the slide that carries the figure or in the closing section:

- figures resting on datasets with confidence 2 or below;
- figures resting on an estimate, a news source (capped at 3), an
  allocation or a proxy (the method in the docs);
- gaps: questions marked "cannot say", nulls, anything stale or broken;
- the drivers that move the result most (the model's sensitivity or the
  scenario deltas).

## Overall confidence

Roughly the low end of the load-bearing figures' confidence; name what drags
it down.
