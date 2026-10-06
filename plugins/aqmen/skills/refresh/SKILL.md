---
name: refresh
description: 'Bring an existing aqmen project up to date when the data moves — new figures, a new quarter, a corrected source — and re-check every conclusion that depended on it. Use for "update the model", "new data arrived", "refresh with the latest figures", "roll it forward a year", "the source was revised", or when describe_workspace or list_insights shows stale items. Step 7 of the aqmen project flow.'
---

# Refresh — nothing stale, nothing silently wrong

The workspace tracks what depends on what. When a dataset changes, the
transformations, spreadsheets, charts, views and insights downstream are
flagged. This step clears those flags honestly: every stale conclusion is
re-checked, and then validated or rejected.

Read `references/practice.md` once per session, and the MCP's `datasets`
topic for append and replace.

## 1. See what moved

`describe_workspace` and `list_insights`. List for the user what is new
(the data they brought, or a newer publication you found) and what is
already stale. Agree on the scope before writing.

## 2. Update the data

- **Append** new periods to a dataset when the series continues: same
  columns, same unit, same scale.
- **Replace** a dataset when the publisher revised its history. This is
  destructive: confirm with the user first. A revision is a better fact,
  so it changes history everywhere, never in one scenario.
- Update `sources` with the new edition, and the docs with what changed
  and why. Update the brief's Sources register.

## 3. Rerun the chain, in order

1. `run_transformation` on each adapting transformation, then the feed.
   Check the feed with `run_sql`: no nulls, the new periods present.
2. `run_spreadsheet` to refresh its connections. Read the report and the
   lint. Rows added inside a connection move what sits below it, so check
   the summary blocks and `checks` still point at the right cells.
3. Charts over the spreadsheet or SQL recompute on read. `show_chart` the
   ones the brief's questions rest on and compare them with before.

## 4. Re-check every stale insight

For each one: recompute the claim. Then `update_insight`: validate it if
it still holds (with the new figure in the title), or reject it if not
and record the new claim as its own insight. Never leave a stale insight
standing because it was inconvenient.

When a rejected insight answered a question, its brief line reads
`Q<n> [answered → <oldId>]`. Point it at the new insight with `edit_docs`
on that exact text, or set it back to `[open]` if nothing answers it now.

A material change to the model (a new segment, a changed method) goes
back through **aqmen:challenge** before the conclusions are trusted.

## 5. Tell the story of the change

A short bridge for the user: what the headline was, what it is now, and
which drivers moved it. A `waterfall` chart where the move is material.
Append a line to the brief's Log.

## Gate

`describe_workspace` shows nothing stale and nothing broken, and every
insight that was stale is now validated or rejected.
