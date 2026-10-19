# Building the memo or report — a Doc, figures by source

The platform's `docs` topic is the contract: the blocks and their Word
forms, sourced blocks (`chart`, `range`, `figure`), ops, the Word export
and import, the hand-over gate. Read it fresh before the first
`create_doc` or `update_doc`; nothing here restates it. This file is the
order of the work and the standard the doc is held to.

## 1. The findings are the outline

A memo is the findings doc rewritten for its reader, not a copy of it. The
findings doc is the working record (every question, caveats, drafts); the
memo is the argument the client reads.

- **Bottom line first**: one paragraph — the answer and the decision it
  informs — then a short executive summary, one bullet per question, each
  a finding with its figure.
- **Then one section per part of the storyline** (for a CDD: Context →
  Market → Competition → Company, `cdd-storyline.md`; otherwise the brief's
  questions in order). Each section opens with its headline finding, then
  the exhibit, then two or three paragraphs of support and caveat.
- On a CDD, **what you need to believe** as its own section, a `range` over
  the `Believe` rows.
- **Sources and confidence** closes it (`deliverable-standards.md`).

Write the headlines first, as one list; read them aloud — they must argue
from the situation to the answer on their own. Show them to the user
before writing the body (step-by-step mode).

## 2. Start from what exists

- **An earlier version of this memo** (`list_docs`): `read_doc`, patch
  what changed with `update_doc`. Never a second doc for the same
  deliverable.
- **The client's Word template or draft**: upload it (`create_upload_slot`
  with the `.docx`) and `create_doc` with its `uploadId` (in
  Deliverables), then insert the
  sourced blocks. A file Aqmen exported comes back with its figures live.
- **Nothing yet**: `create_doc` in the project (`projectId`, the
  Deliverables `collectionId` for the memo the client gets; a working doc
  takes its workstream's), named for the deliverable (`<project>_memo`), from
  `markdown` for the prose skeleton, with `ops` inserting the sourced
  blocks where the figures go.

## 3. Every figure by source, the words yours

| In the memo | How |
| --- | --- |
| A number in a sentence | a `figure` block: `before` + the source (a model `cell`, a chart `field`, a `dataset` value) + `after` |
| A chart | a `chart` block over the saved chart, with a caption that is the finding |
| A table of figures | a `range` block over the model's summary block |
| Method, rationale, caveats | paragraphs and `callout`s — in plain words |
| A figure from outside the workspace | load it as a dataset first; type it only for a one-off quote, its origin stated |

**Never SQL, code or internal names.** No `code` blocks in a client
deliverable; no table, column or chart identifiers. "Allocated by each
region's share of headcount (national statistics, 2024)", not the query.
Display names only.

Build one section per write; `dryRun: true` first on a large batch; after
each write `read_doc` and confirm every new sourced block reads **fresh**.

## 4. Self-audit

`read_doc` (`as: "markdown"` to read it as prose, then the blocks for
sources) and walk it section by section:

- **Typed figures that exist in the workspace** → re-insert them by
  source.
- **Claim drift**: a sentence that no longer says what its sourced figure
  shows. Fix the words.
- **Stale or broken sources**: broken first (`pin` to the replacement, or
  `detach` with the user's yes), then `refresh`.
- Every headline is an approved finding; estimates labelled; Base before
  scenarios; watch-outs where the weak figures are; nothing implied
  complete.
- No SQL, no code blocks, no internal names.

## 5. Hand over

1. **Gate:** `read_doc` shows no stale or broken source.
2. Give the doc's link; `annotate_doc` with a one-line description (who it
   is for, what it answers) and notes: the audience, the storyline, where
   each section's figures come from, the open watch-outs.
3. `export_doc` when the user wants Word; give the link (it expires within
   the hour — call again for a fresh one). If the client edits the Word
   file and sends it back, `create_doc` with its `uploadId` restores the
   figures as live sourced blocks.
4. Record it in the plan's **Deliverables** and the brief's Log: the doc,
   its version, what is open.
