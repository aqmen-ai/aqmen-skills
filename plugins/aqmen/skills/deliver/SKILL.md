---
name: deliver
description: 'Build the deliverable of an Aqmen project in the workspace — a deck (the use case''s storyline, exported to PowerPoint) and/or a memo or report as a Doc (exported to Word) — every workspace figure added by source, written from the approved findings, audited, nothing stale; then show it, file it in the project and export it on request; optionally a matching HTML report whose figures are read from the deck. Use for "build the deck", "make the slides / the readout / the presentation", "write the memo / the report", "write it up", "export to PowerPoint / Word", or after aqmen:conclude. A shared step: the use case (e.g. aqmen:cdd) supplies the storyline.'
---

# Deliver — figures by source

The deliverable lives **in the project**: a **deck** to present, a **doc**
(a memo or report) to read and send as Word, or both. Either is built op by
op through the MCP, shown on its page and downloaded as an editable Office
file. Its figures are the workspace's, **added by source** — so when the
model moves, the deliverable says so instead of quietly showing an old
number. Its claims are the **approved findings** of the project's findings
doc.

Read `references/practice.md` once per session and
`references/deliverable-standards.md`. Then read the platform topic for
the form before its first write — `read_instructions('decks')` for a deck,
`read_instructions('docs')` for a doc: the elements and blocks, ops,
sources, house look and hand-over gate are the platform's, and this skill
does not restate them. Read `charts` before saving a chart the deliverable
needs.

## When to use

The work is concluded and the next step is to present or send it, or the
user asks for a deck, slides, a readout, a memo, a report or a Word or
PowerPoint file. Not for exploring while the work moves (that is a view,
**aqmen:conclude**).

## Choose the form

| The reader needs | Build | Reference |
| --- | --- | --- |
| Slides to present — a readout, a SteerCo | a **deck** | `references/deck.md` |
| Prose to read, forward or edit in Word — a memo, a report, an IC paper | a **doc** | `references/doc.md` |
| Both | the deck first, then the doc from the same findings and sources | both |

The brief's **Deliverable** line usually says; otherwise ask. When the user
wants Word, prefer a doc over the HTML report. An HTML report
(`references/html-companion.md`) remains available as the deck's
self-contained written companion.

## Inputs

- **The brief** with its questions answered (`Q<n> [answered]` or
  `[cannot say: …]`) and **the plan** doc (the deliverables promised, the
  audience).
- **The findings doc**: the approved findings, each headline with its
  sourced figure, exhibit and caveat.
- **The storyline**: the use case's (for a CDD, the cdd skill's
  `cdd-storyline.md` and workstream files), or the slide plan and ghost
  deck from **aqmen:storyline**.
- Saved charts, model cells and ranges for the exhibits.

## Gate in

Hold before building:

- **aqmen:conclude** has passed: every question answered or "cannot say",
  every finding approved.
- `describe_workspace` (with the `projectId`) and `read_doc` on the
  findings doc show nothing stale or broken — no broken link and no
  uncited file among the sources either; otherwise **aqmen:refresh**
  first.
- The values critic has passed on the model's figures (**aqmen:challenge**);
  on a CDD, the skeptic's critical challenges are settled or carried as
  caveats (**aqmen:conclude**).

## Steps

1. **Gather** (`references/gather.md`): the brief, the plan, the findings
   doc, the existing decks and docs (`list_decks`, `list_docs` — a ghost
   deck to fill or an earlier version to update; never a duplicate), the
   figures as sourceable artifacts, the provenance. Build the figure map:
   figure → artifact → how it reaches the page. Missing figures go back to
   **aqmen:model** / **aqmen:conclude** to be saved first.
2. **Plan** from the storyline: the headlines in reading order, read aloud;
   per slide or section the exhibit and its source, two or three takeaways.
   Show the list to the user and wait (step-by-step mode).
3. **Build** — the deck per `references/deck.md`, the doc per
   `references/doc.md` — in the project (`projectId`), in the
   Deliverables collection (its `collectionId` from the brief; a
   sub-collection per hand-over if there are several, "Interim readout",
   "Final"). A working deck or doc (an internal draft, a workstream's
   backup pages) goes in its workstream's collection.
   No SQL, code or internal names anywhere; the method in plain words.
4. **Self-audit**: typed figures that exist in the workspace → by source;
   claim drift fixed; stale or broken sources resolved; detached sources
   re-sourced or agreed; a source line under every exhibit; Sources and
   confidence at the close; no SQL or table names.
5. **Deck gate**: for a client-facing deck, **aqmen:challenge** runs the
   **deck critic** (`aqmen:deck-critic`) in a fresh context: the deck id,
   the audience, the storyline standard, the findings doc id and the brief
   verbatim — never your slide reasoning. It reads the deck as
   communication (storyline, action titles, one message per slide,
   so-whats, the executive summary against the body, numbers consistent
   across slides, lint, the house look) and its sourcing (typed workspace
   figures, stale or broken sources, claim drift, detached sources,
   headlines that are not approved findings), and returns findings with
   ops-level fixes. You apply the accepted ones through `update_deck` (one
   writer per deck), then a recheck. The figures under the deck stay the
   values critic's.
6. **Hand over**: the hand-over gate (below), then `show_deck` or the doc's
   link; `annotate_deck` / `annotate_doc` (description and notes: audience,
   story, where figures come from), filed in Deliverables; `export_deck`
   for the `.pptx` or `export_doc` for the `.docx` when the user wants the
   file (give the link).
7. **Optional HTML report** (`references/html-companion.md`): built after
   the deck's gate, from its pinned figures (`read_deck`), on the
   workstream's template in `assets/`, styled per
   `references/report-style.md`; saved as a local file.
8. Record the deliverable in the plan doc's **Deliverables** (delivered,
   with the date) and append to the brief's Log: the deck or doc and its
   version, the report path, what is open. `update_project` to `in_review`
   or `delivered` when the user says so.
9. **Tidy.** `describe_workspace` on the project: the root is empty;
   file any chart made for the deliverable into its workstream's
   collection (`move_to_collection`).

## Gate

- `read_deck` / `read_doc` shows **no stale or broken source**, no lint,
  every check passing — before `show_deck`, `export_deck` or `export_doc`,
  which do not check.
- No figure that exists in the workspace is typed.
- No SQL, code or internal table name in anything the client reads.
- Every headline is an approved finding; every question in the brief has
  its slide or section, or a stated "cannot say".
- For a deck, the deck critic's findings are resolved or accepted by the
  user, and its recheck shows them fixed.
- On a CDD, the **what you need to believe** slide (or section) is present,
  sourced from the `Believe` ranges and fresh; no headline contradicts a
  verdict (a "the market supports it" title over an `implausible` row).
- A report, if built, matches the deck figure for figure, with its
  "Where each number lives" table.

## Hands over

The deck's or doc's link (and the PowerPoint or Word link when asked), the
report path if built, and a few lines: the bottom line, the exhibits
resting on the weakest data, what was assumed where the model was silent.
When the answers will be shown live, offer **aqmen:demo-prep**. When data
moves later, **aqmen:refresh** brings the deliverables with it.
