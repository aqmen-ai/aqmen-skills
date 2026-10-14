# The aqmen practice (shared by every step skill)

> Synced verbatim into the use-case and step skills. Read it once per session.

## The platform is the spec

The aqmen MCP's `read_instructions` topics define how the platform works:
every tool's contract, the shapes it accepts, the house look of a deck.
**Read them fresh**, before the step that needs them: `workflow` at the
start of a session, then the topic for the layer you are about to use —
`projects`, `datasets` (also `setup`), `sql`, `charts` (also
`visualization`), `spreadsheets`, `views`, `decks`, `docs`, `collections`,
and before any model `modeling`, then `market-sizing`, `company-analysis`
or `competitive-landscape`. Where a skill and a live topic disagree, **the
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
replacing a dataset, a transformation, a spreadsheet, a chart, a view, a
deck or a doc (`delete_deck`, `delete_doc`); overwriting a model's
formulas; a deck's or a doc's `replaceDocument`; a detach that turns a
live figure into a typed one; dropping a finding the user approved. When
the user's own request is the destructive action, doing it is the
confirmation.

## Agents

Agents buy three things: **parallelism**, **independence** (a fresh context
that never saw your reasoning) and **context isolation** (their reading
stays out of yours). Spawn them with the Agent tool as `aqmen:<name>`.

| Agent | Writes | Spawned by |
| --- | --- | --- |
| `researcher` | nothing — returns load-ready packets | research (parallel, disjoint assignments) |
| `data-loader` | datasets only (+ their annotations, notes, filing) | research, refresh |
| `view-builder` | one view (+ its notes, filing) | conclude (one per question), refresh, demo-prep |
| `model-critic` | nothing | model (gate), challenge |
| `values-critic` | nothing | challenge (before done, before deliver) |
| `deck-critic` | nothing | deliver (gate before hand-over) |
| `skeptic` | nothing | challenge, conclude (CDD by default) |

- **Critics are independent.** Their prompt carries only ids (the
  workspace and the project among them), the scope, the use case's
  standard and the brief **verbatim** — never your design reasoning,
  sourcing notes or what you expect them to find. Never run a critique
  inline. A recheck passes the critic its own findings (by id), still
  nothing about how you fixed them.
- **Writers stay in their scope.** A data loader touches only datasets it
  creates (a replace needs the user's yes, relayed in its prompt); a view
  builder only its one view. Everything else — transformations,
  spreadsheets, charts, decks, docs, the brief — is yours, one call at a
  time, never two in flight.
- **Parallel or serial.** Research and views run in parallel (views are
  independent entities: spawn one builder per view, in the background, and
  keep working). Dataset loading is **serialized** — one loader per
  workspace, unless the datasets are independent and you say so in each
  prompt. Deck and doc writing is never delegated: one writer each.
- **Background agents cannot ask the user.** Give them everything they
  need; if the session would prompt for their writes, run them in the
  foreground instead. Collect every result before the step's gate.
- **Trust, then verify.** Read back what a writer says it made
  (`describe_workspace`, `list_views`), and check the project's Activity
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
  and confidence** in its notes (`datasets`). A figure without a source is
  not data.
- **A workspace figure goes into a deliverable by source, never typed.** A
  chart, a KPI, a table that the workspace computes is a sourced element
  on a slide (`decks`) or a sourced block in a doc (`docs`), so the
  deliverable says when the model moves under it. Words are yours; numbers
  are the workspace's.
- **No SQL in a deliverable.** Docs, decks, reports and anything the client
  reads never show SQL, code or internal table names. Describe the method
  in plain words ("allocated by headcount share") and cite the sources.
- **What you need to believe stays live.** The load-bearing assumptions —
  implied metric, reference, verdict, break-even — and the sanity checks
  are a `Believe` block in the model (`modeling`), never a typed list.

## Where the work lives: the project, its brief, its plan

The **workspace is the client** — its data, storage and access. A
**project** is one piece of work inside it; collections are topic folders
inside a project (`projects`). A new engagement for an existing client is
a new project in that client's workspace, never a new workspace. Every
create takes `projectId` (omittable only when the workspace has exactly
one project). Orientation is `list_projects`, then `describe_workspace`
with the `projectId`.

`aqmen:scope` writes two things every later step reads first:

- **The brief** — the project's notes (`annotate_project`): the decision,
  the questions as `Q<n> [status]: …` lines, the frame, the deliverable,
  the plan and findings docs, the sources register and the Log.
  `describe_workspace` with the project returns it. Every step appends one
  dated line to the Log when it ends. Change a question's status with
  `edit_notes` (entityType `project`) find-and-replace on its exact
  `Q<n> [` text, never by rewriting the list. Statuses: `[open]`,
  `[answered]`, `[cannot say: <reason>]`.
- **The plan** — a doc, "<project> — scope and plan" (`docs`): context and
  objectives, the questions, the hypotheses per question, the analyses and
  the data each needs, the deliverables, out of scope, the workplan. Steps
  that settle something keep it current with `update_doc`: a question
  answered, a hypothesis supported or refuted with its figure as a sourced
  block.

**Conclusions live in the findings doc**, "<project> — findings", which
`aqmen:conclude` writes: one section per question, the answer as a
headline sentence, every figure a sourced block. The deck and the memo are
written from it.

## Gates and honest completion

A step is done only when its gate holds. Do not call work complete while
a driver rests on an estimate the user has not seen, a check fails, a
connection, a deck figure or a doc block is stale or broken, or lint is
left on a sheet or a slide. State gaps; never fill them to look finished.

## Speaking to the user

Plain language, the reader's words, not the tools': "loaded the Eurostat
enterprise statistics, cited" rather than a tool name and an identifier.
Lead with what changed and what is left. Numbers as they read in a deck:
$7.5B, 55%, 17.5M. Give a deck, a doc or an export as the link the
platform returns.
