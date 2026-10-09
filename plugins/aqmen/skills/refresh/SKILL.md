---
name: refresh
description: 'Bring an existing aqmen project up to date when the data moves — new figures, a new quarter, a corrected source — and re-check every conclusion and deck figure that depended on it. Use for "update the model", "new data arrived", "refresh with the latest figures", "roll it forward a year", "the source was revised", "update the deck", or when describe_workspace, list_insights or list_decks shows stale items. A shared step.'
---

# Refresh — nothing stale, nothing silently wrong

The workspace tracks what depends on what. When a dataset changes, the
transformations, spreadsheets, charts, views, insights and deck figures
downstream are flagged. This step clears those flags honestly: every stale
conclusion is re-checked, then validated or rejected, and every deck
figure re-read with the words around it.

Read `references/practice.md` once per session, the MCP's `datasets` topic
for append and replace, `insights` for re-checking, and `decks` for stale
and broken sources.

## 1. See what moved

`describe_workspace`, `list_insights` and `list_decks` (stale and broken
counts per deck). List for the user what is new (the data they brought, or
a newer publication you found) and what is already stale. Agree on the
scope before writing.

## 2. Update the data

- **Append** new periods when the series continues: same columns, unit and
  scale.
- **Replace** a dataset when the publisher revised its history. This is
  destructive: confirm first. A revision is a better fact, so it changes
  history everywhere, never in one scenario.
- Update the sources with the new edition, and the docs with what changed
  and why. Update the brief's Sources register.
- New files or a researcher's packet load through **aqmen:data-loader**
  (preview, the user's yes, then load — `mode: "append"` or, confirmed,
  `"replace"`, with the target dataset), one loader at a time, as
  **aqmen:research** describes.

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
   the user like a moved figure, with the insights that rest on that row.

## 4. Re-check every stale insight

Per the `insights` topic: re-check it against its parent.

- **The figure did not move** and no `Believe` row it names changed
  verdict: re-validate it — the user already approved this exact claim.
- **The figure or the claim moved:** it is a new claim, and validating it is
  the user's call (as in **aqmen:conclude**). Show the old and the new
  title side by side and ask; edit and validate only what the user
  approves, reject (or record anew) what they do not.

Never leave a stale insight standing because it was inconvenient.

When a rejected insight answered a question, its brief line reads
`Q<n> [answered → <oldId>]`. Point it at the new insight with `edit_docs`
on that exact text, or set it back to `[open]` if nothing answers it now. A
deck slide sourced from the rejected insight is now wrong: re-point it to
the new one in §5.

A material change to the model (a new segment, a changed method) goes back
through **aqmen:challenge** (the model and values critics, in recheck or a
full pass) before the conclusions are trusted.

**Views.** `list_views` shows each view's state. A **broken** view (a chart,
dataset or spreadsheet it read was deleted or renamed) or one headed by a
rejected insight gets an **aqmen:view-builder** in fix mode: its `viewId`,
the question, the insights and charts that now answer it, the figures that
must appear. Several broken views: one builder each, in the background, in
parallel; collect them before the gate.

## 5. Bring the decks with it

For each deck `list_decks` shows with stale or broken sources:

1. `read_deck`: which elements, why, and what they were built from.
2. **If the deck was already presented or sent**, tell the user which
   figures move and by how much before updating it.
3. **Broken first**: re-point the element to the artifact that replaced its
   source, or — with the user's yes — detach it. Then `refreshSource` the
   stale ones.
4. **Re-read the titles and takeaways** around every moved figure and fix
   the words; their `checks` must pass again. A headline whose claim no
   longer holds changes with its insight.
5. If figures moved materially, run the **deck critic** in recheck or a
   full pass (**aqmen:challenge**) before it goes back to the client.
6. If an HTML report was built from the deck, rebuild it from the new
   version (**aqmen:deliver**).
7. `export_deck` again if the user needs the new file.

## 6. Tell the story of the change

A short bridge for the user: what the headline was, what it is now, and
which drivers moved it — a `waterfall` chart where the move is material.
Append a line to the brief's Log.

## Gate

`describe_workspace` shows nothing stale and nothing broken; every insight
that was stale is validated or rejected; `list_views` shows no broken view; `list_decks` shows no stale or
broken source and every deck's words agree with its figures.
