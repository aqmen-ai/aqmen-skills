# Building the deck — the process around the platform

The platform's `decks` topic is the contract: elements and options, ops,
sources, checks and lint, the house look, charts on a slide, recipes, and
the hand-over gate. Read it fresh before the first `create_deck` or
`update_deck`; nothing here restates it. This file is the order of the work
and the standard the deck is held to.

## 1. The storyline is the plan

The deck's slides come from the use case's storyline (for a CDD,
`cdd-storyline.md` and the workstream files in the cdd skill) or from the
plan **aqmen:storyline** produced. Write the action titles first, in
reading order, as one list; read them aloud — they must argue from the
situation to the answer without the exhibits. Then, per slide: the exhibit,
the figure map entry (`gather.md`), and the two or three takeaways.

A title is a finding with its number — an approved finding from the
findings doc, reworded for the slide if needed but never beyond what it
claims. The title is typed: put a `check` on its figure, and prefer a
sourced KPI (a `cell` or `field`) beside it so the number on the slide is
live.

## 2. Start from what exists

- **A ghost deck** (from aqmen:storyline): its slides already carry the
  action title, the exhibit title and a dashed placeholder named
  `placeholder`, with the content, purpose and data in the notes. Fill it:
  per slide, `deleteElement` the placeholder and `addElement` the sourced
  exhibit in its box; re-word the title to the finding the data supports
  (the plan's title was a hypothesis — say so when the data disagrees);
  replace the notes with speaker notes.
- **An earlier deliverable**: `read_deck`, patch what changed. Patches beat
  re-adding; never a second deck for the same deliverable.
- **Nothing yet**: `create_deck` with the `projectId` and the
  Deliverables `collectionId` (the client's deck; a working or backup
  deck takes its workstream's) and one `addSlide` per slide. Copy the house look's layouts
  from the topic and from the demo readout deck it names — layouts, never
  numbers.

## 3. Build in sections, verify each

- Build one storyline part per write (Context, Market, …), so lint and
  checks stay readable. `dryRun: true` first on a large batch.
- Every write: fix the lint, read the sourced lines (each new sourced
  element should read fresh), confirm the `checks`.
- Show the part (`show_deck` with its `slides`) at each pause in
  step-by-step mode.

## 4. Self-audit before the deck critic

`read_deck` the whole deck and walk it slide by slide:

- **Typed figures that exist in the workspace** → re-add them by source.
  Only words, dates, section titles, rationale and one-off outside quotes
  stay typed; a typed figure carries a `check`.
- **Claim drift**: a title or takeaway that no longer says what its sourced
  figure shows (a "two-thirds" over a bar that reads 58%). Fix the words.
- **Stale or broken sources**: resolve per the topic (broken first).
- **Detached sources** (static data where a source was): re-source unless
  the user agreed to freeze it.
- Every content slide has a source line; the closing slide lists sources
  and confidence; watch-outs sit where the weak figures are.
- Base before scenarios; estimates labelled; nothing implied complete.
- No SQL, code or internal table names on any slide or in the notes the
  client may see; the method in plain words.

## 5. The deck gate (deck critic)

For a client-facing deck, run **aqmen:challenge** with the deck critic
(`aqmen:deck-critic`): the workspace and project ids, the deck id and
version, the findings doc id, the audience, the storyline standard (for a CDD, `cdd-storyline.md`'s parts
in order) and the brief verbatim — nothing about why you built it as you
did. Triage its findings as challenge says. Its suggested ops are written
against the version it read: re-read the deck and apply them through
`update_deck` on the current version, then run it again in recheck mode.

## 6. Hand over

1. **Gate:** `read_deck` shows no stale or broken source, no lint, every
   check passing.
2. `show_deck` — the deck, or the slides that changed — and describe in a
   line what the user is seeing.
3. `annotate` (entityType `deck`): a one-line description (who it is for, what it
   answers) and notes: the audience, the storyline, where each part's
   figures come from, the open watch-outs.
4. The client's deck in Deliverables, a working deck in its
   workstream's collection (`move_to_collection` if it landed wrong).
5. `export_deck` when the user wants the PowerPoint file; give the link (it
   expires within the hour — call again for a fresh one).
6. Record it in the plan's **Deliverables** and the brief's Log: the deck,
   its version, what is open.
