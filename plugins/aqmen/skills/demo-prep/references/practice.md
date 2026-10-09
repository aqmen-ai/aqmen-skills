# The aqmen practice (shared by every step skill)

> Synced verbatim into the use-case and step skills. Read it once per session.

## The platform is the spec

The aqmen MCP's `read_instructions` topics define how the platform works:
every tool's contract, the shapes it accepts, the house look of a deck.
**Read them fresh**, before the step that needs them: `workflow` at the
start of a session, then the topic for the layer you are about to use —
`datasets` (also `setup`), `sql`, `charts` (also `visualization`),
`spreadsheets`, `insights`, `views`, `decks`, `collections`, and before any
model `modeling`, then `market-sizing`, `company-analysis` or
`competitive-landscape`. Where a skill and a live topic disagree, **the
platform wins**. The skills add what the platform does not: the order of
the work, the gates between steps, the parallel research and review
around it, and the standard a deliverable is held to.

## Pacing

Step-by-step by default: at the end of each step, summarise what changed
in plain language and wait for the user. Tell the user once, early, that
they can say "go autonomous". After that, keep going and summarise at
the end of each step instead of stopping. Autonomy is sticky for the
session.

**Destructive actions are always confirmed**, in both modes: deleting or
replacing a dataset, a transformation, a spreadsheet, a chart, a view or a
deck (`delete_deck`); overwriting a model's formulas; a deck's
`replaceDocument`; a `detachSource` that turns a live figure into a typed
one; rejecting an insight someone validated. When the user's own request is
the destructive action, doing it is the confirmation.

## Agents

Agents buy three things: **parallelism**, **independence** (a fresh context
that never saw your reasoning) and **context isolation** (their reading
stays out of yours). Spawn them with the Agent tool as `aqmen:<name>`.

| Agent | Writes | Spawned by |
| --- | --- | --- |
| `researcher` | nothing — returns load-ready packets | research (parallel, disjoint assignments) |
| `data-loader` | datasets only (+ their annotations, docs, filing) | research, refresh |
| `view-builder` | one view (+ its docs, filing) | conclude (one per question), refresh, demo-prep |
| `model-critic` | nothing | model (gate), challenge |
| `values-critic` | nothing | challenge (before done, before deliver) |
| `deck-critic` | nothing | deliver (gate before hand-over) |
| `skeptic` | nothing | challenge, conclude (CDD by default) |

- **Critics are independent.** Their prompt carries only ids, the scope,
  the use case's standard and the brief **verbatim** — never your design
  reasoning, sourcing notes or what you expect them to find. Never run a
  critique inline. A recheck passes the critic its own findings (by id),
  still nothing about how you fixed them.
- **Writers stay in their scope.** A data loader touches only datasets it
  creates (a replace needs the user's yes, relayed in its prompt); a view
  builder only its one view. Everything else — transformations,
  spreadsheets, charts, insights, decks, the brief — is yours, one call at
  a time, never two in flight.
- **Parallel or serial.** Research and views run in parallel (views are
  independent entities: spawn one builder per view, in the background, and
  keep working). Dataset loading is **serialized** — one loader per
  workspace, unless the datasets are independent and you say so in each
  prompt. Deck writing is never delegated: one writer per deck.
- **Background agents cannot ask the user.** Give them everything they
  need; if the session would prompt for their writes, run them in the
  foreground instead. Collect every result before the step's gate.
- **Trust, then verify.** Read back what a writer says it made
  (`describe_workspace`, `list_views`), and check the workspace's Activity
  if any agent reports a write outside its scope.

## Numbers and sources

- **Never invent a number.** Every figure enters the workspace as data
  with its source. When a genuine search finds nothing, say so, and
  record an estimate only as an estimate, with its reasoning, at the
  confidence it deserves.
- **Search in passes:** official statistics and regulators first; then
  major analysts, databases and industry bodies; then company filings;
  news last. The framework topics give each framework's order.
- **Confidence is the platform's 1–5 scale** (`modeling`): news and
  allocations cap at 3, a pure estimate is 1.
- A dataset **cites every document** it came from and **states its method
  and confidence** in its docs (`datasets`). A figure without a source is
  not data.
- **A workspace figure goes on a slide by source, never typed.** A chart,
  a KPI, a table that the workspace computes is added to a deck as a
  sourced element (`decks`), so the deck says when the model moves under
  it. Words are yours; numbers are the workspace's.
- **What you need to believe stays live.** The load-bearing assumptions —
  implied metric, reference, verdict, break-even — and the sanity checks
  are a `Believe` block in the model (`modeling`), never a typed list.

## The brief

The workspace docs hold the brief (`aqmen:scope` writes it): the decision,
the questions as `Q<n> [status]: …` lines, the hypotheses, the frame, the
deliverable, the sources register and the Log. Every step reads it first
and appends one dated line to the Log when it ends. Change a question's
status with `edit_docs` find-and-replace on its exact `Q<n> [` text, never
by rewriting the list.

## Gates and honest completion

A step is done only when its gate holds. Do not call work complete while
a driver rests on an estimate the user has not seen, a check fails, a
connection or a deck figure is stale or broken, or lint is left on a
sheet or a slide. State gaps; never fill them to look finished.

## Speaking to the user

Plain language, the reader's words, not the tools': "loaded the Eurostat
enterprise statistics, cited" rather than a tool name and an identifier.
Lead with what changed and what is left. Numbers as they read in a deck:
$7.5B, 55%, 17.5M. Give a deck or an export as the link the platform
returns.
