---
name: refresh
description: 'Bring an existing aqmen project up to date when the data moves — new figures, a new quarter, a corrected source — and re-check every finding, doc block and deck figure that depended on it, keeping the findings doc and the plan current. Use for "update the model", "new data arrived", "refresh with the latest figures", "roll it forward a year", "the source was revised", "update the deck", "update the memo", or when describe_workspace, list_docs or list_decks shows stale items. A shared step.'
---

# Refresh — nothing stale, nothing silently wrong

The workspace tracks what depends on what. When a dataset changes, the
transformations, spreadsheets, charts, views, doc blocks and deck figures
downstream are flagged. This step clears those flags honestly: every
finding whose figure moved is re-checked and re-approved or dropped, and
every doc block and deck figure is re-read with the words around it.

Stay within the project: other projects that read the same datasets get
their own refresh. Read `references/practice.md` once per session, the
MCP's `datasets` topic for append and replace, and `docs` and `decks` for
stale and broken sources.

## 1. See what moved

`describe_workspace` with the `projectId`, `list_docs` and `list_decks`
with the `projectId` (stale and broken counts per doc and deck). List for the user what is new (the data they brought, or
a newer publication you found) and what is already stale. Agree on the
scope before writing.

## 2. Update the data

- **Append** new periods when the series continues: same columns, unit and
  scale.
- **Replace** a dataset when the publisher revised its history. This is
  destructive: confirm first. A revision is a better fact, so it changes
  history everywhere, never in one scenario.
- **The new edition is a new version of its source**, not a new source:
  `update_source` `replaceFile` with the new upload (the old one stays in
  its History, the citations stay). Re-read it with `read_source` and
  re-check every citation of it (`get_dataset`): the `where` still points
  at the figure (pages and table numbers move between editions) and the
  note still holds; fix them with `annotate_dataset` (`citations`,
  `removeCitations`). A new document is a new source, stored and cited
  (`references/practice.md`, "Sources: store, read, cite"). Then the
  dataset's notes say what changed and why; update the brief's Sources
  register.
- New files or a researcher's packet load through **aqmen:data-loader**
  (preview, the user's yes, then load — `mode: "append"` or, confirmed,
  `"replace"`, with the target dataset, and the collection id of the
  workstream it serves), one loader at a time, as **aqmen:research**
  describes. Next period lands in the same collection, never a folder per
  month.

## 3. Rerun the chain, in order

1. `run_transformation` on each adapting transformation, then the feed.
   Check the feed with `run_sql`: no nulls, the new periods present.
2. `run_spreadsheet` to refresh its connections. Read the report and the
   lint. Rows added inside a connection move what sits below it, so check
   the summary blocks and `checks` still point at the right cells — a deck
   sources those cells.
3. Charts recompute on read. `show_chart` the ones the brief's questions
   rest on and compare them with before.
4. **Re-read the verdicts** of the `Believe` block (`modeling`: what you
   need to believe) and its sanity checks. A verdict that changed, a
   break-even the driver now sits closer to, or a new `FLAG` is reported to
   the user like a moved figure, with the findings that rest on that row.

## 4. Re-check the findings doc and the plan

`read_doc` the findings doc: which sourced blocks are stale or broken.

- **Broken first**: `pin` the block to the artifact that replaced its
  source, or — with the user's yes — `detach` it.
- **Then `refresh`** the stale ones, and re-read every headline, caption
  and caveat around a moved figure.
- **The figure did not move materially** and no `Believe` row the finding
  names changed verdict: the finding stands — the user already approved
  this exact claim.
- **The figure or the claim moved:** it is a new claim, and approving it
  is the user's call (as in **aqmen:conclude**). Show the old and the new
  headline side by side and ask; reword and keep only what the user
  approves; mark it "Draft — not yet approved" until they do; drop (and log
  why) what they reject.

Never leave a stale block or an outdated sentence standing because it was
inconvenient. When a question loses its answer, set its brief line back to
`Q<n> [open]` with `edit_notes` on that exact text. Then the **plan**: a
hypothesis whose deciding figure moved gets its verdict re-read —
supported, refuted or partly supported — in the same `update_doc` pattern.
A deck slide whose headline came from a changed finding is now wrong: fix
it in §5.

A material change to the model (a new segment, a changed method) goes back
through **aqmen:challenge** (the model and values critics, in recheck or a
full pass) before the findings are trusted.

**Views.** `list_views` shows each view's state. A **broken** view (a chart,
dataset or spreadsheet it read was deleted or renamed) or one headed by a
finding that changed gets an **aqmen:view-builder** in fix mode: its
`viewId` and its workstream's collection id, the question, the finding and charts that now answer it, the figures that
must appear. Several broken views: one builder each, in the background, in
parallel; collect them before the gate.

## 5. Bring the deliverables with it

For each deck `list_decks` shows with stale or broken sources, and each
memo or report doc `list_docs` shows (the same steps with `read_doc`,
`pin` / `refresh` and `export_doc`):

1. `read_deck`: which elements, why, and what they were built from.
2. **If the deck was already presented or sent**, tell the user which
   figures move and by how much before updating it.
3. **Broken first**: re-point the element to the artifact that replaced its
   source, or — with the user's yes — detach it. Then `refreshSource` the
   stale ones.
4. **Re-read the titles and takeaways** around every moved figure and fix
   the words; their `checks` must pass again. A headline whose claim no
   longer holds changes with its finding.
5. If figures moved materially, run the **deck critic** in recheck or a
   full pass (**aqmen:challenge**) before it goes back to the client.
6. If an HTML report was built from the deck, rebuild it from the new
   version (**aqmen:deliver**).
7. `export_deck` or `export_doc` again if the user needs the new file.

## 6. Tell the story of the change

A short bridge for the user: what the headline was, what it is now, and
which drivers moved it — a `waterfall` chart where the move is material,
in the workstream's collection. Append a line to the brief's Log.

**Tidy.** `describe_workspace` on the project: the root is empty — file
anything there into its home (`move_to_collection`) — and update a
collection description the refresh made stale (`update_collection`). Its
Sources section: no uncited file left unexplained, no broken link left
standing (replace it with the stored copy, `update_source`
`convertToFile`, or a new URL).

## Gate

`describe_workspace` shows nothing stale and nothing broken, broken
links among them; every
finding whose figure moved is re-approved or dropped; `list_docs` and
`list_decks` show no stale or broken source, and the words in every doc
and deck agree with their figures; the plan's verdicts match the current
figures; `list_views` shows no broken view; the project root is empty.
