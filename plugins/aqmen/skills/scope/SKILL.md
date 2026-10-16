---
name: scope
description: 'Open a piece of work on the aqmen platform — the decision, the questions it must answer, the hypotheses, the analyses and data, the deliverable and the workplan — as a project in the client''s workspace, with a short brief in the project''s notes and the full scope and plan as a Doc. Use when work starts — "we need to decide whether to…", "size the market for X", "benchmark the players in Z", "set up the project", "write the brief", "write the plan / the scope of work" — in a session connected to the aqmen MCP, or as step 1 of a use case such as aqmen:cdd. aqmen:research comes next.'
---

# Scope — the project, the brief and the plan

Every later step reads what this step writes: the researchers search for
what the plan names, the critics judge the model against the brief, and
the deliverable answers its questions. A vague scope produces a vague
model. This step writes it down, in the project, where every future
session starts.

It writes two things:

- **The brief** — the project's notes: short, the thread every step reads
  first and logs to (`references/practice.md`, "Where the work lives").
- **The plan** — a Doc, "<project> — scope and plan": the full scope in
  plain words, for the team and the client to read, edit and export to
  Word.

Read `references/practice.md` once per session. Then read the MCP topics
`workflow`, `projects` and `docs`, and `modeling` if the work involves a
model.

## 1. Find the client, then the work

`list_workspaces`. **The workspace is the client**: if this client already
has one, the work goes there. Then `list_projects` in it and
`describe_workspace` (no `projectId`) for the projects and their goals. If
the subject is already covered by a project, ask whether to continue it
before creating anything. Never create first and ask later. A new
engagement for an existing client is a **new project in its workspace**,
never a new workspace; the second project reads what the first loaded.

Writing the client proposal itself is **aqmen:proposal**; this step writes
the working scope inside the project.

## 2. Start from the proposal, if there is one

If the engagement was scoped with **aqmen:proposal** (a `scope.json` or the
proposal `.docx`), or planned with **aqmen:storyline** (a `plan.json`, the
plan `.xlsx`, or a ghost deck already in the project — `list_decks`), read
it first. Its client questions become the questions, its workstreams and
rated hypotheses carry over as written, its analyses and data request
become the plan's analyses and data, its dates become the workplan, and
the ghost deck is the deck **aqmen:deliver** will fill. Fees and
commercials stay in the proposal, never in the plan. Ask only what it
leaves open.

## 3. Ask, and wait

Ask the user, in one message:

- **The decision.** What will be decided with this, and by whom? Examples:
  an investment, a go-to-market priority, a price, a bid.
- **The questions.** The three to six questions the work must answer, in
  the reader's words. "How large is the addressable market for X in
  LATAM, and how fast is it growing?" Push back on questions no data
  could answer.
- **The hypotheses.** Per question, the answer you expect, as an assertion
  a sceptic could dispute, rated confidence × importance (L/M/H). Propose
  them; the user corrects.
- **The precision.** Directional (±30%), or a bottom-up a board or an
  investment committee will test.
- **The frame.** The geography, the horizon and period (usually base year
  ±5, annual), the currency and the unit the answer is read in; what is
  out of scope.
- **The framework,** if one fits: market sizing, company analysis,
  competitive landscape, or a custom model — one per workstream when the
  use case has several (a CDD has up to three). It decides which platform
  topic the model step follows.
- **The deliverable and the deadline.** A deck (exportable to PowerPoint),
  a memo or report as a Doc (exportable to Word), or both; optionally an
  HTML report; the audience and the dates.

Do not proceed until the user has answered. Propose sensible defaults for
what they leave open, and say they are defaults.

## 4. Create the project

- **The workspace.** Reuse the client's (§1), or `create_workspace` only
  for a new client, named for the client ("Atlas Payments"), with
  `annotate_workspace` describing the client — not this piece of work.
- **The project.** `create_project` with a name a partner would recognise
  ("LATAM payments CDD"), the goal as its `description` (one or two
  sentences) and, if there is one, the engagement `code`; status
  `planning`. Its id is the `projectId` on every create from here on.
- **The collections, the whole skeleton.** Read the `collections` topic.
  Group the questions into 2–5 workstreams, named for the topic a partner
  would use ("Market model", "Competitors", "Pricing"; a CDD's are fixed
  by aqmen:cdd). Then `create_collection` with the `projectId`, BEFORE the
  plan doc and the first dataset, in this order (creation order is
  display order):
  1. **Scope** — "The agreed scope and plan, the proposal, kickoff
     material."
  2. **Each workstream** — the `description` says what belongs and which
     questions it answers ("Q1, Q3 — market size and growth by segment").
     A one-question project still gets one.
  3. **Deliverables** — "The findings, the storyline and what the client
     receives."

  The project root stays empty: every later create takes the
  `collectionId` of its home. Topics, not layers: no raw, outputs or
  charts folders. If the user wants the proposal itself in the project,
  bring the `.docx` in (`create_upload_slot`, then `create_doc` with its
  `uploadId`) into Scope.
- **The client's material, stored as sources.** When the client shares a
  data room or a kickoff pack, store each document as its own source
  (`references/practice.md`, "Sources: store, read, cite"; the `datasets`
  topic): `create_upload_slot` → PUT → `create_source` kind `file`, its
  title, publisher (the client), published, `origin` "Client data room,
  <folder or index number>" (or "Kickoff pack, <date>") and a one-line
  description, filed in **Scope** — or in the one workstream it clearly
  serves. `list_sources` first; never store a document twice. Show the
  user the list for correction. Its tables are loaded later by
  aqmen:research, citing these sources.
- **Interviews and meetings.** Planned expert calls and management
  meetings go in the plan's Analyses and data; each becomes a source of
  kind `reference` (interview or meeting: who, about, when, duration, the
  notes in Markdown) once it is held, filed in its workstream.

## 5. Write the plan, as a Doc

`create_doc` in the project (`projectId`, the Scope collection's
`collectionId`), named `scope_and_plan`,
displayName "<project> — scope and plan", from `markdown`, in plain words
— no tool names, no SQL, no table names; it is read by the client:

```markdown
# <Project> — scope and plan

## Context and objectives
<the situation, the decision, who decides, by when, what success looks like>

## Key questions
1. <Q1, in the reader's words>
2. …

## Hypotheses
### Q1 — <short form>
- <assertion a sceptic could dispute> — confidence L/M/H, importance L/M/H — status: to test
### Q2 — …

## Analyses and data
| Analysis | Answers | Data and sources needed | Owner | Status |
| --- | --- | --- | --- | --- |
| <e.g. bottom-up market model by country> | Q1, Q2 | <national statistics on X; analyst reports on Y; client sales data> | <analyst / agent / client> | planned |

## Deliverables
<deck / memo as a Doc / both — audience, form, dates>

## Out of scope
- …

## Workstreams
| Workstream | Answers | What it covers |
| --- | --- | --- |
| <e.g. Market model> | Q1, Q3 | <market size and growth by segment> |

## Workplan
| Week | Dates | Workstream | Work | Touchpoint |
| --- | --- | --- | --- | --- |
```

The workstreams are the workstream collections of §4, by the same names; every
analysis and every workplan row belongs to one. Low confidence × high
importance is where the work starts: say so in the workplan. `annotate_doc` with a one-line description ("The agreed scope
and plan for …"). Give the user the doc's link; offer `export_doc` if they
want to send it as Word.

## 6. Write the brief, in the project's notes

`annotate_project` with `notes` in this shape — short, every later step
reads it first:

```markdown
# <Project name>

## The decision
<one paragraph: what is decided, by whom, by when>

## Questions
- Q1 [open]: <question>
- Q2 [open]: …

## Frame
- Scope: <what is in, what is out>
- Geography: …   Horizon: …   Currency and unit: …
- Precision: directional | board-grade
- Framework: market sizing | company analysis | competitive landscape | custom
  (one line per workstream when there are several)

## Deliverable
<deck | memo (Doc) | both (+ HTML report)>, audience, deadline

## Docs
- Plan: "<project> — scope and plan" (<docId>)
- Findings: _(written by the conclude step)_

## Collections
- Scope (<collectionId>): the plan, the proposal, kickoff material
- <Workstream> (<collectionId>): Q1, Q3 — <what belongs>
- …
- Deliverables (<collectionId>): the findings, the storyline, the client's decks and memos

## Sources register
_(filled by the research step; the documents are the project's sources)_

## Log
- <date> — scoped with <user>
```

Each question is one line in that fixed format: its number, its status in
brackets, a colon, the question — the same questions, in the same order,
as the plan. Later steps find a question by its `Q<n> [` prefix and change
only the status: `[open]`, `[answered]` or `[cannot say: <reason>]`. Keep
the format when the user edits a question. The hypotheses live in the
plan, not here.

## Gate

The user confirms the questions, the hypotheses and the deliverable as
written: show them the plan doc's link and the brief, and ask. Edits go
through `update_doc` on the plan and `edit_notes` (entityType `project`) on
the brief, never a rewrite, and the two stay in step.
`describe_workspace` on the project shows the skeleton — Scope, the
workstreams, Deliverables, in that order — with the plan and any client
material in Scope and the root empty. Then `update_project` to `in_progress` and offer
**aqmen:research**.
