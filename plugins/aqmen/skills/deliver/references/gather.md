# Gather before you build

A deliverable is only as good as how fully it draws on the workspace. The
workspace holds far more than headline numbers: every dataset cites its
documents and states its method and confidence, every derived figure traces
back through lineage, and the conclusions are the findings doc, each figure a
sourced block. Read the whole project first; never build from partial data, and never
invent a number or a source.

The use case says what to gather for its frameworks (for a CDD, each
`workstream-*.md` in the cdd skill). The general flow:

1. **The brief and the plan.** `describe_workspace` with the `projectId`:
   the datasets with their semantics, the transformations, spreadsheets,
   charts, views, decks and docs, and the project's notes — the decision,
   the questions with their status, the frame, the deliverable, the sources
   register, the Log. `read_doc` the plan for the deliverables promised and
   the hypotheses' verdicts. The deliverable answers the brief's questions,
   in its order.
2. **The deliverables already there.** `list_decks` and `list_docs` (with
   stale and broken counts): a ghost deck from **aqmen:storyline** to fill,
   or an earlier version of this deliverable to update. Update rather than
   duplicate. `read_deck` / `read_doc` it (large ones come back as an
   outline; pass `slides` or `blocks` for the ones you edit).
3. **The figures, as artifacts a slide can source.** `list_charts` — note
   each chart's type: bar, line, pie, waterfall, table and number charts
   draw on a slide; any chart gives a `field`. `list_spreadsheets` and
   `read_spreadsheet` for the model's summary blocks, KPI cells and ranges
   (a slide sources a summary block, not the model's rectangle).
4. **The conclusions.** `read_doc` the findings doc: per question the
   headline with its sourced figure, the exhibit, the method and caveat,
   and whether it is approved (no "Draft" callout) and fresh. Only approved
   findings head a slide or a section.
5. **Provenance.** For each dataset a headline figure rests on,
   `get_dataset`: its citations (each source — title, publisher,
   published — with where in it and the note), its notes (method,
   confidence, caveats), a `confidence` or `method` column where rows differ; for a
   derived one, `get_transformation` — read its SQL and notes to
   understand the method, then **describe it in words**: SQL never reaches
   the deliverable. This is the Sources and confidence section and the
   source lines.
6. **The views** (`list_views`, `read_view`): the pages the team built for
   readers. Their order is often a good draft of the narrative.
7. **Scenarios**, where the model has them: the hypotheses sheet, the
   realization per scenario, the summary block comparing them.

## Map every figure before you write a slide

Keep a short map as you plan: **figure → the artifact that computes it →
how it reaches the page** (on a slide: chart, cell, range, field, or typed
under a check when it lives in a sentence; in a doc: a `chart`, `range` or
`figure` block). A figure with no artifact goes
back to **aqmen:model** or **aqmen:conclude** to be saved first — a chart of
a type a slide draws, or a summary cell. A figure from outside the
workspace is loaded as a dataset first; typed only for a one-off quote,
its origin in the source line.

## Watch-outs come from the data

Surface, on the slide that carries the figure or in the closing section:

- figures resting on datasets with confidence 2 or below;
- figures resting on an estimate, a news source (capped at 3), an
  allocation or a proxy (the method in the notes);
- gaps: questions marked "cannot say", nulls, anything stale or broken;
- the drivers that move the result most (the model's sensitivity or the
  scenario deltas).

## Overall confidence

Roughly the low end of the load-bearing figures' confidence; name what drags
it down.
