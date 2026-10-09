---
name: deliver
description: 'Build the deliverable of an aqmen project as a deck in the workspace — the use case''s storyline, every workspace figure added by source, audited, nothing stale — then show it, file it and export it to PowerPoint on request; optionally a matching HTML report whose figures are read from the deck. Use for "build the deck", "make the slides / the readout / the presentation", "put the analysis into the deck", "write it up", "export to PowerPoint", "the report", or after aqmen:conclude. A shared step: the use case (e.g. aqmen:cdd) supplies the storyline.'
---

# Deliver — the deck, figures by source

The deliverable is a **deck in the workspace**: built op by op through the
MCP, shown in the chat and on its page, downloaded as an editable
PowerPoint. Its figures are the workspace's, **added by source** — so when
the model moves, the deck says so instead of quietly showing an old number.
An HTML report can accompany it, its figures read from the deck.

Read `references/practice.md` once per session and
`references/deliverable-standards.md`. Then `read_instructions('decks')`
before the first deck write — the elements, ops, sources, house look,
recipes and hand-over gate are the platform's, and this skill does not
restate them. Read `charts` before saving a chart a slide needs, and
`insights` before validating one.

## When to use

The work is concluded and the next step is to present it, or the user asks
for a deck, slides, a readout, a PowerPoint or a report. Not for exploring
while the work moves (that is a view, **aqmen:conclude**).

## Inputs

- **The brief** with its questions answered (`Q<n> [answered → …]` or
  `[cannot say: …]`).
- **The storyline**: the use case's (for a CDD, the cdd skill's
  `cdd-storyline.md` and workstream files), or the slide plan and ghost
  deck from **aqmen:storyline**.
- **Validated insights** for the headlines; saved charts, model cells and
  ranges for the exhibits.

## Gate in

Hold before building:

- **aqmen:conclude** has passed: every question answered or "cannot say".
- `describe_workspace` and `list_insights` show nothing stale or broken;
  otherwise **aqmen:refresh** first.
- The values critic has passed on the model's figures (**aqmen:challenge**);
  on a CDD, the skeptic's critical challenges are settled or carried as
  caveats (**aqmen:conclude**).

## Steps

1. **Gather** (`references/gather.md`): the brief, the existing decks
   (`list_decks` — a ghost deck to fill or an earlier version to update;
   never a duplicate), the figures as sourceable artifacts, the insights,
   the provenance. Build the figure map: figure → artifact → how it reaches
   the slide. Missing figures go back to **aqmen:model** / **aqmen:conclude**
   to be saved first.
2. **Plan** the slides from the storyline: the action titles in reading
   order, read aloud; per slide the exhibit and its source, two or three
   takeaways. Show the title list to the user and wait (step-by-step mode).
3. **Build** (`references/deck.md`): fill the ghost deck, patch the earlier
   version, or `create_deck` in the project's collection; one storyline part
   per write; `dryRun` on large batches; fix the lint; `checks` on typed
   headline figures and sourced KPI texts.
4. **Self-audit** with `read_deck`: typed figures that exist in the
   workspace → by source; claim drift fixed; stale or broken sources
   resolved; detached sources re-sourced or agreed; a source line on every
   content slide; Sources and confidence at the close.
5. **Deck gate**: for a client-facing deck, **aqmen:challenge** runs the
   **deck critic** (`aqmen:deck-critic`) in a fresh context: the deck id,
   the audience, the storyline standard and the brief verbatim — never your
   slide reasoning. It reads the deck as communication (storyline, action
   titles, one message per slide, so-whats, the executive summary against
   the body, numbers consistent across slides, lint, the house look) and
   its sourcing (typed workspace figures, stale or broken sources, claim
   drift, detached sources, unvalidated insight headlines), and returns
   findings with ops-level fixes. You apply the accepted ones through
   `update_deck` (one writer per deck), then a recheck. The figures under
   the deck stay the values critic's.
6. **Hand over**: the hand-over gate (below), then `show_deck`,
   `annotate_deck` (description and docs: audience, story, where figures
   come from), filed in the collection, `export_deck` when the user wants
   the `.pptx` (give the link).
7. **Optional HTML report** (`references/html-companion.md`): built after
   the gate, from the deck's pinned figures (`read_deck`), on the
   workstream's template in `assets/`, styled per
   `references/report-style.md`; saved as a local file.
8. Append to the brief's Log: the deck and its version, the report path,
   what is open.

## Gate

- `read_deck` shows **no stale or broken source**, no lint, every check
  passing — before `show_deck` or `export_deck`, which do not check.
- No figure that exists in the workspace is typed on a slide.
- The deck critic's findings are resolved or accepted by the user, and
  its recheck shows them fixed.
- Every question in the brief has its slide, or a stated "cannot say".
- On a CDD, the **what you need to believe** slide is present, sourced
  from the `Believe` ranges and fresh; no headline contradicts a verdict
  (a "the market supports it" title over an `implausible` row).
- A report, if built, matches the deck figure for figure, with its
  "Where each number lives" table.

## Hands over

The deck's link (and the PowerPoint link when asked), the report path if
built, and a few lines: the bottom line, the exhibits resting on the weakest
data, what was assumed where the model was silent. When the answers will be
shown live, offer **aqmen:demo-prep**. When data moves later,
**aqmen:refresh** brings the deck with it.
