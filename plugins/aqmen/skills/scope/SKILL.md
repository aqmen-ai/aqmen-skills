---
name: scope
description: 'Open a strategic-decision project on the aqmen platform — the decision, the questions it must answer, the precision, the horizon and the deliverable — and record them as the workspace brief. Use when a new piece of work starts — "we need to decide whether to…", "size the market for X", "diligence on Y", "benchmark the players in Z", "start a new project" — in a session connected to the aqmen MCP. Step 1 of the aqmen project flow; aqmen:research comes next.'
---

# Scope — the brief

Every later step reads the brief: the researchers search for what it
names, the critics judge the model against it, and the deliverable
answers its questions. A vague brief produces a vague model. This step
writes it down, in the workspace, where every future session starts.

Read `references/practice.md` once per session. Then read the MCP's
`workflow` topic, and `modeling` if the work involves a model.

## 1. Check for existing work

Call `list_workspaces`, then `describe_workspace` on any that look
related. If the subject is already covered, ask whether to continue that
workspace before creating anything. Never create first and ask later.
Writing the client proposal itself is **aqmen:aqmen-scope**; this step writes
the working brief inside the workspace.

## 2. Start from the proposal, if there is one

If the engagement was scoped with **aqmen:aqmen-scope** (a `scope.json` or
the proposal `.docx`), or planned with **aqmen:dot-dash**, read it first. Its
client questions become the brief's questions, its workstreams and rated
hypotheses carry over as written, its data request becomes the research
agenda, and its dates become the deliverable and deadline. Ask only what it
leaves open.

## 3. Ask, and wait

Ask the user, in one message:

- **The decision.** What will be decided with this, and by whom? Examples:
  an investment, a go-to-market priority, a price, a bid.
- **The questions.** The three to six questions the work must answer, in
  the reader's words. "How large is the addressable market for X in
  LATAM, and how fast is it growing?" Push back on questions no data
  could answer.
- **The precision.** Directional (±30%), or a bottom-up a board or an
  investment committee will test.
- **The frame.** The geography, the horizon and period (usually base year
  ±5, annual), the currency and the unit the answer is read in.
- **The framework,** if one fits: market sizing, company analysis,
  competitive landscape, or a custom model. It decides which guidance
  the model step follows.
- **The deliverable and the deadline.** A report, a deck, a memo, or a
  view the client reads in the workspace.

Do not proceed until the user has answered. Propose sensible defaults for
what they leave open, and say they are defaults.

## 4. Write the brief

- **The workspace.** Reuse the one agreed in §1, or `create_workspace`
  with a name a partner would recognise ("Project Atlas: LATAM payments").
- **The brief, in the workspace docs.** Call `annotate_workspace` with a
  one-line `description` and `docs` in this shape:

```markdown
# <Project name>

## The decision
<one paragraph: what is decided, by whom, by when>

## Questions
- Q1 [open]: <question>
- Q2 [open]: …

## Hypotheses
- <an assertion a sceptic could dispute> — confidence L/M/H, importance L/M/H

## Frame
- Scope: <what is in, what is out>
- Geography: …   Horizon: …   Currency and unit: …
- Precision: directional | board-grade
- Framework: market sizing | company analysis | competitive landscape | custom

## Deliverable
<format, audience, deadline>

## Sources register
_(filled by the research step)_

## Log
- <date> — scoped with <user>
```

  Each question is one line in that fixed format: its number, its status
  in brackets, a colon, the question. Later steps find a question by its
  `Q<n> [` prefix and change only the status: `[open]`,
  `[answered → <insightId>]` or `[cannot say: <reason>]`. Keep the format
  when the user edits a question.
- **A collection for the work.** Read the `collections` topic, then
  `create_collection` named for the workstream ("Market model"). File
  everything the project creates in it as you go.

## Gate

The user confirms the questions and the deliverable as written. Show them
the brief and ask. Edits go through `edit_docs` on the workspace, not a
rewrite. Then offer **aqmen:research**.
